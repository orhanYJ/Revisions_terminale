"""Histoire · chapitre 1 « Le krach de 1929 et ses conséquences » — édition française, épisode 3 :
« Nationalisme économique et réponses politiques » (parties II.1 et II.2 du cours).

Traduction et adaptation de h1_3.py (édition anglaise, gardée intacte), selon outils/serie-dnl/EDITION_FR.md :
mêmes scènes, mêmes identifiants de visuels, mêmes repères, mêmes globes (la carte animée passe d'elle-même en français),
mêmes graphes et données, mêmes images (légendes traduites). Aucune mention de la DNL : histoire-géographie de Terminale.
Vocabulaire repris des champs français du cours (dnl/index.html, CHAPTERS.H1, parties II.1 « Le nationalisme économique »
et II.2 « Les réponses politiques à la crise », fiche Smoot-Hawley, graphique du chômage allemand).
Les deux pauses « essay » deviennent des réponses à une question problématisée (plan, arguments avec exemple, conclusion).
Citation de Melita Maschmann : traduction française fidèle de la phrase citée par le cours (« The Nazis promised to end
unemployment and poverty, and I believed them »). Légende du dessin : traduction du cours (« Je ne suis pas sûr qu'on ait
réussi, mon vieux »). Reste dit « hors du cours » : le pont du Golden Gate (inauguré en 1937, projet local).
Chaîne : outils/serie-philo/generer.py h1f_3 ; sortie dans dnl/serie/.
Type globe, sc = numéros de scènes de la carte H1 dans l'ordre chronologique :
  13 Allemagne la plus exposée · 14 militarisme de trois régimes · 15 Smoot-Hawley · 16 blocs impériaux ·
  18 Mandchourie · 20 doctrine Stimson, Shanghai · 21 Hitler appelé, économie nazie · 22 New Deal ·
  23 Roosevelt renverse la politique · 24 Front populaire
Plan de la série : 1 Le grand krach de 1929 · 2 D'un krach américain à une crise mondiale ·
3 Nationalisme économique et réponses politiques · 4 Les démocraties et l'ordre libéral ·
5 La crise à l'épreuve : question problématisée et analyse de document · 6 Récap.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h1f-3"
NOTION = "Le krach de 1929 et ses conséquences"
NUM = 3
TITRE = "Nationalisme économique et réponses politiques"
SUIVANT = "Épisode 4 · Les démocraties et l'ordre libéral"
PRONONCIATION = {
    "Smoot-Hawley": "Smoute-Hôlé", "Smoot": "Smoute", "Hawley": "Hôlé", "Hoover": "Houveur", "Roosevelt": "Rouzvelt",
    "Dawes": "Dôze", "Stimson": "Stimsonne", "Lamont": "Lamonnte", "Dunning": "Deuning", "Kwantung": "Kouan-toung",
    "Maschmann": "Mache-mann", "NSDAP": "N. S. D. A. P.", "Autobahn": "Ao-to-bâne", "Weimar": "Vaï-mar",
    "Deutsche Bank": "Doïtche Bank", "Import Duties Act": "Immporte Diou-tize Akte",
    "Reciprocal Trade Agreements Act": "Ri-ci-pro-keul Trède A-gri-mennts Akte",
    "Civilian Conservation Corps": "Ci-vi-lieune Konn-seur-vé-cheune Kor",
    "Tennessee Valley Authority": "Tè-nè-ssi Va-li O-tho-ri-ti",
    "Social Security Act": "Sô-cheul Si-kiou-ri-ti Akte",
    "Works Progress Administration": "Oueurkse Pro-grèss Ad-mi-nis-tré-cheune",
    "Golden Gate": "Gol-dène Guéte", "Reed": "Ride", "Wall Street": "Wol-Strite",
    "Relief": "Ri-life", "Recovery": "Ri-keu-veu-ri", "Reform": "Ri-forme",
}

# dossier documentaire, document 2 (schéma h1germany) : chômage chez les travailleurs assurés, en %
CHOMAGE = [(1928, 8.6), (1929, 13.3), (1930, 22.7), (1931, 34.3), (1932, 43.8), (1933, 36.2)]
# vote nazi (idée 2 de II.2) : 1928, septembre 1930, juillet 1932, novembre 1932
VOTE = [(1928.4, 2.6), (1930.7, 18.3), (1932.55, 37.3), (1932.85, 33.1)]


def pc(v):
    """Pourcentage à la française : 8.6 → « 8,6 % » (espace insécable)."""
    return f"{v}".replace(".", ",") + " %"


def barres_ans(donnees, c="sa", c_pic="ca", pic=1932, ep=34, retrait=2.1):
    """Barres verticales (droites épaisses) sur un axe en années ; retrait = demi-épaisseur en unités de l'axe y."""
    el = []
    for an, v in donnees:
        el.append(dict(type="droite", pts=[[an, retrait], [an, max(retrait + .1, v - retrait)]], c=c_pic if an == pic else c,
                       ep=ep, dur=.8, lbl=pc(v), lp=[an, v + 4.5]))
    return el


SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}Mille neuf cent trente. Le krach de Wall Street est devenu une dépression mondiale. Tous les gouvernements font face à la même question.",
        "{q1}Quand l'économie mondiale s'effondre, que faire ? Fermer ses portes pour protéger les siens… "
        "ou les ouvrir, et tenter de reconstruire ensemble le marché mondial ?",
        "{-q1}{q2}Et pourquoi la même crise a-t-elle produit un New Deal en Amérique, "
        "un Front populaire en France… et Hitler en Allemagne ?",
        "{-q2}Voici l'épisode trois de notre série sur le premier chapitre. {-g0}{plan}{plan.1}L'épisode un racontait le grand krach, "
        "{plan.2}l'épisode deux, comment un krach américain devient une crise mondiale. {plan.3}Aujourd'hui : le nationalisme économique, "
        "et les réponses politiques à la crise. {plan.4}La prochaine fois, les démocraties et l'ordre libéral. {plan.5}Puis l'épreuve : "
        "la question problématisée et l'analyse de document, {plan.6}et un récap final.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[12]),
        "q1": dict(type="question", t="Fermer les portes… ou les ouvrir ?", bande=True),
        "q2": dict(type="question", t="Une crise : un New Deal, un Front populaire… et Hitler. Pourquoi ?", bande=True),
        "plan": dict(type="liste", titre="Le krach de 1929 et ses conséquences, en six épisodes", items=[
            "Le grand krach de 1929 (partie I.1)", "D'un krach américain à une crise mondiale (I.2–I.3)",
            "Nationalisme économique et réponses politiques (II.1–II.2)", "Les démocraties et l'ordre libéral (II.3)",
            "La crise à l'épreuve : question problématisée et analyse de document", "Récap"], x=170, y=110, w=940),
        "titre": dict(type="titre", sur="Histoire · Chapitre 1 · Épisode 3", t="Nationalisme économique et réponses politiques",
                      sous="1930 – 1936 · droits de douane · blocs fermés · nazisme · New Deal · Front populaire"),
    }),

    # ================================================================ la chronologie sur la carte (1)
    dict(id="carte1", chap="Sur la carte · 1930 – 1932", fond="nuit", humeur="tension",
         retenir="1930-1932 : l'Allemagne la plus exposée · militarisme à Berlin, Rome, Tokyo · 17 juin 1930 : tarif Smoot-Hawley · 1931-1932 : blocs impériaux fermés · 18 sept. 1931 : la Mandchourie.",
         beats=[
        "{g1}Suivons d'abord l'histoire sur la carte. {g1.1}De mille neuf cent trente à mille neuf cent trente-deux, regarde l'Allemagne. "
        "Son industrie vivait du crédit américain. Quand les prêts sont rappelés, la production chute de quarante pour cent. "
        "Le chômage explose. Et dans les mêmes années, le vote nazi grimpe.",
        "{g1.2}Au fil de la décennie, trois régimes prennent la même route : l'Allemagne de Hitler, l'Italie de Mussolini, et le Japon. "
        "Une armée puissante. Des militaires aux commandes. Une politique étrangère agressive. C'est le {!militarisme}militarisme.",
        "{g1.3}Les États-Unis, maintenant. Le dix-sept juin mille neuf cent trente, le président Hoover signe le tarif Smoot-Hawley. "
        "Les droits de douane montent sur plus de vingt mille produits importés. Et le Canada, le plus proche partenaire de l'Amérique, riposte.",
        "{g1.4}En trente et un et trente-deux, les grands empires se referment. Le Royaume-Uni commerce avec ses dominions. "
        "La France fixe des quotas. L'Allemagne vise l'autarcie. Entre vingt-neuf et trente-quatre, "
        "le commerce mondial perd environ deux tiers de sa valeur.",
        "{g1.5}Et en Asie, le dix-huit septembre mille neuf cent trente et un, l'armée japonaise envahit la Mandchourie. "
        "La Société des Nations condamne… et ne peut rien faire de plus.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[13, 14, 15, 16, 18]),
    }),

    # ================================================================ la chronologie sur la carte (2)
    dict(id="carte2", chap="Sur la carte · 1932 – 1936", fond="nuit", humeur="tension",
         retenir="Janv. 1932 : note Stimson, Shanghai bombardée · janv. 1933 : Hitler chancelier · 1933-1935 : le New Deal · 1933-1934 : sortie de l'or, RTAA, URSS reconnue · 1934-1936 : le 6 février, puis le Front populaire.",
         beats=[
        "{g2}{g2.1}Janvier mille neuf cent trente-deux. Le secrétaire d'État américain, Henry Stimson, fait une annonce : "
        "les États-Unis ne reconnaîtront aucune conquête par la force en Chine. La réponse du Japon ? Il bombarde Shanghai. Et Washington ne fait rien.",
        "{g2.2}Janvier mille neuf cent trente-trois, Berlin. Les conservateurs font entrer Adolf Hitler à la chancellerie. Son régime va mettre fin au chômage… "
        "en préparant la guerre.",
        "{g2.3}Mars mille neuf cent trente-trois, Washington. Franklin Roosevelt entre en fonctions, et lance le New Deal. Secourir. Relancer. Réformer.",
        "{g2.4}En trente-trois et trente-quatre, Roosevelt prend le contre-pied de Hoover. Il détache le dollar de l'or. "
        "À partir de trente-quatre, il signe des accords commerciaux, pays par pays. Et il reconnaît l'Union soviétique.",
        "{g2.5}Et la France. Le six février mille neuf cent trente-quatre, les ligues d'extrême droite manifestent violemment à Paris. La peur du fascisme unit la gauche. "
        "En mille neuf cent trente-six, le Front populaire gagne les élections, et Léon Blum devient président du Conseil.",
        "{-g2}{dates}Voici les dates à noter. Mets la vidéo en pause si tu en as besoin.",
        ("P", 10.0),
    ], vis={
        "g2": dict(type="globe", code="H1", sc=[20, 21, 22, 23, 24]),
        "dates": dict(type="liste", titre="Les dates à connaître", items=[
            "17 juin 1930 · tarif Smoot-Hawley (Canada : mai 1930)", "1931 · quotas français · 18 sept. : Mandchourie",
            "1932 · Import Duties Act · Ottawa · note Stimson", "1933 · Hitler (janv.) · cent jours · sortie de l'or · URSS",
            "1934 · émeutes du 6 février · RTAA · 1935 : second New Deal", "Juin 1936 · Front populaire, accords de Matignon"], x=130, y=90, w=1020),
    }),

    # ================================================================ II.1, idée 1 : l'internationalisme indépendant
    dict(id="hoover", chap="II.1 · L'internationalisme indépendant", fond="aube", humeur="calme",
         retenir="L'« internationalisme indépendant » de Hoover : engagé dans l'économie mondiale (exportations, investissements), absent de ses institutions politiques (ni alliance, ni SDN). Pas de l'isolationnisme. Après le krach : la survie intérieure.",
         beats=[
        "{q3}Reprenons maintenant le cours, idée par idée. Deuxième partie, section un : le {!nationalisme économique}nationalisme économique. "
        "Et pour le comprendre, on part d'avant le krach.",
        "{-q3}{def1}Sous le président Hoover, l'Amérique pratique ce que le cours appelle un {!internationalisme indépendant}internationalisme indépendant. "
        "L'étiquette compte : ce n'est pas de l'isolationnisme.",
        "{-def1}{cmp1}{cmp1.g}D'un côté, l'Amérique est pleinement engagée dans l'économie mondiale : exportations, investissements à l'étranger, "
        "leadership économique et technologique. {cmp1.d}De l'autre, elle est délibérément absente de ses institutions politiques : "
        "aucune alliance, et elle reste hors de la Société des Nations.",
        "{-cmp1}{ex1}L'exemple, tu l'as vu dans l'épisode deux. Avec le plan Dawes, les banques américaines prêtent à l'Allemagne, "
        "et les entreprises américaines investissent partout en Europe. Mais Washington ne signe aucune alliance, et ne rejoint aucun organe de sécurité collective. "
        "{ex1.1}Alors quand l'argent rentre au pays, en mille neuf cent trente, rien de politique ne reste derrière.",
        "{-ex1}{surv}Après le krach, la priorité devient la {!survie intérieure}survie intérieure. Les États-Unis coupent la plupart de leurs "
        "engagements internationaux, et ne gardent qu'un minimum d'échanges.",
    ], vis={
        "q3": dict(type="mot", t="Le nationalisme économique", g="Partie II.1 du cours", y=260, taille=80),
        "def1": dict(type="def", cles=["engagée", "absente"], terme="L'internationalisme indépendant (Hoover, années 1920)",
                     t="Pleinement engagée dans l'économie mondiale, l'Amérique est délibérément absente de ses institutions politiques.",
                     etape="Pas de l'isolationnisme : le commerce et l'investissement, oui ; les alliances et la SDN, non.", x=170, y=200, w=940),
        "cmp1": dict(type="cols", g="Engagée", gq="exportations · investissements à l'étranger · leadership économique et technologique",
                     d="Absente", dq="aucune alliance politique ou militaire · hors de la Société des Nations", vs="+"),
        "ex1": dict(type="note", terme="Exemple · les prêts du plan Dawes", cles=["prêtent", "investissent", "alliance"],
                    t="Les banques américaines prêtent à l'Allemagne, les entreprises américaines investissent partout en Europe… mais aucune alliance, aucune sécurité collective.",
                    etape="1930 : l'argent rentre au pays, et rien de politique ne reste derrière.", x=170, y=200, w=940),
        "surv": dict(type="mot", t="La survie intérieure", g="après le krach : engagements coupés, un minimum d'échanges", y=260, taille=86),
    }),

    # ================================================================ II.1, idée 2 : Smoot-Hawley
    dict(id="smoot", chap="II.1 · Le tarif Smoot-Hawley", fond="nuit", humeur="tension",
         retenir="Tarif Smoot-Hawley, signé par Hoover le 17 juin 1930 : droits relevés sur plus de 20 000 produits, 2e niveau le plus élevé de l'histoire américaine. Idéologie : le nationalisme économique. Contre lui : 1 028 économistes, Henry Ford, Thomas Lamont, 23 pays.",
         beats=[
        "{mot1}Deuxième idée. Comment les États-Unis répondent-ils à la crise ? Par le {!protectionnisme}protectionnisme. "
        "Son nom : le tarif Smoot-Hawley. Le cours propose d'en dresser la fiche, en six cases. Remplissons-les.",
        "{-mot1}{fiche}{fiche.1}Première case : de quoi s'agit-il ? D'une loi douanière, signée par Hoover le dix-sept juin mille neuf cent trente. "
        "Elle relève les droits sur plus de vingt mille produits importés. C'est le deuxième niveau le plus élevé de l'histoire américaine.",
        "{fiche.2}Quelle idéologie porte-t-elle ? Le nationalisme économique. Se redresser en fermant la porte à la concurrence étrangère… plutôt qu'en coopérant.",
        "{fiche.3}Qui l'a portée ? Le sénateur Reed Smoot et le représentant Willis Hawley, tous deux républicains. Au départ, c'est une promesse faite aux agriculteurs, "
        "pendant la campagne de mille neuf cent vingt-huit. Puis la loi grossit, par échange de votes au Congrès. Soutiens mon tarif, et je soutiendrai le tien. "
        "À la fin, toutes les industries sont protégées.",
        "{fiche.4}Qui s'y oppose ? Mille vingt-huit économistes signent une pétition, et supplient Hoover d'y mettre son veto. "
        "Henry Ford parle d'une stupidité économique. Et le banquier Thomas Lamont dit s'être presque mis à genoux pour l'arrêter. "
        "{fiche.5}Ses objectifs ? Protéger l'agriculture et l'industrie. Soutenir l'emploi. Dégager des recettes douanières. Bref, un pari sur le marché intérieur. "
        "Et ses conséquences ? On y vient dans un instant.",
        "{-fiche}{ex2}Hoover signe quand même, sous la pression de son parti et des milieux d'affaires. "
        "{ex2.1}L'exemple à citer : vingt-trois pays avaient déposé des protestations officielles avant même le vote de la loi. "
        "{ex2.2}Et deux ans plus tard, aux élections de trente-deux, Smoot et Hawley perdent tous deux leur siège. "
        "Ils avaient promis la prospérité aux électeurs. Les électeurs ont eu l'inverse.",
    ], vis={
        "mot1": dict(type="mot", t="20 000 produits", g="tarif Smoot-Hawley · signé le 17 juin 1930", y=250, taille=100),
        "fiche": dict(type="liste", titre="Fiche · le tarif Smoot-Hawley (juin 1930)",
                      cles=["droits", "nationalisme", "républicains", "économistes", "marché"], items=[
            "Quoi ? Des droits relevés sur plus de 20 000 produits, 2e niveau le plus élevé de l'histoire américaine",
            "Idéologie : le nationalisme économique, fermer la porte à la concurrence étrangère",
            "Portée par Smoot et Hawley (républicains), d'après une promesse de 1928 aux agriculteurs",
            "Contre elle : 1 028 économistes, Henry Ford (« une stupidité économique »), Thomas Lamont",
            "Objectifs : protéger l'agriculture, l'industrie et l'emploi ; parier sur le marché intérieur"], x=130, y=55, w=1020),
        "ex2": dict(type="liste", titre="Une loi qui échoue avant même de commencer", cles=["protestations", "perdent"], items=[
            "23 pays déposent des protestations avant le vote", "1932 : Smoot et Hawley perdent tous deux leur siège"], x=170, y=170, w=940),
    }),

    # ================================================================ II.1, idée 3 : représailles et blocs
    dict(id="blocs", chap="II.1 · Représailles et blocs fermés", fond="nuit", humeur="tension",
         retenir="Représailles : le Canada (mai 1930, 30 % des exportations américaines vers lui), les quotas français (1931), l'Import Duties Act britannique (10 %, 1932), la « préférence impériale » d'Ottawa (1932), l'autarcie allemande. Commerce mondial −66 % en valeur, 1929-1934. Le libre-échange a disparu.",
         beats=[
        "{q5}Troisième idée. Est-ce que ça marche ? Le cours répond à sa propre question par un dessin, et une légende :{-q5}",
        ("C", "Je ne suis pas sûr qu'on ait réussi, mon vieux.", "c_pal"),
        "{-c_pal}{chaine}Pourquoi ? Parce que le protectionnisme se propage par {!représailles}représailles. {chaine.1}Prends le Canada, le premier partenaire commercial des États-Unis. "
        "Il riposte avant même la signature de la loi : en mai mille neuf cent trente, avec le budget Dunning. Ses nouveaux droits frappent environ trente pour cent des exportations américaines vers le Canada. "
        "Et il se tourne plutôt vers l'Empire britannique. {chaine.2}La France instaure des quotas d'importation en mille neuf cent trente et un. "
        "{chaine.3}Le Royaume-Uni vote l'Import Duties Act en mille neuf cent trente-deux : un tarif général de dix pour cent sur la plupart des importations. "
        "{chaine.4}Tous deux épargnent leur empire. Et l'Allemagne bâtit un système d'autarcie.",
        "{-chaine}{def2}Voici le schéma à comprendre. Les grandes puissances commerciales ne ferment pas simplement leurs portes. "
        "Elles redirigent leurs échanges vers l'intérieur, vers des colonies qui ne peuvent pas refuser. "
        "{def2.1}L'économie mondiale devient alors {!un ensemble de blocs impériaux rivaux}un ensemble de blocs impériaux rivaux, au lieu d'un marché unique.",
        "{-def2}{gc}Le résultat ? {gc.1}Le commerce mondial en mille neuf cent vingt-neuf… {gc.2}et en mille neuf cent trente-quatre. Environ deux tiers de sa valeur en moins.",
        "{-gc}{ott}L'exemple : en mille neuf cent trente-deux, la conférence d'Ottawa officialise la {!préférence impériale}préférence impériale. "
        "Le Royaume-Uni et ses dominions baissent leurs droits entre eux, et les gardent élevés pour tous les autres. "
        "{ott.1}Le libre-échange, pilier de l'ordre libéral de mille neuf cent dix-neuf, a disparu.",
        "{-ott}{jug}Alors, le tarif a-t-il causé la Dépression ? Beaucoup d'historiens disent qu'il l'a aggravée. "
        "Mais le jugement le plus juste, celui à écrire, est celui-ci : il a transformé un ralentissement en guerre commerciale.",
    ], vis={
        "q5": dict(type="question", t="Est-ce que ça marche ?"),
        "c_pal": dict(type="cit", a="Légende d'un dessin de presse", o="Le cours, sur le tarif Smoot-Hawley", x=200, y=230, w=880),
        "chaine": dict(type="liste", titre="Le protectionnisme se propage par représailles", cles=["Canada", "quotas", "Royaume-Uni", "autarcie"], items=[
            "Le Canada frappe le premier (budget Dunning, mai 1930) : 30 % des exportations américaines vers lui", "France : quotas d'importation (1931)",
            "Royaume-Uni : Import Duties Act, 10 % sur la plupart des importations (1932)", "Empires épargnés · Allemagne : autarcie"], x=150, y=130, w=980),
        "def2": dict(type="def", cles=["intérieur", "colonies"], terme="Les blocs impériaux fermés",
                     t="Des échanges redirigés vers l'intérieur, vers des colonies qui ne peuvent pas refuser.",
                     etape="Un ensemble de blocs impériaux rivaux, plutôt qu'un marché mondial unique", x=170, y=200, w=940),
        "gc": dict(type="graphe", titre="Le commerce mondial en valeur (1929 = 100 ; chiffre du cours : environ −66 %)", x=340, y=110, w=600, h=520,
                   ax=dict(x=[1927.5, 1935.5], y=[0, 120], gx=[], gy=[50, 100], lx="", ly="indice"),
                   el=[dict(type="droite", pts=[[1929, 7], [1929, 93]], c="sa", ep=60, dur=1.0, lbl="1929 : 100", lp=[1929, 108]),
                       dict(type="droite", pts=[[1934, 7], [1934, 27]], c="ca", ep=60, dur=1.0, lbl="1934 : environ 34", lp=[1934, 45])]),
        "ott": dict(type="note", terme="Exemple · Ottawa, 1932", cles=["entre", "autres"],
                    t="La « préférence impériale » : droits bas entre le Royaume-Uni et ses dominions, droits élevés pour tous les autres.",
                    etape="Le libre-échange, pilier de l'ordre libéral de 1919, a disparu.", x=170, y=200, w=940),
        "jug": dict(type="mot", t="Un ralentissement → une guerre commerciale", g="le jugement nuancé sur le tarif Smoot-Hawley", y=260, taille=64),
    }),

    # ================================================================ II.1, idée 4 : Roosevelt renverse la politique
    dict(id="fdr", chap="II.1 · Roosevelt renverse la politique", fond="aube", humeur="lumiere",
         retenir="Roosevelt : sortie de l'or en 1933, Reciprocal Trade Agreements Act (RTAA, 1934), une vingtaine d'accords en 1939. Aucun avec l'Allemagne, l'Italie ou le Japon : les chefs fascistes les rejettent.",
         beats=[
        "{photo}Quatrième idée. Le quatre mars mille neuf cent trente-trois. Dans la même voiture, en route vers le Capitole, deux hommes. "
        "Le sortant, Herbert Hoover. Et le nouveau, Franklin Roosevelt. Deux hommes, deux politiques.",
        "Le cours associe le tarif à une seconde case : la sortie de l'étalon-or. {-photo}{rev}{rev.1}En mille neuf cent trente-trois, "
        "Roosevelt détache les États-Unis de l'or. Le dollar peut baisser, et les prix remonter. "
        "{rev.2}En trente-quatre vient le {!Reciprocal Trade Agreements Act}Reciprocal Trade Agreements Act, la loi sur les accords commerciaux réciproques. "
        "Elle lui permet de négocier des baisses de droits, pays par pays. "
        "{rev.3}Le but ? Reconstruire les relations commerciales, et libéraliser les marchés mondiaux.",
        "{-rev}{lim}Mais le monde a déjà changé. {lim.1}En trente-neuf, les États-Unis ont signé des accords réciproques "
        "avec une vingtaine de pays. {lim.2}Aucun avec l'Allemagne, l'Italie ou le Japon. Hitler et Mussolini n'en veulent pas. "
        "Leurs économies sont organisées pour l'autarcie et la guerre, pas pour l'échange.",
    ], vis={
        "photo": dict(type="tableau", img="h1-hoover-fdr", de=[1.0, .5, .25], a=[1.15, .55, .2],
                      legende="Herbert Hoover et Franklin D. Roosevelt en route vers l'investiture, 4 mars 1933 (Architect of the Capitol, domaine public)"),
        "rev": dict(type="liste", titre="Roosevelt renverse la politique", cles=["or", "droits", "libéraliser"], items=[
            "1933 : sortie de l'étalon-or, le dollar baisse, les prix remontent",
            "1934 : le Reciprocal Trade Agreements Act (RTAA), baisses de droits pays par pays",
            "But : reconstruire le commerce, libéraliser les marchés mondiaux"], x=170, y=140, w=940),
        "lim": dict(type="cols", g="En 1939", gq="des accords réciproques avec une vingtaine de pays", d="Mais",
                    dq="aucun avec l'Allemagne, l'Italie ou le Japon : l'autarcie et la guerre, pas l'échange", vs="≠"),
    }),

    # ================================================================ à toi : question problématisée sur le tarif
    dict(id="essai", chap="À toi · une question problématisée sur le tarif", fond="aube", humeur="calme",
         retenir="Le tarif Smoot-Hawley : inefficace sur ses propres objectifs (prix agricoles, emploi, sièges perdus), néfaste (guerre commerciale, −66 %, blocs), mais pas la cause de la Dépression. Sa vraie portée : il détruit le libre-échange, pilier de 1919.",
         beats=[
        "{ex3}À toi. Voici la question qui clôt le cours sur le tarif Smoot-Hawley : "
        "{!dans quelle mesure}dans quelle mesure le tarif douanier de mille neuf cent trente a-t-il été une réponse efficace aux défis de la Grande Dépression ?",
        "Un conseil. Mesure l'efficacité à l'aune des objectifs de la loi elle-même : protéger les agriculteurs et l'industrie américaine. "
        "Pose ta problématique, trouve trois arguments, puis fais une pause.",
        "{-ex3}{pa1}",
        ("P", 4.0),
        "{-pa1}{rep1}Voici un plan possible. {rep1.1}Premièrement : la loi échoue même sur ses propres critères. Les prix agricoles continuent de baisser. "
        "Le chômage continue de monter. Et Smoot et Hawley perdent leur siège en trente-deux. Cet échec était annoncé, pas découvert après coup : "
        "souviens-toi des mille vingt-huit économistes, et des vingt-trois pays. "
        "{rep1.2}Deuxièmement : elle déclenche une guerre commerciale. Le Canada, les quotas français, l'Import Duties Act, l'autarcie allemande. "
        "Et le commerce mondial perd environ deux tiers de sa valeur. "
        "{rep1.3}Troisièmement, une nuance. Elle n'a pas causé la Dépression, qui commence avec le krach et les faillites bancaires. "
        "Et le revirement arrive trop tard : quand viennent les accords commerciaux de trente-quatre, Hitler et Mussolini n'en veulent pas.",
        "{rep1.4}La conclusion ? Inefficace sur ses propres objectifs. Néfaste par ses conséquences. Mais pas à l'origine de la Dépression. "
        "Sa vraie portée est politique : elle a détruit le libre-échange, pilier de l'ordre libéral de mille neuf cent dix-neuf.",
    ], vis={
        "ex3": dict(type="exo", niveau="essay", titre="Dans quelle mesure le tarif douanier de 1930 a-t-il été une réponse efficace aux défis de la Grande Dépression ?",
                    src="Le cours, question finale sur le tarif Smoot-Hawley", enonce=["Mesure « efficace » à l'aune des objectifs de la loi",
                                                                                     "Une problématique, trois arguments, une conclusion"]),
        "pa1": dict(type="pause", t="Trouve trois arguments, chacun avec un exemple précis, et une conclusion.",
                    sous="Mets la vidéo en pause, écris ton plan, puis reprends pour voir un modèle."),
        "rep1": dict(type="liste", titre="Un plan possible", cles=["critères", "guerre", "causé", "politique"], items=[
            "I. Elle échoue sur ses propres critères : prix agricoles, emploi, sièges perdus en 1932",
            "II. Elle déclenche une guerre commerciale : Canada, quotas, Import Duties Act, −66 %",
            "III. Mais elle n'a pas causé la Dépression, et le RTAA (1934) arrive trop tard",
            "Conclusion : inefficace, néfaste, et politique : la fin du libre-échange"], x=130, y=120, w=1020),
    }),

    # ================================================================ II.2, idée 1 : l'Allemagne, la plus exposée
    dict(id="allemagne", chap="II.2 · L'Allemagne, la plus exposée", fond="guerre", humeur="tension",
         retenir="Allemagne : industrie dépendante du crédit américain, production −40 %, chômage des travailleurs assurés de 8,6 % (1928) à 43,8 % (1932). Les réparations : aucune issue. Les ouvriers d'abord, puis les classes moyennes.",
         beats=[
        "{q4}Deuxième section : les {!réponses politiques}réponses politiques à la crise. Et d'abord, le pays le plus exposé… et celui qui cède.",
        "{-q4}{cause}{cause.1}L'industrie allemande dépendait du crédit américain. Quand les prêts sont rappelés, elle est frappée la première, et le plus durement. "
        "{cause.2}La production manufacturière chute de quarante pour cent. Les prix s'effondrent. "
        "{cause.3}Et l'Allemagne doit encore des réparations à l'Europe, et des remboursements aux États-Unis. Elle ne peut donc ni emprunter, ni dépenser pour s'en sortir.",
        "{-cause}{gch}Voici le graphique du dossier documentaire, document deux : le chômage chez les travailleurs assurés. "
        "{gch.1}Huit virgule six pour cent en vingt-huit. {gch.2}Treize virgule trois en vingt-neuf. "
        "{gch.3}Vingt-deux virgule sept en trente. {gch.4}Trente-quatre virgule trois en trente et un. "
        "{gch.5}Et en trente-deux, le sommet : quarante-trois virgule huit pour cent. "
        "{gch.6}En trente-trois, il redescend à trente-six virgule deux.",
        "{gch.7}Attention quand tu le cites. Ces chiffres ne comptent que les travailleurs assurés. Sur l'ensemble de la population active, le taux est plus bas : "
        "environ trente pour cent au sommet. Cite donc la source quand tu utilises le chiffre.",
        "{-gch}{arb}{soc}Qui est touché ? {soc.1}Le prolétariat d'abord. Les ouvriers perdent leur emploi, leur revenu, leur nourriture, leur logement. "
        "{soc.2}Puis une partie des classes moyennes. {soc.3}Marches de la faim, soupes populaires et manifestations deviennent des scènes ordinaires. "
        "Pense aux soupes populaires de Hanovre, en trente-deux. {soc.4}Et la perte d'espoir nourrit la protestation. "
        "Comme le dit le cours : la protestation trouve un parti.",
        "{-soc}{-arb}{masch}Melita Maschmann était adolescente à l'époque. Elle se souvient des adultes qui parlaient de six millions de chômeurs… "
        "et qui accusaient les réparations, non la crise mondiale.",
    ], vis={
        "q4": dict(type="mot", t="Les réponses politiques", g="Partie II.2 du cours · les réponses à la crise", y=260, taille=86),
        "cause": dict(type="liste", titre="Pourquoi l'Allemagne cède", cles=["crédit", "production", "réparations"], items=[
            "Une industrie dépendante du crédit américain : les prêts rappelés", "Production manufacturière −40 %, prix effondrés",
            "Réparations et remboursements : ni emprunter ni dépenser"], x=170, y=140, w=940),
        "gch": dict(type="graphe", titre="Chômage en Allemagne chez les travailleurs assurés, en % (dossier documentaire, document 2)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1927.4, 1933.6], y=[0, 52], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50], lx="", ly="%"),
                    el=barres_ans(CHOMAGE) + [dict(type="texte", x=1929.6, y=46, t="travailleurs assurés seulement", c="iv")]),
        "arb": dict(type="tableau", img="h1-arbeitsamt-1932", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .6, .55],
                    legende="Chômeurs devant l'office de l'emploi de Berlin-Nord-Est, 4 mai 1932 (Bundesarchiv, Bild 146-1976-033-23, Seiler, CC BY-SA 3.0 de)"),
        "soc": dict(type="liste", titre="Qui est touché ?", cles=["prolétariat", "classes", "soupes", "parti"], items=[
            "Le prolétariat d'abord : emploi, revenu, nourriture, logement", "Puis une partie des classes moyennes",
            "Marches de la faim, soupes populaires (Hanovre, 1932)", "Perte d'espoir → protestation → un parti"], x=170, y=130, w=940),
        "masch": dict(type="note", terme="Exemple · Melita Maschmann (dossier documentaire)", cles=["millions", "réparations"],
                      t="Les adultes parlaient de « six millions de chômeurs »… et accusaient les réparations, non la crise mondiale.",
                      etape="Une ancienne membre des Jeunesses hitlériennes, mémoires de 1963", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 2 : jamais majoritaires
    dict(id="nazis", chap="II.2 · Jamais majoritaires, mais on les laisse entrer", fond="guerre", humeur="tension",
         retenir="Le vote nazi suit le chômage : 2,6 % (1928), 18,3 % (1930), 37,3 % (juillet 1932), 33,1 % (nov. 1932). Jamais la majorité : Hitler est nommé en janvier 1933 par des conservateurs, par peur du communisme. La crise crée le public ; un calcul ouvre la porte.",
         beats=[
        "{m_ns}Deuxième idée. Le parti nazi, le NSDAP, se nourrit de ce mécontentement. {-m_ns}{nsdap}{nsdap.1}Il accuse la faiblesse de la jeune République de Weimar. "
        "{nsdap.2}Il offre des solutions simples à des problèmes complexes. {nsdap.3}Et il s'adresse directement aux chômeurs, même aux ouvriers communistes. "
        "Un slogan de mille neuf cent trente-trois promet : travail, liberté, pain.",
        "Melita Maschmann encore, dans ses mémoires :{-nsdap}",
        ("C", "Les nazis promettaient de mettre fin au chômage et à la pauvreté, et je les ai crus.", "c_masch"),
        "{-c_masch}{gv}Regarde maintenant deux courbes sur le même graphique. {gv.1}Le chômage. {gv.2}Et le vote nazi. "
        "Deux virgule six pour cent en vingt-huit. Dix-huit virgule trois en trente. "
        "Trente-sept virgule trois en juillet trente-deux. Le vote suit la courbe presque exactement. "
        "{gv.3}Puis, en novembre trente-deux, il retombe, à trente-trois virgule un pour cent.",
        "{-gv}{maj}Retiens donc ceci : les nazis n'ont jamais obtenu la majorité. Jamais plus de la moitié des voix.",
        "{-maj}{porte}Alors, qu'est-ce qui les porte au pouvoir ? {porte.1}La peur. La peur du communisme, chez les classes moyennes et les partis du centre. "
        "Ils préfèrent travailler avec les nazis, plutôt que risquer une révolution venue de la gauche. "
        "{porte.2}Et en janvier mille neuf cent trente-trois, Hitler est nommé chancelier, par des conservateurs qui croient pouvoir l'utiliser.",
        "{-porte}{dist}Voici une distinction très utile dans une composition. {dist.g}La crise a créé le public. "
        "{dist.d}Mais c'est un calcul politique qui a ouvert la porte.",
    ], vis={
        "m_ns": dict(type="mot", t="Le NSDAP", g="le parti nazi se nourrit du mécontentement", y=260, taille=96),
        "nsdap": dict(type="liste", titre="Comment le NSDAP exploite la crise", cles=["Weimar", "simples", "chômeurs"], items=[
            "Il accuse la faiblesse de la République de Weimar", "Des solutions simples à des problèmes complexes",
            "Il s'adresse aux chômeurs, même communistes : « Travail ! Liberté ! Pain ! » (1933)"], x=170, y=140, w=940),
        "c_masch": dict(type="cit", a="Melita Maschmann", o="mémoires, 1963 (dossier documentaire, document 5)", x=200, y=230, w=880),
        "gv": dict(type="graphe", titre="Chômage (travailleurs assurés) et vote nazi, en % (cours)", x=300, y=110, w=680, h=520,
                   ax=dict(x=[1927.6, 1933.4], y=[0, 50], gx=[1928, 1929, 1930, 1931, 1932, 1933], gy=[10, 20, 30, 40, 50], lx="", ly="%"),
                   el=[dict(type="courbe", pts=[list(p) for p in CHOMAGE], c="sa", lbl="chômage", lp=[1929.0, 22], dur=1.8),
                       dict(type="courbe", pts=[list(p) for p in VOTE[:3]], c="ca", lbl="vote nazi", lp=[1930.6, 7], dur=1.8),
                       dict(type="courbe", pts=[list(p) for p in VOTE[2:]], c="ca", lbl="nov. 1932 : 33,1 %", lp=[1932.6, 18], dur=.8)]),
        "maj": dict(type="mot", t="Jamais la majorité", g="le vote nazi n'a jamais dépassé 50 %", y=260, taille=96),
        "porte": dict(type="liste", titre="Laissés entrer, pas élus", cles=["peur", "conservateurs"], items=[
            "La peur du communisme : classes moyennes et partis du centre se rangent aux côtés des nazis",
            "Janvier 1933 : Hitler nommé par des conservateurs qui croient pouvoir l'utiliser"], x=170, y=160, w=940),
        "dist": dict(type="cols", g="La crise", gq="a créé le public", d="Un calcul politique", dq="a ouvert la porte", vs="→"),
    }),

    # ================================================================ II.2, idée 3 : la politique économique nazie
    dict(id="econazie", chap="II.2 · L'économie nazie", fond="guerre", humeur="tension",
         retenir="L'économie nazie. Objectifs : stabilité, plein emploi, autarcie. Moyens : syndicats interdits, salaires gelés, temps de travail allongé · droits de douane · grands travaux (l'Autobahn) · réarmement malgré Versailles · privatisations · pillage et spoliation des Juifs. Chômage : 6 millions (1933) → moins d'1 million (1937).",
         beats=[
        "{buts}Troisième idée : la politique économique nazie. {buts.1}Trois objectifs : la stabilité économique, {buts.2}la fin du chômage, {buts.3}et l'autarcie.",
        "{-buts}{moy}Et les moyens, dans l'ordre du cours. {moy.1}La contrainte : syndicats interdits, salaires gelés, temps de travail allongé. "
        "{moy.2}Des droits de douane sur les importations. {moy.3}L'investissement public, dans la continuité de Weimar : écoles, hôpitaux, routes. Et l'Autobahn, les autoroutes. "
        "{moy.4}Le réarmement, alors que le traité de Versailles l'interdit. "
        "{moy.5}Des privatisations massives : des banques comme la Deutsche Bank, les chemins de fer, les chantiers navals. "
        "{moy.6}Et les deux derniers points ne relèvent pas de l'économie. Ce sont des crimes : le pillage des nations conquises, "
        "et la spoliation des biens juifs.",
        "{-moy}{six}L'exemple. Le réarmement absorbe les chômeurs, et il satisfait l'industrie. "
        "Le chômage enregistré tombe de six millions en trente-trois… à moins d'un million en trente-sept.",
        "{-six}{lec}Lis donc la liste d'un seul tenant. {!un régime qui résout le chômage en préparant la guerre}Un régime qui résout le chômage "
        "en préparant la guerre, et qui le paie par le vol. {lec.1}Une reprise qui n'a de sens que si la guerre suit.",
    ], vis={
        "buts": dict(type="liste", titre="Trois objectifs", cles=["stabilité", "chômage", "autarcie"], items=[
            "La stabilité économique", "La fin du chômage", "L'autarcie"], x=170, y=160, w=940),
        "moy": dict(type="liste", titre="Les moyens (dans l'ordre du cours)", cles=["interdits", "douane", "Autobahn", "réarmement", "privatisations", "crime"], items=[
            "Syndicats interdits · salaires gelés · temps de travail allongé", "Droits de douane sur les importations",
            "Grands travaux, comme sous Weimar : l'Autobahn", "Le réarmement, malgré Versailles",
            "Privatisations : Deutsche Bank, chemins de fer, chantiers navals", "Un crime : pillage à l'étranger, biens juifs spoliés"], x=130, y=80, w=1020),
        "six": dict(type="mot", t="6 millions → moins d'1 million", g="chômage enregistré en Allemagne, 1933 → 1937", y=250, taille=76),
        "lec": dict(type="note", terme="Lire la liste d'un seul tenant", cles=["guerre", "vol"],
                    t="Un régime qui résout le chômage en préparant la guerre, et qui le paie par le vol.",
                    etape="Une reprise qui n'a de sens que si la guerre suit.", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 4 : le militarisme
    dict(id="militarisme", chap="II.2 · Le militarisme de trois régimes", fond="nuit", humeur="tension",
         retenir="Notion clé. Le militarisme : une force militaire puissante, prête à être employée de manière agressive. Trois dimensions : développement des forces armées (budget), contrôle du gouvernement par les militaires (constitution), politique étrangère agressive (guerre). Allemagne, Italie, Japon.",
         beats=[
        "{def3}Quatrième idée : le {!militarisme}militarisme. Il gagne trois régimes à la fois : celui de Hitler, celui de Mussolini, et le gouvernement japonais. "
        "De quoi s'agit-il ? De la conviction qu'un gouvernement doit entretenir une force militaire puissante… et être prêt à l'employer de manière agressive, "
        "pour défendre ou promouvoir l'intérêt national.",
        "Il a trois dimensions, et une composition doit les nommer toutes. {-def3}{dims}{dims.1}Le développement des forces armées : un choix budgétaire. "
        "{dims.2}Le contrôle du gouvernement par les militaires : un choix constitutionnel. "
        "{dims.3}Et une politique étrangère agressive : celle qui finit en guerre.",
        "{-dims}{g3}{g3.1}Le Japon montre le mieux la deuxième dimension. En septembre mille neuf cent trente et un, l'armée du Kwantung agit d'abord en Mandchourie. "
        "Le gouvernement civil de Tokyo doit s'expliquer ensuite. L'armée décide ; le gouvernement suit.",
        "{-g3}{ki}Et la problématique du cours se trouve justement là. Facteurs économiques, idéologie… ou les deux ? On y répond à la fin de cet épisode.",
    ], vis={
        "def3": dict(type="def", cles=["puissante", "agressive"], terme="Le militarisme",
                     t="Un gouvernement doit entretenir une force militaire puissante et être prêt à l'employer de manière agressive.",
                     etape="Allemagne · Italie · Japon, dans les années 1930", x=170, y=200, w=940),
        "dims": dict(type="liste", titre="Les trois dimensions du militarisme", cles=["budgétaire", "constitutionnel", "guerre"], items=[
            "Le développement des forces armées → un choix budgétaire", "Les militaires contrôlent le gouvernement → un choix constitutionnel",
            "Une politique étrangère agressive → celle qui finit en guerre"], x=150, y=140, w=980),
        "g3": dict(type="globe", code="H1", sc=[18]),
        "ki": dict(type="question", t="Facteurs économiques et / ou idéologie ?"),
    }),

    # ================================================================ II.2, idée 5 : le New Deal
    dict(id="newdeal", chap="II.2 · Le New Deal", fond="aube", humeur="lumiere",
         retenir="Roosevelt, démocrate, élu en 1932 : le New Deal, Relief, Recovery, Reform. Premier New Deal (1933-1935) : les cent jours, CCC, TVA, dépôts assurés. Second New Deal (1935) : Social Security Act, WPA. De l'argent public pour des ponts et des droits, pas pour une armée.",
         beats=[
        "{m_nd}Cinquième idée. Les États-Unis choisissent la voie opposée. Le protectionnisme de Hoover a fait la preuve de son inefficacité. "
        "Roosevelt, un démocrate, est élu en mille neuf cent trente-deux. Il promeut un New Deal, et un État-providence : "
        "une politique de relance. {-m_nd}{rrr}En trois mots anglais : {rrr.1}Relief, le secours aux plus démunis. {rrr.2}Recovery, la reprise de l'économie. "
        "{rrr.3}Reform, la réforme du système qui a failli.",
        "{-rrr}{hd}Il vient en deux temps. Le premier New Deal va de mille neuf cent trente-trois à trente-cinq. "
        "Il s'ouvre sur les lois d'urgence des cent premiers jours. {-hd}{c_fdr}Leur but, tel que le cours le résume : "
        "aider les millions de gens qui n'ont jamais eu leur chance. Des hommes à salaire de famine. Des femmes dans les ateliers de misère. Des enfants aux métiers à tisser.",
        "{-c_fdr}{fr1}{fr1.1}Roosevelt, élu en trente-deux. {fr1.2}Les cent jours créent le Civilian Conservation Corps "
        "et la Tennessee Valley Authority. Ils assurent aussi les dépôts bancaires. "
        "{fr1.3}Puis vient le second New Deal, en trente-cinq. Il transforme le secours en droits : le Social Security Act, "
        "avec les retraites et l'assurance chômage. Et la Works Progress Administration.",
        "{fr1.4}Le cours cite aussi le pont du Golden Gate, à San Francisco, qui s'élève à partir de trente-trois sous la même impulsion. "
        "Une précision, hors du cours : il est inauguré en trente-sept. Et c'est un projet local, financé par les emprunts d'un district régional. "
        "Pas un programme fédéral du New Deal.",
        "{-fr1}{cmp2}{cmp2.g}Et maintenant, l'intérêt de la comparaison. Les deux États dépensent de l'argent public contre le chômage. "
        "{cmp2.d}Mais l'un construit des ponts et une assurance sociale… L'autre construit une armée.",
    ], vis={
        "m_nd": dict(type="mot", t="Le New Deal", g="Roosevelt, démocrate, élu en 1932 · un État-providence, une politique de relance", y=250, taille=96),
        "rrr": dict(type="liste", titre="Le New Deal en trois mots", cles=["Relief", "Recovery", "Reform"], items=[
            "Relief · le secours aux plus démunis", "Recovery · la reprise de l'économie", "Reform · la réforme du système qui a failli"], x=170, y=160, w=940),
        "fr1": dict(type="frise", items=[
            dict(nom="Roosevelt élu", d=1932), dict(nom="Les cent jours", d=1933, q="CCC · TVA · dépôts assurés"),
            dict(nom="Second New Deal", d=1935), dict(nom="Golden Gate", d=1937, q="construit de 1933 à 1937 (projet local)")]),
        "hd": dict(type="mot", t="Les cent jours", g="Premier New Deal · 1933 – 1935 · lois d'urgence", y=260, taille=90),
        "c_fdr": dict(type="note", terme="Le but du New Deal (cours)", cles=["millions", "chance"],
                      t="Aider les millions qui n'ont jamais eu leur chance : des hommes à salaire de famine, des femmes dans les ateliers de misère, des enfants aux métiers à tisser.",
                      etape="Le programme de Roosevelt, tel que le cours le résume", x=170, y=200, w=940),
        "cmp2": dict(type="cols", g="États-Unis · le New Deal", gq="de l'argent public pour des ponts, des barrages et une assurance sociale",
                     d="Allemagne · le nazisme", dq="de l'argent public pour des autoroutes et, surtout, une armée", vs="≠"),
    }),

    # ================================================================ II.2, idée 6 : la diplomatie du New Deal
    dict(id="diplo", chap="II.2 · La diplomatie du New Deal", fond="aube", humeur="calme",
         retenir="La diplomatie du New Deal : le RTAA (1934) pour libéraliser le commerce ; l'URSS reconnue (nov. 1933) ; la politique de « bon voisinage » en Amérique latine. Du commerce et de nouveaux partenaires, mais aucune alliance.",
         beats=[
        "{m_dip}Sixième idée. Le New Deal a aussi une politique étrangère, et elle va à contre-courant du nationalisme économique. "
        "{-m_dip}{dip}{dip.1}D'abord, la loi de trente-quatre sur les accords commerciaux, que tu connais déjà : des accords, pays par pays. "
        "Sa limite ? Les chefs fascistes les refusent.",
        "{dip.2}Ensuite. En novembre mille neuf cent trente-trois, Roosevelt reconnaît l'Union soviétique, seize ans après la révolution. "
        "Pourquoi ? L'Union soviétique pourrait aider contre le Japon. Et commercer avec elle pourrait aider l'économie américaine.",
        "{dip.3}Enfin, la politique de {!bon voisinage}bon voisinage. Elle met fin à des décennies d'interventions américaines en Amérique latine. "
        "Les derniers marines avaient quitté le Nicaragua en janvier trente-trois, juste avant l'arrivée de Roosevelt. "
        "Puis, en trente-quatre, les États-Unis renoncent à leur droit d'intervenir à Cuba. Et ils retirent leurs marines d'Haïti.",
        "{-dip}{bil2}Voici donc le tableau : un président qui tente de rouvrir le monde économiquement, {!pendant que son Congrès le ferme politiquement}"
        "pendant que son Congrès le ferme politiquement. Du commerce, de nouveaux partenaires… {bil2.1}mais aucune alliance. Ce sera l'épisode quatre.",
    ], vis={
        "m_dip": dict(type="mot", t="La diplomatie du New Deal", g="une politique étrangère contre le nationalisme économique", y=260, taille=80),
        "dip": dict(type="liste", titre="La diplomatie du New Deal", cles=["accord", "reconnue", "voisinage"], items=[
            "1934 · le RTAA : libéraliser le commerce, accord par accord", "Nov. 1933 · l'URSS reconnue : contre le Japon, pour le commerce",
            "Le « bon voisinage » : fin des interventions (Nicaragua janv. 1933 ; Cuba et Haïti 1934)"], x=150, y=140, w=980),
        "bil2": dict(type="note", terme="Le paradoxe", cles=["rouvre", "ferme"],
                     t="Un président qui rouvre le monde économiquement, un Congrès qui le ferme politiquement.",
                     etape="Du commerce et de nouveaux partenaires, mais aucune alliance.", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 7 : le Front populaire
    dict(id="frontpop", chap="II.2 · Le Front populaire", fond="nuit", humeur="lumiere",
         retenir="France : le 6 février 1934 → socialistes, communistes et radicaux s'unissent → le Front populaire gagne en 1936 (Léon Blum) : semaine de 40 heures, deux semaines de congés payés, la SNCF, accords de Matignon (+7 à 15 %). Déficits keynésiens ; apaisement et non-intervention en Espagne. Gains absorbés par la chute du franc.",
         beats=[
        "{g4}Septième idée. La France répond tard, et par la gauche. {g4.1}Le six février mille neuf cent trente-quatre, "
        "les ligues d'extrême droite manifestent violemment à Paris. Le cours y voit un coup de force manqué. Par peur du fascisme, "
        "socialistes, communistes et radicaux se rassemblent. C'est le {!Front populaire}Front populaire. "
        "Il gagne les élections de trente-six, et Léon Blum devient président du Conseil.",
        "{-g4}{blum}{fp}Que fait-il ? {fp.1}La semaine de quarante heures. {fp.2}Deux semaines de congés payés. "
        "{fp.3}Les compagnies de chemin de fer, nationalisées dans la SNCF. "
        "{fp.4}Et son économie est {!keynésienne}keynésienne : dépenses et déficits, pour relancer la demande. "
        "L'exact opposé de la voie allemande : l'austérité, puis le réarmement.",
        "{-fp}{-blum}{intl}{intl.g}À l'extérieur, il choisit l'apaisement, et la non-intervention dans la guerre d'Espagne. "
        "{intl.d}Mais il lance aussi un plan de réarmement, en septembre trente-six : "
        "quatorze milliards de francs, sur quatre ans.",
        "{-intl}{mat}L'exemple. {mat.1}Les accords de Matignon, en juin mille neuf cent trente-six, relèvent les salaires de sept à quinze pour cent en une semaine. "
        "{mat.2}Mais la France ne quitte l'étalon-or qu'à l'automne, et la chute du franc absorbe les gains. "
        "{mat.3}En trente-huit, la semaine de quarante heures est déjà démantelée.",
        "{-mat}{trois}Une crise, donc, et trois réponses. {trois.1}L'Allemagne : contrainte, réarmement, autarcie, et la guerre. "
        "{trois.2}Les États-Unis : le New Deal, secourir, relancer, réformer. "
        "{trois.3}La France : réforme sociale à l'intérieur, apaisement à l'extérieur.",
    ], vis={
        "g4": dict(type="globe", code="H1", sc=[24]),
        "blum": dict(type="tableau", img="h1-blum-1936", fond=True, sombre=True, de=[1.0, .7, .4], a=[1.15, .72, .35],
                     legende="Léon Blum à son bureau, devant un micro, 1936 (Agence Meurisse, domaine public)"),
        "fp": dict(type="liste", titre="Le Front populaire (Léon Blum, 1936)", cles=["semaine", "congés", "SNCF", "keynésienne"], items=[
            "La semaine de 40 heures", "Deux semaines de congés payés", "Chemins de fer nationalisés : la SNCF",
            "Une économie keynésienne : dépenses et déficits pour relancer la demande"], x=170, y=130, w=940),
        "intl": dict(type="cols", g="À l'extérieur", gq="apaisement · non-intervention en Espagne", d="L'armée",
                     dq="un plan de réarmement, sept. 1936 : 14 milliards de francs sur quatre ans", vs="+"),
        "mat": dict(type="liste", titre="Exemple · les accords de Matignon", cles=["salaires", "franc", "démantelée"], items=[
            "Juin 1936 : salaires +7 à 15 % en une semaine", "Automne 1936 : sortie de l'or, la chute du franc absorbe les gains",
            "1938 : la semaine de 40 heures démantelée"], x=170, y=150, w=940),
        "trois": dict(type="liste", titre="Une crise, trois réponses", cles=["Allemagne", "États-Unis", "France"], items=[
            "Allemagne : contrainte, réarmement, autarcie… la guerre", "États-Unis : le New Deal, Relief, Recovery, Reform",
            "France : réforme sociale à l'intérieur, apaisement à l'extérieur"], x=150, y=150, w=980),
    }),

    # ================================================================ à toi : la problématique du chapitre
    dict(id="keyissue", chap="À toi · la problématique du chapitre", fond="aube", humeur="calme",
         retenir="Le nationalisme économique : un facteur aggravant sérieux, mais pas le facteur décisif. Il explique pourquoi le monde n'a pas su coopérer, pas pourquoi trois régimes ont choisi la guerre. L'économie a créé l'occasion ; l'idéologie a fourni l'intention.",
         beats=[
        "{ex4}Voici maintenant la grande problématique du chapitre. "
        "Dans quelle mesure le nationalisme économique a-t-il été {!le facteur décisif}le facteur décisif de la marche à la guerre en mille neuf cent trente-neuf ?",
        "Définis le nationalisme économique : l'intérêt économique national placé au-dessus de la coopération internationale, "
        "par les droits de douane, les quotas et les choix monétaires. Puis mets à l'épreuve le mot décisif.",
        "{-ex4}{pa2}",
        ("P", 4.0),
        "{-pa2}{rep2}Un plan possible. {rep2.1}Première partie. Oui, le nationalisme économique ronge l'ordre international. "
        "Le tarif Smoot-Hawley, les quotas français, l'Import Duties Act. Le commerce mondial perd deux tiers de sa valeur, et le monde se divise en blocs impériaux. "
        "Il rend même l'autarcie et la conquête rationnelles en apparence, pour un État sans empire. C'est exactement ce que prétendait la politique nazie.",
        "{rep2.2}Deuxième partie. Mais c'est un symptôme autant qu'une cause. Le protectionnisme répond à la Dépression, et la Dépression suit le krach. "
        "La chaîne commence à Wall Street, pas dans les bureaux de douane. Et le Royaume-Uni et la France pratiquent eux aussi le nationalisme économique… "
        "sans choisir la guerre.",
        "{rep2.3}Troisième partie. L'idéologie dispute la même place. Le militarisme, avec ses trois dimensions, à Berlin, à Rome et à Tokyo. "
        "Et le pillage des nations conquises, la spoliation des biens juifs : des crimes qu'aucune barrière douanière n'explique.",
        "{rep2.4}La conclusion. Un facteur aggravant sérieux, mais pas le facteur décisif. Il explique pourquoi le monde n'a pas su coopérer. "
        "Pas pourquoi trois régimes ont choisi la guerre. {!les facteurs économiques ont créé l'occasion}Les facteurs économiques ont créé l'occasion ; "
        "l'idéologie a fourni l'intention.",
    ], vis={
        "ex4": dict(type="exo", niveau="essay", titre="Dans quelle mesure le nationalisme économique a-t-il été le facteur décisif de la marche à la guerre en 1939 ?",
                    src="Problématique du chapitre", enonce=["Définis le nationalisme économique", "Mets à l'épreuve le mot « décisif »",
                                                              "Trois parties et une conclusion"]),
        "pa2": dict(type="pause", t="Fais un plan en trois parties, avec des preuves, et une conclusion : dans quelle mesure ?",
                    sous="Mets la vidéo en pause, écris ton plan, puis reprends pour voir un modèle."),
        "rep2": dict(type="liste", titre="Un plan possible", cles=["ronge", "symptôme", "idéologie", "occasion"], items=[
            "I. Il ronge l'ordre : droits de douane, quotas, blocs, −66 %, l'autarcie paraît rationnelle",
            "II. Un symptôme autant qu'une cause : la chaîne commence à Wall Street",
            "III. L'idéologie dispute la place : militarisme de trois régimes, pillage, spoliation",
            "Conclusion : l'économie a créé l'occasion ; l'idéologie a fourni l'intention"], x=130, y=120, w=1020),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récap", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Le nationalisme économique. L'internationalisme indépendant de Hoover cède la place au tarif Smoot-Hawley. "
        "Puis viennent les représailles, les blocs impériaux fermés, et un commerce mondial amputé des deux tiers. Roosevelt renverse la politique… trop tard. "
        "{carte.2}L'Allemagne, la plus exposée. Les nazis n'ont jamais eu la majorité, mais on les a laissés entrer, et ils ont bâti une économie de guerre. "
        "{carte.3}Le militarisme, dans trois régimes, avec ses trois dimensions. "
        "{carte.4}Et les réponses des démocraties : le New Deal et sa diplomatie, et le Front populaire.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : les démocraties et l'ordre libéral. La Société des Nations, la Mandchourie, les lois de neutralité… "
        "et la route de Munich.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="NATIONALISME ÉCONOMIQUE", branches=[
            dict(t="II.1 · Nationalisme", items=["Smoot-Hawley, 17 juin 1930", "blocs · Ottawa 1932 · −66 %", "sortie de l'or · RTAA 1934"]),
            dict(t="Allemagne", items=["43,8 % de chômeurs (1932)", "jamais majoritaires · janv. 1933", "réarmement · pillage"]),
            dict(t="Militarisme", items=["forces armées · pouvoir militaire", "politique étrangère agressive", "Allemagne · Italie · Japon"]),
            dict(t="Démocraties", items=["New Deal : les 3 R · 1933-1935", "URSS reconnue · bon voisinage", "Front populaire 1936"])]),
        "fin": dict(type="mot", t="Prochain épisode : les démocraties et l'ordre libéral", g="Épisode 4 · la SDN, la neutralité, l'apaisement", y=270, taille=60),
    }),
]

QUIZ = [
    dict(q="Que désigne le cours par l'« internationalisme indépendant » de Hoover ?",
         r=["Engagé dans l'économie mondiale, absent de ses institutions politiques", "Un isolement total du commerce mondial",
            "L'adhésion à la SDN sans alliances", "Des alliances militaires sans commerce"], ok=0, voir="def1",
         ex="Les exportations et l'investissement, oui ; les alliances et la SDN, non. Ce n'est pas de l'isolationnisme."),
    dict(q="Que fait le tarif Smoot-Hawley (17 juin 1930) ?",
         r=["Il relève les droits sur plus de 20 000 produits importés", "Il détache le dollar de l'or",
            "Il baisse les droits pays par pays", "Il assure les dépôts bancaires"], ok=0, voir="fiche",
         ex="Le deuxième niveau de droits le plus élevé de l'histoire américaine, malgré 1 028 économistes et 23 pays qui protestent."),
    dict(q="Qu'officialise la conférence d'Ottawa de 1932 ?",
         r=["La préférence impériale entre le Royaume-Uni et ses dominions", "La fin des réparations",
            "Un accord mondial de libre-échange", "Les quotas d'importation français"], ok=0, voir="ott",
         ex="Des droits bas dans l'Empire, élevés pour tous les autres : le libre-échange, pilier de 1919, a disparu."),
    dict(q="De combien le commerce mondial baisse-t-il en valeur entre 1929 et 1934, selon le cours ?",
         r=["D'environ deux tiers", "D'environ 10 %", "D'environ un quart", "Il double"], ok=0, voir="gc",
         ex="Environ −66 % : l'économie mondiale devient un ensemble de blocs impériaux rivaux."),
    dict(q="Que permet le Reciprocal Trade Agreements Act (RTAA) de 1934 ?",
         r=["Des baisses de droits négociées pays par pays", "Un tarif général de 10 %",
            "La reconnaissance de l'URSS", "La sortie de l'étalon-or"], ok=0, voir="rev",
         ex="Une vingtaine d'accords en 1939, aucun avec l'Allemagne, l'Italie ou le Japon."),
    dict(q="Quel est le chômage des travailleurs assurés en Allemagne en 1932 (dossier documentaire) ?",
         r=["43,8 %", "8,6 %", "25 %", "13,3 %"], ok=0, voir="gch",
         ex="8,6 % en 1928, 43,8 % en 1932 : sur l'ensemble de la population active, le taux est plus bas, environ 30 %."),
    dict(q="Comment Hitler arrive-t-il au pouvoir ?",
         r=["Nommé chancelier par des conservateurs en janvier 1933, sans majorité", "Élu avec 52 % des voix en 1932",
            "Par un coup d'État en novembre 1932", "Nommé par la Société des Nations"], ok=0, voir="porte",
         ex="Le vote nazi culmine à 37,3 % (juillet 1932) ; la peur du communisme ouvre la porte."),
    dict(q="Quels sont les trois mots du New Deal ?",
         r=["Relief, Recovery, Reform", "Travail, Liberté, Pain", "Stabilité, Emploi, Autarcie", "Cash and carry"], ok=0, voir="rrr",
         ex="Le secours aux plus démunis, la reprise de l'économie, la réforme du système qui a failli."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 1 « Le krach de 1929 et ses conséquences » (parties II.1 et II.2 : la fiche du tarif Smoot-Hawley, le dossier documentaire sur l'Allemagne), tel qu'il est rédigé sur le site ; la carte animée du chapitre.",
    "Hors cours (signalé dans la vidéo) : l'inauguration du pont du Golden Gate (1937) et son financement local.",
    "Photographie : Herbert Hoover et Franklin D. Roosevelt en route vers l'investiture, 4 mars 1933 (Architect of the Capitol, domaine public, Wikimedia Commons).",
    "Photographie : chômeurs devant l'office de l'emploi de Berlin-Nord-Est, 4 mai 1932 (Bundesarchiv, Bild 146-1976-033-23, photographe Seiler, CC BY-SA 3.0 de, Wikimedia Commons).",
    "Photographie : Léon Blum à son bureau, devant un micro, 1936 (Agence de presse Meurisse, domaine public, Wikimedia Commons).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
