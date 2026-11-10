"""SVT, chapitre 3 du thème 1.A : « L'évolution du génome au sein des populations » — la vidéo du chapitre.

Même chaîne que les vidéos de physique-chimie (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les
mots) ; moteur svt/serie/moteur.js (type mental = carte mentale du thème 1.A) ; illustrations propres au chapitre dans
svt/serie/illu-svt-ch3.js (melange, population, croisement, barres, derive9, buri, fondateur, beringie, amish, tri,
reseau, denisova, speciation).
Contenu : les pages t3 et t3b du site (svt/index.html), rien au-delà. Ce qui dépasse le programme est dit « hors
programme ». Les courbes des scénarios et l'histogramme de Buri sont des SIMULATIONS (graines fixes ci-dessous),
annoncées comme telles. L'explication du groupe O est présentée comme une hypothèse. Aucune référence à un enseignant
ni à un document scolaire : que du contenu (consigne du 10/11/2026). Les trois exercices sont inventés pour la vidéo (valeurs recalculées en commentaire).
Usage : python3 outils/serie-philo/verifier.py svt_ch3 ; puis generer.py svt_ch3 ; chevauchements.py svt-ch3 ; fermer.py svt_ch3.
"""
import random

SITE = "svt"
CODE = "svt-ch3"
NOTION = "L'évolution du génome au sein des populations"
NUM = 3
RYTHME = "vivant"
TITRE = "L'évolution du génome au sein des populations"
SUIVANT = "Chapitre 4 · La diversité non génétique du vivant"
PRONONCIATION = {"p": "pé", "q": "ku", "m": "ème", "Hardy": "Hardi", "Weinberg": "Vaïnbergue", "Buri": "Bouri",
                 "bw75": "bé double-vé soixante-quinze", "bw": "bé double-vé", "AceR": "assé erre", "AceS": "assé esse", "Culex": "Culèxe",
                 "pipiens": "pipiènce", "Ellis-van": "Élisse-vane", "Creveld": "Crévelde", "HLA": "ache èl a",
                 "Kell": "Kèl", "Doolittle": "Doulitel", "Denisova": "Dénissova", "Mezmaiskaya": "Mezmaïskaïa",
                 "Vindija": "Vindiya", "Han": "Hane", "lugubris": "lugubrisse", "paralugubris": "paralugubrisse",
                 "Mendel": "Mendèle", "Huttérites": "Hutérites", "Linné": "Liné"}


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
    """Valeurs sélectives A//A = 1, A//B = 0,8, B//B = 0,8 (scénario 4), population de n individus."""
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
         (1990, .52), (1992, .57), (1994, .6), (1996, .61), (1998, .6), (2000, .6)]   # allure des données publiées (population 1)


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
        "{ouv_m}Voici la carte mentale du thème un, partie A : génétique et évolution. Quatre chapitres.",
        "Le premier : comment chaque individu reçoit un génotype unique. Le deuxième : comment les génomes se complexifient.",
        "{ouv_m.1}Ici, on change d'échelle. Oublie l'individu, oublie la cellule. "
        "On regarde une population entière. Et une question : que deviennent ses allèles, génération après génération ?",
        ("P", 0.6),
        "{ouv_m.2}D'abord, un modèle : l'équilibre de Hardy-Weinberg. Une population idéale, où rien ne bouge.",
        "{ouv_m.3}Ensuite, tout ce qui fait bouger les choses : la dérive, l'effet fondateur, la sélection. "
        "Avec des cas réels : les drosophiles de Buri, les Amish, le groupe O des Amérindiens, les moustiques du Languedoc.",
        "{ouv_m.4}Et pour finir, une question qui a l'air simple. Elle ne l'est pas. Qu'est-ce qu'une espèce ?",
        "{ouv_m.5}Les calculs de Hardy-Weinberg tombent souvent au bac. On les fait ensemble, pas à pas. Puis tu les fais seul, sur trois exercices.",
        "{-ouv_m}{titre}",
        ("P", 3.2),
    ], vis={
        "ouv_m": dict(type="mental", vers=["t1a", "c3", "c3a", "c3b", "c3c", "c3"], pousse=True),
        "titre": dict(type="titre", sur="SVT · Thème 1 · Chapitre 3", t="L'évolution du génome au sein des populations",
                      sous="Tout le chapitre, de zéro au bac"),
    }),

    # ================================================================ A. Hardy-Weinberg : l'énigme
    dict(id="enigme", chap="L'énigme de la diversité", fond="foret", humeur="mystere",
         retenir="L'hérédité par mélange est fausse : les allèles se transmettent intacts. D'où la persistance des variants.",
         beats=[
        "{m_a}{m_a.1}Première branche : l'équilibre de Hardy-Weinberg. Pourquoi a-t-on eu besoin d'un tel modèle ? Pour le comprendre, remontons vers mille huit cents.",
        "{-m_a}{mel}À l'époque, personne ne connaît la méiose. Et l'idée admise, c'est l'{!hérédité par mélange}. "
        "Le descendant serait un mélange de ses deux parents. "
        "{mel.1}Exemple : une souris noire, une souris blanche. Leur petit ? Une souris grise.",
        "{mel.2}Mais alors, chaque variant se diluerait un peu plus à chaque génération. Gris, puis gris, puis gris. "
        "Au bout de quelques générations, tout le monde se ressemblerait.",
        "Or c'est l'inverse qu'on observe. Regarde une population humaine : une diversité immense, qui se maintient génération après génération. "
        "Voilà l'énigme : pourquoi les variants persistent-ils ?",
        "{mel.3}La réponse, tu l'as vue au chapitre un. Les allèles se transmettent intacts, par la méiose et la fécondation. "
        "Un hétérozygote peut avoir un phénotype intermédiaire. Mais ses deux allèles, eux, ne se mélangent pas. "
        "{mel.4}Ils peuvent se séparer à nouveau dans ses gamètes. Mendel l'avait montré dès les années mille huit cent soixante.",
        "{-mel}{hw}Reste une question : que font les fréquences des allèles à l'échelle d'une population entière ? "
        "En mille neuf cent huit, deux hommes répondent, chacun de son côté. Le mathématicien britannique Godfrey Harold Hardy. "
        "Et le médecin allemand Wilhelm Weinberg.",
        ("P", 0.7),
        "{-hw}{pb}Voici donc la question de tout le chapitre. {pb.1}Comment les fréquences des allèles évoluent-elles dans une population, "
        "au fil des générations ? Et pourquoi s'écartent-elles de l'équilibre prévu par Hardy et Weinberg ?",
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
        "{defs}Trois définitions. À savoir par cœur. {defs.1}Une population : des individus de la même espèce, "
        "dans une même zone, qui peuvent se reproduire entre eux et avoir une descendance fertile.",
        ("{defs.2}Son patrimoine génétique : tous les allèles présents dans cette population. "
         "{defs.3}Et la fréquence d'un allèle : sa proportion parmi tous les exemplaires du gène.", {"rate": "-4%"}),
        "{-defs}{pop}{pop.1}Comptons ensemble. Vingt-cinq individus, un gène, deux allèles : A et m. "
        "Chaque individu est diploïde. Il porte donc deux exemplaires du gène : une moitié de disque chacun.",
        "{pop.2}Les neuf homozygotes A A apportent deux allèles A chacun. Ça fait dix-huit. "
        "{pop.3}Les douze hétérozygotes A m en apportent un. Douze de plus. Les m m ? Aucun.",
        "{pop.4}Vingt-cinq individus, deux exemplaires chacun : cinquante en tout. Trente allèles A sur cinquante. "
        "La fréquence de A vaut zéro virgule six. Et celle de m ? Un moins zéro virgule six : zéro virgule quatre.",
        "{-pop}{f_fa}On généralise. {f_fa.1}N individus, c'est deux N exemplaires du gène. "
        "{f_fa.2}La fréquence de A : deux fois le nombre de A A, plus le nombre de A m, le tout sur deux N. "
        "{f_fa.3}Et la fréquence de m : un moins celle de A.",
        ("P", 0.6),
        "{-f_fa}{pa_f}À toi. Mille individus : trois cent soixante A A, quatre cent quatre-vingts A m, cent soixante m m. "
        "Calcule la fréquence de A. Puis les trois fréquences génotypiques.",
        "{pa_f.stop}{-pa_f}{f_ex}Solution. {f_ex.1}Mille individus : deux mille exemplaires du gène. "
        "{f_ex.2}Les allèles A : deux fois trois cent soixante, plus quatre cent quatre-vingts. Mille deux cents. "
        "{f_ex.3}Mille deux cents sur deux mille : la fréquence de A vaut zéro virgule six. Celle de m, zéro virgule quatre.",
        "{f_ex.4}Les fréquences génotypiques, maintenant. C'est la part de chaque génotype : "
        "zéro virgule trente-six pour A A, zéro virgule quarante-huit pour A m, zéro virgule seize pour m m. "
        "Attention à ne jamais confondre : la fréquence d'un allèle, et celle d'un génotype.",
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
        "f_ex": dict(type="formule", titre="Solution · 360 A//A, 480 A//m, 160 m//m", x=150, y=120, w=980, lignes=[
            dict(f="2N = 2 × 1 000 = 2 000 exemplaires du gène"),
            dict(f="allèles A : 2 × 360 + 480 = 1 200"),
            dict(f="f(A) = " + fr("1 200", "2 000") + " = 0,6  ·  f(m) = 0,4", cadre=True),
            dict(f="génotypes : f(A//A) = 0,36 · f(A//m) = 0,48 · f(m//m) = 0,16", taille=32)]),
    }),

    # ================================================================ la loi de Hardy-Weinberg
    dict(id="loi", chap="La loi de Hardy-Weinberg", fond="foret", humeur="lumiere",
         retenir="p + q = 1. À l'équilibre : f(A//A) = p², f(A//m) = 2pq, f(m//m) = q², et p² + 2pq + q² = 1.",
         beats=[
        "{f_pq}{f_pq.1}Deux lettres à retenir. p, la fréquence de l'allèle A. q, celle de l'allèle m. "
        "{f_pq.2}Il n'y a que deux allèles. Donc p plus q égale un.",
        "{-f_pq}{cr}{cr.1}Maintenant, laissons les gamètes se rencontrer au hasard. Un gamète porte A avec la probabilité p. "
        "Et m avec la probabilité q. Le tableau de croisement devient un carré de côté un.",
        "{cr.2}A rencontre A : p fois p. p au carré. Voilà la fréquence des homozygotes A A.",
        "{cr.3}A rencontre m : p fois q. Mais regarde bien : il y a deux cases ! A peut venir du père, ou de la mère. "
        "Les hétérozygotes valent donc deux p q.",
        "{cr.4}Et m rencontre m : q au carré. Les homozygotes m m.",
        "{cr.5}Les quatre cases remplissent tout le carré. p au carré, plus deux p q, plus q au carré : un. "
        "Normal : c'est p plus q, au carré. Un au carré, un.",
        "{-cr}{f_hw}Et voilà la loi de Hardy-Weinberg. {f_hw.1}{f_hw.2}{f_hw.3}",
        ("Les A A : p au carré. Les A m : deux p q. Les m m : q au carré. "
         "{f_hw.4}Et le tout, p au carré plus deux p q plus q au carré, égale un.", {"rate": "-4%"}),
        ("P", 0.8),
        "{-f_hw}{piege_hw}Deux pièges. {piege_hw.1}On écrit souvent « p deux plus deux p q plus q deux », et on oublie le « égale un ». "
        "Écris-le toujours. Et l'hétérozygote compte double : avec p q au lieu de deux p q, la somme ne fait plus un.",
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
        "{demo}{demo.1}Et à la génération suivante ? Que devient la fréquence de A ? Faisons le calcul. "
        "Les allèles A des enfants viennent de deux sources. Tous ceux des homozygotes A A. "
        "Et la moitié de ceux des hétérozygotes. {demo.2}La nouvelle fréquence de A vaut donc p au carré, plus la moitié de deux p q. Soit p au carré plus p q.",
        "{demo.3}On met p en facteur : p fois, p plus q. {demo.4}Or p plus q vaut un. Il reste p. La même fréquence qu'au départ !",
        "{-demo}{gr_eq}{gr_eq.1}Sur un graphique, ça donne une droite bien horizontale. Génération après génération. "
        "{gr_eq.2}{gr_eq.3}{gr_eq.4}Et les génotypes ? Ils se calculent à partir de p et q. Donc eux non plus ne bougent pas : "
        "trente-six, quarante-huit et seize pour cent. Pour toujours.",
        ("P", 0.7),
        "{-gr_eq}{mot}La conclusion, à retenir mot pour mot. {mot.1}Il n'y a donc pas d'évolution dans ce cadre de modélisation théorique.",
        "Et voilà la réponse à l'énigme du début. La reproduction sexuée, à elle seule, ne fait disparaître aucun allèle. "
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
                          dict(type="courbe", pts=[[0, .36], [10, .36]], c="or", lbl="A//A : p² = 0,36", lp=[2.2, .30]),
                          dict(type="courbe", pts=[[0, .16], [10, .16]], c="ca", lbl="m//m : q² = 0,16", lp=[6.2, .1])]),
        "mot": dict(type="def", terme="À retenir mot pour mot", cles=["pas", "d'évolution"],
                    t="Il n'y a donc pas d'évolution dans ce cadre de modélisation théorique.",
                    etape="La reproduction sexuée, à elle seule, ne fait disparaître aucun allèle : les variants persistent.",
                    x=170, y=210, w=940),
    }),

    # ================================================================ vérifier l'équilibre
    dict(id="verifier", chap="Vérifier qu'une population est à l'équilibre", fond="foret", humeur="lumiere",
         retenir="Méthode : p et q d'après les effectifs observés ; effectifs attendus p²N, 2pqN, q²N ; comparer.",
         beats=[
        "{meth}La méthode qui tombe au bac tient en trois étapes. {meth.1}Un : calculer p et q, à partir des effectifs observés. "
        "{meth.2}Deux : calculer les effectifs attendus à l'équilibre. p au carré fois N, deux p q fois N, q au carré fois N. "
        "{meth.3}Trois : comparer. Observé contre attendu.",
        "{-meth}{b1}{b1.1}On reprend notre population : trois cent soixante, quatre cent quatre-vingts, cent soixante. "
        "Ce sont les effectifs observés. {b1.2}Avec p égal zéro virgule six, on attend : zéro virgule trente-six fois mille, trois cent soixante. "
        "Zéro virgule quarante-huit fois mille, quatre cent quatre-vingts. Et cent soixante. "
        "{b1.3}Les barres se superposent. La population est à l'équilibre.",
        "{-b1}{b2}{b2.1}Une autre population, maintenant. Cinq cents A A, deux cents A m, trois cents m m. "
        "Calcule p : mille plus deux cents, sur deux mille. Encore zéro virgule six ! La même fréquence allélique.",
        "{b2.2}On attend donc les mêmes effectifs. Trois cent soixante, quatre cent quatre-vingts, cent soixante. "
        "{b2.3}Mais regarde : beaucoup trop d'homozygotes. Pas assez d'hétérozygotes. Cette population s'écarte de l'équilibre.",
        "Quelque chose cloche dans les conditions du modèle. Par exemple, des accouplements entre individus apparentés. "
        "Ils fabriquent des homozygotes.",
        ("P", 0.6),
        "{-b2}{lecon}La leçon ? {lecon.1}Une fréquence allélique ne suffit pas. Deux populations peuvent avoir le même p. "
        "Ce qui révèle l'écart, c'est la comparaison des génotypes : observés contre attendus.",
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
        "{cond}Le modèle promet des fréquences stables. {cond.1}Mais à une condition : une population idéale. "
        "Une taille infinie. En pratique, très grande. "
        "{cond.2}Une espèce diploïde, à reproduction sexuée. "
        "{cond.3}La panmixie : des croisements au hasard. "
        "{cond.4}Une population isolée. Pas de migration, pas de flux de gènes. "
        "{cond.5}Pas de sélection naturelle. {cond.6}Pas de mutation. "
        "{cond.7}Et des générations qui ne se chevauchent pas.",
        "{-cond}{panm}Un mot savant mérite qu'on s'y arrête : {panm.1}la panmixie. Trois idées dedans. "
        "Des gamètes équiprobables : c'est la pangamie. Des accouplements au hasard, sans préférence. "
        "Et des allèles répartis au hasard dans les gamètes, à la méiose.",
        ("P", 0.6),
        "{-panm}{ref}{ref.1}Tu vois le problème ? Aucune population réelle ne coche toutes ces cases. "
        "Une population réelle à l'équilibre, c'est presque impossible.",
        "{ref.2}Alors, à quoi bon ce modèle ? C'est une {!référence}. Si une population s'en écarte, c'est qu'une force agit sur elle. "
        "Et l'écart permet de la traquer. Comme un thermomètre : ce qui compte, ce n'est pas le trente-sept degrés. C'est la fièvre.",
        "{-ref}",
    ], vis={
        "cond": dict(type="liste", titre="Les conditions du modèle", items=[
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
        "{cau}Retournons la question. Dans la réalité, qu'est-ce qui peut faire dévier une population ? "
        "{cau.1}Simple : chaque condition non respectée devient une cause.",
        "Pas de mutation ? En réalité, des mutations apparaissent. Elles créent de nouveaux allèles. "
        "C'est la source de la variabilité, vue en Première.",
        "{cau.2}Population isolée ? En réalité, des individus migrent. De nouvelles variations arrivent. Ou un groupe part et s'isole. "
        "Une barrière naturelle peut aussi couper la population en deux.",
        "{cau.3}Pas de sélection ? Un changement de climat, un nouvel environnement, et les chances de survie changent. "
        "Une nouvelle espèce qui convoite les mêmes ressources ? Même effet.",
        "{cau.4}Accouplements au hasard ? Il existe des préférences sexuelles. La reproduction n'est pas un tirage au sort.",
        "{cau.5}Population infinie ? Elle peut être minuscule. Et là, le hasard de la reproduction pèse très lourd.",
        ("P", 0.6),
        "{-cau}{fe}Ces causes d'écart ont un nom. {fe.1}Les {!forces évolutives}. C'est la deuxième branche de la carte. "
        "Mais d'abord, à toi de jouer : deux exercices sur Hardy-Weinberg.",
        "{-fe}",
    ], vis={
        "cau": dict(type="liste", titre="Condition non respectée → ce qui se passe", items=[
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
        "{ex1}Premier exercice. Deux cent cinquante papillons : cent soixante A A, quatre-vingts A m, et dix m m. "
        "Trois questions. Les fréquences des deux allèles. Les effectifs attendus à l'équilibre. Et la conclusion.",
        "{-ex1}{pa1}Prends une feuille. Mets sur pause. Et déroule la méthode en trois étapes.",
        "{pa1.stop}{-pa1}{ex1c}{ex1c.q1}Solution. {s11}{s11.1}Deux cent cinquante individus : cinq cents exemplaires du gène. "
        "{s11.2}Les allèles A : deux fois cent soixante, plus quatre-vingts. Quatre cents. "
        "{s11.3}p vaut quatre cents sur cinq cents : zéro virgule huit. Et q, zéro virgule deux.",
        "{-s11}{ex1c.q2}{s12}{s12.1}Les effectifs attendus. A A : p au carré, zéro virgule soixante-quatre, fois deux cent cinquante. Cent soixante. "
        "{s12.2}A m : deux p q, zéro virgule trente-deux, fois deux cent cinquante. Quatre-vingts. "
        "{s12.3}m m : q au carré, zéro virgule zéro quatre, fois deux cent cinquante. Dix. "
        "{s12.4}Petite vérification : zéro virgule soixante-quatre, plus zéro virgule trente-deux, plus zéro virgule zéro quatre. Un. Parfait.",
        "{-s12}{ex1c.q3}{s13}{s13.1}La conclusion. Observés : cent soixante, quatre-vingts, dix. Attendus : exactement les mêmes. "
        "{s13.2}La population est à l'équilibre de Hardy-Weinberg. Ses fréquences devraient rester stables, tant que les conditions du modèle tiennent.",
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
        "{ex2}Deuxième exercice. Plus corsé. Quatre cents escargots : cent soixante A A, quatre-vingts A m, et cent soixante m m. "
        "On demande p et q. Les effectifs attendus. Si la population est à l'équilibre. "
        "Et pour finir : quelle condition du modèle n'est sans doute pas respectée, et pourquoi ?",
        "{-ex2}{pa2}Cette dernière question, il faut la raisonner, pas seulement la calculer. Pause !",
        "{pa2.stop}{-pa2}{ex2c}{ex2c.q1}Solution. {s21}{s21.1}Huit cents exemplaires du gène. "
        "{s21.2}Les allèles A : trois cent vingt plus quatre-vingts. Quatre cents. {s21.3}p vaut zéro virgule cinq. Et q aussi.",
        "{-s21}{ex2c.q2}{s22}{s22.1}Les attendus. p au carré, zéro virgule vingt-cinq, fois quatre cents : cent A A. "
        "{s22.2}Deux p q, zéro virgule cinq, fois quatre cents : deux cents A m. {s22.3}Et cent m m.",
        "{-s22}{ex2c.q3}{b3}{b3.1}{b3.2}{b3.3}On compare. On attendait deux cents hétérozygotes. On n'en voit que quatre-vingts ! "
        "Et soixante homozygotes de trop, de chaque côté. Pas d'équilibre.",
        "{-b3}{ex2c.q4}{s24}{s24.1}Alors, quelle condition ? Trop d'homozygotes, pas assez d'hétérozygotes : c'est la signature d'une reproduction non aléatoire. "
        "{s24.2}Des accouplements entre individus semblables, ou apparentés. La panmixie n'est pas respectée. "
        "{s24.3}Et attention à la rédaction. On propose une hypothèse. Le calcul montre l'écart ; à lui seul, il n'en prouve pas la cause.",
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
         retenir="Modélisation : un logiciel fait se reproduire une population ; on change un paramètre à la fois et on suit les fréquences.",
         beats=[
        "{m_b}{m_b.1}Deuxième branche : les écarts à l'équilibre. La dérive génétique, l'effet fondateur, la sélection naturelle. "
        "Sans oublier deux autres forces : les mutations et les migrations.",
        "{-m_b}{q2}Toute cette partie répond à une question. {q2.1}Comment les forces évolutives font-elles s'écarter les fréquences alléliques "
        "de l'équilibre de Hardy-Weinberg ?",
        "{-q2}{act}Pour le voir, on va simuler. {act.1}Un logiciel crée une population, et la fait se reproduire, génération après génération. "
        "{act.2}On ne touche qu'à un réglage à la fois : la taille, les mutations, le hasard des accouplements, "
        "ou l'avantage d'un caractère. {act.3}Et on suit les fréquences sur une dizaine de générations. Les écarts, ça se voit dans la durée.",
        "{-act}{gr_s1}{gr_s1.1}Toutes les courbes qui suivent sont simulées. On lance le modèle, et on regarde. "
        "Scénario un, le témoin. Mille individus, deux allèles à cinquante pour cent, pas de mutation, rencontres au hasard. "
        "La courbe tremble à peine autour de zéro virgule cinq. Aucun allèle ne disparaît.",
        "Une grande population, c'est presque la population idéale du modèle. Les fréquences tiennent. Garde ce témoin en tête.",
        "{-gr_s1}",
    ], vis={
        "m_b": dict(type="mental", vers=["c3", "c3b"]),
        "q2": dict(type="def", terme="La question de la partie II", cles=["écart"],
                   t="Comment les forces évolutives sont-elles à l'origine d'un écart des fréquences alléliques par rapport à l'équilibre théorique de Hardy-Weinberg ?",
                   x=170, y=200, w=940),
        "act": dict(type="liste", titre="La modélisation · le principe", items=[
            "Un logiciel simule une population qui se reproduit, génération après génération",
            "On change un seul paramètre : taille, mutations, accouplements, avantage d'un caractère",
            "On suit les fréquences sur une dizaine de générations"], marques=["1", "2", "3"], x=150, y=170, w=980),
        "gr_s1": gr_freq("Scénario 1 · témoin, 1 000 individus (simulé)", [(S1, "sa", "1 000 individus", [5.2, .62])]),
    }),

    # ================================================================ la dérive génétique
    dict(id="derive", chap="La dérive génétique", fond="cellule", humeur="tension",
         retenir="Dérive génétique : évolution aléatoire des fréquences, due au hasard de la reproduction, d'autant plus forte que la population est petite.",
         beats=[
        "{gr_s2}Scénario deux. Cette fois, neuf individus seulement. Deux allèles à cinquante pour cent, onze générations. {gr_s2.1}Et on lance la simulation deux fois. "
        "Premier lancement : la fréquence fait des bonds… et l'allèle finit fixé, à un. L'autre a disparu.",
        "{gr_s2.2}Deuxième lancement. Mêmes conditions, exactement. Et cette fois, l'allèle disparaît ! "
        "Même départ, deux destins opposés. Personne n'a favorisé un allèle. C'est le hasard.",
        ("P", 0.6),
        "{-gr_s2}{d_der}Ce hasard porte un nom : la {!dérive génétique}. {d_der.1}Une évolution aléatoire, due au hasard de la reproduction et de la descendance. "
        "Et plus la population est petite, plus elle frappe fort.",
        "{-d_der}{d9}{d9.1}Regarde ce qui se passe, génération par génération. Neuf individus au départ. "
        "{d9.2}Seuls cinq se reproduisent. Et pas autant les uns que les autres : deux descendants, un, un, un, et trois. "
        "Quatre individus n'ont aucun descendant. Leurs allèles sont perdus.",
        "{d9.3}Deuxième génération : huit individus. Et les couleurs n'ont plus les mêmes proportions. "
        "{d9.4}Troisième génération : dix. {d9.5}Et dans dix générations ? Impossible de prévoir la composition.",
        "{-d9}{expl}Mais pourquoi le hasard pèse-t-il autant ? "
        "{expl.1}Dans une petite population, les allèles n'ont pas tous la même chance d'être transmis. "
        "{expl.2}Pour transmettre à coup sûr tous ses allèles, un individu devrait avoir une infinité de descendants. "
        "{expl.3}Donc, statistiquement, certains allèles ne passent à aucun enfant. C'est inévitable. "
        "{expl.4}Les effectifs des allèles font le yoyo : certains se retrouvent sur-représentés, d'autres sous-représentés.",
        "{-expl}{fix}Deux idées à retenir. {fix.1}Plus la population est petite, plus la dérive est forte. "
        "{fix.2}Et elle peut aller jusqu'au bout : la {!fixation} d'un allèle, à la fréquence un, et la disparition de l'autre. "
        "{fix.3}Conséquence : la dérive peut appauvrir la diversité génétique, et même condamner une population. "
        "Mais elle peut aussi aider à faire naître une nouvelle espèce. On y reviendra.",
        "{-fix}",
    ], vis={
        "gr_s2": gr_freq("Scénario 2 · dérive, 9 individus (simulé)",
                         [(S2a, "sa", "lancement 1 : fixé", [7.2, .93]), (S2b, "or", "lancement 2 : perdu", [7.2, .1])], gens=11),
        "d_der": dict(type="def", terme="Dérive génétique", cles=["aléatoire", "petite"],
                      t="Un phénomène d'évolution aléatoire, dû au hasard de la reproduction et de la descendance. Elle est beaucoup plus forte sur une petite population.",
                      x=170, y=200, w=940),
        "d9": dict(type="illu", nom="derive9", x=110, y=96, w=1060, h=560),
        "expl": dict(type="liste", titre="L'explication", items=[
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
        "{tab_dro}Passons au réel. Une expérience célèbre, sur la drosophile : la petite mouche du vinaigre des labos de génétique. "
        "{buri_p}En mille neuf cent cinquante-six, Peter Buri lance cent sept populations. Toutes selon le même protocole. "
        "{buri_p.1}Au départ, seize mouches par population. Toutes hétérozygotes pour la mutation brown eye : bw75 sur bw. "
        "Huit mâles, huit femelles. {buri_p.2}Partout, la fréquence de bw75 vaut donc zéro virgule cinq.",
        "{buri_p.3}À chaque génération, on tire au hasard huit mâles et huit femelles parmi les descendants. Ce sont eux qui feront la suite. "
        "{buri_p.4}Et ça dure dix-neuf générations.",
        "{-buri_p}{-tab_dro}{hb}Voici le résultat. L'histogramme range les populations selon leur fréquence de bw75. "
        "Il est reproduit ici par simulation, avec le protocole de Buri. Les chiffres ne sont pas les siens, mais le phénomène est le même. "
        "{hb.1}Au départ, les cent sept populations sont toutes au même endroit : zéro virgule cinq.",
        "Puis, génération après génération, elles s'étalent. Certaines montent, d'autres descendent. "
        "Et bientôt, des populations touchent les bords : zéro, ou un. Là, elles ne bougent plus. Il ne reste qu'un seul allèle.",
        "{hb.2}À la fin, l'histogramme dessine un U. {hb.3}Beaucoup de populations ont fixé bw75. Beaucoup d'autres l'ont perdu. "
        "À peu près autant d'un côté que de l'autre.",
        ("P", 0.6),
        "{-hb}{exb}Comment l'expliquer ? {exb.1}Les cent sept populations ont été traitées exactement de la même façon. "
        "{exb.2}La couleur des yeux ne change rien à la survie en élevage. Donc pas de sélection. "
        "{exb.3}Ce qui a fait diverger les fréquences, c'est le seul hasard du tirage, dans de toutes petites populations de seize. La dérive génétique. "
        "{exb.4}Imprévisible pour une population donnée. Mais elle mène souvent à la fixation, ou à la perte, d'un allèle.",
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
        "{gr_s3}Retour à la simulation. Scénario trois : toujours neuf individus, {gr_s3.1}mais un départ déséquilibré. Vingt pour cent seulement pour le premier allèle. "
        "Le plus souvent, cet allèle rare disparaît en quelques générations. {gr_s3.2}Mais parfois, par hasard, il grimpe.",
        "{-gr_s3}{d_fond}Ce scénario imite l'{!effet fondateur}. {d_fond.1}Un petit groupe quitte la population de départ. Lors d'une migration, par exemple. "
        "Il n'emporte qu'un échantillon des allèles, tiré au hasard. Un échantillon non représentatif. "
        "{d_fond.2}Ses fréquences peuvent donc être très différentes.",
        "{-d_fond}{ifo}Regarde bien. {ifo.1}Une grande population, trois allèles. "
        "{ifo.2}Huit individus partent coloniser un nouveau milieu. Et par hasard, aucun ne porte l'allèle violet.",
        "{ifo.3}Compare : la colonie n'a plus du tout la composition de départ. Un allèle a disparu d'un coup. Sans aucune sélection. "
        "{ifo.4}Puis la colonie grandit. Mais elle reste petite. Et la dérive continue son travail.",
        "{-ifo}{cause}Pourquoi un tel écart ? {cause.1}Parce que les fondateurs ne sont qu'un échantillon non représentatif des allèles de départ. "
        "Ils n'y sont pas dans les bonnes proportions. {cause.2}Et souvent, s'y ajoute une reproduction non aléatoire. "
        "Dans une petite communauté isolée, on se reproduit entre soi.",
        "{-cause}",
    ], vis={
        "gr_s3": gr_freq("Scénario 3 · fondateur, 20 % au départ (simulé)",
                         [(S3a, "or", "lancement 1 : perdu", [5.5, .1]), (S3b, "sa", "lancement 2 : par hasard, il monte", [6.3, 1.0])], gens=11),
        "d_fond": dict(type="def", terme="Effet fondateur", cles=["échantillon", "non", "représentatif"],
                       t="Une petite sous-population se sépare de la population initiale. Elle n'emporte qu'un échantillon non représentatif, tiré au hasard, des allèles de la population mère.",
                       etape="Ses fréquences peuvent être fort différentes ; l'écart est d'autant plus grand qu'elle est petite, et la dérive s'y ajoute.",
                       x=170, y=170, w=940),
        "ifo": dict(type="illu", nom="fondateur", x=90, y=96, w=1100, h=560),
        "cause": dict(type="liste", titre="La cause de l'écart", items=[
            "Un échantillon non représentatif des allèles de départ",
            "Une reproduction non aléatoire : une petite communauté isolée se reproduit en son sein"], marques=["1", "2"], x=150, y=190, w=980),
    }),

    # ================================================================ Amish et Huttérites
    dict(id="amish", chap="Les Amish et les Huttérites", fond="cellule", humeur="calme",
         retenir="Amish : syndrome d'Ellis-van Creveld, q = 0,07, toutes les familles descendent d'un même couple d'immigrants. C'est l'effet fondateur.",
         beats=[
        "{tab_am}Chez l'humain, maintenant. Les Amish de Pennsylvanie. Une communauté d'origine européenne, installée en Amérique du Nord. Elle vit à l'écart, et on s'y marie entre soi. "
        "{evc}Et chez eux, un syndrome rare ailleurs est fréquent. {evc.1}Le syndrome d'Ellis-van Creveld : une forme de nanisme, avec des doigts surnuméraires.",
        "{evc.2}L'allèle en cause atteint q égal zéro virgule zéro sept. Dans le reste du monde, la maladie est exceptionnelle. "
        "{evc.3}Mieux : toutes les familles amish étudiées portent la même mutation. Et toutes descendent d'un même couple d'immigrants.",
        "{-evc}{-tab_am}{ham}{ham.1}Allons plus loin, avec un tableau publié par McLellan et ses collègues en mille neuf cent quatre-vingt-sept. "
        "Trois groupes : les Européens et Américains, les Huttérites, une autre communauté d'origine européenne, et les Amish. "
        "Groupe sanguin A : vingt-cinq à trente-deux pour cent en Europe. Trente-cinq chez les Huttérites. Et soixante-six chez les Amish !",
        "{ham.2}L'allèle H L A A onze, un marqueur tissulaire : quatre virgule cinq à sept virgule quatre pour cent en Europe. Zéro chez les Huttérites : il a disparu. "
        "Quatorze chez les Amish. {ham.3}Et le groupe Kell : trois à cinq pour cent en Europe. Quatorze chez les Huttérites. Zéro virgule deux chez les Amish.",
        "{-ham}{exa}Que voit-on ? {exa.1}Les deux communautés s'écartent nettement de l'Europe d'où elles viennent. Et elles ne se ressemblent pas entre elles. "
        "Ici, un allèle a disparu. Là, il est bien plus fréquent qu'ailleurs.",
        "{exa.2}L'explication : chaque communauté est née d'une poignée d'immigrants. Ils n'emportaient qu'un échantillon non représentatif des allèles européens. "
        "L'effet fondateur. {exa.3}Ensuite, ces communautés vivent isolées, et on s'y marie entre soi : une reproduction non aléatoire. "
        "Et leur petite taille renforce la dérive. Trois mécanismes, qui s'additionnent.",
        "{-exa}",
    ], vis={
        "tab_am": dict(type="tableau", img="ch3-amish", fond=True, sombre=True, de=[1.0, .7, .5], a=[1.2, .68, .5],
                       legende="Buggy amish sur une route de Pennsylvanie, photo Ad Meskens, CC BY-SA 3.0"),
        "evc": dict(type="liste", titre="Les Amish de Pennsylvanie", items=[
            "Syndrome d'Ellis-van Creveld : nanisme, doigts surnuméraires",
            "Fréquence de l'allèle : q = 0,07 ; maladie exceptionnelle ailleurs",
            "Même mutation dans toutes les familles : un même couple d'immigrants"], marques=["1", "2", "3"], x=130, y=150, w=1020),
        "ham": dict(type="illu", nom="amish", x=150, y=100, w=980, h=540),
        "exa": dict(type="liste", titre="Ce qu'on observe, et pourquoi", items=[
            "Les deux communautés s'écartent de l'Europe, et diffèrent entre elles",
            "Effet fondateur : peu d'immigrants, un échantillon non représentatif",
            "Reproduction non aléatoire + petite taille (dérive)"], marques=["1", "2", "3"], x=150, y=170, w=980),
    }),

    # ================================================================ le groupe O
    dict(id="groupeo", chap="Le groupe O des Amérindiens", fond="cellule", humeur="mystere",
         retenir="Groupe O : 90 à 100 % chez les Amérindiens. Hypothèse : un effet fondateur à l'échelle d'un continent, puis la dérive.",
         beats=[
        "{obs_o}{obs_o.1}Deuxième cas, à l'échelle du monde. La part des personnes de groupe sanguin O, dans les populations autochtones. "
        "Presque partout, elle est élevée : souvent cinquante à soixante-dix pour cent. "
        "{obs_o.2}Mais chez les Amérindiens ? Quatre-vingt-dix à cent pour cent ! En Amérique, presque tout le monde est de groupe O.",
        "{-obs_o}{ber}{ber.1}Comment l'expliquer ? Voici l'hypothèse la plus souvent avancée. "
        "En Asie, les trois allèles A, B et O sont présents. "
        "{ber.2}L'Amérique a été peuplée par un petit groupe venu d'Asie, à travers la Béringie. "
        "Et ce groupe portait, par hasard, énormément d'allèles O.",
        "{ber.3}Ensuite, la dérive a pu effacer les allèles A et B dans plusieurs populations. "
        "Un effet fondateur… à l'échelle d'un continent.",
        "{-ber}",
    ], vis={
        "obs_o": dict(type="liste", titre="Groupe sanguin O", items=[
            "Dans le monde : souvent 50 à 70 % des personnes", "Chez les Amérindiens : 90 à 100 %"],
            marques=["◐", "●"], x=150, y=200, w=980),
        "ber": dict(type="illu", nom="beringie", x=90, y=96, w=1100, h=560),
    }),

    # ================================================================ la sélection naturelle
    dict(id="selection", chap="La sélection naturelle", fond="foret", humeur="lumiere",
         retenir="Sélection naturelle : les génotypes au meilleur succès reproducteur dans un milieu donné voient leurs allèles augmenter. Valeur sélective : 1 au maximum.",
         beats=[
        ("{d_sel}Troisième force : la {!sélection naturelle}. {d_sel.1}Elle favorise les individus dont le génotype donne, dans un milieu donné, "
         "une meilleure survie et une meilleure reproduction.", {"rate": "-4%"}),
        "Ces individus laissent plus de descendants. Et la fréquence de leurs allèles grimpe, génération après génération.",
        "{-d_sel}{vs}Pour la mesurer : la valeur sélective. {vs.1}C'est la probabilité qu'un génotype passe à la descendance. "
        "{vs.2}Elle vaut un pour le génotype qui se reproduit le mieux. "
        "{vs.3}Et si tous les génotypes ont la même valeur ? Alors, pas de sélection naturelle.",
        "{-vs}{tab_ph}Un exemple classique : la phalène du bouleau. Sur des troncs noircis par la suie, la forme noire passe inaperçue. "
        "Les oiseaux la repèrent moins. Elle survit, et laisse plus de descendants.",
        "{-tab_ph}{gr_s4}Retour à la simulation. Scénario quatre : "
        "{gr_s4.1}le génotype A A a une valeur sélective de un. A B et B B, zéro virgule huit. "
        "La fréquence de A monte, régulièrement. Elle file vers la fixation. "
        "{gr_s4.2}Et si on relance ? Presque la même courbe.",
        "Et c'est là toute la différence avec la dérive. Le résultat se répète, d'un lancement à l'autre. "
        "La sélection pousse les fréquences dans une direction : celle de l'allèle favorable, dans ce milieu.",
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
        "gr_s4": gr_freq("Scénario 4 · sélection, A//A = 1, autres 0,8 (simulé)",
                         [(S4a, "sa", "lancement 1", [6.4, .8]), (S4b, "te", "lancement 2", [8.4, .66])]),
    }),

    # ================================================================ Culex pipiens
    dict(id="culex", chap="Culex pipiens et les insecticides", fond="foret", humeur="tension",
         retenir="Culex pipiens : l'insecticide trie les larves ; AceR augmente tant que le milieu le favorise. L'allèle préexistait : pas de finalisme.",
         beats=[
        "{tab_cu}Un cas réel, tout près de chez nous : les moustiques Culex pipiens, dans le Languedoc-Roussillon. "
        "{ctx}{ctx.1}Depuis mille neuf cent soixante-huit, on les combat en épandant des insecticides sur les eaux où vivent les larves. "
        "Surtout des organophosphorés. Ils tuent les larves en perturbant certaines synapses.",
        "{ctx.2}Le gène Ace existe sous deux allèles. AceR résiste aux organophosphorés. Mais il ralentit le développement du moustique. "
        "AceS, lui, ne protège pas. {ctx.3}Dans les années quatre-vingt-dix, on épand beaucoup moins. Et on change de produit : le téméphos.",
        "{-ctx}{-tab_cu}{gr_cu}{gr_cu.1}Voici l'allure des données publiées, pour une population. "
        "Jusqu'au début des années quatre-vingt, AceR est presque absent. "
        "Puis il décolle. Il atteint environ zéro virgule six vers le milieu des années quatre-vingt-dix. Et là, il plafonne.",
        "{-gr_cu}{itr}Que s'est-il passé ? {itr.1}Dans l'eau, les larves porteuses de AceR sont rares. "
        "{itr.2}On épand l'insecticide. {itr.3}Les larves sensibles meurent. Les résistantes survivent. "
        "{itr.4}Elles seules se reproduisent. À la génération suivante, AceR est bien plus fréquent. L'insecticide exerce une {!pression de sélection}.",
        "{-itr}{cout}Mais alors, pourquoi la courbe plafonne-t-elle vers zéro virgule six ? {cout.1}Parce que l'allèle a un prix : un développement plus lent. "
        "Sans insecticide, il pénalise ses porteurs. {cout.2}Son avantage dépend donc du milieu. Moins d'insecticide, et sa progression s'arrête.",
        "{-cout}{fin_c}Et maintenant, un piège de rédaction. Très important. {fin_c.1}Jamais de finalisme. "
        "Un moustique ne devient pas résistant « pour » survivre. L'allèle AceR existait déjà, apparu par mutation. L'insecticide a simplement trié les porteurs. "
        "{fin_c.2}Même raisonnement que pour les bactéries et les antibiotiques, vu en Première. L'antibiotique ne crée pas la résistance. Il élimine les sensibles.",
        "{-fin_c}",
    ], vis={
        "tab_cu": dict(type="tableau", img="ch3-culex", fond=True, de=[1.0, .4, .56], a=[1.35, .42, .58],
                       legende="Culex pipiens, photo gbohne, CC BY-SA 2.0"),
        "ctx": dict(type="liste", titre="Culex pipiens en Languedoc-Roussillon", items=[
            "Depuis 1968 : insecticides organophosphorés sur les eaux où vivent les larves",
            "Gène Ace : AceR résiste mais ralentit le développement ; AceS ne protège pas",
            "Années 1990 : bien moins d'insecticide, et un autre produit, le téméphos"], marques=["1", "2", "3"], x=130, y=150, w=1020),
        "gr_cu": dict(type="graphe", titre="Fréquence de AceR (allure des données)", x=280, y=110, w=720, h=520,
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
        "{dvs}{dvs.g}Dérive ou sélection ? C'est la question qu'on te posera le plus souvent. Voici le tableau à savoir refaire. "
        "À gauche, la dérive génétique, avec l'effet fondateur. Sa cause : le hasard de la reproduction. "
        "Sa direction : aucune. Elle est imprévisible : deux populations identiques évoluent différemment. Et elle frappe fort dans les petites populations. "
        "Exemples : les drosophiles de Buri, les Amish, le groupe O des Amérindiens.",
        "{dvs.1}À droite, la sélection naturelle. Sa cause : un avantage de survie ou de reproduction, dans un milieu donné. "
        "Sa direction : orientée. L'allèle favorable augmente, et on retrouve le même résultat à chaque fois. Quelle que soit la taille de la population. "
        "Exemples : Culex pipiens et les insecticides, la phalène du bouleau.",
        ("P", 0.6),
        "{-dvs}{reflexe}Devant un document, un réflexe. {reflexe.1}Des populations identiques qui divergent dans tous les sens, sans lien avec le milieu ? La dérive. "
        "{reflexe.2}Un allèle qui progresse là où il est avantageux, et seulement là ? La sélection.",
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
        "{m_c}{m_c.1}Troisième branche : la notion d'espèce. Et une vraie question. "
        "Si les fréquences des allèles changent sans cesse, qu'est-ce qu'une espèce ?",
        "{-m_c}{p_lin}Au dix-huitième siècle, Linné invente le nom scientifique en deux mots : le genre, puis l'espèce. "
        "Pour lui, une espèce, ce sont des individus semblables, qui donnent des individus semblables. Elle est fixe. Créée telle quelle.",
        "{-p_lin}{p_dar}Au dix-neuvième siècle, Darwin renverse tout. Les espèces sont parentes. "
        "La variabilité des individus, triée par la sélection naturelle, les transforme au cours du temps. "
        "Et elles descendent d'ancêtres communs.",
        "Ce chapitre te donne justement les mécanismes que Darwin ignorait. La dérive, l'effet fondateur, la sélection : "
        "tout ce qui change les fréquences des allèles.",
        "{-p_dar}",
        "{crit}Alors, comment savoir si deux individus sont de la même espèce ? {crit.1}Trois critères. Et chacun a ses failles. "
        "Le critère phénotypique : la ressemblance. Le plus simple. Mais il trompe. "
        "Un mâle et une femelle de la même espèce peuvent sembler n'avoir rien à voir : c'est le dimorphisme sexuel.",
        "Exemple : l'aurore, un papillon blanc de nos prairies. Seul le mâle a le bout des ailes orange.",
        "{crit.2}Le critère biologique : l'interfécondité. Une espèce, ce sont des populations dont les individus peuvent se reproduire entre eux, "
        "avec une descendance fertile. C'est la définition de référence. Mais impossible de l'appliquer aux fossiles. "
        "Ni aux organismes sans reproduction sexuée. Et des espèces distinctes s'hybrident parfois : deux espèces de canards fuligules, par exemple.",
        "{crit.3}Le critère moléculaire : on compare les séquences d'ADN. Exemple : jusqu'en mille neuf cent quatre-vingt-seize, "
        "deux fourmis des bois, Formica lugubris et Formica paralugubris, passaient pour une seule espèce. "
        "L'ADN a tranché : ce sont deux espèces.",
        ("P", 0.6),
        "{-crit}{aucun}Bilan : {aucun.1}aucun critère ne suffit seul. Voilà une première raison pour laquelle l'espèce est si difficile à définir.",
        "{-aucun}",
    ], vis={
        "m_c": dict(type="mental", vers=["c3", "c3c"]),
        "p_lin": dict(type="portrait", img="ch3-linne", nom="Carl von Linné", dates="1707-1778", annee=1750,
                      legende="naturaliste suédois · portrait par Alexander Roslin, 1775 (domaine public)"),
        "p_dar": dict(type="portrait", img="ch3-darwin", nom="Charles Darwin", dates="1809-1882", annee=1859,
                      legende="L'Origine des espèces, 1859 · photographie vers 1874 (domaine public)"),
        "crit": dict(type="liste", titre="Trois critères, trois limites", items=[
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
        "{arb}Deux sortes d'arbres. {arb.1}L'arbre des espèces raconte l'histoire évolutive d'un groupe d'espèces. "
        "{arb.2}L'arbre des molécules raconte l'histoire d'une famille de gènes, ou de protéines.",
        "{arb.3}Et les deux ne coïncident pas toujours. Un gène peut avoir été copié plusieurs fois dans une espèce : des duplications. "
        "Il peut avoir été perdu dans une lignée. Ou passé d'une espèce à une autre, par transfert horizontal. "
        "Le chapitre deux, tu te souviens ?",
        "{-arb}{ires}Ces transferts sèment le trouble dans la classification. {ires.1}Un arbre suppose des branches qui ne se croisent jamais. "
        "{ires.2}Or, dans les années mille neuf cent quatre-vingt-dix, on séquence des génomes de bactéries. Et surprise : elles ont échangé énormément de gènes. "
        "Comparer ces gènes ne dit plus qui est parent de qui. Ça dit seulement quand chaque gène a été transféré.",
        "{cit_d}Le microbiologiste canadien William Ford Doolittle en tire une conclusion {-ires}radicale.",
        ("C", "Vouloir construire un arbre du vivant n'a pas de sens.", "cit_d"),
        "{-cit_d}{ires2}{ires2.1}{ires2.2}{ires2.3}À la place, il propose un réseau du vivant. Les espèces y sont reliées en plusieurs points, à chaque transfert de gènes.",
        "{-ires2}",
    ], vis={
        "arb": dict(type="liste", titre="Deux arbres", items=[
            "Arbre des espèces : l'histoire évolutive d'un groupe d'espèces",
            "Arbre des molécules : l'histoire d'une famille de gènes ou de protéines",
            "Ils diffèrent : duplications, pertes de gènes, transferts horizontaux"], marques=["1", "2", "≠"], x=150, y=170, w=980),
        "ires": dict(type="illu", nom="reseau", x=170, y=110, w=940, h=540),
        "cit_d": dict(type="cit", t="Vouloir construire un arbre du vivant n'a pas de sens.", a="William Ford Doolittle",
                      o="microbiologiste", x=170, y=230, w=940),
        "ires2": dict(type="illu", nom="reseau", x=170, y=110, w=940, h=540),
    }),

    # ================================================================ Denisova
    dict(id="denisova", chap="Denisova : une espèce identifiée par son ADN", fond="roche", humeur="mystere",
         retenir="Denisova : une phalange et une molaire ; leur ADN révèle une forme humaine distincte des sapiens et des Néandertaliens.",
         beats=[
        "{meth_d}{meth_d.1}Aujourd'hui, l'ADN suffit pour rattacher un spécimen à une espèce. On place la séquence d'un gène indicateur dans un arbre. "
        "Un arbre construit avec ce même gène, chez toutes les espèces connues. Les séquences sont dans des bases de données ouvertes à tous. "
        "{meth_d.2}Verdict : une espèce connue… ou une espèce nouvelle pour la science.",
        "{-meth_d}{tab_den}Cette technique a éclairé l'histoire du genre Homo. On a le génome complet de plusieurs Néandertaliens. Celui d'un très grand nombre de sapiens. "
        "Et l'ADN d'une phalange et d'une molaire, trouvées dans une grotte de Sibérie : la grotte de Denisova.",
        "{-tab_den}{iden}Voici l'arbre obtenu. {iden.1}D'un côté, les sapiens actuels : San, Yoruba, Français, Han, Papous. "
        "{iden.2}De l'autre, les Néandertaliens de Mezmaiskaya et de Vindija. "
        "{iden.3}Et Denisova ? Il se range près des Néandertaliens. Loin des sapiens.",
        "L'ADN confirme donc que Néandertaliens et humains modernes sont deux espèces différentes. "
        "Et il révèle une autre forme humaine : les Dénisoviens. Leur ADN ne ressemble ni à celui des sapiens, ni à celui des Néandertaliens. "
        "Et pourtant, de leur corps, on ne connaît presque rien. Une phalange. Une molaire.",
        ("P", 0.6),
        "{-iden}{hp_d}Et cet ADN n'a pas fini de bousculer l'idée d'espèces bien séparées. "
        "{hp_d.1}Ce qui suit est hors programme. Sapiens, Néandertaliens et Dénisoviens se sont reproduits entre eux. "
        "Hors d'Afrique, les humains actuels portent un à quatre pour cent d'ADN néandertalien. Certaines populations d'Océanie, jusqu'à cinq pour cent d'ADN dénisovien. "
        "Avec le critère d'interfécondité, ce ne seraient donc pas des espèces totalement séparées.",
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
        "{isp}{isp.1}Et maintenant, on relie tout le chapitre. L'environnement, par définition, change sans cesse. "
        "{isp.2}Imagine une population coupée en deux. Un fleuve, une montagne.",
        "{isp.3}De chaque côté, la sélection et la dérive travaillent. Chacune à sa façon. Peu à peu, les deux moitiés se différencient génétiquement.",
        "{isp.4}Et un jour, elles ne peuvent plus échanger de gènes. Plus de reproduction entre elles : "
        "elles sont devenues trop différentes.",
        "{-isp}{d_dev}C'est une {!espèce en devenir}. {d_dev.1}Une population suffisamment isolée génétiquement des autres populations.",
        ("P", 0.7),
        "{-d_dev}{bil}{bil.1}D'où la conclusion. La notion d'espèce est délicate à définir.",
        ("{bil.2}Les espèces sont des ensembles hétérogènes de populations, évoluant distinctement dans le temps.", {"rate": "-4%"}),
        "Cette phrase-là, retiens-la telle quelle.",
        "{-bil}",
    ], vis={
        "isp": dict(type="illu", nom="speciation", x=110, y=96, w=1060, h=560),
        "d_dev": dict(type="def", terme="Espèce en devenir", cles=["isolée"],
                      t="Une population suffisamment isolée génétiquement des autres populations.",
                      x=170, y=220, w=940),
        "bil": dict(type="liste", titre="Bilan", items=[
            "La notion d'espèce est délicate à définir",
            "Les espèces sont des ensembles hétérogènes de populations, évoluant distinctement dans le temps"], marques=["1", "2"], x=150, y=200, w=980),
    }),

    # ================================================================ exercice 3 (type bac)
    # 1 naissance sur 2 500 malade (m//m) : q² = 4 × 10^-4 → q = 0,02 ; p = 0,98 ; 2pq = 0,0392 ≈ 1/25,5 (≈ 1 sur 25)
    # communauté isolée : q = 0,07 → q² = 0,0049 ≈ 1 sur 204, 12 fois plus que 4 × 10^-4
    dict(id="exo3", chap="Exercice 3 · type bac", fond="aube", humeur="tension", beats=[
        "{ex3}Dernier exercice. Format bac. Une maladie génétique est due à un allèle récessif m. Seuls les homozygotes m m sont malades. "
        "Dans une grande population, supposée à l'équilibre de Hardy-Weinberg, une naissance sur deux mille cinq cents est atteinte.",
        "{-ex3}{ex3b}Cinq questions. Un : calculer q, puis p. Deux : la proportion de porteurs sains, les hétérozygotes. "
        "Trois : pourquoi faut-il le modèle pour l'estimer ? "
        "Quatre : une petite communauté isolée, fondée par quelques couples. La fréquence de m y atteint zéro virgule zéro sept. "
        "Quelle proportion de malades attendre ? Et pourquoi un tel écart avec la grande population ? "
        "Cinq : on y observe encore plus de malades que prévu. Propose une explication.",
        "{-ex3b}{pa3}Vingt minutes, comme au bac. Pause, et rédige.",
        "{pa3.stop}{-pa3}{ex3c}{ex3c.q1}Solution. {s31}{s31.1}Les malades sont les m m. Leur fréquence, c'est q au carré. "
        "{s31.2}q au carré vaut un sur deux mille cinq cents. Quatre fois dix puissance moins quatre. "
        "{s31.3}On prend la racine : q égale zéro virgule zéro deux. Et p, zéro virgule quatre-vingt-dix-huit.",
        "{-s31}{ex3c.q2}{s32}{s32.1}Les porteurs sains : deux p q. Deux fois zéro virgule quatre-vingt-dix-huit, fois zéro virgule zéro deux. "
        "{s32.2}Zéro virgule zéro trente-neuf. Environ quatre pour cent : une personne sur vingt-cinq ! "
        "Cent fois plus que les malades. L'allèle se cache surtout chez des gens en parfaite santé.",
        "{-s32}{ex3c.q3}{s33}{s33.1}Pourquoi le modèle ? Parce que les hétérozygotes ne sont pas malades. Impossible de les repérer à leur phénotype. "
        "{s33.2}On ne connaît que les malades, donc q au carré. Seule la loi de Hardy-Weinberg permet de remonter à q, puis à deux p q.",
        "{-s33}{ex3c.q4}{s34}{s34.1}Dans la communauté : q au carré, c'est zéro virgule zéro sept au carré. Zéro virgule zéro zéro quarante-neuf. "
        "{s34.2}Environ un malade sur deux cents. Douze fois plus que dans la grande population ! "
        "{s34.3}Pourquoi ? Un effet fondateur. Les quelques couples fondateurs portaient, par hasard, beaucoup d'allèles m. "
        "Puis la petite taille de la communauté a laissé jouer la dérive. Exactement comme les Amish et le syndrome d'Ellis-van Creveld.",
        "{-s34}{ex3c.q5}{s35}{s35.1}Et encore plus de malades que prévu ? C'est un excès d'homozygotes. "
        "{s35.2}Dans une petite communauté isolée, on se marie entre apparentés. La reproduction n'est pas aléatoire : pas de panmixie. "
        "{s35.3}Les conditions du modèle ne sont pas réunies. La loi de Hardy-Weinberg ne s'applique donc pas exactement. "
        "Et le calcul de la question quatre n'était qu'une estimation. C'est le regard critique qu'on attend.",
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
        "{bac}{bac.1}Et maintenant, la liste à cocher. Ce que le bac peut te demander. "
        "Définir une population, son patrimoine génétique, une fréquence allélique. "
        "{bac.2}Calculer des fréquences alléliques et génotypiques à partir d'effectifs. "
        "{bac.3}Établir et utiliser p au carré plus deux p q plus q au carré égale un. Et tester l'équilibre : observé contre attendu. "
        "{bac.4}Donner les conditions du modèle, et en tirer les causes d'écart : les forces évolutives.",
        "{bac.5}Expliquer la dérive, et son lien avec la taille de la population. Avec Buri. "
        "{bac.6}Expliquer l'effet fondateur. Avec les Amish et le groupe O. "
        "{bac.7}Expliquer la sélection naturelle. Avec Culex pipiens, et sans finalisme. "
        "{bac.8}Et discuter les critères de l'espèce, jusqu'à l'espèce en devenir.",
        ("P", 0.6),
        "{-bac}{fin_m}Retour à la carte. {fin_m.1}Le chapitre trois, c'est trois branches. {fin_m.2}Un modèle où rien n'évolue. "
        "{fin_m.3}Les forces qui en écartent les vraies populations. {fin_m.4}Et des espèces qui ne sont jamais figées. "
        "{fin_m.5}Le chapitre suivant va encore plus loin. Le phénotype peut se diversifier… sans que le génome change.",
        "Pour t'entraîner : refais les trois exercices de tête, sans regarder les solutions.",
        "{-fin_m}",
    ], vis={
        "bac": dict(type="liste", titre="Pour le bac · à cocher", petit=True, items=[
            "Définir population, patrimoine génétique, fréquence allélique", "Calculer fréquences alléliques et génotypiques",
            "p² + 2pq + q² = 1 : tester l'équilibre (observé / attendu)", "Conditions du modèle → forces évolutives",
            "Dérive et taille de la population (Buri)", "Effet fondateur (Amish, groupe O)",
            "Sélection naturelle sans finalisme (Culex pipiens)", "Critères de l'espèce, espèce en devenir"],
            marques=["✓"] * 8, x=150, y=104, w=980),
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
    "Carte mentale du thème. Schémas, graphiques et simulations faits pour la vidéo : les courbes des scénarios "
    "et l'histogramme de Buri sont des simulations, pas les résultats originaux de Buri. Les trois exercices sont inventés pour la vidéo.",
]
