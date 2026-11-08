"""Histoire · chapitre 2 « Les régimes totalitaires » — série vidéo, édition française, épisode 3 :
« Trois régimes, trois idéologies » (partie I.3 du cours, « Les spécificités de chaque régime », quinze idées).

Édition française de h2_3.py (cahier des charges : EDITION_FR.md ; l'anglais est gardé intact) : histoire-géographie
classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes visuels, mêmes repères,
mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H2 : 7 putsch manqué, Mein Kampf · 8 fascisme, la dictature rendue légale · 12 stalinisme, plan et collectivisation ·
       14 une terreur moins oppressive ? puis le tournant raciste · 15 les koulaks · 19 l'Holodomor ·
       23 nazisme, la lutte des races
Adaptations : Worksheet 2 → le dossier documentaire sur la collectivisation (sources → documents 1, 2, 4, 5) ; paragraphe
d'essay « Explain how » → paragraphe de réponse à une question problématisée ; « synthesis grid » → le tableau de
synthèse du cours. Noms sous leur graphie française (Guépéou pour l'OGPU, Kaganovitch, Ordjonikidze, Chalamov),
« placed on the blackboard » → « inscrits au tableau noir » (l'expression de Nicolas Werth). Citations de la Doctrine
du fascisme (1932), de Staline (7 janvier 1933) et de la lettre de Feigin (9 avril 1932) traduites au plus près des
phrases citées par le cours. Faits identiques à l'anglais ; dit « hors du cours » comme dans l'anglais : bilan d'environ
quatre millions de morts de l'Holodomor, relégation à Lipari, déportation des koulaks vers la Sibérie et le Kazakhstan,
« grand tournant » de la fin 1929, 1,8 million de koulaks déportés. Correction du cours : Matteotti tué en 1924.
Chaîne : outils/serie-philo/generer.py h2f_3 ; sortie dans dnl/serie/ (h2f-3.*).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-3"
NOTION = "Les régimes totalitaires"
NUM = 3
TITRE = "Trois régimes, trois idéologies"
SUIVANT = "Épisode 4 · Le chef, le parti et l'homme nouveau"
PRONONCIATION = {"Matteotti": "Mat-té-otti", "Duce": "Dou-tché", "Führer": "Fu-reur", "Gentile": "Djenn-tilé",
                 "Giacomo": "Dja-ko-mo", "Giovanni": "Djo-vanni", "fascistissimes": "fa-chis-tis-si-mé",
                 "Mostra della Rivoluzione Fascista": "Mosstra dèla Rivolou-tsio-né Fa-chis-ta",
                 "La Difesa della Razza": "La Di-fé-za dèla Rat-tsa", "Benigni": "Bé-ni-nyi",
                 "koulak": "kou-lak", "koulaks": "kou-lak", "Holodomor": "Ho-lo-do-mor",
                 "Ordjonikidze": "Or-djo-ni-kid-zé", "Feigin": "Féi-guine", "Werth": "Vèrt",
                 "Novossibirsk": "No-vo-si-birsk", "Der Giftpilz": "Dèr Guift-pilts", "Bauer": "Baou-eur",
                 "Elvira": "Èl-vi-ra", "Mein Kampf": "Maïne Kampf", "Arendt": "A-rennte", "Bamberg": "Bamm-bèrg",
                 "SA": "èss-a"}

# dossier documentaire, document 2 : part des foyers paysans collectivisés (h2collect)
COLLECT = [(1928, 7), (1929, 15), (1930, 57), (1936, 90)]


def barres_collect():
    """Barres verticales (droites épaisses, comme dans h3_4) : l'année sous l'axe, la valeur au-dessus de la barre."""
    el = [dict(type="texte", x=i, y=-8, t=str(an), c="iv") for i, (an, _) in enumerate(COLLECT, start=1)]
    for i, (an, v) in enumerate(COLLECT, start=1):
        el.append(dict(type="droite", pts=[[i, 4.5], [i, max(5, v - 4.5)]], c="sa", ep=46, dur=1.0,
                       lbl=f"{v} %", lp=[i, v + 7]))
    el.append(dict(type="texte", x=2.5, y=78, t="1929-1930 : la contrainte, pas le consentement", c="ca"))
    return el


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Trois régimes. Chacun avec un parti unique, un chef, une police et une propagande.",
        "{-q1}{q2}Et pourtant, ils ne voulaient pas la même chose. Mussolini rêvait de la nation. Hitler, de la race. Staline, de la classe.",
        "{-q2}{q3}Alors, qu'est-ce qui rend chacun d'eux singulier ? Et pourquoi cette différence compte-t-elle autant ? Parce que le but décide "
        "de qui est l'ennemi. Et l'ennemi décide de qui sont les victimes.",
        "{-q3}{-g0}{plan}Voici le plan. {plan.1}D'abord, l'histoire sur la carte. {plan.2}Puis le fascisme, avec la nation et l'État. "
        "{plan.3}Puis le stalinisme : la classe, la collectivisation et la famine. {plan.4}Puis le nazisme, et la race. "
        "{plan.5}Ensuite, la comparaison, avec le tableau de synthèse du cours. {plan.6}Et enfin, à toi, avec un paragraphe de composition.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[0]),
        "q1": dict(type="question", t="Une même méthode de pouvoir…", bande=True),
        "q2": dict(type="question", t="… trois buts différents : la nation, la race, la classe.", bande=True),
        "q3": dict(type="question", t="Le but décide de l'ennemi.", bande=True),
        "plan": dict(type="liste", titre="Épisode 3 · partie I.3 du cours", items=[
            "L'histoire sur la carte : 1923 – 1939", "Le fascisme : la nation et l'État absolu",
            "Le stalinisme : lutte des classes, collectivisation, Holodomor", "Le nazisme : la lutte des races",
            "La comparaison : le tableau de synthèse du cours", "À toi : un paragraphe de composition"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 3", t="Trois régimes, trois idéologies",
                      sous="Fascisme · stalinisme · nazisme · partie I.3 du cours"),
    }),

    # ================================================================ la carte (1) : 1923-1938
    dict(id="carte1", chap="Sur la carte : Rome et Moscou", fond="nuit", humeur="tension",
         retenir="1924-1925 : Matteotti assassiné, les lois « fascistissimes » · 1928 : le premier plan quinquennal · 1929 : les accords du Latran · 1938 : l'Italie fasciste devient raciste.",
         beats=[
        "{g1}Suivons d'abord l'histoire sur la carte. {g1.1}Novembre mille neuf cent vingt-trois, à Munich. Le coup de force de Hitler échoue. "
        "En prison, il écrit Mein Kampf. Ses idées racistes sont donc sur le papier dix ans avant sa prise du pouvoir.",
        "{g1.2}Pendant ce temps, à Rome, Mussolini gouverne depuis mille neuf cent vingt-deux. En mille neuf cent vingt-quatre, le député socialiste Matteotti est enlevé et assassiné. "
        "En janvier mille neuf cent vingt-cinq, Mussolini en revendique la responsabilité. Puis les lois fascistissimes font de l'Italie un État totalitaire.",
        "{g1.3}Direction l'Union soviétique, où Staline gouverne depuis mille neuf cent vingt-quatre. En mille neuf cent vingt-huit, il lance le premier plan quinquennal. "
        "Ses cibles : l'industrie, et la collectivisation forcée des campagnes.",
        "{g1.4}Retour en Italie. En mille neuf cent vingt-neuf, Mussolini signe un accord avec le pape : les accords du Latran. "
        "Et le fascisme n'est pas raciste. Pas avant mille neuf cent trente-huit, quand Mussolini s'allie à Hitler.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[7, 8, 12, 14]),
    }),

    # ================================================================ la carte (2) : 1929-1939
    dict(id="carte2", chap="Sur la carte : les campagnes et la race", fond="nuit", humeur="tension",
         retenir="1929-1932 : les koulaks, ennemis de classe · 1932-1933 : l'Holodomor en Ukraine · 1933-1939 : la lutte des races nazie, l'enseignement racial (1933), T4 (1939).",
         beats=[
        "{g2}{g2.1}Dans les campagnes soviétiques, à partir de mille neuf cent vingt-neuf, tout paysan qui résiste à la collectivisation est déclaré koulak. Un ennemi de classe. "
        "Ses terres et ses bêtes sont confisquées, et beaucoup sont déportés.",
        "{g2.2}En mille neuf cent trente-deux et trente-trois, en Ukraine, le grain est pris quelle que soit la récolte. Les villages qui résistent sont privés de tout ravitaillement. "
        "Le résultat est une famine provoquée par l'homme : l'Holodomor.",
        "{g2.3}Et en Allemagne, à partir de mille neuf cent trente-trois, les nazis font de leur lutte des races des lois, et des leçons d'école. "
        "En mille neuf cent trente-neuf, ils en font le meurtre d'Allemands handicapés.",
        "{-g2}{fr}Voici donc les dates de cet épisode. {fr.1}Mille neuf cent vingt-quatre, Matteotti. {fr.2}Mille neuf cent vingt-cinq, les lois fascistissimes. {fr.3}Mille neuf cent vingt-huit, le Plan. {fr.4}Mille neuf cent vingt-neuf, l'Église. "
        "{fr.5}Mille neuf cent trente-deux, la Doctrine. {fr.6}Mille neuf cent trente-trois, les leçons raciales. {fr.7}Mille neuf cent trente-huit, le tournant raciste de l'Italie. {fr.8}Et mille neuf cent trente-neuf, T quatre. Mets la vidéo en pause pour les recopier.",
        ("P", 3.0),
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[15, 19, 23]),
        "fr": dict(type="frise", items=[
            dict(nom="Matteotti", d=1924, q="assassiné"), dict(nom="Lois fascistissimes", d=1925, q="Mein Kampf"),
            dict(nom="Plan quinquennal", d=1928, q="collectivisation"), dict(nom="Accords du Latran", d=1929, q="l'Église"),
            dict(nom="Doctrine du fascisme", d=1932, q="Mussolini et Gentile"), dict(nom="Enseignement racial", d=1933, q="écoles allemandes"),
            dict(nom="La Difesa della Razza", d=1938, q="l'Italie devient raciste"), dict(nom="T4", d=1939, q="Allemands handicapés")]),
    }),

    # ================================================================ trois idéologies
    dict(id="ideologie", chap="Qu'est-ce qu'une idéologie ?", fond="aube", humeur="calme",
         retenir="Une idéologie : un ensemble de croyances qui fixe un but suprême. Fascisme → la nation · nazisme → la race · stalinisme → la classe.",
         beats=[
        "{def1}Avant le cours, un mot à maîtriser. L'{!idéologie}idéologie. Tu connais la définition depuis l'épisode un : "
        "un ensemble de croyances qui fixe un but suprême à atteindre. {def1.1}Et un but suprême justifie tous les moyens.",
        "{-def1}{trois}{trois.1}Voici les trois buts suprêmes. Pour le fascisme, la nation, incarnée dans un État absolu. "
        "{trois.2}Pour le nazisme, la race. {trois.3}Pour le stalinisme, la classe. "
        "Garde ces trois mots en tête pendant tout l'épisode. La nation, la race, la classe.",
    ], vis={
        "def1": dict(type="def", cles=["croyances", "suprême"], terme="L'idéologie",
                     t="Un ensemble de croyances qui fixe un but suprême à atteindre.",
                     etape="Un but suprême justifie tous les moyens", x=170, y=200, w=940),
        "trois": dict(type="cartes", petit=True, items=[
            dict(t="Nation", q="Fascisme · l'État absolu"), dict(t="Race", q="Nazisme · une race pure"),
            dict(t="Classe", q="Stalinisme · une société sans classes")]),
    }),

    # ================================================================ fascisme, idée 1
    dict(id="fas1", chap="Le fascisme · une « nouvelle révolution »", fond="nuit", humeur="lumiere",
         retenir="Le fascisme : une « nouvelle révolution », ni libérale ni socialiste, pour transformer la civilisation et retrouver la gloire de Rome. Le calendrier fasciste : 1922 = an I.",
         beats=[
        "{photo1}{def2}Le fascisme d'abord. Idée un. Le fascisme se présente comme une {!nouvelle révolution}nouvelle révolution. Ni libérale, ni socialiste. "
        "{def2.1}Son but : transformer la civilisation italienne, et retrouver la grandeur de la Rome antique. "
        "Mussolini veut un peuple discipliné, guerrier, uni derrière l'État.",
        "{-def2}{an11}Et l'ambition est totale. L'histoire elle-même doit recommencer avec le fascisme. "
        "La preuve est dans le cours. C'est l'affiche de l'exposition de la révolution fasciste, la Mostra della Rivoluzione Fascista, "
        "à Rome, en mille neuf cent trente-deux. Et elle est datée de l'an onze. {an11.1}Pourquoi ? Parce que le calendrier fasciste part de mille neuf cent vingt-deux, l'année où Mussolini prend le pouvoir. "
        "L'an un. Une ère nouvelle.{-photo1}",
    ], vis={
        "photo1": dict(type="tableau", img="h2-mostra", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="L'exposition de la révolution fasciste, Rome : la salle consacrée à 1914 · Photographe inconnu, domaine public"),
        "def2": dict(type="def", cles=["révolution", "Rome"], terme="Le fascisme · une « nouvelle révolution »",
                     t="Ni libérale ni socialiste : transformer la civilisation italienne et retrouver la gloire de la Rome antique.",
                     etape="Un peuple discipliné, guerrier, uni derrière l'État", x=170, y=200, w=940),
        "an11": dict(type="cols", g="L'affiche", gq="Mostra della Rivoluzione Fascista, Rome, 1932 : « an XI »",
                     d="Le calendrier", dq="1922, la prise du pouvoir = an I", vs="=", repere="L'histoire recommence avec le fascisme"),
    }),

    # ================================================================ fascisme, idée 2
    dict(id="fas2", chap="Le fascisme · du meurtre à la dictature légale", fond="guerre", humeur="tension",
         retenir="Matteotti enlevé et tué, 10 juin 1924 · 3 janv. 1925 : Mussolini en revendique la responsabilité · 1925 : les lois « fascistissimes » · le roi reste, le Parlement ne compte plus.",
         beats=[
        "{g3}{g3.1}Idée deux. Une fois au pouvoir, Mussolini doit encore affronter la gauche. {mat}{mat.1}Giacomo Matteotti est un député socialiste. "
        "Au Parlement, il dénonce ouvertement la fraude électorale et la violence. Le dix juin mille neuf cent vingt-quatre, il est enlevé. Son corps est retrouvé plus tard.",
        "{mat.2}Le trois janvier mille neuf cent vingt-cinq, Mussolini parle devant la Chambre. Il revendique publiquement la responsabilité, et traite Matteotti d'ennemi de la paix. "
        "{mat.3}Puis viennent les lois fascistissimes, les lois les plus fascistes. Elles font de l'Italie un État totalitaire.",
        "{mat.4}C'est la fin de la monarchie parlementaire. Le roi reste. Mais le Parlement ne compte plus. "
        "{!La violence d'abord, puis la loi}La violence d'abord. Puis la loi.",
        "{-mat}{-g3}{att1}Un point à surveiller. Le cours date le meurtre de mille neuf cent vingt-cinq. {att1.1}En réalité, Matteotti a été enlevé et tué en juin mille neuf cent vingt-quatre. "
        "Mille neuf cent vingt-cinq, c'est l'année où le meurtre porte ses fruits. Dans ta copie, écris donc mille neuf cent vingt-quatre. Ou mille neuf cent vingt-quatre, vingt-cinq.",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[8]),
        "mat": dict(type="liste", titre="L'affaire Matteotti", petit=True, bande=True, x=40, y=120, w=540, items=[
            "10 juin 1924 : Matteotti, député socialiste, enlevé et tué", "3 janv. 1925 : Mussolini en revendique la responsabilité",
            "1925 : les lois « fascistissimes », un État totalitaire", "Le roi reste ; le Parlement ne compte plus"]),
        "att1": dict(type="note", terme="Attention · une date", cles=["1924"],
                     t="Le cours date le meurtre de 1925 : Matteotti a été tué en juin 1924.",
                     etape="1925 : la revendication et les lois fascistissimes · écris 1924, ou 1924-1925", x=170, y=200, w=940),
    }),

    # ================================================================ fascisme, idées 3, 4 et 5
    dict(id="doctrine", chap="Le fascisme · la Doctrine de 1932", fond="aube", humeur="calme",
         retenir="Doctrine du fascisme (Mussolini et Gentile, 1932) : « tout est dans l'État » · des nations, pas des classes · contre le parlementarisme, le libéralisme, le marxisme et les droits de l'homme · nationaliste, militariste.",
         beats=[
        "{photo2}{doc}Les idées trois, quatre et cinq viennent toutes d'un même texte, cité par le cours : la {!Doctrine du fascisme}Doctrine du fascisme. "
        "Elle est écrite en mille neuf cent trente-deux, par Mussolini et le philosophe Giovanni Gentile. {doc.1}L'idée trois porte sur le mot totalitaire. "
        "Aujourd'hui, c'est une accusation. Mais les fascistes l'employaient avec fierté. Pour eux, il désignait un État qui englobe tout.{-doc}",
        ("C", "tout est dans l'État… en ce sens, le fascisme est totalitaire", "c_doc1"),
        "{-c_doc1}{-photo2}{tot}Pour eux, totalitaire voulait dire complet, uni et fort. Le contraire d'une société libérale divisée. "
        "{tot.1}Le mot ne devient une accusation qu'après la guerre, quand des historiens et des philosophes, comme Hannah Arendt, "
        "l'appliquent au nazisme et au stalinisme.",
        "{-tot}{cl}{cl.g}Idée quatre. Le fascisme divise l'humanité en nations, pas en classes. Le marxisme dit que la société est divisée en classes, engagées dans une lutte. {cl.d}Le fascisme dit l'inverse. Ce qui divise l'humanité, ce sont les nations. Et dans la nation, toutes les classes doivent être unies "
        "sous l'État. La Doctrine attaque donc le socialisme, qui{-cl}",
        ("C", "enferme le mouvement de l'histoire dans la lutte des classes", "c_doc2"),
        "{-c_doc2}{ban}La lutte des classes est interdite. Voilà pourquoi les possédants qui craignaient le socialisme aimaient le fascisme. "
        "{-ban}Idée cinq. Pour le cours, le fascisme est le premier totalitarisme. Et il se définit par ce qu'il rejette. "
        "{contre}{contre.1}Il rejette le parlementarisme, le pouvoir des assemblées élues. {contre.2}Il ne croit pas aux droits de l'homme. "
        "{contre.3}Il est contre le libéralisme, et contre le marxisme aussi. {contre.4}Et il est nationaliste et militariste.",
        "{-contre}{ind}Le libéralisme part de l'individu, et de ses droits. Le fascisme part de l'État. Seul l'État donne sa valeur à l'individu. "
        "Selon les mots de la Doctrine,{-ind}",
        ("C", "le libéralisme niait l'État dans l'intérêt de l'individu particulier", "c_doc3"),
    ], vis={
        "photo2": dict(type="tableau", img="h2-mussolini", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Benito Mussolini, Duce de l'Italie fasciste, vers 1937-1940 · Keystone, domaine public"),
        "doc": dict(type="def", cles=["Mussolini", "Gentile"], terme="La Doctrine du fascisme · 1932",
                    t="Écrite par Mussolini et le philosophe Giovanni Gentile.",
                    etape="Idée 3 : « totalitaire », un mot que les fascistes employaient avec fierté", x=170, y=200, w=940),
        "c_doc1": dict(type="cit", a="Mussolini et Gentile", o="La Doctrine du fascisme, 1932 (cité par le cours, traduction)", x=200, y=200, w=880),
        "tot": dict(type="cols", g="Pour les fascistes", gq="« totalitaire » = complet, uni, fort",
                    d="Après la guerre", dq="une accusation : Arendt, sur le nazisme et le stalinisme", vs="→"),
        "cl": dict(type="cols", g="Le marxisme", gq="une société divisée en classes, engagées dans une lutte", d="Le fascisme",
                   dq="une humanité divisée en nations ; toutes les classes unies sous l'État", vs="≠", repere="Idée 4 : des nations, pas des classes"),
        "ban": dict(type="mot", t="La lutte des classes interdite", g="l'unité nationale au lieu de la révolution : les possédants se rallient au fascisme", y=260, taille=78),
        "c_doc2": dict(type="cit", a="Mussolini et Gentile", o="La Doctrine du fascisme, 1932, à propos du socialisme (traduction)", x=200, y=220, w=880),
        "contre": dict(type="liste", titre="Idée 5 · le premier totalitarisme est contre…", cles=["parlementarisme", "droits", "libéralisme", "nationaliste"], items=[
            "Le parlementarisme : le pouvoir des assemblées élues", "Les droits de l'homme : il ne croit pas qu'ils existent",
            "Le libéralisme comme le marxisme", "… et il est nationaliste et militariste"], x=170, y=140, w=940),
        "ind": dict(type="cols", g="Le libéralisme", gq="part de l'individu et de ses droits", d="Le fascisme",
                    dq="part de l'État, qui seul donne sa valeur à l'individu", vs="≠"),
        "c_doc3": dict(type="cit", a="Mussolini et Gentile", o="La Doctrine du fascisme, 1932 (cité par le cours, traduction)", x=200, y=220, w=880),
    }),

    # ================================================================ fascisme, idées 6 et 7
    dict(id="fas67", chap="Le fascisme · une terreur moins oppressive ?", fond="nuit", humeur="mystere",
         retenir="Moins oppressive : des opposants réduits au silence, pas tous tués · un contre-pouvoir : l'Église (accords du Latran, 1929), et le roi · pas raciste avant 1938 : La Difesa della Razza (août 1938), lois antisémites.",
         beats=[
        "{g4}{g4.1}Idée six. Le cours pose une question, avec un point d'interrogation : {!une terreur moins oppressive}une terreur moins oppressive ? "
        "{lim}{lim.1}En un sens, oui. Le fascisme veut réduire ses opposants au silence, pas tous les tuer. "
        "La plupart sont envoyés en relégation, sur des îles comme Lipari. Cet exemple est hors du cours.",
        "{lim.2}Et son pouvoir est incomplet. Mussolini n'est pas assez fort pour prendre le contrôle de l'Église. Alors il s'entend avec le pape. "
        "Ils signent un concordat, les accords du Latran, en mille neuf cent vingt-neuf. {lim.3}Et le roi reste chef de l'État.",
        "{-lim}{-g4}{amb}Voici une phrase à retenir pour une copie. {amb.1}Une ambition totalitaire ne signifie pas toujours un contrôle totalitaire.",
        "{-amb}{rac}{rac.1}Idée sept. Contrairement au nazisme, le fascisme italien n'est pas fondé sur le racisme. L'antisémitisme ne fait pas partie de son premier programme. "
        "{rac.2}Le tournant vient en mille neuf cent trente-huit. Désormais allié à Hitler, Mussolini impose des lois antisémites, et la nation devient officiellement raciste. "
        "{rac.3}Voici l'exemple. Une revue, La Difesa della Razza, la défense de la race, publiée à partir d'août mille neuf cent trente-huit. Elle oppose un profil romain "
        "à des visages juifs et africains. Et de prétendus spécialistes de la race viennent dans les écoles enseigner la supériorité de la race fasciste.",
        "{-rac}{nuance}En Italie, le racisme est donc un tournant tardif, lié à l'alliance allemande. Ce n'est pas le cœur de l'idéologie. "
        "{nuance.1}Mais il n'en est pas moins réel pour ses victimes. Le film de Roberto Benigni, La vie est belle, de mille neuf cent quatre-vingt-dix-sept, tourne ce racisme en dérision.",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[14]),
        "lim": dict(type="liste", titre="Idée 6 · moins oppressive, moins complète", petit=True, bande=True, x=40, y=120, w=520, items=[
            "Des opposants réduits au silence plutôt que tous tués : relégation sur des îles comme Lipari (hors du cours)",
            "Un contre-pouvoir : l'Église · accords du Latran, 1929", "Le roi reste chef de l'État"]),
        "amb": dict(type="mot", t="Ambition ≠ contrôle", g="une ambition totalitaire ne signifie pas toujours un contrôle totalitaire", y=250, taille=96),
        "rac": dict(type="liste", titre="Idée 7 · le tournant raciste de 1938", cles=["1938", "antisémites", "Difesa"], items=[
            "Avant 1938 : pas fondé sur le racisme ; pas d'antisémitisme dans le premier programme",
            "1938 : allié à Hitler, lois antisémites ; officiellement raciste",
            "La Difesa della Razza (août 1938) ; des « spécialistes » de la race dans les écoles"], x=150, y=140, w=980),
        "nuance": dict(type="note", terme="La nuance", cles=["tardif", "victimes"],
                       t="Un tournant tardif lié à l'alliance allemande, pas le cœur de l'idéologie.",
                       etape="Pas moins réel pour ses victimes · tourné en dérision dans La vie est belle de Benigni (1997)", x=170, y=200, w=940),
    }),

    # ================================================================ stalinisme, idée 8
    dict(id="sta8", chap="Le stalinisme · la lutte des classes pour moteur", fond="nuit", humeur="tension",
         retenir="Marxisme : l'histoire = la lutte des classes, vers une société sans classes, sans propriété, sans profit. Plan quinquennal (1928) : une URSS industrielle, indépendante du capitalisme mondial, débarrassée des derniers éléments capitalistes.",
         beats=[
        "{g5}{g5.1}Passons au stalinisme. Idée huit. L'idéologie soviétique est marxiste. L'histoire est une {!lutte des classes}lutte des classes. "
        "Et elle aboutit à une société sans classes, sans propriété privée, et sans profit.",
        "{-g5}{photo3}{plan5}{plan5.g}Le plan quinquennal de Staline, lancé en mille neuf cent vingt-huit, en fait un programme. Avec deux buts. "
        "Le premier : faire de l'Union soviétique un pays industriel et puissant, indépendant du capitalisme mondial. "
        "{plan5.d}Le second : se débarrasser des derniers éléments capitalistes. Surtout dans les campagnes, où la plupart des gens cultivent encore leur propre terre.",
        "{-plan5}{src1}L'exemple vient du dossier documentaire, document un. C'est le discours de Staline au Comité central, le sept janvier mille neuf cent trente-trois. "
        "Le Plan, dit-il, devait transformer un pays doté d'une{-src1}",
        ("C", "technique arriérée, et en partie médiévale", "c_st1"),
        "{-c_st1}en un pays",
        ("C", "pleinement autonome et indépendant des caprices du capitalisme mondial", "c_st2"),
        "{-c_st2}{-photo3}{date33}Regarde la date. Janvier mille neuf cent trente-trois. Dans ces mêmes mois, la famine tue les paysans d'Ukraine.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[12]),
        "photo3": dict(type="tableau", img="h2-fyp-poster", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.1, .5, .45],
                       legende="« L'arithmétique d'un contre-plan : 2 + 2 plus l'enthousiasme des travailleurs = 5 », affiche du plan quinquennal, 1931 · Yakov Guminer, domaine public"),
        "plan5": dict(type="cols", g="But 1 · l'industrie", gq="une URSS industrielle, puissante, indépendante du capitalisme mondial",
                      d="But 2 · les campagnes", dq="chasser les derniers éléments capitalistes : les fermes des paysans",
                      vs="+", repere="Le premier plan quinquennal, 1928"),
        "src1": dict(type="note", terme="Dossier documentaire · document 1", cles=["Staline", "Plan"],
                     t="Le discours de Staline au Comité central, 7 janvier 1933, sur ce que devait accomplir le plan quinquennal.",
                     etape="Deux buts : l'industrie, et plus aucun élément capitaliste", x=170, y=200, w=940),
        "date33": dict(type="mot", t="Janvier 1933", g="les mois mêmes de la famine en Ukraine", y=260, taille=96),
        "c_st1": dict(type="cit", a="Joseph Staline", o="discours au Comité central, 7 janvier 1933 (dossier documentaire, document 1, traduction)", x=200, y=210, w=880),
        "c_st2": dict(type="cit", a="Joseph Staline", o="discours au Comité central, 7 janvier 1933 (dossier documentaire, document 1, traduction)", x=200, y=210, w=880),
    }),

    # ================================================================ stalinisme, idée 9
    dict(id="sta9", chap="Le stalinisme · la collectivisation forcée", fond="nuit", humeur="tension",
         retenir="Collectivisation : les petites exploitations dispersées regroupées en kolkhozes (collectifs) et sovkhozes (d'État). Foyers collectivisés : 7 % (1928) · 15 % (1929) · 57 % (1930) · 90 % (1936).",
         beats=[
        "{def3}Idée neuf. La {!collectivisation}collectivisation. Il s'agit de regrouper les petites exploitations dispersées en grandes fermes collectives. "
        "{def3.1}Les exploitations familiales indépendantes sont supprimées. Les paysans sont regroupés dans des kolkhozes, des fermes collectives, ou dans des sovkhozes, "
        "qui appartiennent à l'État. Le but du Plan : la collectivisation totale, en cinq ans. Ainsi, plus de retour possible au capitalisme dans les campagnes.",
        "{-def3}{poster}La propagande se veut joyeuse. Le cours montre une affiche soviétique de mille neuf cent trente. Elle lance : "
        "{!Venez avec nous au kolkhoze, camarades !}Venez avec nous au kolkhoze, camarades !",
        "{-poster}{gc}Mais regarde maintenant les chiffres, dans le document deux du dossier. C'est la part des foyers paysans collectivisés. "
        "{gc.1}{gc.2}{gc.3}{gc.4}{gc.5}En mille neuf cent vingt-huit, sept pour cent. {gc.6}En mille neuf cent vingt-neuf, quinze pour cent. "
        "{gc.7}En mille neuf cent trente, cinquante-sept pour cent. {gc.8}Et en mille neuf cent trente-six, quatre-vingt-dix pour cent.",
        "{gc.9}Regarde le bond entre mille neuf cent vingt-neuf et mille neuf cent trente. De quinze à cinquante-sept pour cent, en une seule année. "
        "C'est un bond de la contrainte, pas du consentement. C'est le moment où les paysans abattent leur bétail plutôt que de le livrer. "
        "Le dossier fait tout partir de mille neuf cent vingt-huit. Hors du cours, beaucoup d'historiens le font partir de la fin de mille neuf cent vingt-neuf.",
    ], vis={
        "def3": dict(type="def", cles=["regrouper", "kolkhozes", "sovkhozes"], terme="La collectivisation",
                     t="Les petites exploitations dispersées regroupées en grandes fermes collectives ; les exploitations familiales supprimées.",
                     etape="Kolkhozes (fermes collectives) · sovkhozes (fermes d'État) · collectivisation totale en 5 ans", x=170, y=200, w=940),
        "poster": dict(type="mot", t="« Venez avec nous au kolkhoze, camarades ! »", g="affiche soviétique, 1930 (cours)", y=260, taille=60),
        "gc": dict(type="graphe", titre="Foyers paysans collectivisés (dossier documentaire, document 2)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[0.4, 4.6], y=[0, 105], gx=[], gy=[25, 50, 75, 100], lx="", ly="%"), el=barres_collect()),
    }),

    # ================================================================ stalinisme, idée 10
    dict(id="sta10", chap="Le stalinisme · les koulaks", fond="nuit", humeur="tension",
         retenir="Koulak : en théorie un paysan possédant plus de 8 acres ; en pratique tout paysan qui refuse la collectivisation. Persécutés en tant que classe : terres et bêtes confisquées, beaucoup déportés. Le « sabotage koulak ».",
         beats=[
        "{g6}{g6.1}Idée dix. L'étiquette de {!koulak}koulak. {kul}{kul.1}En théorie, un koulak est un paysan qui possède plus de huit acres de terre. "
        "{kul.2}En pratique, l'étiquette vise tout paysan qui refuse la collectivisation. On l'accuse d'être trop égoïste pour partager.",
        "{kul.3}Les koulaks sont donc persécutés {!en tant que classe}en tant que classe. Leurs terres et leurs bêtes sont confisquées, et beaucoup sont déportés. "
        "Les flèches de la carte montrent les déportations vers la Sibérie et le Kazakhstan. Ce détail est hors du cours. "
        "{kul.4}Et quand ils résistent, le régime parle de sabotage koulak. Un sabotage qu'il faut briser.",
        "{-kul}{-g6}{ex10}Voici deux exemples. {ex10.g}D'abord, le cours. En mille neuf cent vingt-neuf, des kolkhoziens manifestent contre les koulaks. "
        "Leur banderole réclame la liquidation des koulaks en tant que classe. {ex10.d}Ensuite, l'Ukraine, en mille neuf cent trente-deux. Selon l'historien Nicolas Werth, "
        "les paysans qui cachent du grain sont accusés de sabotage koulak. Quelle que soit la taille de leur terre.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[15]),
        "kul": dict(type="liste", titre="L'étiquette de koulak", petit=True, bande=True, x=40, y=120, w=540, items=[
            "En théorie : un paysan possédant plus de 8 acres", "En pratique : tout paysan qui refuse la collectivisation",
            "Persécutés en tant que classe : terres, bêtes confisquées ; déportés", "La résistance qualifiée de « sabotage koulak »"]),
        "ex10": dict(type="cols", g="1929 · le cours", gq="des kolkhoziens sous une banderole : liquider les koulaks en tant que classe",
                     d="1932 · Ukraine (Werth)", dq="les paysans qui cachent du grain accusés de « sabotage koulak »", vs="+"),
    }),

    # ================================================================ stalinisme, idée 11
    dict(id="sta11", chap="Le stalinisme · l'Holodomor", fond="guerre", humeur="tension",
         retenir="Grain réquisitionné quelle que soit la récolte · brigades de la Guépéou · Molotov et Kaganovitch : villages « rebelles » privés de tout ravitaillement · sept. 1932 : 32 % de l'objectif, 25 oct. : 22 % · l'Holodomor, 1932-1933.",
         beats=[
        "{g7}{g7.1}Idée onze : le résultat. Ukraine, mille neuf cent trente-deux. Le grain est {!réquisitionné}réquisitionné, quelle que soit la récolte. "
        "Cela se fait étape par étape. {hol}{hol.1}Les paysans résistent. Ils cachent du grain dans des fosses, et dans des greniers secrets. "
        "Ou ils envoient enfants et vieillards couper les épis la nuit. "
        "{hol.2}Le régime répond par des brigades, appuyées par la police politique, la Guépéou. Leur mission : prendre le grain.",
        "{hol.3}Le Politburo envoie Molotov et Kaganovitch. D'abord, ils suspendent les livraisons de produits manufacturés aux districts qui n'ont pas rempli le plan. "
        "{hol.4}Puis les villages les plus rebelles sont inscrits au tableau noir. Cela veut dire qu'ils sont privés de tout ravitaillement, nourriture comprise.",
        "{-hol}{-g7}{pct}L'historien Nicolas Werth, dans le document quatre, donne les chiffres. {pct.g}En septembre mille neuf cent trente-deux, l'Ukraine n'atteint que trente-deux pour cent "
        "de son objectif mensuel de collecte de grain. {pct.d}Le vingt-cinq octobre, plus que vingt-deux pour cent.",
        "{-pct}{bil}Le résultat est une famine provoquée par l'homme : l'Holodomor, en mille neuf cent trente-deux et trente-trois. "
        "Elle a tué environ quatre millions de personnes en Ukraine. Ce bilan est ajouté hors du cours.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[19]),
        "hol": dict(type="liste", titre="Ukraine, 1932 : étape par étape", petit=True, bande=True, x=40, y=120, w=540, items=[
            "Les paysans cachent le grain dans des fosses ; les enfants coupent les épis la nuit", "Des brigades appuyées par la Guépéou pour « prendre le grain »",
            "Molotov et Kaganovitch suspendent les produits manufacturés aux districts en retard", "Les villages « rebelles » « inscrits au tableau noir » : plus de nourriture"]),
        "pct": dict(type="cols", g="Septembre 1932", gq="32 % de l'objectif mensuel de grain atteint", d="25 octobre 1932",
                    dq="plus que 22 %", vs="→", repere="Nicolas Werth (dossier documentaire, document 4)"),
        "bil": dict(type="mot", t="≈ 4 millions de morts", g="l'Holodomor, Ukraine, 1932-1933 · bilan ajouté hors du cours", y=250, taille=90),
    }),

    # ================================================================ stalinisme, idée 12 et le dossier documentaire
    dict(id="sta12", chap="Le stalinisme · un échec économique", fond="aube", humeur="calme",
         retenir="La collectivisation ruine l'agriculture : plus de motivation, bétail abattu, production en baisse. Feigin, 9 avril 1932 : les vaches des kolkhozes donnent 1 à 3 litres de lait par jour au lieu de 5 à 7 ; « les gens meurent de faim ».",
         beats=[
        "{def4}Idée douze. Au-delà de la famine, la collectivisation est un {!échec économique}échec économique. "
        "{def4.1}Les paysans qui ont perdu leurs terres et leurs bêtes n'ont aucune raison de travailler dur pour le kolkhoze. Beaucoup abattent leur bétail "
        "plutôt que de le livrer. La production baisse. Les ressources se raréfient. Et les campagnes deviennent hostiles.",
        "{-def4}{src5}Voici l'exemple, dans le document cinq. C'est une lettre écrite à Novossibirsk le neuf avril mille neuf cent trente-deux, par un responsable nommé Feigin. "
        "Il écrit au dirigeant soviétique Ordjonikidze. {-src5}{lait}{lait.g}D'ordinaire, une vache donne cinq à sept litres de lait par jour. "
        "{lait.d}Les vaches du kolkhoze en donnent un à trois. Les paysans abattent leurs dernières bêtes. Et Feigin écrit :{-lait}",
        ("C", "les gens meurent de faim", "c_fei"),
        "{-c_fei}{choix}Le régime a donc fait un choix. {!L'idéologie et le contrôle}L'idéologie et le contrôle d'abord. Avant de nourrir son propre peuple.",
        "{-choix}Le dossier documentaire résume tout le processus en quatre cases. {ws2}{ws2.1}L'idéologie : le marxisme. {ws2.2}L'objectif : "
        "la collectivisation totale en cinq ans. {ws2.3}La mise en œuvre : les fermes collectives, et la persécution des koulaks. "
        "{ws2.4}Et les résultats : l'Holodomor, la résistance, et l'échec économique.",
        ("P", 3.0),
    ], vis={
        "def4": dict(type="def", cles=["raison", "abattent", "baisse"], terme="Idée 12 · un échec économique",
                     t="Plus de motivation dans le kolkhoze, le bétail abattu, la production en baisse.",
                     etape="Les campagnes deviennent hostiles", x=170, y=200, w=940),
        "src5": dict(type="note", terme="Dossier documentaire · document 5", cles=["Feigin", "Ordjonikidze"],
                     t="Une lettre de Feigin, un responsable, au dirigeant soviétique Ordjonikidze.",
                     etape="Novossibirsk, 9 avril 1932", x=170, y=200, w=940),
        "lait": dict(type="cols", g="Une vache ordinaire", gq="5 à 7 litres de lait par jour", d="Une vache de kolkhoze, 1932",
                     dq="1 à 3 litres par jour", vs="≠", repere="Feigin à Ordjonikidze, Novossibirsk, 9 avril 1932 (document 5)"),
        "c_fei": dict(type="cit", a="Feigin, lettre à Ordjonikidze", o="Novossibirsk, 9 avril 1932 (dossier documentaire, document 5, traduction)", x=200, y=230, w=880),
        "choix": dict(type="mot", t="L'idéologie avant le pain", g="le régime fait passer le contrôle avant le ravitaillement de son peuple", y=260, taille=84),
        "ws2": dict(type="liste", titre="Dossier documentaire · le processus de collectivisation", petit=True, items=[
            "Idéologie : le marxisme · ni propriété privée, ni profit, ni classes · contre le capitalisme",
            "Objectif : la collectivisation totale en 5 ans · une URSS industrielle moderne · l'autarcie",
            "Mise en œuvre : fermes collectives (kolkhozes, sovkhozes) · koulaks persécutés",
            "Résultats : l'Holodomor (1932-1933) · grain caché, bétail abattu · échec économique"], x=130, y=130, w=1020),
    }),

    # ================================================================ nazisme, idée 13
    dict(id="naz13", chap="Le nazisme · la lutte des races", fond="nuit", humeur="tension",
         retenir="Le nazisme : l'histoire comme une lutte entre races, rangées selon une hiérarchie, les « Aryens » étant les plus purs. La survie par la pureté de la race (relations mixtes interdites) et par le territoire. Mein Kampf, 1924-1925.",
         beats=[
        "{g8}{g8.1}Passons au nazisme. Idée treize. Pour les nazis, l'histoire de l'humanité est une {!lutte entre les races}lutte entre les races. "
        "{race}{race.1}Les races forment une hiérarchie. Certaines vaudraient plus que d'autres : il est donc crucial de les reconnaître, et de les étudier. "
        "Et les prétendus Aryens sont les plus purs.",
        "{race.2}Chaque individu partage un instinct collectif de survie. {race.3}Et la survie de la race dépend de deux choses. "
        "La première, c'est la pureté de la race. D'où l'interdiction des relations entre races. {race.4}La seconde, c'est la conquête de territoires, pour que la population puisse croître. "
        "Hitler avait exposé ces idées racistes dès mille neuf cent vingt-quatre et vingt-cinq, dans Mein Kampf.",
        "{-race}{-g8}{hum}Le cours en donne l'exemple. {hum.g}Une scène d'humiliation publique, en mille neuf cent trente-cinq. Une femme non juive et un homme juif "
        "sont entourés d'hommes de la SA. On les force à porter des pancartes qui dénoncent leur relation. "
        "{hum.d}Le cours montre aussi un tableau du ministère nazi de la santé, à Bamberg. Il classe les groupes raciaux de la terre.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[23]),
        "race": dict(type="liste", titre="Idée 13 · la vision nazie de l'histoire", petit=True, bande=True, x=40, y=120, w=500, items=[
            "L'histoire = une lutte entre races, rangées selon une hiérarchie", "Un instinct collectif de survie",
            "Survie 1 : la pureté de la race · relations entre « races » interdites", "Survie 2 : le territoire, pour accroître la population"]),
        "hum": dict(type="cols", g="1935 · une humiliation publique", gq="un couple forcé par des SA à porter des pancartes dénonçant leur relation",
                    d="Bamberg · un tableau du ministère de la santé", dq="les « groupes raciaux de la terre » classés", vs="+", repere="le cours"),
    }),

    # ================================================================ nazisme, idée 14
    dict(id="naz14", chap="Le nazisme · le langage des « bactéries »", fond="guerre", humeur="tension",
         retenir="Les Juifs, la « race la plus dangereuse » dans l'idéologie nazie ; décrits comme des « bactéries », un « virus » à éliminer : l'élimination présentée comme de l'hygiène. Enseignement racial obligatoire, sept. 1933 ; Der Giftpilz (1938).",
         beats=[
        "{dang}Idée quatorze. Dans l'idéologie nazie, les Juifs sont la race la plus dangereuse. {dang.1}Pourquoi ? Parce que, prétendent les nazis, "
        "contrairement aux autres, ils n'ont pas d'espace vital à eux. {dang.2}On les accuse donc de chercher à dominer les peuples parmi lesquels ils vivent, "
        "en détruisant l'État-nation. {dang.3}Et de viser l'abâtardissement de tous les peuples, et la fin de tous les États.",
        "{-dang}{bio}Le cours relève le {!langage biologique}langage biologique qui en découle. {bio.1}Les Juifs sont décrits comme des bactéries, qui infectent "
        "le corps de la nation. Un virus, à éliminer. {bio.2}Et si un peuple est décrit comme une maladie, alors l'éliminer devient de l'hygiène. "
        "Pas un crime. {!Les mots ont préparé les actes}Les mots ont préparé les actes.",
        "{-bio}{eco14}L'exemple, c'est l'école. {eco14.1}En septembre mille neuf cent trente-trois, l'enseignement racial devient obligatoire dans les écoles allemandes. "
        "{eco14.2}Les livres pour enfants portent le même message. Comme le livre d'Elvira Bauer, en mille neuf cent trente-six, dont le titre promettait que tous les Juifs devaient partir. "
        "{eco14.3}Ou Der Giftpilz, le Champignon vénéneux, publié à Nuremberg en mille neuf cent trente-huit.",
    ], vis={
        "dang": dict(type="liste", titre="Idée 14 · la « race la plus dangereuse », dans l'idéologie nazie", items=[
            "Pas d'espace vital à eux, disent les nazis", "Donc censés vouloir dominer les peuples hôtes et détruire l'État-nation",
            "Et viser « l'abâtardissement » de tous les peuples, la fin de tous les États"], x=150, y=150, w=980),
        "bio": dict(type="def", cles=["bactéries", "virus", "hygiène"], terme="Un langage biologique",
                    t="Les Juifs décrits comme des « bactéries » qui infectent la nation, un « virus » à éliminer.",
                    etape="Si un peuple est une maladie, l'éliminer devient de « l'hygiène » : les mots ont préparé les actes", x=170, y=200, w=940),
        "eco14": dict(type="liste", titre="Le message transmis aux enfants", items=[
            "Septembre 1933 : l'enseignement racial obligatoire dans les écoles allemandes",
            "Le livre pour enfants d'Elvira Bauer, 1936 : « tous les Juifs doivent partir »",
            "Der Giftpilz (« Le Champignon vénéneux »), Nuremberg, 1938"], x=150, y=150, w=980),
    }),

    # ================================================================ nazisme, idée 15
    dict(id="naz15", chap="Le nazisme · des Allemands jugés « inaptes »", fond="nuit", humeur="tension",
         retenir="Le racisme nazi frappe aussi des Allemands : les handicapés, les malades héréditaires. T4, lancé en 1939 : environ 70 000 Allemands handicapés assassinés, 1939-1941, surtout dans des chambres à gaz.",
         beats=[
        "{unfit}Idée quinze. La liste des personnes à éliminer ne s'arrête pas aux Juifs. {unfit.1}Elle comprend les personnes handicapées. "
        "{unfit.2}Les malades héréditaires. {unfit.3}Et quiconque a une relation sexuelle avec ceux que les nazis appellent des virus.",
        "{-unfit}{t4}L'exemple, c'est le {!programme T4}programme T quatre, lancé en mille neuf cent trente-neuf. C'est le meurtre de personnes handicapées, en Allemagne même, "
        "dans des chambres à gaz construites à cet effet. {t4.1}Selon la version révisée du cours, environ soixante-dix mille personnes sont tuées entre mille neuf cent trente-neuf et mille neuf cent quarante et un. "
        "{t4.2}Une version antérieure disait deux cent mille. C'est le bilan jusqu'en mille neuf cent quarante-cinq. Pour le cours, retiens soixante-dix mille, de mille neuf cent trente-neuf à quarante et un.",
    ], vis={
        "unfit": dict(type="liste", titre="Idée 15 · également visés", items=[
            "Les personnes handicapées", "Les malades héréditaires", "Quiconque a une relation avec ces prétendus « virus »"],
            x=170, y=170, w=940),
        "t4": dict(type="def", cles=["1939", "gaz"], terme="Le programme T4 · 1939",
                   t="Le meurtre d'Allemands handicapés, dans des chambres à gaz construites à cet effet : environ 70 000 en 1939-1941.",
                   etape="Version antérieure : 200 000 = le bilan jusqu'en 1945 · retiens 70 000 pour 1939-1941", x=170, y=200, w=940),
    }),

    # ================================================================ comparaison : h2ideo
    dict(id="compare", chap="Trois idéologies comparées", fond="aube", humeur="lumiere",
         retenir="Points communs : le rejet de la démocratie libérale, un but suprême qui justifie tous les moyens, le contrôle total par la contrainte, un « homme nouveau ». Différence : le but (nation / race / classe), donc l'ennemi et son sort.",
         beats=[
        "{com}Comparons maintenant. Qu'ont les trois en commun ? {com.1}Ils rejettent la démocratie libérale. "
        "{com.2}Ils fixent un but suprême qui justifie tous les moyens. {com.3}Ils cherchent le contrôle total de la société, par la contrainte. "
        "{com.4}Et ils veulent un homme nouveau. Ce sera pour l'épisode quatre.",
        "{-com}{but}{but.1}Mais leurs buts suprêmes s'opposent. Pour le fascisme, une nation unie, disciplinée et grande. "
        "{but.2}Pour le nazisme, une race pure, qui étend son territoire et sa population. "
        "{but.3}Pour le stalinisme, une Union soviétique socialiste : industrielle, autonome, sans plus aucun élément capitaliste.",
        "{-but}{enn}{enn.1}L'ennemi intérieur n'est donc pas le même. En Italie, c'est la gauche et ses critiques, comme le socialiste Matteotti. "
        "{enn.2}En Allemagne, ce sont les Juifs, les personnes handicapées, les malades héréditaires. Le prétendu virus. "
        "{enn.3}En Union soviétique, ce sont les koulaks, et tous les éléments capitalistes.",
        "{-enn}{sort}{sort.1}Et le sort de l'ennemi n'est pas le même non plus. En Italie, réduit au silence plutôt que tué. {sort.2}En Allemagne, à éliminer, pour purifier la race. "
        "{sort.3}En Union soviétique, persécuté en tant que classe. Pense à l'Holodomor, en mille neuf cent trente-deux et trente-trois.",
        "{-sort}{rule}Voici donc la règle pour une copie. {rule.g}Ce qu'ils partagent, c'est la méthode de pouvoir. "
        "{rule.d}Ce qui diffère, c'est le but qu'elle sert. Et donc, la cible de la terreur.",
    ], vis={
        "com": dict(type="liste", titre="Commun aux trois", cles=["démocratie", "suprême", "contrainte", "nouveau"], items=[
            "Le rejet de la démocratie libérale", "Un but suprême qui justifie tous les moyens",
            "Le contrôle total de la société par la contrainte", "La volonté de créer un « homme nouveau »"], x=170, y=140, w=940),
        "but": dict(type="cartes", petit=True, items=[
            dict(t="Fascisme", q="but suprême : une nation unie, disciplinée, grande"),
            dict(t="Nazisme", q="but suprême : une race pure qui étend son territoire"),
            dict(t="Stalinisme", q="but suprême : une URSS socialiste, industrielle, autonome")]),
        "enn": dict(type="cartes", petit=True, items=[
            dict(t="Fascisme", q="ennemi intérieur : la gauche et ses critiques (Matteotti, 1924)"),
            dict(t="Nazisme", q="ennemi intérieur : les Juifs, les handicapés (T4, 1939)"),
            dict(t="Stalinisme", q="ennemi intérieur : les koulaks, les « éléments capitalistes » (1932)")]),
        "sort": dict(type="cartes", petit=True, items=[
            dict(t="Fascisme", q="l'ennemi réduit au silence plutôt que tué"),
            dict(t="Nazisme", q="l'ennemi à éliminer, pour « purifier » la race"),
            dict(t="Stalinisme", q="l'ennemi persécuté en tant que classe ; l'Holodomor")]),
        "rule": dict(type="cols", g="En commun", gq="la méthode de pouvoir", d="La différence", dq="le but qu'elle sert → la cible de la terreur",
                     vs="≠", repere="La phrase clé de la comparaison"),
    }),

    # ================================================================ le tableau de synthèse et les points à confirmer
    dict(id="grille", chap="Le tableau de synthèse du cours", fond="aube", humeur="calme",
         retenir="Le tableau, rubrique « Idéologie » : points communs (rejet de la démocratie libérale ; un but suprême ; contrôle total pour un homme nouveau) · spécificités : l'État absolu / la lutte des races / la lutte des classes.",
         beats=[
        "{gr}{gr.1}Le cours résume le chapitre dans un tableau de synthèse. Fascisme, nazisme, stalinisme. Sur le site, tu peux masquer les cases et les réciter. "
        "Voici sa rubrique idéologie. "
        "D'abord, les points communs, les mêmes pour les trois. Le rejet de la démocratie libérale. Un but suprême. Et le contrôle total, pour créer un homme nouveau.",
        "{gr.2}Puis les spécificités du fascisme. {gr.3}Du nazisme. {gr.4}Et du stalinisme. C'est tout ce que tu viens de voir. "
        "Mets la vidéo en pause, et récite chaque colonne à voix haute.",
        "{-gr}{chk}{chk.1}Et trois points à surveiller. Matteotti : mille neuf cent vingt-quatre, pas vingt-cinq. {chk.2}La collectivisation : mille neuf cent vingt-huit, ou la fin de mille neuf cent vingt-neuf. "
        "{chk.3}Et les exemples hors du cours. Ils sont exacts. Mais dans une copie, préfère ceux du cours.",
        ("P", 3.0),
    ], vis={
        "gr": dict(type="liste", titre="Le tableau du cours · Idéologie", petit=True, items=[
            "Points communs (les trois) : rejet de la démocratie libérale · un but suprême · contrôle total pour créer un homme nouveau",
            "Fascisme : l'État absolu · contre le libéralisme, le marxisme, le parlementarisme, les droits de l'homme · nationaliste, militariste · raciste seulement à partir de 1938",
            "Nazisme : la lutte des races · hiérarchie des races, les « Aryens » les plus purs · pureté et territoire · les Juifs, « race la plus dangereuse » · T4",
            "Stalinisme : la lutte des classes · ni propriété, ni classes · plan quinquennal, collectivisation · koulaks ennemis de classe"],
            x=110, y=110, w=1060),
        "chk": dict(type="liste", titre="Trois points à surveiller", items=[
            "Matteotti : tué le 10 juin 1924, pas en 1925", "La collectivisation : « dès 1928 » (dossier documentaire) ; fin 1929 pour beaucoup d'historiens",
            "Hors du cours : Lipari, ≈ 4 millions de morts de l'Holodomor, 1,8 million de koulaks déportés"], x=150, y=150, w=980),
    }),

    # ================================================================ à toi : un paragraphe de composition
    dict(id="essai", chap="À toi · un paragraphe de composition", fond="aube", humeur="calme",
         retenir="Un paragraphe de comparaison : le point commun (un but suprême, le contrôle total) · nation / race / classe, un exemple chacun · la conclusion : le but décide de l'ennemi.",
         beats=[
        "{ex1}À toi maintenant. Voici un sujet que tu pourrais avoir, dans l'esprit du cours. "
        "{!Explique}Explique en quoi les idéologies du fascisme, du nazisme et du stalinisme diffèrent.",
        "{-ex1}{str}Comment construire un paragraphe de comparaison ? {str.1}Commence par une phrase d'annonce : le point commun. "
        "{str.2}Puis prends chaque régime : son but suprême, et un exemple précis. {str.3}Puis la conséquence : l'ennemi. "
        "{str.4}Et termine par une phrase qui répond à la question.",
        "{-str}{pa1}",
        ("P", 2.0),
        "{-pa1}{mod}Voici un modèle. {mod.1}Les trois régimes rejettent la démocratie libérale. Chacun fixe un but suprême qui justifie un contrôle total. "
        "Mais ce but diffère. {mod.2}Le fascisme place au-dessus de tout la nation, incarnée dans un État absolu. La Doctrine de mille neuf cent trente-deux affirme "
        "que tout est dans l'État. Et le fascisme unit toutes les classes, au lieu de les opposer. "
        "{mod.3}Le nazisme voit l'histoire comme une lutte entre les races. Il interdit les relations entre races et, à partir de septembre mille neuf cent trente-trois, enseigne le racisme à l'école. "
        "{mod.4}Le stalinisme, au contraire, est marxiste : l'histoire est une lutte des classes. Le plan quinquennal de mille neuf cent vingt-huit collectivise donc les terres, "
        "de sept pour cent des foyers paysans à quatre-vingt-dix pour cent en mille neuf cent trente-six. "
        "{mod.5}Par conséquent, l'ennemi diffère. En Italie, les critiques de l'État, comme Matteotti. En Allemagne, les Juifs, et les handicapés, "
        "assassinés par le programme T quatre à partir de mille neuf cent trente-neuf. En Union soviétique, les koulaks, persécutés en tant que classe. Le but décide de l'ennemi.",
        ("P", 2.0),
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Explique en quoi les idéologies du fascisme, du nazisme et du stalinisme diffèrent.",
                    src="Sujet écrit pour cette vidéo, sur la partie I.3", enonce=["Un paragraphe de comparaison : la nation, la race, la classe"]),
        "str": dict(type="liste", titre="Un paragraphe de comparaison", cles=["commun", "but", "ennemi", "répond"], items=[
            "Phrase d'annonce : le point commun", "Chaque régime : son but suprême + un exemple précis",
            "La conséquence : l'ennemi", "Une phrase finale qui répond à la question"], x=170, y=140, w=940),
        "pa1": dict(type="pause", t="Question problématisée : en quoi les idéologies du fascisme, du nazisme et du stalinisme diffèrent-elles ?",
                    sous="La nation, la race, la classe : un exemple chacun. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "mod": dict(type="liste", titre="Un paragraphe modèle", petit=True, items=[
            "Point commun : pas de démocratie libérale ; un but suprême qui justifie le contrôle total",
            "Fascisme → la nation et l'État : « tout est dans l'État » (1932) ; les classes unies",
            "Nazisme → la race : relations entre « races » interdites ; enseignement racial, sept. 1933",
            "Stalinisme → la classe : plan quinquennal (1928) ; de 7 % à 90 % collectivisés (1936)",
            "Donc l'ennemi diffère : Matteotti · les Juifs et les handicapés (T4) · les koulaks"], x=130, y=120, w=1020),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Le fascisme : la nation, et l'État absolu. Matteotti. L'Église et le roi. Et le racisme seulement à partir de mille neuf cent trente-huit. "
        "{carte.2}Le stalinisme : la lutte des classes. La collectivisation, de sept à quatre-vingt-dix pour cent. Les koulaks. L'Holodomor. "
        "{carte.3}Le nazisme : la lutte des races, la pureté et le territoire. Les Juifs décrits comme des bactéries. Et T quatre. "
        "{carte.4}Enfin, la comparaison. La même méthode, mais trois buts. Et le but décide de l'ennemi.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : le chef, le parti et l'homme nouveau. Comment le Duce, le Führer et le petit père des peuples "
        "ont été changés en idoles. Et comment chaque régime a voulu refaire l'être humain.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="NATION · RACE · CLASSE", branches=[
            dict(t="Fascisme", items=["nouvelle révolution · Rome", "Matteotti 1924 · lois 1925", "Église, roi · raciste en 1938"]),
            dict(t="Stalinisme", items=["lutte des classes · Plan 1928", "7 % → 90 % · koulaks", "Holodomor · échec"]),
            dict(t="Nazisme", items=["lutte des races", "les Juifs comme « bactéries »", "T4, 1939"]),
            dict(t="Comparaison", items=["même méthode", "trois buts", "le but décide de l'ennemi"])]),
        "fin": dict(type="mot", t="Prochain épisode : le chef et l'homme nouveau", g="Épisode 4 · culte du chef · contrôle total", y=270, taille=64),
    }),
]

QUIZ = [
    dict(q="Pourquoi l'affiche de 1932 de l'exposition de la révolution fasciste est-elle datée de « l'an XI » ?",
         r=["Le calendrier fasciste part de 1922, l'année où Mussolini prend le pouvoir", "Le fascisme est né en 1921",
            "C'était la onzième exposition", "Rome a été fondée en l'an XI"], ok=0, voir="an11",
         ex="L'histoire devait recommencer avec le fascisme : 1922 = an I."),
    dict(q="En quel sens les fascistes employaient-ils le mot « totalitaire » ?",
         r=["Positivement : un État complet, uni, fort, où « tout est dans l'État »", "Comme une insulte contre Staline",
            "Pour décrire une démocratie", "Seulement après 1945"], ok=0, voir="c_doc1",
         ex="Le sens accusateur vient après la guerre, avec des historiens et des philosophes comme Arendt."),
    dict(q="Selon la Doctrine du fascisme, qu'est-ce qui divise l'humanité ?",
         r=["Les nations, pas les classes", "Les classes, pas les nations", "Les races", "Les religions"], ok=0, voir="cl",
         ex="La lutte des classes est interdite ; toutes les classes sont unies dans la nation, sous l'État."),
    dict(q="Quel contre-pouvoir limite le contrôle de Mussolini ?",
         r=["L'Église catholique (accords du Latran, 1929)", "Les syndicats", "Le Parti communiste", "La Société des Nations"], ok=0, voir="lim",
         ex="Et le roi reste chef de l'État : une ambition totalitaire n'est pas toujours un contrôle totalitaire."),
    dict(q="Quelle part des foyers paysans soviétiques est collectivisée en 1930 ?",
         r=["57 %", "7 %", "15 %", "90 %"], ok=0, voir="gc",
         ex="7 % en 1928, 15 % en 1929, 57 % en 1930, 90 % en 1936 : le bond de 1929-1930 est celui de la contrainte."),
    dict(q="En pratique, qui est déclaré koulak ?",
         r=["Tout paysan qui refuse la collectivisation", "Seulement les paysans possédant plus de 8 acres", "Un membre d'un kolkhoze",
            "Un officier de la Guépéou"], ok=0, voir="kul",
         ex="En théorie, plus de 8 acres ; en pratique, tout paysan qui résiste, « trop égoïste pour partager »."),
    dict(q="Qu'est-ce que l'Holodomor ?",
         r=["La famine provoquée de 1932-1933 en Ukraine", "Le premier plan quinquennal", "Une ferme collective soviétique",
            "Une purge de l'Armée rouge"], ok=0, voir="bil",
         ex="Réquisitions et villages « rebelles » privés de tout ravitaillement : le 25 oct. 1932, seuls 22 % de l'objectif de grain étaient atteints."),
    dict(q="Que fait le programme T4, lancé en 1939 ?",
         r=["Il assassine des Allemands handicapés, environ 70 000 en 1939-1941", "Il rend l'enseignement racial obligatoire",
            "Il interdit les relations entre « races »", "Il déporte les koulaks"], ok=0, voir="t4",
         ex="Le racisme nazi frappe aussi des Allemands qui ne correspondent pas à l'idéal de la race pure."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 2 « Les régimes totalitaires », partie I.3 « Les spécificités de chaque régime », avec le dossier documentaire sur la collectivisation, la comparaison des trois idéologies, le tableau de synthèse et les points à confirmer, tel qu'il est rédigé sur le site ; carte animée du chapitre (site).",
    "Ajouté hors du cours, et dit comme tel : le bilan de l'Holodomor (≈ 4 millions de morts), la relégation à Lipari, la déportation des koulaks vers la Sibérie et le Kazakhstan, le « grand tournant » de la fin 1929, le chiffre de 1,8 million de koulaks déportés.",
    "Correction du cours : Matteotti a été enlevé et tué le 10 juin 1924 (le cours dit 1925, l'année de la revendication de Mussolini et des lois fascistissimes).",
    "Citations, en traduction française : La Doctrine du fascisme (Mussolini et Gentile, 1932) et le discours de Staline du 7 janvier 1933, tels que le cours les cite ; la lettre de Feigin du 9 avril 1932 (dossier documentaire, document 5).",
    "Photographies et affiches (via Wikimedia Commons) : l'exposition de la révolution fasciste, Rome, salle « 1914 » (photographe inconnu, domaine public) ; Benito Mussolini, vers 1937-1940 (Keystone, domaine public) ; affiche du plan quinquennal « 2 + 2 = 5 », 1931 (Yakov Guminer, domaine public).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
