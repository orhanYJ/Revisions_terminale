"""Histoire · « La Seconde Guerre mondiale » — édition française de la série vidéo, épisode 2 : « La défaite de la France »
(partie I.1 du cours : l'invasion nazie de l'Europe de l'Ouest, le cas français).

Traduction et adaptation de h3_2.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
histoire-géographie classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes
visuels, mêmes repères, mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H3 : 6 drôle de guerre · 7 partage de la Pologne · 10 Danemark et Norvège · 11 attaque à l'ouest · 12 Ardennes ·
       13 Dunkerque · 14 chute de Paris, exode · 15 appel du 18 juin · 16 armistice, zones · 18 Vichy ·
       19 annexions soviétiques de l'été 1940 · 23 Balkans · 34 France exploitée · 35 étoile jaune et rafles ·
       39 Torch, zone libre envahie
Adaptations : Worksheet 1 → « le dossier documentaire » ; Source N → « document N » ; paragraphe d'essay → paragraphe de
réponse à une question problématisée ; DBQ a) « How useful » → analyse de document (présenter, situer, expliquer,
intérêt et limites, bilan critique). Citations : appel du 18 juin dans son texte original ; Churchill et The Observer
en traduction française. Mesures de Vichy nommées par leur nom français (statut des Juifs d'octobre 1940, Commissariat
général aux questions juives de mars 1941). Erreur du cours signalée comme dans l'édition anglaise (arrestations de
l'été 1942 par la police française, non par la Milice).
Chaîne : outils/serie-philo/generer.py h3f_2 ; sortie dans dnl/serie/ (h3f-2.*).
Plan de la série : 1 Une guerre mondiale · 2 La défaite de la France · 3 Le Royaume-Uni seul · 4 Barbarossa ·
5 Vers le génocide · 6 La guerre à l'épreuve (composition et analyse de document) · 7 Récapitulatif.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h3f-2"
NOTION = "La Seconde Guerre mondiale"
NUM = 2
TITRE = "La défaite de la France"
SUIVANT = "Épisode 3 · Le Royaume-Uni seul"
PRONONCIATION = {"Blitzkrieg": "Blits-krig", "Panzerdivision": "Pann-tsèr-divizion", "Erwin": "Èr-vine",
                 "Reichsmarks": "Raïchs-mark", "Royal Navy": "Roï-al Né-vi", "BBC": "bé-bé-cé", "MBF": "èm-bé-èf",
                 "STO": "èss-té-o", "Herrenvolk": "Hé-renn-folk", "Pariser Zeitung": "Pa-ri-zeur Tsaï-toung",
                 "The Observer": "Zi Obb-zeur-veur", "Observer": "Obb-zeur-veur", "Torch": "Tortch"}

# tableau des divisions du cours (H3_DIV) : 1940, 1942, 1943, 1944, 1945
ANS = [1940, 1942, 1943, 1944, 1945]
DIV_FRA = list(zip(ANS, [105, 0, 5, 7, 14]))
DIV_GB = list(zip(ANS, [34, 38, 39, 37, 31]))

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture2", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{q1}Le quatorze juin 1940. Les troupes allemandes entrent dans Paris. Le dix mai, la France avait encore "
        "l'une des plus grandes armées du monde.",
        "{-q1}{q2}Alors comment a-t-elle pu s'effondrer en six semaines seulement ? C'est la première question de cet épisode.",
        "{-q2}{q3}Et la seconde : qu'a fait l'Allemagne de la France ensuite ? Occupation, collaboration, exploitation, "
        "persécution. La France est la première étude de cas du Nouvel Ordre européen.",
        "{-q3}{-g0}{plan}Le plan. {plan.1}L'histoire sur la carte. {plan.2}Pourquoi la France tombe. {plan.3}Dunkerque et la défaite. "
        "{plan.4}La France découpée, et Vichy. {plan.5}Exploitation et persécution. {plan.6}Et de l'entraînement : la composition et l'analyse de document.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H3", sc=[14]),
        "q1": dict(type="question", t="14 juin 1940 : les Allemands entrent dans Paris.", bande=True),
        "q2": dict(type="question", t="Comment la France a-t-elle pu tomber en six semaines ?", bande=True),
        "q3": dict(type="question", t="Et qu'a fait l'Allemagne de la France ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 2 · partie I.1 du cours", items=[
            "L'histoire sur la carte : 1939 – 1942", "Pourquoi la France tombe : stratégie et Blitzkrieg",
            "Dunkerque, la défaite, l'exode", "La France découpée ; le régime de Vichy",
            "Exploitée, persécutée, réprimée, séduite", "Entraînement : composition et analyse de document"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · La Seconde Guerre mondiale · Épisode 2", t="La défaite de la France",
                      sous="mai 1940 – novembre 1942 · défaite · occupation · collaboration"),
    }),

    # ================================================================ I. la chronologie sur la carte (1)
    dict(id="sixsemaines", chap="Six semaines sur la carte", fond="nuit", humeur="tension",
         retenir="Drôle de guerre (sept. 1939 – mai 1940) · 10 mai : l'attaque · 13-20 mai : les Ardennes · 26 mai – 4 juin : Dunkerque · 14 juin : chute de Paris.",
         beats=[
        "{g1}Suivons d'abord l'histoire sur la carte. {g1.1}Septembre 1939 : après l'invasion de la Pologne, le Royaume-Uni et la France "
        "déclarent la guerre à l'Allemagne. Et ensuite… presque rien. L'armée française attend derrière la ligne Maginot : c'est la drôle de guerre.",
        "{g1.2}Avril 1940 : l'Allemagne frappe d'abord au nord. Elle occupe le Danemark et envahit la Norvège.",
        "{g1.3}Le dix mai 1940 : la vraie attaque. L'armée allemande envahit les Pays-Bas, la Belgique et le Luxembourg. "
        "Et le même jour, à Londres, Winston Churchill devient Premier ministre.",
        "{g1.4}Du treize au vingt mai : la surprise. Les chars allemands passent par la forêt des Ardennes, "
        "percent les lignes françaises et foncent vers les côtes de la Manche. Les meilleures troupes alliées, envoyées en Belgique, sont prises au piège dans le nord.",
        "{g1.5}Du vingt-six mai au quatre juin : Dunkerque. L'opération Dynamo évacue trois cent trente-huit mille soldats alliés vers l'Angleterre.",
        "{g1.6}Vient ensuite l'offensive de la Somme vers Paris. Le gouvernement français quitte la capitale "
        "et, le quatorze juin 1940, Paris tombe. Quelque huit millions de civils fuient vers le sud : {!l'exode}l'exode.",
    ], vis={
        "g1": dict(type="globe", code="H3", sc=[6, 10, 11, 12, 13, 14]),
    }),

    # ================================================================ II. la chronologie sur la carte (2)
    dict(id="armistice", chap="L'armistice et les zones", fond="nuit", humeur="tension",
         retenir="18 juin 1940 : l'appel du général de Gaulle · 22 juin : armistice à Rethondes, la France découpée · Vichy collabore · 11 nov. 1942 : la zone libre envahie.",
         beats=[
        "{g2}Le gouvernement est désormais dirigé par le maréchal Pétain, l'un des vainqueurs de 1918, et il demande l'armistice. "
        "Un général refuse : Charles de Gaulle. Il gagne Londres et, le dix-huit juin, à la radio de la BBC, "
        "il appelle les Français à poursuivre le combat. Écoute la fin de son appel.{-g2}",
        ("C", "Quoi qu'il arrive, la flamme de la résistance française ne doit pas s'éteindre et ne s'éteindra pas.", "c_gaulle"),
        "{-c_gaulle}{g2b}{g2b.1}Mais le vingt-deux juin 1940, à Rethondes, dans la forêt de Compiègne, la France signe l'armistice. "
        "Et le pays est découpé : une zone occupée, au nord et sur toute la côte atlantique ; "
        "et une zone dite libre, au sud, gouvernée depuis Vichy.",
        "{g2b.2}Dans cette zone, le maréchal Pétain installe à Vichy un nouveau régime : un État français autoritaire, "
        "qui choisit de collaborer avec l'Allemagne.",
        "{g2b.3}Ce partage dure deux ans. Le huit novembre 1942, les Alliés débarquent en Afrique du Nord française : "
        "c'est l'opération Torch. En riposte, le onze novembre, les forces allemandes envahissent la zone libre, "
        "et les troupes italiennes occupent une grande partie du sud-est. Désormais, toute la France est occupée.",
        "{-g2b}{dates}Avant le cours lui-même, voici donc les dates à recopier. Mets la vidéo en pause si tu en as besoin.",
        ("P", 5.0),
    ], vis={
        "g2": dict(type="globe", code="H3", sc=[15]),
        "g2b": dict(type="globe", code="H3", sc=[16, 18, 39]),
        "c_gaulle": dict(type="cit", a="Charles de Gaulle", o="appel du 18 juin 1940, BBC, Londres", x=200, y=190, w=880),
        "dates": dict(type="liste", titre="Les dates à connaître", petit=True, items=[
            "sept. 1939 – mai 1940 · la drôle de guerre", "10 mai 1940 · l'attaque allemande ; Churchill Premier ministre",
            "13-20 mai · la percée des Ardennes", "26 mai – 4 juin · Dunkerque, l'opération Dynamo",
            "14 juin · chute de Paris ; l'exode", "22 juin · l'armistice de Rethondes",
            "11 nov. 1942 · la zone libre envahie (après Torch)"], x=170, y=100, w=940),
    }),

    # ================================================================ III. l'Europe submergée (idée 1)
    dict(id="europe41", chap="L'Europe submergée, 1939-1941", fond="nuit", humeur="tension",
         retenir="1939-1941 : l'Allemagne et l'URSS attaquent les premières ; l'Axe submerge l'Europe continentale ; l'URSS prend sa part à l'est ; seul le Royaume-Uni résiste encore.",
         beats=[
        "{g3}Passons au cours, idée par idée. Il s'ouvre sur une carte de l'Europe de 1939 à 1941, qu'on peut te demander de décrire. "
        "{g3.1}L'Allemagne et l'Union soviétique sont les deux puissances qui attaquent les premières, en 1939. En septembre, elles se partagent la Pologne.",
        "{g3.2}L'Union soviétique continue de prendre sa part de l'Europe de l'Est : à l'été 1940, elle annexe les pays baltes "
        "et prend la Bessarabie à la Roumanie.",
        "{g3.3}Et au printemps 1941, l'Axe a progressé très vite partout : la Yougoslavie et la Grèce sont envahies, "
        "tandis que la Hongrie, la Roumanie et la Bulgarie se rangent aux côtés de l'Allemagne.",
        "{-g3}{l1}Voici donc la situation à décrire. {l1.1}L'Europe continentale est submergée par l'Axe. "
        "{l1.2}L'Union soviétique a pris sa part de l'Europe de l'Est. {l1.3}Et en 1941, seul le Royaume-Uni résiste encore. "
        "{l1.4}L'exemple à citer : la Belgique, les Pays-Bas, le Luxembourg et la France, submergés en six semaines à partir de mai 1940.",
    ], vis={
        "g3": dict(type="globe", code="H3", sc=[7, 19, 23]),
        "l1": dict(type="liste", titre="L'Europe, 1939 – 1941", cles=["Axe", "part", "Royaume-Uni"], items=[
            "L'Axe submerge l'Europe continentale", "L'URSS prend sa part à l'est",
            "1941 : seul le Royaume-Uni résiste encore", "Exemple : quatre pays submergés en six semaines"], x=170, y=130, w=940),
    }),

    # ================================================================ IV. une armée immense, une stratégie dépassée (idée 2)
    dict(id="strategie", chap="Une armée immense, une stratégie dépassée", fond="nuit", humeur="calme",
         retenir="France : 105 divisions en 1940, Royaume-Uni : 34. Mais une armée dirigée par les vainqueurs de 1918, une stratégie défensive, la ligne Maginot (pas sur la frontière belge), la drôle de guerre.",
         beats=[
        "{q5}Premier paradoxe. En 1940, la France a l'une des plus grandes armées du monde. La défaite n'est donc pas une question de nombre.",
        "{-q5}{gr}Regarde le tableau des divisions. {gr.1}La France : 105 divisions en 1940. {gr.2}Le Royaume-Uni : 34 seulement. "
        "Souviens-toi de l'épisode un : les Alliés avaient 393 divisions en tout, contre 272 pour l'Axe. "
        "{gr.3}Et regarde maintenant la France en 1942 : zéro. En deux ans, l'armée française a disparu.",
        "{-gr}{def3}Alors, qu'est-ce qui n'a pas marché ? Cette armée était dirigée par les vainqueurs de 1918, et elle était peu moderne. "
        "Et la France et le Royaume-Uni avaient choisi une {!stratégie défensive}stratégie défensive. {def3.1}Leur plan : éviter une nouvelle guerre de tranchées et ses hécatombes, "
        "et résister à une attaque allemande massive à l'abri de fortifications.",
        "{-def3}{mag}Le symbole de cette stratégie, c'est la ligne Maginot : une chaîne de fortifications perfectionnée, le long de la frontière avec l'Allemagne. "
        "{mag.1}Mais elle avait une faiblesse, et elle fut fatale : elle ne couvrait pas la frontière franco-belge.",
        "{-mag}{drole}Alors, de septembre 1939 à mai 1940, la France et le Royaume-Uni attendent : la guerre est déclarée, mais on ne se bat presque pas. "
        "{drole.1}C'est la drôle de guerre.",
    ], vis={
        "q5": dict(type="question", t="L'une des plus grandes armées du monde… battue en six semaines ?"),
        "gr": dict(type="graphe", titre="Divisions disponibles (tableau du cours)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1939.5, 1945.5], y=[0, 120], gx=ANS, gy=[20, 40, 60, 80, 100], lx="année", ly="divisions"),
                   el=[dict(type="point", x=1940, y=105, c="el", lbl="France 1940 : 105", lp=[1941.3, 98], proj=True),
                       dict(type="point", x=1940, y=34, c="vert", lbl="Royaume-Uni : 34", lp=[1940.7, 40]),
                       dict(type="courbe", pts=[list(p) for p in DIV_FRA], c="ca", lbl="France : 0 en 1942", lp=[1943.0, 26], dur=2.0)]),
        "def3": dict(type="def", cles=["tranchées", "résister", "fortifications"], terme="Une stratégie défensive",
                     t="Éviter une nouvelle guerre de tranchées et ses hécatombes ; résister à une attaque allemande massive à l'abri de fortifications.",
                     etape="Une armée dirigée par les vainqueurs de 1918, et peu moderne", x=170, y=200, w=940),
        "mag": dict(type="def", cles=["fortifications", "Allemagne"], terme="La ligne Maginot",
                    t="Une chaîne de fortifications perfectionnée, le long de la frontière entre la France et l'Allemagne.",
                    etape="Sa faiblesse : elle ne couvrait pas la frontière franco-belge.", x=170, y=200, w=940),
        "drole": dict(type="def", cles=["déclarée", "bat"], terme="La drôle de guerre · sept. 1939 – mai 1940",
                      t="La guerre est déclarée, mais on ne se bat presque pas à l'ouest.",
                      etape="La France attend l'attaque derrière la ligne Maginot.", x=170, y=200, w=940),
    }),

    # ================================================================ V. la Blitzkrieg par les Ardennes (idée 3)
    dict(id="ardennes", chap="La Blitzkrieg par les Ardennes", fond="guerre", humeur="tension",
         retenir="Blitzkrieg : chars et avions pour une victoire rapide. Les Alliés attendaient l'attaque au centre de la Belgique, comme en 1914 ; elle passe par les Ardennes (13-20 mai 1940).",
         beats=[
        "{def4}L'Allemagne, elle, veut une victoire rapide. Sa méthode, c'est la {!Blitzkrieg}Blitzkrieg, la guerre éclair : "
        "une offensive rapide qui combine les chars et les avions. {def4.1}Les raids aériens avaient déjà été testés en Belgique et aux Pays-Bas.",
        "{-def4}{cmp1}Et l'Allemagne y ajoute la surprise. {cmp1.g}Les chefs britanniques et français pensaient que les Allemands attaqueraient par le centre de la Belgique, "
        "comme en 1914. Alors, le dix mai, ils y envoient en hâte leurs meilleures forces. "
        "{cmp1.d}Mais l'attaque principale passe par la forêt vallonnée des Ardennes, au sud-est de la Belgique et au nord du Luxembourg : "
        "exactement là où personne ne l'attendait.",
        "{-cmp1}{g4}{g4.1}Entre le treize et le vingt mai, les chars allemands sortent des Ardennes, "
        "percent les lignes françaises et avancent jusqu'aux côtes de la Manche. La septième Panzerdivision d'Erwin Rommel "
        "traverse la campagne française en direction de la Somme.",
        "Les meilleures forces alliées, en Belgique, sont désormais coupées du reste de la France. {!Un piège}C'est un piège.",
    ], vis={
        "def4": dict(type="def", cles=["rapide", "chars", "avions"], terme="Blitzkrieg · « guerre éclair »",
                     t="Une offensive rapide qui combine les chars et les avions, pour remporter une victoire rapide.",
                     etape="Raids aériens déjà testés en Belgique et aux Pays-Bas", x=170, y=200, w=940),
        "cmp1": dict(type="cols", g="Ce qu'on attendait", gq="une attaque par le centre de la Belgique, comme en 1914", d="La réalité",
                     dq="l'attaque principale par la forêt vallonnée des Ardennes", vs="≠", repere="10 mai : les meilleures forces alliées envoyées en Belgique"),
        "g4": dict(type="globe", code="H3", sc=[12]),
    }),

    # ================================================================ VI. Dunkerque (idée 4)
    dict(id="dunkerque", chap="Dunkerque", fond="nuit", humeur="tension",
         retenir="Opération Dynamo, 26 mai – 4 juin 1940 : 338 000 soldats alliés évacués. Une trahison pour les Français ; pour le Royaume-Uni, la Royal Navy et la RAF sauvées.",
         beats=[
        "{g5}{g5.1}Acculé à la côte, le corps expéditionnaire britannique organise une évacuation précipitée par la mer : {!l'opération Dynamo}l'opération Dynamo. "
        "Du vingt-six mai au quatre juin 1940, trois cent trente-huit mille soldats alliés sont embarqués sur les plages de Dunkerque, vers la Grande-Bretagne.",
        "{-g5}{cols2}Dunkerque, défaite ou succès ? Tout dépend du point de vue. "
        "{cols2.g}Pour les troupes françaises, c'est une trahison : leur allié rentre chez lui et les laisse se battre seules. "
        "{cols2.d}Pour le Royaume-Uni, l'essentiel est sauvé : la Royal Navy et la RAF sont intactes.",
        "{-cols2}{chu}Et Winston Churchill, Premier ministre depuis le dix mai, le jour même de l'attaque allemande, "
        "affirme que le Royaume-Uni continuera le combat, pour vaincre plus tard, avec l'aide américaine. Le quatre juin, il déclare à la Chambre des communes :{-chu}",
        ("C", "nous nous battrons sur les plages… nous ne nous rendrons jamais", "c_church"),
        "{-c_church}Un discours pour l'épisode trois.",
    ], vis={
        "g5": dict(type="globe", code="H3", sc=[13]),
        "cols2": dict(type="cols", g="Pour les Français", gq="une trahison : les Britanniques les laissent se battre seuls", d="Pour le Royaume-Uni",
                      dq="l'armée sauvée ; la Royal Navy et la RAF intactes", vs="≠"),
        "chu": dict(type="note", terme="Churchill · Premier ministre depuis le 10 mai 1940", cles=["combat", "américaine"],
                    t="Le Royaume-Uni continuera le combat, et vaincra plus tard, avec l'aide américaine.", x=170, y=470, w=940),
        "c_church": dict(type="cit", a="Winston Churchill", o="Chambre des communes, 4 juin 1940 (traduction)", x=200, y=150, w=880),
    }),

    # ================================================================ VII. la défaite en six semaines (idée 5)
    dict(id="defaite", chap="La défaite en six semaines", fond="guerre", humeur="tension",
         retenir="Paris tombe le 14 juin 1940. ≈ 100 000 soldats français tués (recherches récentes : ≈ 60 000), 200 000 blessés, 1 850 000 prisonniers ; 8 millions sur les routes. Armistice : 22 juin, Rethondes.",
         beats=[
        "{g6}{g6.1}À partir du cinq juin, les forces allemandes frappent de la Somme vers Paris. Le gouvernement fuit, "
        "et Paris tombe le quatorze, cinq semaines après le début de la campagne. Des millions de civils affolés prennent les routes du sud.",
        "{-g6}{toll}Le coût humain est énorme. {toll.1}Environ cent mille soldats français tués au combat, selon le cours ; "
        "des recherches récentes disent environ soixante mille. {toll.2}Deux cent mille blessés. "
        "{toll.3}Un million huit cent cinquante mille prisonniers. Garde ce chiffre en tête : il reviendra avec le STO. "
        "{toll.4}Et quelque huit millions de personnes sur les routes de l'exode.",
        "{-toll}{arm}Le vingt-deux juin 1940, la France signe un armistice à Rethondes, dans la forêt de Compiègne. "
        "{arm.1}Pas un traité de paix : un accord qui met fin aux combats. Et le Royaume-Uni est désormais seul face à l'Allemagne.",
    ], vis={
        "g6": dict(type="globe", code="H3", sc=[14]),
        "toll": dict(type="liste", titre="Le coût de six semaines (chiffres du cours)", items=[
            "≈ 100 000 soldats français tués (recherches récentes : ≈ 60 000)", "200 000 blessés", "1 850 000 prisonniers de guerre",
            "≈ 8 millions de civils dans l'exode"], x=170, y=130, w=940),
        "arm": dict(type="def", cles=["fin", "combats"], terme="Armistice · 22 juin 1940, Rethondes",
                    t="Un accord qui met fin aux combats, signé par la France dans la forêt de Compiègne.",
                    etape="Pas un traité de paix · le Royaume-Uni est désormais seul face à l'Allemagne", x=170, y=200, w=940),
    }),

    # ================================================================ VIII. le dossier documentaire et premier « À toi »
    dict(id="worksheet1", chap="Le dossier documentaire : deux stratégies", fond="aube", humeur="calme",
         retenir="Pourquoi la France tombe : une vieille stratégie défensive (ligne Maginot, drôle de guerre), la surprise des Ardennes (13-20 mai), la Blitzkrieg des chars et des avions (la 7e Panzerdivision de Rommel).",
         beats=[
        "{ws_plan}Le dossier documentaire résume tout cela dans un tableau : deux camps face à face, et trois lignes. "
        "{ws_plan.g}Première ligne, le plan. Pour la France, le Royaume-Uni et leurs alliés : éviter une nouvelle guerre de tranchées et ses hécatombes, "
        "et résister à une attaque allemande massive. {ws_plan.d}Pour l'Allemagne nazie : une victoire rapide, grâce à la Blitzkrieg.",
        "{-ws_plan}{ws_meth}Deuxième ligne, les moyens. {ws_meth.1}Côté allié : la ligne Maginot et la drôle de guerre. "
        "{ws_meth.2}Puis les meilleures forces envoyées au centre de la Belgique ; Dunkerque ; et l'espoir d'une intervention britannique plus tard, avec l'aide américaine. "
        "{ws_meth.3}Côté allemand : la percée par les Ardennes jusqu'à la Manche, et des raids aériens déjà testés. "
        "{ws_meth.4}Puis l'offensive de la Somme vers Paris, du cinq au treize juin.",
        "{-ws_meth}{ws_res}Troisième ligne, le résultat. {ws_res.g}Pour la France : le gouvernement quitte Paris pour Vichy, sous Pétain, "
        "et le coût humain que tu connais. {ws_res.d}Pour l'Allemagne : Paris occupé le quatorze juin, et l'armistice de Rethondes.",
        "{-ws_res}{pa1}À toi maintenant. Un sujet de question problématisée que tu pourrais avoir : pourquoi la France est-elle vaincue si vite en 1940 ? "
        "Rédige un paragraphe, avec trois arguments et un exemple précis pour chacun.",
        ("P", 2.0),
        "{-pa1}{rep1}On peut le rédiger ainsi. {rep1.1}La France est vaincue en six semaines pour trois raisons principales. "
        "D'abord, elle s'appuie sur une vieille stratégie défensive : la ligne Maginot protège la frontière avec l'Allemagne, mais pas la frontière belge, "
        "et pendant la drôle de guerre, l'armée se contente d'attendre. "
        "{rep1.2}Ensuite, les Allemands attaquent là où personne ne les attend : tandis que les meilleures forces alliées se précipitent au centre de la Belgique, "
        "les chars passent par les Ardennes, entre le treize et le vingt mai. "
        "{rep1.3}Enfin, la Blitzkrieg combine les chars et les avions dans une offensive rapide : la septième Panzerdivision de Rommel fonce vers la Somme. "
        "{rep1.4}La défaite n'est donc pas une question de nombre, puisque la France avait 105 divisions, mais de stratégie et de surprise.",
    ], vis={
        "ws_plan": dict(type="cols", g="Alliés · le plan", gq="éviter une nouvelle guerre de tranchées ; résister à une attaque massive",
                        d="Allemagne · le plan", dq="une victoire rapide par la Blitzkrieg", vs="vs", repere="Dossier documentaire · ligne 1"),
        "ws_meth": dict(type="liste", titre="Dossier documentaire · ligne 2 : les moyens", petit=True, items=[
            "Alliés : la ligne Maginot (pas la frontière belge) ; la drôle de guerre",
            "Alliés : les meilleures forces au centre de la Belgique (10 mai) ; Dunkerque, 338 000 évacués",
            "Allemagne : percée blindée par les Ardennes jusqu'à la Manche (13-20 mai) ; raids aériens testés",
            "Allemagne : offensive de la Somme vers Paris (5-13 juin)"], x=170, y=140, w=940),
        "ws_res": dict(type="cols", g="Alliés · résultat", gq="le gouvernement à Vichy (Pétain) ; ≈ 100 000 morts, 1 850 000 prisonniers ; 8 millions dans l'exode",
                       d="Allemagne · résultat", dq="Paris occupé, 14 juin ; armistice, 22 juin", vs="vs", repere="Dossier documentaire · ligne 3"),
        "pa1": dict(type="pause", t="Question problématisée : pourquoi la France est-elle vaincue si vite en 1940 ?",
                    sous="Trois arguments, un exemple précis pour chacun. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "rep1": dict(type="liste", titre="Un paragraphe modèle", petit=True, items=[
            "Une vieille stratégie défensive → ligne Maginot, drôle de guerre",
            "La surprise → les Ardennes, 13-20 mai, pendant que les Alliés foncent en Belgique",
            "La Blitzkrieg → chars et avions ; la 7e Panzerdivision de Rommel vers la Somme",
            "Conclusion : pas le nombre (105 divisions), mais la stratégie et la surprise"], x=170, y=140, w=940),
    }),

    # ================================================================ IX. la France découpée (idée 6)
    dict(id="zones", chap="La France découpée en zones", fond="nuit", humeur="tension",
         retenir="Cinq zones : occupée (3/5, MBF), « libre » (Vichy), italienne (≈ 15 communes), Nord–Pas-de-Calais (Bruxelles), Alsace-Moselle annexée. La zone libre envahie le 11 nov. 1942.",
         beats=[
        "{g7}{g7.1}Venons-en à la France occupée. L'armistice découpe le pays en cinq zones, chacune avec un maître différent.",
        "{zones}{zones.1}Un : la zone occupée. L'Allemagne occupe les trois cinquièmes de la France métropolitaine : les régions au plus fort potentiel économique, "
        "et les côtes de l'Atlantique et du nord, pour guetter tout débarquement. Elle est administrée par un commandement militaire allemand, le MBF. "
        "{zones.2}Deux : la zone dite libre, au sud, gouvernée depuis Vichy. Une {!ligne de démarcation}ligne de démarcation sépare les deux, "
        "comme une frontière à l'intérieur du pays.",
        "{zones.3}Trois : une petite zone italienne, une quinzaine de communes, surtout dans les Alpes-Maritimes. "
        "{zones.4}Quatre : le Nord et le Pas-de-Calais, rattachés au commandement militaire allemand de Bruxelles. "
        "{zones.5}Et cinq : l'Alsace et la Moselle, purement et simplement annexées à l'Allemagne. Retour aux frontières de 1871.",
        "{-zones}{g7.2}Pourquoi des guillemets autour du mot libre ? Parce que cette liberté ne dure pas. Le onze novembre 1942, "
        "après le débarquement allié en Afrique du Nord française, l'opération Torch, les forces allemandes envahissent la zone libre. "
        "Et de novembre 1942 à septembre 1943, les troupes italiennes occupent une bien plus grande partie du sud-est.",
    ], vis={
        "g7": dict(type="globe", code="H3", sc=[16, 39]),
        "zones": dict(type="liste", titre="Cinq zones", x=942, y=20, w=328, petit=True, bande=True, items=[
            "Zone occupée : 3/5, régions riches, côtes (MBF)", "« Zone libre » : Vichy",
            "Zone italienne : ≈ 15 communes", "Nord, Pas-de-Calais : Bruxelles",
            "Alsace-Moselle annexée (1871)"]),
    }),

    # ================================================================ X. Vichy (idée 7)
    dict(id="vichy", chap="Vichy : un État qui choisit de collaborer", fond="guerre", humeur="tension",
         retenir="Vichy : l'État français, autoritaire, du maréchal Pétain, souvent empressé de collaborer. Oct. 1940 : statut des Juifs ; mars 1941 : Commissariat général aux questions juives. De Gaulle : la France libre, depuis Londres.",
         beats=[
        "{photo1}{def5}Dans la zone libre, un nouveau gouvernement prend le pouvoir, dirigé par le maréchal Pétain et installé dans la ville thermale de Vichy. "
        "{def5.1}Il se nomme l'État français, et c'est un régime autoritaire.",
        "{-def5}{collab}Dès l'armistice, il recherche la {!collaboration}collaboration avec les autorités allemandes. "
        "Derrière, l'image qui la résume : Pétain serrant la main de Hitler à Montoire, en octobre 1940, une rencontre hors du cours. "
        "Et attention à la nuance que fait le cours. {collab.1}Vichy subit la pression nazie, oui. Mais il est souvent empressé de collaborer.",
        "{-collab}{antij}La preuve : Vichy commence à persécuter les Juifs avant même que les Allemands ne l'exigent. "
        "{antij.1}En octobre 1940, un statut des Juifs, adopté par Vichy, définit qui est juif et limite leur place dans la société française. "
        "{antij.2}En mars 1941, Vichy crée un Commissariat général aux questions juives. "
        "{antij.3}Ce sont des initiatives françaises, pas des ordres allemands : un argument précis, pour toute composition sur la collaboration.",
        "{-antij}{-photo1}{dg}Face à Vichy, un homme dit non. {dg.g}D'un côté, Vichy : Pétain et la collaboration. "
        "{dg.d}De l'autre, Londres : le général de Gaulle, qui a refusé la capitulation et lancé la France libre.",
    ], vis={
        "photo1": dict(type="tableau", img="h3-montoire", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .3, .45],
                       legende="Pétain serre la main de Hitler, Montoire, 24 octobre 1940 (hors du cours) · Heinrich Hoffmann, Bundesarchiv, Bild 183-H25217, CC BY-SA 3.0 DE"),
        "def5": dict(type="def", cles=["Pétain", "Vichy"], terme="Le régime de Vichy",
                     t="Le nouveau gouvernement du maréchal Pétain, installé dans la ville thermale de Vichy.",
                     etape="« L'État français » : un régime autoritaire", x=170, y=200, w=940),
        "collab": dict(type="note", terme="Attention à la nuance", cles=["pression", "empressé"],
                       t="La collaboration : recherchée par Vichy dès l'armistice.",
                       etape="Sous la pression nazie… mais souvent empressé de collaborer.", x=170, y=200, w=940),
        "antij": dict(type="liste", titre="Avant que les Allemands ne l'exigent", cles=["statut", "Commissariat", "initiatives"], items=[
            "Octobre 1940 : un statut des Juifs définit qui est juif", "Mars 1941 : un Commissariat général aux questions juives",
            "Des initiatives françaises, pas des ordres allemands"], x=170, y=150, w=940),
        "dg": dict(type="cols", g="Vichy", gq="le maréchal Pétain · un État autoritaire · la collaboration", d="Londres",
                   dq="le général de Gaulle · la France libre · la résistance", vs="≠"),
    }),

    # ================================================================ XI. la France exploitée (idée 8)
    dict(id="exploitation", chap="La France exploitée", fond="nuit", humeur="tension",
         retenir="Exploitation : 20 millions de Reichsmarks par jour, réquisitions (charbon, nourriture, carburant), rationnement et marché noir. Main-d'œuvre : la Relève (juin 1942), puis le travail forcé, le STO (févr. 1943), créé par Vichy : hommes de 18 à 50 ans, femmes célibataires de 21 à 35 ans.",
         beats=[
        "{g9}{g9.1}Pour l'Allemagne, la France est d'abord une ressource : l'occupation est avant tout une exploitation économique. "
        "{expl}{expl.1}L'argent : la France doit payer de lourds frais d'occupation, vingt millions de Reichsmarks par jour. "
        "{expl.2}Cet argent finance les réquisitions allemandes et le pillage des ressources françaises : charbon, nourriture, carburant. "
        "{expl.3}Résultat pour les Français : le rationnement, et le {!marché noir}marché noir. "
        "{expl.4}Et les travailleurs : à partir de 1942, des ouvriers français sont envoyés en Allemagne, d'abord comme volontaires, puis, à partir de février 1943, de force, avec le STO.",
        "{-expl}{-g9}{sto}Regarde bien le STO, le Service du travail obligatoire : il a été créé par Vichy, pas par l'Allemagne. "
        "{sto.1}Avec la loi sur le travail de septembre 1942 et la loi du STO de février 1943, tous les hommes valides de dix-huit à cinquante ans, "
        "et les femmes célibataires de vingt et un à trente-cinq ans, pouvaient être envoyés.",
        "Avant cela, dès juin 1942, la Relève promettait de libérer un prisonnier de guerre français pour trois ouvriers volontaires. "
        "Souviens-toi du million huit cent cinquante mille prisonniers de 1940 : les voici, utilisés comme monnaie d'échange.",
    ], vis={
        "g9": dict(type="globe", code="H3", sc=[34]),
        "expl": dict(type="liste", titre="La France exploitée", x=850, y=270, w=400, petit=True, bande=True, items=[
            "Argent : 20 millions de RM par jour", "Réquisitions : charbon, nourriture, carburant",
            "Rationnement et marché noir", "La Relève (1942), puis le STO (1943)"]),
        "sto": dict(type="def", cles=["Vichy", "femmes"], terme="STO · Service du travail obligatoire",
                    t="Créé par Vichy en février 1943 : des travailleurs français envoyés de force en Allemagne.",
                    etape="Hommes de 18 à 50 ans, femmes célibataires de 21 à 35 ans · avant, la Relève (juin 1942) : un prisonnier libéré pour trois volontaires", x=170, y=200, w=940),
    }),

    # ================================================================ XII. les Juifs persécutés (idée 9)
    dict(id="persecution", chap="Persécutés, spoliés, déportés", fond="guerre", humeur="tension",
         retenir="≈ 350 000 Juifs en France en 1940. Aryanisation, étoile jaune (juin 1942), arrestations à partir de l'été 1942 par la police française. ≈ 80 000 déportés ; environ 3 % ont survécu.",
         beats=[
        "{g10}{g10.1}En 1940, environ trois cent cinquante mille Juifs vivent en France ; plus de la moitié sont des réfugiés étrangers. Dans la zone occupée, "
        "ils subissent aussitôt une persécution comparable à celle de la Pologne. {pers}Elle se fait par étapes. "
        "{pers.1}La spoliation : avec les lois d'{!aryanisation}aryanisation, leurs entreprises et leurs biens sont confisqués, "
        "et des familles se retrouvent sans logement ni travail. {pers.2}Le marquage : à partir de juin 1942, ils doivent porter l'étoile jaune. "
        "{pers.3}L'arrestation : à partir de l'été 1942, ils sont arrêtés en vue de leur déportation vers l'Est, surtout par la police française. "
        "{pers.4}Et à partir de 1942, des Juifs sont aussi déportés depuis la zone de Vichy.",
        "{-pers}{-g10}{bilj}Le bilan : quelque quatre-vingt mille Juifs déportés de France pendant la guerre. Seuls trois pour cent environ ont survécu.",
        "{-bilj}{milice}Attention : ici, le cours se trompe. Il attribue les arrestations de 1942 à la Milice. "
        "{milice.1}Mais la Milice n'a été créée qu'en janvier 1943. La grande rafle de juillet 1942 à Paris, "
        "la rafle du Vel' d'Hiv, les seize et dix-sept juillet, est l'œuvre de la police française. "
        "Dans ta copie, écris : la police française.",
    ], vis={
        "g10": dict(type="globe", code="H3", sc=[35]),
        "pers": dict(type="liste", titre="La persécution, étape par étape", x=850, y=70, w=400, petit=True, bande=True, items=[
            "Spoliation : « aryanisation » des entreprises et des biens", "Marquage : l'étoile jaune, juin 1942",
            "Arrestation en vue de la déportation, été 1942 : la police française", "Dès 1942 : déportations depuis la zone de Vichy aussi"]),
        "bilj": dict(type="mot", t="≈ 80 000 déportés", g="Juifs déportés de France · environ 3 % ont survécu", y=250, taille=96),
        "milice": dict(type="note", terme="Attention · une erreur du cours", cles=["Milice", "police"],
                       t="Pas « la Milice » (créée seulement en janvier 1943), mais la police française.",
                       etape="Rafle du Vel' d'Hiv, Paris, 16-17 juillet 1942", x=170, y=200, w=940),
    }),

    # ================================================================ XIII. répression et séduction (idée 10)
    dict(id="seduction", chap="Répression et séduction", fond="nuit", humeur="mystere",
         retenir="La terreur pour les opposants (Juifs, communistes, « terroristes » : Gestapo et polices de Vichy) ; la flatterie pour les autres. The Observer, 7 sept. 1941 : gagner Paris « par la flatterie plutôt que par la répression ».",
         beats=[
        "{cols3}L'occupant se sert de deux armes à la fois. {cols3.g}La terreur pour les opposants. Les Juifs, les communistes et les « terroristes », "
        "le mot de l'occupant pour désigner les résistants, sont visés à la fois par la Gestapo et par les polices de Vichy. "
        "{cols3.d}Et la flatterie pour tous les autres. La propagande allemande fait l'éloge de la culture française, flatte les milieux d'affaires français, "
        "et présente la collaboration comme la place naturelle de la France dans l'Europe nouvelle.",
        "{-cols3}{obs}Un journal britannique l'a très bien vu. Le sept septembre 1941, l'hebdomadaire The Observer "
        "décrit la Pariser Zeitung, un quotidien de langue allemande publié à Paris. {obs.1}Il présente Paris comme le futur lieu de villégiature "
        "du Herrenvolk nazi, la race des seigneurs. Et la collaboration est son thème quotidien. "
        "La conclusion de l'Observer : les Allemands cherchent à gagner Paris…{-obs}",
        ("C", "par la flatterie plutôt que par la répression", "c_obs"),
        "{-c_obs}Répression et séduction vont donc ensemble : la terreur pour les quelques-uns qui résistent, la flatterie pour le plus grand nombre.",
    ], vis={
        "cols3": dict(type="cols", g="Répression", gq="Juifs, communistes, « terroristes » : la Gestapo et les polices de Vichy",
                      d="Séduction", dq="faire l'éloge de la culture française, flatter les affaires, vendre la collaboration", vs="+"),
        "obs": dict(type="note", terme="The Observer · 7 septembre 1941", cles=["Paris", "collaboration"],
                    t="La Pariser Zeitung, aux mains des Allemands, présente Paris comme le lieu de villégiature du « Herrenvolk » nazi.",
                    etape="« La collaboration » : son thème quotidien", x=170, y=200, w=940),
        "c_obs": dict(type="cit", a="The Observer", o="7 septembre 1941, à propos de la Pariser Zeitung (traduction)", x=200, y=220, w=880),
    }),

    # ================================================================ XIV. trois documents sur la France occupée
    dict(id="sources", chap="La vie en France occupée : trois documents", fond="aube", humeur="calme",
         retenir="Document 1 (The Observer, 1941) : le découpage et la séduction · Document 2 (affiche d'aryanisation, 1942) : la persécution, ≈ 10 000 entreprises · Document 3 (affiche du STO, 1943) : l'exploitation organisée par Vichy.",
         beats=[
        "{src}Le cours propose ensuite trois documents sur la France occupée. La consigne : repérer dans chacun le découpage du territoire "
        "et les politiques de répression ou de persécution. {src.1}Document un : l'article de l'Observer que nous venons de lire, septembre 1941. "
        "{src.2}Document deux : une affiche d'aryanisation, Paris, avril 1942 : un magasin appartenant à des Juifs, confié à un administrateur provisoire non juif. "
        "{src.3}Document trois : une affiche de propagande pour le STO, 1943, qui appelle les Français à aller travailler en Allemagne.",
        "{-src}{srep}Et les réponses. {srep.1}Le document un montre le découpage du territoire : le journal ne circule pas en zone non occupée, "
        "et traite la presse de Vichy comme celle d'un pays étranger. Sa ligne est antibritannique, anticommuniste et antisémite. "
        "Mais surtout, il montre la séduction.",
        "{srep.2}Le document deux montre la persécution : la spoliation, décidée par les Allemands en octobre 1940 en zone occupée, "
        "puis rendue obligatoire par Vichy en juillet 1941 dans le reste de la France. L'historien Henry Rousso compte environ dix mille entreprises aryanisées : "
        "les mesures raciales servaient aussi l'exploitation économique.",
        "{srep.3}Le document trois montre l'exploitation et la contrainte : les propres lois de Vichy sur le travail, celle de septembre 1942, signée par Pétain, "
        "et celle de février 1943, le STO, signée par Laval. La collaboration servait l'effort de guerre allemand.",
    ], vis={
        "src": dict(type="liste", titre="La vie en France occupée · trois documents", items=[
            "The Observer, 7 septembre 1941", "Une affiche d'« aryanisation », Paris, avril 1942",
            "Une affiche de propagande pour le STO, 1943"], x=170, y=150, w=940),
        "srep": dict(type="liste", titre="Les réponses", petit=True, items=[
            "Document 1 → le découpage (pas vendu en zone libre ; presse de Vichy « étrangère »), une ligne antisémite, surtout la séduction",
            "Document 2 → la persécution : l'aryanisation (oct. 1940, puis Vichy, juillet 1941) ; ≈ 10 000 entreprises (Henry Rousso)",
            "Document 3 → l'exploitation : lois de sept. 1942 (Pétain) et de févr. 1943 (STO, Laval) ; Vichy organise le travail forcé"], x=150, y=140, w=980),
    }),

    # ================================================================ XV. l'analyse de document
    dict(id="dbq", chap="Analyse de document : le document 1", fond="aube", humeur="calme",
         retenir="Analyse de document : présenter (nature, auteur, date), situer dans le contexte, expliquer, montrer l'intérêt et les limites, conclure par un bilan critique.",
         beats=[
        "{dbq}À toi de nouveau, avec une analyse de document. Que nous apprend le document 1 sur la politique allemande en France occupée ? "
        "La démarche : {dbq.q1}présenter le document, sa nature, son auteur, sa date ; "
        "{dbq.q2}le situer dans son contexte ; {dbq.q3}l'expliquer et montrer son intérêt, avec plusieurs arguments ; "
        "{dbq.q4}puis montrer ses limites, avant un bilan critique.",
        "{-dbq}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep2}Voici un modèle. {rep2.1}Le document 1 est un article de l'Observer, un hebdomadaire britannique, publié le sept septembre 1941, "
        "qui décrit la Pariser Zeitung, un quotidien de langue allemande publié à Paris. "
        "{rep2.2}Paris est alors occupé depuis le quatorze juin 1940 ; la ligne de démarcation coupe la France en deux, et Vichy recherche la collaboration depuis l'armistice.",
        "{rep2.3}Son intérêt. D'abord, il révèle la stratégie de séduction : Paris, futur lieu de villégiature du Herrenvolk, "
        "la collaboration comme thème quotidien. Ensuite, il montre le découpage du territoire : le journal n'est pas vendu en zone non occupée. "
        "Enfin, il montre la ligne de l'occupant : antibritannique, anticommuniste et antisémite. Et il a été écrit pendant l'occupation elle-même.",
        "{rep2.4}Ses limites. D'abord, c'est un regard britannique, donc hostile, sur la propagande allemande. "
        "Ensuite, il décrit un seul journal parisien, ni toute la France, ni Vichy. "
        "Puis, il montre ce que voulait la propagande, pas ce qu'en pensaient les Français. "
        "Et il ne dit rien des vingt millions de Reichsmarks par jour, du STO, ni des rafles de 1942. "
        "Bilan critique : un document très utile pour comprendre la séduction, à compléter pour comprendre l'exploitation et la persécution.",
    ], vis={
        "dbq": dict(type="exo", niveau="dbq", titre="Que nous apprend le document 1 sur la politique allemande en France occupée ?",
                    src="Document 1 · The Observer (hebdomadaire britannique), 7 septembre 1941, à propos de la Pariser Zeitung",
                    enonce=["La Pariser Zeitung, aux mains des Allemands, présente Paris comme le futur lieu de villégiature du « Herrenvolk » nazi ; "
                            "« la collaboration » est son thème quotidien : une tentative de gagner Paris « par la flatterie plutôt que par la répression »."],
                    questions=["Présenter le document : nature, auteur, date",
                               "Le situer dans son contexte",
                               "L'expliquer et montrer son intérêt : plusieurs arguments", "Montrer ses limites, puis un bilan critique"]),
        "pa2": dict(type="pause", t="Analyse de document : que nous apprend le document 1 sur la politique allemande en France occupée ?",
                    sous="Présentation, contexte, intérêt, limites, bilan. Mets la vidéo en pause, rédige, puis relance pour voir un modèle."),
        "rep2": dict(type="liste", titre="Un modèle de réponse", petit=True, items=[
            "Présentation : The Observer, hebdomadaire britannique, 7 sept. 1941, à propos de la Pariser Zeitung",
            "Contexte : Paris occupé depuis le 14 juin 1940 ; la ligne de démarcation ; Vichy collabore",
            "Intérêt : la séduction (Herrenvolk, « collaboration ») ; le découpage ; la ligne antisémite ; écrit sur le moment",
            "Limites : un regard britannique hostile ; un seul journal ; les buts, pas la réception ; rien sur l'argent, le STO, les rafles · bilan : très utile pour la séduction"],
                     x=150, y=130, w=980),
    }),

    # ================================================================ XVI. conclusion sur la France (idée 11)
    dict(id="casparticulier", chap="Un cas particulier", fond="nuit", humeur="lumiere",
         retenir="La France, un cas particulier : un pouvoir de décision partagé (l'occupant et Vichy). Répression, racisme et ressources pour la guerre totale : 20 millions de RM par jour, le STO, ≈ 80 000 Juifs déportés.",
         beats=[
        "{q6}Alors, pour conclure : pourquoi la France est-elle un cas particulier ?",
        "{-q6}{def6}Parce que le pouvoir de décision n'y était pas unifié. Les forces d'occupation allemandes et les autorités françaises coexistaient : "
        "{!deux maîtres}deux maîtres sur le même territoire.",
        "{-def6}{trois}Pourtant, la France montre bien à quoi servait le Nouvel Ordre européen. {trois.1}La répression et la terreur contre les opposants, "
        "pratiquées à la fois par les nazis et par Vichy. {trois.2}Des politiques racistes, appliquées par les deux. "
        "{trois.3}Et l'utilisation du territoire et de la population de la France, pour fournir à l'Allemagne les ressources humaines, matérielles et financières "
        "dont elle avait besoin pour la guerre totale.",
        "{-trois}{chif}Trois chiffres le résument. {chif.1}Vingt millions de Reichsmarks par jour : l'argent. {chif.2}La Relève, puis le STO : les travailleurs. "
        "{chif.3}Quelque quatre-vingt mille Juifs déportés : la politique raciale.",
        "{-chif}{lien2}C'est le cinquième moteur du Nouvel Ordre européen, vu dans l'épisode un : fournir la guerre totale. "
        "À l'Ouest, la France est exploitée, mais traitée en partenaire, en apparence. À l'Est, dans l'épisode quatre, c'est une guerre d'anéantissement.",
    ], vis={
        "q6": dict(type="question", t="Pourquoi la France est-elle un cas particulier ?"),
        "def6": dict(type="def", cles=["unifié", "coexistaient"], terme="Un cas particulier",
                     t="Le pouvoir de décision n'était pas unifié : forces d'occupation allemandes et autorités françaises coexistaient.",
                     etape="Deux maîtres sur le même territoire", x=170, y=200, w=940),
        "trois": dict(type="liste", titre="Le Nouvel Ordre européen vu de France", cles=["terreur", "racistes", "ressources"], items=[
            "Répression et terreur : les nazis et Vichy", "Politiques racistes : appliquées par les deux",
            "Ressources pour la guerre totale : hommes, biens, argent"], x=170, y=150, w=940),
        "chif": dict(type="liste", titre="Trois chiffres, trois dimensions", items=[
            "20 millions de Reichsmarks par jour → l'argent", "La Relève (1942), le STO (1943) → les travailleurs",
            "≈ 80 000 Juifs déportés → la politique raciale"], x=170, y=150, w=940),
        "lien2": dict(type="cols", g="À l'Ouest", gq="la France exploitée, « partenaire » en apparence", d="À l'Est",
                      dq="une guerre d'anéantissement (épisode 4)", vs="≠"),
    }),

    # ================================================================ récap
    dict(id="recap2", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Pourquoi la France tombe : 105 divisions, mais une vieille stratégie défensive, face à la Blitzkrieg et à la surprise des Ardennes. "
        "{carte.2}Six semaines : Dunkerque, Paris le quatorze juin, l'exode, l'armistice le vingt-deux. "
        "{carte.3}La France découpée en cinq zones, et Vichy, empressé de collaborer, jusqu'en novembre 1942. "
        "{carte.4}Et la France exploitée et persécutée : vingt millions de Reichsmarks par jour, le STO, l'étoile jaune, quatre-vingt mille Juifs déportés.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : le Royaume-Uni seul. À partir du quatre juin 1940, l'île de Churchill fait face seule à l'Allemagne… "
        "avec le Blitz, et avec l'Amérique derrière elle.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LA DÉFAITE DE LA FRANCE", branches=[
            dict(t="Pourquoi la France tombe", items=["105 divisions, vieille stratégie", "ligne Maginot · drôle de guerre", "Ardennes · Blitzkrieg"]),
            dict(t="Six semaines", items=["Dunkerque : 338 000", "Paris 14 juin · exode", "armistice 22 juin"]),
            dict(t="Découpée · Vichy", items=["5 zones · 3/5 occupés", "Pétain : la collaboration", "zone libre envahie 11/1942"]),
            dict(t="Exploitée · persécutée", items=["20 millions de RM par jour", "STO · étoile jaune", "≈ 80 000 Juifs déportés"])]),
        "fin": dict(type="mot", t="Le Royaume-Uni seul", g="Prochain épisode · épisode 3 · 1940 – 1941", y=270, taille=78),
    }),
]

QUIZ = [
    dict(q="Qu'est-ce que la « drôle de guerre » ?",
         r=["Sept. 1939 – mai 1940 : la guerre est déclarée, mais on ne se bat presque pas à l'ouest", "L'attaque allemande par les Ardennes",
            "L'évacuation de Dunkerque", "La guerre entre Vichy et de Gaulle"], ok=0, voir="drole",
         ex="La France et le Royaume-Uni attendent derrière la ligne Maginot : une stratégie défensive."),
    dict(q="Quelle était la faiblesse de la ligne Maginot ?",
         r=["Elle ne couvrait pas la frontière franco-belge", "Elle a été construite après 1940", "Elle faisait face à l'Italie, pas à l'Allemagne",
            "Elle n'avait pas d'artillerie"], ok=0, voir="mag",
         ex="L'attaque allemande principale passe par les Ardennes, au sud-est de la Belgique et au nord du Luxembourg."),
    dict(q="Par où passe l'attaque allemande principale de mai 1940 ?",
         r=["La forêt des Ardennes", "Le centre de la Belgique, comme en 1914", "La ligne Maginot", "La Suisse"], ok=0, voir="cmp1",
         ex="Les Alliés envoient leurs meilleures forces au centre de la Belgique ; les chars percent dans les Ardennes, du 13 au 20 mai 1940."),
    dict(q="Pourquoi les troupes françaises voient-elles l'opération Dynamo comme une trahison ?",
         r=["Les Britanniques évacuent leur armée et les laissent se battre seules", "Les Britanniques capitulent les premiers",
            "Les Britanniques signent l'armistice", "Les Britanniques envahissent la Normandie"], ok=0, voir="cols2",
         ex="26 mai – 4 juin 1940 : 338 000 soldats alliés évacués ; pour le Royaume-Uni, la Royal Navy et la RAF sont sauvées."),
    dict(q="Quels chiffres donnent le coût humain de la défaite de 1940 ?",
         r=["≈ 100 000 tués, 200 000 blessés, 1 850 000 prisonniers", "338 000 tués et 8 millions de prisonniers",
            "20 millions de morts", "1 850 000 tués"], ok=0, voir="toll",
         ex="Le cours donne ≈ 100 000 morts (recherches récentes : ≈ 60 000). 338 000, c'est Dunkerque ; 8 millions, l'exode ; 20 millions, les frais d'occupation quotidiens en Reichsmarks."),
    dict(q="Quel territoire est purement et simplement annexé à l'Allemagne en 1940 ?",
         r=["L'Alsace et la Moselle", "Le Nord et le Pas-de-Calais", "Les Alpes-Maritimes", "La zone libre"], ok=0, voir="zones",
         ex="Retour aux frontières de 1871 ; le Nord et le Pas-de-Calais sont rattachés au commandement allemand de Bruxelles."),
    dict(q="Quelle mesure montre que Vichy persécute les Juifs avant que les Allemands ne l'exigent ?",
         r=["Le statut des Juifs d'octobre 1940, qui définit qui est juif", "Le STO", "L'armistice de Rethondes",
            "La ligne de démarcation"], ok=0, voir="antij",
         ex="Et en mars 1941, Vichy crée un Commissariat général aux questions juives : des initiatives françaises, pas des ordres allemands."),
    dict(q="Qui procède à la rafle de juillet 1942 à Paris ?",
         r=["La police française", "La Milice", "La Wehrmacht seule", "Les Français libres du général de Gaulle"], ok=0, voir="milice",
         ex="Le cours dit « la Milice », mais la Milice n'est créée qu'en janvier 1943 : écris « la police française »."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 3 « La Seconde Guerre mondiale », partie I.1 (l'invasion nazie de l'Europe de l'Ouest : le cas français), avec le dossier documentaire, la carte des zones, trois documents sur la France occupée et le tableau des divisions, tel qu'il est rédigé sur le site ; carte animée du chapitre (site).",
    "Correction du cours : les arrestations de l'été 1942 (rafle du Vel' d'Hiv, 16-17 juillet 1942) sont l'œuvre de la police française, non de la Milice (créée en janvier 1943).",
    "Citations : appel du 18 juin 1940 du général de Gaulle (texte original) ; Winston Churchill (4 juin 1940) et The Observer (7 septembre 1941) en traduction française.",
    "Photographie : le maréchal Pétain et Adolf Hitler à Montoire, 24 octobre 1940 (Heinrich Hoffmann, Bundesarchiv, Bild 183-H25217, via Wikimedia Commons, CC BY-SA 3.0 DE) ; la rencontre elle-même est hors du cours.",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
