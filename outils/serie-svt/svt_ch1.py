"""SVT, thème 1.A, chapitre 1 « L'origine du génotype des individus » — le chapitre en vidéo.

Même chaîne que les vidéos de physique-chimie (voir outils/serie-pc/pc_ch4.py) : generer.py svt_ch1, verifier.py,
chevauchements.py svt-ch1, fermer.py svt_ch1. Contenu : les pages t1u1, t1u2, t1u2b et t1u3 de svt/index.html, rien
au-delà ; ce que le site marque « hors programme » l'est aussi dans la vidéo, et ce qui ne vient pas du cours est dit.
Plan : la carte mentale du thème (svt/carte-mentale.js), branche par branche (c1a, c1b, c1c, c1d).
Animations du site rejouées (svt/anim/) : clonal, mitose, replication, meiose (deux orientations), nondisj (anaphase I
et anaphase II), coinegal, globines. Illustrations propres au chapitre : svt/serie/illu-svt-ch1.js.
Exercice type bac : inventé pour la vidéo (valeurs en commentaire).
"""

SITE = "svt"
CODE = "svt-ch1"
NOTION = "L'origine du génotype des individus"
NUM = 1
TITRE = "L'origine du génotype des individus"
SUIVANT = "Chapitre 2 · La complexification des génomes"
PRONONCIATION = {
    "Pando": "Panndo", "mdm2": "M D M deux", "p53": "P cinquante-trois", "TERT": "Tert", "ade2": "adé deux",
    "Hayflick": "Hèyflik", "Sturtevant": "Steurtevannt", "Morgan": "Morgane", "Boveri": "Bovéri", "Sutton": "Seuttonne",
    "Tschermak": "Tchermak", "Correns": "Corrensse", "Klinefelter": "Klaïnfelteur", "Turner": "Turneur",
    "ebony": "èbonie", "vestigial": "vestijial", "Geniegen": "Géniegène", "AMY1": "A M Y un",
    "Philadelphie": "Philadelphie", "BCR-ABL": "B C R A B L", "FNAEG": "F N A E G", "CNIL": "C nil",
    "23andMe": "vingt-trois and mi", "deCODE": "di code", "Myriad": "Myriade", "CFTR": "C F T R",
    "Jolie": "Joli", "Inserm": "Insèrme", "Bourgain": "Bourgain", "Haemophilus": "Hémophilusse",
}


SCENES = [
    # ================================================================ ouverture : la carte du thème, puis le chapitre 1
    dict(id="ouverture", chap="Ouverture", fond="foret", humeur="mystere", carton=False, beats=[
        "{carte}Voici la carte mentale de toute la partie A du thème un : génétique et évolution. "
        "Quatre chapitres. Ils racontent comment se construit, puis se transforme, le génome des êtres vivants.",
        "{carte.1}Nous allons dans le premier : l'origine du génotype des individus. "
        "Ta carte l'annote d'un mot qui le résume : transferts verticaux. Des gènes transmis de cellule en cellule, et des parents aux enfants.",
        "Le chapitre a quatre branches, et la vidéo les suit dans l'ordre. "
        "D'abord la stabilité du génome et l'évolution clonale : comment un organisme entier peut descendre d'une seule cellule. "
        "Ensuite les conséquences de la reproduction sexuée : méiose, fécondation, et les deux brassages. "
        "Puis les accidents de la méiose, et ce qu'ils ont fait de l'évolution. "
        "Et enfin, plus court, les limites éthiques du séquençage de l'ADN.",
        "Les petites étoiles de la carte marquent les schémas à savoir refaire. Pour chacun, la vidéo s'arrêtera pour te laisser le dessiner.",
        "{-carte}{titre}",
        ("P", 3.4),
    ], vis={
        "carte": dict(type="mental", vers=["t1a", "c1"], pousse=True, vol=2.0),
        "titre": dict(type="titre", sur="SVT · Thème 1 A · Chapitre 1", t="L'origine du génotype des individus",
                      sous="Le chapitre complet, expliqué de zéro au bac"),
    }),

    # ================================================================ c1a · 1 · le problème
    dict(id="probleme", chap="Stabilité & évolution clonale · le problème", fond="foret", humeur="calme", beats=[
        "{z1a}{z1a.1}Première branche : stabilité et évolution clonale. Dans ton cours, c'est l'unité un.",
        "{-z1a}{q_cell}Tu es parti d'une seule cellule. Une cellule-œuf, un seul noyau, un seul lot d'information génétique. "
        "Aujourd'hui, tu en comptes des dizaines de milliers de milliards. Et chacune descend de celle-là, par une chaîne ininterrompue de divisions.",
        "{-q_cell}{tension}Deux constats s'opposent alors. {tension.1}La stabilité : toutes ces cellules portent, à très peu de chose près, la même information. "
        "Le caryotype de l'espèce humaine se maintient identique, d'une division à l'autre, et d'une génération à l'autre. "
        "{tension.2}La diversité : et pourtant, un même organe peut présenter des phénotypes différents.",
        "{-tension}{tab_chat}Regarde ce chat. Toutes les cellules de sa peau descendent de la même cellule-œuf. Et elles ne font pas la même chose : "
        "certaines fabriquent du poil noir, d'autres du poil orange. On reviendra sur son cas.",
        "{-tab_chat}{q_unite}D'où la question à laquelle répond toute cette branche : quelles peuvent être les conséquences des modifications génétiques "
        "qui surviennent au cours de la multiplication d'un clone cellulaire ?",
        "{-q_unite}{plan1}On va procéder dans cet ordre. {plan1.1}Ce qu'est un clone, et à quoi il sert. {plan1.2}Par quel mécanisme il reste conforme. "
        "{plan1.3}Pourquoi cette conformité n'est jamais parfaite. {plan1.4}Et ce que cette imperfection produit : du grain de beauté à la tumeur.",
        "{-plan1}",
    ], vis={
        "z1a": dict(type="mental", vers=["c1", "c1a"]),
        "q_cell": dict(type="question", t="Une seule cellule au départ, des dizaines de milliers de milliards à l'arrivée."),
        "tension": dict(type="cols", g="La stabilité", gq="le même caryotype dans toutes les cellules, à chaque division",
                        d="La diversité", dq="des phénotypes différents dans un même organe", vs="mais"),
        "tab_chat": dict(type="tableau", img="ch1-chat", de=[1.0, .5, .5], a=[1.25, .45, .4],
                         legende="Chatte à la robe écaille de tortue, photo Kiiro, CC BY-SA 4.0 (Wikimedia Commons)"),
        "q_unite": dict(type="question", t="Quelles conséquences ont les modifications génétiques survenant dans un clone cellulaire ?"),
        "plan1": dict(type="liste", titre="Le chemin de l'unité 1", items=[
            "Le clone, et à quoi il sert", "La mitose, qui le garde conforme",
            "Pourquoi la conformité n'est jamais parfaite", "L'évolution clonale : du grain de beauté à la tumeur"], x=170, y=170, w=940),
    }),

    # ================================================================ c1a · 2 · le clone
    dict(id="clone", chap="Le clone, unité de base du vivant", fond="foret", humeur="lumiere",
         retenir="Clone : cellules génétiquement identiques issues de mitoses successives d'une même cellule. Cinq fonctions : croissance, régénération, reproduction asexuée, immunité, collaboration.",
         beats=[
        "{def_clone}Commençons par le mot. {def_clone.1}Un clone, c'est un ensemble de cellules qui, par mitoses successives, se copient "
        "pour donner des cellules filles génétiquement identiques à la cellule de départ. Le mot désigne aussi bien cet ensemble que l'unique cellule qui en est à l'origine. "
        "Un clone, c'est de la copie, pas de la création.",
        "{-def_clone}{an_clonal}{pts_cl}{pts_cl.1}Regarde. Au départ, une seule cellule. {an_clonal.1}{pts_cl.2}Elle se divise par mitose, ses filles aussi, et ainsi de suite : "
        "toutes portent la même information génétique. Le caryotype est conservé d'une génération cellulaire à l'autre.",
        "{pts_cl.3}Attention au mot. Dans le langage courant, « clonage » évoque la brebis Dolly et le laboratoire. "
        "En biologie cellulaire, c'est un phénomène parfaitement ordinaire, qui se produit dans ton corps à chaque seconde. Ton intestin fabrique des milliards de cellules par jour.",
        "Les cellules d'un clone ne sont pas forcément collées les unes aux autres. "
        "{-pts_cl}{-an_clonal}{formes}{formes.g}Elles peuvent rester associées et jointives : on parle alors d'un tissu, comme l'épiderme ou l'épithélium intestinal. "
        "{formes.d}Ou elles peuvent se séparer et circuler indépendamment, comme les lymphocytes B issus d'un même lymphocyte activé. "
        "La différence est spatiale, pas génétique. Dans les deux cas, une cellule mère, des mitoses, des copies.",
        "C'est maintenant le point qu'on attend en devoir. Une seule mécanique, la mitose, rend possibles cinq fonctions qui n'ont, en apparence, rien à voir entre elles. "
        "{-formes}{cinq}{cinq.1}La croissance des tissus : un organisme grandit parce que ses cellules se copient. "
        "{cinq.2}La régénération des tissus lésés : la cicatrisation d'une plaie, le renouvellement des cellules intestinales mortes. "
        "{cinq.3}La reproduction asexuée, chez les végétaux et les bactéries : des individus entiers produits par simples mitoses, sans deux partenaires.",
        "{cinq.4}La défense immunitaire : face à un antigène, le lymphocyte qui le reconnaît se multiplie à l'identique, pour produire une armée de cellules de même spécificité. "
        "{cinq.5}Et le partage, la collaboration entre les cellules d'un même organisme.",
        "{-cinq}{tab_pando}Pour cette cinquième fonction, ton cours donne un exemple spectaculaire : Pando. Dans l'Utah, une colonie de peupliers faux-trembles couvre quarante-trois hectares. "
        "{pando}{pando.1}Ce qui ressemble à une forêt de dizaines de milliers d'arbres est en réalité un seul individu. "
        "Tous les troncs sont reliés par un unique système racinaire, et ils sont génétiquement identiques.",
        "{pando.2}Ils sont apparus par drageonnage, c'est-à-dire par mitoses à partir des racines. Un clone d'environ quatre-vingt mille ans. "
        "{pando.3}Et l'intérêt est direct : les racines partagent l'eau et les nutriments entre tous les troncs. Un tronc à l'ombre est nourri par ses voisins au soleil. "
        "La collaboration, à l'échelle d'un hectare.",
        "Dans la séance un, tu as comparé cinq situations. Voici le tableau, en entier. "
        "{-pando}{-tab_pando}{tab_cmp}{tab_cmp.1}Le peuplier faux-tremble : Pando, une forêt issue d'un seul individu, qui partage ses nutriments par les racines. "
        "{tab_cmp.2}Les lymphocytes : des cellules séparées, lymphocytes B mémoire et plasmocytes, qui stockent l'information de l'antigène et détruisent le pathogène. "
        "{tab_cmp.3}L'intestin grêle : le renouvellement des cellules mortes. "
        "{tab_cmp.4}La peau : la cicatrisation, et les autogreffes. "
        "{tab_cmp.5}La pomme de terre : des plants issus d'un même tubercule, qui conservent les caractères de la plante, comme la taille ou la teneur en amidon.",
        "{-tab_cmp}{autog}Une conséquence médicale, enfin : l'autogreffe. Les cellules d'un clone sont identiques phénotypiquement et génétiquement. "
        "Elles portent donc exactement les mêmes marqueurs de surface, ces molécules par lesquelles le système immunitaire distingue le soi du non-soi. "
        "{autog.1}On peut cultiver, à partir d'un fragment de peau d'un grand brûlé, un clone de cellules d'épiderme, et le lui greffer. "
        "Son système immunitaire ne voit que du soi : pas de rejet. Avec la peau d'un donneur, ce serait l'inverse.",
        "{-autog}",
    ], vis={
        "def_clone": dict(type="def", terme="Clone", cles=["mitoses", "identiques"], x=150, y=190, w=980,
                          t="Ensemble de cellules qui, par mitoses successives, se copient pour donner des cellules filles génétiquement identiques à la cellule de départ.",
                          etape="Le mot désigne aussi la cellule unique qui est à l'origine de l'ensemble."),
        "an_clonal": dict(type="anim", nom="clonal", x=40, y=72, h=624, seg=[[0, 4.9], [5, 15.9]]),
        "pts_cl": dict(type="liste", petit=True, titre="Ce que montre l'animation", x=680, y=140, w=560, items=[
            "Une seule cellule au départ", "Des mitoses successives : des cellules filles identiques",
            "Un phénomène ordinaire, à chaque seconde dans ton corps"]),
        "formes": dict(type="cols", g="Un tissu", gq="cellules jointives : épiderme, épithélium intestinal",
                       d="Des cellules libres", dq="lymphocytes B issus d'un même lymphocyte activé", vs="ou",
                       repere="La différence est spatiale, pas génétique"),
        "cinq": dict(type="liste", titre="Cinq fonctions assurées par les clones", x=150, y=110, w=980, cles=["croissance", "régénération", "asexuée", "immunitaire", "collaboration"], items=[
            "La croissance des tissus", "La régénération des tissus lésés : cicatrisation, renouvellement de l'intestin",
            "La reproduction asexuée des végétaux et des bactéries", "La défense immunitaire : une armée de lymphocytes identiques",
            "Le partage et la collaboration entre cellules"]),
        "tab_pando": dict(type="tableau", img="ch1-pando", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                          legende="Pando, peupliers faux-trembles, Utah, photo Mx. Granger, CC0 (Wikimedia Commons)"),
        "pando": dict(type="liste", titre="Pando, un clone de 80 000 ans", x=170, y=170, w=940, items=[
            "Un seul individu : un système racinaire, des troncs génétiquement identiques",
            "Apparus par drageonnage : des mitoses à partir des racines",
            "Les racines partagent eau et nutriments : la collaboration"]),
        "tab_cmp": dict(type="liste", titre="Séance 1 · cinq clones, cinq fonctions", x=110, y=110, w=1060, items=[
            "Peuplier (Pando) · tissus : oui · partage des nutriments, extension de l'individu",
            "Lymphocytes · cellules séparées · LB mémoire, plasmocytes : défense immunitaire",
            "Intestin grêle · tissu · renouvellement des cellules mortes",
            "Peau · tissu · cicatrisation, autogreffes",
            "Pomme de terre · plants d'un même tubercule · caractères conservés, reproduction asexuée"]),
        "autog": dict(type="note", titre="L'autogreffe", cles=["marqueurs", "soi"], x=170, y=190, w=940,
                      t="Les cellules d'un clone portent les mêmes marqueurs de surface : le système immunitaire n'y voit que du soi.",
                      etape="Peau du patient cultivée puis greffée sur ses brûlures : pas de rejet."),
    }),

    # ================================================================ c1a · 3 · la mitose
    dict(id="mitose", chap="La mitose conserve le caryotype", fond="cellule", humeur="calme",
         retenir="Le nombre de chromosomes ne varie jamais au cours du cycle. La phase S double les chromatides et l'ADN ; l'anaphase sépare les chromatides. La conformité vient de la réplication semi-conservative.",
         beats=[
        "{an_mit}{pts_mit}Comment un clone reste-t-il conforme ? Par la mitose, préparée par la réplication. {an_mit.1}{pts_mit.1}Suis cette cellule à quatre chromosomes, deux paires. "
        "En G1, chaque chromosome n'a qu'une chromatide, et l'ADN est décondensé dans le noyau.",
        "{an_mit.2}{pts_mit.2}En phase S, l'ADN est répliqué : chaque chromosome passe de une à deux chromatides. La quantité d'ADN double. "
        "Mais le nombre de chromosomes, lui, ne change pas. C'est le piège de tous les graphiques.",
        "{an_mit.3}{pts_mit.3}En prophase, les chromosomes se condensent : chacun montre ses deux chromatides sœurs, reliées par le centromère. "
        "En métaphase, ils s'alignent sur la plaque équatoriale.",
        "{an_mit.4}{pts_mit.4}En anaphase, les centromères se clivent : les deux chromatides de chaque chromosome partent vers des pôles opposés. "
        "{an_mit.5}Et après la télophase, deux cellules filles, avec chacune quatre chromosomes à une chromatide. Deux clones de la cellule mère.",
        "Résume-le dans ce tableau, qui fait tomber la moitié des copies. "
        "{-pts_mit}{-an_mit}{tab_cy}{tab_cy.1}En G1 : deux n chromosomes, une chromatide chacun, une quantité d'ADN Q. "
        "{tab_cy.2}Après la phase S : toujours deux n chromosomes, mais deux chromatides, et deux Q. "
        "{tab_cy.3}En métaphase : pareil. {tab_cy.4}Et après l'anaphase, dans chaque futur noyau : deux n, une chromatide, Q.",
        "{tab_cy.5}Une seule colonne ne bouge jamais : le nombre de chromosomes. Ce que la phase S double, c'est le nombre de chromatides, donc la quantité d'ADN. "
        "Et l'anaphase ne divise pas le nombre de chromosomes : elle sépare les deux chromatides de chacun.",
        "{-tab_cy}{gr_adn}{gr_adn.1}Sur un graphique de la quantité d'ADN par cellule, ça donne ceci : un plateau à Q en G1, "
        "{gr_adn.2}une montée progressive pendant la phase S, jusqu'à deux Q, {gr_adn.3}puis une chute brutale à la division, quand l'ADN est partagé entre les deux cellules filles.",
        "Mais alors, d'où vient la conformité ? Pas de la mitose elle-même. Elle est héritée de la réplication, qui a eu lieu bien avant, en phase S. "
        "{-gr_adn}{an_rep}{pts_rep}{an_rep.1}{pts_rep.1}L'hélicase ouvre la double hélice. {an_rep.2}{pts_rep.2}Chaque brin parental sert de matrice : les nucléotides s'apparient par complémentarité, "
        "A en face de T, C en face de G, et l'ADN polymérase les assemble.",
        "{pts_rep.3}La réplication est semi-conservative : chaque nouvelle molécule garde un brin parental comme référence. C'est ce qui rend l'erreur peu probable.",
        "Le raisonnement tient donc en trois maillons. {-pts_rep}{-an_rep}{maillons}{maillons.1}En phase S, chaque molécule d'ADN est copiée de façon semi-conservative. "
        "{maillons.2}Les deux chromatides sœurs qui en résultent sont donc, sauf accident, strictement identiques. "
        "{maillons.3}Et la mitose se contente de distribuer une chromatide à chaque cellule fille.",
        "Autrement dit, la mitose ne vérifie rien et ne copie rien. Elle partage un travail déjà fait. "
        "Si le travail était bon, les deux cellules filles sont des clones. S'il ne l'était pas, elles héritent toutes les deux de l'erreur.",
        "{-maillons}{controle}Pour aller plus loin. La cellule ne se lance pas en mitose sans vérifications. À plusieurs endroits du cycle, des points de contrôle bloquent la progression : "
        "ADN intact avant d'entrer en phase S, réplication achevée avant la mitose, chromosomes bien accrochés au fuseau avant l'anaphase. "
        "Retiens-le, parce qu'il resurgira : ce sont les protéines de ces points de contrôle, p53 la première, qui sont mutées dans les cancers.",
        "{-controle}",
    ], vis={
        "an_mit": dict(type="anim", nom="mitose", x=40, y=72, h=624, seg=[[0, 6.9], [7, 12.9], [13, 27.9], [28, 34.9], [35, 51.5]]),
        "pts_mit": dict(type="liste", petit=True, titre="Les étapes", x=680, y=110, w=560, items=[
            "G1 : chromosomes à une chromatide, ADN = Q", "Phase S : deux chromatides, ADN = 2Q, toujours 4 chromosomes",
            "Prophase, métaphase : condensation, plaque équatoriale", "Anaphase, télophase : chromatides séparées, deux clones"]),
        "tab_cy": dict(type="formule", titre="Ce qui varie, ce qui ne varie pas", x=150, y=110, w=980, lignes=[
            dict(f="G1 : 2n chromosomes · 1 chromatide · Q", taille=34),
            dict(f="après la phase S : 2n · 2 chromatides · 2Q", taille=34),
            dict(f="métaphase : 2n · 2 chromatides · 2Q", taille=34),
            dict(f="après l'anaphase, par noyau : 2n · 1 chromatide · Q", taille=34),
            dict(f="Le nombre de chromosomes ne varie jamais", cadre=True, taille=36, n="la phase S double les chromatides, donc l'ADN")]),
        "gr_adn": dict(type="graphe", titre="Quantité d'ADN par cellule au cours d'un cycle", x=250, y=110, w=780, h=500,
                       ax=dict(x=[0, 10], y=[0, 2.4], gx=[], gy=[1, 2], lx="temps", ly="ADN (en Q)"),
                       el=[dict(type="courbe", pts=[[0, 1], [3, 1]], c="sa", dur=1.2, lbl="G1", lp=[1.3, 1.25]),
                           dict(type="courbe", pts=[[3, 1], [5.5, 2], [7.5, 2]], c="el", dur=1.6, lbl="phase S puis G2 et mitose", lp=[4.4, 2.25]),
                           dict(type="courbe", pts=[[7.5, 2], [7.55, 1], [10, 1]], c="ca", dur=1.2, lbl="division : 2Q → Q", lp=[8.6, 1.3])]),
        "an_rep": dict(type="anim", nom="replication", x=40, y=72, h=624, seg=[[6.5, 13.9], [14, 24.4]]),
        "pts_rep": dict(type="liste", petit=True, titre="La réplication, en phase S", x=680, y=140, w=560, items=[
            "L'hélicase ouvre la double hélice", "Complémentarité : A–T, C–G ; l'ADN polymérase assemble",
            "Semi-conservative : un brin parental dans chaque copie"]),
        "maillons": dict(type="liste", titre="Pourquoi la mitose donne des clones", x=150, y=170, w=980, items=[
            "Phase S : réplication semi-conservative de chaque molécule d'ADN",
            "Deux chromatides sœurs strictement identiques, sauf accident",
            "La mitose distribue une chromatide à chaque cellule fille"]),
        "controle": dict(type="note", titre="Les points de contrôle du cycle", plus=True, cles=["contrôle", "p53"], x=170, y=180, w=940,
                         t="ADN intact avant la phase S, réplication achevée avant la mitose, chromosomes accrochés avant l'anaphase.",
                         etape="Les protéines de ces contrôles, p53 la première, sont mutées dans les cancers."),
    }),

    # ================================================================ c1a · 4 · la conformité n'est jamais parfaite
    # doc 4 : 6,4e9 nucléotides × 2,66e-9 par nucléotide ≈ 17 erreurs par copie du génome
    dict(id="erreurs", chap="Pourquoi la copie n'est jamais parfaite", fond="cellule", humeur="tension",
         retenir="La mutation est aléatoire. Elle ne s'installe que si la réparation échoue avant la réplication suivante. Les agents mutagènes augmentent le taux d'erreurs, au hasard.",
         beats=[
        "{q_err}Copier trois milliards de paires de bases, des milliards de fois par jour, sans jamais se tromper : c'est impossible.",
        "Il existe pourtant des sécurités. {-q_err}{secu}{secu.1}La complémentarité des bases ne laisse qu'un seul nucléotide possible en face de chaque base de la matrice. "
        "{secu.2}L'ADN polymérase relit ce qu'elle vient de poser, et remplace le nucléotide mal apparié. "
        "Ces deux filtres ramènent le taux d'erreur à environ une pour un milliard de nucléotides. "
        "{secu.3}Restent les systèmes de réparation, dernière ligne de défense, qui corrigent les lésions avant la division suivante.",
        "{-secu}{f_mut}{f_mut.1}D'où la règle à écrire : une mutation ne s'installe que si la réparation échoue avant la réplication suivante. "
        "Après, elle est copiée comme le reste.",
        "Le document quatre de l'activité deux donne l'ordre de grandeur. {-f_mut}{doc4}{doc4.1}Un nouveau-né compte environ un virgule vingt-cinq fois dix puissance douze cellules. "
        "{doc4.2}Chacune porte six virgule quatre milliards de nucléotides. {doc4.3}Et le taux de mutation vaut deux virgule soixante-six fois dix puissance moins neuf par nucléotide. "
        "{doc4.4}Multiplie : à chaque copie du génome, environ dix-sept nucléotides sont changés. "
        "La mutation n'est pas un accident rare. C'est le bruit de fond inévitable de la réplication.",
        "{-doc4}{mutag}Et l'environnement en rajoute. Aux erreurs spontanées s'ajoutent les agents mutagènes : les ultraviolets, les rayonnements ionisants, "
        "des substances chimiques du tabac, certains virus. Ils n'orientent rien : ils augmentent le taux d'erreurs, au hasard.",
        "{-mutag}{piege_f}Et voici la formulation à surveiller. Ne dis jamais qu'une cellule mute pour s'adapter, "
        "ni qu'un agent mutagène provoque une mutation précise. La mutation est aléatoire, quant à sa position et à ses conséquences. "
        "C'est ensuite, et seulement ensuite, que la sélection trie.",
        "{-piege_f}",
    ], vis={
        "q_err": dict(type="question", t="Trois milliards de paires de bases, copiées des milliards de fois par jour, sans erreur ?"),
        "secu": dict(type="liste", titre="Trois sécurités", x=150, y=110, w=980, items=[
            "La complémentarité des bases : un seul nucléotide possible", "L'ADN polymérase relit et corrige : ≈ 1 erreur pour 10⁹ nucléotides",
            "Les systèmes de réparation, dernière ligne de défense"]),
        "f_mut": dict(type="formule", x=150, y=300, w=980, nu=True, lignes=[
            dict(f="Mutation = erreur que la réparation n'a pas corrigée avant la réplication suivante", cadre=True, taille=30)]),
        "doc4": dict(type="formule", titre="Activité 2 · document 4, l'ordre de grandeur", x=150, y=110, w=980, lignes=[
            dict(f="nouveau-né : ≈ 1,25 × 10^{12} cellules", taille=34),
            dict(f="génome : 6,4 × 10^{9} nucléotides par cellule", taille=34),
            dict(f="taux de mutation : 2,66 × 10^{-9} par nucléotide", taille=34),
            dict(f="6,4 × 10^{9} × 2,66 × 10^{-9} ≈ 17 nucléotides changés à chaque copie", cadre=True, taille=32,
                 n="la mutation est le bruit de fond de la réplication")]),
        "mutag": dict(type="def", terme="Agents mutagènes", cles=["hasard", "augmentent"], x=170, y=200, w=940,
                      t="UV, rayonnements ionisants, substances du tabac, certains virus : ils augmentent le taux d'erreurs, au hasard."),
        "piege_f": dict(type="note", titre="Formulation interdite", cles=["aléatoire", "ensuite"], x=170, y=200, w=940,
                        t="Jamais « la cellule mute pour s'adapter ». La mutation est aléatoire ; la sélection trie ensuite."),
    }),

    # ================================================================ c1a · 5 · l'évolution clonale
    dict(id="sousclone", chap="L'évolution clonale", fond="cellule", humeur="mystere",
         retenir="Sous-clone : descendance d'une cellule mutée, qui porte toute la mutation. Évolution clonale : diversification d'un clone par sous-clones successifs. Tout organisme est une mosaïque.",
         beats=[
        "{an_cl2}{pts_cl2}Reprenons notre clone. {an_cl2.1}{pts_cl2.1}Une erreur non corrigée s'installe dans une seule de ses cellules : ici, le point magenta. "
        "C'est une mutation somatique, dans une cellule du corps.",
        "{an_cl2.2}{pts_cl2.2}Cette cellule se divise à son tour, et toutes ses descendantes portent la mutation. "
        "Ce groupe, génétiquement distinct du reste du clone, s'appelle un sous-clone.",
        "{an_cl2.3}{pts_cl2.3}D'autres mutations peuvent s'ajouter dans le sous-clone, puis dans ses propres descendants. "
        "{an_cl2.4}La diversification progressive d'un clone, par accumulation de sous-clones successifs, s'appelle l'évolution clonale.",
        "{-pts_cl2}{-an_cl2}{def_sc}{def_sc.1}Retiens les deux définitions mot pour mot : le sous-clone, et l'évolution clonale.",
        "Le phénomène s'observe à toutes les échelles du vivant. {-def_sc}{echelles}{echelles.g}Chez un unicellulaire : le document un de l'activité deux montre des colonies de levures, "
        "la souche ade deux, qui synthétisent un pigment rouge. Après sept jours de culture à trente degrés, certaines colonies rouges portent un secteur blanc. "
        "Une cellule a muté pendant la multiplication et a perdu le pigment. Toutes ses descendantes sont blanches : la mutation se voit à l'œil nu.",
        "{echelles.d}Chez un pluricellulaire : une tumeur. Le document deux la modélise : chaque point coloré est une cellule, et plus les couleurs sont proches, "
        "plus les génomes le sont. On obtient une mosaïque. Les cellules d'une même tumeur ne partagent pas toutes le même génome : c'est l'hétérogénéité tumorale.",
        "{-echelles}{mosa}Et compte tenu des dix-sept erreurs par copie du génome vues plus haut, chacun de nous naît déjà mosaïque. "
        "Un organisme n'est jamais un clone parfait de sa cellule-œuf, mais un assemblage de sous-clones légèrement différents. "
        "La très grande majorité de ces différences est sans aucune conséquence.",
        "Et notre chat ? Son cas est hors programme, mais il mérite une précision : sa robe ne vient pas d'une mutation. "
        "{-mosa}{tab_chat2}{chat}{chat.1}Chez les mammifères femelles, chaque cellule de l'embryon précoce inactive au hasard l'un de ses deux chromosomes X, "
        "et cette inactivation est transmise à toute sa descendance. {chat.2}Or le gène de la couleur orange du pelage est porté par le X. "
        "Chez une chatte hétérozygote, les cellules qui ont éteint l'X portant l'allèle orange donnent du poil noir, les autres du poil orange.",
        "{chat.3}Chaque plage de couleur est donc le clone d'une cellule embryonnaire. D'où les taches, et d'où le fait que ces chats soient presque toujours des femelles. "
        "La leçon reste celle du chapitre : au sein d'un clone, des cellules quasi identiques peuvent avoir des phénotypes différents.",
        "{-chat}{-tab_chat2}",
    ], vis={
        "an_cl2": dict(type="anim", nom="clonal", x=40, y=72, h=624, seg=[[16, 23.9], [24, 35.9], [36, 45.9], [46, 55.5]]),
        "pts_cl2": dict(type="liste", petit=True, titre="L'évolution clonale", x=680, y=140, w=560, items=[
            "Une mutation somatique dans une cellule du clone", "Ses descendantes la portent : un sous-clone",
            "Des mutations s'ajoutent : des sous-clones de sous-clones"]),
        "def_sc": dict(type="def", terme="Sous-clone", cles=["descendantes", "distinct"], x=150, y=170, w=980,
                       t="Groupe des cellules descendant d'une cellule mutée du clone : toutes portent la mutation, génétiquement distinct du reste du clone.",
                       etape="Évolution clonale : diversification progressive d'un clone par accumulation de sous-clones successifs."),
        "echelles": dict(type="cols", g="Un unicellulaire", gq="levure ade2 : colonie rouge, secteur blanc qui a perdu le pigment",
                         d="Un pluricellulaire", dq="une tumeur : mosaïque de sous-clones, l'hétérogénéité tumorale", vs="et"),
        "mosa": dict(type="note", titre="Le mosaïcisme est la règle", cles=["mosaïque", "conséquence"], x=170, y=200, w=940,
                     t="Chacun naît déjà mosaïque : un assemblage de sous-clones légèrement différents, presque toujours sans conséquence."),
        "tab_chat2": dict(type="tableau", img="ch1-chat", fond=True, sombre=True, de=[1.2, .5, .45], a=[1.0, .5, .5],
                          legende="Chatte à la robe écaille de tortue, photo Kiiro, CC BY-SA 4.0 (Wikimedia Commons)"),
        "chat": dict(type="liste", titre="Pourquoi la peau du chat est bicolore · hors programme", x=150, y=150, w=980, items=[
            "Femelle : chaque cellule de l'embryon éteint au hasard un de ses deux X, pour toute sa descendance",
            "Le gène orange est sur le X : X orange éteint → poil noir, X noir éteint → poil orange",
            "Chaque tache est le clone d'une cellule embryonnaire"]),
    }),

    # ================================================================ c1a · 6 · où tombe la mutation
    dict(id="cancer", chap="Où tombe la mutation décide de tout", fond="nuit", humeur="tension",
         retenir="Séquence codante → protéine modifiée (levure ade2). Séquence régulatrice → expression modifiée (TERT). Gène du contrôle du cycle → prolifération (p53). Le cancer : une accumulation de mutations.",
         beats=[
        "C'est le cœur de l'unité. {trois}Les conséquences d'une mutation dépendent moins de la mutation elle-même que de l'endroit où elle tombe. Trois cas, par gravité croissante. "
        "{trois.1}Sur une séquence codante : c'est la protéine elle-même qui change, donc le phénotype de la cellule mutée et de tout son sous-clone. Exemple : la levure ade deux qui perd son pigment rouge.",
        "{trois.2}Sur une séquence régulatrice : la protéine ne change pas, mais son niveau d'expression, qui peut être augmenté ou supprimé. Exemple : le gène TERT, surexprimé. "
        "{trois.3}Sur un gène du contrôle du cycle : la cellule endommagée n'est plus ni réparée, ni éliminée. Elle prolifère, et accumule d'autres mutations. Exemple : le gène p53.",
        "{-trois}{il_p53}Commençons par p53, le frein. Découverte en mille neuf cent soixante-dix-neuf, la protéine p53 est un facteur de transcription : elle se lie à l'ADN et commande l'expression d'autres gènes. "
        "En temps normal, elle est maintenue à un niveau très bas par une protéine partenaire, mdm2, qui l'envoie en permanence à la destruction. "
        "{il_p53.1}Quand une lésion de l'ADN apparaît, {il_p53.2}p53 échappe à mdm2 et s'accumule. Elle déclenche alors l'une de deux réponses. "
        "{il_p53.3}Soit l'arrêt de la division, le temps que la réparation fasse son travail. {il_p53.4}Soit l'apoptose, la mort programmée de la cellule, si les dégâts sont irréparables.",
        "{il_p53.5}Sans p53 fonctionnelle, aucune de ces deux issues ne se déclenche. Les cellules à l'ADN endommagé survivent, se divisent, et accumulent les mutations suivantes. "
        "C'est pourquoi p53 est le gène le plus fréquemment altéré dans les cellules tumorales. On l'appelle parfois le gardien du génome.",
        "Passons à TERT, l'accélérateur. Son cas est plus subtil. Le document six compare la séquence d'un témoin à celles de deux cancers : "
        "{-il_p53}{tert}{tert.1}on relève deux substitutions, non pas dans la partie codante du gène, mais dans sa séquence régulatrice. {tert.2}La mutation n'est pas dans le gène, elle est à côté. "
        "Elle suffit à faire fabriquer beaucoup plus de protéine TERT. {tert.3}La protéine, elle, est parfaitement normale.",
        "{-tert}{telo}Pourquoi est-ce si grave ? C'est hors programme, mais éclairant. Les extrémités des chromosomes portent des séquences répétées, les télomères. "
        "À chaque réplication, le bout du brin n'est pas tout à fait copié : le chromosome raccourcit un peu. "
        "Après une cinquantaine de divisions, les télomères sont trop courts, et la cellule cesse de se diviser : c'est la limite de Hayflick, décrite en mille neuf cent soixante et un.",
        "{telo.1}TERT est la sous-unité catalytique de la télomérase, l'enzyme qui reconstruit les télomères. La surexprimer, c'est remettre le compteur à zéro, indéfiniment : la cellule devient immortelle. "
        "C'est le cas dans environ quatre-vingt-dix pour cent des cellules cancéreuses.",
        "{-telo}{tumeur}Réunis les deux. {tumeur.1}Un accélérateur bloqué : la division sans fin. {tumeur.2}Un frein cassé : ni réparation, ni apoptose. "
        "{tumeur.3}Le sous-clone se multiplie indéfiniment, accumule de nouvelles mutations à chaque cycle, et engendre lui-même de nouveaux sous-clones. "
        "Cet empilement de lignées, c'est une tumeur.",
        "{-tumeur}{piege_k}Le piège classique : ne dis pas que la mutation provoque le cancer. Une mutation isolée ne suffit jamais. "
        "Il faut une accumulation de mutations successives, qui touchent à la fois l'accélérateur et les freins. Le cancer est un processus, étalé souvent sur des années. Pas un événement.",
        "Et c'est ce qui explique pourquoi certains traitements échouent : il suffit qu'un sous-clone porte par hasard une mutation qui le rend insensible au médicament, pour qu'il repeuple la tumeur à lui seul.",
        "{-piege_k}",
    ], vis={
        "trois": dict(type="liste", titre="La mutation touche…", x=110, y=120, w=1060, items=[
            "Une séquence codante → la protéine change · levure ade2 : perte du pigment rouge",
            "Une séquence régulatrice → l'expression change · gène TERT surexprimé",
            "Un gène du contrôle du cycle → la cellule prolifère · gène p53"]),
        "il_p53": dict(type="illu", nom="p53", x=140, y=90, w=1000, h=580),
        "tert": dict(type="liste", titre="Activité 2 · document 6 : le gène TERT", x=150, y=170, w=980, items=[
            "Deux substitutions dans la séquence régulatrice", "Pas dans la partie codante : la mutation est à côté du gène",
            "Beaucoup plus de protéine TERT, mais une protéine normale"]),
        "telo": dict(type="note", titre="Télomères et immortalité · hors programme", plus=True, cles=["télomères", "Hayflick"], x=150, y=170, w=980,
                     t="Les télomères raccourcissent à chaque réplication ; après une cinquantaine de divisions, la cellule s'arrête : la limite de Hayflick (1961).",
                     etape="TERT reconstruit les télomères : surexprimée, elle rend la cellule immortelle (≈ 90 % des cancers)."),
        "tumeur": dict(type="liste", titre="Du sous-clone à la tumeur", x=150, y=170, w=980, items=[
            "Accélérateur bloqué (TERT) : division sans fin", "Frein cassé (p53) : ni réparation, ni apoptose",
            "Le sous-clone accumule des mutations et engendre de nouveaux sous-clones"]),
        "piege_k": dict(type="note", titre="Le piège classique", cles=["accumulation", "processus"], x=170, y=190, w=940,
                        t="Une mutation isolée ne suffit jamais : le cancer est une accumulation de mutations, un processus, pas un événement."),
    }),

    # ================================================================ c1a · 7 · somatique ou germinale
    dict(id="lignee", chap="Qui hérite ? Somatique ou germinale", fond="foret", humeur="calme",
         retenir="Mutation somatique : change le phénotype de l'individu, pas transmise. Mutation germinale : transmise à la descendance. Conséquences selon la nature, la portion touchée, la lignée.",
         beats=[
        "{som_ger}{som_ger.g}Dernière distinction, décisive. Une mutation somatique touche une cellule du corps. Elle peut modifier le phénotype de l'individu, "
        "mais elle n'est pas transmise à ses enfants. {som_ger.d}Une mutation germinale touche une cellule de la lignée reproductrice. "
        "Elle peut ne rien changer chez l'individu, et pourtant être transmise à toute sa descendance.",
        "{-som_ger}{souris}Le document cinq le montre en une image : deux embryons de souris. {souris.1}Même mutation, même moment du développement. "
        "{souris.2}Si elle touche la lignée somatique, une tache apparaît sur la peau de l'animal, et sur lui seul. "
        "{souris.3}Si elle touche la lignée germinale, la tache se retrouve chez tous ses descendants.",
        "Les deux questions sont indépendantes : une mutation germinale peut être totalement invisible chez son porteur et ressortir chez un petit-enfant ; "
        "une mutation somatique peut être spectaculaire chez l'individu, et disparaître avec lui.",
        "{-souris}{mosg}Pour aller plus loin, hors programme : il existe un cas intermédiaire, le mosaïcisme germinal. "
        "Une mutation survenue tôt dans le développement peut toucher une partie seulement des futurs gamètes. "
        "Des parents en apparence indemnes, chez qui aucun test sanguin ne détecte rien, peuvent alors avoir plusieurs enfants atteints de la même maladie génétique.",
        "Voici le bilan de toute la branche, qui fait un plan de paragraphe argumenté tout prêt. Les conséquences d'une mutation varient selon trois critères. "
        "{-mosg}{bilan1}{bilan1.1}Sa nature : silencieuse ou non. {bilan1.2}La portion du chromosome affectée : séquence codante, séquence régulatrice, ou gène du contrôle du cycle. "
        "{bilan1.3}Et la lignée cellulaire concernée : somatique, ou germinale.",
        "Voilà pour la conservation du génome et ses accidents. La branche suivante aborde une autre source de diversité : ni accidentelle, ni pathologique, mais programmée, et massive. "
        "La reproduction sexuée.",
        "{-bilan1}",
    ], vis={
        "som_ger": dict(type="cols", g="Mutation somatique", gq="cellule du corps : phénotype de l'individu, jamais transmise",
                        d="Mutation germinale", dq="lignée reproductrice : transmise à toute la descendance", vs="≠"),
        "souris": dict(type="liste", titre="Activité 2 · document 5, deux embryons de souris", x=150, y=170, w=980, items=[
            "Même mutation, au même moment du développement", "Lignée somatique : une tache sur l'animal seul",
            "Lignée germinale : la tache chez tous ses descendants"]),
        "mosg": dict(type="note", titre="Le mosaïcisme germinal · hors programme", plus=True, cles=["gamètes", "indemnes"], x=170, y=200, w=940,
                     t="Une mutation précoce touche une partie seulement des gamètes : des parents indemnes peuvent avoir plusieurs enfants atteints."),
        "bilan1": dict(type="liste", titre="Les conséquences d'une mutation dépendent de…", x=150, y=170, w=980, items=[
            "Sa nature : silencieuse ou non", "La portion touchée : codante, régulatrice, gène du contrôle du cycle",
            "La lignée : somatique ou germinale"]),
    }),

    # ================================================================ c1b · 1 · méiose et fécondation (★)
    dict(id="cadre", chap="Reproduction sexuée · méiose et fécondation", fond="foret", humeur="lumiere",
         retenir="Diploïde 2n (cellules du corps), haploïde n (gamètes). Méiose : 2n → n. Fécondation : n + n → 2n. La mitose donne des clones ; la méiose, non.",
         beats=[
        "{z1b}{z1b.1}Deuxième branche : les conséquences de la reproduction sexuée, et la diversité. Deux schémas y portent l'étoile : à savoir refaire.",
        "{-z1b}{q_div}Deux parents, quatre enfants. Aucun n'est identique aux autres, aucun n'est identique à ses parents. "
        "Pourtant, tous appartiennent à la même espèce, et tous possèdent quarante-six chromosomes, comme leurs père et mère.",
        "Il y a donc deux exigences contradictoires à satisfaire en même temps. {-q_div}{deux_ex}{deux_ex.g}Conserver le caryotype de l'espèce, génération après génération. "
        "{deux_ex.d}Et produire, à chaque fois, un individu qui n'a jamais existé. "
        "La réponse tient en deux mécanismes complémentaires : la méiose fabrique des gamètes tous différents, et la fécondation en combine deux, au hasard.",
        "{-deux_ex}{diplo}D'abord le vocabulaire. {diplo.1}Les cellules somatiques possèdent deux exemplaires de chaque information génétique, portés par des chromosomes homologues réunis en paires. "
        "Elles sont diploïdes, notées deux n. Chez l'humain, deux n égale quarante-six. "
        "{diplo.2}Les gamètes n'ont qu'un exemplaire de chaque paire. Ils sont haploïdes, notés n : vingt-trois chez l'humain.",
        "{-diplo}{homol}Un point à ne pas laisser flou : deux chromosomes homologues portent les mêmes gènes, aux mêmes emplacements, mais pas forcément les mêmes allèles. "
        "L'un vient du père, l'autre de la mère. Tout le chapitre découle de cette dissymétrie. S'ils portaient les mêmes allèles, il n'y aurait rien à brasser.",
        "{-homol}{cyc}{cyc.1}Voici maintenant le premier schéma à savoir refaire : le cycle de vie. Une cellule de l'individu est diploïde : deux n. "
        "{cyc.2}Dans les gonades, la méiose forme les gamètes. Elle divise le nombre de chromosomes par deux : de deux n à n. "
        "{cyc.3}La fécondation réunit deux gamètes, deux génomes haploïdes d'origine indépendante, et rétablit la diploïdie : n plus n donne deux n. La cellule obtenue est le zygote, ou cellule-œuf.",
        "{cyc.4}Puis des mitoses successives, qui forment un clone, construisent l'individu, toujours à deux n. "
        "{cyc.5}C'est cet aller-retour, entre une phase diploïde et une courte phase haploïde, qui maintient quarante-six chromosomes d'une génération à la suivante. "
        "Sans méiose, le nombre de chromosomes doublerait à chaque génération.",
        "{-cyc}{pa_cyc}À toi. Sur une feuille, refais ce cycle : l'individu, la méiose, les gamètes, la fécondation, le zygote, les mitoses, avec deux n et n à chaque étape.",
        "{pa_cyc.stop}Et une confusion à ne pas faire. Toute division cellulaire ne mène pas à un clone. "
        "{-pa_cyc}{mit_mei}{mit_mei.g}La mitose répartit équitablement le matériel génétique dans chaque cellule fille, et forme des clones. "
        "{mit_mei.d}La méiose ne transmet que la moitié de l'information génétique de la cellule initiale, et s'accompagne d'un brassage des allèles maternels et paternels. "
        "La reproduction sexuée ne produit donc pas de clones.",
        "{-mit_mei}{bil_fec}Le bilan à savoir écrire : {bil_fec.1}la fécondation entre gamètes haploïdes rassemble, au hasard, dans une même cellule diploïde, deux génomes d'origine indépendante, "
        "qui apportent chacun un lot d'allèles. Chaque paire d'allèles est faite de deux allèles identiques, c'est l'homozygotie, ou de deux allèles différents, l'hétérozygotie.",
        "{-bil_fec}{reine}Une question hors programme, pour finir : pourquoi le sexe ? Une femelle qui se reproduirait seule transmettrait cent pour cent de ses gènes, contre cinquante en reproduction sexuée. "
        "L'explication la plus solide : le brassage produit à chaque génération des combinaisons inédites, et c'est décisif face aux parasites, qui s'adaptent à la combinaison la plus répandue. "
        "Une population sexuée leur offre une cible qui se dérobe. C'est l'hypothèse de la Reine Rouge.",
        "{-reine}",
    ], vis={
        "z1b": dict(type="mental", vers=["c1", "c1b"]),
        "q_div": dict(type="question", t="Deux parents, quatre enfants, tous différents : comment ?"),
        "deux_ex": dict(type="cols", g="Conserver", gq="le caryotype de l'espèce, 46 chromosomes à chaque génération",
                        d="Innover", dq="un individu qui n'a jamais existé", vs="et"),
        "diplo": dict(type="liste", titre="Deux états", x=150, y=170, w=980, items=[
            "Diploïde (2n) : cellules somatiques, chromosomes homologues par paires · 2n = 46",
            "Haploïde (n) : gamètes, un chromosome de chaque paire · n = 23"]),
        "homol": dict(type="def", terme="Chromosomes homologues", cles=["gènes", "allèles"], x=170, y=200, w=940,
                      t="Les mêmes gènes, aux mêmes emplacements, mais pas forcément les mêmes allèles : l'un vient du père, l'autre de la mère."),
        "cyc": dict(type="illu", nom="cycle", x=140, y=78, w=1000, h=620),
        "pa_cyc": dict(type="pause", t="Refais le cycle méiose – fécondation, avec 2n et n à chaque étape.",
                       sous="Schéma ★ à savoir refaire. Mets la vidéo sur pause, dessine-le, puis compare."),
        "mit_mei": dict(type="cols", g="Mitose", gq="tout le matériel génétique dans chaque fille : des clones",
                        d="Méiose", dq="la moitié de l'information, brassée : pas de clones", vs="≠"),
        "bil_fec": dict(type="def", terme="La fécondation", cles=["hasard", "indépendante"], x=150, y=180, w=980,
                        t="Elle rassemble au hasard, dans une cellule diploïde, deux génomes d'origine indépendante, chacun avec son lot d'allèles.",
                        etape="Deux allèles identiques : homozygotie. Deux allèles différents : hétérozygotie."),
        "reine": dict(type="note", titre="Pourquoi le sexe ? · hors programme", plus=True, cles=["parasites", "Reine"], x=170, y=190, w=940,
                      t="Le brassage crée des combinaisons inédites : face aux parasites, une cible qui se dérobe. L'hypothèse de la Reine Rouge."),
    }),

    # ================================================================ c1b · 2 · Mendel
    dict(id="mendel", chap="Comment on l'a compris : Mendel", fond="aube", humeur="lumiere",
         retenir="Lignées pures croisées : F1 uniforme (dominance), F2 en 3/4 – 1/4 (705 violettes, 224 blanches). Trois lois : pureté des gamètes, dominance, ségrégation indépendante.",
         beats=[
        "{melange}Comment a-t-on compris tout cela ? Jusqu'au dix-huitième siècle, on croyait à l'hérédité par mélange : les caractères des deux parents se mélangeraient comme deux liquides. "
        "Une fleur rouge croisée avec une blanche devrait donner une fleur rose. {melange.1}Défaut fatal : si les caractères se mélangeaient, toute variation s'effacerait en quelques générations. "
        "On n'observe rien de tel.",
        "{-melange}{por_mendel}Entre en scène Gregor Mendel, moine et naturaliste, avec ses pois. Son dispositif repose sur trois mots. "
        "{voc_m}{voc_m.1}Une lignée pure : une lignée dont le caractère reste inchangé de génération en génération, obtenue par autofécondation. En termes modernes, elle est homozygote. "
        "{voc_m.2}L'hybridation : un croisement entre deux variétés de la même espèce, en contrôlant la fécondation. "
        "{voc_m.3}Le monohybridisme : une hybridation entre deux lignées pures qui ne diffèrent que par un seul caractère.",
        "Le pois n'est pas un choix anodin : il s'autoféconde naturellement, ce qui donne des lignées pures, et on peut empêcher cette autofécondation pour croiser comme on veut. "
        "Et Mendel a compté ses plants, par milliers. C'est la première fois que la statistique entre dans l'étude de l'hérédité.",
        "{-voc_m}{-por_mendel}{tab_pois}Il croise deux lignées pures : des pois à fleurs violettes, de génotype V V, et des pois à fleurs blanches, v v.",
        "Chaque parent de lignée pure ne produit qu'un seul type de gamète : {-tab_pois}{ech1}{ech1.1}V pour l'un, {ech1.2}v pour l'autre. "
        "{ech1.3}Toutes les cases donnent le même génotype, V v, et le même phénotype : violet. {ech1.4}La F1 est uniforme. Et surtout, pas de rose : la théorie du mélange tombe.",
        "{-ech1}Puis il laisse les F1 s'autoféconder. {ech2}{ech2.1}Cette fois, chaque F1 produit deux types de gamètes, V et v, {ech2.2}de chaque côté. "
        "{ech2.3}Trois cases sur quatre donnent du violet, une seule du blanc. {ech2.4}Le blanc réapparaît, dans un rapport de trois quarts, un quart. "
        "Et c'est exactement ce que Mendel a compté : sept cent cinq plants à fleurs violettes, deux cent vingt-quatre à fleurs blanches.",
        "{-ech2}C'est la réapparition qui est le coup décisif. {reapp}{reapp.1}Un caractère qui disparaît puis revient intact n'a pas été dilué. Il a été transmis sans s'exprimer. "
        "Il existe donc, dans l'hybride, deux éléments distincts qui ne se mélangent pas : ce que nous appelons aujourd'hui des allèles.",
        "D'où les trois lois, dans l'ordre du cours. {-reapp}{lois}{lois.1}La loi de pureté des gamètes, ou loi de ségrégation, ou de disjonction des allèles : "
        "lors de la formation des gamètes, les deux allèles d'un gène, portés par les deux chromosomes d'une paire, se séparent obligatoirement. Chaque gamète n'en reçoit qu'un.",
        "{lois.2}La loi de dominance : chez un hétérozygote, l'allèle dominant masque l'expression de l'allèle récessif. D'où l'uniformité de la F1. "
        "{lois.3}La loi de ségrégation indépendante : les allèles de gènes différents sont distribués dans les gamètes indépendamment les uns des autres.",
        "Attention : la fiche d'activité numérotait ces lois autrement. Retiens l'ordre du diaporama, celui-ci : c'est celui de ton cours.",
        "{-lois}{frise_m}Hors programme, l'histoire de ce que tu apprends. {frise_m.1}Mendel publie en mille huit cent soixante-six, et personne ne comprend. "
        "Il meurt en mille huit cent quatre-vingt-quatre sans savoir ce qu'il avait trouvé. {frise_m.2}En mille neuf cent, trois botanistes, de Vries, Correns et Tschermak, "
        "refont les mêmes expériences et exhument son article. {frise_m.3}Et en mille neuf cent deux, Sutton et Boveri font le rapprochement avec les chromosomes, "
        "qui vont par paires et se séparent lors de la formation des gamètes. C'est la théorie chromosomique de l'hérédité.",
        "{-frise_m}",
    ], vis={
        "melange": dict(type="def", terme="Hérédité par mélange", cles=["mélange", "effacerait"], x=170, y=190, w=940,
                        t="Croyance ancienne : les caractères des parents se mélangent comme deux liquides. Rouge × blanc donnerait rose.",
                        etape="Faux : toute variation s'effacerait en quelques générations."),
        "por_mendel": dict(type="portrait", img="ch1-mendel", nom="Gregor Mendel", dates="1822 – 1884", annee=1866,
                           legende="photo d'archives publiée par Hugo Iltis, CC BY 4.0"),
        "voc_m": dict(type="liste", titre="Le vocabulaire de Mendel", x=640, y=150, w=580, petit=True, items=[
            "Lignée pure : caractère inchangé de génération en génération, homozygote",
            "Hybridation : croisement contrôlé de deux variétés de la même espèce",
            "Monohybridisme : deux lignées pures qui diffèrent par un seul caractère"]),
        "tab_pois": dict(type="tableau", img="ch1-pois", de=[1.0, .5, .5], a=[1.3, .5, .45],
                         legende="Fleur de pois (Pisum sativum), photo Dyorkey, CC BY-SA 3.0 (Wikimedia Commons)"),
        "ech1": dict(type="illu", nom="echiquier", x=190, y=90, w=900, h=560, titre="(V//V) violet × (v//v) blanc : la F1",
                     col=["V", "V"], lig=["v", "v"], hl=[0, 1, 2, 3], bas="F1 uniforme : 100 % [violet]",
                     cases=[["(V//v)", "[violet]", "#b48cff"], ["(V//v)", "[violet]", "#b48cff"], ["(V//v)", "[violet]", "#b48cff"], ["(V//v)", "[violet]", "#b48cff"]]),
        "ech2": dict(type="illu", nom="echiquier", x=190, y=90, w=900, h=560, titre="(V//v) × (V//v) : la F2",
                     col=["V", "v"], lig=["V", "v"], hl=[3], bas="3/4 [violet] – 1/4 [blanc] · Mendel : 705 et 224",
                     cases=[["(V//V)", "[violet]", "#b48cff"], ["(V//v)", "[violet]", "#b48cff"], ["(V//v)", "[violet]", "#b48cff"], ["(v//v)", "[blanc]", "#e7f2da"]]),
        "reapp": dict(type="note", titre="Le coup décisif", cles=["intact", "allèles"], x=170, y=200, w=940,
                      t="Un caractère qui disparaît en F1 puis revient intact en F2 a été transmis sans s'exprimer.",
                      etape="Deux éléments distincts qui ne se mélangent pas : des allèles."),
        "lois": dict(type="liste", titre="Les trois lois, dans l'ordre du cours", x=130, y=150, w=1020, items=[
            "Pureté des gamètes (ségrégation, disjonction) : un seul allèle de chaque gène par gamète",
            "Dominance : l'allèle dominant masque le récessif, d'où l'uniformité de la F1",
            "Ségrégation indépendante : les allèles de gènes différents se répartissent indépendamment"]),
        "frise_m": dict(type="liste", titre="D'où vient ce que tu apprends · hors programme", x=150, y=170, w=980, items=[
            "1866 · Mendel publie : personne ne comprend ; il meurt en 1884",
            "1900 · De Vries, Correns et Tschermak refont les expériences et exhument son article",
            "1902 · Sutton et Boveri : théorie chromosomique de l'hérédité"]),
    }),

    # ================================================================ c1b · 3 · groupes sanguins
    dict(id="groupes", chap="Une application : les groupes sanguins", fond="aube", humeur="calme",
         retenir="Trois allèles A, B, O ; deux par individu. A et B dominants sur O, codominants entre eux. Génotype (A//O), phénotype [A].",
         beats=[
        "Application immédiate : les groupes sanguins. {gs}Le gène possède trois allèles, A, B et O, alors qu'un individu n'en porte que deux. "
        "{gs.1}A A ou A O donnent le groupe A : A est dominant sur O, un seul allèle A suffit. {gs.2}De même, B B ou B O donnent le groupe B. "
        "{gs.3}A B donne le groupe A B : A et B sont codominants, aucun ne masque l'autre. {gs.4}Et O O donne le groupe O : O est récessif, il faut les deux allèles pour qu'il s'exprime.",
        "Conséquence pratique : un individu de groupe A peut cacher un allèle O. Prenons un homme A O et une femme B O. "
        "{-gs}{ech3}{ech3.1}La femme produit des gamètes B et O. {ech3.2}L'homme, des gamètes A et O. "
        "{ech3.3}Le couple peut avoir des enfants des quatre groupes : A B, A, B et O. {ech3.4}En proportions égales, un quart chacun.",
        "Et une exigence d'écriture, valable à chaque exercice : {-ech3}{ecr}{ecr.1}le génotype s'écrit entre parenthèses, les deux allèles séparés par une double barre. "
        "{ecr.2}Le phénotype s'écrit entre crochets. Cette convention se perd vite : garde-la.",
        "{-ecr}",
    ], vis={
        "gs": dict(type="liste", titre="Le gène du groupe sanguin : trois allèles", x=150, y=150, w=980, items=[
            "(A//A) ou (A//O) → [A] : A dominant sur O", "(B//B) ou (B//O) → [B] : B dominant sur O",
            "(A//B) → [AB] : A et B codominants", "(O//O) → [O] : O récessif"]),
        "ech3": dict(type="illu", nom="echiquier", x=190, y=90, w=900, h=560, titre="♂ (A//O) × ♀ (B//O)",
                     col=["B", "O"], lig=["A", "O"], hl=[0, 1, 2, 3], bas="Quatre groupes possibles, 1/4 chacun",
                     cases=[["(A//B)", "[AB]", "#ffd24a"], ["(A//O)", "[A]", "#ff6b5b"], ["(B//O)", "[B]", "#6fd3e8"], ["(O//O)", "[O]", "#e7f2da"]]),
        "ecr": dict(type="formule", titre="L'écriture exigée", x=200, y=200, w=880, lignes=[
            dict(f="génotype : (A//O)", taille=44, n="entre parenthèses, double barre entre les deux allèles"),
            dict(f="phénotype : [A]", taille=44, n="entre crochets")]),
    }),

    # ================================================================ c1b · 4 · brassage interchromosomique (★)
    # 2^23 = 8 388 608 ≈ 8 millions ; (2^23)^2 ≈ 7,0 × 10^13 = 70 000 milliards
    dict(id="inter", chap="Le brassage interchromosomique", fond="cellule", humeur="mystere",
         retenir="Préparé en métaphase I (orientation aléatoire et indépendante des paires), effectué en anaphase I (séparation des homologues). 2ⁿ gamètes équiprobables ; 2²³ ≈ 8 millions chez l'humain.",
         beats=[
        "{def_inter}{def_inter.1}Premier brassage, le brassage interchromosomique. C'est le mécanisme de la méiose qui répartit au hasard les chromosomes paternels et maternels dans les gamètes. "
        "Il concerne les gènes portés par des paires de chromosomes différentes, c'est-à-dire des gènes indépendants.",
        "{-def_inter}{an_me1}{pts_me1}Regarde cette cellule à deux n égale quatre. {an_me1.1}{pts_me1.1}Deux paires d'homologues : dans chaque paire, un chromosome maternel, en magenta, et un paternel, en cyan. "
        "Le grand porte les gènes A et B, le petit le gène D. La cellule est hétérozygote pour les trois.",
        "{an_me1.2}{pts_me1.2}Avant la méiose, l'ADN est répliqué : chaque chromosome a deux chromatides sœurs.",
        "{an_me1.3}{pts_me1.3}En métaphase un, les paires d'homologues se placent de part et d'autre du plan équatorial. Chaque paire dans une position aléatoire. "
        "C'est là que le brassage est préparé.",
        "{an_me1.4}{pts_me1.4}En anaphase un, les homologues de chaque paire se séparent et migrent vers des pôles opposés. La séparation des homologues entraîne celle des allèles. "
        "C'est là que le brassage s'effectue. Ici, le grand et le petit chromosome magenta partent du même côté. "
        "Tu remarques au passage que des morceaux de chromatides ont changé de couleur : c'est le crossing-over, l'autre brassage, qu'on verra juste après.",
        "{-pts_me1}{-an_me1}{an_me2}{pts_me2}Mais rien n'obligeait les paires à s'orienter ainsi. {an_me2.1}{pts_me2.1}Rejouons la métaphase un, avec l'autre orientation de la petite paire. "
        "{an_me2.2}{pts_me2.2}Cette fois, en anaphase un, chaque pôle reçoit un grand chromosome d'une couleur et un petit de l'autre. "
        "{an_me2.3}{pts_me2.3}Puis vient la méiose deux. Dans chacune des deux cellules, les chromatides sœurs se séparent, comme lors d'une mitose. "
        "On obtient quatre cellules haploïdes, avec un seul chromosome de chaque paire. Compare-les avec celles de la première orientation : "
        "les associations d'allèles ne sont plus les mêmes. Ce sont d'autres gamètes, avec d'autres combinaisons d'allèles.",
        "Les deux verbes sont attendus mot pour mot. {-pts_me2}{-an_me2}{deux_v}{deux_v.1}Le brassage interchromosomique est préparé en métaphase un : les paires d'homologues s'y placent de part et d'autre du plan équatorial, dans une position aléatoire. "
        "{deux_v.2}Il s'effectue en anaphase un, quand les homologues se séparent. "
        "{deux_v.3}Et le mot décisif est : indépendant. L'orientation d'une paire ne dit rien de l'orientation des autres. Avec deux paires, on obtient quatre gamètes équiprobables, au contenu allélique différent.",
        "{-deux_v}{kineto}Pour aller plus loin : pourquoi est-ce vraiment aléatoire ? Rien ne marque un chromosome comme paternel ou maternel. "
        "Les fibres du fuseau arrivent des deux pôles, à l'aveugle, et s'accrochent aux kinétochores. Lequel des deux homologues part à gauche dépend seulement de la fibre arrivée la première. "
        "Une loterie, paire par paire.",
        "{-kineto}{deuxn}Combien de gamètes différents ? {deuxn.1}Chaque paire offre deux possibilités, et les paires sont indépendantes. "
        "Un gène hétérozygote : deux gamètes. Deux gènes sur deux paires : quatre. Trois : huit. Avec n paires, deux puissance n. "
        "{deuxn.2}Chez l'humain, vingt-trois paires donnent deux puissance vingt-trois : environ huit millions de gamètes différents, chez un seul individu.",
        "{deuxn.3}Et la fécondation en combine deux, au hasard : huit millions fois huit millions, de l'ordre de soixante-dix mille milliards de zygotes différents possibles, pour un seul couple.",
        "{deuxn.4}Une précision qui compte : un gène homozygote donne toujours le même allèle, quelle que soit l'orientation de sa paire. Il ne contribue pas à la diversité. "
        "Le nombre de combinaisons est d'autant plus élevé que les parents ont de gènes à l'état hétérozygote.",
        "{-deuxn}{pa_inter}À toi : schéma étoilé. Dessine une cellule à deux n égale quatre en métaphase un, avec deux allèles par paire, puis les deux orientations possibles, "
        "et les quatre types de gamètes qu'elles donnent.",
        "{pa_inter.stop}{-pa_inter}",
    ], vis={
        "def_inter": dict(type="def", terme="Brassage interchromosomique", cles=["hasard", "indépendants"], x=150, y=180, w=980,
                          t="Mécanisme de la méiose qui répartit au hasard les chromosomes paternels et maternels dans les gamètes.",
                          etape="Il concerne des gènes portés par des paires différentes : des gènes indépendants."),
        "an_me1": dict(type="anim", nom="meiose", x=40, y=72, h=624, seg=[[0, 6.9], [7, 13.9], [36, 43.9], [44, 57.9]]),
        "pts_me1": dict(type="liste", petit=True, titre="La méiose, première orientation", x=680, y=110, w=560, items=[
            "2n = 4 : deux paires, maternel en magenta, paternel en cyan", "Réplication : deux chromatides par chromosome",
            "Métaphase I : paires sur le plan équatorial, orientation aléatoire", "Anaphase I : les homologues se séparent"]),
        "an_me2": dict(type="anim", nom="meiose", x=40, y=72, h=624, opt=1, vit=1.3, seg=[[36.6, 43.9], [44, 57.9], [58, 83.5]]),
        "pts_me2": dict(type="liste", petit=True, titre="L'autre orientation", x=680, y=110, w=560, items=[
            "Métaphase I : la petite paire s'oriente dans l'autre sens", "Anaphase I : d'autres associations de chromosomes",
            "Méiose II : d'autres gamètes"]),
        "deux_v": dict(type="liste", titre="Le brassage interchromosomique, à rédiger ainsi", x=130, y=150, w=1020, items=[
            "Préparé en métaphase I : paires d'homologues de part et d'autre du plan équatorial, position aléatoire",
            "Effectué en anaphase I : les homologues se séparent, et les allèles avec eux",
            "Orientation indépendante d'une paire à l'autre : des gamètes équiprobables"]),
        "kineto": dict(type="note", titre="Une loterie, paire par paire · hors programme", plus=True, cles=["aveugle", "loterie"], x=170, y=190, w=940,
                       t="Les fibres du fuseau s'accrochent aux kinétochores à l'aveugle : le premier attachement décide du pôle de chaque homologue."),
        "deuxn": dict(type="formule", titre="Combien de gamètes différents ?", x=150, y=100, w=980, lignes=[
            dict(f="1, 2, 3 … n gènes hétérozygotes sur des paires différentes → 2, 4, 8 … 2^{n} gamètes", taille=32),
            dict(f="humain : 2^{23} ≈ 8 millions de gamètes différents", cadre=True, taille=36),
            dict(f="fécondation : 8 millions × 8 millions ≈ 70 000 milliards de zygotes possibles", taille=32),
            dict(f="un gène homozygote n'ajoute aucune diversité", txt=True, taille=28)]),
        "pa_inter": dict(type="pause", t="Une cellule 2n = 4 en métaphase I, deux orientations, quatre types de gamètes.",
                         sous="Schéma ★ à savoir refaire. Mets la vidéo sur pause, dessine-le, puis reprends."),
    }),

    # ================================================================ c1b · 5 · brassage intrachromosomique (★)
    dict(id="intra", chap="Le brassage intrachromosomique", fond="cellule", humeur="mystere",
         retenir="Crossing-over en prophase I, entre chromatides non sœurs d'un bivalent (chiasma). Il concerne des gènes liés ; gamètes recombinés minoritaires, non équiprobables. Les deux brassages se cumulent.",
         beats=[
        "{lim}Le brassage interchromosomique a une limite évidente. Il ne peut rien pour deux gènes situés sur la même paire de chromosomes. "
        "Ceux-là devraient voyager ensemble, indéfiniment, et la troisième loi de Mendel serait fausse pour eux. "
        "{lim.1}L'expérience montre qu'elle l'est presque : les quatre phénotypes attendus apparaissent, mais deux sont largement majoritaires, et deux sont rares. "
        "Les allèles restent solidaires la plupart du temps. Mais pas toujours.",
        "{-lim}{an_me3}{pts_me3}Revenons à la prophase un. {an_me3.1}{pts_me3.1}Les chromosomes homologues s'apparient étroitement, sur toute leur longueur. "
        "Chaque paire forme un bivalent, de quatre chromatides.",
        "{an_me3.2}{pts_me3.2}Deux chromatides non sœurs se croisent en un point : le chiasma. {pts_me3.3}À cet endroit, elles se cassent au même niveau et échangent leurs segments. "
        "C'est le crossing-over, ou enjambement. Les allèles B et b changent de chromatide : A b et a B sont des combinaisons nouvelles.",
        "{pts_me3.4}Sur les quatre chromatides du bivalent, deux restent parentales, et deux deviennent recombinées.",
        "Deux précisions qui font la différence en devoir. {-pts_me3}{-an_me3}{deux_p}{deux_p.1}L'échange a lieu entre chromatides non sœurs. "
        "Entre chromatides sœurs, identiques, il ne produirait rigoureusement rien. "
        "{deux_p.2}Et le crossing-over ne se produit pas dans toutes les cellules, ni toujours au même endroit. C'est pourquoi les gamètes recombinés restent minoritaires. "
        "{deux_p.3}L'individu produit donc quatre types de gamètes, mais non équiprobables.",
        "Le piège classique : confondre les deux brassages. {-deux_p}{piege_b}{piege_b.g}L'interchromosomique concerne des paires différentes, se joue en métaphase un puis en anaphase un, et donne des gamètes équiprobables. "
        "{piege_b.d}L'intrachromosomique concerne une seule paire, se joue en prophase un, et donne des gamètes non équiprobables. "
        "Et surtout : ils ne s'excluent pas. Ils se cumulent à chaque méiose, leurs effets se multiplient. Puis la fécondation multiplie encore le résultat.",
        "{-piege_b}{sturt}Pour aller plus loin, hors programme. Plus deux gènes sont éloignés sur le chromosome, plus il y a de place entre eux pour qu'un crossing-over tombe, "
        "donc plus les recombinés sont fréquents. En mille neuf cent treize, Alfred Sturtevant, étudiant chez Morgan, en tire la première carte génétique : "
        "le pourcentage de recombinés est une distance. Un centimorgan, c'est un pour cent de descendants recombinés.",
        "{-sturt}{pa_intra}À toi : deuxième schéma étoilé du brassage. Dessine un bivalent en prophase un, avec deux gènes, A et B, puis le crossing-over entre deux chromatides non sœurs, "
        "et les quatre chromatides obtenues, deux parentales, deux recombinées.",
        "{pa_intra.stop}{-pa_intra}",
    ], vis={
        "lim": dict(type="note", titre="Deux gènes sur la même paire", cles=["majoritaires", "rares"], x=170, y=190, w=940,
                    t="Ils devraient voyager ensemble. Or les quatre phénotypes apparaissent : deux majoritaires, deux rares.",
                    etape="Les allèles restent solidaires la plupart du temps, mais pas toujours."),
        "an_me3": dict(type="anim", nom="meiose", x=40, y=72, h=624, seg=[[14, 21.9], [22, 35.9]]),
        "pts_me3": dict(type="liste", petit=True, titre="Le crossing-over", x=680, y=110, w=560, items=[
            "Prophase I : homologues appariés, un bivalent de 4 chromatides", "Chiasma : deux chromatides non sœurs se croisent",
            "Cassure au même niveau, échange de segments", "2 chromatides parentales, 2 recombinées"]),
        "deux_p": dict(type="liste", titre="Deux précisions, une conséquence", x=150, y=160, w=980, items=[
            "Entre chromatides non sœurs (entre sœurs, rien ne changerait)",
            "Pas dans toutes les cellules, pas toujours au même endroit : recombinés minoritaires",
            "Quatre types de gamètes, non équiprobables"]),
        "piege_b": dict(type="cols", g="Interchromosomique", gq="paires différentes, métaphase I puis anaphase I, gamètes équiprobables",
                        d="Intrachromosomique", dq="une seule paire, prophase I, gamètes non équiprobables", vs="+",
                        repere="Ils se cumulent à chaque méiose"),
        "sturt": dict(type="note", titre="Une distance en pourcentages · hors programme", plus=True, cles=["distance", "centimorgan"], x=170, y=190, w=940,
                      t="Plus deux gènes sont éloignés, plus les recombinés sont fréquents. Sturtevant, 1913 : 1 centimorgan = 1 % de recombinés."),
        "pa_intra": dict(type="pause", t="Un bivalent avec deux gènes, le crossing-over, deux chromatides parentales et deux recombinées.",
                         sous="Schéma ★ à savoir refaire. Mets la vidéo sur pause, dessine-le, puis reprends."),
    }),

    # ================================================================ c1b · 6 · le test-cross, TP 2 et TP 3
    # TP 2 : 17, 14, 12, 11 sur 54 (31, 26, 22, 20 %) ; TP 3 : 16, 17, 3, 4 sur 40 → 82,5 % parentaux, 17,5 % recombinés
    dict(id="testcross", chap="L'outil : le test-cross", fond="foret", humeur="calme",
         retenir="Test-cross : F1 double hétérozygote × double homozygote récessif. 4 × 25 % → gènes indépendants. 2 classes majoritaires (parentaux) + 2 minoritaires (recombinés) → gènes liés.",
         beats=[
        "{def_tc}Comment savoir, dans une expérience, quel brassage a joué ? Avec l'outil du chapitre : le test-cross. "
        "{def_tc.1}C'est un croisement entre un individu double hétérozygote, issu de la F1, et un individu double homozygote récessif. Les descendants forment la F2.",
        "Tout l'intérêt est dans le second partenaire. Le double homozygote récessif ne transmet que des allèles récessifs : il ne masque rien. "
        "Chaque descendant exprime donc directement l'allèle qu'il a reçu de la F1. On lit les gamètes de la F1 sur les phénotypes de la F2.",
        "{-def_tc}{fam}Deux familles de phénotypes. {fam.g}Les phénotypes parentaux reproduisent les combinaisons d'allèles de la génération P. "
        "{fam.d}Les phénotypes recombinés portent une combinaison nouvelle. C'est là qu'est créée la diversité génétique.",
        "La méthode, en trois réflexes, à appliquer sur n'importe quel énoncé. {-fam}{reflexes}{reflexes.1}Compte les phénotypes : s'il y en a quatre, les deux gènes ont chacun deux allèles. "
        "{reflexes.2}Regarde les proportions. Quatre classes à vingt-cinq pour cent : gamètes équiprobables, gènes indépendants, brassage interchromosomique seul. "
        "Deux classes majoritaires et deux minoritaires : gènes partiellement liés, et les minoritaires sont le produit d'un crossing-over. "
        "{reflexes.3}Identifie parentaux et recombinés, en revenant toujours aux phénotypes des parents de lignée pure.",
        "{-reflexes}{tab_dro}Tu l'as fait au TP, avec des drosophiles. {tp2}Le TP deux étudie deux gènes situés sur deux paires différentes. "
        "{tp2.1}La couleur du corps : clair, eb plus, dominant, ou sombre, ebony. {tp2.2}La longueur des ailes : longues, vg plus, dominant, ou courtes, vestigial. "
        "{tp2.3}On croise la F1, eb plus eb, vg plus vg, avec le parent double récessif.",
        "{-tp2}{-tab_dro}{bar2}{bar2.1}Résultats de la correction, sur cinquante-quatre mouches : dix-sept, quatorze, douze et onze. Trente et un, vingt-six, vingt-deux et vingt pour cent. "
        "{bar2.2}Aucune classe n'est massivement majoritaire : on est proche des vingt-cinq pour cent attendus. Les écarts sont des fluctuations d'échantillonnage, sur un petit effectif. "
        "Gènes indépendants : hypothèse validée.",
        "{-bar2}{tp3}Le TP trois étudie deux gènes situés, cette fois, sur la même paire. {tp3.1}Corps gris, b plus, ou noir, black. Ailes normales, vg plus, ou courtes. "
        "{tp3.2}Comme les deux gènes sont sur le même chromosome, on les écrit du même côté de la double barre. La F1 est vg plus b plus, sur vg b.",
        "{-tp3}{bar3}{bar3.1}Le test-cross, sur quarante mouches : seize gris aux ailes normales, dix-sept noirs aux ailes courtes, trois gris aux ailes courtes, quatre noirs aux ailes normales. "
        "{bar3.2}On est très loin des vingt-cinq pour cent. {bar3.3}Les deux classes majoritaires reproduisent les parents : quatre-vingt-deux et demi pour cent de parentaux. "
        "Les deux minoritaires sont recombinées : dix-sept et demi pour cent. Les gènes sont partiellement liés, et les recombinés viennent d'un crossing-over.",
        "Et, d'après l'approfondissement de tout à l'heure, ces dix-sept et demi pour cent mesurent une distance : environ dix-sept centimorgans entre les deux gènes.",
        "{-bar3}",
    ], vis={
        "def_tc": dict(type="def", terme="Test-cross", cles=["hétérozygote", "récessif"], x=150, y=180, w=980,
                       t="Croisement d'un individu double hétérozygote de la F1 avec un double homozygote récessif.",
                       etape="Le récessif ne masque rien : les phénotypes de la F2 révèlent les gamètes de la F1."),
        "fam": dict(type="cols", g="Phénotypes parentaux", gq="les combinaisons d'allèles de la génération P",
                    d="Phénotypes recombinés", dq="une combinaison nouvelle : la diversité", vs="≠"),
        "reflexes": dict(type="liste", titre="Lire un test-cross en trois réflexes", x=110, y=130, w=1060, items=[
            "Compter les phénotypes : quatre, donc deux gènes à deux allèles",
            "Les proportions : 4 × 25 % → indépendants ; 2 majoritaires + 2 minoritaires → liés",
            "Majoritaires = parentaux, minoritaires = recombinés (vérifier avec les parents)"]),
        "tab_dro": dict(type="tableau", img="ch1-drosophiles", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="Tubes de culture de drosophiles, photo Masur, CC BY-SA 4.0 (Wikimedia Commons)"),
        "tp2": dict(type="liste", titre="TP 2 · deux gènes indépendants", x=150, y=170, w=980, items=[
            "Corps : clair eb+ (dominant) ou sombre eb (ebony)", "Ailes : longues vg+ (dominant) ou courtes vg (vestigial)",
            "Test-cross : F1 (eb+//eb ; vg+//vg) × P2 (eb//eb ; vg//vg)"]),
        "bar2": dict(type="illu", nom="barres", x=190, y=84, w=900, h=600, titre="TP 2 · test-cross, 54 drosophiles", total=54, max=40, dec=0,
                     classes=[["ailes longues ; corps sombre", 17, ""], ["ailes longues ; corps clair", 14, ""],
                              ["ailes courtes ; corps clair", 12, ""], ["ailes courtes ; corps sombre", 11, ""]]),
        "tp3": dict(type="formule", titre="TP 3 · deux gènes liés", x=150, y=170, w=980, lignes=[
            dict(f="corps gris b+ ou noir b · ailes normales vg+ ou courtes vg", taille=30),
            dict(f="F1 : (vg+ b+ // vg b) × P2 : (vg b // vg b)", cadre=True, taille=36, n="deux gènes liés : du même côté de la double barre")]),
        "bar3": dict(type="illu", nom="barres", x=190, y=84, w=900, h=600, titre="TP 3 · test-cross, 40 drosophiles", total=40, max=50,
                     somme="parentaux : 82,5 % · recombinés : 17,5 %",
                     classes=[["corps gris ; ailes normales", 16, "p"], ["corps noir ; ailes courtes", 17, "p"],
                              ["corps gris ; ailes courtes", 3, "r"], ["corps noir ; ailes normales", 4, "r"]]),
    }),

    # ================================================================ c1c · 1 · la mauvaise disjonction (★)
    dict(id="nondisj", chap="Accidents de la méiose · la mauvaise disjonction", fond="nuit", humeur="tension",
         retenir="Anaphase I : une paire d'homologues ne se sépare pas → 4 gamètes anormaux. Anaphase II : deux chromatides ne se séparent pas → 2 gamètes anormaux. n + 1 → trisomie (47) ; n − 1 → monosomie (45).",
         beats=[
        "{z1c}{z1c.1}Troisième branche : les accidents méiotiques, et leur rôle dans l'évolution. Trois schémas étoilés.",
        "{-z1c}{q_acc}La méiose qu'on vient de voir fonctionne : elle produit des gamètes tous différents, mais tous équilibrés, avec exactement un chromosome de chaque paire. "
        "Cette mécanique est précise. Elle n'est pas infaillible. Un chromosome peut migrer du mauvais côté. Deux chromosomes peuvent se casser et échanger des morceaux. "
        "Deux homologues peuvent s'apparier de travers.",
        "On parle d'accidents génétiques : des erreurs rares, survenant au hasard, qui produisent des gamètes anormaux. "
        "{-q_acc}{acc}{acc.1}La plupart sont néfastes : fausses couches, syndromes, maladies. {acc.2}Mais certains, très rares, enrichissent le génome de gènes nouveaux, et ont joué un rôle majeur dans l'évolution. "
        "Le plan suit l'exposé présenté en classe : le nombre de chromosomes, puis les échanges de portions, puis l'évolution.",
        "{-acc}{an_nd}{pts_nd}Premier accident : une mauvaise répartition des chromosomes. {an_nd.1}{pts_nd.1}Une cellule à deux n égale quatre entre en méiose. Le petit chromosome joue le rôle du chromosome vingt et un. "
        "{an_nd.2}{pts_nd.2}En métaphase un, les paires sont en place, comme d'habitude.",
        "{an_nd.3}{pts_nd.3}Mais en anaphase un, les deux homologues de la paire vingt et un partent vers le même pôle. C'est une mauvaise disjonction, en anaphase un. "
        "{an_nd.4}La cellule se divise : l'une des deux cellules filles a reçu les deux chromosomes vingt et un, l'autre aucun. "
        "{an_nd.5}Puis la méiose deux sépare les chromatides. Les quatre gamètes sont anormaux : deux en ont un en trop, n plus un, et deux un en moins, n moins un.",
        "{an_nd.6}{pts_nd.4}Si un gamète n plus un est fécondé par un gamète normal, la cellule-œuf a trois chromosomes vingt et un : quarante-sept chromosomes. C'est une trisomie vingt et un.",
        ("P", 4.0),
        "{-pts_nd}{-an_nd}{an_nd2}{pts_nd2}L'erreur peut aussi survenir plus tard. {an_nd2.1}{pts_nd2.1}Cette fois, l'anaphase un se passe bien : chaque pôle reçoit un chromosome de chaque paire. "
        "{an_nd2.2}{pts_nd2.2}C'est en méiose deux que les deux chromatides d'un chromosome vingt et un restent ensemble, et partent vers le même pôle, dans une seule des deux cellules. "
        "{an_nd2.3}{pts_nd2.3}Résultat : deux gamètes anormaux, un n plus un et un n moins un, et deux gamètes normaux.",
        "La différence est souvent demandée. {-pts_nd2}{-an_nd2}{tab_nd}{tab_nd.1}Erreur en anaphase un : les deux homologues d'une paire migrent ensemble, les quatre gamètes sont anormaux. "
        "{tab_nd.2}Erreur en anaphase deux : deux chromatides migrent ensemble, deux gamètes anormaux, deux normaux. "
        "{tab_nd.3}Après fécondation par un gamète normal : n plus un plus n, deux n plus un, quarante-sept, une trisomie. "
        "{tab_nd.4}Ou n moins un plus n, deux n moins un, quarante-cinq, une monosomie.",
        "{-tab_nd}{voc_nd}Le vocabulaire exact : ton cours dit mauvaise disjonction, ou migration anormale des chromosomes. Les manuels disent non-disjonction : c'est la même chose. "
        "Et on nomme l'anomalie d'après le chromosome concerné : trois chromosomes vingt et un, trisomie vingt et un. Un seul X sans Y, monosomie X.",
        "{-voc_nd}{pa_nd}À toi : schéma étoilé. Dessine une mauvaise disjonction en anaphase un, puis en anaphase deux, avec les quatre gamètes obtenus dans chaque cas, "
        "et le caryotype de la cellule-œuf après fécondation.",
        "{pa_nd.stop}{-pa_nd}",
    ], vis={
        "z1c": dict(type="mental", vers=["c1", "c1c"]),
        "q_acc": dict(type="question", t="Un chromosome du mauvais côté, des morceaux échangés, un appariement de travers…"),
        "acc": dict(type="liste", titre="Les accidents génétiques : rares, aléatoires", x=150, y=180, w=980, items=[
            "Le plus souvent néfastes : fausses couches, syndromes, maladies",
            "Parfois source de gènes nouveaux : un moteur de l'évolution"]),
        "an_nd": dict(type="anim", nom="nondisj", x=40, y=72, h=624, seg=[[0, 5.9], [6, 12.9], [13, 20.9], [21, 27.9], [28, 44.9], [45, 65.5]], vit=1.2),
        "pts_nd": dict(type="liste", petit=True, titre="Erreur en anaphase I", x=680, y=110, w=560, items=[
            "2n = 4 : le petit chromosome joue le 21", "Métaphase I : les paires en place",
            "Anaphase I : la paire 21 migre vers le même pôle", "Fécondation : 47 chromosomes, trisomie 21"]),
        "an_nd2": dict(type="anim", nom="nondisj", x=40, y=72, h=624, opt=1, vit=1.3, seg=[[13, 27.9], [28, 37.9], [38, 44.9]]),
        "pts_nd2": dict(type="liste", petit=True, titre="Erreur en anaphase II", x=680, y=110, w=560, items=[
            "Anaphase I normale", "Méiose II : les deux chromatides d'un 21 restent ensemble",
            "Deux gamètes anormaux, deux normaux"]),
        "tab_nd": dict(type="formule", titre="La mauvaise disjonction", x=120, y=110, w=1040, lignes=[
            dict(f="anaphase I : deux homologues ensemble → 4 gamètes anormaux (2 à n + 1, 2 à n − 1)", taille=29),
            dict(f="anaphase II : deux chromatides ensemble → 2 anormaux (n + 1, n − 1), 2 normaux", taille=29),
            dict(f="(n + 1) + n = 2n + 1 = 47 : trisomie", cadre=True, taille=34),
            dict(f="(n − 1) + n = 2n − 1 = 45 : monosomie", cadre=True, taille=34)]),
        "voc_nd": dict(type="note", titre="Le vocabulaire exact", cles=["disjonction", "chromosome"], x=170, y=200, w=940,
                       t="Mauvaise disjonction = migration anormale = non-disjonction. On nomme l'anomalie d'après le chromosome : trisomie 21, monosomie X."),
        "pa_nd": dict(type="pause", t="Mauvaise disjonction en anaphase I, puis en anaphase II : les gamètes, puis la cellule-œuf.",
                      sous="Schéma ★ à savoir refaire. Mets la vidéo sur pause, dessine-le, puis reprends."),
    }),

    # ================================================================ c1c · 2 · viables ou non : trisomie 21, Turner
    dict(id="viables", chap="Viables ou non viables", fond="nuit", humeur="calme",
         retenir="La plupart des anomalies du nombre sont non viables (trisomie 14, monosomies d'autosomes). Viables avec symptômes : trisomie 21, XXY, Turner (45, X0).",
         beats=[
        "{quant}Pourquoi ces anomalies sont-elles si graves ? Une anomalie du nombre ne change aucun gène : elle change la quantité de gènes. "
        "Or toutes les protéines d'une cellule sont produites en proportions équilibrées. Un chromosome en trop, avec ses centaines de gènes, dérègle cet équilibre. "
        "La conséquence dépend donc de la taille du chromosome, et du nombre de gènes qu'il porte.",
        "{-quant}{viab}{viab.1}La plupart sont non viables : l'embryon meurt précocement, et la grossesse se termine par une fausse couche spontanée. "
        "C'est le cas de la trisomie quatorze, et de toutes les monosomies qui portent sur les autosomes. "
        "{viab.2}Quelques-unes sont viables, mais avec des symptômes : la trisomie vingt et un, ou les anomalies des chromosomes sexuels, comme le caryotype X X Y, le syndrome de Klinefelter. "
        "{viab.3}Les fréquences de ton tableau ne viennent pas du cours : le document de l'exposé était resté vide. Par exemple, une naissance sur sept cents à mille pour la trisomie vingt et un, sans dépistage.",
        "{-viab}{tab_k21}Voici les chromosomes d'une cellule de personne trisomique, photographiés au microscope pendant une division, avant d'être rangés. "
        "{-tab_k21}{k21}Rangés par paires, de la plus grande à la plus petite, ils forment le caryotype. {k21.1}Compte ceux de la paire vingt et un : il y en a trois. Quarante-sept chromosomes.",
        "{-k21}{t21}{t21.1}Le plus souvent, l'erreur s'est produite pendant la méiose d'un des parents, en anaphase un ou deux, et le gamète n plus un a été fécondé. "
        "{t21.2}Le phénotype : un visage caractéristique, des doigts courts, une nuque plate et épaisse, une hyperlaxité des articulations, "
        "une déficience intellectuelle d'intensité variable, et souvent une malformation cardiaque.",
        "{t21.3}Le diagnostic peut se faire avant la naissance : l'amniocentèse prélève du liquide amniotique, qui contient des cellules du fœtus. "
        "On en établit le caryotype, et on compte les chromosomes vingt et un.",
        "{-t21}{age}Hors programme : pourquoi le risque augmente-t-il avec l'âge de la mère ? Le plus souvent, le chromosome en trop vient de l'ovocyte, et l'erreur date de la méiose un. "
        "Chez la femme, la méiose un commence avant la naissance, puis s'arrête en prophase un. Elle ne reprend qu'à l'ovulation, parfois quarante ans plus tard. "
        "Pendant ce temps, les protéines qui tiennent les homologues ensemble s'usent.",
        "Un exemple de monosomie viable : le syndrome de Turner. {-age}{turner}{turner.1}Il ne touche que les filles. Leur caryotype n'a qu'un seul chromosome X, sans second chromosome sexuel. "
        "On écrit quarante-cinq, X zéro. Le gamète fécondant ne contenait aucun chromosome sexuel. "
        "{turner.2}Il est rare parce que, dans la grande majorité des cas, l'embryon X zéro meurt.",
        "{turner.3}Le phénotype : une petite taille, environ un mètre quarante-cinq à l'âge adulte ; pas de puberté spontanée ; une infertilité définitive ; "
        "et des troubles associés, dont des malformations cardiaques, une hypertension, une scoliose, une hypothyroïdie. "
        "{turner.4}Pas de guérison : un traitement hormonal déclenche la puberté, mais l'infertilité ne se corrige pas.",
        "{-turner}{hypo}Une erreur à ne pas recopier : la diapositive de l'exposé parlait d'hyperthyroïdie. Le trouble associé au syndrome de Turner est l'inverse : "
        "l'hypothyroïdie, une thyroïde qui ne fonctionne pas assez.",
        "{-hypo}",
    ], vis={
        "quant": dict(type="def", terme="Une question de quantité", cles=["quantité", "équilibre"], x=170, y=190, w=940,
                      t="L'anomalie ne change aucun gène, mais la quantité de gènes : l'équilibre des protéines est rompu.",
                      etape="Plus le chromosome porte de gènes, plus c'est grave."),
        "viab": dict(type="liste", titre="Viables ou non viables", x=130, y=140, w=1020, items=[
            "Non viables : trisomie 14, monosomies d'autosomes → fausse couche",
            "Viables avec symptômes : trisomie 21, XXY (Klinefelter), X0 (Turner)",
            "Fréquences (sources médicales, hors cours) : trisomie 21 ≈ 1 naissance sur 700 à 1 000"]),
        "tab_k21": dict(type="tableau", img="ch1-caryotype21", de=[1.0, .5, .5], a=[1.15, .62, .62],
                        legende="Chromosomes d'une cellule 47, XY, +21 en métaphase, Doc. Josef Reischig, CC BY-SA 3.0 (Wikimedia Commons)"),
        "k21": dict(type="illu", nom="caryo21", x=140, y=90, w=1000, h=600),
        "t21": dict(type="liste", titre="La trisomie 21", x=150, y=150, w=980, items=[
            "Génotype : un chromosome 21 en plus, 47 chromosomes",
            "Phénotype : visage caractéristique, doigts courts, hyperlaxité, déficience intellectuelle variable, souvent malformation cardiaque",
            "Diagnostic prénatal : amniocentèse, caryotype des cellules du fœtus"]),
        "age": dict(type="note", titre="L'âge de la mère · hors programme", plus=True, cles=["prophase", "ovulation"], x=170, y=190, w=940,
                    t="La méiose I de l'ovocyte s'arrête en prophase I avant la naissance et ne reprend qu'à l'ovulation, parfois quarante ans plus tard."),
        "turner": dict(type="liste", titre="Le syndrome de Turner · 45, X0", x=130, y=130, w=1020, items=[
            "Filles seulement : un seul chromosome X", "Rare : la plupart des embryons X0 meurent",
            "Petite taille (≈ 1,45 m), pas de puberté spontanée, infertilité définitive, troubles associés",
            "Traitement hormonal pour la puberté ; l'infertilité demeure"]),
        "hypo": dict(type="note", titre="Erreur de l'exposé", cles=["hypothyroïdie"], x=170, y=210, w=940,
                     t="Pas « hyperthyroïdie » : le syndrome de Turner s'accompagne souvent d'une hypothyroïdie."),
    }),

    # ================================================================ c1c · 3 · translocations (★ échange de portions)
    dict(id="transloc", chap="Les translocations", fond="nuit", humeur="mystere",
         retenir="Translocation : un segment se fixe sur un chromosome d'une autre paire (réciproque ou robertsonienne). Souvent sans effet chez le porteur, mais trisomie ou monosomie possible dans sa descendance.",
         beats=[
        "{def_tr}Deuxième famille d'accidents : les chromosomes eux-mêmes sont modifiés. Des morceaux se cassent, changent de place, sont perdus ou dupliqués. "
        "{def_tr.1}Une translocation, c'est un segment de chromosome qui se casse et va se fixer sur un autre chromosome, non homologue, c'est-à-dire d'une autre paire.",
        "{-def_tr}{types_tr}Il en existe deux types. {types_tr.1}La translocation réciproque : deux chromosomes de paires différentes échangent chacun un segment. "
        "{types_tr.2}La translocation robertsonienne : deux chromosomes de paires différentes, dont le centromère est tout près d'une extrémité, fusionnent au niveau du centromère, pour n'en former plus qu'un.",
        "Ne confonds pas avec le crossing-over. {-types_tr}{tr_co}{tr_co.g}Le crossing-over se fait entre chromatides de chromosomes homologues, de la même paire. Il est normal. "
        "{tr_co.d}La translocation se fait entre chromosomes de paires différentes. C'est un accident.",
        "{-tr_co}{il_tr}Une translocation est le plus souvent équilibrée : aucun gène n'est perdu, il a seulement changé de place. Le porteur est en bonne santé, et l'ignore souvent. "
        "Le problème apparaît dans sa descendance. L'exemple du cours : {il_tr.1}un chromosome vingt et un s'est fixé sur un chromosome quatorze. "
        "Le porteur a un quatorze normal, un vingt et un normal, et un chromosome quatorze-vingt et un : quarante-cinq chromosomes, mais tous ses gènes en double.",
        "{il_tr.2}Lors de sa méiose, ces trois chromosomes se répartissent entre les gamètes. Un gamète avec le quatorze et le vingt et un normaux donne un enfant au caryotype normal. "
        "Le chromosome quatorze-vingt et un seul donne un porteur sain, comme son parent.",
        "{il_tr.3}Mais le quatorze-vingt et un avec le vingt et un normal donne une trisomie vingt et un : trois exemplaires des gènes du vingt et un. "
        "{il_tr.4}Et les trois autres combinaisons donnent une monosomie vingt et un, une trisomie quatorze ou une monosomie quatorze : toutes non viables.",
        "{-il_tr}{prin_tr}Retiens le principe. {prin_tr.1}Une translocation a rarement des conséquences sur l'individu qui la porte, mais elle peut produire des gamètes déséquilibrés, "
        "donc une trisomie ou une monosomie dans sa descendance. On parle de trisomie vingt et un par translocation : quelques pour cent des cas, chiffre qui vient de sources extérieures au cours.",
        "{-prin_tr}{lmc}Hors programme : une translocation peut aussi survenir dans une cellule somatique. Dans la leucémie myéloïde chronique, les chromosomes neuf et vingt-deux échangent un segment, "
        "dans une cellule souche de la moelle. Le vingt-deux raccourci s'appelle le chromosome Philadelphie. À la jonction, un gène hybride stimule la division sans arrêt : "
        "un sous-clone de globules blancs prolifère. L'évolution clonale de la branche un, déclenchée cette fois par un remaniement. "
        "La diapositive de l'exposé parlait d'une mutation du chromosome vingt-deux : c'est en réalité une translocation entre le neuf et le vingt-deux.",
        "{-lmc}",
    ], vis={
        "def_tr": dict(type="def", terme="Translocation", cles=["autre paire", "non homologue"], x=170, y=190, w=940,
                       t="Un segment de chromosome se casse et va se fixer sur un chromosome non homologue, d'une autre paire."),
        "types_tr": dict(type="liste", titre="Deux types", x=150, y=180, w=980, items=[
            "Réciproque : deux chromosomes de paires différentes échangent un segment",
            "Robertsonienne : deux chromosomes à centromère terminal fusionnent en un seul"]),
        "tr_co": dict(type="cols", g="Crossing-over", gq="entre homologues, même paire : normal",
                      d="Translocation", dq="entre paires différentes : accident", vs="≠"),
        "il_tr": dict(type="illu", nom="transloc", x=110, y=70, w=1060, h=630),
        "prin_tr": dict(type="note", titre="Le principe", cles=["porte", "descendance"], x=170, y=200, w=940,
                        t="Rarement de conséquence pour le porteur ; mais des gamètes déséquilibrés, donc trisomie ou monosomie dans la descendance.",
                        etape="Trisomie 21 par translocation : quelques pour cent des cas (source hors cours)."),
        "lmc": dict(type="note", titre="Une translocation qui donne un cancer · hors programme", plus=True, cles=["Philadelphie", "sous-clone"], x=150, y=170, w=980,
                    t="Leucémie myéloïde chronique : translocation réciproque 9-22 dans une cellule de la moelle, chromosome Philadelphie, gène hybride, sous-clone qui prolifère.",
                    etape="Pas « une mutation du chromosome 22 », comme sur la diapositive de l'exposé."),
    }),

    # ================================================================ c1c · 4 · crossing-over inégal (★)
    dict(id="coinegal", chap="Le crossing-over inégal", fond="cellule", humeur="mystere",
         retenir="Crossing-over inégal : homologues appariés de façon décalée en prophase I, portions échangées de longueurs différentes. Gamètes : 2 normaux, 1 avec duplication, 1 avec délétion.",
         beats=[
        "{def_ci}{def_ci.1}Dernier accident : le crossing-over inégal. C'est un crossing-over au cours duquel les portions de chromatides échangées n'ont pas la même longueur. "
        "Il se produit en prophase un, quand deux homologues se sont appariés de façon décalée.",
        "{-def_ci}{an_ci}{pts_ci}{an_ci.1}{pts_ci.1}Deux chromosomes homologues, déjà répliqués. Ils portent le même gène, la bande dorée, au même emplacement. "
        "{an_ci.2}{pts_ci.2}En prophase un, ils s'apparient, mais de travers : le chromosome paternel est décalé, les deux gènes ne sont plus en face.",
        "{an_ci.3}{pts_ci.3}Deux chromatides non sœurs se croisent et échangent leurs segments, comme d'habitude. Mais à cause du décalage, la cassure ne tombe pas au même niveau. "
        "L'une récupère un segment plus long que celui qu'elle cède. L'autre, un plus court.",
        "{an_ci.4}{pts_ci.4}Après les deux divisions de la méiose, chaque chromatide se retrouve dans un gamète. Deux gamètes normaux. "
        "Un gamète porte une duplication : le gène en deux exemplaires sur le même chromosome. Et un gamète porte une délétion : le gène a disparu.",
        "Les conséquences sont très différentes. {-pts_ci}{-an_ci}{cons_ci}{cons_ci.g}Une délétion fait perdre un gène : c'est souvent néfaste. "
        "{cons_ci.d}Une duplication est souvent sans effet visible, puisque l'une des deux copies continue d'assurer la fonction. "
        "Et c'est précisément ce qui en fait une matière première pour l'évolution.",
        "{-cons_ci}{pa_ci}À toi : schéma étoilé. Dessine deux homologues mal appariés, le crossing-over inégal, puis les quatre gamètes : deux normaux, une duplication, une délétion.",
        "{pa_ci.stop}Le bilan des échanges de portions, en deux phrases. {-pa_ci}{bil_ech}{bil_ech.1}La translocation, entre chromosomes de paires différentes, est souvent sans effet chez le porteur, "
        "mais peut provoquer une trisomie ou une monosomie dans sa descendance. "
        "{bil_ech.2}Le crossing-over inégal, entre homologues mal appariés, produit des gamètes porteurs d'une délétion, ou d'une duplication de gènes.",
        "{-bil_ech}",
    ], vis={
        "def_ci": dict(type="def", terme="Crossing-over inégal", cles=["longueur", "décalée"], x=150, y=190, w=980,
                       t="Crossing-over où les portions de chromatides échangées n'ont pas la même longueur, en prophase I, entre homologues appariés de façon décalée."),
        "an_ci": dict(type="anim", nom="coinegal", x=40, y=72, h=624, seg=[[0, 5.9], [6, 13.9], [14, 24.9], [25, 32.9]]),
        "pts_ci": dict(type="liste", petit=True, titre="Le crossing-over inégal", x=680, y=110, w=560, items=[
            "Deux homologues, le même gène au même locus", "Prophase I : appariement décalé",
            "Échange de segments de longueurs différentes", "Gamètes : 2 normaux, 1 duplication, 1 délétion"]),
        "cons_ci": dict(type="cols", g="Délétion", gq="un gène perdu : souvent néfaste",
                        d="Duplication", dq="une copie de réserve : matière première de l'évolution", vs="≠"),
        "pa_ci": dict(type="pause", t="Deux homologues mal appariés, le crossing-over inégal, les quatre gamètes.",
                      sous="Schéma ★ à savoir refaire. Mets la vidéo sur pause, dessine-le, puis reprends."),
        "bil_ech": dict(type="liste", titre="Les échanges de portions de chromosomes", x=150, y=180, w=980, items=[
            "Translocation (paires différentes) : porteur sain, descendance à risque",
            "Crossing-over inégal (homologues décalés) : délétion ou duplication"]),
    }),

    # ================================================================ c1c · 5 · familles multigéniques : opsines (★)
    dict(id="famille", chap="Accidents et évolution · les familles multigéniques", fond="cellule", humeur="lumiere",
         retenir="Famille multigénique : gènes d'un même génome à plus de 20 % de similitudes, issus d'un gène ancestral par duplication (crossing-over inégal), mutations indépendantes, parfois transposition. Opsines S, M, L.",
         beats=[
        "{an_ci2}{pts_ci2}Suivons le gamète porteur de la duplication. {an_ci2.1}{pts_ci2.1}Son chromosome possède deux copies identiques du gène, au même endroit. "
        "Que deviennent-elles ? {an_ci2.2}{pts_ci2.2}Au fil des générations, chaque copie accumule des mutations différentes, indépendamment de l'autre. "
        "Leurs séquences restent proches, puisqu'elles partent du même gène, mais elles divergent peu à peu, et les protéines peuvent acquérir des fonctions différentes, ou complémentaires.",
        "{an_ci2.3}{pts_ci2.3}Une copie peut aussi être déplacée sur un autre chromosome : c'est une transposition. "
        "{an_ci2.4}{pts_ci2.4}Duplication, transposition, mutation : ce mécanisme crée de nouveaux gènes et enrichit le génome. C'est un mécanisme essentiel de sa complexification.",
        "{-pts_ci2}{-an_ci2}{def_fm}{def_fm.1}À noter, mot pour mot : une famille multigénique est un ensemble de gènes, au sein d'un même génome, qui présentent des homologies de séquence : "
        "plus de vingt pour cent de similitudes dans leur séquence nucléotidique. Ils sont issus d'un gène ancestral, par duplication, crossing-over inégal, puis mutations différentes, et parfois transposition.",
        "Par conséquent, ces gènes sont le plus souvent sur un même chromosome, ou sur deux s'il y a eu transposition. Et les protéines qu'ils codent sont homologues aussi : "
        "plus de vingt pour cent de similitudes entre leurs séquences d'acides aminés, une structure tridimensionnelle proche, globalement les mêmes fonctions.",
        "{-def_fm}{vingt}Pourquoi vingt pour cent ? {vingt.1}Il existe vingt acides aminés. Si l'on compare deux protéines sans aucun lien de parenté, le hasard seul fait coïncider environ une position sur vingt : "
        "cinq pour cent. {vingt.2}Au-delà de vingt pour cent de ressemblance, le hasard ne suffit plus : les deux séquences dérivent d'un ancêtre commun. C'est ce seuil qui permet de parler d'homologie, donc de parenté.",
        "{-vingt}{ops}Premier exemple, celui du cours : les opsines, les protéines qui captent la lumière dans les cellules de la rétine. Chez l'humain, trois opsines permettent de distinguer les couleurs. "
        "Elles ont plus de quarante pour cent de similitudes : une famille multigénique. Voici leur histoire. {ops.1}Un gène ancestral unique a été dupliqué.",
        "{ops.2}Une copie a été transposée sur un autre chromosome, le sept. {ops.3}Elle a accumulé ses propres mutations : c'est le gène de l'opsine S, pour short, qui absorbe surtout le bleu. "
        "{ops.4}Beaucoup plus tard, un nouveau crossing-over inégal a dédoublé le gène resté sur le chromosome X : deux gènes voisins, qui ont divergé. Les opsines M et L, pour medium et long : le vert et le rouge.",
        "{ops.5}Résultat : là où un seul pigment existait, trois pigments absorbent des longueurs d'onde différentes, ce qui améliore la perception des couleurs. "
        "Un accident génétique est à l'origine de notre vision trichromatique.",
        "{-ops}{mn}Un détail d'écriture : les trois opsines se notent S, M et L, pour courte, moyenne et longue longueur d'onde absorbée. Sur un schéma, ne note pas N à la place de M.",
        "{-mn}{pa_fm}À toi : le dernier schéma étoilé de la branche. Dessine la formation d'une famille multigénique : un gène ancestral, sa duplication par crossing-over inégal, "
        "une transposition, des mutations sur chaque copie. Puis applique-le aux opsines.",
        "{pa_fm.stop}{-pa_fm}",
    ], vis={
        "an_ci2": dict(type="anim", nom="coinegal", x=40, y=72, h=624, seg=[[33, 40.9], [41, 52.9], [53, 60.9], [61, 67.5]]),
        "pts_ci2": dict(type="liste", petit=True, titre="Duplication, mutation, transposition", x=680, y=110, w=560, items=[
            "Deux copies identiques, côte à côte", "Des mutations différentes sur chaque copie : divergence",
            "Une copie transposée sur un autre chromosome", "Une famille multigénique"]),
        "def_fm": dict(type="def", terme="Famille multigénique", cles=["20 %", "ancestral"], x=130, y=170, w=1020,
                       t="Ensemble de gènes d'un même génome qui présentent plus de 20 % de similitudes dans leur séquence nucléotidique.",
                       etape="Issus d'un gène ancestral : duplication par crossing-over inégal, mutations différentes, parfois transposition."),
        "vingt": dict(type="formule", titre="Pourquoi le seuil de 20 % ?", x=200, y=170, w=880, lignes=[
            dict(f="20 acides aminés : au hasard, 1 position sur 20 coïncide, soit 5 %", taille=34),
            dict(f="> 20 % de similitudes : une origine commune, une homologie", cadre=True, taille=36)]),
        "ops": dict(type="illu", nom="opsines", x=140, y=80, w=1000, h=620),
        "mn": dict(type="note", titre="S, M, L", cles=["M"], x=170, y=220, w=940,
                   t="Short, medium, long : opsines S (bleu), M (vert), L (rouge). Pas de « N »."),
        "pa_fm": dict(type="pause", t="Gène ancestral, duplication, transposition, mutations : la famille multigénique, puis les opsines.",
                      sous="Schéma ★ à savoir refaire. Mets la vidéo sur pause, dessine-le, puis reprends."),
    }),

    # ================================================================ c1c · 6 · le TP globines
    dict(id="globines", chap="Le TP : la famille des globines", fond="cellule", humeur="calme",
         retenir="Globines : > 20 % de similitudes (≈ 41 % minimum en nucléotides, 22 % en acides aminés), même structure 3D, même fonction, gènes regroupés sur les chromosomes 16 et 11. Chaque nœud de l'arbre = une duplication.",
         beats=[
        "{glob}Second exemple, celui du TP : les globines. {glob.1}Les hémoglobines, qui transportent le dioxygène dans les hématies, sont faites de quatre chaînes, les globines. "
        "{glob.2}Leurs gènes forment deux groupes : le groupe alpha sur le chromosome seize, le groupe bêta sur le chromosome onze, rangés dans l'ordre de leur expression. "
        "{glob.3}Car les globines exprimées changent au cours de la vie : zêta et epsilon chez l'embryon ; alpha et gamma chez le fœtus ; alpha et bêta chez l'adulte, très majoritaires, avec un peu de delta.",
        "La stratégie, rédigée comme à l'épreuve pratique. {-glob}{strat}{strat.1}On cherche à montrer que les gènes des globines appartiennent à une famille multigénique. "
        "{strat.2}On compare donc, avec Geniegen deux, les séquences nucléotidiques et les séquences d'acides aminés des globines alpha, bêta, delta, gamma, epsilon et de la myoglobine. "
        "{strat.3}Si c'est une famille multigénique, on s'attend à plus de vingt pour cent de similitudes entre toutes les séquences, deux à deux. "
        "Et attention : les deux types de séquences, et pas l'un ou l'autre. Sinon la démonstration est à moitié faite.",
        "Pour communiquer, la correction du TP insiste sur un point : ne recopie pas le tableau brut du logiciel. Fais un tableau titré, qui ne retient que l'essentiel. "
        "{-strat}{res}{res.1}D'après une copie d'élève : environ cinquante-sept pour cent entre alpha et bêta, quatre-vingt-treize entre bêta et delta, {res.2}de soixante-dix-huit à quatre-vingt-quatre entre epsilon et les autres du groupe bêta, "
        "{res.3}de quarante et un à quarante-six entre la myoglobine et les globines. {res.4}Toutes les similitudes dépassent vingt pour cent : au moins quarante et un pour cent en nucléotides, vingt-deux en acides aminés. "
        "Ces ressemblances ne peuvent pas être dues au hasard : origine commune.",
        "{-res}{an_gl}{pts_gl}Reste à raconter cette histoire. {an_gl.1}{pts_gl.1}Au départ, un seul gène de globine. Il est dupliqué, {an_gl.2}{pts_gl.2}puis une copie est transposée sur un autre chromosome. "
        "Le premier nœud de l'arbre porte donc duplication plus transposition.",
        "{an_gl.3}{pts_gl.3}Chaque copie accumule ses mutations, puis de nouvelles duplications ont lieu sur le même chromosome, sans transposition : les gènes restent voisins. "
        "C'est le futur chromosome onze, le groupe bêta. Sur l'autre chromosome, le gène se duplique lui aussi, sur place : ce sera le groupe alpha, sur le chromosome seize. "
        "{an_gl.4}{pts_gl.4}On aboutit aux deux groupes, et à l'arbre de parenté.",
        "L'arbre de la correction, construit à partir des séquences nucléotidiques. {-pts_gl}{-an_gl}{arbre}{arbre.1}Le premier nœud sépare la myoglobine de toutes les globines : duplication plus transposition. "
        "{arbre.2}Le nœud qui sépare alpha, sur le seize, du groupe bêta, sur le onze : duplication plus transposition, lui aussi. "
        "{arbre.3}Les nœuds internes du groupe bêta, gamma et epsilon d'un côté, delta et bêta de l'autre : duplication seule. Ces gènes sont restés côte à côte sur le onze.",
        "{arbre.4}Ce que signifie chaque nœud : une duplication génique, avec ou sans changement de chromosome. Un nœud ne porte jamais une transposition seule. "
        "Et des mutations sont notées sur chaque branche, après chaque nœud.",
        "La conclusion de la correction rassemble quatre types d'arguments, et c'est ce qui la rend complète. "
        "{-arbre}{concl}{concl.1}Les séquences : plus de vingt pour cent de similitudes, nucléotidiques et protéiques. {concl.2}La structure tridimensionnelle : les chaînes sont presque superposables. "
        "{concl.3}La fonction : toutes transportent le dioxygène, à des moments différents de la vie. {concl.4}La localisation : des gènes regroupés sur les chromosomes seize et onze. "
        "Les globines forment bien une famille multigénique, issue d'une globine ancestrale par duplications, mutations et transpositions.",
        "{-concl}{myo}Un point douteux de la correction : elle place la myoglobine sur le chromosome vingt. Les bases de données de génétique humaine indiquent le chromosome vingt-deux. "
        "Ça ne change rien au raisonnement. Au bac, c'est la donnée du sujet qui fait foi. "
        "Et hors programme : les gènes notés psi, sur la carte des chromosomes, sont des pseudogènes, des copies devenues incapables de produire une protéine. Des fossiles moléculaires.",
        "{-myo}",
    ], vis={
        "glob": dict(type="liste", titre="Les globines", x=130, y=140, w=1020, items=[
            "Hémoglobine : quatre chaînes, les globines, qui transportent le dioxygène",
            "Groupe alpha : chromosome 16 · groupe bêta : chromosome 11, dans l'ordre d'expression",
            "Embryon ζ, ε · fœtus α, γ · adulte α, β (97 %), un peu de δ"]),
        "strat": dict(type="liste", titre="TP · la stratégie", x=130, y=150, w=1020, items=[
            "Montrer que les gènes des globines forment une famille multigénique",
            "Comparer avec Geniegen2 les séquences nucléotidiques ET protéiques (α, β, δ, γ, ε, myoglobine)",
            "Attendu : plus de 20 % de similitudes, deux à deux"]),
        "res": dict(type="formule", titre="Similitudes nucléotidiques (une copie d'élève)", x=150, y=110, w=980, lignes=[
            dict(f="α / β ≈ 57 %  ·  β / δ ≈ 93 %", taille=34),
            dict(f="ε / autres globines du groupe bêta : 78 à 84 %", taille=34),
            dict(f="myoglobine / globines : 41 à 46 %", taille=34),
            dict(f="toutes > 20 % (protéines : ≥ 22 %) : origine commune", cadre=True, taille=34, n="valeurs à revérifier sur Geniegen2")]),
        "an_gl": dict(type="anim", nom="globines", x=40, y=72, h=624, vit=1.4, seg=[[0, 13.9], [14, 21.9], [22, 47.9], [48, 61.5]]),
        "pts_gl": dict(type="liste", petit=True, titre="L'histoire des globines", x=680, y=110, w=560, items=[
            "Un gène ancestral, dupliqué", "Une copie transposée : duplication + transposition",
            "Mutations, puis duplications sur place", "Deux groupes de gènes, un arbre"]),
        "arbre": dict(type="formule", titre="L'arbre de la correction", x=120, y=110, w=1040, lignes=[
            dict(f="((((γ, ε), (δ, β)), α), myoglobine)", taille=40, cadre=True),
            dict(f="myoglobine | globines : duplication + transposition", taille=30),
            dict(f="α (chr. 16) | groupe bêta (chr. 11) : duplication + transposition", taille=30),
            dict(f="nœuds du groupe bêta : duplication seule ; mutations sur chaque branche", taille=30)]),
        "concl": dict(type="liste", titre="La conclusion : quatre types d'arguments", x=130, y=140, w=1020, items=[
            "Séquences : > 20 % de similitudes, nucléotides et acides aminés", "Structure 3D : chaînes presque superposables",
            "Fonction : le transport du dioxygène, à différents âges", "Localisation : gènes regroupés sur les chromosomes 16 et 11"]),
        "myo": dict(type="note", titre="Points à vérifier", cles=["22", "pseudogènes"], x=170, y=180, w=940,
                    t="La correction place la myoglobine sur le chromosome 20 ; les bases de données disent 22. Au bac, la donnée du sujet fait foi.",
                    etape="Hors programme : les gènes ψ sont des pseudogènes, copies devenues non fonctionnelles."),
    }),

    # ================================================================ c1c · 7 · avantage sélectif : l'amylase
    dict(id="amylase", chap="Duplications et avantage sélectif", fond="aube", humeur="calme",
         retenir="AMY1 : plusieurs copies identiques ; plus de copies, plus d'amylase. Régime riche en amidon → pression de sélection → plus de copies en moyenne. Jamais l'inverse, jamais « pour ».",
         beats=[
        "{amy_doc}Les duplications peuvent-elles être avantageuses ? {amy_doc.1}L'exemple du cours : l'amylase salivaire, une enzyme qui commence la digestion de l'amidon dès la bouche. "
        "{amy_doc.2}Sa quantité dans la salive varie beaucoup d'un individu à l'autre : on l'a vu en analysant la salive de cinquante personnes. "
        "{amy_doc.3}Les banques de données détectent trois gènes de l'amylase salivaire, AMY un, aux séquences codantes identiques : trois copies d'un même gène, issues de duplications.",
        "{-amy_doc}{il_amy}{il_amy.1}Et chez les individus étudiés, le nombre de copies n'est pas le même. {il_amy.2}Un individu en a peu, {il_amy.3}un autre beaucoup. "
        "{il_amy.4}Plus un individu possède de copies, plus il produit d'amylase.",
        ("P", 1.5),
        "Ce lien a une portée évolutive. Les populations à l'alimentation traditionnellement riche en amidon, céréales ou tubercules, ont en moyenne plus de copies que les autres. "
        "Cette comparaison de populations, publiée en deux mille sept, vient de sources extérieures au cours. Le raisonnement est celui de la sélection naturelle. "
        "{-il_amy}{sel}{sel.1}Les duplications d'AMY un sont survenues au hasard, par accident génétique : le nombre de copies varie entre individus. "
        "{sel.2}Là où l'on mange beaucoup d'amidon, ceux qui ont plus de copies digèrent mieux, en tirent plus d'énergie : un avantage sélectif. "
        "{sel.3}Ils survivent et se reproduisent davantage, et transmettent leurs copies. Au fil des générations, le nombre moyen de copies augmente.",
        "{-sel}{causal}Attention au sens de la causalité. N'écris pas : s'ils ont beaucoup de gènes de l'amylase, alors leur régime consomme plus d'amidon. C'est l'inverse. "
        "C'est le régime alimentaire de la population qui a créé une pression de sélection, favorable aux porteurs de nombreuses copies. "
        "Et jamais de formulation finaliste : les gènes ne se sont pas dupliqués pour digérer l'amidon.",
        "{-causal}",
    ], vis={
        "amy_doc": dict(type="liste", titre="L'amylase salivaire", x=130, y=160, w=1020, items=[
            "Une enzyme qui commence la digestion de l'amidon dès la bouche",
            "Sa quantité varie beaucoup d'un individu à l'autre (salive de 50 personnes)",
            "Trois gènes AMY1 aux séquences codantes identiques : des copies issues de duplications"]),
        "il_amy": dict(type="illu", nom="amylase", x=140, y=100, w=1000, h=560),
        "sel": dict(type="liste", titre="Le raisonnement de la sélection naturelle", x=130, y=150, w=1020, items=[
            "Duplications au hasard : le nombre de copies d'AMY1 varie entre individus",
            "Régime riche en amidon : plus de copies, meilleure digestion, avantage sélectif",
            "Plus de survie et de descendants : le nombre moyen de copies augmente"]),
        "causal": dict(type="note", titre="Le sens de la causalité", cles=["régime", "pression"], x=170, y=190, w=940,
                       t="Le régime de la population crée une pression de sélection. Le nombre de copies ne choisit pas ce qu'on mange.",
                       etape="Et jamais : « les gènes se sont dupliqués pour digérer l'amidon »."),
    }),

    # ================================================================ c1c · 8 · remaniements et spéciation
    dict(id="speciation", chap="Remaniements chromosomiques et spéciation", fond="foret", humeur="mystere",
         retenir="Humain (2n = 46) et chimpanzé (2n = 48) : fusion (chromosome 2), inversions, additions. Des remaniements accumulés → hybrides peu fertiles → barrière → spéciation, à partir d'un ancêtre commun.",
         beats=[
        "{tab_chimp}Dernier rôle des accidents : la naissance des espèces. Comparons les caryotypes de l'humain, deux n égale quarante-six, et du chimpanzé, deux n égale quarante-huit.",
        "{-tab_chimp}{il_fus}Leurs chromosomes sont très semblables, bande par bande. {il_fus.1}Mais ils diffèrent par plusieurs remaniements. "
        "Une fusion : ces deux chromosomes distincts du chimpanzé, {il_fus.2}soudés bout à bout, correspondent à un seul chromosome chez l'humain, le chromosome deux. "
        "{il_fus.3}C'est ce qui explique le passage de quarante-huit à quarante-six.",
        "{il_fus.4}Des inversions : un segment s'est retourné, et l'ordre des gènes y est inversé. Et enfin, des additions de portions d'ADN sur certains chromosomes.",
        "{-il_fus}{mots_sp}Trois mots clés. {mots_sp.1}Un remaniement chromosomique : une modification de la structure des chromosomes, fusion, inversion, translocation, addition ou perte d'un segment. "
        "{mots_sp.2}Une barrière entre populations : un obstacle qui empêche les échanges génétiques entre deux groupes d'une même espèce. Géographique, une montagne, un bras de mer, ou génétique. "
        "{mots_sp.3}La spéciation : le processus par lequel de nouvelles espèces apparaissent à partir d'une espèce d'origine.",
        "Pourquoi ces remaniements comptent-ils ? {-mots_sp}{pourquoi}{pourquoi.1}Quand une population accumule des remaniements, ses chromosomes deviennent différents de ceux des populations voisines. "
        "{pourquoi.2}Chez un éventuel hybride, les chromosomes hérités des deux parents ne sont plus parfaitement homologues : ils s'apparient mal en prophase un, et la méiose produit des gamètes déséquilibrés. "
        "{pourquoi.3}L'hybride est peu fertile, ou stérile : les échanges génétiques cessent. Une barrière, ici génétique, s'est installée. "
        "{pourquoi.4}Ajoutés à l'éloignement géographique et au temps, ces remaniements font diverger les populations, jusqu'à des espèces distinctes : c'est la spéciation.",
        "{-pourquoi}{anc}Une phrase interdite : l'humain ne descend pas du chimpanzé. Le chimpanzé est une espèce actuelle, aussi évoluée que la nôtre. "
        "Les deux descendent d'un ancêtre commun, il y a environ six à sept millions d'années, et chaque lignée a accumulé ses propres remaniements.",
        "{-anc}{cicatr}Hors programme : la fusion du chromosome deux a laissé sa cicatrice. Au milieu du chromosome deux humain, on trouve des séquences de télomères placées tête-bêche, "
        "et les restes d'un second centromère, devenu inactif. Exactement ce que laisserait la soudure de deux chromosomes par leurs extrémités.",
        "{-cicatr}{bil_acc}Le bilan de la branche. {bil_acc.1}Les accidents génétiques de la méiose sont rares et aléatoires : la plupart sont néfastes, quelques-uns enrichissent le génome. "
        "{bil_acc.2}Les duplications créent les familles multigéniques, et la sélection naturelle peut les retenir. "
        "{bil_acc.3}Les remaniements chromosomiques peuvent isoler des populations et participer à la spéciation.",
        "{-bil_acc}",
    ], vis={
        "tab_chimp": dict(type="tableau", img="ch1-chimpanze", de=[1.0, .5, .45], a=[1.25, .5, .4],
                          legende="Chimpanzé, photo Tony Hisgett, CC BY 2.0 (Wikimedia Commons)"),
        "il_fus": dict(type="illu", nom="fusion", x=140, y=90, w=1000, h=580),
        "mots_sp": dict(type="liste", titre="Les mots clés", x=130, y=140, w=1020, items=[
            "Remaniement chromosomique : fusion, inversion, translocation, addition, perte d'un segment",
            "Barrière entre populations : géographique ou génétique",
            "Spéciation : apparition de nouvelles espèces à partir d'une espèce d'origine"]),
        "pourquoi": dict(type="liste", titre="Des remaniements à la spéciation", x=130, y=130, w=1020, items=[
            "Une population accumule des remaniements", "Chez l'hybride : appariement difficile en prophase I, gamètes déséquilibrés",
            "Hybride peu fertile ou stérile : une barrière génétique", "Avec l'isolement et le temps : deux espèces"]),
        "anc": dict(type="note", titre="Phrase interdite", cles=["ancêtre"], x=170, y=200, w=940,
                    t="L'humain ne descend pas du chimpanzé : les deux descendent d'un ancêtre commun, il y a 6 à 7 millions d'années."),
        "cicatr": dict(type="note", titre="La cicatrice du chromosome 2 · hors programme", plus=True, cles=["télomères", "centromère"], x=170, y=190, w=940,
                       t="Au milieu du chromosome 2 humain : des télomères tête-bêche et un second centromère inactif."),
        "bil_acc": dict(type="liste", titre="Accidents génétiques et évolution", x=130, y=170, w=1020, items=[
            "Rares, aléatoires, le plus souvent néfastes", "Duplications → familles multigéniques, retenues par la sélection",
            "Remaniements → barrières → spéciation"]),
    }),

    # ================================================================ c1d · séquençage et éthique (unité courte)
    dict(id="ethique", chap="Cadre théorique, limites éthiques", fond="aube", humeur="calme",
         retenir="Séquencer : lire l'enchaînement des nucléotides. Pour : gènes des maladies, prédiction (mucoviscidose), dépistage, DPI / DPN, justice. Contre : génotype incomplet, erreurs, données, eugénisme, fichage, brevets.",
         beats=[
        "{z1d}{z1d.1}Dernière branche, très courte : le cadre théorique et les limites éthiques. Elle vient d'un débat en classe, et ne tombera pas seule au bac. "
        "Il suffit de savoir donner deux ou trois arguments de chaque côté, avec un exemple.",
        "{-z1d}{tab_seq}{seq}Tout ce qu'on vient de voir construit le génotype d'un individu. Aujourd'hui, ce génotype se lit. "
        "{seq.1}Séquencer, c'est connaître l'enchaînement exact des nucléotides d'un ADN. {seq.2}Le premier génome humain a été achevé en avril deux mille trois, par le Human Genome Project : "
        "treize ans de travail, environ deux virgule sept milliards de dollars. {seq.3}Plus de soixante-dix millions d'euros par génome en deux mille un, environ cinq mille en deux mille treize, "
        "moins de mille dollars et quelques heures en deux mille dix-neuf. Possible parce que le génome est écrit avec quatre bases : un code qui se prête au traitement par ordinateur.",
        "{-seq}{-tab_seq}{pour}Les arguments pour. {pour.1}Trouver les gènes des maladies, en mettant en commun des milliers de séquences dans des bases de données mondiales. "
        "{pour.2}Prédire pour un enfant à venir : la mucoviscidose, due à des mutations du gène CFTR, la plus fréquente étant delta F cinq cent huit, soixante-six pour cent des allèles mutés. "
        "Deux parents sains hétérozygotes : un risque de un sur quatre pour chaque enfant. {pour.3}Dépister et prévenir : en deux mille treize, Angelina Jolie annonce une ablation préventive après un test génétique. "
        "{pour.4}Le diagnostic préimplantatoire et le diagnostic prénatal. {pour.5}La justice, avec le fichier national des empreintes génétiques, créé en mille neuf cent quatre-vingt-dix-huit.",
        "{-pour}{contre}Les arguments contre. {contre.1}Le génotype ne dit pas tout : il ignore l'environnement et le microbiote. "
        "{contre.2}L'ADN n'est pas la reine des preuves : chez 23andMe en deux mille dix, une plaque de quatre-vingt-seize échantillons retournée ; au moins onze erreurs judiciaires imputables à l'ADN aux États-Unis. "
        "{contre.3}Des données difficiles à protéger, et marchandisées. {contre.4}Le risque de dérive eugénique : la recherche de l'enfant parfait. "
        "{contre.5}Le fichage : plus d'un million et demi de personnes en France, avec des segments plus parlants que prévu. "
        "{contre.6}Et les brevets : Myriad Genetics détenait ceux de BRCA un et deux, jusqu'à ce que la Cour suprême des États-Unis tranche, en deux mille treize, que l'ADN en tant que tel ne se brevette pas.",
        "{-contre}{loi}{loi.1}Le cadre français : un particulier n'a pas le droit de demander son propre séquençage. L'examen n'est permis qu'à des fins médicales, de recherche, de paternité, ou dans une enquête criminelle. "
        "{loi.2}Il est fait par des praticiens agréés par l'Agence de la biomédecine, avec un accompagnement psychologique, et la CNIL contrôle la confidentialité des données.",
        "{-loi}",
    ], vis={
        "z1d": dict(type="mental", vers=["c1", "c1d"]),
        "tab_seq": dict(type="tableau", img="ch1-sequenceur", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Séquenceur Illumina MiSeq, photo Konrad Förstner, CC BY 2.0 (Wikimedia Commons)"),
        "seq": dict(type="liste", titre="Une technique devenue rapide et bon marché", x=130, y=140, w=1020, items=[
            "Séquencer : lire l'enchaînement exact des nucléotides", "Premier génome humain : avril 2003, Human Genome Project",
            "> 70 M€ (2001) → ≈ 5 000 € (2013) → < 1 000 $ en quelques heures (2019)"]),
        "pour": dict(type="liste", titre="Pour", x=130, y=110, w=1020, marques=["+", "+", "+", "+", "+"], items=[
            "Trouver les gènes des maladies (bases de données mondiales)", "Prédire : mucoviscidose, CFTR, ΔF508 (66 %), risque 1/4",
            "Dépister et prévenir : test BRCA1, Angelina Jolie (2013)", "DPI et DPN : éviter une maladie grave",
            "Justice : le FNAEG établit ou exclut un rapprochement"]),
        "contre": dict(type="liste", titre="Contre", x=130, y=90, w=1020, marques=["−", "−", "−", "−", "−", "−"], items=[
            "Le génotype ignore l'environnement et le microbiote", "Erreurs : 23andMe (2010), 11 erreurs judiciaires aux États-Unis",
            "Données mal protégées, marchandisation", "Dérive eugénique : l'« enfant parfait », le choix du sexe",
            "Fichage : 1,5 million de personnes en France", "Brevets sur les gènes : Myriad Genetics, tranché en 2013"]),
        "loi": dict(type="liste", titre="Le cadre de la loi française", x=130, y=180, w=1020, items=[
            "Pas de séquençage à la demande d'un particulier : fins médicales, recherche, paternité, enquête",
            "Praticiens agréés par l'Agence de la biomédecine ; la CNIL contrôle les données"]),
    }),

    # ================================================================ exercice type bac (inventé)
    # 408 + 402 = 810 parentaux (81 %) ; 92 + 98 = 190 recombinés (19 %) ; total 1 000
    dict(id="exobac", chap="Exercice type bac · un test-cross", fond="nuit", humeur="tension", beats=[
        "{exb}Pour finir, un exercice au format du bac. Il n'est pas dans ton cours : il est inventé pour la vidéo, sur le modèle des TP. "
        "Chez une plante, on étudie deux gènes. La couleur du fruit : rouge ou jaune. Sa forme : ronde ou allongée. "
        "On croise deux lignées pures, l'une à fruits rouges et ronds, l'autre à fruits jaunes et allongés. Toute la F1 a des fruits rouges et ronds.",
        "Puis on réalise un test-cross de la F1. Sur mille plantes : quatre cent huit à fruits rouges et ronds, quatre cent deux jaunes et allongés, "
        "quatre-vingt-douze rouges et allongés, quatre-vingt-dix-huit jaunes et ronds.",
        "Quatre questions. {exb.1}Un : quels allèles sont dominants ? Écris le génotype de la F1. {exb.2}Deux : pourquoi faire un test-cross, et avec quel partenaire ? "
        "{exb.3}Trois : les deux gènes sont-ils indépendants ou liés ? Justifie avec des pourcentages. "
        "{exb.4}Quatre : explique, par un schéma de la méiose, l'origine des fruits rouges et allongés.",
        "{-exb}{pa_exb}Prends quinze minutes. Mets sur pause, et rédige.",
        "{pa_exb.stop}{-pa_exb}{exbc}{exbc.q1}Correction. {s1}{s1.1}Question un : la F1 issue de deux lignées pures est uniforme, à fruits rouges et ronds. "
        "Rouge et rond sont donc dominants. {s1.2}La F1 est double hétérozygote. Si les gènes sont liés, on l'écrit R L sur r l, les deux allèles de chaque parent du même côté de la double barre.",
        "{-s1}{exbc.q2}{s2}{s2.1}Question deux : on croise la F1 avec un double homozygote récessif, à fruits jaunes et allongés. "
        "{s2.2}Il ne transmet que des allèles récessifs, qui ne masquent rien : les phénotypes des descendants révèlent directement les gamètes de la F1.",
        "{-s2}{exbc.q3}{s3}{s3.1}Question trois. Quatre phénotypes, mais pas quatre fois vingt-cinq pour cent. {s3.2}Les deux majoritaires reproduisent les parents : quatre cent huit plus quatre cent deux, "
        "huit cent dix sur mille, quatre-vingt-un pour cent de parentaux. {s3.3}Les deux minoritaires sont recombinés : cent quatre-vingt-dix, dix-neuf pour cent. "
        "{s3.4}Gamètes non équiprobables : les gènes sont partiellement liés, sur la même paire de chromosomes.",
        "{-s3}{exbc.q4}{s4}{s4.1}Question quatre. En prophase un, chez la F1, les homologues s'apparient en bivalent. {s4.2}Deux chromatides non sœurs se croisent, au niveau d'un chiasma situé entre les deux gènes, "
        "et échangent leurs segments. {s4.3}On obtient des chromatides recombinées, R l et r L. {s4.4}Le gamète R l, fécondé par un gamète r l du parent récessif, donne une plante à fruits rouges et allongés. "
        "Comme le crossing-over ne se produit pas dans toutes les cellules, ces recombinés restent minoritaires.",
        "{-s4}{-exbc}",
    ], vis={
        "exb": dict(type="exo", niveau="Exercice type bac", y=70, titre="Couleur et forme du fruit", src="Exercice inventé pour la vidéo, sur le modèle des TP 2 et 3",
                    enonce=["Lignée pure [rouge ; rond] × lignée pure [jaune ; allongé] → F1 100 % [rouge ; rond].",
                            "Test-cross de la F1, 1 000 plantes : 408 [rouge ; rond], 402 [jaune ; allongé], 92 [rouge ; allongé], 98 [jaune ; rond]."],
                    questions=["Allèles dominants, génotype de la F1.", "Pourquoi un test-cross ? Avec quel partenaire ?",
                               "Gènes indépendants ou liés ? Justifier par des pourcentages.",
                               "Expliquer par un schéma l'origine des plantes [rouge ; allongé]."]),
        "pa_exb": dict(type="pause", t="Dominance, test-cross, gènes liés ou non, schéma du crossing-over."),
        "exbc": dict(type="exo", mode="coin", niveau="Exercice type bac", titre="Couleur et forme du fruit",
                     donnees=["F1 [rouge ; rond]", "408 · 402 · 92 · 98 sur 1 000"],
                     questions=["Dominance, génotype F1 ?", "Pourquoi un test-cross ?", "Indépendants ou liés ?", "Origine des [rouge ; allongé] ?"]),
        "s1": dict(type="formule", titre="1 · Dominance et génotype", x=540, y=170, w=700, lignes=[
            dict(f="F1 uniforme [rouge ; rond] : R et L dominants", taille=32),
            dict(f="F1 : (R L // r l)", cadre=True, taille=40, n="gènes liés : allèles de chaque parent du même côté")]),
        "s2": dict(type="formule", titre="2 · Le test-cross", x=540, y=170, w=700, lignes=[
            dict(f="F1 × (r l // r l) [jaune ; allongé]", taille=34),
            dict(f="le récessif ne masque rien : phénotypes de la F2 = gamètes de la F1", cadre=True, taille=28)]),
        "s3": dict(type="formule", titre="3 · Indépendants ou liés ?", x=540, y=120, w=700, lignes=[
            dict(f="pas 4 × 25 %", taille=34, ko=True),
            dict(f="parentaux : (408 + 402) / 1 000 = 81 %", taille=32),
            dict(f="recombinés : (92 + 98) / 1 000 = 19 %", taille=32),
            dict(f="gamètes non équiprobables : gènes liés", cadre=True, ok=True, taille=32)]),
        "s4": dict(type="formule", titre="4 · L'origine des recombinés", x=540, y=110, w=700, lignes=[
            dict(f="prophase I : bivalent (R L // r l)", taille=32),
            dict(f="chiasma entre les deux gènes, chromatides non sœurs", taille=30),
            dict(f="chromatides recombinées : R l et r L", taille=32),
            dict(f="gamète R l + gamète r l → [rouge ; allongé]", cadre=True, taille=32)]),
    }),

    # ================================================================ récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="aube", humeur="lumiere", beats=[
        "{bac}Récapitulons ce que le bac peut te demander sur ce chapitre. {bac.1}Définir un clone, et citer ses cinq fonctions avec un exemple. "
        "{bac.2}Expliquer pourquoi la mitose conserve le caryotype, et lire un graphique de quantité d'ADN. "
        "{bac.3}Expliquer l'évolution clonale et la cancérisation, avec p53 et TERT, et distinguer somatique et germinale.",
        "{bac.4}Relier méiose et fécondation à la stabilité du caryotype. {bac.5}Énoncer les lois de Mendel, et faire un échiquier, avec les bonnes écritures. "
        "{bac.6}Expliquer les deux brassages, et interpréter un test-cross. "
        "{bac.7}Expliquer une trisomie, une translocation, un crossing-over inégal, et la formation d'une famille multigénique. "
        "{bac.8}Et donner deux arguments pour et deux contre le séquençage.",
        "Et les schémas étoilés de la carte, à savoir refaire sans modèle. {-bac}{schemas}{schemas.1}Le cycle méiose, fécondation. {schemas.2}Le brassage interchromosomique. "
        "{schemas.3}Le crossing-over. {schemas.4}La mauvaise disjonction, en anaphase un et en anaphase deux. {schemas.5}Le crossing-over inégal. "
        "{schemas.6}Et la famille multigénique, avec les opsines.",
        "{-schemas}",
        ("P", 0.8),
        "{carte_f}Reprends maintenant la carte. Le chapitre un, ce sont des transferts verticaux. {carte_f.1}Des mitoses qui conservent le génome et ses accidents, "
        "une méiose et une fécondation qui le brassent, des accidents qui l'enrichissent, et une technique qui permet de le lire.",
        "Le chapitre deux ouvre une autre voie, plus surprenante : des gènes échangés entre organismes non apparentés. Les transferts horizontaux. "
        "En attendant, les questions du quiz t'attendent, juste sous la vidéo.",
        "{-carte_f}",
    ], vis={
        "bac": dict(type="liste", titre="Pour le bac · à cocher", x=110, y=70, w=1060, petit=True, marques=["✓"] * 8, items=[
            "Clone : définition, cinq fonctions, un exemple (Pando, autogreffe)", "Mitose et caryotype ; graphique de la quantité d'ADN",
            "Évolution clonale, p53, TERT ; somatique ou germinale", "Méiose + fécondation : stabilité du caryotype",
            "Lois de Mendel, échiquier, écritures (A//O) et [A]", "Les deux brassages ; lire un test-cross",
            "Trisomie, translocation, crossing-over inégal, famille multigénique", "Séquençage : deux arguments pour, deux contre"]),
        "schemas": dict(type="liste", titre="Les schémas ★ à savoir refaire", x=150, y=110, w=980, marques=["★"] * 6, items=[
            "Le cycle méiose – fécondation (2n, n)", "Le brassage interchromosomique (deux orientations)",
            "Le crossing-over (brassage intrachromosomique)", "La mauvaise disjonction en anaphase I et en anaphase II",
            "Le crossing-over inégal : duplication et délétion", "La famille multigénique : les opsines"]),
        "carte_f": dict(type="mental", vers=["t1a"], vol=2.0),
    }),
]

QUIZ = [
    dict(q="Au cours d'un cycle cellulaire, qu'est-ce qui ne varie jamais ?",
         r=["La quantité d'ADN", "Le nombre de chromatides par chromosome", "Le nombre de chromosomes"], ok=2,
         ex="La phase S double les chromatides et l'ADN ; l'anaphase les sépare. Le nombre de chromosomes reste 2n.", voir="tab_cy"),
    dict(q="Une mutation de la séquence régulatrice du gène TERT…",
         r=["modifie la protéine TERT", "augmente la quantité de protéine TERT, normale", "empêche toute division"], ok=1,
         ex="La mutation est à côté du gène : la protéine est normale, mais surexprimée.", voir="tert"),
    dict(q="Une mutation somatique…", r=["est transmise aux enfants", "peut changer le phénotype de l'individu, mais n'est pas transmise", "touche les gamètes"], ok=1,
         ex="Somatique : cellule du corps, jamais transmise. Germinale : transmise à la descendance.", voir="som_ger"),
    dict(q="Le brassage interchromosomique est…",
         r=["préparé en prophase I", "préparé en métaphase I et effectué en anaphase I", "effectué en anaphase II"], ok=1,
         ex="Orientation aléatoire des paires en métaphase I, séparation des homologues en anaphase I.", voir="deux_v"),
    dict(q="Combien de gamètes différents un humain peut-il produire par le seul brassage interchromosomique ?",
         r=["46", "2 × 23", "2²³, environ 8 millions"], ok=2, ex="Deux possibilités par paire, 23 paires indépendantes : 2²³.", voir="deuxn"),
    dict(q="Le crossing-over a lieu…", r=["entre chromatides sœurs, en anaphase I", "entre chromatides non sœurs, en prophase I", "entre chromosomes de paires différentes"], ok=1,
         ex="Dans le bivalent, en prophase I ; entre sœurs, l'échange ne changerait rien.", voir="pts_me3"),
    dict(q="Un test-cross donne 40 %, 42,5 %, 7,5 % et 10 %. Les gènes sont…",
         r=["indépendants", "partiellement liés", "sur des chromosomes sexuels"], ok=1,
         ex="Deux classes majoritaires (parentaux) et deux minoritaires (recombinés) : gamètes non équiprobables, gènes liés.", voir="bar3"),
    dict(q="Une mauvaise disjonction en anaphase I donne…",
         r=["quatre gamètes anormaux", "deux gamètes anormaux et deux normaux", "quatre gamètes normaux"], ok=0,
         ex="Les deux homologues partent ensemble : deux gamètes n + 1 et deux n − 1.", voir="tab_nd"),
    dict(q="Un porteur sain d'une translocation 14-21 possède…",
         r=["47 chromosomes", "45 chromosomes, tous ses gènes en double", "46 chromosomes, un 21 en moins"], ok=1,
         ex="Le 21 est fixé sur le 14 : 45 chromosomes, mais aucun gène perdu.", voir="il_tr"),
    dict(q="Les gènes d'une famille multigénique…",
         r=["ont plus de 20 % de similitudes et dérivent d'un gène ancestral", "sont toujours sur des chromosomes différents", "codent la même protéine"], ok=0,
         ex="Duplication par crossing-over inégal, mutations indépendantes, parfois transposition : plus de 20 % de similitudes.", voir="def_fm"),
]

CREDITS = [
    "Photos (Wikimedia Commons) : Pando, Mx. Granger, CC0 ; chatte écaille de tortue, Kiiro, CC BY-SA 4.0 ; "
    "Gregor Mendel, photo publiée par Hugo Iltis, CC BY 4.0 ; fleur de pois, Dyorkey, CC BY-SA 3.0 ; "
    "tubes de drosophiles, Masur, CC BY-SA 4.0 ; chromosomes d'une cellule 47, XY, +21, Josef Reischig, CC BY-SA 3.0 ; chimpanzé, Tony Hisgett, CC BY 2.0 ; séquenceur Illumina MiSeq, Konrad Förstner, CC BY 2.0.",
    "Animations et schémas : faits pour le site. Exercice type bac inventé pour la vidéo. "
    "Fréquences des trisomies, trisomie 21 par translocation, comparaison des populations pour AMY1 : sources extérieures au cours, signalées.",
]
