"""Histoire · « La Seconde Guerre mondiale » — édition française de la série vidéo, épisode 1 : « Une guerre mondiale »
(l'introduction du chapitre).

Traduction et adaptation de h3_1.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
histoire-géographie classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes
visuels, mêmes repères, mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H3 : 0 guerre-monde · 1 Mandchourie · 3 Chine 1937 · 4 pacte · 5 Pologne · 11 attaque à l'ouest · 16 armistice ·
       24 pourquoi l'URSS · 25 Barbarossa · 28 anéantissement · 31 Pearl Harbor · 33 guerre mondiale · 34 France exploitée ·
       41 Nouvel Ordre européen fin 1942 · 42 Stalingrad · 45 bilan du génocide
  H2 : 27 Abyssinie · 28 Rhénanie · 33 Anschluss · 34 Munich · 35 Prague · 37 Pologne
Chaîne : outils/serie-philo/generer.py h3f_1 ; sortie dans dnl/serie/ (h3f-1.*).
La citation de Hitler (11 décembre 1941) est traduite de la version anglaise que cite le cours, et présentée comme telle.
Plan de la série : 1 Une guerre mondiale · 2 La défaite de la France · 3 Le Royaume-Uni seul · 4 Barbarossa ·
5 Vers le génocide · 6 La guerre à l'épreuve (composition et analyse de document) · 7 Récapitulatif.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-1"
NOTION = "La Seconde Guerre mondiale"
NUM = 1
TITRE = "Une guerre mondiale"
SUIVANT = "Épisode 2 · La défaite de la France"
PRONONCIATION = {"Lebensraum": "Lé-benss-raoum", "Grossraum": "Gross-raoum", "Einsatzgruppen": "Aïne-zats-groupen",
                 "Wehrmacht": "Vèr-markt", "Reichstag": "Raïchs-tag", "Reichsmarks": "Raïchs-mark",
                 "Untermenschen": "Ounn-teur-mènn-chenn", "Mein Kampf": "Maïne Kammpf", "Puyi": "Pou-yi",
                 "Jay Winter": "Djé Ouinn-teur", "Pearl Harbor": "Peurl Har-beur", "Anschluss": "Ann-chlouss",
                 "Blitzkrieg": "Blits-krig", "SDN": "èss-dé-ène", "STO": "èss-té-o"}

# tableau des divisions du cours (introduction) : 1940, 1942, 1943, 1944, 1945
ANS = [1940, 1942, 1943, 1944, 1945]
DIV_ALLIES = list(zip(ANS, [393, 397, 524, 575, 656]))
DIV_AXE = list(zip(ANS, [272, 350, 413, 349, 328]))
DIV_URSS = list(zip(ANS, [200, 250, 350, 400, 488]))
DIV_ALL = list(zip(ANS, [189, 261, 327, 347, 319]))
DIV_USA = list(zip(ANS, [24, 76, 95, 94, 94]))
DIV_FRA = list(zip(ANS, [105, 0, 5, 7, 14]))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Soixante millions de morts. Des combats de l'Atlantique au Pacifique, de l'Arctique aux déserts d'Afrique, "
        "des rues de Stalingrad aux îles du Pacifique. La Seconde Guerre mondiale est le conflit le plus meurtrier de l'histoire de l'humanité.",
        "{-q1}{q2}Mais quand a-t-elle commencé ? La plupart des gens répondraient : le premier septembre 1939, quand l'Allemagne envahit la Pologne. "
        "Ce chapitre donne une autre réponse… et cette réponse est ton premier argument dans une composition.",
        "{-q2}{q3}Et une deuxième question, plus importante encore : que voulaient construire les nazis avec cette guerre ? "
        "Pas seulement une Allemagne plus grande. Un continent tout entier. C'est le sujet de cet épisode.",
        "{-q3}{-g0}{plan}Cette série couvre tout le chapitre, en sept épisodes. {plan.1}Aujourd'hui : pourquoi c'est une guerre mondiale, "
        "pourquoi elle est si meurtrière, et ce que les nazis voulaient construire avec elle. {plan.2}Ensuite, la défaite de la France, {plan.3}le Royaume-Uni seul, "
        "{plan.4}l'opération Barbarossa, {plan.5}et la politique raciale qui mène au génocide. "
        "{plan.6}Puis un épisode réservé à l'épreuve : la composition et l'analyse de document. {plan.7}Et un récapitulatif final.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[0]),
        "q1": dict(type="question", t="60 millions de morts.", bande=True),
        "q2": dict(type="question", t="Quand la guerre a-t-elle vraiment commencé ?", bande=True),
        "q3": dict(type="question", t="Que voulaient construire les nazis ?", bande=True),
        "plan": dict(type="liste", titre="La Seconde Guerre mondiale en sept épisodes", items=[
            "Une guerre mondiale : dates, idéologie, Nouvel Ordre européen", "La défaite de la France (partie I.1)",
            "Le Royaume-Uni seul, soutenu par les États-Unis (partie I.2)", "Barbarossa : une guerre d'anéantissement (partie II)",
            "Vers le génocide (partie III)", "La Seconde Guerre mondiale à l'examen : composition et analyse de document", "Récap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Seconde Guerre mondiale · Épisode 1", t="Une guerre mondiale",
                      sous="1931 – 1947 · une guerre idéologique · le Nouvel Ordre européen"),
    }),

    # ================================================================ I. en Asie, dès 1931
    dict(id="asie", chap="Tout commence en Asie", fond="nuit", humeur="tension",
         retenir="La guerre commence en Asie : la Mandchourie en 1931, la Chine du Sud en 1937. Chaque fois, la SDN échoue à arrêter le Japon.",
         beats=[
        "{g1}Beaucoup d'historiens, dont Jay Winter et Robert Frank, ont montré que la guerre a commencé avant 1939. "
        "Sa chronologie peut s'étirer de 1931… jusqu'à 1947. Pour comprendre pourquoi, il faut se tourner vers l'Asie.",
        "{g1.1}Septembre 1931. Tu l'as vu au chapitre un : la Grande Dépression frappe durement le Japon, et son armée veut ses propres "
        "matières premières et ses propres marchés. Après l'incident de Moukden, l'armée japonaise conquiert la Mandchourie, au nord-est de la Chine.",
        "La Mandchourie est riche en charbon et en fer : exactement ce qu'il faut à une puissance industrielle sans ressources. "
        "Le Japon en fait un État fantoche, le Mandchoukouo, avec à sa tête, en titre, le dernier empereur de Chine, Puyi. Mais tout se décide à Tokyo.",
        "{lig1}Que fait la Société des Nations ? {lig1.1}Elle condamne l'invasion. {lig1.2}Le Japon quitte tout simplement la SDN, en 1933. "
        "{lig1.3}Et il ne se passe rien d'autre : ni sanctions, ni armée. La leçon est claire pour tous les régimes agressifs : "
        "la sécurité collective n'a aucun moyen de se faire respecter.",
        "{-lig1}{g1.2}Et 1937 marque le tournant. Le Japon attaque la Chine du Sud : c'est une guerre ouverte, de grande ampleur. "
        "La Chine appelle aussitôt la Société des Nations à l'aide… et une fois encore, la SDN se montre incapable de régler la crise.",
        "{-g1}{g1b}{g1b.1}Derrière cette expansion, le chapitre deux t'a montré une idéologie. Le Japon veut l'autarcie, ses propres ressources, "
        "et se dit une race supérieure, destinée à diriger l'Asie. {g1b.2}Et en décembre 1937, à Nankin, les troupes japonaises tuent "
        "entre deux cent mille et trois cent mille civils et prisonniers. Idéologie raciste, militarisme, civils pris pour cibles : "
        "{!les traits de la guerre à venir}les traits de la guerre mondiale à venir sont déjà là.",
        "{-g1b}{livre}Voilà pourquoi Robert Frank et Alya Aglan ont mis des dates sur la couverture de leur livre, en 2015 : "
        "La Guerre-monde, de 1937 à 1947. {!Les dates sont un argument}Les dates elles-mêmes sont un argument : "
        "la guerre a commencé en Asie, deux ans avant de commencer en Europe.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[1, 3]),
        "lig1": dict(type="liste", titre="Mandchourie, 1931 : la réponse de la SDN", x=60, y=150, w=600, petit=True, bande=True, items=[
            "Elle condamne l'invasion", "Le Japon quitte la SDN (1933)", "Ni sanctions, ni armée : la sécurité collective échoue"]),
        "g1b": dict(type="globe", code="H2", sc=[18, 32]),
        "livre": dict(type="mot", t="1937 – 1947", g="Robert Frank et Alya Aglan, La Guerre-monde (2015)", y=250, taille=110),
    }),

    # ================================================================ II. en Europe, la marche à la guerre
    dict(id="europe", chap="La marche à la guerre en Europe", fond="nuit", humeur="tension",
         retenir="1935 Éthiopie · 1936 Rhénanie · 1938 Anschluss et Munich · mars 1939 Prague · août 1939 le pacte · 1er septembre 1939 la Pologne.",
         beats=[
        "{g2}En Europe, la marche à la guerre est une suite d'épreuves de force, et chaque fois, les démocraties cèdent. Le chapitre deux en soixante secondes.",
        "{g2.1}Octobre 1935 : l'Italie fasciste envahit l'Abyssinie, l'Éthiopie. La SDN impose des sanctions faibles… qui ne changent rien.",
        "{g2.2}Mars 1936 : Hitler fait entrer des troupes en Rhénanie, démilitarisée depuis le traité de Versailles. Un coup de poker. "
        "La France et le Royaume-Uni ne font rien, et le pari est gagné.",
        "{g2.3}Mars 1938 : l'Anschluss. L'Autriche est annexée à l'Allemagne. {g2.4}Septembre 1938 : à Munich, la France et le Royaume-Uni livrent "
        "les Sudètes à Hitler, sans même consulter les Tchèques. C'est la politique d'apaisement.",
        "{g2.5}Mars 1939 : Hitler prend Prague. Cette fois, il ne réunit pas des Allemands : c'est une conquête. L'apaisement est mort.",
        "{-g2}{g3}{g3.1}Août 1939 : le coup de théâtre. L'Allemagne nazie et l'Union soviétique, ennemies idéologiques jurées, signent un pacte. "
        "Dans un protocole secret, elles prévoient de se partager la Pologne. {g3.2}Et le premier septembre 1939, l'Allemagne envahit la Pologne. "
        "Deux jours plus tard, le Royaume-Uni et la France lui déclarent la guerre. La guerre a commencé en Europe.",
        "{-g3}{g4}Mais même alors, ce n'est pas encore une guerre mondiale. Elle le devient en 1941. {g4.1}En juin, l'Allemagne envahit l'Union soviétique. "
        "{g4.2}En décembre, le Japon attaque la flotte américaine à Pearl Harbor, {g4.3}et l'Allemagne et l'Italie déclarent la guerre aux États-Unis. "
        "Désormais, on se bat sur tous les océans et sur tous les continents.",
        "{-g4}{frise}Voici donc la chronologie à retenir. {frise.1}1931, la Mandchourie. {frise.2}1937, le Japon attaque la Chine du Sud. "
        "{frise.3}1939, l'Allemagne envahit la Pologne : la guerre commence en Europe. {frise.4}1941, Barbarossa en juin, Pearl Harbor en décembre : "
        "la guerre devient vraiment mondiale. {frise.5}1945, la fin des combats. {frise.6}Et 1947, la fin de la guerre-monde pour Frank et Aglan : "
        "le moment où un nouveau conflit, la guerre froide, prend le relais. Ce sera le chapitre quatre.",
        "{-frise}{pa1}",
        ("P", 2.0),
        "{-pa1}{rep1}On peut le dire ainsi. {rep1.1}La guerre n'a pas commencé en Europe, mais en Asie. "
        "{rep1.2}Elle commence avec l'agression japonaise, en Mandchourie en 1931, et surtout contre la Chine en 1937. "
        "{rep1.3}Et l'échec de la Société des Nations, en Asie comme en Europe, lui a permis de s'étendre au monde entier.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[27, 28, 33, 34, 35]),
        "g3": dict(type="globe", code="H3", sc=[4, 5]),
        "g4": dict(type="globe", code="H3", sc=[25, 31, 33]),
        "frise": dict(type="frise", items=[
            dict(nom="Mandchourie", d=1931, q="le Japon s'en empare"), dict(nom="Chine", d=1937, q="le tournant"),
            dict(nom="Pologne", d=1939, q="la guerre en Europe"), dict(nom="Guerre mondiale", d=1941, q="Barbarossa · Pearl Harbor"),
            dict(nom="Fin des combats", d=1945, q="l'Europe, puis l'Asie"), dict(nom="Fin de la guerre", d=1947, q="selon Frank et Aglan")]),
        "pa1": dict(type="pause", t="En deux phrases : pourquoi peut-on dire que la guerre a commencé avant 1939 ?",
                    sous="Mets la vidéo en pause, écris ta réponse, puis relance pour comparer."),
        "rep1": dict(type="liste", titre="Une réponse possible", items=[
            "Elle commence en Asie, pas en Europe.", "L'agression japonaise : la Mandchourie (1931), la Chine du Sud (1937).",
            "L'échec de la SDN lui permet de s'étendre au monde."], x=170, y=150, w=940),
    }),

    # ================================================================ III. une guerre idéologique
    dict(id="ideologie", chap="Une guerre idéologique", fond="guerre", humeur="tension",
         retenir="Non seulement vaincre des armées, mais détruire la civilisation de l'ennemi : une guerre idéologique, environ 60 millions de morts, dont les trois cinquièmes sur le front de l'Est.",
         beats=[
        "{q4}Pourquoi cette guerre a-t-elle été si meurtrière ? Parce qu'elle ne ressemblait pas aux autres.",
        "{-q4}{def1}Dans la plupart des guerres, le but est de vaincre les armées ennemies, puis de négocier la paix. "
        "Ici, le but était de détruire la civilisation de l'ennemi. C'était une {!guerre idéologique}guerre idéologique, "
        "où aucun camp ne renoncerait avant la mort.",
        "{-def1}{photo}Le chapitre s'ouvre sur une photographie qui le dit mieux que toute définition. "
        "Des tueurs des Einsatzgruppen, vers 1941 ou 1942, abattent des hommes debout dans une fosse. Une photographie sans doute prise par l'un des tueurs. "
        "Les tueurs photographient leurs propres crimes : ils n'en ont pas honte, ils croient construire quelque chose. "
        "Nous reviendrons sur ces unités mobiles de tuerie dans l'épisode cinq.",
        "{-photo}{ideo}Le cours appelle cette guerre {!le creuset idéologique}le creuset idéologique du vingtième siècle : "
        "le moment où les grandes idéologies du siècle se rencontrent, dans une guerre totale. {ideo.1}Le nazisme, qui voit l'histoire comme une lutte des races. "
        "{ideo.2}Le fascisme, le modèle italien de l'État tout-puissant. {ideo.3}Le communisme soviétique, qui la voit comme une lutte des classes. "
        "{ideo.4}Et la démocratie libérale, le Royaume-Uni et les États-Unis, qui se battent pour la liberté… et pour leurs empires.",
        "{-ideo}{bil}Et le bilan est sans précédent. {bil.1}Environ soixante millions de morts au total. "
        "{bil.2}Les trois cinquièmes des morts de la guerre sont tombés sur le front de l'Est. "
        "{bil.3}L'Union soviétique, à elle seule, a perdu vingt-sept à vingt-huit millions de personnes : un habitant sur sept. "
        "{bil.4}Et six millions de Juifs ont été assassinés dans le génocide. "
        "La plupart des victimes étaient des civils : c'est la marque d'une guerre idéologique.",
    ], vis={
        "q4": dict(type="question", t="Pourquoi cette guerre a-t-elle été si meurtrière ?"),
        "def1": dict(type="def", cles=["armées", "civilisation"], terme="Une guerre idéologique",
                     t="Le but n'est pas seulement de vaincre les armées de l'ennemi, mais de détruire sa civilisation.",
                     etape="Aucun camp ne renonce avant la mort · aucune limite à la violence", x=170, y=200, w=940),
        "photo": dict(type="note", cles=["Einsatzgruppen", "tueurs"], terme="Le premier document du chapitre",
                      t="Des tueurs des Einsatzgruppen abattent des hommes debout dans une fosse, vers 1941-1942.",
                      etape="Une photographie sans doute prise par l'un des tueurs (décrite ici, non montrée).", x=170, y=200, w=940),
        "ideo": dict(type="liste", titre="Les idéologies dans le creuset", cles=["races", "État", "classes", "liberté"], items=[
            "Nazisme : l'histoire comme lutte des races", "Fascisme : l'État tout-puissant", "Communisme : l'histoire comme lutte des classes",
            "Démocratie libérale : la liberté… et les empires"], x=170, y=130, w=940),
        "bil": dict(type="liste", titre="Le bilan (chiffres du cours)", items=[
            "≈ 60 millions de morts", "3/5 sur le front de l'Est", "URSS : 27 à 28 millions, un habitant sur sept",
            "6 millions de Juifs assassinés"], x=170, y=130, w=940),
    }),

    # ================================================================ IV. une guerre de nombres
    dict(id="nombres", chap="Une guerre de nombres", fond="nuit", humeur="lumiere",
         retenir="1940 : l'Axe gagne avec moins de divisions (surprise, Blitzkrieg). Après 1942, les Alliés le dépassent, jusqu'à 656 contre 328 en 1945. L'URSS porte le poids de la guerre.",
         beats=[
        "{gr}Encore un document de l'introduction : le nombre de divisions de chaque camp. Une division est une grande unité de l'armée, "
        "de dix à vingt mille hommes environ (hors du cours). {gr.1}Les Alliés, en bleu. {gr.2}L'Axe, en rouge.",
        "{gr.3}Regarde 1940 : 393 divisions alliées contre 272 pour l'Axe. Les Alliés sont plus nombreux… et pourtant, l'Axe gagne partout. "
        "Pourquoi ? La surprise, la vitesse, les chars et les avions qui agissent ensemble : la Blitzkrieg. Ce sera l'épisode deux.",
        "{gr.4}Puis, après 1942, l'écart se creuse et ne se referme plus. 524 contre 413 en 1943, 575 contre 349 en 1944, "
        "656 contre 328 en 1945. Deux contre un.",
        "{-gr}{gr2}Regarde maintenant pays par pays. {gr2.1}L'Union soviétique : 200 divisions en 1940, 350 en 1943, 488 en 1945. "
        "{gr2.2}L'Allemagne culmine à 347, en 1944, puis recule. {gr2.3}Les États-Unis passent de 24 à 95 : leur armée se construit pendant la guerre. "
        "{gr2.4}Et la France : 105 divisions en 1940… zéro en 1942. En deux ans, l'armée française disparaît. Ça aussi, c'est l'épisode deux.",
        "{-gr2}{lec}Trois leçons, donc, à tirer de ce tableau. {lec.1}En 1940, le nombre ne suffit pas : l'Axe gagne avec moins de divisions. "
        "{lec.2}À partir de 1942, quand l'Union soviétique et les États-Unis sont pleinement dans la guerre, le nombre décide : l'Axe ne peut pas gagner une guerre longue. "
        "{lec.3}Et c'est l'Union soviétique qui porte l'essentiel du poids sur terre.",
        "{lec.4}Un détail à connaître : le tableau compte la Roumanie parmi les Alliés, alors qu'elle a combattu aux côtés de l'Axe jusqu'en août 1944. "
        "Si tu analyses ce tableau, c'est une limite à signaler.",
    ], vis={
        "gr": dict(type="graphe", titre="Divisions de chaque camp, 1940-1945 (cours)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1939.5, 1945.5], y=[0, 700], gx=ANS, gy=[200, 400, 600], lx="année", ly="divisions"),
                   el=[dict(type="courbe", pts=[list(p) for p in DIV_ALLIES], c="el", lbl="Alliés", lp=[1944.6, 690], dur=2.0),
                       dict(type="courbe", pts=[list(p) for p in DIV_AXE], c="ca", lbl="Axe", lp=[1944.7, 280], dur=2.0),
                       dict(type="points", pts=[[1940, 393], [1940, 272]], c="sa", lbl="1940 : 393 / 272", lp=[1941.0, 470]),
                       dict(type="points", pts=[[1945, 656], [1945, 328]], c="sa", lbl="1945 : 656 / 328", lp=[1943.6, 600])]),
        "gr2": dict(type="graphe", titre="Divisions par pays (cours)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1939.5, 1945.5], y=[0, 520], gx=ANS, gy=[100, 200, 300, 400, 500], lx="année", ly="divisions"),
                    el=[dict(type="courbe", pts=[list(p) for p in DIV_URSS], c="el", lbl="URSS", lp=[1944.8, 505], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_ALL], c="ca", lbl="Allemagne", lp=[1944.4, 375], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_USA], c="vert", lbl="États-Unis", lp=[1944.4, 120], dur=1.8),
                        dict(type="courbe", pts=[list(p) for p in DIV_FRA], c="sa", lbl="France", lp=[1941.0, 120], dur=1.8)]),
        "lec": dict(type="liste", titre="Ce que montre le tableau", items=[
            "1940 : l'Axe gagne avec moins de divisions", "Dès 1942 : le nombre décide, l'Axe perd une guerre longue",
            "L'URSS porte le poids sur terre", "Limite : la Roumanie comptée parmi les Alliés"], x=170, y=130, w=940),
    }),

    # ================================================================ V. le Nouvel Ordre européen
    dict(id="ordre", chap="Le Nouvel Ordre européen", fond="nuit", humeur="tension",
         retenir="Notion clé. Le Nouvel Ordre européen : la domination nazie sur l'Europe, présentée comme le salut de la civilisation européenne. Cinq moteurs.",
         beats=[
        "{g5}Pour les nazis, la guerre et la conquête sont une occasion. {g5.1}L'occasion de bâtir un immense appareil politique et économique, "
        "qui ancrerait leur domination sur l'Europe. Regarde la carte à la fin de 1942 : de l'Atlantique à la Volga, "
        "de la Norvège à la Méditerranée.",
        "{-g5}{def2}C'est une {!notion clé}notion clé du chapitre : le {!Nouvel Ordre européen}Nouvel Ordre européen. "
        "La domination nazie sur le continent, présentée par ses partisans comme le salut d'une civilisation européenne menacée d'effondrement. "
        "Remarque le mot présentée : c'est de la propagande. En réalité, l'Europe est organisée au profit de l'Allemagne.",
        "{-def2}{forces}Le cours lui donne cinq moteurs. Apprends-les : c'est un plan tout prêt. "
        "{forces.1}Un : l'Europe comme entité raciale, et la purification raciale par le génocide. "
        "{forces.2}Deux : la conquête du Lebensraum, l'espace vital, à l'Est. "
        "{forces.3}Trois : la croisade contre le communisme. "
        "{forces.4}Quatre : le Grossraum, un seul grand espace économique européen, au service de l'Allemagne. "
        "{forces.5}Et cinq : fournir à l'Allemagne les hommes, les matières premières et l'argent qu'exige la guerre totale.",
        "{-forces}{unex}Maintenant, un exemple pour chacun, tiré du reste du chapitre. Dans une composition, un argument sans exemple ne vaut rien.",
    ], vis={
        "g5": dict(type="globe", code="H3", sc=[41]),
        "def2": dict(type="def", cles=["domination", "présentée", "salut"], terme="Notion clé · le Nouvel Ordre européen",
                     t="La domination nazie sur l'Europe, présentée par ses partisans comme le salut d'une civilisation européenne menacée d'effondrement.",
                     etape="« Présentée » : de la propagande. En réalité, l'Europe est organisée au profit de l'Allemagne.", x=170, y=200, w=940),
        "unex": dict(type="mot", t="Un moteur · un exemple", g="dans une composition, un argument sans exemple ne vaut rien", y=260, taille=80),
        "forces": dict(type="liste", titre="Les cinq moteurs", cles=["raciale", "Lebensraum", "communisme", "Grossraum", "totale"], items=[
            "L'Europe comme entité raciale : la purification par le génocide", "Le Lebensraum : l'espace vital à l'Est",
            "Une croisade contre le communisme", "Le Grossraum : un espace économique au service de l'Allemagne",
            "Fournir la guerre totale : hommes, matières premières, argent"], x=170, y=110, w=940),
    }),

    # ================================================================ VI. cinq moteurs, cinq exemples
    dict(id="exemples", chap="Cinq moteurs, cinq exemples", fond="nuit", humeur="tension",
         retenir="Race : 6 millions de Juifs assassinés · Lebensraum : Barbarossa · anticommunisme : commissaires fusillés (ordre des commissaires, juin 1941) · Grossraum : blé ukrainien, pétrole du Caucase · guerre totale : 20 millions de Reichsmarks par jour payés par la France.",
         beats=[
        "{g6}{g6.1}Un : l'entité raciale. Les nazis voulaient une Europe purifiée par la race. Le résultat : six millions de Juifs assassinés, "
        "les deux tiers des Juifs d'Europe. Sur la carte, la part des Juifs tués : quatre-vingt-dix pour cent en Pologne, quatre-vingt-dix-sept en Lituanie.",
        "{g6.2}Deux : le Lebensraum. Dans Mein Kampf, Hitler voulait déjà conquérir un espace vital à l'Est. Le vingt-deux juin 1941, "
        "l'opération Barbarossa lance l'armée allemande vers Leningrad, Moscou et Kiev. "
        "Les Slaves sont vus comme des Untermenschen, des sous-hommes, à asservir ou à chasser pour faire place à des colons allemands.",
        "{g6.3}Trois : la croisade contre le communisme. Les nazis parlent de judéo-bolchevisme, comme si communistes et Juifs ne formaient qu'un seul ennemi. "
        "L'ordre des commissaires, émis par le haut commandement de la Wehrmacht le six juin 1941 : les commissaires politiques soviétiques doivent être fusillés dès leur capture. "
        "Ni prisonniers, ni règles : une guerre d'anéantissement.",
        "{g6.4}Quatre : le Grossraum, le grand espace économique. L'Est doit nourrir l'Allemagne : le blé d'Ukraine, le pétrole du Caucase. "
        "C'est pourquoi, en 1942, l'armée allemande se dirige vers Stalingrad et le Caucase.",
        "{g6.5}Et cinq : fournir la guerre totale. La France occupée paie vingt millions de Reichsmarks par jour de frais d'occupation. "
        "Son charbon, sa nourriture, son carburant sont réquisitionnés. Et à partir de 1942, des ouvriers français partent pour l'Allemagne : "
        "d'abord des volontaires, avec la Relève, puis, à partir de février 1943, des travailleurs forcés, avec le STO.",
        "{-g6}{tab5}Voici donc ton tableau : cinq moteurs, cinq exemples. Mets la vidéo en pause et recopie-le : c'est la colonne vertébrale de toute composition sur ce chapitre.",
        ("P", 4.0),
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[45, 25, 28, 24, 34]),
        "tab5": dict(type="liste", titre="Cinq moteurs · cinq exemples", items=[
            "Entité raciale → 6 millions de Juifs assassinés (90 % en Pologne)", "Lebensraum → Barbarossa, 22 juin 1941 ; les Slaves vus comme des « Untermenschen »",
            "Anticommunisme → l'ordre des commissaires (juin 1941) : commissaires fusillés", "Grossraum → blé ukrainien, pétrole du Caucase",
            "Guerre totale → France : 20 millions de RM par jour, le STO"], x=150, y=110, w=980),
    }),

    # ================================================================ VII. Hitler le dit lui-même
    dict(id="hitler", chap="Hitler le dit lui-même", fond="guerre", humeur="tension",
         retenir="Hitler, 11 décembre 1941, tel que le cours le cite : « l'élimination absolue des Juifs, l'établissement de la suprématie du peuple allemand et la création d'une véritable communauté des nations sous direction allemande ».",
         beats=[
        "{reich}Et Hitler l'a dit lui-même, d'après le cours, devant le Reichstag, le onze décembre 1941, "
        "le jour où l'Allemagne déclare la guerre aux États-Unis. Voici la phrase telle que le cours la cite. Écoute bien.",
        ("C", "l'élimination absolue des Juifs, l'établissement de la suprématie du peuple allemand "
              "et la création d'une véritable communauté des nations sous direction allemande", "c_hitler"),
        "{-c_hitler}{-reich}{ana}Décomposons-la. {ana.1}D'abord, l'élimination absolue des Juifs : le but racial, "
        "annoncé en public, au moment même où les tueries de masse ont commencé à l'Est. "
        "{ana.2}Ensuite, la suprématie du peuple allemand : le but national, la race des seigneurs qui domine les autres. "
        "{ana.3}Enfin, une communauté des nations sous direction allemande : le but européen. On croirait entendre une coopération… "
        "mais direction veut dire domination.",
        "{-ana}{lien}Trois buts en une phrase : racial, national, européen. Garde cette citation : "
        "elle convient à l'introduction de presque toute composition sur le Nouvel Ordre européen. Et retiens la date : elle montre que le génocide "
        "n'était pas un effet secondaire et caché de la guerre, mais l'un de ses buts déclarés.",
    ], vis={
        "reich": dict(type="tableau", img="h3-reichstag", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                      legende="Hitler déclare la guerre aux États-Unis, Reichstag, 11 décembre 1941 (Wikimedia Commons, CC BY-SA 3.0)"),
        "c_hitler": dict(type="cit", a="Adolf Hitler", o="discours au Reichstag, 11 décembre 1941, tel que le cours le cite (traduction)", x=200, y=170, w=880),
        "ana": dict(type="liste", titre="Trois buts en une phrase", cles=["racial", "national", "européen"], items=[
            "« l'élimination absolue des Juifs » → le but racial", "« la suprématie du peuple allemand » → le but national",
            "« une communauté des nations sous direction allemande » → le but européen"], x=150, y=130, w=980),
        "lien": dict(type="note", terme="Pourquoi cette citation compte", cles=["buts", "déclarés"],
                     t="Le génocide n'était pas un effet secondaire caché de la guerre, mais l'un de ses buts déclarés.",
                     etape="Un discours public, le 11 décembre 1941, alors que les tueries ont commencé à l'Est.", x=170, y=200, w=940),
    }),

    # ================================================================ VIII. trois études de cas
    dict(id="cas", chap="Trois études de cas", fond="nuit", humeur="calme",
         retenir="Le chapitre met le Nouvel Ordre européen à l'épreuve de trois cas : la France à l'Ouest, Barbarossa à l'Est, le génocide.",
         beats=[
        "{g7}Le chapitre évalue donc cet ordre à travers trois cas. {g7.1}À l'Ouest, l'invasion et l'occupation de la France : "
        "une défaite en six semaines, un pays découpé en zones, un régime qui collabore.",
        "{g7.2}À l'Est, la conquête du Lebensraum et la guerre contre l'Union soviétique : une guerre d'anéantissement, "
        "cinq millions de morts dans les deux cents premiers jours, et le tournant de Stalingrad.",
        "{g7.3}Et partout, la politique raciale qui mène au génocide : les ghettos, les fusillades, les centres de mise à mort.",
        "{-g7}{cmp}Remarque le contraste. {cmp.1}À l'Ouest, la France est exploitée, mais traitée en partenaire, du moins en apparence. "
        "{cmp.2}À l'Est, les peuples conquis doivent être asservis ou exterminés. Le même ordre, deux visages : "
        "ce contraste est un excellent argument pour une composition.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[16, 25, 32]),
        "cmp": dict(type="cols", g="À l'Ouest", gq="la France exploitée, « partenaire » en apparence : la collaboration", d="À l'Est",
                    dq="des peuples asservis ou exterminés : une guerre d'anéantissement", vs="≠"),
    }),

    # ================================================================ IX. pour la composition
    dict(id="essay", chap="Pour la composition", fond="aube", humeur="calme",
         retenir="Problématique : quels étaient les buts du Nouvel Ordre européen ? Introduction : accroche, définition, contexte, problématique, plan. Trois parties : ordre racial et idéologique, ordre colonial et économique, guerre totale.",
         beats=[
        "{ki}La problématique de ce chapitre, c'est exactement cela : {!Quels buts ?}quels étaient les buts du Nouvel Ordre européen, "
        "et dans quelle mesure ont-ils été atteints ? Et deux notions clés : le Nouvel Ordre européen, et le Lebensraum.",
        "{-ki}{intro}Une bonne introduction a cinq étapes. {intro.1}Une accroche : une date, une citation, un chiffre. "
        "{intro.2}La définition de la notion clé. {intro.3}Le contexte : les dates et les lieux. "
        "{intro.4}La problématique. {intro.5}Et l'annonce du plan.",
        "{-intro}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}Voici un modèle. Le onze décembre 1941, Hitler annonce, selon la citation du cours, l'élimination absolue des Juifs "
        "et la création d'une communauté des nations sous direction allemande. C'est le Nouvel Ordre européen : la domination nazie sur l'Europe, "
        "présentée comme le salut de la civilisation européenne. Entre 1939 et 1942, l'Allemagne le construit par la conquête, de la France à la Volga. "
        "Quels étaient ses buts, et dans quelle mesure ont-ils été atteints ? Nous verrons que c'était un ordre racial et idéologique, "
        "un ordre colonial et économique, et un ordre conçu pour la guerre totale.",
        "{-rep2}{plan2}Et le plan, avec les exemples de chaque partie. {plan2.1}Première partie : un ordre racial et idéologique. "
        "Le génocide, six millions de Juifs ; la croisade contre le judéo-bolchevisme. "
        "{plan2.2}Deuxième partie : un ordre colonial et économique. Le Lebensraum et Barbarossa ; le Grossraum, le blé ukrainien et le pétrole du Caucase. "
        "{plan2.3}Troisième partie : un ordre pour la guerre totale. La France paie vingt millions de Reichsmarks par jour ; le STO ; les prisonniers soviétiques morts de faim.",
        "{plan2.4}Et pour discuter, pas seulement décrire : montre les limites. L'ordre s'effondre sur le champ de bataille, à Stalingrad, "
        "en février 1943 ; et il se heurte à des résistances, de Londres à Varsovie.",
    ], vis={
        "ki": dict(type="question", t="Problématique : quels étaient les buts du Nouvel Ordre européen ?"),
        "intro": dict(type="liste", titre="Une introduction en cinq étapes", items=[
            "Une accroche : date, citation, chiffre", "Définir la notion clé", "Le contexte : dates et lieux", "La problématique",
            "L'annonce du plan"], x=170, y=120, w=940),
        "pa2": dict(type="pause", t="Rédige l'introduction d'une composition sur les buts du Nouvel Ordre européen.",
                    sous="Mets la vidéo en pause, suis les cinq étapes, puis relance pour voir un modèle."),
        "rep2": dict(type="note", terme="Un modèle d'introduction", cles=["racial", "colonial", "totale"],
                     t="11 déc. 1941 : Hitler annonce (selon la citation du cours) « l'élimination absolue des Juifs »… Le Nouvel Ordre européen : la domination nazie présentée comme le salut de l'Europe. "
                       "1939-1942, de la France à la Volga. Quels buts ? Un ordre racial, un ordre colonial, un ordre pour la guerre totale.",
                     etape="Accroche · définition · contexte · problématique · plan", x=150, y=150, w=980),
        "plan2": dict(type="liste", titre="Un plan en trois parties, avec des exemples", items=[
            "I. Racial et idéologique : le génocide (6 millions), le « judéo-bolchevisme »",
            "II. Colonial et économique : Lebensraum, Barbarossa, Grossraum",
            "III. Guerre totale : 20 millions de RM par jour, le STO, les prisonniers soviétiques",
            "Discuter : les limites — Stalingrad (févr. 1943), les résistances"], x=150, y=110, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Une guerre mondiale, qui commence en Asie, en 1931 et en 1937, gagne l'Europe en 1939 et le monde entier en 1941. "
        "{carte.2}Une guerre idéologique, environ soixante millions de morts, le creuset du siècle. "
        "{carte.3}Une guerre de nombres, que les Alliés gagnent après 1942, l'Union soviétique portant l'essentiel du poids. "
        "{carte.4}Et la notion clé : le Nouvel Ordre européen, avec ses cinq moteurs et un exemple pour chacun.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : la défaite de la France. Six semaines en mai et juin 1940, un armistice, un pays coupé en deux… "
        "et un régime qui choisit la collaboration.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="UNE GUERRE MONDIALE", branches=[
            dict(t="Dates", items=["1931 Mandchourie · 1937 Chine", "1939 Pologne · 1941 mondiale", "1937-1947 : Frank et Aglan"]),
            dict(t="Idéologie", items=["détruire une civilisation", "≈ 60 millions de morts", "3/5 sur le front de l'Est"]),
            dict(t="Nombres", items=["1940 : 393 / 272", "1945 : 656 / 328", "URSS : 488"]),
            dict(t="Nouvel Ordre européen", items=["race · Lebensraum", "anticommunisme", "Grossraum · guerre totale"])]),
        "fin": dict(type="mot", t="La défaite de la France", g="Prochain épisode · épisode 2 · mai – juin 1940", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Pourquoi des historiens comme Robert Frank font-ils commencer la guerre en 1937 ?",
         r=["Le Japon attaque la Chine du Sud et la SDN se montre impuissante", "L'Allemagne envahit la Pologne",
            "L'Italie envahit l'Éthiopie", "L'Allemagne déclare la guerre aux États-Unis"], ok=0, voir="livre",
         ex="Leur livre s'intitule La Guerre-monde, 1937-1947 (2015) ; sa chronologie peut même partir de 1931, avec la Mandchourie."),
    dict(q="Que fait la SDN après l'invasion de la Mandchourie par le Japon en 1931 ?",
         r=["Elle condamne l'invasion, et le Japon quitte la SDN", "Elle envoie une armée internationale",
            "Elle impose un embargo pétrolier au Japon", "Elle reconnaît la Mandchourie comme japonaise"], ok=0, voir="lig1",
         ex="Une condamnation sans sanctions : la sécurité collective n'avait aucun moyen de se faire respecter."),
    dict(q="Quel événement de mars 1939 met fin à la politique d'apaisement ?",
         r=["Hitler prend Prague", "L'Anschluss", "La conférence de Munich", "La remilitarisation de la Rhénanie"], ok=0, voir="g2",
         ex="Prague n'était pas un territoire germanophone : c'était une conquête, et le Royaume-Uni et la France cessent de céder."),
    dict(q="Qu'est-ce qui fait de la Seconde Guerre mondiale une guerre idéologique ?",
         r=["Le but est de détruire la civilisation de l'ennemi, pas seulement ses armées", "Elle n'oppose que des dictatures",
            "Elle ne se déroule qu'en Europe", "Elle se termine par une paix négociée"], ok=0, voir="def1",
         ex="Aucun camp ne renonce avant la mort : d'où environ 60 millions de morts, des civils pour la plupart."),
    dict(q="En 1945, combien de divisions ont les Alliés et l'Axe, selon le tableau du cours ?",
         r=["656 contre 328", "328 contre 656", "393 contre 272", "488 contre 347"], ok=0, voir="gr",
         ex="393 contre 272, c'est 1940 ; 488, c'est l'URSS seule en 1945 ; 347, le sommet de l'Allemagne en 1944."),
    dict(q="Qu'est-ce que le Nouvel Ordre européen ?",
         r=["La domination nazie sur l'Europe, présentée comme le salut de sa civilisation", "Le plan allié pour la paix après 1945",
            "La SDN réformée en 1940", "La constitution de Vichy"], ok=0, voir="def2",
         ex="C'est une notion clé du chapitre : définis-la, puis donne ses cinq moteurs, avec un exemple pour chacun."),
    dict(q="Quel exemple illustre le Grossraum ?",
         r=["Le blé ukrainien et le pétrole du Caucase pour l'Allemagne", "L'ordre des commissaires de juin 1941",
            "Le ghetto de Varsovie", "L'appel du 18 juin 1940 du général de Gaulle"], ok=0, voir="g6",
         ex="Le Grossraum, c'est l'Europe comme un seul espace économique au service de l'Allemagne : l'Est devait nourrir le Reich."),
    dict(q="Quand Hitler définit-il l'« ordre nouveau » devant le Reichstag ?",
         r=["Le 11 décembre 1941", "Le 1er septembre 1939", "Le 22 juin 1941", "Le 30 janvier 1933"], ok=0, voir="c_hitler",
         ex="Le jour où l'Allemagne déclare la guerre aux États-Unis : « l'élimination absolue des Juifs… », selon la citation du cours."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 3 « La Seconde Guerre mondiale » (introduction, avec des exemples des parties I à III, et des rappels des chapitres 1 et 2), tel qu'il est rédigé sur le site ; cartes animées des chapitres 2 et 3 (site).",
    "Citation de Hitler (11 décembre 1941) : traduction française de la version que cite le cours.",
    "Photographie : Hitler déclare la guerre aux États-Unis, Reichstag, 11 décembre 1941 (photographe inconnu, Wikimedia Commons, CC BY-SA 3.0).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
