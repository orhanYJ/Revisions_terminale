"""Histoire · « La Seconde Guerre mondiale » — édition française de la série vidéo, épisode 4 :
« Barbarossa : une guerre d'anéantissement » (parties II.1 et II.2 du cours).

Traduction et adaptation de h3_4.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
plus de mention de la DNL ni de l'anglais d'examen ; Worksheet 3 → « le dossier documentaire » (Source N → document N) ;
l'essay devient un paragraphe de composition, le DBQ une analyse de document (présenter, situer, intérêt et limites).
Mêmes scènes, mêmes visuels, mêmes repères, mêmes cartes animées (sc, voir h3_4.py) et mêmes données chiffrées.
Chaîne : outils/serie-philo/generer.py h3f_4 ; sortie dans dnl/serie/ (code h3f-4).
Citations en traduction française fidèle : ordre des commissaires (juin 1941), ordre de Reichenau (10 octobre 1941),
discours de Staline (6 novembre 1941), ordre n° 227 (28 juillet 1942), lettres d'un soldat allemand (document 6).
Toukhatchevski : exemple ajouté hors cours, dit comme tel.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-4"
NOTION = "La Seconde Guerre mondiale"
NUM = 4
TITRE = "Barbarossa : une guerre d'anéantissement"
SUIVANT = "Épisode 5 · Vers le génocide"
PRONONCIATION = {"Grossraum": "Gross-raoum", "Lebensraum": "Lé-benss-raoum", "Wehrmacht": "Vèr-markt",
                 "Einsatzgruppen": "Aïne-zats-groupen", "Übermensch": "Uber-mènch", "Untermensch": "Ounter-mènch",
                 "Vernichtungskrieg": "Fèr-nich-tounks-krik", "Reichenau": "Raï-che-nao", "Walther": "Valter",
                 "Paulus": "Paou-louss", "Białystok": "Bia-wis-tok", "Lvov": "Lvof", "Mein Kampf": "Maïne-Kampf",
                 "Ribbentrop": "Ribbène-trop", "Molotov-Ribbentrop": "Molotov-Ribbène-trop",
                 "Auschwitz-Birkenau": "Aouch-vits-Birke-nao"}


def barres(cats, cG, cS, lp_leg=124):
    """Graphique en barres : pour chaque catégorie (nom, Allemands, Soviétiques), le texte puis deux barres.
    Même construction que dans h3_4.py ; légendes en français et nombres écrits à la française (1 011 500)."""
    el = [dict(type="texte", x=1.0, y=lp_leg, t="Allemands", c=cG), dict(type="texte", x=2.0, y=lp_leg, t="Soviétiques", c=cS)]
    for i, (nom, g, s) in enumerate(cats, start=1):
        m = max(g, s)
        hg, hs = 100 * g / m, 100 * s / m
        bas = min(hg, hs) + 8
        el.append(dict(type="texte", x=i, y=-9, t=nom, c="iv"))
        for dx, v, h_, c in ((-0.17, g, hg, cG), (0.17, s, hs, cS)):
            lab = h_ + 8 if h_ == min(hg, hs) else max(h_ + 8, bas + 12)
            el.append(dict(type="droite", pts=[[i + dx, 5.5], [i + dx, max(6, h_ - 5.5)]], c=c, ep=34, dur=1.0,
                           lbl=f"{v:,}".replace(",", " "), lp=[i + dx, lab]))
    return el


AX_BARRES = dict(x=[0.35, 4.65], y=[0, 130], gx=[], gy=[], lx="", ly="")
FORCES = [("Hommes", 1011500, 1143500), ("Canons", 10290, 13541), ("Chars", 675, 894), ("Avions", 1216, 1115)]
PERTES = [("Pertes", 760000, 1130000), ("Chars perdus", 500, 4341), ("Avions perdus", 900, 2769)]

ANS = [1940, 1942, 1943, 1944, 1945]
DIV_URSS = list(zip(ANS, [200, 250, 350, 400, 488]))
DIV_ALL = list(zip(ANS, [189, 261, 327, 347, 319]))
DIV_AXE = list(zip(ANS, [272, 350, 413, 349, 328]))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Le vingt-deux juin 1941. Sur un front qui va de la Baltique à la mer Noire, "
        "l'armée allemande envahit l'Union soviétique. Nom de code : opération Barbarossa.",
        "{q1}En deux cents jours, cinq millions de personnes meurent. Mille par heure, des civils pour la plupart.",
        "{-q1}{q2}Pourquoi Hitler a-t-il rompu son pacte avec Staline ? Et pourquoi cette guerre est-elle devenue, des deux côtés, une guerre sans pitié ?",
        "{-q2}{-g0}{plan}Aujourd'hui, la deuxième partie du chapitre. {plan.1}D'abord, le récit sur la carte. "
        "{plan.2}Puis les projets allemands pour l'Europe de l'Est. {plan.3}Puis Barbarossa, deuxième étude de cas. "
        "{plan.4}Puis Stalingrad et son dossier documentaire. {plan.5}Et l'épreuve : un paragraphe de composition et une analyse de document.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[25]),
        "q1": dict(type="question", t="5 millions de morts en 200 jours.", bande=True),
        "q2": dict(type="question", t="Pourquoi une guerre sans pitié ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 4 · le plan", items=[
            "La guerre à l'Est sur la carte, 1939-1943", "II.1 · Les projets allemands pour l'Europe de l'Est : trois raisons",
            "II.2 · Barbarossa : une guerre d'anéantissement", "Stalingrad, le tournant · le dossier documentaire",
            "À l'épreuve : un paragraphe de composition et une analyse de document"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · La Seconde Guerre mondiale · Épisode 4", t="Barbarossa",
                      sous="Une guerre d'anéantissement · 1939 – 1943 · partie II du cours"),
    }),

    # ================================================================ la carte : 1939-1941
    dict(id="carte1", chap="Sur la carte : 1939 – 1941", fond="nuit", humeur="tension",
         retenir="Août 1939 le pacte · sept. 1939 la Pologne partagée · été 1940 les annexions soviétiques · 22 juin 1941 Barbarossa · déc. 1941 l'arrêt devant Leningrad et Moscou.",
         beats=[
        "{g1}{g1.1}Août 1939. L'Allemagne nazie et l'Union soviétique, ennemies idéologiques jurées, signent un pacte. "
        "Hitler s'assure la neutralité de l'Union soviétique, et en secret, les deux puissances prévoient de se partager la Pologne. "
        "L'Allemagne se sent prête à conquérir son espace vital à l'Est.",
        "{g1.2}Le premier septembre, l'Allemagne envahit la Pologne. Le dix-sept, l'Armée rouge entre dans l'est du pays. "
        "En un mois, la Pologne est vaincue et partagée, de part et d'autre d'une ligne de démarcation entre Varsovie et Białystok.",
        "{g1.3}À l'été 1940, pendant que l'Allemagne écrase l'Ouest, l'Union soviétique prend sa part. "
        "Elle annexe l'Estonie, la Lettonie et la Lituanie, et elle prend à la Roumanie la Bucovine du Nord et la Bessarabie.",
        "{-g1}{g2}{g2.1}Puis, le vingt-deux juin 1941, Hitler rompt le pacte. C'est l'opération Barbarossa : trois poussées allemandes, "
        "sur un front de la Baltique à la mer Noire. Au nord vers Leningrad, au centre vers Moscou, "
        "au sud à travers l'Ukraine, vers Kiev et Rostov.",
        "{g2.2}De juin à décembre 1941, l'armée allemande s'enfonce profondément en Union soviétique. L'Armée rouge recule. "
        "Et devant l'envahisseur, les paysans brûlent leurs récoltes, emmènent leur bétail et détruisent leurs villages. C'est la terre brûlée.",
        "{g2.3}Derrière l'armée viennent les Einsatzgruppen, les unités mobiles de tuerie qui fusillent les Juifs : ce sera l'épisode cinq. "
        "{g2.4}Et sur ce front, les lois de la guerre disparaissent. Prisonniers et civils sont assassinés de façon systématique. "
        "C'est déjà une guerre d'anéantissement.",
        "{g2.5}Le six novembre, à Moscou, alors que les Allemands marchent encore sur la capitale, Staline répond : "
        "si les Allemands veulent une guerre d'anéantissement, ils l'auront. "
        "{g2.6}Et en décembre 1941, les Allemands sont arrêtés, devant Leningrad, désormais assiégée, et devant Moscou. "
        "La guerre éclair a échoué : la guerre à l'Est sera longue.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[4, 7, 19]),
        "g2": dict(type="globe", code="H3", sc=[25, 26, 27, 28, 29, 30]),
    }),

    # ================================================================ la carte : 1942-1943
    dict(id="carte2", chap="Sur la carte : 1942 – 1943", fond="nuit", humeur="tension",
         retenir="Été 1942 : la seconde offensive, vers Stalingrad et le Caucase · nov. 1942 : l'armée allemande encerclée · 31 janv. 1943 : Paulus capitule (fin des combats le 2 févr.).",
         beats=[
        "{g3}{g3.1}Été 1942. Arrêtés devant Moscou, les Allemands frappent au sud : une seconde offensive, "
        "vers la Volga et le pétrole du Caucase. Le vingt-huit juillet, l'ordre numéro deux cent vingt-sept de Staline exige : "
        "pas un pas en arrière.",
        "{g3.2}À partir d'août, les Allemands atteignent Stalingrad, sur la Volga. Les Russes la défendent à tout prix, "
        "rue par rue, usine par usine. C'est là que l'avancée allemande atteint son point extrême.",
        "{g3.3}Novembre 1942. L'Armée rouge aligne désormais plus d'hommes, plus de canons et plus de chars que les Allemands. "
        "Et ce même mois, la contre-attaque soviétique se referme sur l'armée allemande : elle est encerclée.",
        "{g3.4}Le trente et un janvier 1943, Paulus, le commandant allemand, capitule ; les derniers combattants se rendent le deux février. "
        "Environ quatre-vingt-onze mille soldats allemands sont faits prisonniers. Une défaite retentissante pour la Wehrmacht : le tournant de la guerre.",
        "{-g3}{fr1}Voici donc six dates à savoir par cœur. {fr1.1}Août 1939, le pacte. {fr1.2}Le vingt-deux juin 1941, Barbarossa. "
        "{fr1.3}Décembre 1941, l'arrêt devant Moscou. {fr1.4}L'été 1942, la seconde offensive. "
        "{fr1.5}Novembre 1942, l'encerclement. {fr1.6}Et le trente et un janvier 1943, la capitulation de Paulus.",
    ], vis={
        "g3": dict(type="globe", code="H3", sc=[36, 38, 40, 42]),
        "fr1": dict(type="frise", items=[
            dict(nom="Le pacte", d=1939, q="août"), dict(nom="Barbarossa", d=1941, q="22 juin"),
            dict(nom="Moscou", d=1941, q="décembre : l'arrêt"), dict(nom="Seconde offensive", d=1942, q="été"),
            dict(nom="Encerclement", d=1942, q="novembre"), dict(nom="Capitulation", d=1943, q="31 janvier")]),
    }),

    # ================================================================ II.1, idée 1 : le pacte
    dict(id="pacte", chap="II.1 · Le pacte ouvre la route de l'Est", fond="nuit", humeur="tension",
         retenir="Le pacte (août 1939) : neutralité soviétique + plan secret de partage de la Pologne. Pologne partagée (17 sept. 1939). L'URSS annexe les pays baltes, la Bucovine du Nord et la Bessarabie (1940).",
         beats=[
        "{def3}Passons au cours, idée par idée. Partie deux, point un : les projets allemands pour l'Europe de l'Est. "
        "Première idée : le pacte germano-soviétique {!a ouvert la route de l'Est}a ouvert la route de l'Est. "
        "Hitler s'est assuré la neutralité de l'Union soviétique, et les deux puissances ont prévu en secret de se partager la Pologne. "
        "{def3.1}L'Allemagne se sentait donc prête à conquérir son {!Lebensraum}Lebensraum, l'espace vital à l'Est annoncé dans Mein Kampf.",
        "{-def3}{sl}Un document du cours le montre en trois images. {sl.1}Staline et Ribbentrop se serrent la main après la signature. "
        "{sl.2}Les axes de l'invasion allemande du premier septembre 1939. "
        "{sl.3}Et l'Europe de l'Est après le pacte : la ligne germano-soviétique passe entre Varsovie et Białystok, "
        "et entre Lublin et Lvov. {sl.4}Sur cette carte, les annexions soviétiques de 1940 : l'Estonie, la Lettonie et la Lituanie, "
        "ainsi que la Bucovine du Nord et la Bessarabie, prises à la Roumanie.",
        "{-sl}{lec2}Pour ta copie : les deux dictatures se partagent l'Europe de l'Est. Mais pour Hitler, ce n'est qu'une étape : "
        "l'espace vital qu'il veut à l'Est, c'est le territoire soviétique.",
    ], vis={
        "def3": dict(type="def", cles=["neutralité", "secret", "Pologne"], terme="Le pacte germano-soviétique · août 1939",
                     t="Hitler s'assure la neutralité de l'URSS ; en secret, les deux puissances prévoient de se partager la Pologne.",
                     etape="Étape suivante : le Lebensraum, l'espace vital à l'Est annoncé dans Mein Kampf", x=170, y=200, w=940),
        "sl": dict(type="liste", titre="Un document du cours", items=[
            "Staline et Ribbentrop se serrent la main après la signature", "Les axes de l'invasion allemande, 1er septembre 1939",
            "La ligne germano-soviétique : Varsovie–Białystok, Lublin–Lvov", "1940 : pays baltes, Bucovine du Nord, Bessarabie annexés par l'URSS"],
            x=150, y=130, w=980),
        "lec2": dict(type="note", terme="Pour la composition", cles=["étape", "soviétique"],
                     t="Le pacte n'est qu'une étape : l'espace vital que veut Hitler à l'Est, c'est le territoire soviétique.",
                     etape="1939-1941 : les deux dictatures se partagent l'Europe de l'Est", x=170, y=200, w=940),
    }),

    # ================================================================ II.1, idée 2 : la raison économique
    dict(id="raisons", chap="II.1 · Pourquoi envahir l'URSS ? La raison économique", fond="nuit", humeur="tension",
         retenir="Raison économique : le Grossraum, un Reich agrandi et autosuffisant · la germanisation : colons allemands, Slaves asservis · les ressources (terres agricoles, minerais, pétrole) pour l'autarcie et une guerre longue. Exemple : Stalingrad et le pétrole du Caucase.",
         beats=[
        "{g4}{g4.1}Alors pourquoi Hitler a-t-il envahi l'Union soviétique ? Le cours donne trois raisons, la colonne vertébrale "
        "de toute composition sur cette partie : {!économique, idéologique, raciale}une raison économique, une raison idéologique et une raison raciale. "
        "Regarde la carte : l'Ukraine, le Caucase, Moscou. Tout ce que voulait l'Allemagne était là.",
        "{-g4}{eco}Première raison, la raison économique. {eco.1}Hitler voulait un {!Grossraum}Grossraum, un grand espace : "
        "un Troisième Reich agrandi, capable de vivre de ses propres ressources. "
        "{eco.2}À l'Est, des colons allemands seraient installés, et les populations slaves réduites en esclavage : "
        "c'est le projet de {!germanisation}germanisation de l'Est. "
        "{eco.3}Et les ressources naturelles de l'Union soviétique, ses terres agricoles, ses minerais, son pétrole, étaient une nécessité économique : "
        "pour atteindre l'autarcie, et pour mener une guerre longue.",
        "{eco.4}L'exemple vient du dossier documentaire. Stalingrad comptait parce que c'était un grand centre industriel et un nœud de transport sur la Volga, "
        "qui assurait aux Soviétiques l'accès au pétrole du Caucase. Un pétrole dont l'économie de guerre allemande avait besoin.",
    ], vis={
        "g4": dict(type="globe", code="H3", sc=[24]),
        "eco": dict(type="liste", titre="1 · La raison économique", cles=["Grossraum", "germanisation", "ressources"], items=[
            "Le Grossraum : un Troisième Reich agrandi, autosuffisant", "La germanisation : colons allemands, Slaves asservis",
            "Les ressources : terres, minerais, pétrole → autarcie, guerre longue", "Exemple : Stalingrad, la Volga, le pétrole du Caucase (dossier)"],
            x=150, y=130, w=980),
    }),

    # ================================================================ II.1, idées 3 et 4 : idéologique et raciale
    dict(id="raisons2", chap="II.1 · Les raisons idéologique et raciale", fond="guerre", humeur="tension",
         retenir="Idéologique : la croisade contre le « judéo-bolchevisme » (l'ordre des commissaires, rédigé en mai, signé le 6 juin 1941 : les commissaires « liquidés par les armes »). Raciale : l'Übermensch contre l'Untermensch (l'ordre de Reichenau, 10 oct. 1941).",
         beats=[
        "{def6}Deuxième raison, la raison idéologique. Deux populations étaient vues comme hostiles et dangereuses pour la domination allemande à l'Est : "
        "les dirigeants communistes, et les Juifs. La propagande nazie qualifiait l'Union soviétique de régime {!judéo-bolchevique}judéo-bolchevique, "
        "en fondant l'ennemi politique et l'ennemi racial en un seul. "
        "{def6.1}Cette guerre n'était donc pas seulement une conquête. C'était une guerre contre une vision du monde.",
        "{-def6}L'exemple : le document un du dossier, l'ordre des commissaires, rédigé en mai 1941 et signé le six juin par le haut commandement de la Wehrmacht. "
        "Il désigne les commissaires politiques, les cadres communistes, comme",
        ("C", "les instigateurs de méthodes de combat barbares et asiatiques", "c_jodl"),
        "{-c_jodl}{jodl}Une fois capturés, ils doivent être liquidés par les armes, par principe. Fusillés sur place.",
        "{-jodl}{def7}Troisième raison, la raison raciale. Les nazis étaient convaincus d'appartenir à l'{!Übermensch}Übermensch aryen, "
        "le surhomme, au-dessus de l'Untermensch slave, le sous-homme. "
        "Les Slaves devaient être asservis, ou chassés pour faire place aux colons allemands. Et les Juifs devaient être éliminés. "
        "{def7.1}Cette hiérarchie raciale, vue au chapitre deux, fait de la campagne de l'Est une guerre de destruction dès le départ.",
        "{-def7}L'exemple : le document deux, l'ordre du maréchal Walther von Reichenau sur la conduite des troupes à l'Est, le dix octobre 1941. Il appelle à",
        ("C", "l'extermination de l'influence asiatique dans la civilisation européenne", "c_rei1"),
        "{-c_rei1}et à une expiation sévère mais juste, imposée à ce qu'il appelle",
        ("C", "la sous-humanité juive", "c_rei2"),
        "{-c_rei2}{tab3}Voici donc le tableau à recopier : trois raisons, un exemple chacune. "
        "{tab3.1}Économique : Stalingrad et le pétrole du Caucase. {tab3.2}Idéologique : l'ordre des commissaires. {tab3.3}Raciale : l'ordre de Reichenau. "
        "Et remarque le lien : le mot judéo-bolchevisme mêle déjà l'ennemi idéologique et l'ennemi racial.",
        ("P", 4.0),
    ], vis={
        "def6": dict(type="def", cles=["communistes", "Juifs", "seul"], terme="2 · La raison idéologique : le « judéo-bolchevisme »",
                     t="Dirigeants communistes et Juifs : l'ennemi politique et l'ennemi racial fondus en un seul.",
                     etape="Pas seulement une conquête : une guerre contre une vision du monde", x=170, y=200, w=940),
        "c_jodl": dict(type="cit", a="Haut commandement de la Wehrmacht", o="Ordre des commissaires, rédigé en mai, signé le 6 juin 1941 (dossier, document 1)", x=200, y=190, w=880),
        "jodl": dict(type="note", terme="Document 1 · l'ordre des commissaires, 6 juin 1941", cles=["armes", "principe"],
                     t="Les commissaires politiques capturés doivent être « liquidés par les armes », par principe.",
                     etape="Fusillés sur place : les lois de la guerre ne s'appliquent plus", x=170, y=200, w=940),
        "def7": dict(type="def", cles=["Übermensch", "Untermensch", "éliminés"], terme="3 · La raison raciale",
                     t="L'« Übermensch » aryen au-dessus de l'« Untermensch » slave : Slaves asservis ou chassés, Juifs éliminés.",
                     etape="Une hiérarchie raciale (chapitre 2) → une guerre de destruction dès le départ", x=170, y=200, w=940),
        "c_rei1": dict(type="cit", a="Le maréchal Walther von Reichenau", o="Ordre sur la conduite des troupes à l'Est, 10 octobre 1941 (dossier, document 2)", x=200, y=190, w=880),
        "c_rei2": dict(type="cit", a="Le maréchal Walther von Reichenau", o="Ordre sur la conduite des troupes à l'Est, 10 octobre 1941 (dossier, document 2)", x=200, y=210, w=880),
        "tab3": dict(type="liste", titre="Pourquoi envahir l'URSS ? · raison → exemple", items=[
            "Économique : Grossraum, germanisation, ressources → Stalingrad, pétrole du Caucase",
            "Idéologique : la croisade contre le « judéo-bolchevisme » → l'ordre des commissaires, juin 1941",
            "Raciale : Übermensch / Untermensch → l'ordre de Reichenau, 10 oct. 1941"], x=130, y=150, w=1020),
    }),

    # ================================================================ II.2, idées 1 et 2 : Barbarossa
    dict(id="barbarossa", chap="II.2 · L'opération Barbarossa", fond="guerre", humeur="tension",
         retenir="22 juin 1941 : Barbarossa, une croisade contre le communisme. Trois poussées : Leningrad · Moscou · Kiev et Rostov, avec les alliés de l'Allemagne. Arrêtée devant Leningrad et Moscou : 200 jours, 5 millions de morts.",
         beats=[
        "{g5}{g5.1}Partie deux, point deux : l'opération Barbarossa, une guerre d'anéantissement, deuxième étude de cas. "
        "Première idée. Le vingt-deux juin 1941, Hitler rompt le pacte Molotov-Ribbentrop. "
        "La Wehrmacht voit cette guerre comme une {!croisade contre le communisme}croisade contre le communisme.",
        "{thr}Deuxième idée : trois poussées sur un front immense, de la Baltique à la mer Noire. "
        "{thr.1}Au nord, à travers les pays baltes, vers Leningrad. {thr.2}Au centre, par Minsk et Smolensk, vers Moscou. "
        "{thr.3}Au sud, par l'Ukraine et Kiev, vers Rostov. "
        "{thr.4}Et l'Allemagne ne se bat pas seule : la carte du cours désigne comme ses alliés la Finlande, la Roumanie, la Hongrie, la Slovaquie, l'Italie et la Croatie.",
        "{-thr}{-g5}{att}Attention. Une seconde carte du cours, intitulée Opération Barbarossa, place Stalingrad parmi les trois objectifs. "
        "Mais en 1941, la poussée du sud vise l'Ukraine, Kiev et Rostov. "
        "{att.1}Stalingrad et le Caucase sont les cibles de la seconde offensive, à l'été 1942. Dans ta copie, écris-le ainsi.",
        "{-att}{bil2}Jusqu'en décembre 1941, les Allemands s'enfoncent profondément en Union soviétique, mais la résistance croissante de l'Armée rouge "
        "les arrête devant Leningrad et Moscou. La guerre éclair, qui avait gagné en six semaines en France, échoue dans l'immensité russe. "
        "Et le bilan de ces deux cents premiers jours : cinq millions de morts. En moyenne, {!mille par heure}mille personnes tuées chaque heure, "
        "des civils pour la plupart.",
    ], vis={
        "g5": dict(type="globe", code="H3", sc=[25]),
        "thr": dict(type="liste", titre="Trois poussées, juin 1941", petit=True, bande=True, x=60, y=130, w=560, items=[
            "Nord : pays baltes → Leningrad", "Centre : Minsk, Smolensk → Moscou", "Sud : Ukraine, Kiev → Rostov",
            "Alliés : Finlande, Roumanie, Hongrie, Slovaquie, Italie, Croatie"]),
        "att": dict(type="note", terme="Attention · une carte du cours", cles=["Rostov", "seconde"],
                    t="1941 : Leningrad, Moscou, Kiev et Rostov. Stalingrad et le Caucase : la seconde offensive, été 1942.",
                    etape="La carte « Opération Barbarossa » place Stalingrad parmi les objectifs : pas en 1941", x=170, y=200, w=940),
        "bil2": dict(type="mot", t="5 millions de morts", g="200 jours de guerre · mille par heure, surtout des civils", y=250, taille=86),
    }),

    # ================================================================ II.2, idée 3 : du côté soviétique
    dict(id="sovietique", chap="II.2 · Du côté soviétique", fond="nuit", humeur="tension",
         retenir="L'Armée rouge, « décapitée » par les Grandes Purges (surtout 1937-1938), recule mais ne s'effondre pas. Terre brûlée : récoltes brûlées, bétail emmené, villages détruits.",
         beats=[
        "{sov}Troisième idée : que se passe-t-il du côté soviétique ? Deux choses. {sov.g}D'abord, une armée affaiblie. L'Armée rouge est désorganisée, "
        "{!décapitée}décapitée, dit le cours, par les Grandes Purges, qui ont détruit une grande partie de ses cadres. "
        "Un exemple hors du cours : le maréchal Toukhatchevski, son principal stratège, est fusillé en juin 1937, "
        "et des milliers d'officiers sont renvoyés ou arrêtés.",
        "{sov.d}Ensuite, une population qui ne laisse rien derrière elle. Les paysans russes fuient devant les Allemands, "
        "en brûlant leurs récoltes, en emmenant leur bétail et en détruisant leurs villages : "
        "c'est la politique de la {!terre brûlée}terre brûlée. L'envahisseur ne trouve rien pour vivre.",
        "{-sov}{dat}Une date à corriger : le cours place ces purges en 1938. La grande purge de l'armée a eu lieu surtout "
        "en 1937 et 1938, comme le dit le chapitre deux.",
        "{-dat}{res}Et le point clé de cette idée : l'Armée rouge recule… mais elle ne s'effondre pas. "
        "Sa résistance arrête les Allemands devant Leningrad et Moscou.",
    ], vis={
        "sov": dict(type="cols", g="Une armée affaiblie", gq="« décapitée » par les Grandes Purges : une grande partie de ses cadres détruits",
                    d="La terre brûlée", dq="récoltes brûlées, bétail emmené, villages détruits", vs="+",
                    repere="Toukhatchevski fusillé, juin 1937 (hors du cours)"),
        "dat": dict(type="note", terme="Attention · une date", cles=["purge", "surtout"],
                    t="La grande purge de l'armée : surtout 1937-1938 (le cours dit 1938).",
                    etape="Le chapitre 2 donne 1937-1938", x=170, y=200, w=940),
        "res": dict(type="question", t="Elle recule… mais elle ne s'effondre pas."),
    }),

    # ================================================================ II.2, idée 4 : la réponse de Staline
    dict(id="staline", chap="II.2 · La réponse de Staline", fond="guerre", humeur="tension",
         retenir="6 nov. 1941, Moscou : Staline retourne contre les nazis leur propre mot, Vernichtungskrieg : anéantir les envahisseurs « jusqu'au dernier ». Des deux côtés, une guerre sans pitié.",
         beats=[
        "{g6}{g6.1}Quatrième idée : la réponse de Staline. Le six novembre 1941, à Moscou, à la veille de l'anniversaire de la révolution. "
        "Les troupes allemandes marchent encore sur la capitale. "
        "Staline reprend le mot même des nazis, {!Vernichtungskrieg}Vernichtungskrieg, guerre d'anéantissement… et le retourne contre eux.",
        "{-g6}",
        ("C", "Eh bien, si les Allemands veulent une guerre d'anéantissement, ils l'auront.", "c_st1"),
        "{-c_st1}Dans le texte du discours, cette phrase est suivie d'applaudissements tumultueux et prolongés. Puis : la tâche est désormais",
        ("C", "d'anéantir jusqu'au dernier tous les Allemands qui ont pénétré sur le territoire de notre patrie pour l'occuper. "
              "Pas de pitié pour les occupants allemands !", "c_st2"),
        "{-c_st2}{miroir}Tous les peuples de l'Union soviétique doivent désormais anéantir les envahisseurs jusqu'au dernier. "
        "{miroir.g}Côté allemand, l'ennemi est un sous-homme : l'ordre des commissaires, l'ordre de Reichenau. "
        "{miroir.d}Côté soviétique : pas de pitié. {!Anéantissement contre anéantissement}Anéantissement contre anéantissement. "
        "Des deux côtés, la guerre à l'Est est déclarée sans pitié : voilà pourquoi on parle de guerre d'anéantissement.",
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[29]),
        "c_st1": dict(type="cit", a="Joseph Staline", o="discours, Moscou, 6 novembre 1941 (traduction française)", x=200, y=210, w=880),
        "c_st2": dict(type="cit", a="Joseph Staline", o="discours, Moscou, 6 novembre 1941 (traduction française)", x=200, y=170, w=880),
        "miroir": dict(type="cols", g="Allemagne", gq="l'ennemi « sous-homme » : l'ordre des commissaires, l'ordre de Reichenau",
                       d="URSS", dq="« Pas de pitié pour les occupants allemands ! » Staline, 6 nov. 1941", vs="=",
                       repere="Anéantissement contre anéantissement"),
    }),

    # ================================================================ II.2, idée 5 : une guerre d'anéantissement
    dict(id="aneantissement", chap="II.2 · Une guerre d'anéantissement", fond="guerre", humeur="tension",
         retenir="Plus de lois de la guerre : les crimes de guerre deviennent le cours normal de la guerre. Prisonniers soviétiques : environ 2,8 millions tués (juin 1941 – févr. 1942) ; au total 3,3 millions morts en captivité sur 5,7, près de 6 sur 10 ; Auschwitz-Birkenau d'abord construit pour eux. Les 3/5 des morts de la guerre sur le front de l'Est.",
         beats=[
        "{def4}Cinquième idée. Sur le front de l'Est, les lois de la guerre disparaissent. La violence est sans précédent : "
        "le seul but est la destruction totale de l'ennemi… ou la résistance jusqu'à la mort. "
        "{def4.1}Les crimes de guerre deviennent le cours normal de la guerre : le meurtre ou les mauvais traitements infligés aux civils et aux prisonniers, "
        "et une violence sans objectif militaire clair.",
        "{-def4}{pow}L'exemple le plus net : les prisonniers de guerre soviétiques. {pow.1}Environ deux virgule huit millions d'entre eux ont été tués "
        "par les forces armées allemandes et les unités spéciales entre juin 1941 et février 1942, surtout par la famine. "
        "{pow.2}Au total, environ trois virgule trois millions des cinq virgule sept millions de prisonniers soviétiques sont morts en captivité allemande : près de six sur dix. "
        "{pow.3}Et le document huit du dossier : le camp d'Auschwitz-Birkenau a d'abord été construit pour les prisonniers soviétiques, "
        "et le gazage leur a été appliqué en premier… puis aux Juifs.",
        "{-pow}{fig}Attention : le texte du cours donne environ deux virgule huit millions ; le document huit du dossier donne "
        "deux millions de morts en février 1942. Cite toujours le document que tu utilises.",
        "{-fig}{frac}Résultat : {!trois cinquièmes}les trois cinquièmes de tous les morts de la Seconde Guerre mondiale "
        "sont tombés sur le front de l'Est.",
    ], vis={
        "def4": dict(type="def", cles=["destruction", "totale", "lois"], terme="Notion clé · la guerre d'anéantissement (Vernichtungskrieg)",
                     t="Une guerre qui vise la destruction totale de l'ennemi, sans lois de la guerre.",
                     etape="Les crimes de guerre, cours normal de la guerre : civils et prisonniers assassinés ou maltraités", x=170, y=200, w=940),
        "pow": dict(type="liste", titre="Les prisonniers de guerre soviétiques", cles=["famine", "captivité", "gazage"], items=[
            "≈ 2,8 millions tués, juin 1941 – févr. 1942, surtout par la famine", "Au total, 3,3 millions morts en captivité sur 5,7 : près de 6 sur 10",
            "Auschwitz-Birkenau d'abord construit pour eux ; le gazage appliqué à eux d'abord, puis aux Juifs (document 8)"],
            x=150, y=140, w=980),
        "fig": dict(type="note", terme="Attention · deux chiffres", cles=["cours", "document"],
                    t="Texte du cours : ≈ 2,8 millions tués (juin 1941 – févr. 1942). Dossier, document 8 : 2 millions de morts en févr. 1942.",
                    etape="Cite le document que tu utilises", x=170, y=200, w=940),
        "frac": dict(type="mot", t="3/5", g="des morts de la Seconde Guerre mondiale sont tombés sur le front de l'Est", y=240, taille=150),
    }),

    # ================================================================ II.2, idée 6 : Stalingrad, le tournant
    dict(id="stalingrad", chap="II.2 · Stalingrad, le tournant", fond="nuit", humeur="tension",
         retenir="Pourquoi défendre Stalingrad ? Un bastion de la stratégie défensive de Staline · un centre industriel et de transport sur la Volga · l'accès au pétrole du Caucase · la ville de Staline. Ordre n° 227 · encerclement en nov. 1942 · Paulus capitule le 31 janv. 1943 (dernières troupes le 2 févr.) : environ 91 000 prisonniers.",
         beats=[
        "{g7}{g7.1}Sixième idée : Stalingrad, le tournant de la guerre. Leningrad, Moscou et Stalingrad sont les bastions de la défense soviétique. "
        "À l'été 1942, les Allemands, euphoriques, foncent vers la Volga et le Caucase. Et Stalingrad leur barre la route.",
        "{g7.2}Les Russes défendent la ville à tout prix. Pourquoi ? Quatre raisons, à apprendre sous forme de liste : "
        "c'est aussi une question du dossier.",
        "{-g7}{why}{why.1}Un : Stalingrad est un bastion de la stratégie défensive de Staline. "
        "{why.2}Deux : c'est un grand centre industriel et un nœud de transport sur la Volga. "
        "{why.3}Trois : la ville assure aux Soviétiques l'accès au pétrole du Caucase, stratégique pour la suite du conflit, et pour l'approvisionnement allemand en pétrole. "
        "{why.4}Et quatre : c'est un symbole. La ville porte le nom de Staline.",
        "{-why}D'où l'ordre numéro deux cent vingt-sept de Staline, du vingt-huit juillet 1942.",
        ("C", "Il est temps d'en finir avec la retraite. Pas un pas en arrière !", "c_227"),
        "{-c_227}{eta}La bataille, étape par étape. {eta.1}Été 1942 : l'euphorie. Les Allemands atteignent la Volga le vingt-trois août. "
        "{eta.2}Septembre et octobre : on se bat rue par rue, usine par usine : l'usine Barricades, Octobre rouge. "
        "{eta.3}Fin novembre : l'armée allemande est encerclée. {eta.4}Puis l'hiver, et la famine. "
        "{eta.5}Et le trente et un janvier 1943, Paulus, commandant de l'armée allemande, capitule ; les dernières troupes se rendent le deux février. "
        "Environ quatre-vingt-onze mille soldats allemands sont faits prisonniers ; le dossier dit quatre-vingt-quinze mille. Une défaite retentissante pour la Wehrmacht.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[36, 38]),
        "why": dict(type="liste", titre="Pourquoi défendre Stalingrad à tout prix ?", cles=["stratégie", "Volga", "pétrole", "symbole"], items=[
            "Un bastion de la stratégie défensive de Staline", "Un grand centre industriel et de transport sur la Volga",
            "L'accès au pétrole du Caucase : stratégique pour les deux camps", "Un symbole : la ville qui porte le nom de Staline"], x=170, y=140, w=940),
        "c_227": dict(type="cit", a="Joseph Staline", o="Ordre n° 227, 28 juillet 1942 (dossier, document 3)", x=200, y=210, w=880),
        "eta": dict(type="liste", titre="La bataille en cinq étapes", items=[
            "Été 1942 : l'euphorie ; la Volga atteinte le 23 août", "Sept.-oct. : rue par rue, usine par usine",
            "Fin novembre : l'armée allemande encerclée", "L'hiver : la famine",
            "31 janv. 1943 : Paulus capitule · ≈ 91 000 prisonniers"], x=150, y=130, w=980),
    }),

    # ================================================================ II.2, idée 7 : le rapport de forces
    dict(id="forces", chap="II.2 · Le rapport de forces s'est inversé", fond="nuit", humeur="lumiere",
         retenir="Stalingrad, nov. 1942 (Allemands / Soviétiques) : hommes 1 011 500 / 1 143 500 · canons 10 290 / 13 541 · chars 675 / 894 · avions 1 216 / 1 115. En 1944, l'URSS aligne à elle seule plus de divisions que tout l'Axe : 400 contre 349.",
         beats=[
        "{gf}Septième idée : en novembre 1942, le rapport de forces s'est inversé en faveur des Soviétiques. "
        "Voici le tableau du cours des forces en présence à Stalingrad. {gf.1}Les Allemands en rouge, {gf.2}les Soviétiques en bleu. "
        "{gf.3}{gf.4}{gf.5}Les hommes : environ un million onze mille Allemands, contre un million cent quarante-trois mille Soviétiques.",
        "{gf.6}{gf.7}{gf.8}Les canons : environ dix mille, contre treize mille cinq cents. "
        "{gf.9}{gf.10}{gf.11}Les chars : six cent soixante-quinze, contre huit cent quatre-vingt-quatorze. "
        "{gf.12}{gf.13}{gf.14}Il n'y a qu'en avions que les Allemands sont légèrement devant.",
        "{-gf}{gd2}Malgré ses pertes énormes de 1941, l'Union soviétique mobilise plus vite que l'Allemagne. "
        "Le tableau des divisions de l'introduction le confirme. {gd2.1}Divisions soviétiques : deux cents en 1940, trois cent cinquante en 1943, quatre cent quatre-vingt-huit en 1945. "
        "{gd2.2}L'Allemagne culmine à trois cent quarante-sept, en 1944. "
        "{gd2.3}Et en 1944, l'Union soviétique aligne à elle seule plus de divisions que tout l'Axe : quatre cents contre trois cent quarante-neuf, "
        "sans compter le Japon. {gd2.4}Et ce même mois de novembre 1942, l'armée allemande est encerclée.",
    ], vis={
        "gf": dict(type="graphe", titre="Forces à Stalingrad, novembre 1942 (tableau du cours)", x=300, y=110, w=680, h=520,
                   ax=AX_BARRES, el=barres(FORCES, "ca", "el")),
        "gd2": dict(type="graphe", titre="Divisions, 1940-1945 (tableau du cours)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1939.5, 1945.5], y=[0, 520], gx=ANS, gy=[100, 200, 300, 400, 500], lx="année", ly="divisions"),
                    el=[dict(type="courbe", pts=[list(p) for p in DIV_URSS], c="el", lbl="URSS", lp=[1944.8, 505], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_ALL], c="ca", lbl="Allemagne", lp=[1942.3, 205], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_AXE], c="sa", tir=True, lbl="tout l'Axe", lp=[1941.2, 380], dur=1.8),
                        dict(type="points", pts=[[1944, 400], [1944, 349]], c="iv", lbl="1944 : 400 / 349", lp=[1943.6, 455])]),
    }),

    # ================================================================ II.2, idée 8 : une guerre totale
    dict(id="totale", chap="II.2 · Stalingrad, une guerre totale", fond="guerre", humeur="tension",
         retenir="Guerre totale = mobilisation de toutes les ressources d'une société + effacement de la limite entre front et arrière (vu en Première). Stalingrad : usines de l'arrière, combats de rue au milieu des civils, propagande, aucune reddition. Bilan (document 7) : URSS 1,13 million (500 000 tués), Allemagne et alliés 760 000. L'URSS dans la guerre : 27 à 28 millions de morts, un habitant sur sept.",
         beats=[
        "{def5}Huitième idée : Stalingrad correspond à la définition de la guerre totale. Souviens-toi de la définition vue en Première : "
        "la guerre totale, c'est {!la mobilisation de toutes les ressources d'une société}la mobilisation de toutes les ressources d'une société, "
        "{def5.1}et l'effacement de la limite entre le front et l'arrière.",
        "{-def5}{crit}Stalingrad remplit tous les critères. {crit.1}Toute l'économie est derrière le front : dans le document trois, les usines de l'arrière "
        "envoient toujours plus d'avions, de chars et de canons. "
        "{crit.2}Les combats se déroulent rue par rue et usine par usine, avec des civils au milieu du champ de bataille. "
        "{crit.3}La propagande, des deux côtés : le document cinq, une affiche bolchevique de 1943, avec Stalingrad écrit sur le drapeau. "
        "{crit.4}Et le refus de toute reddition, jusqu'à la mort ou la capture.",
        "{-crit}Les lettres d'un soldat allemand, le document six, montrent la descente. Au début :",
        ("C", "prendre Stalingrad n'est pas difficile", "c_l1"),
        "{-c_l1}Puis des semaines de combats pour l'usine Barricades, l'encerclement, et le vingt-six décembre :",
        ("C", "les chevaux ont déjà été mangés", "c_l2"),
        "{-c_l2}{gt}Et le bilan de la bataille, document sept. {gt.1}{gt.2}{gt.3}{gt.4}{gt.5}L'Union soviétique a perdu un million cent trente mille soldats et civils, "
        "tués, blessés ou capturés, dont cinq cent mille tués. L'Allemagne et ses alliés en ont perdu sept cent soixante mille. "
        "{gt.6}{gt.7}{gt.8}Chars perdus : quatre mille trois cent quarante et un, contre cinq cents. "
        "{gt.9}{gt.10}{gt.11}Avions : deux mille sept cent soixante-neuf, contre neuf cents.",
        "{-gt}{urss}L'Union soviétique a payé le prix le plus lourd de toute la guerre. Les pertes soviétiques sont aujourd'hui estimées officiellement "
        "à vingt-sept ou vingt-huit millions : {!un sur sept}un habitant sur sept de la population d'avant-guerre.",
    ], vis={
        "def5": dict(type="def", cles=["ressources", "front", "arrière"], terme="Notion clé · la guerre totale (vue en Première)",
                     t="La mobilisation de toutes les ressources d'une société…",
                     etape="… et l'effacement de la limite entre le front et l'arrière", x=170, y=200, w=940),
        "crit": dict(type="liste", titre="Stalingrad, une guerre totale : quatre critères", cles=["économie", "civils", "propagande", "reddition"], items=[
            "Toute l'économie derrière le front : les usines de l'arrière (document 3)", "Rue par rue, usine par usine : des civils sur le champ de bataille",
            "La propagande des deux côtés : l'affiche de 1943 (document 5)", "Aucune reddition, jusqu'à la mort ou la capture"], x=150, y=130, w=980),
        "c_l1": dict(type="cit", a="Un soldat allemand", o="lettres, juillet-décembre 1942 (dossier, document 6)", x=200, y=230, w=880),
        "c_l2": dict(type="cit", a="Un soldat allemand", o="lettre, 26 décembre 1942 (dossier, document 6)", x=200, y=230, w=880),
        "gt": dict(type="graphe", titre="Le bilan de Stalingrad (dossier, document 7)", x=300, y=110, w=680, h=520,
                   ax=dict(AX_BARRES, x=[0.35, 3.65]), el=barres(PERTES, "ca", "el")),
        "urss": dict(type="mot", t="27 à 28 millions", g="pertes soviétiques dans la guerre : un habitant sur sept d'avant-guerre", y=250, taille=90),
    }),

    # ================================================================ le dossier documentaire
    dict(id="ws3", chap="Le dossier documentaire · les réponses clés", fond="aube", humeur="calme",
         retenir="Le dossier : l'ennemi déshumanisé et assassiné (documents 1, 2, 8) · cinq étapes de la bataille · une brutalité extrême · quatre raisons de défendre la ville · guerre totale : largement.",
         beats=[
        "{wsrc}Maintenant, le dossier documentaire : la bataille de Stalingrad, une guerre d'anéantissement. Sept documents : "
        "{wsrc.1}l'ordre des commissaires, {wsrc.2}l'ordre de Reichenau, {wsrc.3}l'ordre numéro deux cent vingt-sept de Staline, "
        "{wsrc.4}une affiche et des photographies, {wsrc.5}les lettres d'un soldat, {wsrc.6}le bilan, {wsrc.7}les prisonniers soviétiques.",
        "{-wsrc}{wq}Cinq questions, avec leurs réponses clés, proposées par le site, sauf la quatrième, donnée par le cours. "
        "{wq.1}Un : dans les ordres allemands, l'ennemi est déshumanisé : barbare, asiatique, sous-homme ; les commissaires fusillés, les prisonniers affamés, "
        "les premiers gazés. {wq.2}Deux : les étapes, que tu connais maintenant. "
        "{wq.3}Trois : la brutalité : beaucoup de croix surmontées de nos casques, écrit le soldat ; des hommes qui mangent les chevaux, "
        "qui ressemblent à des cadavres ou à des fous. {wq.4}Quatre : les quatre raisons de défendre la ville. "
        "{wq.5}Et cinq : la guerre totale. Celle-là, c'est toi qui vas la rédiger.",
    ], vis={
        "wsrc": dict(type="liste", titre="Le dossier · les documents", marques=["1", "2", "3", "5", "6", "7", "8"], petit=True, items=[
            "L'ordre des commissaires, mai-juin 1941", "L'ordre de Reichenau, 10 oct. 1941", "L'ordre n° 227 de Staline, 28 juillet 1942",
            "Une affiche bolchevique (1943) ; des photographies de soldats", "Les lettres d'un soldat allemand, juillet-déc. 1942",
            "Le bilan de la bataille", "Les prisonniers de guerre soviétiques"], x=170, y=90, w=940),
        "wq": dict(type="liste", titre="Le dossier · les réponses clés", petit=True, items=[
            "Ennemis déshumanisés : « barbares », « asiatiques », « sous-humanité » · commissaires fusillés, prisonniers affamés, premiers gazés",
            "Contexte et étapes : Barbarossa arrêtée → euphorie → rues → encerclement → faim → 31 janv. 1943",
            "Brutalité : usine par usine, « des croix surmontées de nos casques », chevaux mangés",
            "Pourquoi la défendre : stratégie, nœud de la Volga, pétrole du Caucase, ville de Staline (réponse du cours)",
            "Guerre totale ? → à toi"], x=130, y=110, w=1020),
    }),

    # ================================================================ à toi : un paragraphe de composition
    dict(id="essai", chap="À toi · un paragraphe de composition", fond="aube", humeur="calme",
         retenir="Un paragraphe : idée directrice (largement) · définition · arguments et exemples précis (usines de l'arrière, combats de rue, propagande et ordre n° 227, le bilan) · nuance (une bataille localisée, mais au cœur d'une guerre totale).",
         beats=[
        "{ex5}Voici la question cinq du dossier, traitée comme un paragraphe de composition. "
        "{!Dans quelle mesure}Dans quelle mesure la bataille de Stalingrad correspond-elle à la définition de la guerre totale ?",
        "{-ex5}{pa4}",
        ("P", 2.0),
        "{-pa4}{mod4}Voici un paragraphe modèle. La bataille de Stalingrad correspond largement à la définition de la guerre totale, "
        "c'est-à-dire la mobilisation de toutes les ressources d'une société et l'effacement de la limite entre le front et l'arrière. "
        "D'abord, toute l'économie soviétique se trouvait derrière le front : dans le document trois, les usines de l'arrière envoient toujours plus d'avions, "
        "de chars et de canons. Ensuite, les combats se sont déroulés dans une ville habitée, rue par rue et usine par usine, "
        "comme dans la lutte pour l'usine Barricades. Enfin, la propagande a mobilisé les esprits des deux côtés, et aucune reddition n'était acceptée : "
        "l'ordre numéro deux cent vingt-sept exigeait pas un pas en arrière. "
        "{mod4.1}Une nuance : Stalingrad est restée une bataille militaire localisée. Mais elle était au cœur d'une guerre totale, "
        "menée sur tout le front de l'Est.",
    ], vis={
        "ex5": dict(type="exo", niveau="essay", titre="Dans quelle mesure la bataille de Stalingrad correspond-elle à la définition de la guerre totale ?",
                    src="Dossier documentaire, question 5", enonce=["Un paragraphe : idée directrice, définition, arguments et exemples, nuance"]),
        "pa4": dict(type="pause", t="Rédige le paragraphe : une idée directrice, la définition, trois arguments avec un exemple précis, une nuance.",
                    sous="Mets la vidéo en pause, rédige-le sur une feuille, puis relance pour voir un modèle."),
        "mod4": dict(type="note", terme="Paragraphe modèle", cles=["largement", "économie", "ville", "propagande"],
                     t="Largement : l'économie derrière le front (document 3), des combats dans une ville habitée (l'usine Barricades), "
                       "la propagande et « Pas un pas en arrière ! », 1,13 million de pertes soviétiques.",
                     etape="Nuance : une bataille localisée… mais au cœur d'une guerre totale sur tout le front de l'Est", x=150, y=170, w=980),
    }),

    # ================================================================ à toi : une analyse de document
    dict(id="dbq", chap="À toi · une analyse de document", fond="guerre", humeur="tension",
         retenir="Analyse de document : présentation · contexte · intérêt (un témoin direct, des dates qui suivent les étapes, le coût humain) · limites (un seul soldat allemand, pas de chiffres, s'arrête en décembre, des lettres à la famille).",
         beats=[
        "{ex6}Maintenant, une analyse de document, sur un document du dossier. {!En quoi}En quoi le document six, les lettres d'un soldat allemand "
        "de juillet à décembre 1942, permet-il de comprendre la bataille de Stalingrad ? Et quelles en sont les limites ?",
        "{-ex6}{str2}La démarche. {str2.1}D'abord, présenter le document : sa nature, son auteur, sa date. "
        "{str2.2}Le situer dans son contexte. {str2.3}Montrer son intérêt, avec plusieurs arguments. "
        "{str2.4}Puis ses limites, avec plusieurs arguments : c'est le bilan critique.",
        "{-str2}{pa5}",
        ("P", 2.0),
        "{-pa5}{rep5}Un modèle. {rep5.1}Le document six est une série de lettres écrites par un soldat allemand entre juillet et décembre 1942, "
        "pendant la bataille elle-même. {rep5.2}Elles sont écrites pendant la seconde offensive allemande vers la Volga, "
        "jusqu'à l'encerclement de l'armée allemande.",
        "{rep5.3}Son intérêt. C'est un témoignage direct, de l'intérieur de la bataille. Ses dates suivent les étapes : "
        "l'euphorie de l'été, les semaines devant l'usine Barricades, l'encerclement le vingt-neuf novembre, la faim de décembre. "
        "Et il montre le coût humain, les croix surmontées de casques, qu'aucun tableau de chiffres ne peut montrer.",
        "{rep5.4}Ses limites. C'est le regard d'un seul soldat allemand : rien sur le camp soviétique, les civils ou la stratégie. "
        "Pas de chiffres : il faut pour cela le document sept et le tableau des forces. Il s'arrête en décembre, avant la capitulation. "
        "Et une lettre à sa famille peut cacher le pire. Bilan : un document précieux pour l'expérience de la bataille, beaucoup moins pour son ampleur.",
    ], vis={
        "ex6": dict(type="exo", niveau="dbq", titre="En quoi le document 6 permet-il de comprendre la bataille de Stalingrad ? Quelles en sont les limites ?",
                    src="Consigne écrite pour cette vidéo, sur le dossier documentaire", enonce=["Analyse de document : présentation, contexte, intérêt, limites"],
                    donnees=["Lettres d'un soldat allemand, juillet-décembre 1942 : « prendre Stalingrad n'est pas difficile » … encerclés (29 novembre) … « les chevaux ont déjà été mangés »"]),
        "str2": dict(type="liste", titre="L'analyse de document : la démarche", cles=["présenter", "situer", "intérêt", "limites"], items=[
            "Présenter le document : nature, auteur, date", "Le situer dans son contexte",
            "Son intérêt : plusieurs arguments", "Ses limites : plusieurs arguments, puis le bilan critique"], x=150, y=130, w=980),
        "pa5": dict(type="pause", t="Rédige la présentation et le contexte, puis l'intérêt et les limites du document.",
                    sous="Mets la vidéo en pause, rédige ta réponse, puis relance pour voir un modèle."),
        "rep5": dict(type="liste", titre="Un modèle", items=[
            "Lettres d'un soldat allemand, juillet-déc. 1942, écrites pendant la bataille", "Contexte : la seconde offensive vers la Volga, jusqu'à l'encerclement",
            "Intérêt : un témoin direct · des dates qui suivent les étapes · le coût humain",
            "Limites : un seul soldat allemand · pas de chiffres · s'arrête en décembre · une lettre à la famille"], x=150, y=130, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Récapitulons. {carte.1}Les projets : le pacte de 1939 a ouvert la route de l'Est, et il y a trois raisons d'envahir l'Union soviétique, "
        "économique, idéologique et raciale, chacune avec son exemple. "
        "{carte.2}Barbarossa : le vingt-deux juin 1941, trois poussées, arrêtées devant Leningrad et Moscou ; cinq millions de morts en deux cents jours. "
        "{carte.3}Une guerre d'anéantissement : plus de lois de la guerre, le pas de pitié de Staline, les prisonniers soviétiques affamés, les trois cinquièmes des morts à l'Est. "
        "{carte.4}Et Stalingrad : le tournant, l'encerclement en novembre 1942, la capitulation de Paulus le trente et un janvier 1943. Une guerre totale.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : vers le génocide. Les ghettos, les Einsatzgruppen, les centres de mise à mort… et Treblinka.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="BARBAROSSA", branches=[
            dict(t="II.1 · Les projets", items=["pacte d'août 1939 · Pologne partagée", "économique : Grossraum, pétrole", "idéologique · raciale"]),
            dict(t="Barbarossa", items=["22 juin 1941 · trois poussées", "purges · terre brûlée", "déc. 1941 : Moscou tient"]),
            dict(t="L'anéantissement", items=["Staline, 6 nov. 1941", "3,3 millions de prisonniers morts sur 5,7", "3/5 des morts à l'Est"]),
            dict(t="Stalingrad", items=["ordre n° 227", "nov. 1942 : forces inversées", "31 janv. 1943 · guerre totale"])]),
        "fin": dict(type="mot", t="À suivre : vers le génocide", g="Épisode 5 · ghettos, Einsatzgruppen, centres de mise à mort", y=270, taille=68),
    }),
]

QUIZ = [
    dict(q="Qu'apporte à Hitler le pacte germano-soviétique d'août 1939 ?",
         r=["La neutralité de l'URSS et un plan secret de partage de la Pologne", "Une alliance militaire contre le Royaume-Uni",
            "Les pays baltes et la Bessarabie", "Du pétrole soviétique en échange des Sudètes"], ok=0, voir="def3",
         ex="C'est l'URSS qui annexe les pays baltes, la Bucovine du Nord et la Bessarabie en 1940."),
    dict(q="Quel exemple illustre la raison économique de l'invasion de l'URSS ?",
         r=["Stalingrad, un nœud sur la Volga qui assure l'accès au pétrole du Caucase", "L'ordre des commissaires sur les commissaires politiques",
            "L'ordre de Reichenau", "Le discours de Staline du 6 novembre 1941"], ok=0, voir="eco",
         ex="Le Grossraum avait besoin des ressources de l'URSS : terres agricoles, minerais, pétrole."),
    dict(q="Que prévoit l'ordre des commissaires (signé le 6 juin 1941) pour les commissaires politiques capturés ?",
         r=["Être « liquidés par les armes », par principe", "Être échangés contre des prisonniers allemands",
            "Être envoyés dans des camps de travail en Allemagne", "Être jugés par des tribunaux militaires"], ok=0, voir="jodl",
         ex="Un exemple de la raison idéologique : la croisade contre le « judéo-bolchevisme »."),
    dict(q="En 1941, que vise la poussée allemande du sud ?",
         r=["L'Ukraine, Kiev et Rostov", "Stalingrad et le Caucase", "Moscou", "Leningrad"], ok=0, voir="att",
         ex="Stalingrad et le Caucase sont les cibles de la seconde offensive, à l'été 1942."),
    dict(q="Quel est le bilan des 200 premiers jours de Barbarossa, selon le cours ?",
         r=["5 millions de morts, mille par heure", "60 millions de morts", "91 000 prisonniers", "27 à 28 millions de morts"], ok=0, voir="bil2",
         ex="27 à 28 millions, c'est le bilan soviétique de toute la guerre ; environ 91 000, les Allemands faits prisonniers à Stalingrad."),
    dict(q="Comment Staline répond-il aux nazis le 6 novembre 1941 ?",
         r=["« Si les Allemands veulent une guerre d'anéantissement, ils l'auront »", "« Pas un pas en arrière ! »",
            "« Nous ne nous rendrons jamais »", "Il propose un armistice"], ok=0, voir="c_st1",
         ex="« Pas un pas en arrière ! », c'est l'ordre n° 227, du 28 juillet 1942."),
    dict(q="Au total, combien des 5,7 millions de prisonniers de guerre soviétiques sont morts en captivité allemande ?",
         r=["Environ 3,3 millions : près de 6 sur 10", "Environ 170 000 : 3 sur 100", "Environ 1 million : moins de 2 sur 10", "Presque tous"], ok=0, voir="pow",
         ex="Environ 2,8 millions avaient déjà été tués entre juin 1941 et février 1942, surtout par la famine (texte du cours)."),
    dict(q="À Stalingrad, en novembre 1942, dans quelle catégorie les Allemands sont-ils encore devant ?",
         r=["Les avions", "Les hommes", "Les canons", "Les chars"], ok=0, voir="gf",
         ex="1 216 avions allemands contre 1 115 ; les Soviétiques sont devant pour les hommes, les canons et les chars."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre « La Seconde Guerre mondiale » (parties II.1 et II.2, dossier documentaire sur Stalingrad, "
    "tableau des forces à Stalingrad, tableau des divisions de l'introduction), tel qu'il est présenté sur le site ; réponses aux questions 1, 2, 3 et 5 "
    "du dossier proposées par le site ; l'exemple de Toukhatchevski ajouté hors du cours ; carte animée du chapitre 3 (site).",
    "Citations en traduction française : ordre des commissaires (juin 1941), ordre de Reichenau (10 octobre 1941), discours de Staline "
    "(6 novembre 1941), ordre n° 227 (28 juillet 1942), lettres d'un soldat allemand (juillet-décembre 1942).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
