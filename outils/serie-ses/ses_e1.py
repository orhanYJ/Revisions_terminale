"""SES, É1 : « Quels sont les sources et les défis de la croissance économique ? » — le chapitre en vidéo (pilote SES).

Même chaîne que les autres vidéos (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots) ; moteur
ses/serie/moteur.js, qui ajoute les types donnees (graphiques du site), chaine (chaînes causales du site), chiffres,
sanim (animations du site rejouées), auteur et compare.
Contenu : le chapitre É1 du site « Faits & Courbes » (outils/specialites/ses/src/data-e1.js, data-anim-e1.js), rien
au-delà. Les graphiques, chaînes causales et animations sont lus dans les sources du site (site_ses.py) : mêmes données,
mêmes sources. Les sujets corrigés sont ceux du site (« sujet inventé pour le site ») ; les nombres lus par la voix sont
écrits en lettres.
Usage : python3 outils/serie-philo/verifier.py ses_e1 ; SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py ses_e1
(brouillon sans voix) ; chevauchements.py ses-e1 ; fermer.py ses_e1.
"""
import site_ses

SITE = "ses"
CODE = "ses-e1"
NOTION = "La croissance économique"
NUM = 1
TITRE = "Quels sont les sources et les défis de la croissance économique ?"
SUIVANT = "É2 · Les fondements du commerce international"
RYTHME = "vivant"
PRONONCIATION = {"Solow": "Sollo", "Romer": "Romeure", "Barro": "Baro", "Douglass": "Douglasse", "North": "Norse",
                 "Acemoglu": "Adjémo-olou", "Schumpeter": "Choumpéteur", "Aghion": "Aguion", "Howitt": "Haouitte",
                 "Mokyr": "Mokir", "Goldin": "Goldine", "Katz": "Katse", "Autor": "Otor", "Meadows": "Médoze",
                 "Donella": "Donéla", "Jevons": "Djévonse", "Stanley": "Stanlé", "Karikó": "Kariko", "Katalin": "Katalinne",
                 "Weissman": "Ouaïsmane", "Drew": "Drou", "BioNTech": "Bio-ène-tèque", "Pfizer": "Faïzeur", "Insee": "Inssé",
                 "Citepa": "Sitépa", "Lawrence": "Lorince", "Peter": "Piteur", "Joel": "Djoël", "Simon": "Saïmone",
                 "Johnson": "Djonsone", "James": "Djèmse", "Daron": "Daronne", "David": "Dévid", "LED": "èl-eu-dé",
                 "Dennis": "Dénisse", "Covid-19": "Covid dix-neuf", "PIB": "pé-i-bé", "PGF": "pé-gé-èf",
                 "ARN": "a-èr-ène", "SES": "èss-eu-èss"}

D = site_ses.donnees()
G, CHN, CH = D["graphes"], D["chaines"], D["ch"]["e1"]
CHIF = CH["chiffres"]          # les trois « En chiffres » du chapitre

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="canard", humeur="mystere", carton=False, beats=[
        "{q_86}En mille neuf cent cinquante, la France produit une certaine quantité de biens et de services. "
        "Soixante-quinze ans plus tard, combien en produit-elle ?",
        "{-q_86}{cf_86}{cf_86.1}Huit virgule six fois plus. À prix constants. Huit fois et demie plus de richesses produites.",
        "{-cf_86}{q_ouv}Alors, d'où vient tout ça ? Plus de travailleurs ? Plus de machines ? Ou autre chose ?",
        "{-q_ouv}{q_ouv2}Et deux autres questions, tout aussi importantes. Cette croissance profite-t-elle à tout le monde ? "
        "Et peut-elle continuer sur une planète aux ressources limitées ?",
        "{-q_ouv2}{plan}Voilà le chemin. {plan.1}D'abord, mesurer la croissance. "
        "{plan.2}Ensuite, ses sources : le travail, le capital, et surtout le progrès technique. "
        "{plan.3}Puis les institutions, et la destruction créatrice. {plan.4}Les inégalités que crée le progrès technique. "
        "{plan.5}Les limites écologiques. {plan.6}Et pour finir, le bac : les calculs, les trois parties de l'épreuve composée et la dissertation, "
        "avec des sujets corrigés.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q_86": dict(type="question", t="1950 → 2025 : combien de fois plus ?"),
        "cf_86": dict(type="chiffres", titre="En chiffres", x=110, y=150, w=1060, items=[
            dict(n="×8,6", l="Le PIB de la France en volume entre 1950 et 2025 : de 309,1 à 2 646,7 milliards d'euros de 2020.",
                 s="Insee, comptes nationaux annuels, base 2020")]),
        "q_ouv": dict(type="question", t="Plus de travailleurs ? Plus de machines ? Ou autre chose ?"),
        "q_ouv2": dict(type="question", t="Pour tout le monde ? Et sur une planète finie ?"),
        "plan": dict(type="liste", titre="Le chemin", x=170, y=96, w=940, items=[
            "Mesurer la croissance", "Ses sources : travail, capital, progrès technique",
            "Institutions et destruction créatrice", "Progrès technique et inégalités",
            "Les limites écologiques", "Au bac : calculs, épreuve composée, dissertation"]),
        "titre": dict(type="titre", sur="SES · Terminale · É1", t="Les sources et les défis de la croissance",
                      sous="Le chapitre complet, de zéro au bac"),
    }),

    # ================================================================ I. mesurer
    dict(id="mesurer", chap="Mesurer la croissance", fond="nuit", humeur="lumiere",
         retenir="Croissance : augmentation durable de la production, mesurée par le taux de variation du PIB en volume. "
                 "France : 5,2 % par an de 1950 à 1973, environ 1 % par an depuis 2007 (Insee).",
         beats=[
        "{def_cr}Commençons par une définition à savoir par cœur. La croissance économique, c'est l'augmentation {!durable}durable "
        "de la production de biens et de services d'un pays.",
        "Durable : pas un bond d'une seule année. {def_cr.1}Et on la mesure par le taux de variation du PIB, le produit intérieur brut… en volume.",
        "{-def_cr}{def_pib}Le PIB, c'est la somme des valeurs ajoutées produites sur le territoire pendant un an. "
        "On y ajoute les impôts sur les produits, et on retire les subventions sur les produits.",
        "{-def_pib}{cols_vv}Pourquoi en volume ? {cols_vv.g}Parce qu'un PIB en valeur peut augmenter… simplement parce que les prix montent. "
        "{cols_vv.d}Le PIB en volume, lui, est corrigé de la hausse des prix : il mesure les quantités produites, pas l'inflation.",
        "C'est un rappel de Première, mais c'est le piège numéro un des copies : la croissance, c'est toujours le PIB en volume.",
        ("P", 0.5),
        "{-cols_vv}{gr_pib}Maintenant, regardons soixante-quinze ans de croissance française, année par année. "
        "Chaque barre, c'est le taux de croissance d'une année. La source : l'Insee.",
        "{gr_pib.1}Premier âge : de mille neuf cent cinquante à mille neuf cent soixante-treize, le cœur des Trente Glorieuses. "
        "La croissance dépasse souvent cinq pour cent. En moyenne : cinq virgule deux pour cent par an. La France rattrape son retard.",
        "{gr_pib.2}Puis viennent les chocs pétroliers. En mille neuf cent soixante-quinze, le PIB recule : moins zéro virgule neuf pour cent. "
        "Et la croissance ne retrouvera plus jamais ce rythme : deux virgule quatre pour cent par an en moyenne de mille neuf cent soixante-treize "
        "à deux mille sept, avec une récession en mille neuf cent quatre-vingt-treize.",
        "{gr_pib.3}Deux mille neuf : la crise financière. Moins deux virgule huit pour cent.",
        "{gr_pib.4}Les années deux mille dix : une croissance faible. Un virgule quatre pour cent par an en moyenne.",
        "{gr_pib.5}Et deux mille vingt : le Covid. Moins sept virgule quatre pour cent, la pire année de la série. "
        "Puis un rebond : plus six virgule neuf en deux mille vingt et un. Et en deux mille vingt-cinq ? Plus zéro virgule huit pour cent.",
        "{-gr_pib}{gr_per}Résumons par période. {gr_per.1}Cinq virgule deux pour cent par an pendant les Trente Glorieuses. "
        "{gr_per.2}Deux virgule quatre de mille neuf cent soixante-treize à deux mille sept. "
        "{gr_per.3}Un pour cent de deux mille sept à deux mille dix-neuf. {gr_per.4}Et zéro virgule neuf depuis deux mille dix-neuf.",
        "La croissance française a été divisée par cinq. Toute la question du chapitre est là : qu'est-ce qui fait la croissance ? "
        "Et pourquoi ralentit-elle ?",
        "{-gr_per}{cols_dev}{cols_dev.g}Deux distinctions encore, rapidement. Croissance n'est pas développement. "
        "Le développement, c'est l'amélioration durable du bien-être : la santé, l'éducation, le niveau de vie. "
        "La croissance en fournit les moyens… sans le garantir.",
        "{cols_dev.d}Et la croissance effective, celle qu'on observe, n'est pas la croissance potentielle : "
        "celle que permettraient tous les facteurs de production pleinement employés. Elle dépend justement des sources de la croissance.",
        "{-cols_dev}",
    ], vis={
        "def_cr": dict(type="def", terme="Croissance économique", cles=["durable", "volume"],
                       t="Augmentation durable de la production de biens et de services d'un pays.",
                       etape="On la mesure par le taux de variation du PIB en volume.", x=170, y=170, w=940),
        "def_pib": dict(type="def", terme="PIB · produit intérieur brut", cles=["valeurs", "territoire"],
                        t="Somme des valeurs ajoutées produites sur le territoire pendant un an (plus les impôts sur les produits, moins les subventions sur les produits).",
                        x=170, y=180, w=940),
        "cols_vv": dict(type="cols", g="En valeur", gq="Aux prix de l'année : il monte aussi quand seuls les prix montent.",
                        d="En volume", dq="Corrigé de la hausse des prix : il mesure les quantités produites.", vs="≠",
                        repere="La croissance se mesure toujours en volume"),
        "gr_pib": dict(type="donnees", g=G["e1-pib"], x=60, y=74, w=1160, h=600, phases=[
            dict(de=1950, a=1973, l="Trente Glorieuses", moy=5.2, dur=4.5),
            dict(de=1974, a=2007, l="Après les chocs pétroliers", moy=2.4, dur=5, lp=[1998, 5.6]),
            dict(de=2008, a=2009, l="Crise financière", dur=1.4),
            dict(de=2010, a=2019, l="Années 2010", moy=1.4, dur=3, lp=[2014, 4.2]),
            dict(de=2020, a=2025, l="Covid, rebond", dur=3)]),
        "gr_per": dict(type="donnees", g=G["e1-periodes"], x=110, y=110, w=1060, h=500, lab=230),
        "cols_dev": dict(type="cols", g="Croissance ≠ développement", gq="Le développement : l'amélioration durable du bien-être (santé, éducation, niveau de vie).",
                         d="Effective ≠ potentielle", dq="La potentielle : celle que permettraient tous les facteurs pleinement employés.", vs="≠"),
    }),

    # ================================================================ II. les sources
    dict(id="sources", chap="Les sources de la croissance", fond="canard", humeur="lumiere",
         retenir="Croissance extensive (plus de facteurs) ou intensive (plus de productivité). La PGF, le « résidu » de Solow, "
                 "reflète le progrès technique : sans lui, l'accumulation du capital s'essouffle.",
         beats=[
        "{q_src}Pour produire plus, il n'y a que deux moyens. Lesquels ?",
        "{-q_src}{cols_ei}{cols_ei.g}Premier moyen : utiliser plus de facteurs de production. Plus de travailleurs, plus d'heures, "
        "plus de machines, de bâtiments, de logiciels. C'est la croissance {!extensive}extensive.",
        "{cols_ei.d}Deuxième moyen : les utiliser plus efficacement. Produire plus avec les mêmes quantités de facteurs. "
        "C'est la croissance intensive : elle vient de la hausse de la productivité.",
        "{-cols_ei}{cols_prod}Et attention : il existe deux mesures de la productivité. {cols_prod.g}La productivité apparente du travail : "
        "la production divisée par la quantité de travail, par emploi ou par heure. Elle augmente aussi quand chaque travailleur dispose de plus de capital.",
        "{cols_prod.d}Et la productivité globale des facteurs, la {!PGF}PGF. Elle mesure l'efficacité de la combinaison du travail et du capital. "
        "C'est la part de la croissance que la hausse des quantités de facteurs n'explique pas.",
        "{-cols_prod}{au_solow}Pour comprendre pourquoi la PGF compte autant, il faut passer par Robert Solow, prix Nobel en mille neuf cent quatre-vingt-sept.",
        "{-au_solow}{an_solow}Suivons son raisonnement. {an_solow.1}Plus chaque travailleur a de capital, plus il produit : c'est la fonction de production.",
        "{an_solow.2}Mais les rendements sont décroissants. La première machine change tout. La dixième… beaucoup moins.",
        "{an_solow.3}Résultat : si on se contente d'accumuler du capital, on bute sur un plafond. La croissance s'essouffle. "
        "C'est le modèle de Solow, en mille neuf cent cinquante-six.",
        "{an_solow.4}Alors, comment croître durablement ? Grâce au progrès technique. Il déplace toute la courbe vers le haut : "
        "avec le même capital, on produit plus. C'est exactement la hausse de la productivité globale des facteurs.",
        "{an_solow.5}Et en mille neuf cent cinquante-sept, Solow le mesure. Aux États-Unis, de mille neuf cent neuf à mille neuf cent quarante-neuf, quatre-vingt-sept et demi pour cent, sept huitièmes, "
        "de la hausse de la production par heure de travail ne vient pas du capital. Elle vient du progrès technique. "
        "Ce supplément, on l'appelle le {!résidu}résidu : le résidu de Solow.",
        "{-an_solow}{ill_res}Comment mesure-t-on ce résidu ? En creux. Prenons un exemple chiffré, inventé. Une économie croît de deux pour cent par an. "
        "{ill_res.1}La hausse du travail y contribue pour zéro virgule quatre point. {ill_res.2}Celle du capital, pour zéro virgule six point. "
        "{ill_res.3}Et le reste, c'est la PGF. {ill_res.4}Deux, moins zéro virgule quatre, moins zéro virgule six : un point. La moitié de la croissance.",
        "Petite subtilité : ce résidu mesure aussi, en partie, notre ignorance. La qualité du travail, l'organisation, les institutions s'y mélangent.",
        "{-ill_res}{def_pt}Le lien avec le progrès technique est direct. Le progrès technique, c'est l'ensemble des innovations "
        "qui améliorent les produits, les procédés et l'organisation. Il fait augmenter la PGF.",
        "{-def_pt}{an_gains}Mais comment des gains de productivité deviennent-ils de la croissance ? Entrons dans une usine. "
        "{an_gains.1}Cent objets par jour, avec dix salariés : dix objets par salarié et par jour.",
        "{an_gains.2}Une nouvelle machine arrive. Les mêmes dix salariés produisent cent vingt-cinq objets. "
        "La productivité du travail augmente de vingt-cinq pour cent.",
        "{an_gains.3}Chaque objet coûte donc moins cher à produire. L'entreprise dispose d'un surplus. Et la vraie question, c'est : qui le reçoit ?",
        "{an_gains.4}Les consommateurs, par des prix plus bas. Les salariés, par des salaires plus élevés. L'entreprise, par des profits.",
        "{an_gains.5}Et tout ce monde dépense ou investit davantage. La demande augmente : il faut produire plus, et embaucher. "
        "Les gains de productivité nourrissent la croissance.",
        "{-an_gains}{ch_pgf}{ch_pgf.1}Voici ce mécanisme en chaîne causale. C'est elle qu'il faut savoir dérouler dans une copie. "
        "Le progrès technique fait augmenter la productivité globale des facteurs. "
        "{ch_pgf.2}Donc on produit davantage avec les mêmes quantités de travail et de capital. {ch_pgf.3}Donc le coût unitaire de production baisse.",
        "{ch_pgf.4}Les gains se partagent : les prix peuvent baisser, et le pouvoir d'achat augmente. Les salaires et les profits peuvent augmenter. "
        "{ch_pgf.5}Donc la demande augmente : la consommation et l'investissement. {ch_pgf.6}Et les entreprises produisent plus : c'est la croissance du PIB.",
        "{ch_pgf.tout}",
        ("P", 1.6),
        "{-ch_pgf}",
    ], vis={
        "q_src": dict(type="question", t="Produire plus : quels sont les deux seuls moyens ?"),
        "cols_ei": dict(type="cols", g="Croissance extensive", gq="Plus de facteurs : plus de travail (emplois, heures), plus de capital (machines, logiciels).",
                        d="Croissance intensive", dq="Plus de productivité : plus de production avec les mêmes facteurs.", vs="ou"),
        "cols_prod": dict(type="cols", g="Productivité du travail", gq="Production ÷ quantité de travail (par emploi ou par heure).",
                          d="Productivité globale des facteurs", dq="Efficacité de la combinaison travail + capital : le reflet du progrès technique.", vs="≠"),
        "au_solow": dict(type="auteur", mono="RS", nom="Robert Solow", info="1924-2023 · Nobel 1987", cles=["progrès", "résidu"],
                         t="Accumuler du capital ne suffit pas : seul le progrès technique permet une croissance durable. Sa part mesurée, c'est le « résidu ».",
                         x=170, y=210, w=940),
        "an_solow": dict(type="sanim", nom="e1-solow", x=60, y=88, h=520, w=1160),
        "ill_res": dict(type="illu", nom="residu", x=110, y=120, w=1060, h=480),
        "def_pt": dict(type="def", terme="Progrès technique", cles=["innovations", "PGF"],
                       t="L'ensemble des innovations qui améliorent les produits, les procédés et l'organisation. Il fait augmenter la PGF.",
                       x=170, y=200, w=940),
        "an_gains": dict(type="sanim", nom="e1-gains", x=60, y=88, h=530, w=1160),
        "ch_pgf": dict(type="chaine", c=CHN["e1-pgf"], x=190, w=900),
    }),

    # ================================================================ III. le progrès technique endogène
    dict(id="endogene", chap="Un progrès technique endogène", fond="moutarde", humeur="lumiere",
         retenir="Progrès technique endogène : produit par la R&D (Romer : connaissances non rivales, externalités positives), "
                 "le capital humain (Lucas) et les dépenses publiques productives (Barro). La croissance finance l'innovation qui la relance.",
         beats=[
        "{q_end}Mais alors, d'où vient le progrès technique ?",
        "{-q_end}{cols_exo}{cols_exo.g}Chez Solow, il est {!exogène}exogène : il vient de l'extérieur du modèle, comme une manne tombée du ciel. "
        "{cols_exo.d}À partir des années mille neuf cent quatre-vingt, les théories de la croissance endogène disent l'inverse : "
        "le progrès technique est produit par des décisions économiques. Investir, chercher, former.",
        "{-cols_exo}{def_innov}D'abord, une définition à ne pas rater. L'innovation, c'est l'application économique d'une invention : "
        "un nouveau produit, un nouveau procédé, une nouvelle organisation, un nouveau débouché. "
        "{def_innov.1}L'invention, c'est la découverte. L'innovation, c'est sa mise sur le marché.",
        "{-def_innov}{ca_end}Les économistes mettent en avant trois sources d'innovation. {ca_end.1}Paul Romer : la recherche et développement. "
        "{ca_end.2}Robert Lucas : le capital humain. {ca_end.3}Robert Barro : les dépenses publiques productives.",
        "{-ca_end}{au_romer}Commençons par Romer, prix Nobel deux mille dix-huit. L'investissement en recherche produit des connaissances. "
        "Or une connaissance est {!non rivale}non rivale : l'utiliser n'empêche pas les autres de l'utiliser.",
        "Elle se diffuse, elle profite à d'autres entreprises. Ce sont des externalités positives. Et ce sont elles qui rendent les rendements croissants.",
        "Tu vois la différence avec Solow ? Une machine ne sert qu'à un ouvrier à la fois. Une idée peut servir à tout le monde, en même temps.",
        "{-au_romer}{au_lucas}Lucas, prix Nobel mille neuf cent quatre-vingt-quinze, insiste sur le capital humain : les connaissances et les compétences "
        "acquises par la formation et l'expérience. Elles rendent chacun plus productif. Et elles rendent aussi plus productifs ceux qui travaillent avec lui.",
        "{-au_lucas}{au_barro}Et pour Barro, les dépenses publiques productives, les infrastructures, la recherche publique, l'éducation, "
        "augmentent la productivité des entreprises privées.",
        "{-au_barro}{ch_endo}{ch_endo.1}Mets tout ça bout à bout, et tu obtiens un cercle vertueux. Au départ, de la croissance. "
        "{ch_endo.2}Donc les profits des entreprises et les recettes publiques augmentent. "
        "{ch_endo.3}Ce qui permet aux entreprises d'investir en recherche et développement, et à l'État de financer l'éducation, la recherche publique, les infrastructures.",
        "{ch_endo.4}Donc davantage d'innovations, et de capital humain. {ch_endo.5}Or les connaissances, non rivales, se diffusent : "
        "ce sont des externalités positives. {ch_endo.6}Donc la productivité globale des facteurs augmente… et il y a une nouvelle croissance.",
        "{ch_endo.boucle}Et regarde : la dernière étape relance la première. C'est pour ça qu'on dit que le progrès technique est "
        "{!endogène}endogène : il est produit par la croissance elle-même.",
        ("P", 1.2),
        "{-ch_endo}{ex_arn}Un exemple qui montre tout ça en action : les vaccins à ARN messager contre le Covid-19. "
        "{ex_arn.1}Ils arrivent sur le marché fin deux mille vingt, avec BioNTech et Pfizer, et avec Moderna. "
        "{ex_arn.2}Mais ils reposent sur des décennies de recherche, en grande partie publique et universitaire.",
        "{ex_arn.3}Les travaux de Katalin Karikó et Drew Weissman sur la modification de l'ARN datent de deux mille cinq. "
        "Ils leur ont valu le prix Nobel de médecine en deux mille vingt-trois. "
        "{ex_arn.4}Recherche publique, R et D privée, capital humain : c'est la croissance endogène en action.",
        "{-ex_arn}{cf_rd}Et en France, où en est l'effort de recherche ? {cf_rd.1}Deux virgule dix-huit pour cent du PIB, en deux mille vingt-trois. "
        "Soixante et un virgule cinq milliards d'euros de dépense intérieure de recherche et développement, dont environ deux tiers par les entreprises.",
        "{-cf_rd}{note_etat}Conséquence : l'État a un rôle à jouer. Car le marché, seul, sous-investit dans ce qui profite aussi aux autres. "
        "D'où le financement de la recherche fondamentale, de l'éducation, ou le crédit d'impôt recherche.",
        "{-note_etat}",
    ], vis={
        "q_end": dict(type="question", t="D'où vient le progrès technique ?"),
        "cols_exo": dict(type="cols", g="Exogène (Solow)", gq="Il vient de l'extérieur du modèle : une « manne tombée du ciel ».",
                         d="Endogène (années 1980)", dq="Il est produit par des décisions économiques : investir, chercher, former.", vs="→"),
        "def_innov": dict(type="def", terme="Innovation", cles=["application", "invention"],
                          t="Application économique d'une invention : nouveau produit, procédé, organisation ou débouché.",
                          etape="Invention = la découverte · innovation = sa mise sur le marché.", x=170, y=180, w=940),
        "ca_end": dict(type="cartes", items=[
            dict(ic="rd", t="Recherche", q="Paul Romer : la R&D produit des connaissances."),
            dict(ic="humain", t="Capital humain", q="Robert Lucas : formation et expérience."),
            dict(ic="infra", t="Dépenses publiques", q="Robert Barro : infrastructures, recherche publique, éducation.")]),
        "au_romer": dict(type="auteur", mono="PR", nom="Paul Romer", info="né en 1955 · Nobel 2018", cles=["rivale", "externalités"],
                         t="Une connaissance est non rivale : elle se diffuse et profite à d'autres entreprises (externalités positives), d'où des rendements croissants.",
                         x=170, y=210, w=940),
        "au_lucas": dict(type="auteur", mono="RL", nom="Robert Lucas", info="1937-2023 · Nobel 1995", cles=["capital"],
                         t="Le capital humain rend chacun plus productif, et rend plus productifs ceux qui travaillent avec lui.",
                         x=170, y=210, w=940),
        "au_barro": dict(type="auteur", mono="RB", nom="Robert Barro", info="né en 1944", cles=["dépenses"],
                         t="Les dépenses publiques productives (infrastructures, recherche publique, éducation) augmentent la productivité des entreprises privées.",
                         x=170, y=210, w=940),
        "ch_endo": dict(type="chaine", c=CHN["e1-endo"], x=170, w=940, boucle=True),
        "ex_arn": dict(type="liste", titre="Exemple · les vaccins à ARN messager", x=150, y=130, w=980, items=[
            "Fin 2020 : mis sur le marché par BioNTech-Pfizer et Moderna",
            "Des décennies de recherche, en grande partie publique et universitaire",
            "Karikó et Weissman, article de 2005 : Nobel de médecine 2023",
            "Recherche publique + R&D privée + capital humain"], marques=["1", "2", "3", "→"]),
        "cf_rd": dict(type="chiffres", x=170, y=170, w=940, items=[dict(n=CHIF[1]["n"], l=CHIF[1]["l"], s=CHIF[1]["s"])]),
        "note_etat": dict(type="note", titre="Le rôle de l'État", cles=["sous-investit", "recherche"],
                          t="Le marché seul sous-investit dans ce qui profite aussi aux autres : l'État finance recherche fondamentale, éducation, crédit d'impôt recherche.",
                          x=170, y=190, w=940),
    }),

    # ================================================================ IV. les institutions
    dict(id="institutions", chap="Les institutions, règles du jeu", fond="nuit", humeur="calme",
         retenir="Institutions : les « règles du jeu » (North). Droits de propriété, État de droit et brevets permettent à l'innovateur "
                 "de s'approprier ses gains : ils incitent à investir et à innover. Institutions inclusives ou extractives (Acemoglu et Robinson).",
         beats=[
        "{q_inst}Imagine : tu inventes un produit génial. Et le lendemain, on te le copie, sans rien te payer. "
        "Ou un pouvoir arbitraire te le confisque. Est-ce que tu investirais encore ?",
        "{-q_inst}{def_inst}Voilà pourquoi les institutions comptent. Les institutions, c'est l'ensemble des règles qui encadrent les comportements dans une société. "
        "{def_inst.1}Des règles formelles : la Constitution, les lois, les droits de propriété, les contrats. Et des règles informelles : les normes, les coutumes.",
        "Douglass North, prix Nobel en mille neuf cent quatre-vingt-treize, les appelle les {!règles du jeu}règles du jeu.",
        "{-def_inst}{ca_inst}Trois outils sont au cœur du mécanisme. {ca_inst.1}Les droits de propriété : le droit d'utiliser un bien, d'en tirer un revenu, de le céder. "
        "{ca_inst.2}Un État de droit qui les garantit. {ca_inst.3}Et le brevet : un monopole d'exploitation temporaire, vingt ans au plus, "
        "en échange de la publication de l'invention.",
        "{-ca_inst}{ch_inst}{ch_inst.1}La chaîne causale. Des droits de propriété garantis : les brevets, l'État de droit, une justice indépendante. "
        "{ch_inst.2}Donc l'innovateur peut s'approprier les gains de son innovation : une rente de monopole temporaire. "
        "{ch_inst.3}Donc il est incité à investir, et à prendre le risque d'innover.",
        "{ch_inst.4}Donc davantage d'innovations, de produit et de procédé. {ch_inst.5}Et donc des gains de productivité, de nouveaux marchés : de la croissance.",
        "{-ch_inst}{au_ar}Daron Acemoglu et James Robinson, prix Nobel deux mille vingt-quatre avec Simon Johnson, vont plus loin. "
        "Des institutions {!inclusives}inclusives, avec des droits de propriété pour tous, de la concurrence, un pouvoir politique partagé, "
        "favorisent la croissance. Des institutions extractives, qui permettent à une élite de capter les richesses, la bloquent.",
        "{-au_ar}{cols_coree}L'un de leurs exemples les plus célèbres : la Corée, divisée depuis la fin des années mille neuf cent quarante. "
        "Même peuple, même culture, même géographie au départ. "
        "{cols_coree.g}Au Sud : une économie de marché, devenue démocratique. Aujourd'hui, un pays riche et innovant. "
        "{cols_coree.d}Au Nord : une économie planifiée, sous dictature. L'un des pays les plus pauvres du monde.",
        "La différence ? Les institutions.",
        "{-cols_coree}{note_brev}Mais attention, la protection a un revers. Un brevet trop long, ou trop large, freine la diffusion des connaissances. "
        "Les institutions doivent donc arbitrer : {!inciter}inciter l'innovateur… et diffuser l'innovation.",
        "{-note_brev}",
    ], vis={
        "q_inst": dict(type="question", t="Copié dès le lendemain, ou confisqué : investirais-tu encore ?"),
        "def_inst": dict(type="def", terme="Institutions", cles=["règles"],
                         t="L'ensemble des règles qui encadrent les comportements dans une société : les « règles du jeu » (Douglass North, Nobel 1993).",
                         etape="Formelles : Constitution, lois, droits de propriété, contrats · informelles : normes, coutumes.", x=170, y=170, w=940),
        "ca_inst": dict(type="cartes", items=[
            dict(ic="loi", t="Droits de propriété", q="Utiliser un bien, en tirer un revenu, le céder."),
            dict(ic="usine", t="État de droit", q="Il garantit ces droits contre l'arbitraire."),
            dict(ic="brevet", t="Brevet", q="Un monopole temporaire (20 ans au plus) contre la publication.")]),
        "ch_inst": dict(type="chaine", c=CHN["e1-inst"], x=190, w=900),
        "au_ar": dict(type="auteur", mono="AR", nom="Acemoglu et Robinson", info="Nobel 2024 avec Simon Johnson", cles=["inclusives", "extractives"],
                      t="Des institutions inclusives favorisent la croissance ; des institutions extractives, qui permettent à une élite de capter les richesses, la bloquent.",
                      x=170, y=210, w=940),
        "cols_coree": dict(type="cols", g="Corée du Sud", gq="Économie de marché devenue démocratique : un pays riche et innovant.",
                           d="Corée du Nord", dq="Économie planifiée sous dictature : l'un des pays les plus pauvres du monde.", vs="≠",
                           repere="Même peuple, même culture, même géographie au départ"),
        "note_brev": dict(type="note", titre="Le revers de la protection", cles=["inciter", "diffuser"],
                          t="Un brevet trop long ou trop large freine la diffusion des connaissances : il faut arbitrer entre inciter et diffuser.",
                          x=170, y=200, w=940),
    }),

    # ================================================================ V. la destruction créatrice
    dict(id="destruction", chap="La destruction créatrice", fond="corail", humeur="tension",
         retenir="Destruction créatrice (Schumpeter, 1942) : l'innovation détruit des activités anciennes en en créant de nouvelles. "
                 "Aghion et Howitt, Nobel 2025. Un coût social réel, mais un déversement des emplois (Sauvy).",
         beats=[
        "{au_schum}Place à Joseph Schumpeter. Pour lui, le moteur du capitalisme, c'est l'entrepreneur innovateur. "
        "Les innovations majeures arrivent en grappes. Et elles provoquent une {!destruction créatrice}destruction créatrice : "
        "les activités nouvelles remplacent les anciennes. L'expression vient de son livre Capitalisme, socialisme et démocratie, en mille neuf cent quarante-deux.",
        "{-au_schum}{ch_dc}{ch_dc.1}Déroulons. Une innovation majeure apparaît : l'appareil photo numérique, puis le smartphone. "
        "{ch_dc.2}Et en même temps, deux choses se produisent. Création : de nouvelles entreprises, de nouveaux produits, de nouveaux emplois. "
        "Et destruction : des produits, des entreprises, des emplois anciens deviennent obsolètes.",
        "{ch_dc.3}Donc le travail et le capital se réallouent vers les activités les plus productives. "
        "{ch_dc.4}Et la productivité globale augmente : c'est la croissance à long terme. Mais avec des coûts pour les perdants : le chômage, la reconversion.",
        "{-ch_dc}{li_kodak}L'histoire de Kodak est presque trop belle. {li_kodak.1}Kodak, c'est le leader mondial de la pellicule photo. "
        "{li_kodak.2}Et c'est Kodak qui fabrique, dès mille neuf cent soixante-quinze, le premier prototype d'appareil photo numérique !",
        "{li_kodak.3}Mais l'entreprise tarde à basculer vers le numérique. {li_kodak.4}En janvier deux mille douze, elle se déclare en faillite aux États-Unis. "
        "Pendant ce temps, le numérique, puis le smartphone, créent de nouvelles entreprises et de nouveaux métiers.",
        "{-li_kodak}{au_ah}Cette idée a été couronnée tout récemment. Philippe Aghion et Peter Howitt, prix Nobel deux mille vingt-cinq, avec Joel Mokyr. "
        "Leur modèle de mille neuf cent quatre-vingt-douze fait de la destruction créatrice le cœur de la croissance : "
        "chaque innovation rend la précédente obsolète, et procure à son auteur une rente temporaire.",
        "{-au_ah}{note_dc}Mais la destruction créatrice a un coût social : des faillites, des licenciements, des reconversions difficiles, des territoires en déclin. "
        "D'où l'idée de politiques qui l'accompagnent, sans la bloquer : la formation, l'indemnisation du chômage, l'aide à la mobilité.",
        "{-note_dc}{def_dev}Et à long terme ? Alfred Sauvy parlait de {!déversement}déversement. "
        "Les gains de productivité suppriment des postes dans un secteur. Mais la hausse des revenus crée de nouveaux besoins… donc des emplois ailleurs.",
        "{-def_dev}",
    ], vis={
        "au_schum": dict(type="auteur", mono="JS", nom="Joseph Schumpeter", info="1883-1950 · Capitalisme, socialisme et démocratie, 1942",
                         cles=["entrepreneur", "grappes", "destruction"],
                         t="L'entrepreneur innovateur est le moteur du capitalisme. Les innovations arrivent en grappes et provoquent une « destruction créatrice ».",
                         x=170, y=210, w=940),
        "ch_dc": dict(type="chaine", c=CHN["e1-dc"], x=170, w=940),
        "li_kodak": dict(type="liste", titre="Exemple · Kodak", x=170, y=140, w=940, items=[
            "Leader mondial de la pellicule photo", "1975 : il fabrique le premier prototype d'appareil photo numérique",
            "Il tarde à basculer vers le numérique", "Janvier 2012 : faillite aux États-Unis"]),
        "au_ah": dict(type="auteur", mono="AH", nom="Philippe Aghion et Peter Howitt", info="Nobel 2025 avec Joel Mokyr", cles=["obsolète", "rente"],
                      t="Modèle de 1992 : chaque innovation rend la précédente obsolète et procure à son auteur une rente temporaire.",
                      x=170, y=210, w=940),
        "note_dc": dict(type="note", titre="Un coût social", cles=["accompagnent"],
                        t="Faillites, licenciements, reconversions, territoires en déclin : des politiques qui l'accompagnent sans la bloquer.",
                        x=170, y=200, w=940),
        "def_dev": dict(type="def", terme="Le déversement (Alfred Sauvy)", cles=["suppriment", "besoins"],
                        t="Les gains de productivité suppriment des postes dans un secteur, mais la hausse des revenus crée de nouveaux besoins, donc des emplois ailleurs.",
                        x=170, y=180, w=940),
    }),

    # ================================================================ VI. inégalités
    dict(id="inegalites", chap="Progrès technique et inégalités", fond="corail", humeur="mystere",
         retenir="Le progrès technique peut accroître les inégalités de revenus : biais en faveur du travail qualifié (course éducation / technologie, "
                 "Goldin et Katz), polarisation des emplois (Autor), rentes de l'innovation.",
         beats=[
        "{q_ineg}Le progrès technique enrichit le pays dans son ensemble. Mais enrichit-il tout le monde de la même façon ?",
        "{-q_ineg}{li_ineg}Non. Et trois mécanismes l'expliquent. {li_ineg.1}Un progrès technique biaisé en faveur du travail qualifié. "
        "{li_ineg.2}La polarisation des emplois. {li_ineg.3}Et les rentes de l'innovation.",
        "{-li_ineg}{cols_biais}Premier mécanisme. Les technologies numériques sont {cols_biais.g}complémentaires du travail qualifié : "
        "elles rendent un ingénieur, un analyste, un médecin plus productifs. {cols_biais.d}Et elles sont substituables au travail peu qualifié et répétitif : "
        "la machine peut le remplacer.",
        "{-cols_biais}{ch_biais}{ch_biais.1}La chaîne. Un progrès technique biaisé : le numérique, l'automatisation, l'intelligence artificielle. "
        "{ch_biais.2}Donc la demande de travail qualifié augmente, et celle de travail peu qualifié et routinier baisse.",
        "{ch_biais.3}Or, si l'offre de diplômés progresse moins vite que cette demande… {ch_biais.4}l'écart de salaire entre qualifiés et peu qualifiés se creuse. "
        "{ch_biais.5}Et les inégalités de revenus augmentent.",
        "{-ch_biais}{au_gk}C'est l'idée de Claudia Goldin et Lawrence Katz, dans un livre de deux mille huit sur la course entre l'éducation et la technologie. "
        "Une course, oui. Si l'offre de diplômés augmente plus vite que la demande de qualifications, les écarts se réduisent. "
        "Sinon, ils se creusent.",
        "{-au_gk}{ill_pol}Deuxième mécanisme : la {!polarisation}polarisation des emplois. "
        "L'automatisation remplace d'abord les tâches routinières, faciles à coder : la saisie, le guichet, le travail à la chaîne. "
        "{ill_pol.1}Ces emplois sont souvent au milieu de l'échelle des salaires. Et ils reculent.",
        "{ill_pol.2}Les emplois très qualifiés, et certains emplois peu qualifiés mais non routiniers, comme l'aide à domicile, la livraison ou la restauration, "
        "résistent mieux. L'emploi se polarise aux deux extrémités, et les salaires du milieu stagnent.",
        "L'économiste David Autor l'a documenté aux États-Unis. Et tu le vois autour de toi : caisses automatiques, banque en ligne, logiciels de comptabilité. "
        "Moins de caissiers et de guichetiers. Plus de développeurs et d'analystes de données.",
        "{-ill_pol}{def_rente}Troisième mécanisme : les rentes de l'innovation. L'innovateur qui réussit obtient un pouvoir de marché temporaire, "
        "par un brevet ou par un effet de réseau. Avec le numérique, un produit peut conquérir un marché mondial à coût presque nul. "
        "{def_rente.1}Le gagnant rafle presque tout. Et ces rentes nourrissent la hausse des très hauts revenus.",
        "{-def_rente}{note_fatal}Mais ces inégalités ne sont pas une fatalité. Leur ampleur dépend de l'éducation, de la formation continue, de la fiscalité, "
        "et de la concurrence, qui limite la durée des rentes. Philippe Aghion souligne d'ailleurs que les inégalités nées de l'innovation "
        "s'accompagnent souvent de davantage de mobilité sociale que les rentes héritées.",
        "{-note_fatal}",
    ], vis={
        "q_ineg": dict(type="question", t="Le progrès technique enrichit-il tout le monde de la même façon ?"),
        "li_ineg": dict(type="liste", titre="Trois mécanismes", x=170, y=180, w=940, items=[
            "Un progrès technique biaisé en faveur du travail qualifié", "La polarisation des emplois", "Les rentes de l'innovation"]),
        "cols_biais": dict(type="cols", g="Complémentaire", gq="du travail qualifié : ingénieur, analyste, médecin deviennent plus productifs.",
                           d="Substituable", dq="au travail peu qualifié et répétitif : la machine peut le remplacer.", vs="≠"),
        "ch_biais": dict(type="chaine", c=CHN["e1-biais"], x=170, w=940),
        "au_gk": dict(type="auteur", mono="GK", nom="Claudia Goldin et Lawrence Katz", info="The Race between Education and Technology, 2008",
                      cles=["course", "diplômés"],
                      t="Une course entre éducation et technologie : si l'offre de diplômés augmente plus vite que la demande de qualifications, les écarts se réduisent ; sinon, ils se creusent.",
                      x=170, y=210, w=940),
        "ill_pol": dict(type="illu", nom="polarisation", x=110, y=110, w=1060, h=540),
        "def_rente": dict(type="def", terme="Rentes de l'innovation", cles=["pouvoir", "marché"],
                          t="L'innovateur qui réussit obtient un pouvoir de marché temporaire (brevet, effet de réseau).",
                          etape="Avec le numérique, « le gagnant rafle presque tout » : la hausse des très hauts revenus.", x=170, y=180, w=940),
        "note_fatal": dict(type="note", titre="Pas une fatalité", cles=["éducation", "fiscalité", "concurrence"],
                           t="Leur ampleur dépend de l'éducation, de la formation continue, de la fiscalité et de la concurrence.",
                           x=170, y=200, w=940),
    }),

    # ================================================================ VII. limites écologiques
    dict(id="ecologie", chap="Les limites écologiques", fond="vert", humeur="calme",
         retenir="Limites : épuisement des ressources, pollution, réchauffement. L'innovation peut les reculer (France 1990-2025 : PIB +69 %, "
                 "GES −34,3 %), mais effet rebond (Jevons) et débat soutenabilité faible / forte.",
         beats=[
        "{def_sout}Dernière grande question : la croissance peut-elle durer sur une planète finie ? "
        "Une croissance soutenable, c'est une croissance qui répond aux besoins du présent sans compromettre la capacité des générations futures à répondre aux leurs. "
        "{def_sout.1}Elle suppose de transmettre un stock de capital : physique, humain, naturel, institutionnel.",
        "{-def_sout}{def_cn}Et le capital naturel, c'est l'ensemble des ressources naturelles qui rendent des services à l'économie : "
        "les sols, l'eau, les forêts, les énergies fossiles, les minerais, la biodiversité, un climat stable.",
        "{-def_cn}{ca_lim}Produire, c'est prélever des ressources et rejeter des déchets. La croissance se heurte donc à trois limites, "
        "que le programme cite explicitement. {ca_lim.1}L'épuisement des ressources : le pétrole, le gaz, les minerais, "
        "et la surexploitation des forêts, des poissons, des nappes d'eau. {ca_lim.2}La pollution de l'air, de l'eau et des sols. "
        "{ca_lim.3}Et le réchauffement climatique, dû aux émissions de gaz à effet de serre.",
        "{-ca_lim}{ch_lim}{ch_lim.1}La chaîne. Croissance de la production et de la consommation. "
        "{ch_lim.2}Donc plus de prélèvements, et plus de rejets. "
        "{ch_lim.3}Donc épuisement des ressources, pollution, réchauffement.",
        "{ch_lim.4}Donc le capital naturel se dégrade. {ch_lim.5}Et la croissance future est menacée : catastrophes, pénuries, coûts de réparation.",
        "{-ch_lim}{au_mead}L'alerte date de mille neuf cent soixante-douze, avec le rapport Meadows sur les limites de la croissance, écrit pour le Club de Rome par une équipe menée par Donella et Dennis Meadows. "
        "Sa thèse : dans un monde fini, si les tendances se poursuivent, une croissance exponentielle de la production et de la population mène à l'épuisement des ressources, et à une pollution croissante.",
        "{-au_mead}{def_ext}Pourquoi le marché ne règle-t-il pas ça tout seul ? Parce que ces dommages sont des {!externalités négatives}externalités négatives : "
        "le pollueur ne paie pas le coût qu'il impose aux autres. Donc le marché, seul, produit trop de pollution.",
        "{-def_ext}{li_inno}La bonne nouvelle : l'innovation peut reculer ces limites. {li_inno.1}Elle améliore l'efficacité : produire autant avec moins d'énergie "
        "et de matières. {li_inno.2}Elle permet des substitutions : les renouvelables et le nucléaire à la place des fossiles. "
        "{li_inno.3}Et elle permet de réparer, ou de capter : la dépollution, le captage du carbone, encore peu développé.",
        "{-li_inno}{gr_dec}Et ça marche ? Regarde la France, entre mille neuf cent quatre-vingt-dix et deux mille vingt-cinq. "
        "{gr_dec.1}Le PIB en volume augmente d'environ soixante-neuf pour cent. {gr_dec.2}Et les émissions de gaz à effet de serre baissent de trente-quatre virgule trois pour cent. "
        "Les sources : l'Insee et le Citepa.",
        "C'est un {!découplage}découplage absolu : les émissions baissent pendant que le PIB augmente. "
        "Un découplage relatif, ce serait des émissions qui augmentent, mais moins vite que le PIB.",
        "{-gr_dec}{note_emp}Mais attention au piège. Ces émissions sont mesurées sur le territoire. Elles ne comptent pas les gaz émis à l'étranger "
        "pour fabriquer les biens que la France importe. L'empreinte carbone, qui les inclut, est plus élevée, et sa baisse doit être vérifiée séparément.",
        "{-note_emp}{ch_reb}{ch_reb.1}Et l'innovation a une autre limite, plus surprenante : l'effet rebond. "
        "Une innovation améliore l'efficacité énergétique : un moteur plus sobre, l'éclairage LED. "
        "{ch_reb.2}Donc moins d'énergie consommée par unité produite ou utilisée. {ch_reb.3}Donc le coût d'usage baisse.",
        "{ch_reb.4}Donc on utilise davantage le bien : plus de kilomètres, plus d'équipements. "
        "{ch_reb.5}Et les économies d'énergie sont en partie, voire totalement, annulées.",
        "{-ch_reb}{au_jev}Le premier à l'avoir vu ? William Stanley Jevons, en mille huit cent soixante-cinq, dans un livre sur la question du charbon. "
        "Les machines à vapeur plus économes en charbon ont fait augmenter… la consommation totale de charbon en Angleterre. "
        "C'est le paradoxe de Jevons : la forme extrême de l'effet rebond.",
        "{-au_jev}{cmp_sout}D'où un débat entre deux conceptions de la soutenabilité. "
        "{cmp_sout.1}Pour la soutenabilité faible, les capitaux sont substituables : plus de capital physique, humain ou technologique compense le capital naturel perdu. "
        "Pour la soutenabilité forte, une partie du capital naturel est irremplaçable : le climat, la biodiversité.",
        "{cmp_sout.2}L'innovation ? Centrale pour la première. Insuffisante seule pour la seconde : il faut aussi des normes, des quotas, une sobriété.",
        "{cmp_sout.3}Et la conséquence. D'un côté, la croissance peut continuer si l'on investit assez. "
        "De l'autre, certaines productions doivent baisser : la croissance doit changer de contenu.",
        "{-cmp_sout}",
    ], vis={
        "def_sout": dict(type="def", terme="Croissance soutenable", cles=["besoins", "générations"],
                         t="Elle répond aux besoins du présent sans compromettre la capacité des générations futures à répondre aux leurs.",
                         etape="Elle suppose de transmettre un stock de capital : physique, humain, naturel, institutionnel.", x=170, y=170, w=940),
        "def_cn": dict(type="def", terme="Capital naturel", cles=["ressources", "services"],
                       t="Les ressources naturelles qui rendent des services à l'économie : sols, eau, forêts, énergies fossiles, minerais, biodiversité, climat stable.",
                       x=170, y=190, w=940),
        "ca_lim": dict(type="cartes", items=[
            dict(ic="ressource", t="Épuisement", q="Pétrole, gaz, minerais ; forêts, poissons, nappes d'eau surexploités."),
            dict(ic="pollution", t="Pollution", q="De l'air, de l'eau et des sols."),
            dict(ic="climat", t="Réchauffement", q="Dû aux émissions de gaz à effet de serre.")]),
        "ch_lim": dict(type="chaine", c=CHN["e1-limites"], x=170, w=940),
        "au_mead": dict(type="auteur", mono="DM", nom="Donella et Dennis Meadows", info="The Limits to Growth, rapport au Club de Rome, 1972",
                        cles=["fini", "exponentielle"],
                        t="Dans un monde fini, si les tendances se poursuivent, une croissance exponentielle de la production et de la population mène à l'épuisement des ressources et à une pollution croissante.",
                        x=170, y=210, w=940),
        "def_ext": dict(type="def", terme="Externalité négative", cles=["pollueur", "coût"],
                        t="Le pollueur ne paie pas le coût qu'il impose aux autres : le marché seul produit trop de pollution.",
                        x=170, y=200, w=940),
        "li_inno": dict(type="cartes", items=[
            dict(ic="efficacite", t="Efficacité", q="Moins d'énergie et de matières : moteurs sobres, isolation, recyclage."),
            dict(ic="substitution", t="Substitution", q="Renouvelables et nucléaire à la place des fossiles ; matériaux nouveaux."),
            dict(ic="capter", t="Réparer, capter", q="Dépollution, captage du carbone (encore peu développé).")]),
        "gr_dec": dict(type="donnees", g=G["e1-decouplage"], x=110, y=100, w=1060, h=520, lab=330),
        "note_emp": dict(type="note", titre="Territoire ou empreinte ?", cles=["territoire", "empreinte"],
                         t="Les émissions sont mesurées sur le territoire ; l'empreinte carbone, qui compte les importations, est plus élevée.",
                         x=170, y=200, w=940),
        "ch_reb": dict(type="chaine", c=CHN["e1-rebond"], x=170, w=940),
        "au_jev": dict(type="auteur", mono="WJ", nom="William Stanley Jevons", info="1835-1882 · The Coal Question, 1865", cles=["charbon", "paradoxe"],
                       t="Des machines à vapeur plus économes en charbon ont fait augmenter la consommation totale de charbon : le « paradoxe de Jevons ».",
                       x=170, y=210, w=940),
        "cmp_sout": dict(type="compare", titre="Deux conceptions de la soutenabilité", x=80, y=96, w=1120,
                         cols=["Soutenabilité faible", "Soutenabilité forte"], lignes=[
                             ["Idée", "Les capitaux sont substituables : plus de capital physique, humain, technologique compense le capital naturel perdu.",
                              "Une partie du capital naturel est critique et irremplaçable (climat, biodiversité)."],
                             ["Innovation", "Centrale : le progrès technique reculera les limites.", "Insuffisante seule : normes, quotas, sobriété."],
                             ["Conséquence", "La croissance peut continuer si l'on investit assez.", "Certaines productions doivent baisser : la croissance change de contenu."]]),
    }),

    # ================================================================ VIII. pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="nuit", humeur="tension", beats=[
        "{cmp_p1}Avant le bac, sept pièges qui coûtent des points. {cmp_p1.1}Un : « le PIB a augmenté de trois pour cent, donc la production aussi ». "
        "Seulement si c'est le PIB en volume ! En valeur, une partie de la hausse peut venir des prix.",
        "{cmp_p1.2}Deux : confondre la productivité du travail et la productivité globale des facteurs. C'est la PGF qui reflète le progrès technique.",
        "{cmp_p1.3}Trois : invention et innovation, ce n'est pas pareil. L'invention est une découverte. L'innovation, sa mise en œuvre économique.",
        "{cmp_p1.4}Quatre : endogène ne veut pas dire « qui vient de l'intérieur du pays ». Endogène, ça veut dire expliqué par le modèle : "
        "produit par des décisions économiques, comme investir en recherche ou en éducation.",
        "{-cmp_p1}{cmp_p2}{cmp_p2.1}Cinq : la destruction créatrice, ce n'est pas seulement la disparition d'emplois. C'est un processus double : "
        "des activités disparaissent pendant que d'autres apparaissent.",
        "{cmp_p2.2}Six : « le progrès technique crée du chômage, donc il réduit la croissance ». Non : à long terme, c'est le déversement de Sauvy. "
        "Les coûts sont réels, mais concentrés sur certains travailleurs et certains territoires.",
        "{cmp_p2.3}Et sept : « la France a découplé, le problème climatique est réglé ». Non plus. Ce sont les émissions territoriales. "
        "Il faut aussi regarder l'empreinte, et le rythme : l'objectif, c'est moins cinquante pour cent en deux mille trente par rapport à mille neuf cent quatre-vingt-dix.",
        "{-cmp_p2}",
    ], vis={
        "cmp_p1": dict(type="compare", titre="Les pièges · 1 à 4", x=70, y=86, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["1 · Volume", "« Le PIB a augmenté de 3 %, donc la production aussi. »", "Seulement en volume : en valeur, une partie de la hausse vient des prix."],
            ["2 · Productivité", "Confondre productivité du travail et PGF.", "La PGF mesure l'efficacité de la combinaison travail + capital."],
            ["3 · Innovation", "« Invention et innovation, c'est pareil. »", "Invention = découverte ; innovation = sa mise en œuvre économique."],
            ["4 · Endogène", "« Endogène : qui vient de l'intérieur du pays. »", "Expliqué par le modèle : produit par des décisions économiques."]]),
        "cmp_p2": dict(type="compare", titre="Les pièges · 5 à 7", x=70, y=96, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["5 · Destruction créatrice", "« C'est la disparition d'emplois. »", "Un processus double : des activités disparaissent, d'autres apparaissent."],
            ["6 · Chômage", "« Le progrès technique crée du chômage, donc il réduit la croissance. »", "À long terme, déversement (Sauvy) ; des coûts réels mais concentrés."],
            ["7 · Découplage", "« La France a découplé : c'est réglé. »", "Émissions territoriales seulement ; voir l'empreinte et le rythme (−50 % en 2030 par rapport à 1990)."]]),
    }),

    # ================================================================ IX. au bac
    dict(id="epreuve", chap="Ce chapitre au bac", fond="canard", humeur="lumiere", beats=[
        "{li_ep}Passons au bac. L'écrit de SES dure quatre heures, au coefficient seize. Et tu choisis entre deux sujets. "
        "Soit l'épreuve composée, en trois parties : {li_ep.1}la mobilisation des connaissances, sur trois virgule cinq points, "
        "{li_ep.2}l'étude d'un document, sur cinq virgule cinq points, {li_ep.3}et le raisonnement sur un dossier documentaire, sur neuf points. "
        "{li_ep.4}Soit la dissertation, appuyée sur un dossier documentaire.",
        "Ce barème s'applique à partir de la session deux mille vingt-sept. Et dans les deux sujets, deux points sur vingt sont réservés à l'orthographe et à la syntaxe.",
        "Bonne nouvelle : la croissance fait partie des neuf questions du programme qui peuvent tomber à l'écrit.",
        "{-li_ep}{li_aei}Une méthode revient partout, dans toutes les parties : le paragraphe {!AEI}A, E, I. "
        "{li_aei.1}A : affirmer l'idée. {li_aei.2}E : expliquer le mécanisme, avec une chaîne causale, comme celles de ce chapitre. "
        "{li_aei.3}I : illustrer, par un exemple précis, chiffré ou daté.",
        "Mais d'abord, un savoir-faire indispensable pour la partie deux : calculer.",
        "{-li_aei}",
    ], vis={
        "li_ep": dict(type="liste", titre="L'écrit de SES · 4 heures · coefficient 16", x=150, y=120, w=980, items=[
            "Partie 1 · Mobilisation des connaissances : 3,5 points", "Partie 2 · Étude d'un document : 5,5 points",
            "Partie 3 · Raisonnement sur un dossier documentaire : 9 points", "Ou : la dissertation, appuyée sur un dossier documentaire"],
            marques=["1", "2", "3", "D"]),
        "li_aei": dict(type="liste", titre="Le paragraphe AEI", x=170, y=170, w=940, items=[
            "Affirmer l'idée", "Expliquer le mécanisme : une chaîne causale", "Illustrer : un exemple précis, chiffré ou daté"],
            marques=["A", "E", "I"]),
    }),

    # ================================================================ X. savoir-faire : calculer avec le PIB
    # 999,1 / 309,1 = 3,232 ; 2 504,6 / 2 233,0 = 1,1216 ; (2 646,7 − 2 625,6) / 2 625,6 = 0,80 % (exercice du site, données Insee)
    dict(id="calcul", chap="Savoir-faire · calculer avec le PIB", fond="nuit", humeur="calme", beats=[
        "{ex_c}Voici un exercice, avec les vraies données de l'Insee. Le PIB de la France en volume, en milliards d'euros de deux mille vingt. "
        "Trois questions. Un : calcule le coefficient multiplicateur entre mille neuf cent cinquante et mille neuf cent soixante-treize, "
        "puis entre deux mille sept et deux mille dix-neuf. Deux : calcule le taux de croissance de deux mille vingt-cinq. "
        "Trois : rédige une phrase sur la croissance des Trente Glorieuses.",
        "Et attention : les sujets récents interdisent la calculatrice. Entraîne-toi à calculer à la main.",
        "{-ex_c}{pa_c}À toi. Mets la vidéo sur pause, prends une feuille, et fais les trois calculs.",
        "{pa_c.stop}{-pa_c}{ex_cc}{ex_cc.q1}Correction. {s_c1}{s_c1.1}Un coefficient multiplicateur, c'est la valeur d'arrivée divisée par la valeur de départ. "
        "{s_c1.2}Neuf cent quatre-vingt-dix-neuf virgule un, divisé par trois cent neuf virgule un. À la main : trois fois trois cent neuf, ça fait neuf cent vingt-sept. "
        "Il reste soixante-douze, un peu moins d'un quart de trois cent neuf. Environ trois virgule vingt-trois : le PIB a été multiplié par trois virgule deux en vingt-trois ans.",
        "{s_c1.3}Entre deux mille sept et deux mille dix-neuf : deux mille cinq cent quatre virgule six, divisé par deux mille deux cent trente-trois. Deux mille deux cent trente-trois fois un virgule un, ça fait environ deux mille quatre cent cinquante-six ; il reste une cinquantaine, encore deux pour cent environ. Donc environ un virgule douze. Plus douze pour cent… en douze ans seulement.",
        "{-s_c1}{ex_cc.q2}{s_c2}{s_c2.1}Deux : un taux de variation, c'est l'arrivée moins le départ, divisé par le départ, fois cent. "
        "{s_c2.2}L'écart vaut vingt et un virgule un milliards. Rapporté à deux mille six cent vingt-cinq virgule six. Un pour cent, ce serait environ vingt-six milliards ; vingt et un, c'est un peu plus des trois quarts de vingt-six. Donc environ plus zéro virgule huit pour cent.",
        "{-s_c2}{ex_cc.q3}{s_c3}{s_c3.1}Trois : la racine vingt-troisième est donnée, un virgule zéro cinquante-deux. Donc cinq virgule deux pour cent par an. "
        "{s_c3.2}La phrase : « Entre mille neuf cent cinquante et mille neuf cent soixante-treize, selon l'Insee, le PIB de la France en volume a crû en moyenne "
        "d'environ cinq virgule deux pour cent par an : il a été multiplié par trois virgule deux. »",
        "{s_c3.3}Et retiens la méthode : pour comparer deux périodes de longueurs différentes, on compare des taux annuels moyens, pas des taux globaux.",
        "{-s_c3}{-ex_cc}",
    ], vis={
        "ex_c": dict(type="exo", niveau="calcul", titre="Calculer avec le PIB", src="Exercice du site, données Insee", y=80,
                     enonce=["PIB de la France en volume (milliards d'euros 2020) : 1950 : 309,1 · 1973 : 999,1 · 2007 : 2 233,0 · "
                             "2019 : 2 504,6 · 2024 : 2 625,6 · 2025 : 2 646,7."],
                     questions=["Calcule le coefficient multiplicateur entre 1950 et 1973, puis entre 2007 et 2019.",
                                "Calcule le taux de croissance de 2025.",
                                "Sachant que (999,1 / 309,1)^{1/23} ≈ 1,052, rédige une phrase sur la croissance des Trente Glorieuses."]),
        "pa_c": dict(type="pause", t="Deux coefficients multiplicateurs, un taux de croissance, une phrase."),
        "ex_cc": dict(type="exo", mode="coin", niveau="calcul", titre="Calculer avec le PIB",
                      donnees=["1950 : 309,1", "1973 : 999,1", "2007 : 2 233,0", "2019 : 2 504,6", "2024 : 2 625,6", "2025 : 2 646,7"],
                      questions=["Coefficients multiplicateurs ?", "Taux de 2025 ?", "Phrase sur 1950-1973 ?"]),
        "s_c1": dict(type="formule", titre="1 · Coefficients multiplicateurs", x=540, y=140, w=700, lignes=[
            dict(f="CM = arrivée ÷ départ", taille=36),
            dict(f="999,1 ÷ 309,1 ≈ 3,23", cadre=True, taille=36, n="multiplié par 3,2 en 23 ans"),
            dict(f="2 504,6 ÷ 2 233,0 ≈ 1,12", cadre=True, taille=36, n="+12 % en 12 ans seulement")]),
        "s_c2": dict(type="formule", titre="2 · Le taux de croissance de 2025", x=540, y=170, w=700, lignes=[
            dict(f="taux = " + "[[arrivée − départ|départ]]" + " × 100", taille=36),
            dict(f="[[2 646,7 − 2 625,6|2 625,6]]" + " × 100 ≈ +0,8 %", cadre=True, taille=36)]),
        "s_c3": dict(type="formule", titre="3 · La phrase", x=540, y=110, w=700, lignes=[
            dict(f="1,052 → +5,2 % par an en moyenne", taille=34),
            dict(f="« Entre 1950 et 1973, selon l'Insee, le PIB de la France en volume a crû en moyenne d'environ 5,2 % par an : "
                   "il a été multiplié par 3,2. »", txt=True),
            dict(f="Deux périodes de longueurs différentes : on compare des taux annuels moyens.", txt=True, pt=True)]),
    }),

    # ================================================================ XI. partie 1
    dict(id="partie1", chap="Partie 1 · mobiliser ses connaissances", fond="canard", humeur="tension", beats=[
        "{ex_p1}Partie un de l'épreuve composée : la mobilisation des connaissances. Une question, sans document. Le sujet : "
        "« Montrez que les institutions peuvent favoriser la croissance économique. » Trois virgule cinq points, une vingtaine de lignes.",
        "{ex_p1.1}La méthode. Repère le verbe : « montrez que », c'est un mécanisme qui va dans un sens. Pas de discussion ! "
        "{ex_p1.2}Définis les notions du sujet en une phrase. {ex_p1.3}Puis deux paragraphes A, E, I, bien séparés.",
        "{-ex_p1}{pa_p1}À toi. Mets sur pause, et rédige : deux définitions, deux mécanismes, deux exemples.",
        "{pa_p1.stop}{-pa_p1}{ex_p1c}{ex_p1c.q1}Correction. {s_p11}{s_p11.1}On commence par définir. Les institutions sont, selon Douglass North, "
        "les règles du jeu d'une société, formelles ou informelles. {s_p11.2}La croissance, c'est l'augmentation durable de la production.",
        "{-s_p11}{ex_p1c.q2}{s_p12}Premier paragraphe. {s_p12.1}A : des droits de propriété garantis incitent à innover. "
        "{s_p12.2}E : le brevet accorde à l'innovateur un monopole d'exploitation temporaire. Il peut s'approprier les gains de son invention, "
        "donc il est incité à investir en recherche et développement. Les innovations augmentent la productivité globale des facteurs, donc la croissance. "
        "{s_p12.3}Et sans cette protection ? L'innovation serait copiée sans contrepartie, et personne ne prendrait le risque de la financer.",
        "{-s_p12}{ex_p1c.q3}{s_p13}Deuxième paragraphe. {s_p13.1}A : des institutions inclusives favorisent l'investissement de tous. "
        "{s_p13.2}E : selon Acemoglu et Robinson, quand l'État de droit protège chacun contre l'arbitraire et que la concurrence est ouverte, "
        "entrepreneurs et ménages investissent, car leurs gains futurs sont sûrs. À l'inverse, des institutions extractives captent la richesse au profit d'une élite. "
        "{s_p13.3}I : la Corée du Sud, riche et innovante, et la Corée du Nord, restée très pauvre : deux populations au départ comparables.",
        "{-s_p13}{ex_p1c.q4}{s_p14}{s_p14.1}Le barème indicatif : les définitions, zéro virgule cinq point. {s_p14.2}Les deux mécanismes expliqués, deux points. "
        "{s_p14.3}Les exemples précis, un point.",
        "{-s_p14}{-ex_p1c}",
    ], vis={
        "ex_p1": dict(type="exo", niveau="p1", titre="Montrez que les institutions peuvent favoriser la croissance économique.",
                      src="Sujet inventé pour le site · 3,5 points · sans document",
                      enonce=["Une vingtaine de lignes, qui répondent exactement à la consigne."],
                      questions=["Repérer le verbe : « montrez que » = un mécanisme, dans un sens", "Définir les notions du sujet",
                                 "Deux paragraphes AEI, bien séparés"]),
        "pa_p1": dict(type="pause", t="Deux définitions, deux mécanismes, deux exemples."),
        "ex_p1c": dict(type="exo", mode="coin", niveau="p1", titre="Les institutions et la croissance",
                       questions=["Définir", "Paragraphe 1 : droits de propriété", "Paragraphe 2 : institutions inclusives", "Barème"]),
        "s_p11": dict(type="liste", titre="Définir", x=540, y=150, w=700, petit=True, items=[
            "Institutions : les « règles du jeu », formelles ou informelles (North)",
            "Croissance : l'augmentation durable de la production"]),
        "s_p12": dict(type="liste", titre="Paragraphe 1 · les droits de propriété", x=540, y=120, w=700, petit=True, items=[
            "A · Des droits de propriété garantis incitent à innover",
            "E · Brevet → monopole temporaire → gains appropriés → R&D → innovations → PGF → croissance",
            "Sans protection : copie sans contrepartie, personne ne finance le risque"], marques=["A", "E", "+"]),
        "s_p13": dict(type="liste", titre="Paragraphe 2 · les institutions inclusives", x=540, y=120, w=700, petit=True, items=[
            "A · Des institutions inclusives favorisent l'investissement de tous",
            "E · État de droit + concurrence → gains futurs sûrs → on investit ; institutions extractives : une élite capte",
            "I · Corée du Sud riche et innovante / Corée du Nord très pauvre"], marques=["A", "E", "I"]),
        "s_p14": dict(type="liste", titre="Barème indicatif", x=540, y=180, w=700, petit=True, items=[
            "Définitions : 0,5 point", "Deux mécanismes expliqués : 2 points", "Exemples précis : 1 point"]),
    }),

    # ================================================================ XII. partie 2
    # valeurs lues dans GRAPHES["e1-pib"] : 1960 8,0 ; 1969 7,1 ; 2012 0,2 ; 2017 2,1 ; moyenne 2010-2019 1,4 %
    dict(id="partie2", chap="Partie 2 · étudier un document", fond="nuit", humeur="tension", beats=[
        "{ex_p2}Partie deux : l'étude d'un document. Cinq virgule cinq points. Le document, tu le connais : le taux de croissance du PIB de la France en volume, "
        "de mille neuf cent cinquante à deux mille vingt-cinq, d'après l'Insee. Deux questions.",
        "{ex_p2.1}Un : à l'aide du document, compare la croissance de mille neuf cent cinquante à mille neuf cent soixante-treize à celle des années deux mille dix. "
        "{ex_p2.2}Deux : à l'aide du document et de tes connaissances, montre que le ralentissement de la croissance peut s'expliquer par celui des gains de productivité.",
        "{-ex_p2}{gr_doc}Avant tout chiffre : lis le titre, la source, l'unité, la date. Ici, des pourcentages de variation par rapport à l'année précédente.",
        "{-gr_doc}{pa_p2}À toi. Mets sur pause : des données précises pour la question un, un mécanisme pour la question deux.",
        "{pa_p2.stop}{-pa_p2}{ex_p2c}{ex_p2c.q1}{gr_q1}Correction de la question un. Il faut des données précises, avec l'année, l'unité et la source. "
        "{gr_q1.1}{s_p21}{s_p21.1}Selon l'Insee, la croissance du PIB en volume dépasse le plus souvent quatre pour cent par an entre mille neuf cent cinquante et mille neuf cent soixante-treize : "
        "huit pour cent en mille neuf cent soixante, sept virgule un pour cent en mille neuf cent soixante-neuf. Cinq virgule deux pour cent par an en moyenne.",
        "{gr_q1.2}{s_p21.2}Dans les années deux mille dix, elle reste toujours sous deux virgule cinq pour cent : zéro virgule deux en deux mille douze, "
        "deux virgule un en deux mille dix-sept. {s_p21.3}En moyenne, un virgule quatre pour cent par an de deux mille dix à deux mille dix-neuf : près de quatre fois moins.",
        "{-s_p21}{-gr_q1}{ex_p2c.q2}{s_p22}Question deux : un mécanisme, relié au document. {s_p22.1}La croissance intensive repose sur la hausse de la productivité globale des facteurs. "
        "{s_p22.2}Pendant les Trente Glorieuses, la France rattrape son retard technologique sur les États-Unis : elle adopte des techniques déjà inventées, "
        "la production de masse, la mécanisation agricole. D'où des gains de productivité très rapides, et une croissance forte.",
        "{s_p22.3}Une fois le rattrapage achevé, il faut innover soi-même, ce qui est plus lent. Et la tertiarisation pèse aussi : "
        "les gains de productivité sont plus difficiles dans beaucoup de services. {s_p22.4}Moins de gains de productivité, c'est moins de baisse des coûts, "
        "moins de demande : la croissance ralentit. Exactement ce que montre le document après mille neuf cent soixante-quatorze, et surtout après deux mille huit.",
        "{-s_p22}{-ex_p2c}",
    ], vis={
        "ex_p2": dict(type="exo", niveau="p2", titre="La croissance française depuis 1950", src="Exercice du site, document Insee · 5,5 points",
                      enonce=["Document : « Taux de croissance du PIB de la France en volume, 1950-2025 » (Insee)."],
                      questions=["À l'aide du document, comparez la croissance de 1950-1973 à celle des années 2010.",
                                 "À l'aide du document et de vos connaissances, montrez que le ralentissement de la croissance peut s'expliquer par celui des gains de productivité."]),
        "gr_doc": dict(type="donnees", g=G["e1-pib"], kicker="Document · partie 2", x=60, y=74, w=1160, h=600,
                       phases=[dict(de=1950, a=2025, dur=3.2)]),
        "pa_p2": dict(type="pause", t="Question 1 : des données précises. Question 2 : un mécanisme relié au document."),
        "ex_p2c": dict(type="exo", mode="coin", niveau="p2", titre="La croissance française",
                       questions=["Comparer 1950-1973 et les années 2010", "Expliquer par les gains de productivité"]),
        "gr_q1": dict(type="donnees", g=G["e1-pib"], kicker="Le document", titre="Croissance du PIB en volume (Insee)", sous=False,
                      src="Source : Insee, comptes nationaux annuels, base 2020.", x=530, y=66, w=720, h=340, phases=[dict(de=1950, a=1973, moy=5.2, dur=2.5), dict(de=2010, a=2019, moy=1.4, dur=1.5, lp=[2014, 5])]),
        "s_p21": dict(type="liste", titre="Question 1 · comparer", x=540, y=424, w=700, petit=True, items=[
            "1950-1973 : souvent > 4 % (8,0 % en 1960, 7,1 % en 1969)",
            "Années 2010 : toujours < 2,5 % (0,2 % en 2012)",
            "5,2 %/an contre 1,4 %/an : près de quatre fois moins"]),
        "s_p22": dict(type="liste", titre="Question 2 · le mécanisme", x=540, y=110, w=700, petit=True, items=[
            "Croissance intensive = hausse de la PGF",
            "Trente Glorieuses : rattrapage des États-Unis, techniques déjà inventées → gains rapides",
            "Puis innover soi-même, plus lent ; tertiarisation",
            "Moins de gains → moins de baisse des coûts, de pouvoir d'achat, de demande → croissance plus faible"]),
    }),

    # ================================================================ XIII. partie 3
    dict(id="partie3", chap="Partie 3 · raisonner sur un dossier", fond="moutarde", humeur="tension", beats=[
        "{ex_p3}Partie trois : le raisonnement sur un dossier documentaire. Neuf points, la plus grosse. Le sujet : "
        "« À l'aide du dossier, montrez que l'innovation est une source de croissance économique. »",
        "{ex_p3.p1}Trois documents. L'effort de recherche de la France. {ex_p3.p2}Le graphique de la croissance française. "
        "{ex_p3.p3}Et la mise au point des vaccins à ARN messager.",
        "On attend une introduction, un développement organisé, une conclusion. Et chaque paragraphe s'appuie sur au moins un document, cité précisément.",
        "{-ex_p3}{pa_p3}À toi. Mets sur pause et construis le plan : deux ou trois idées, chacune avec son mécanisme et son document.",
        "{pa_p3.stop}{-pa_p3}{li_p3}Correction. {li_p3.1}En introduction : on définit l'innovation, l'application économique d'une invention, et la croissance. "
        "Puis on annonce : l'innovation stimule la croissance parce qu'elle accroît la productivité, puis parce qu'elle crée de nouveaux produits et entretient un cercle vertueux.",
        "{li_p3.2}Un : l'innovation accroît la productivité globale des facteurs. On produit plus avec autant de facteurs, les coûts baissent, la demande augmente. "
        "Le document deux montre une croissance forte quand les gains de productivité étaient élevés : cinq virgule deux pour cent par an pendant les Trente Glorieuses. "
        "Et Solow : le résidu.",
        "{li_p3.3}Deux : l'innovation crée de nouveaux produits et de nouveaux marchés. C'est la destruction créatrice de Schumpeter : "
        "de nouvelles activités, de nouveaux emplois, de nouveaux investissements. Document trois : les vaccins à ARN, de nouveaux produits, une nouvelle industrie.",
        "{li_p3.4}Trois : un cercle vertueux, la croissance finance l'innovation. La croissance endogène : la recherche avec Romer, le capital humain avec Lucas, "
        "la recherche publique avec Barro. Document un : soixante et un virgule cinq milliards d'euros de R et D en deux mille vingt-trois. "
        "Et le document trois montre que la recherche publique a précédé l'innovation privée : des externalités.",
        "{li_p3.5}En conclusion : l'innovation est une source majeure de croissance, par la productivité et par de nouveaux marchés. Et la croissance lui fournit, en retour, ses moyens.",
        "{-li_p3}{note_p3}Et une règle d'or : pas de partie « limites » ! On ne discute pas un « montrez que ». On le démontre.",
        "{-note_p3}",
    ], vis={
        "ex_p3": dict(type="exo", niveau="p3", titre="Montrez que l'innovation est une source de croissance économique.",
                      src="Sujet inventé pour le site · 9 points", y=80,
                      enonce=["Document 1 : effort de recherche de la France, 2,18 % du PIB en 2023 (61,5 milliards d'euros ; SIES).",
                              "Document 2 : taux de croissance du PIB de la France en volume, 1950-2025 (Insee).",
                              "Document 3 : la mise au point des vaccins à ARN messager, fondée sur des recherches universitaires financées sur fonds publics, puis industrialisée par des entreprises en 2020."]),
        "pa_p3": dict(type="pause", t="Deux ou trois idées, chacune avec un mécanisme et un document."),
        "li_p3": dict(type="liste", titre="Le plan corrigé", x=110, y=90, w=1060, items=[
            "Introduction : définir innovation et croissance, annoncer les idées",
            "I. L'innovation accroît la PGF : coûts, prix, revenus, demande · document 2, Solow",
            "II. Elle crée de nouveaux produits et marchés : destruction créatrice · document 3",
            "III. Un cercle vertueux : croissance endogène (Romer, Lucas, Barro) · documents 1 et 3",
            "Conclusion : par la productivité et les nouveaux marchés ; la croissance lui rend ses moyens"],
            marques=["→", "I", "II", "III", "✓"]),
        "note_p3": dict(type="note", titre="Règle d'or de la partie 3", cles=["démontre"],
                        t="Pas de partie « limites » : un « montrez que » ne se discute pas, il se démontre.", x=170, y=220, w=940),
    }),

    # ================================================================ XIV. dissertation
    dict(id="dissertation", chap="La dissertation", fond="corail", humeur="tension", beats=[
        "{ex_d}Et la dissertation. Le sujet : « Le progrès technique suffit-il à rendre la croissance soutenable ? »",
        "{ex_d.1}Commence par analyser chaque mot. Le progrès technique, la croissance, la soutenabilité. "
        "{ex_d.2}Puis repère le type de question : « suffit-il » appelle une réponse nuancée. "
        "{ex_d.3}Et ne commente pas le dossier document par document : tes connaissances sont attendues.",
        "{-ex_d}{pa_d}À toi. Mets sur pause : écris la problématique, puis le plan détaillé, avec deux ou trois sous-parties par partie.",
        "{pa_d.stop}{-pa_d}{def_pb}Correction. La problématique. La croissance dégrade le capital naturel. Le progrès technique, qui repousse depuis deux siècles "
        "les limites de la production, peut-il à lui seul concilier croissance et préservation de l'environnement ? Ou faut-il d'autres leviers ?",
        "{-def_pb}{cm_d}Et le plan, en trois parties. {cm_d.1}Un : le progrès technique peut reculer les limites écologiques. "
        "Il améliore l'efficacité. Il permet des substitutions, comme les énergies bas carbone. Et il permet un découplage : en France, de mille neuf cent quatre-vingt-dix "
        "à deux mille vingt-cinq, le PIB en volume progresse de soixante-neuf pour cent, et les émissions territoriales baissent de trente-quatre virgule trois pour cent. "
        "C'est la logique de la soutenabilité faible.",
        "{cm_d.2}Deux : mais il ne suffit pas. L'effet rebond annule une partie des gains, c'est Jevons. Le découplage est fragile : les émissions importées, "
        "et un rythme insuffisant au regard de l'objectif de moins cinquante pour cent en deux mille trente. Et une partie du capital naturel est irremplaçable : "
        "c'est la soutenabilité forte.",
        "{cm_d.3}Trois : il doit être orienté et complété par l'action publique. Les externalités négatives appellent des instruments : la taxation, les quotas, les normes. "
        "Il faut subventionner l'innovation verte, car le marché sous-investit dans les technologies propres. Et changer le contenu de la croissance : "
        "la sobriété, les services, la réparation.",
        ("P", 1.0),
        "Pourquoi ce plan ? Parce que « suffit-il » appelle d'abord un oui, puis un pas seul, puis une réponse construite.",
        "{-cm_d}",
    ], vis={
        "ex_d": dict(type="exo", niveau="dissert", titre="Le progrès technique suffit-il à rendre la croissance soutenable ?",
                     src="Sujet inventé pour le site",
                     enonce=["Construis la problématique et le plan détaillé."],
                     questions=["Analyser chaque mot du sujet", "Repérer le type de question : « suffit-il » appelle une réponse nuancée",
                                "Mobiliser ses connaissances, sans commenter le dossier document par document"]),
        "pa_d": dict(type="pause", t="La problématique, puis le plan détaillé : trois parties, deux ou trois sous-parties chacune."),
        "def_pb": dict(type="def", terme="Problématique", cles=["capital", "concilier", "leviers"],
                       t="La croissance dégrade le capital naturel. Le progrès technique peut-il à lui seul concilier croissance et préservation de l'environnement, ou faut-il d'autres leviers ?",
                       x=150, y=170, w=980),
        "cm_d": dict(type="plan", titre="Le progrès technique suffit-il à rendre la croissance soutenable ?", x=70, y=120, w=1140, parties=[
            dict(t="I. Il peut reculer les limites", items=["A. Efficacité : moins d'énergie et de matières", "B. Substitutions : énergies bas carbone",
                                                           "C. Découplage : PIB +69 %, GES −34,3 % (1990-2025) ; soutenabilité faible"]),
            dict(t="II. Mais il ne suffit pas", items=["A. Effet rebond (Jevons, 1865)", "B. Empreinte importée, rythme insuffisant (−50 % en 2030)",
                                                      "C. Capital naturel critique : soutenabilité forte"]),
            dict(t="III. Il doit être orienté et complété", items=["A. Externalités : taxes, quotas, normes", "B. Subventionner l'innovation verte",
                                                                  "C. Changer le contenu : sobriété, services, réparation"])]),
    }),

    # ================================================================ XV. récap
    dict(id="recap", chap="Pour le bac", fond="canard", humeur="lumiere", beats=[
        "{cm_r}On récapitule. Au centre, la croissance : l'augmentation durable du PIB en volume. "
        "{cm_r.1}Ses sources : l'accumulation des facteurs, et surtout la productivité globale des facteurs. Le résidu de Solow, et un progrès technique endogène : "
        "Romer, Lucas, Barro. {cm_r.2}Les institutions, droits de propriété et brevets, et la destruction créatrice de Schumpeter, d'Aghion et de Howitt.",
        "{cm_r.3}Les inégalités : un progrès technique biaisé, la polarisation des emplois, les rentes de l'innovation. "
        "{cm_r.4}Et les limites écologiques : le découplage, l'effet rebond, la soutenabilité faible ou forte.",
        "{-cm_r}{fr_r}Les auteurs, dans l'ordre. {fr_r.1}Jevons, mille huit cent soixante-cinq. {fr_r.2}Schumpeter, mille neuf cent quarante-deux. "
        "{fr_r.3}Solow, mille neuf cent cinquante-six. {fr_r.4}Meadows, mille neuf cent soixante-douze. {fr_r.5}Lucas, mille neuf cent quatre-vingt-huit. "
        "{fr_r.6}Aghion et Howitt, mille neuf cent quatre-vingt-douze. {fr_r.7}Goldin et Katz, deux mille huit.",
        ("P", 4.0),
        "{-fr_r}{cf_r}{cf_r.1}Et trois chiffres à citer dans une copie. Cinq virgule deux pour cent de croissance par an pendant les Trente Glorieuses, "
        "contre un pour cent entre deux mille sept et deux mille dix-neuf. {cf_r.2}Deux virgule dix-huit pour cent du PIB pour la recherche en deux mille vingt-trois. "
        "{cf_r.3}Et moins trente-quatre virgule trois pour cent d'émissions de gaz à effet de serre depuis mille neuf cent quatre-vingt-dix.",
        ("P", 1.5),
        "{-cf_r}{fin}Les fiches à imprimer, le quiz, les cartes de révision et les animations de ce chapitre sont sur le site Faits et Courbes. "
        "Le lien est dans la description. Prochain dossier : le commerce international.",
        ("P", 2.5),
        "{-fin}",
    ], vis={
        "cm_r": dict(type="plan", titre="La croissance : l'augmentation durable du PIB en volume", x=60, y=140, w=1160, parties=[
            dict(t="Les sources", items=["Facteurs et PGF : le résidu (Solow)", "Progrès endogène : Romer, Lucas, Barro"]),
            dict(t="Institutions et innovation", items=["Droits de propriété, brevets (North)", "Destruction créatrice : Schumpeter, Aghion et Howitt"]),
            dict(t="Les inégalités", items=["Progrès biaisé (Goldin et Katz)", "Polarisation, rentes de l'innovation"]),
            dict(t="Les limites écologiques", items=["Découplage, effet rebond (Jevons)", "Soutenabilité faible / forte"])]),
        "fr_r": dict(type="frise", de=1850, a=2020, items=[
            dict(d=1865, nom="Jevons", q="l'effet rebond"), dict(d=1942, nom="Schumpeter", q="destruction créatrice"),
            dict(d=1956, nom="Solow", q="le résidu"), dict(d=1972, nom="Meadows", q="limites de la croissance"),
            dict(d=1988, nom="Lucas", q="capital humain"), dict(d=1992, nom="Aghion, Howitt", q="Nobel 2025"),
            dict(d=2008, nom="Goldin, Katz", q="éducation / technologie")]),
        "cf_r": dict(type="chiffres", titre="Trois chiffres à citer", x=90, y=150, w=1100,
                     items=[dict(n=c["n"], l=c["l"], s=c["s"]) for c in CHIF]),
        "fin": dict(type="titre", sur="Faits & Courbes · SES Terminale", t="Fiches, quiz et animations",
                    sous="Le lien est dans la description · prochain dossier : le commerce international"),
    }),
]

QUIZ = [
    dict(q="La croissance économique se mesure par le taux de variation…",
         r=["du PIB en volume", "du PIB en valeur", "de l'indice des prix"], ok=0,
         ex="Le PIB en volume neutralise la hausse des prix : il mesure l'évolution des quantités produites.", voir="cols_vv"),
    dict(q="Entre 1950 et 1973, le PIB français a crû en moyenne d'environ…",
         r=["1 % par an", "5 % par an", "10 % par an"], ok=1,
         ex="5,2 % par an en moyenne selon les niveaux Insee, contre environ 1 % par an entre 2007 et 2019.", voir="gr_pib"),
    dict(q="La productivité globale des facteurs mesure…",
         r=["la production par travailleur", "l'efficacité de la combinaison du travail et du capital", "le nombre d'heures travaillées"], ok=1,
         ex="C'est la part de la croissance non expliquée par la hausse des quantités de facteurs : le résidu de Solow.", voir="cols_prod"),
    dict(q="Chez Solow, pourquoi l'accumulation de capital ne suffit-elle pas à une croissance durable ?",
         r=["Parce que le capital est non rival", "Parce que ses rendements sont décroissants", "Parce que l'État la freine"], ok=1,
         ex="Chaque machine supplémentaire rapporte moins que la précédente : sans progrès technique, la croissance s'essouffle.", voir="an_solow"),
    dict(q="Pour Paul Romer, les connaissances favorisent la croissance parce qu'elles sont…",
         r=["non rivales et génèrent des externalités positives", "rares et coûteuses", "protégées à vie par des brevets"], ok=0,
         ex="Une connaissance peut être utilisée par tous sans s'épuiser : elle se diffuse et profite à d'autres entreprises.", voir="au_romer"),
    dict(q="Un brevet incite à innover parce qu'il…",
         r=["rend l'innovation gratuite pour tous", "accorde un monopole d'exploitation temporaire à l'innovateur", "interdit la concurrence pour toujours"], ok=1,
         ex="L'innovateur s'approprie les gains de son invention pendant vingt ans au plus, en échange de sa publication.", voir="ch_inst"),
    dict(q="La « destruction créatrice » désigne…",
         r=["le remplacement d'activités anciennes par des activités nouvelles issues de l'innovation", "la baisse du PIB pendant une récession",
            "la destruction de capital lors des guerres"], ok=0,
         ex="Schumpeter : les innovations créent de nouvelles activités et en rendent d'autres obsolètes.", voir="ch_dc"),
    dict(q="La « polarisation des emplois » signifie que…",
         r=["tous les emplois deviennent qualifiés", "les emplois intermédiaires routiniers reculent au profit des deux extrémités", "l'emploi se concentre dans l'industrie"], ok=1,
         ex="L'automatisation remplace d'abord les tâches routinières, souvent au milieu de l'échelle des salaires.", voir="ill_pol"),
    dict(q="L'effet rebond désigne…",
         r=["la reprise de la croissance après une récession", "une hausse de l'usage qui annule une partie des économies permises par une innovation plus efficace",
            "la hausse des prix de l'énergie"], ok=1,
         ex="Moins de coût d'usage → plus d'usage : c'est le paradoxe observé par Jevons dès 1865.", voir="ch_reb"),
    dict(q="La soutenabilité « forte » considère que…",
         r=["tous les capitaux sont substituables", "l'innovation suffit à tout résoudre", "une partie du capital naturel est irremplaçable"], ok=2,
         ex="Pour la soutenabilité forte, le capital naturel critique (climat, biodiversité) doit être préservé.", voir="cmp_sout"),
]

CREDITS = [
    "Données : Insee, comptes nationaux annuels, base 2020 (mai 2026) ; Citepa, rapport Secten 2026 ; ministère de l'Enseignement supérieur et de la Recherche, SIES, note n° 2025-12.",
    "Graphiques, chaînes causales, animations et sujets : site Faits & Courbes (SES Terminale) ; les sujets sont inventés pour le site.",
    "Polices : IBM Plex Sans Condensed, Archivo, Spectral, JetBrains Mono (SIL Open Font License).",
]
