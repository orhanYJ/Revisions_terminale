"""Histoire · H1 « Le krach de 1929 et ses conséquences » — édition française de la série vidéo, épisode 4 :
« Les démocraties et l'ordre libéral » (partie II.3 du cours, « De grandes démocraties réticentes à défendre l'ordre
libéral établi en 1919 »).

Traduction et adaptation de outils/serie-dnl/h1_4.py (gardé intact), selon outils/serie-dnl/EDITION_FR.md :
mêmes scènes, mêmes visuels, mêmes repères, mêmes cartes animées (la carte passe d'elle-même en français).
Key Term « Appeasement » → notion clé « l'apaisement » ; key issue → problématique ; essay → réponse à une question
problématisée. Les dessins de David Low (The Doormat, Stepping Stones to Glory) ne sont pas dans le domaine public :
décrits, pas montrés. Citations en traduction française courante, source affichée : Roosevelt « Je hais la guerre »
(1936), accords de Munich (le texte français de l'accord, préambule), Chamberlain « la paix pour notre temps »
(hors cours, dit comme tel). Le paragraphe modèle a été écrit pour la vidéo.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h1f-4"
NOTION = "Le krach de 1929 et ses conséquences"
NUM = 4
TITRE = "Les démocraties et l'ordre libéral"
SUIVANT = "Épisode 5 · La crise à l'épreuve"
PRONONCIATION = {"Mukden": "Moukdène", "Lytton": "Litonne", "Briand-Kellogg": "Briand-Kélogue", "Stimson": "Stimsonne",
                 "Panay": "Panaï", "Anschluss": "Anne-chlouss", "Vandenberg": "Vanne-denne-bergue", "Nye": "Naï",
                 "Hoover": "Houveur", "Heston": "Hèss-tonne", "Punch": "Peunch", "Lodge": "Lodje",
                 "Cabot": "Ka-botte", "Sherman": "Chèr-manne", "Smoot-Hawley": "Smoute-Hô-lé",
                 "Chamberlain": "Tchèm-beur-lène", "Woodrow": "Wou-dro", "Roosevelt": "Rouz-velt",
                 "Gerald": "Djé-ralde", "John": "Djonne", "Low": "Lô", "Detroit": "Dé-troïte",
                 "cash and carry": "kache ènde kari", "anti-Komintern": "anti-Komme-inn-tèrne"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False,
         retenir="La question de l'épisode : en 1919, les démocraties ont bâti un ordre mondial libéral. Pourquoi ont-elles refusé de le défendre dans les années 1930 ?",
         beats=[
        "{g0}{q1}Le premier septembre mille neuf cent trente-neuf. Les troupes allemandes entrent en Pologne. Deux jours plus tard, la France et le Royaume-Uni déclarent la guerre. "
        "Vingt ans après la paix de mille neuf cent dix-neuf, l'Europe est de nouveau en guerre.",
        "{-q1}{q2}Pourtant, les grandes démocraties avaient gagné la guerre précédente. Elles avaient écrit la paix, et bâti un ordre pour la garder. "
        "Alors pourquoi l'ont-elles laissé s'effondrer, pas à pas, sans se battre ?",
        "{-q2}{-g0}{plan}Le plan. {plan.1}D'abord, l'histoire sur la carte. "
        "{plan.2}Puis l'ordre libéral de mille neuf cent dix-neuf, et la Société des Nations. "
        "{plan.3}Puis l'Amérique : des mots, la neutralité, puis l'arsenal de la démocratie. "
        "{plan.4}Puis l'apaisement, ses raisons et ses conséquences. "
        "{plan.5}Et enfin, la problématique du chapitre, en réponse à une question problématisée.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[31]),
        "q1": dict(type="note", terme="1er septembre 1939", t="La guerre, de nouveau.", x=440, y=560, w=800),
        "q2": dict(type="question", t="Pourquoi les démocraties ont-elles laissé leur ordre s'effondrer ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 4 · Les démocraties et l'ordre libéral", items=[
            "Sur la carte : de 1919 à 1939", "L'ordre libéral et la Société des Nations",
            "L'Amérique : des mots, la neutralité, puis l'arsenal de la démocratie", "Royaume-Uni et France : l'apaisement et ses conséquences",
            "À l'épreuve : la problématique, en question problématisée"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · H1 · Épisode 4", t="Les démocraties et l'ordre libéral",
                      sous="1919 – 1939 · de grandes démocraties réticentes à défendre l'ordre de 1919"),
    }),

    # ================================================================ I. sur la carte : de 1919 à Shanghai
    dict(id="carte1", chap="De 1919 à Shanghai, sur la carte", fond="nuit", humeur="mystere",
         retenir="1918-1919 Quatorze points, Versailles, Société des Nations à Genève ; le Sénat américain refuse · 18 sept. 1931 Mukden, Mandchourie · 7 janv. 1932 la note Stimson, puis Shanghai bombardée.",
         beats=[
        "{g1}{g1.1}Mille neuf cent dix-huit, mille neuf cent dix-neuf. La guerre est finie. Le président américain, Woodrow Wilson, présente ses Quatorze points : "
        "la démocratie, le droit des peuples à disposer d'eux-mêmes, le libre-échange. Puis la paix leur donne des institutions. La conférence de la paix, à Paris. Le traité de Versailles. "
        "Et une Société des Nations, installée à Genève. "
        "Mais à Washington, le Sénat refuse de ratifier le traité. Les États-Unis n'y entreront jamais.",
        "{g1.2}Douze ans plus tard, le dix-huit septembre mille neuf cent trente et un. À Mukden, en Mandchourie, des soldats japonais font sauter un tronçon de leur propre voie ferrée, "
        "accusent les Chinois, et s'en servent de prétexte pour envahir. La Mandchourie devient un État fantoche, le Mandchoukouo. "
        "La Société des Nations condamne, et le Japon s'en va, tout simplement.",
        "{g1.3}Le sept janvier mille neuf cent trente-deux. Le secrétaire d'État américain, Henry Stimson, annonce que les États-Unis "
        "ne reconnaîtront aucune conquête par la force en Chine. Le Japon répond en bombardant Shanghai, avec de lourdes pertes civiles. "
        "{!Aucune réponse américaine}Aucune réponse américaine ne suit.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[0, 18, 20]),
    }),

    # ================================================================ II. sur la carte : de la neutralité à la guerre
    dict(id="carte2", chap="De la neutralité à la guerre, sur la carte", fond="nuit", humeur="tension",
         retenir="1935-1937 lois de neutralité, USS Panay · oct. 1935 Éthiopie · 7 mars 1936 Rhénanie · mars 1938 Anschluss, sept. 1938 Munich · mars 1939 Prague, 1er sept. 1939 Pologne · nov. 1939 cash and carry.",
         beats=[
        "{g2}{g2.1}De mille neuf cent trente-cinq à mille neuf cent trente-sept, le Congrès américain vote les lois de neutralité : l'Amérique restera à l'écart des guerres des autres. "
        "En décembre mille neuf cent trente-sept, en Chine, des avions japonais coulent une canonnière américaine, le Panay. Le Japon s'excuse et paie. Et il va plus loin.",
        "{g2.2}Octobre mille neuf cent trente-cinq. L'Italie de Mussolini envahit l'Éthiopie, en Afrique de l'Est. Le Royaume-Uni refuse l'embargo pétrolier qui l'aurait arrêté. "
        "Les chars et les avions italiens ne manquent de rien.",
        "{g2.3}Le sept mars mille neuf cent trente-six. Hitler envoie des troupes en Rhénanie, une région démilitarisée par le traité de Versailles. "
        "La France et le Royaume-Uni ne bougent pas.",
        "{-g2}{g3}{g3.1}Mars mille neuf cent trente-huit : l'Allemagne annexe l'Autriche, c'est l'Anschluss. Septembre mille neuf cent trente-huit : à Munich, les chefs de gouvernement britannique et français, "
        "Chamberlain et Daladier, livrent à Hitler les Sudètes, une partie de la Tchécoslovaquie.",
        "{g3.2}Mars mille neuf cent trente-neuf : l'Allemagne occupe le reste de la Tchécoslovaquie. Le premier septembre, elle envahit la Pologne. "
        "La France et le Royaume-Uni déclarent la guerre.",
        "{g3.3}Et en novembre mille neuf cent trente-neuf, la guerre une fois commencée, Roosevelt obtient une nouvelle loi : le cash and carry. "
        "Les démocraties peuvent désormais acheter des armes américaines. Dix ans après le krach, les usines américaines repartent.",
        "{-g3}{fr1}Vingt ans en huit dates. Note-les. {fr1.1}Mille neuf cent dix-neuf, la Société des Nations. "
        "{fr1.2}Mille neuf cent trente et un, la Mandchourie. {fr1.3}Mille neuf cent trente-cinq, la première loi de neutralité, et l'Éthiopie. "
        "{fr1.4}Mille neuf cent trente-six, la Rhénanie. {fr1.5}Mars mille neuf cent trente-huit, l'Anschluss. {fr1.6}Septembre mille neuf cent trente-huit, Munich. "
        "{fr1.7}Mars mille neuf cent trente-neuf, Prague. {fr1.8}Et le premier septembre mille neuf cent trente-neuf, la Pologne.",
        ("P", 2.5),
    ], vis={
        "g2": dict(type="globe", code="H1", sc=[26, 27, 29]),
        "g3": dict(type="globe", code="H1", sc=[30, 31, 32]),
        "fr1": dict(type="frise", items=[
            dict(nom="Société des Nations", d=1919), dict(nom="Mandchourie", d=1931, q="18 sept. : Mukden"),
            dict(nom="Éthiopie", d=1935), dict(nom="Rhénanie", d=1936, q="7 mars"),
            dict(nom="Anschluss", d=1938), dict(nom="Munich", d=1938, q="septembre"),
            dict(nom="Prague", d=1939), dict(nom="Pologne", d=1939, q="1er septembre : la guerre"),
        ]),
    }),

    # ================================================================ III. idée 1 : l'ordre libéral de 1919
    dict(id="wilson", chap="II.3 · L'ordre libéral de 1919", fond="nuit", humeur="lumiere",
         retenir="Les grandes démocraties de 1919 : Royaume-Uni, France, États-Unis. Le wilsonisme (Quatorze points, 1918) : démocratie, droit des peuples à disposer d'eux-mêmes, libre-échange. Institutions : conférence de la paix de Paris, Versailles, Société des Nations à Genève. Le Sénat américain refuse de ratifier : les États-Unis n'y entrent jamais.",
         beats=[
        "{q3}Maintenant le cours, idée par idée. D'abord : que devaient défendre les démocraties ?",
        "{-q3}{pw}{lo1}Les grandes démocraties de mille neuf cent dix-neuf sont trois : {lo1.1}le Royaume-Uni, {lo1.2}la France, {lo1.3}et les États-Unis.",
        "{-lo1}{wd}Leur ordre repose sur une idée : {!le wilsonisme}le wilsonisme. Dans son discours des Quatorze points, en mille neuf cent dix-huit, le président Woodrow Wilson "
        "porte le libéralisme dans la politique étrangère, {-wd}{wi}à travers trois principes. {wi.1}La démocratie. {wi.2}Le droit des peuples à disposer d'eux-mêmes : "
        "chaque peuple doit choisir son gouvernement. {wi.3}Et le libre-échange.",
        "{-wi}{inst}Puis la paix donne des institutions à ces principes. {inst.1}La conférence de la paix, à Paris. {inst.2}Le traité de Versailles. "
        "{inst.3}Et la Société des Nations, installée à Genève, pour garder la paix par la sécurité collective. "
        "C'est, dit le cours, {!l'ordre mondial libéral}l'ordre mondial libéral.",
        "{-inst}{-pw}{gap}Mais sa faiblesse est là dès la naissance. Regarde ce dessin, montré dans le cours. Il vient du magazine britannique Punch, en décembre mille neuf cent dix-neuf. "
        "Le panneau le dit : ce pont a été conçu par le président des États-Unis. La Belgique, la France, l'Angleterre, l'Italie sont en place. "
        "Mais il manque une pierre au milieu. Et l'Oncle Sam se prélasse sur la rive, les pieds en l'air, accoudé à la pierre manquante. {!La clé de voûte : USA}La clé de voûte : U S A.",
        "{-gap}{sen}Pourquoi ? Au Sénat, les républicains sont majoritaires. Et le Sénat refuse de ratifier le traité de Versailles, "
        "qui contenait le pacte de la Société des Nations. {sen.1}L'opposition est menée par le sénateur {!Henry Cabot Lodge}Henry Cabot Lodge. "
        "{sen.2}Et voici la phrase à retenir : "
        "les États-Unis ne sont jamais entrés dans la Société des Nations que leur propre président avait imaginée.",
    ], vis={
        "q3": dict(type="question", t="Qu'est-ce que les démocraties étaient censées défendre ?"),
        "pw": dict(type="tableau", img="h1-wilson", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .25],
                   legende="Woodrow Wilson, 1919, par Harris & Ewing (Library of Congress, Wikimedia Commons, domaine public)"),
        "lo1": dict(type="liste", titre="Les grandes démocraties de 1919", items=["Le Royaume-Uni", "La France", "Les États-Unis"],
                    x=270, y=170, w=740),
        "wd": dict(type="def", terme="Le wilsonisme", cles=["Quatorze", "libéralisme"],
                   t="Les Quatorze points de Woodrow Wilson (1918) : le libéralisme porté dans la politique étrangère.", x=170, y=200, w=940),
        "wi": dict(type="liste", titre="Le wilsonisme · les Quatorze points (1918)", cles=["démocratie", "peuples", "libre-échange"],
                   items=["La démocratie", "Le droit des peuples à disposer d'eux-mêmes", "Le libre-échange"], x=270, y=170, w=740),
        "inst": dict(type="liste", titre="Les institutions de l'ordre libéral", items=[
            "La conférence de la paix de Paris", "Le traité de Versailles", "La Société des Nations, installée à Genève"], x=270, y=170, w=740),
        "gap": dict(type="tableau", img="h1-gap-bridge", de=[1.0, .5, .4], a=[1.06, .5, .2],
                    legende="Leonard Raven-Hill, « The Gap in the Bridge » (Le trou dans le pont), Punch, 10 décembre 1919 (Wikimedia Commons, domaine public)"),
        "sen": dict(type="note", terme="Le Sénat dit non", cles=["Sénat", "jamais", "entrés"],
                    t="La majorité républicaine du Sénat refuse de ratifier Versailles, qui contenait le pacte de la Société des Nations.",
                    etape="L'opposition est menée par le sénateur Henry Cabot Lodge.",
                    x=170, y=200, w=940),
    }),

    # ================================================================ IV. idée 2 : les faiblesses de la SDN
    dict(id="sdn", chap="II.3 · Pourquoi la Société des Nations a échoué", fond="nuit", humeur="mystere",
         retenir="Faiblesses structurelles (dès 1919) : pas de ratification américaine · intérêts nationaux avant l'intérêt international · les agresseurs la sapent, aidés par la dépression · pas d'armée · un veto pour chaque membre, une représentation incomplète. Causes conjoncturelles (années 1930) : impuissante face aux militarismes italien, allemand, japonais.",
         beats=[
        "{pal}{d2}Deuxième idée. La Société des Nations a échoué, et le cours distingue deux sortes de causes. "
        "{d2.1}Des faiblesses structurelles, présentes dès mille neuf cent dix-neuf. Et des causes conjoncturelles, les crises des années trente, qui les ont révélées.",
        "{-d2}{str}Les faiblesses structurelles, dans l'ordre du cours. "
        "{str.1}Un : le Congrès américain n'a pas ratifié le traité de Versailles, qui contenait le pacte. "
        "{str.2}Deux : les États membres refusent de faire passer l'intérêt international avant leurs intérêts nationaux. "
        "{str.3}Trois : les nations agressives sapent son autorité. La dépression rend les États plus agressifs les uns envers les autres. "
        "{str.4}Quatre : elle n'a {!pas d'armée à elle}pas d'armée à elle. "
        "{str.5}Cinq : son mode de vote. Chaque État membre a un droit de veto, les résolutions passent donc difficilement. "
        "Et beaucoup de pays du monde n'y sont pas représentés du tout.",
        "{-str}{ctx}Puis les causes conjoncturelles. {ctx.1}La Société des Nations est impuissante face au militarisme italien, "
        "{ctx.2}face au militarisme allemand, {ctx.3}et face au militarisme japonais.",
        "{-ctx}{-pal}{lien}Dans une copie, ne fais pas une liste. Sers-toi des cinq faiblesses pour expliquer pourquoi les trois échecs "
        "des années trente étaient inévitables. Une Société sans armée, où chaque membre a un veto, ne peut pas arrêter une grande puissance.",
        "{-lien}{mlow1}Le dessinateur britannique David Low l'a dessiné en mille neuf cent trente-trois, dans un dessin intitulé Le Paillasson. {-mlow1}{low1}On ne peut pas le montrer ici, "
        "alors imagine-le. {low1.1}Un soldat japonais marche sur la Société des Nations, étendue par terre comme un paillasson. "
        "{low1.2}Les fonctionnaires de la Société s'inclinent. {low1.3}Et le ministre britannique des Affaires étrangères, John Simon, lui poudre le nez, avec une trousse pour sauver la face.",
    ], vis={
        "pal": dict(type="tableau", img="h1-palais-nations", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                    legende="Le palais des Nations, Genève, construit pour la Société des Nations (1929-1938), photo 2014 (Vassil, Wikimedia Commons, CC0)"),
        "d2": dict(type="cols", g="Structurelles", gq="des faiblesses présentes dès 1919", d="Conjoncturelles",
                   dq="les crises des années 1930, qui les révèlent", vs="+", repere="Pourquoi la Société des Nations a échoué"),
        "str": dict(type="liste", titre="Faiblesses structurelles (dès 1919)", cles=["ratifié", "nationaux", "agressives", "armée", "veto"], items=[
            "Le Congrès américain n'a pas ratifié Versailles et son pacte",
            "Les membres font passer leurs intérêts nationaux d'abord",
            "Les nations agressives la sapent ; la dépression pousse à l'agression",
            "Pas d'armée à elle",
            "Un veto pour chaque membre ; beaucoup de pays non représentés"], x=110, y=95, w=1060),
        "ctx": dict(type="liste", titre="Causes conjoncturelles (années 1930)", items=[
            "Impuissante face au militarisme italien", "Impuissante face au militarisme allemand", "Impuissante face au militarisme japonais"],
                    x=170, y=160, w=940),
        "lien": dict(type="mot", t="Cinq faiblesses → trois échecs", g="la structure explique pourquoi les échecs étaient inévitables", y=250, taille=70),
        "mlow1": dict(type="mot", t="David Low, 1933", g="« The Doormat » (Le Paillasson) : un dessin décrit, pas montré", y=250, taille=72),
        "low1": dict(type="liste", titre="David Low, « The Doormat » (1933) · décrit, pas montré", items=[
            "Un soldat japonais marche sur la Société, étendue comme un paillasson", "Les fonctionnaires de la Société s'inclinent",
            "John Simon, ministre britannique, lui poudre le nez : une trousse « pour sauver la face »"], x=150, y=150, w=980),
    }),

    # ================================================================ V. idée 3 : la Mandchourie
    dict(id="mandch", chap="II.3 · La Mandchourie : la SDN face à une grande puissance", fond="nuit", humeur="tension",
         retenir="La Corée déjà japonaise · 18 sept. 1931 attentat sous faux drapeau à Mukden → le Mandchoukouo, État fantoche · commission Lytton (rapport oct. 1932, adopté fév. 1933) · le Japon quitte la SDN (mars 1933) · Hoover : aucune action militaire américaine · Kellogg-Briand (1928) : la guerre mise hors la loi, sans moyen de contrainte.",
         beats=[
        "{g4}Troisième idée : la Société des Nations s'est montrée incapable d'arrêter l'agression d'une grande puissance. Le cas d'école, c'est la Mandchourie. "
        "La Corée, juste à côté, est déjà une possession japonaise. "
        "Le dix-huit septembre mille neuf cent trente et un, des soldats japonais organisent un {!attentat sous faux drapeau}attentat sous faux drapeau contre leur propre voie ferrée, à Mukden. "
        "C'est le prétexte pour envahir la Mandchourie, où ils installent le Mandchoukouo, un État fantoche.",
        "{-g4}{mk}Et la Société des Nations ? {mk.1}Elle envoie une enquête, la commission Lytton. "
        "{mk.2}Son rapport n'arrive qu'en octobre mille neuf cent trente-deux, plus d'un an après, et il condamne le Japon. "
        "{mk.3}La Société adopte le rapport en février mille neuf cent trente-trois. {mk.4}Et le Japon quitte tout simplement la Société, en mars mille neuf cent trente-trois. "
        "{mk.5}Aucune sanction ne suit.",
        "{-mk}{hv}Et les États-Unis ? Le président Hoover refuse toute action militaire américaine en Extrême-Orient.",
        "{-hv}{kb}Une autre pièce de l'ordre s'effondre ici. Le pacte {!Briand-Kellogg}Briand-Kellogg, en mille neuf cent vingt-huit, avait mis la guerre hors la loi, "
        "et obligeait ses signataires à négocier. {kb.1}Mais il ne prévoyait aucun moyen de faire respecter cette promesse. "
        "La Mandchourie l'a prouvé, trois ans plus tard.",
        "{-kb}{prom}Retiens la formule : {!une promesse sans mécanisme}une promesse sans mécanisme.",
    ], vis={
        "g4": dict(type="globe", code="H1", sc=[18]),
        "mk": dict(type="liste", titre="La réponse de la Société des Nations, 1931-1933", cles=["Lytton", "condamne", "quitte", "sanction"], items=[
            "Une enquête : la commission Lytton", "Rapport en octobre 1932 seulement : il condamne le Japon",
            "Février 1933 : la Société adopte le rapport", "Mars 1933 : le Japon quitte la Société", "Aucune sanction"],
                   x=170, y=120, w=940),
        "hv": dict(type="note", terme="Washington, 1931", cles=["Hoover", "aucune"],
                   t="Le président Hoover ne veut aucune action militaire américaine en Extrême-Orient.",
                   etape="La Société condamne ; personne n'agit", x=170, y=220, w=940),
        "kb": dict(type="def", terme="Le pacte Briand-Kellogg (1928)", cles=["hors", "négocier"],
                   t="Un traité qui met la guerre hors la loi et oblige ses signataires à négocier.",
                   etape="Mais aucun moyen de le faire respecter", x=170, y=200, w=940),
        "prom": dict(type="mot", t="Une promesse sans mécanisme", g="Briand-Kellogg, 1928 → Mandchourie, 1931", y=260, taille=76),
    }),

    # ================================================================ VI. idée 4 : la doctrine Stimson
    dict(id="stimson", chap="II.3 · L'Amérique : des mots, pas d'action", fond="nuit", humeur="tension",
         retenir="7 janv. 1932, la note Stimson : aucune reconnaissance d'une situation créée par la force en Chine (souveraineté, intégrité territoriale, porte ouverte). Une doctrine de non-reconnaissance, pas d'action. Le Japon bombarde Shanghai (1932) : aucune réponse américaine.",
         beats=[
        "{g5}Quatrième idée : les États-Unis condamnent l'agression en paroles, mais refusent d'agir. "
        "{st}{st.1}Le sept janvier mille neuf cent trente-deux, le secrétaire d'État, Henry Stimson, envoie une note au Japon et à la Chine. "
        "{st.2}Le message ? Les États-Unis ne reconnaîtront aucune situation, aucun traité, aucun accord obtenu par la force, "
        "s'il porte atteinte aux droits que les traités leur donnent en Chine. "
        "{st.3}C'est-à-dire la souveraineté et l'intégrité territoriale de la République chinoise. "
        "{st.4}Et la politique de la porte ouverte : toutes les grandes puissances ont un accès égal au commerce en Chine.",
        "{-st}{-g5}{od}Note l'intérêt américain : la porte ouverte. Stimson défend un principe de l'ordre de mille neuf cent dix-neuf, "
        "mais aussi le commerce américain en Chine.",
        "{-od}{wa}Alors, qu'est-ce que la doctrine Stimson ? {!non-reconnaissance}Une doctrine de non-reconnaissance, pas d'action.",
        "{-wa}{jp}Et la réponse du Japon ? {jp.1}Le Japon est furieux. Après tout, dit-il, les États-Unis ont eux-mêmes conquis de nouveaux territoires, "
        "il y a quelques décennies à peine. {jp.2}Puis il bombarde Shanghai, en mille neuf cent trente-deux, faisant d'énormes pertes. "
        "{jp.3}Aucune réponse américaine ne suit.",
    ], vis={
        "g5": dict(type="globe", code="H1", sc=[20]),
        "st": dict(type="liste", titre="La note Stimson · 7 janv. 1932", bande=True, petit=True, x=50, y=90, w=560,
                   cles=["reconnaissance", "force", "ouverte"], items=[
                       "Au Japon et à la Chine", "Aucune reconnaissance d'une conquête par la force",
                       "Souveraineté, intégrité territoriale de la Chine", "La porte ouverte en Chine"]),
        "od": dict(type="def", terme="La politique de la porte ouverte", cles=["égal", "accès"],
                   t="Un accès égal aux affaires en Chine pour toutes les grandes puissances.",
                   etape="Un principe, et un intérêt commercial américain", x=170, y=200, w=940),
        "wa": dict(type="cols", g="Des mots", gq="« nous ne reconnaîtrons pas » une conquête par la force", d="L'action",
                   dq="aucune : ni sanction, ni force, ni réponse", vs="≠", repere="La doctrine Stimson"),
        "jp": dict(type="liste", titre="La réponse du Japon", items=[
            "Furieux : « les États-Unis ont conquis des territoires il y a quelques décennies »",
            "1932 : Shanghai bombardée, d'énormes pertes", "Aucune réponse américaine"], x=170, y=160, w=940),
    }),

    # ================================================================ VII. idée 5 : les lois de neutralité
    dict(id="neutre", chap="II.3 · Les lois de neutralité", fond="nuit", humeur="mystere",
         retenir="L'isolationnisme après la Dépression : la politique intérieure d'abord. Lois de neutralité (un Congrès démocrate, sous la pression de Nye, Vandenberg) : 1935 embargo sur les armes · 1936 pas de prêts · 1937 embargo permanent, pas de voyages sur les navires des belligérants, autres marchandises au comptant et transportées par l'acheteur. Roosevelt : « Je hais la guerre » (1936). Déc. 1937 : l'USS Panay ; le Japon s'excuse, paie — et y voit un permis.",
         beats=[
        "{fdr}Cinquième idée : les lois de neutralité rendent indisponible la plus grande des démocraties. "
        "{iso}{iso.1}La cause, c'est la Grande Dépression. Les États-Unis se replient dans {!l'isolationnisme}l'isolationnisme, et ferment les yeux sur les tensions internationales. "
        "{iso.2}Le Congrès et les présidents se tournent vers la politique intérieure : protectionnisme et État-providence. C'était l'épisode trois.",
        "{-iso}{nad}Un Congrès démocrate, sous la pression des isolationnistes, parmi eux les sénateurs républicains Gerald Nye et Arthur Vandenberg, "
        "vote les lois de neutralité. "
        "{-nad}{na}Retiens-les en trois temps. {na.1}En mille neuf cent trente-cinq, un embargo sur les armes vers toute nation engagée dans un conflit. "
        "{na.2}En mille neuf cent trente-six, l'interdiction de leur prêter de l'argent. "
        "{na.3}En mille neuf cent trente-sept, l'embargo devient permanent, et les Américains n'ont plus le droit de voyager sur les navires des nations en guerre.",
        "{-na}{prec}La loi de mille neuf cent trente-sept ajoute une règle. "
        "{prec.1}Les autres marchandises peuvent encore être vendues aux nations en guerre, mais seulement au comptant. "
        "{prec.2}Et elles doivent les emporter sur leurs propres navires. C'est déjà un cash and carry, deux ans avant la loi de mille neuf cent trente-neuf.",
        "{-prec}{nye}Pourquoi de telles lois ? Prends la commission Nye, de mille neuf cent trente-quatre à mille neuf cent trente-six. Pendant deux ans, elle soutient que marchands d'armes et banquiers "
        "avaient entraîné l'Amérique dans la Première Guerre mondiale. {nye.1}Les lois de neutralité sont écrites pour que cela ne puisse pas se reproduire, "
        "quoi qu'il arrive en Europe ou en Asie.",
        "{-nye}{-fdr}{rw}Même le président dit l'humeur du pays. En mille neuf cent trente-six, Franklin Roosevelt déclare :",
        ("C", "Je hais la guerre.", "c_war"),
        "{-c_war}{-rw}{g6}{pn}Puis vient l'épreuve. {pn.1}En décembre mille neuf cent trente-sept, en Chine, des avions japonais bombardent la canonnière américaine Panay, et trois pétroliers américains. "
        "{pn.2}Le Japon s'excuse, paie une indemnité, et promet qu'il n'y aura plus d'attaque. "
        "{pn.3}Et le Japon lit le ton américain comme un permis pour de nouvelles agressions.",
        "{-pn}{-g6}",
    ], vis={
        "fdr": dict(type="tableau", img="h1-roosevelt-1933", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .25],
                    legende="Franklin D. Roosevelt, 1933, par Elias Goldensky (Wikimedia Commons, domaine public)"),
        "iso": dict(type="liste", titre="L'Amérique se replie", cles=["isolationnisme", "intérieure"], items=[
            "Après la Dépression : l'isolationnisme, les yeux fermés sur les tensions internationales",
            "La politique intérieure d'abord : protectionnisme et État-providence"], x=170, y=170, w=940),
        "nad": dict(type="def", terme="Les lois de neutralité (1935-1937)", cles=["démocrate", "Nye", "Vandenberg"],
                    t="Votées par un Congrès démocrate, sous la pression d'isolationnistes comme les sénateurs républicains Gerald Nye et Arthur Vandenberg.",
                    x=170, y=200, w=940),
        "na": dict(type="liste", titre="Les lois de neutralité", cles=["armes", "prêter", "permanent"], items=[
            "1935 : embargo sur les armes vers les nations en conflit",
            "1936 : interdiction de leur prêter de l'argent",
            "1937 : embargo permanent ; pas d'Américains à bord des navires des belligérants"], x=150, y=150, w=980),
        "prec": dict(type="note", terme="1937 · un premier « cash and carry »", cles=["comptant", "navires"],
                     t="Les autres marchandises restent vendues aux nations en guerre, mais seulement au comptant…",
                     etape="… et emportées sur leurs propres navires.",
                     x=170, y=200, w=940),
        "nye": dict(type="note", terme="La commission Nye (1934-1936)", cles=["armes", "banquiers"],
                    t="Les marchands d'armes et les banquiers, soutient-elle, ont entraîné l'Amérique dans la Première Guerre mondiale.",
                    etape="Les lois de neutralité : plus jamais", x=170, y=200, w=940),
        "rw": dict(type="mot", t="Le président dit l'humeur du pays", g="Franklin D. Roosevelt, 1936", y=150, taille=56),
        "c_war": dict(type="cit", a="Franklin D. Roosevelt", o="discours « I hate war » (« Je hais la guerre »), 1936", x=200, y=300, w=880),
        "g6": dict(type="globe", code="H1", sc=[26]),
        "pn": dict(type="liste", titre="L'USS Panay · décembre 1937", bande=True, petit=True, x=620, y=440, w=620,
                   cles=["Panay", "excuse", "permis"], items=[
                       "USS Panay + trois pétroliers américains bombardés", "Le Japon s'excuse, paie, promet",
                       "… et y voit un permis"]),
    }),

    # ================================================================ VIII. idée 6 : cash and carry
    dict(id="cash", chap="II.3 · De la neutralité à l'arsenal de la démocratie", fond="nuit", humeur="lumiere",
         retenir="Nov. 1939, la guerre commencée : la loi de neutralité de 1939, le cash and carry (payer comptant, transporter sur ses propres navires) → avantage au Royaume-Uni et à la France, maîtres des mers. L'Amérique, arsenal de la démocratie : le réarmement, pas le New Deal, met fin à la Dépression.",
         beats=[
        "{g7}Sixième idée : à partir de mille neuf cent trente-neuf, les États-Unis passent de la neutralité à l'approvisionnement des démocraties. "
        "{cc}{cc.1}C'est seulement une fois la guerre commencée que Roosevelt convainc le Congrès, en session extraordinaire, de voter la loi de neutralité de mille neuf cent trente-neuf. "
        "{cc.2}Les États-Unis peuvent désormais vendre des armes aux démocraties européennes, selon le principe du {!cash and carry}cash and carry : "
        "{cc.3}payer comptant, et emporter la marchandise sur ses propres navires.",
        "{-cc}{fv}À qui cela profite-t-il ? {fv.1}À ceux qui tiennent la mer : le Royaume-Uni et la France. "
        "{fv.2}Mais seulement s'ils ont l'argent. {fv.3}Et cela arrive dix ans après la crise qui avait produit l'isolement.",
        "{-fv}{-g7}{ars}Résultat : l'Amérique devient ce que Roosevelt appellera, en décembre mille neuf cent quarante, {!l'arsenal de la démocratie}l'arsenal de la démocratie. "
        "Ses usines, durement frappées depuis mille neuf cent vingt-neuf, repartent pour armer les guerres des autres.",
        "{-ars}{sh}Un exemple du cours : des chars Sherman qui sortent de la chaîne de l'arsenal de chars de Detroit. "
        "{sh.1}Cette usine n'existait pas en mille neuf cent trente-neuf.",
        "{-sh}{cure}Voici donc une idée forte pour une copie. {cure.1}La Dépression ne s'est pas terminée avec le New Deal, mais avec le réarmement. "
        "{cure.2}Le même remède que l'Allemagne, appliqué tard, et de l'autre côté.",
    ], vis={
        "g7": dict(type="globe", code="H1", sc=[32]),
        "cc": dict(type="liste", titre="La loi de neutralité de 1939", bande=True, petit=True, x=620, y=440, w=620,
                   cles=["extraordinaire", "comptant", "navires"], items=[
                       "La guerre commencée : session extraordinaire", "Des armes pour les démocraties",
                       "Payer comptant · transporter sur ses navires"]),
        "fv": dict(type="liste", titre="À qui cela profite-t-il ?", bande=True, petit=True, x=620, y=440, w=620,
                   items=["À qui tient la mer : Royaume-Uni, France", "… s'ils ont l'argent",
                          "… et dix ans après la crise"]),
        "ars": dict(type="def", terme="L'arsenal de la démocratie", cles=["1929", "repartent"],
                    t="L'Amérique, fournisseur d'armes des démocraties à partir de 1939, sans combattre elle-même.",
                    etape="Des usines à l'arrêt depuis 1929 repartent pour armer les guerres des autres", x=170, y=200, w=940),
        "sh": dict(type="note", terme="Dans le cours", cles=["Sherman", "Detroit"],
                   t="Des chars M4 Sherman sortent de la chaîne de l'arsenal de chars de Detroit.",
                   etape="Une usine qui n'existait pas en 1939", x=170, y=200, w=940),
        "cure": dict(type="cols", g="Allemagne", gq="le réarmement absorbe les chômeurs, dès 1933", d="États-Unis",
                     dq="le réarmement met fin à la Dépression, dès 1939", vs="=", repere="Pas le New Deal : le réarmement"),
    }),

    # ================================================================ IX. idée 7 : l'apaisement et ses six raisons
    dict(id="apais", chap="II.3 · L'apaisement, et six raisons rationnelles", fond="nuit", humeur="tension",
         retenir="L'apaisement (notion clé) : céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre. 1935 Éthiopie : pas d'embargo pétrolier · 1936 Rhénanie : pas d'intervention. Six raisons : pacifisme · un empire à surveiller, pas d'argent pour réarmer · sympathie pour l'Allemagne · les problèmes économiques d'abord · l'isolationnisme américain · la peur du communisme plus que du fascisme.",
         beats=[
        "{ap}Septième idée. De l'autre côté de l'Atlantique, le Royaume-Uni et la France suivent une politique qui porte un nom. La notion clé de cet épisode : "
        "{!l'apaisement}l'apaisement. {ap.1}Céder aux exigences d'un agresseur, dans l'espoir d'éviter la guerre.",
        "{-ap}{dbl}Avec l'isolationnisme américain, l'apaisement a contrecarré tous les efforts de la Société des Nations pour empêcher les conflits. Deux épreuves. "
        "{dbl.1}En mille neuf cent trente-cinq, quand Mussolini attaque l'Éthiopie, le Royaume-Uni refuse l'embargo pétrolier qui l'aurait arrêté.",
        "{-dbl}{g8}{rh}{rh.1}Et en mars mille neuf cent trente-six, Hitler envoie des troupes en Rhénanie, démilitarisée par Versailles. La France et le Royaume-Uni décident de ne pas intervenir. "
        "{rh.2}L'exemple du cours : l'armée allemande est entrée avec l'ordre de se retirer au premier signe de résistance française. "
        "{!Il n'y en eut aucun}Il n'y en eut aucun. {rh.3}Hitler dira plus tard que les quarante-huit heures qui ont suivi furent les plus éprouvantes de sa vie.",
        "{-rh}{-g8}Pourquoi ont-ils cédé ? {six}Le cours donne six raisons, et il faut les apprendre. "
        "{six.1}Un : le pacifisme. Les deux pays veulent à tout prix éviter une autre guerre mondiale. "
        "{six.2}Deux : le Royaume-Uni surveille son empire, et n'a pas les moyens d'un grand réarmement. "
        "{six.3}Trois : beaucoup de Britanniques ont de la sympathie pour l'Allemagne. Ils trouvent qu'elle a été traitée injustement à la fin de la guerre. "
        "{six.4}Quatre : les deux pays sont très affaiblis, et leurs propres problèmes économiques passent d'abord. "
        "{six.5}Cinq : tous deux pensent que l'isolationnisme américain les laisse sans protection. "
        "{six.6}Et six : tous deux craignent le communisme plus que le fascisme.",
        "{-six}{ns}La phrase importante, maintenant. {!Aucune de ces raisons n'est stupide}Aucune de ces raisons n'est stupide. "
        "Ensemble, elles expliquent pourquoi des démocraties qui pouvaient agir ont choisi de ne rien faire.",
    ], vis={
        "ap": dict(type="def", terme="Notion clé · L'apaisement", cles=["Céder", "agresseur", "éviter"],
                   t="Céder aux exigences d'un agresseur dans l'espoir d'éviter la guerre.",
                   etape="Le Royaume-Uni et la France, de l'Éthiopie (1935) à Munich (1938)", x=170, y=200, w=940),
        "dbl": dict(type="note", terme="Épreuve 1 · l'Éthiopie, 1935", cles=["pétrolier", "embargo"],
                    t="Mussolini attaque l'Éthiopie. Le Royaume-Uni refuse l'embargo pétrolier qui l'aurait arrêté.",
                    etape="Apaisement + isolationnisme américain : la Société est bloquée", x=170, y=200, w=940),
        "g8": dict(type="globe", code="H1", sc=[29]),
        "rh": dict(type="liste", titre="Épreuve 2 · la Rhénanie, 7 mars 1936", bande=True, petit=True, x=620, y=440, w=620,
                   cles=["intervenir", "retirer", "48"], items=[
                       "La France et le Royaume-Uni n'interviennent pas", "Ordre : se retirer si la France résiste",
                       "Hitler : les 48 heures les plus éprouvantes"]),
        "six": dict(type="liste", titre="Six raisons rationnelles de l'apaisement", cles=["pacifisme", "empire", "injustement", "économiques", "isolationnisme", "communisme"], items=[
            "Le pacifisme : éviter à tout prix une autre guerre mondiale", "Le Royaume-Uni surveille son empire ; pas les moyens d'un grand réarmement",
            "Sympathie pour une Allemagne traitée injustement à Versailles (1919)", "Des pays affaiblis : leurs problèmes économiques d'abord",
            "L'isolationnisme américain les laisse sans protection", "Ils craignent le communisme plus que le fascisme"], x=120, y=105, w=1040),
        "ns": dict(type="mot", t="Aucune de ces raisons n'est stupide", g="des démocraties qui auraient pu agir ont choisi de ne pas le faire", y=250, taille=72),
    }),

    # ================================================================ X. idée 8 : les conséquences jusqu'en septembre 1939
    dict(id="consq", chap="II.3 · Les conséquences : les marches vers la guerre", fond="guerre", humeur="tension",
         retenir="1931 Mandchourie → 1935 Éthiopie → 1936 Rhénanie → mars 1938 Anschluss → sept. 1938 Munich (les Sudètes cédés) → mars 1939 Prague → 1er sept. 1939 Pologne ; le 3 sept., la France et le Royaume-Uni déclarent la guerre. Chaque concession est suivie d'une exigence plus grande.",
         beats=[
        "{q4}Dernière idée du cours : les conséquences. L'apaisement a permis à l'Allemagne nazie d'aller plus loin, jusqu'en septembre mille neuf cent trente-neuf. "
        "Le cours donne une chaîne. Apprends-la dans l'ordre.",
        "{-q4}{sl}{sl.1}Mille neuf cent trente et un, la Mandchourie. La Société des Nations condamne, le Japon s'en va. Aucune sanction. "
        "{sl.2}Mille neuf cent trente-cinq, l'Éthiopie. Le Royaume-Uni refuse l'embargo pétrolier. "
        "{sl.3}Mille neuf cent trente-six, la Rhénanie. La France et le Royaume-Uni ne bougent pas. "
        "{sl.4}Mars mille neuf cent trente-huit, l'Anschluss : l'Allemagne annexe l'Autriche. "
        "{sl.5}Septembre mille neuf cent trente-huit, Munich. Hitler exige une partie de la Tchécoslovaquie. Chamberlain et Daladier rencontrent Hitler et Mussolini, et ils acceptent. "
        "Les Tchèques ne sont même pas invités. "
        "{sl.6}Mars mille neuf cent trente-neuf, Prague : l'Allemagne occupe toute la Tchécoslovaquie. "
        "{sl.7}Et le premier septembre mille neuf cent trente-neuf, la Pologne. Le trois, la France et le Royaume-Uni déclarent la guerre.",
        "{-sl}{mun}Munich est l'acte qui définit l'apaisement. L'accord prend acte de",
        ("C", "la cession à l'Allemagne des territoires des Allemands des Sudètes", "c_mun"),
        "{-c_mun}{-mun}{mun2}Voici Neville Chamberlain, de retour de Munich, le trente septembre mille neuf cent trente-huit, à l'aérodrome de Heston, près de Londres. "
        "Il agite le papier qu'il a signé avec Hitler. {ch}{ch.1}Le soir même, et ce n'est pas dans le cours, il parle de {!la paix pour notre temps}la paix pour notre temps. "
        "{ch.2}Six mois plus tard, l'Allemagne occupe Prague. Munich n'avait rien acheté.",
        "{-ch}{-mun2}{axe}Entre-temps, les trois puissances militaristes se rapprochent. En mille neuf cent trente-six, l'axe Rome-Berlin. "
        "{axe.1}La même année, l'Allemagne et le Japon signent le pacte anti-Komintern, que l'Italie rejoint en mille neuf cent trente-sept. "
        "Leur alliance en bonne et due forme, le pacte tripartite, ne vient qu'en septembre mille neuf cent quarante.",
        "{-axe}{mlow2}David Low a dessiné toute la chaîne deux ans avant Munich, en juillet mille neuf cent trente-six, dans un dessin intitulé Les marches vers la gloire. "
        "{-mlow2}{low2}Là encore, imagine-le. {low2.1}Hitler monte un escalier fait des dos courbés des dirigeants sans colonne vertébrale de la démocratie. "
        "{low2.2}Les marches s'appellent le réarmement, la Rhénanie, {low2.3}et la dernière marche : maître de l'univers.",
        "{-low2}{arg}Voilà l'argument central contre l'apaisement : {!une exigence plus grande}chaque concession est suivie d'une exigence plus grande. "
        "Le désordre européen s'aggrave à chaque concession.",
    ], vis={
        "q4": dict(type="question", t="À quoi l'apaisement a-t-il mené ?"),
        "sl": dict(type="liste", titre="Les marches vers la guerre, 1931-1939", cles=["Mandchourie", "Éthiopie", "Rhénanie", "Anschluss", "Munich", "Prague", "Pologne"], items=[
            "1931 · Mandchourie : la SDN condamne, le Japon part", "1935 · Éthiopie : pas d'embargo pétrolier",
            "1936 · Rhénanie : pas d'intervention", "Mars 1938 · Anschluss : l'Autriche annexée",
            "Sept. 1938 · Munich : les Sudètes cédés", "Mars 1939 · Prague : toute la Tchécoslovaquie",
            "1er sept. 1939 · Pologne : invasion ; la guerre le 3 sept."], x=120, y=95, w=1040),
        "mun": dict(type="tableau", img="h1-chamberlain-munich", fond=True, de=[1.0, .5, .4], a=[1.25, .52, .4],
                    legende="Neville Chamberlain de retour de Munich, aérodrome de Heston, 30 septembre 1938 (ministère britannique de l'Information, Wikimedia Commons, domaine public)"),
        "mun2": dict(type="tableau", img="h1-chamberlain-munich", de=[1.0, .5, .4], a=[1.15, .52, .4],
                     legende="Neville Chamberlain de retour de Munich, aérodrome de Heston, 30 septembre 1938 (ministère britannique de l'Information, Wikimedia Commons, domaine public)"),
        "c_mun": dict(type="cit", a="Les accords de Munich", o="29-30 septembre 1938 (traduction du texte de l'accord)", x=200, y=200, w=880),
        "ch": dict(type="liste", titre="Aérodrome de Heston · 30 septembre 1938", bande=True, petit=True, x=60, y=430, w=620,
                   items=["« La paix pour notre temps » (le soir même ; hors cours)", "Mars 1939 : Prague. Munich n'avait rien acheté."]),
        "axe": dict(type="note", terme="L'Axe", cles=["axe", "anti-Komintern", "tripartite"],
                    t="L'axe Rome-Berlin (1936) · le pacte anti-Komintern : Allemagne et Japon 1936, Italie 1937.",
                    etape="L'alliance en bonne et due forme, le pacte tripartite : septembre 1940", x=170, y=200, w=940),
        "mlow2": dict(type="mot", t="David Low, juillet 1936", g="« Stepping Stones to Glory » (Les marches vers la gloire) : décrit, pas montré", y=250, taille=72),
        "low2": dict(type="liste", titre="David Low, « Stepping Stones to Glory » (juillet 1936) · décrit", items=[
            "Hitler monte sur les dos courbés des « dirigeants sans colonne vertébrale de la démocratie »",
            "Les marches : le réarmement, la Rhénanie…", "La dernière marche : « maître de l'univers » (Boss of the Universe)"], x=150, y=150, w=980),
        "arg": dict(type="mot", t="Chaque concession, une exigence plus grande", g="l'argument central contre l'apaisement", y=250, taille=74),
    }),

    # ================================================================ XI. à vérifier
    dict(id="verif", chap="Attention : points à vérifier", fond="aube", humeur="calme",
         retenir="Points qui dépassent le document du cours : la commission Nye · Lodge, à la tête de l'opposition à la SDN · le détail des lois de neutralité · le pacte tripartite, seulement en 1940.",
         beats=[
        "{chk}Quatre points dépassent le document du cours : vérifie-les dans un manuel. {chk.1}La commission Nye. "
        "{chk.2}Le sénateur Lodge, qui mène l'opposition à la Société des Nations. {chk.3}Le détail de chaque loi de neutralité. "
        "{chk.4}Et la date du pacte tripartite : septembre mille neuf cent quarante.",
    ], vis={
        "chk": dict(type="liste", titre="Points qui dépassent le document du cours", cles=["Nye", "Lodge", "neutralité", "tripartite"], items=[
            "La commission Nye (1934-1936)", "Le sénateur Lodge mène l'opposition à la SDN",
            "Les lois de neutralité, une par une : 1935, 1936, 1937", "Le pacte tripartite : septembre 1940"], x=150, y=140, w=980),
    }),

    # ================================================================ XII. à l'épreuve : la problématique en question problématisée
    dict(id="essai", chap="À toi · la problématique en question problématisée", fond="aube", humeur="calme",
         retenir="Sujet : « Les grandes puissances démocratiques sont-elles en partie responsables des origines de la Seconde Guerre mondiale ? » · Oui, en partie : elles ont bâti un ordre qu'elles ne voulaient pas garantir, l'ont affaibli après 1929, ont refusé de le défendre — mais l'initiative revient aux régimes militaristes.",
         beats=[
        "{ki}Passons à l'épreuve. Voici la problématique du chapitre, posée comme une question problématisée. "
        "{ki.1}Les grandes puissances démocratiques sont-elles en partie responsables des origines de la Seconde Guerre mondiale ?",
        "{-ki}{mots}D'abord, lis bien le sujet. {mots.1}En partie : il appelle une réponse nuancée, pas un oui ou un non. "
        "{mots.2}Les grandes puissances démocratiques : le Royaume-Uni, la France et les États-Unis, les garants de l'ordre de mille neuf cent dix-neuf. "
        "{mots.3}Dans quelle mesure : des arguments pour, des arguments contre, et une réponse argumentée.",
        "{-mots}{pa1}",
        ("P", 4.0),
        "{-pa1}{pl}Voici un plan modèle. {pl.1}Un : elles ont bâti un ordre qu'elles ne voulaient pas garantir. "
        "Le Sénat refuse Versailles ; la Société des Nations n'a pas d'armée, chaque membre a un veto ; le pacte Briand-Kellogg n'a aucun mécanisme. "
        "{pl.2}Deux : elles l'ont affaibli économiquement après mille neuf cent vingt-neuf. Le tarif Smoot-Hawley et les représailles qui suivent étouffent le commerce mondial : en mille neuf cent trente-quatre, il a chuté des deux tiers. "
        "Le rappel des prêts américains déstabilise l'Allemagne. Et la défense de l'étalon-or aggrave le chômage. "
        "{pl.3}Trois : elles refusent de le défendre quand il est mis à l'épreuve. La Mandchourie et la note Stimson, les lois de neutralité et le Panay, "
        "pas d'embargo pétrolier contre l'Italie, la Rhénanie, Munich. "
        "{pl.4}Et quatre, l'autre versant : l'initiative revient aux régimes militaristes, à Berlin, à Rome et à Tokyo.",
        "{-pl}{pa2}",
        ("P", 4.0),
        "{-pa2}{par}Voici un modèle de ce dernier paragraphe, écrit pour cette vidéo. "
        "{par.1}Cependant, les démocraties ont été réticentes, mais ce ne sont pas elles qui ont décidé la guerre. "
        "{par.2}Le militarisme est un choix délibéré, à Berlin, à Rome et à Tokyo. Ces régimes renforcent leurs armées, donnent aux militaires le contrôle du gouvernement, et choisissent une politique étrangère agressive. "
        "{par.3}La misère économique a donné un public aux nazis, mais elle n'obligeait personne à piller les nations conquises. "
        "{par.4}Et l'apaisement avait des raisons rationnelles : le pacifisme, un empire à surveiller, la peur du communisme. "
        "{par.5}Les démocraties ont donc facilité l'agression. Mais ce sont les agresseurs qui ont choisi la guerre.",
        "{-par}{ccl}Et la conclusion. {ccl.1}Oui, en partie. Les démocraties sont responsables d'un ordre qu'elles ont affaibli et refusé de défendre. "
        "Les agresseurs sont responsables de la guerre. {ccl.2}Et reprends le mot même du cours. {!réticentes}Réticentes. Elles auraient pu agir, et ont choisi de ne pas le faire.",
    ], vis={
        "ki": dict(type="question", t="Les grandes puissances démocratiques sont-elles en partie responsables des origines de la Seconde Guerre mondiale ?"),
        "mots": dict(type="liste", titre="Lire le sujet", cles=["partie", "démocratiques", "mesure"], items=[
            "« En partie » : une réponse nuancée", "« Les grandes puissances démocratiques » : Royaume-Uni, France, États-Unis",
            "« Dans quelle mesure » : pour, contre, une réponse argumentée"], x=150, y=150, w=980),
        "pa1": dict(type="pause", t="Les grandes démocraties sont-elles responsables des origines de la Seconde Guerre mondiale ? Écris ton plan : trois ou quatre parties.",
                    sous="Mets la vidéo en pause, écris ton plan, puis reprends pour comparer."),
        "pl": dict(type="liste", titre="Un plan modèle", items=[
            "Un ordre qu'elles ne voulaient pas garantir", "Un ordre affaibli économiquement après 1929",
            "Un ordre qu'elles refusent de défendre", "Mais l'initiative revient aux régimes militaristes"], x=150, y=140, w=980),
        "pa2": dict(type="pause", t="Rédige le paragraphe « cependant » : pourquoi les démocraties ne sont pas les principales coupables.",
                    sous="Mets la vidéo en pause, écris cinq phrases, puis reprends pour voir un modèle."),
        "par": dict(type="liste", titre="Un paragraphe modèle (écrit pour la vidéo)", items=[
            "Cependant : réticentes, mais pas responsables de la décision de faire la guerre",
            "Le militarisme, un choix délibéré à Berlin, Rome, Tokyo",
            "La misère donne un public aux nazis ; elle n'oblige à aucun pillage",
            "L'apaisement avait des raisons rationnelles", "Donc : les démocraties facilitent l'agression ; les agresseurs choisissent la guerre"], x=110, y=95, w=1060),
        "ccl": dict(type="def", terme="Conclusion", cles=["partie", "réticentes"],
                    t="Oui, en partie : responsables d'un ordre qu'elles ont affaibli et refusé de défendre ; les agresseurs, de la guerre.",
                    etape="Le mot du cours : « réticentes ». Elles auraient pu agir, et ont choisi de ne pas le faire.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}En mille neuf cent dix-neuf, les démocraties bâtissent un ordre libéral sur les principes de Wilson. "
        "Mais les États-Unis n'entrent jamais dans la Société des Nations. Et la Société n'a pas d'armée, et un veto pour chaque membre. "
        "{carte.2}Dans les années trente, elle condamne le Japon en Mandchourie, et rien ne suit. L'Amérique condamne en paroles, avec la note Stimson. "
        "Puis elle s'enferme avec les lois de neutralité, jusqu'au cash and carry de mille neuf cent trente-neuf. "
        "{carte.3}Le Royaume-Uni et la France choisissent l'apaisement, pour six raisons rationnelles, de l'Éthiopie et de la Rhénanie jusqu'à Munich. "
        "{carte.4}Et chaque concession est suivie d'une exigence plus grande, jusqu'à la Pologne, en septembre mille neuf cent trente-neuf.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : la crise à l'épreuve. Question problématisée et analyse de document sur tout le chapitre, avec des modèles.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="DES DÉMOCRATIES RÉTICENTES", branches=[
            dict(t="L'ordre de 1919", items=["Wilson : 3 principes", "les États-Unis n'y entrent pas", "pas d'armée, un veto chacun"]),
            dict(t="L'Amérique", items=["Stimson : des mots", "lois de neutralité 1935-1937", "cash and carry, nov. 1939"]),
            dict(t="L'apaisement", items=["Éthiopie, Rhénanie", "six raisons rationnelles", "Munich, sept. 1938"]),
            dict(t="Les conséquences", items=["Anschluss, Prague", "chaque concession, une exigence plus grande", "1er sept. 1939 : la Pologne"])]),
        "fin": dict(type="mot", t="Prochain épisode : la crise à l'épreuve", g="Épisode 5 · question problématisée et analyse de document", y=270, taille=80),
    }),
]

QUIZ = [
    dict(q="Quels trois principes les Quatorze points de Wilson portent-ils dans la politique étrangère ?",
         r=["Démocratie, droit des peuples à disposer d'eux-mêmes, libre-échange", "Isolement, protection, neutralité",
            "Empire, réarmement, étalon-or", "Communisme, pacifisme, autarcie"], ok=0, voir="wi",
         ex="Le wilsonisme : la base de l'ordre mondial libéral de 1919, doté d'institutions à Paris, Versailles et Genève."),
    dict(q="Laquelle est une faiblesse STRUCTURELLE de la Société des Nations ?",
         r=["Elle n'avait pas d'armée à elle", "Elle était impuissante face au militarisme italien",
            "Le Japon a envahi la Mandchourie", "L'Allemagne a remilitarisé la Rhénanie"], ok=0, voir="str",
         ex="Structurelles : présentes dès 1919 (pas de ratification américaine, les intérêts nationaux d'abord, pas d'armée, un veto pour chaque membre). Les autres réponses sont des événements conjoncturels des années 1930."),
    dict(q="Que se passe-t-il après l'adoption du rapport Lytton par la Société des Nations, en février 1933 ?",
         r=["Le Japon quitte la Société", "Le Japon se retire de Mandchourie", "Les États-Unis envoient des troupes", "Le Royaume-Uni impose un embargo pétrolier"],
         ok=0, voir="mk", ex="Le Japon quitte la Société en mars 1933 : la Société ne peut pas arrêter une grande puissance."),
    dict(q="La note Stimson du 7 janvier 1932 est…",
         r=["une doctrine de non-reconnaissance, pas d'action", "une déclaration de guerre au Japon",
            "un embargo sur tout le commerce avec le Japon", "l'entrée des États-Unis dans la Société des Nations"], ok=0, voir="wa",
         ex="Des mots sans action : le Japon répond en bombardant Shanghai en 1932, et aucune réponse américaine ne suit."),
    dict(q="Comment le Japon a-t-il lu la réponse américaine au naufrage de l'USS Panay (décembre 1937) ?",
         r=["Comme un permis pour de nouvelles agressions", "Comme une déclaration de guerre", "Comme une raison de quitter la Chine", "Comme une invitation à rejoindre la Société"],
         ok=0, voir="pn", ex="Le Japon s'excuse et paie une indemnité — et en conclut que l'Amérique n'agira pas."),
    dict(q="Que permet la loi de neutralité de 1939, le « cash and carry » ?",
         r=["Les démocraties peuvent acheter des armes américaines si elles paient comptant et les transportent sur leurs navires",
            "Les États-Unis peuvent prêter des armes sans paiement", "Des soldats américains peuvent combattre en Europe",
            "L'Allemagne peut acheter des chars américains"], ok=0, voir="cc",
         ex="Elle profite à qui tient la mer, le Royaume-Uni et la France — s'ils ont l'argent."),
    dict(q="Laquelle N'EST PAS une des six raisons de l'apaisement selon le cours ?",
         r=["Une alliance militaire avec l'Allemagne nazie", "Le pacifisme", "Une peur du communisme plus grande que celle du fascisme",
            "La sympathie pour une Allemagne traitée injustement à Versailles (1919)"], ok=0, voir="six",
         ex="Les six : le pacifisme, un empire à surveiller, la sympathie pour l'Allemagne, les problèmes économiques d'abord, l'isolationnisme américain, la peur du communisme."),
    dict(q="Qu'ont accepté Chamberlain et Daladier à Munich, en septembre 1938 ?",
         r=["La cession des Sudètes à l'Allemagne", "L'Anschluss de l'Autriche", "L'occupation de Prague",
            "L'invasion de la Pologne"], ok=0, voir="sl",
         ex="Munich, l'acte qui définit l'apaisement ; en mars 1939, l'Allemagne occupe toute la Tchécoslovaquie : Munich n'avait rien acheté."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 1 (partie II.3, « De grandes démocraties réticentes à défendre l'ordre libéral établi en 1919 »), "
    "tel qu'il est rédigé sur le site, avec ses schémas (pourquoi la Société des Nations a échoué, les marches vers la guerre, points à vérifier) et la fiche de la problématique ; "
    "carte animée du chapitre 1 (site). Hors cours : « la paix pour notre temps ». Les dessins de David Low sont décrits, pas reproduits. "
    "Citations en traduction française : Roosevelt (1936), Chamberlain (1938) ; accords de Munich d'après leur texte français. "
    "Le paragraphe modèle a été écrit pour cette vidéo.",
    "Photographie : Woodrow Wilson, 1919, par Harris & Ewing (Library of Congress, Wikimedia Commons, domaine public).",
    "Dessin : Leonard Raven-Hill, « The Gap in the Bridge », Punch, 10 décembre 1919 (Wikimedia Commons, domaine public).",
    "Photographie : le palais des Nations, Genève, 2014, par Vassil (Wikimedia Commons, CC0).",
    "Photographie : Franklin D. Roosevelt, 1933, par Elias Goldensky (Wikimedia Commons, domaine public).",
    "Photographie : Neville Chamberlain à l'aérodrome de Heston, 30 septembre 1938, photographe officiel du ministère britannique de l'Information (Wikimedia Commons, domaine public).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
