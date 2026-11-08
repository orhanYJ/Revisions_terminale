"""Histoire · « Les régimes totalitaires » — édition française de la série vidéo, épisode 5 : « La terreur de masse »
(partie II.3 du cours).

Traduction et adaptation de h2_5.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
histoire-géographie classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes
visuels, mêmes repères, mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H2 : 14 « une terreur moins oppressive ? » (Italie, confino, Lipari) · 15 les koulaks · 17 le Goulag, canal de la
       mer Blanche · 19 l'Holodomor · 21 l'incendie du Reichstag · 22 polices politiques et camps (Dachau) ·
       23 la lutte des races (T4) · 30 procès de Moscou et Grande Purge · 38 la terreur dévore les siens (Iejov, Trotski)
Contenu : CHAPTERS.H2 du site, section II.3 (8 idées), schéma de la Worksheet 4 (→ « le dossier documentaire sur la
terreur » : les six similitudes et les différences), tableau des totalitarismes parcouru comme synthèse des parties I et
II, Arendt (la confiance des masses). Worksheet 2 → « le dossier documentaire sur les koulaks ».
Corrections et précisions dites comme dans l'édition anglaise : pas de camps pour les opposants en Italie même, mais des
camps en Libye (Cyrénaïque, 1930-1933), hors du cours ; Beria à la tête du NKVD de 1938 à 1945 seulement, hors du cours ;
Iejov remplacé par Beria avant d'être exécuté ; procès de Moscou 1936-1938 et Grande Purge 1937-1938.
Adaptations : « Your turn » 1 = le dossier documentaire sur la terreur (similitudes) ; « Your turn » 2, essay « How far »
→ réponse à une question problématisée « Dans quelle mesure… ? » (plan et introduction), avec un modèle.
Citations en traduction française : Arendt (Les Origines du totalitarisme), Zinoviev et Kamenev (procès de 1936,
traduction au plus près de la version anglaise du cours).
Ton : sobre et factuel ; aucune image de victimes.
Chaîne : outils/serie-philo/generer.py h2f_5 ; sortie dans dnl/serie/ (h2f-5.*).
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-5"
NOTION = "Les régimes totalitaires"
NUM = 5
TITRE = "La terreur de masse"
SUIVANT = "Épisode 6 · Des ambitions hégémoniques"
PRONONCIATION = {"Il Duce ha sempre ragione": "Il Dou-tché a sèmm-pré ra-djo-né", "Biennio Rosso": "Bi-èn-nio Ros-so",
                 "Holodomor": "Ho-lo-do-mor", "Iejov": "Ié-jof", "Zinoviev": "Zi-no-vièf", "Kamenev": "Ka-mé-nièf",
                 "Rykov": "Ri-kof", "OVRA": "O-vra", "OGPU": "o-gué-pé-ou", "NKVD": "èn-ka-vé-dé",
                 "Matteotti": "Mat-té-ot-ti", "Himmler": "Himm-leur", "Dachau": "Da-kao", "Reichstag": "Raïchs-tag",
                 "Reichsmarks": "Raïchs-mark", "confino": "conn-fi-no", "Arendt": "A-rennt", "Duce": "Dou-tché",
                 "Führer": "Fu-reur", "Balilla": "Ba-lil-la", "Komsomol": "Komm-so-mol", "squadristi": "skoua-dris-ti",
                 "Hindenburg": "Hinn-denn-bourg", "Lebensraum": "Lé-benss-raoum", "Heil Hitler": "Haïl Hitler",
                 "SS": "èss-èss", "SA": "èss-a", "T4": "té-quatre", "Alexeï": "A-lek-sè-ï"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="guerre", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Moscou, mille neuf cent trente-six. Dans le box des accusés, d'anciens compagnons de Lénine. "
        "Ils avouent des crimes qu'ils n'ont jamais commis. "
        "À la fin de mille neuf cent trente-huit, la Grande Purge aura fait six cent quatre-vingt mille exécutions.",
        "{q1}Pourquoi un régime terroriserait-il son propre peuple ? Et pourquoi finirait-il par frapper ses propres hommes ?",
        "{-q1}{-g0}{plan}Aujourd'hui, la partie deux, point trois du chapitre : la terreur de masse. {plan.1}On commence par les événements, sur la carte. "
        "{plan.2}Puis le cours, idée par idée : la police, les procès, les camps, les purges. "
        "{plan.3}Puis le dossier documentaire sur la terreur. Qu'ont en commun les trois terreurs ? Et qu'est-ce qui les distingue ? "
        "{plan.4}Ensuite, tout le tableau des totalitarismes, en synthèse des parties un et deux. "
        "{plan.5}Enfin, une question problématisée : la terreur a-t-elle été le principal instrument de ces régimes ?",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[30]),
        "q1": dict(type="question", t="Pourquoi terroriser son propre peuple ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 5 · le plan", items=[
            "La terreur sur la carte, 1929 – 1940", "II.3 · La terreur de masse : huit idées",
            "Le dossier documentaire · les similitudes dans l'usage de la violence", "Le tableau des totalitarismes : parties I et II",
            "À toi : la terreur, principal instrument ?"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 5", t="La terreur de masse",
                      sous="Police · procès · camps · purges · partie II.3 du cours"),
    }),

    # ================================================================ la carte : 1929-1933
    dict(id="carte1", chap="Sur la carte : 1929 – 1933", fond="nuit", humeur="mystere",
         retenir="Italie : opposants envoyés sur des îles (le confino) · URSS 1929-1932 : les koulaks déportés · 1931-1933 : le canal de la mer Blanche, creusé par les détenus du Goulag · 1932-1933 : l'Holodomor en Ukraine.",
         beats=[
        "{g1}Commençons sur la carte, dans l'ordre chronologique. {g1.1}L'Italie, à partir de mille neuf cent vingt-neuf. "
        "Mussolini doit composer avec l'Église, et avec le roi. Ses opposants, en général, ne sont pas exécutés. "
        "On les envoie en relégation, sur des îles comme Lipari. "
        "Le cours pose la question, avec un point d'interrogation : une terreur moins oppressive ?",
        "{g1.2}Passons à l'Union soviétique, de mille neuf cent vingt-neuf à mille neuf cent trente-deux. C'est la collectivisation forcée, "
        "que tu as vue dans l'épisode trois. Tout paysan qui résiste est traité de koulak : un ennemi de classe. "
        "On lui confisque sa terre et ses bêtes. Et beaucoup sont déportés.",
        "{g1.3}Puis le Grand Nord, de mille neuf cent trente et un à mille neuf cent trente-trois. Les détenus du Goulag creusent le canal de la mer Blanche à la Baltique : "
        "deux cent vingt-sept kilomètres, en grande partie avec des outils à main. Le camp est devenu un chantier.",
        "{g1.4}Et l'Ukraine, en mille neuf cent trente-deux et trente-trois. C'est l'Holodomor. Le grain est réquisitionné, quelle que soit la récolte. "
        "Les villages rebelles sont privés de tout ravitaillement. La famine tue des millions de personnes. "
        "C'est une famine provoquée par une décision politique.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[14, 15, 17, 19]),
    }),

    # ================================================================ la carte : 1933-1940
    dict(id="carte2", chap="Sur la carte : 1933 – 1940", fond="nuit", humeur="tension",
         retenir="27 févr. 1933 : l'incendie du Reichstag · 1933 : Gestapo, Dachau · 1933-1939 : stérilisation, lois de Nuremberg, T4 · 1936-1938 : procès de Moscou, Grande Purge · 1940 : Iejov exécuté, Trotski assassiné au Mexique.",
         beats=[
        "{g2}{g2.1}L'Allemagne, le vingt-sept février mille neuf cent trente-trois. Le Reichstag est en feu. "
        "Les nazis accusent les communistes. Les libertés sont suspendues. Des milliers de communistes sont arrêtés.",
        "{g2.2}La même année, la police politique est placée au-dessus des lois. Et le premier camp ouvre à Dachau, près de Munich. "
        "L'Italie a sa propre police politique, l'OVRA, depuis mille neuf cent vingt-sept. L'Union soviétique crée le NKVD en mille neuf cent trente-quatre.",
        "{g2.3}À partir de mille neuf cent trente-trois, la violence nazie frappe aussi des Allemands, au nom de la biologie. "
        "D'abord la stérilisation forcée. Puis les lois de Nuremberg, en mille neuf cent trente-cinq. "
        "Et à partir de mille neuf cent trente-neuf, le meurtre des handicapés.",
        "{g2.4}Moscou, de mille neuf cent trente-six à mille neuf cent trente-huit. Ce sont les procès spectacles, et la Grande Purge. "
        "Le parti est décimé. L'armée est affaiblie.",
        "{g2.5}Et puis, mille neuf cent quarante. Iejov, qui dirigeait la police soviétique pendant la purge, est exécuté. "
        "Au Mexique, Trotski, le grand rival de Staline, est assassiné par un agent de la police soviétique. La terreur dévore les siens. Même à l'étranger.",
        "{-g2}{fr1}Six dates à retenir. {fr1.1}Mille neuf cent vingt-sept : l'OVRA. {fr1.2}Mille neuf cent trente et un : début des travaux du canal de la mer Blanche. "
        "{fr1.3}Mille neuf cent trente-trois : Dachau. {fr1.4}Mille neuf cent trente-quatre : la nuit des Longs Couteaux. "
        "{fr1.5}Mille neuf cent trente-sept et trente-huit : la Grande Purge. {fr1.6}Et mille neuf cent quarante : Iejov, et Trotski.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[21, 22, 23, 30, 38]),
        "fr1": dict(type="frise", items=[
            dict(nom="OVRA", d=1927, q="Italie"), dict(nom="Canal de la mer Blanche", d=1931, q="1931-1933, Goulag"),
            dict(nom="Dachau", d=1933, q="Allemagne"), dict(nom="Longs Couteaux", d=1934, q="85 assassinés"),
            dict(nom="Grande Purge", d=1937, q="1937-1938 : 680 000"), dict(nom="Iejov, Trotski", d=1940, q="exécuté, assassiné")]),
    }),

    # ================================================================ II.3, idée 1 : une méthode de gouvernement
    dict(id="methode", chap="II.3 · La terreur, une méthode de gouvernement", fond="nuit", humeur="mystere",
         retenir="La violence totalitaire est permanente, organisée, planifiée. Arendt : « dominer et terroriser les êtres humains de l'intérieur » : une peur si profonde que chacun se censure lui-même. Exemple : Tintin au pays des Soviets (1930).",
         beats=[
        "{def1}Passons au cours, idée par idée. Première idée. Dans un régime totalitaire, la terreur n'est pas un raté de l'ordre. "
        "C'est {!une méthode de gouvernement}une méthode de gouvernement. "
        "{def1.1}La violence n'est pas une réponse exceptionnelle à une crise. Elle est permanente. Elle est organisée. Elle est planifiée.",
        "{photo1}Hannah Arendt, que tu as rencontrée dans l'épisode un, a écrit que ces régimes avaient trouvé{-def1}",
        ("C", "un moyen de dominer et de terroriser les êtres humains de l'intérieur", "c_ar"),
        "{-c_ar}{-photo1}{fear}Alors, à quoi sert la terreur ? {fear.1}Pas seulement à punir. {fear.2}Elle installe la peur au plus profond de chacun. "
        "{fear.3}Si profond que chacun se censure lui-même. "
        "{fear.4}Et alors, l'obéissance n'a plus besoin d'être commandée.",
        "{-fear}{tin}L'exemple est une bande dessinée. En mille neuf cent trente, Tintin au pays des Soviets, d'Hergé, "
        "montrait déjà aux lecteurs occidentaux un État policier. Des élections truquées. Une famine cachée. Une caricature, bien sûr. "
        "{tin.1}Mais elle a répandu l'image de la terreur soviétique bien avant que les historiens puissent ouvrir les archives.",
    ], vis={
        "def1": dict(type="def", cles=["permanente", "organisée", "planifiée"], terme="Idée 1 · la terreur comme méthode",
                     t="La violence n'est pas la réponse exceptionnelle à une crise : elle est permanente, organisée et planifiée.",
                     etape="Pas un raté de l'ordre : une manière de gouverner", x=170, y=200, w=940),
        "photo1": dict(type="tableau", img="h2-arendt", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.12, .5, .25],
                       legende="Hannah Arendt, autrice des Origines du totalitarisme (1951), en 1958 · Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0"),
        "c_ar": dict(type="cit", a="Hannah Arendt", o="Les Origines du totalitarisme, 1951 (traduction)", x=200, y=200, w=880),
        "fear": dict(type="liste", titre="Comment la terreur agit", cles=["punir", "peur", "censure", "obéissance"], items=[
            "Pas seulement punir", "Installer la peur au plus profond", "Chacun se censure lui-même",
            "L'obéissance n'a plus besoin d'être commandée"], x=170, y=140, w=940),
        "tin": dict(type="note", terme="Exemple · Hergé, 1930", cles=["truquées", "cachée", "famine"],
                    t="Tintin au pays des Soviets : un État policier, des élections truquées, une famine cachée.",
                    etape="Une caricature qui a répandu l'image de la terreur bien avant l'ouverture des archives", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 2 : la police politique
    dict(id="police", chap="II.3 · Une police politique au-dessus des lois", fond="nuit", humeur="tension",
         retenir="Italie : l'OVRA (1927) · Allemagne : la Gestapo (police d'État, 1933) et la SS (police du parti), sous Himmler dès 1936 · URSS : l'OGPU, puis le NKVD (1934), qui organise les déportations. Elles répondent au chef, jamais à un juge.",
         beats=[
        "{g3}{g3.1}Deuxième idée. Chaque régime a bâti une police politique. Elle répond au parti, pas aux tribunaux. "
        "C'est l'instrument de la terreur : {!une police au-dessus des lois}une police placée au-dessus des lois.",
        "{pol}{pol.1}En Italie, Mussolini crée l'OVRA en mille neuf cent vingt-sept. "
        "{pol.2}L'Allemagne a deux forces. La Gestapo, la police d'État, à partir de mille neuf cent trente-trois. Et la SS, la police du parti. "
        "{pol.3}En Union soviétique, il y a d'abord l'OGPU. Puis, à partir de mille neuf cent trente-quatre, le NKVD. "
        "C'est lui qui organise les déportations vers les camps de travail.",
        "{-pol}{-g3}{him}L'exemple à retenir, c'est Heinrich Himmler. La Gestapo est placée sous son autorité. "
        "Et à partir de mille neuf cent trente-six, il tient à la fois les deux polices allemandes : la police d'État, et la police du parti. "
        "{him.1}En un seul homme, le parti et l'État ont fusionné.",
        "{-him}{voc}Pourquoi ? Parce que ces organes répondent au chef. "
        "Alors {!aucun juge}aucun juge ne peut protéger un citoyen contre eux. "
        "Dans ta copie, appelle-la par son nom : une police politique.",
    ], vis={
        "g3": dict(type="globe", code="H2", sc=[22]),
        "pol": dict(type="liste", titre="Trois polices politiques", petit=True, bande=True, x=60, y=130, w=620, items=[
            "Italie : l'OVRA, 1927", "Allemagne : Gestapo (État, 1933) + SS (parti)", "URSS : OGPU, puis NKVD (1934)"]),
        "him": dict(type="cols", g="La Gestapo", gq="la police d'État, créée en 1933", d="La SS", dq="la police du parti",
                    vs="+", repere="Toutes deux dirigées par Himmler à partir de 1936"),
        "voc": dict(type="def", cles=["chef", "tribunaux", "juge"], terme="Vocabulaire · police politique",
                    t="Une police qui répond au chef ou au parti plutôt qu'aux tribunaux : OVRA, Gestapo, NKVD.",
                    etape="Aucun juge ne peut protéger un citoyen contre elle", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 3 : les procès de Moscou
    dict(id="proces", chap="II.3 · La justice en spectacle : les procès de Moscou", fond="guerre", humeur="tension",
         retenir="Procès spectacles (1936-1938) : de vieux bolcheviks avouent des crimes inventés, leurs familles menacées. Grande Purge (1937-1938) : 680 000 exécutions, parti décimé, armée affaiblie, Staline renforcé. Zinoviev et Kamenev fusillés (1936).",
         beats=[
        "{g4}{g4.1}Troisième idée. La justice devient un spectacle. La terreur soviétique atteint son sommet avec les procès de Moscou. "
        "Ce sont des {!procès spectacles}procès spectacles, mis en scène pour le public. De vieux bolcheviks, compagnons de Lénine, "
        "avouent des crimes qu'ils n'ont pas commis. Pourquoi ? Parce qu'on a menacé leurs familles.",
        "À son procès, en mille neuf cent trente-six, Zinoviev se déclare{-g4}",
        ("C", "le principal organisateur de l'assassinat de Kirov", "c_zi"),
        "{-c_zi}Et Kamenev dit avoir été",
        ("C", "mû par une haine sans bornes et par la soif du pouvoir", "c_ka"),
        "{-c_ka}{photo}Regarde maintenant une photographie, prise en mille neuf cent vingt-cinq. {photo.1}Staline pose avec Zinoviev, Kamenev, et Alexeï Rykov. "
        "{photo.2}Staline a fait fusiller ces trois hommes. {photo.3}Zinoviev et Kamenev en mille neuf cent trente-six. Rykov en mille neuf cent trente-huit.",
        "{-photo}{photo2}{purge}Vient ensuite la Grande Purge, en mille neuf cent trente-sept et trente-huit. "
        "{!680 000}Le dossier compte six cent quatre-vingt mille exécutions. "
        "Le parti est décimé. L'armée est affaiblie.",
        "{-purge}{para}Voici le paradoxe à expliquer dans une copie. La purge a renforcé Staline. Pourquoi ? "
        "Justement parce qu'elle a détruit tous ceux qui auraient pu le remplacer. "
        "{para.1}Et un détail de dates. Les procès spectacles vont de mille neuf cent trente-six à trente-huit. "
        "La Grande Purge couvre mille neuf cent trente-sept et trente-huit.{-photo2}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[30]),
        "c_zi": dict(type="cit", a="Grigori Zinoviev", o="procès de Moscou, 1936 (traduction)", x=200, y=210, w=880),
        "c_ka": dict(type="cit", a="Lev Kamenev", o="procès de Moscou, 1936 (traduction)", x=200, y=210, w=880),
        "photo": dict(type="liste", titre="Une photographie, 1925", items=[
            "Staline, Zinoviev, Kamenev, Rykov", "Les trois compagnons fusillés sur ordre de Staline",
            "Zinoviev et Kamenev en 1936 · Rykov en 1938"], x=170, y=150, w=940),
        "photo2": dict(type="tableau", img="h2-moscow-trial", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.1, .5, .45],
                       legende="Les accusés du deuxième procès de Moscou, janvier 1937 · photographe inconnu, domaine public"),
        "purge": dict(type="mot", t="680 000", g="exécutions de la Grande Purge, 1937-1938 · le parti décimé, l'armée affaiblie", y=240, taille=140),
        "para": dict(type="note", terme="Le paradoxe", cles=["renforcé", "remplacer"],
                     t="La purge a renforcé Staline : elle a détruit tous ceux qui auraient pu le remplacer.",
                     etape="Dates : procès spectacles 1936-1938 · Grande Purge 1937-1938", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 4 : le camp
    dict(id="camps", chap="II.3 · Le camp, une institution permanente", fond="nuit", humeur="mystere",
         retenir="Goulag : des camps là où il faut de la main-d'œuvre ; canal mer Blanche-Baltique (227 km, 1931-1933) ; 1,5 million de détenus au début des années 1950. Dachau (1933) : triangles de couleur. Le camp n'est pas nazi ; la chambre à gaz l'est.",
         beats=[
        "{g5}{g5.1}Quatrième idée. Le camp devient une institution permanente, et le travail forcé une ressource économique. "
        "La répression n'est pas seulement judiciaire. Elle est territoriale. Des populations entières sont enfermées.",
        "{g5.2}Le Goulag soviétique répand ses camps dans tout le pays. Et il les place là où l'on a besoin de main-d'œuvre : "
        "dans les mines, dans les forêts, le long des canaux. La terreur produit donc aussi. "
        "{-g5}{photo3}L'exemple, c'est le canal de la mer Blanche à la Baltique. Deux cent vingt-sept kilomètres, "
        "creusés entre mille neuf cent trente et un et mille neuf cent trente-trois, en grande partie avec des outils à main. "
        "C'est le premier grand chantier soviétique réalisé par les détenus du Goulag.",
        "{-photo3}{gul}Le graphique du dossier donne l'échelle. {gul.1}{gul.2}{gul.3}Au début des années mille neuf cent cinquante, "
        "les camps comptent plus d'{!un million et demi}un million et demi de détenus.",
        "{-gul}{tri}L'Allemagne ouvre Dachau en mille neuf cent trente-trois. Le camp est destiné à tous ceux qu'on juge incompatibles avec la société. "
        "À l'intérieur, les détenus sont classés par triangles de couleur. "
        "{tri.1}Rouge pour les détenus politiques. {tri.2}Vert pour les criminels. {tri.3}Rose pour les homosexuels. "
        "{tri.4}Noir pour ceux qu'on appelle les asociaux. {tri.5}Violet pour les Témoins de Jéhovah. {tri.6}Et un triangle jaune est ajouté pour les Juifs.",
        "{-tri}{phr}Retiens cette phrase du cours. Les nazis n'ont pas inventé le camp. {phr.1}Ce qu'ils ont ajouté, c'est la chambre à gaz.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[17]),
        "photo3": dict(type="tableau", img="h2-belomorkanal", de=[1.0, .3, .5], a=[1.05, .7, .5],
                       legende="Des détenus du Goulag creusent le canal mer Blanche-Baltique, été 1932 · photographe inconnu, domaine public"),
        "gul": dict(type="graphe", titre="Population des camps du Goulag (graphique du dossier)", x=300, y=110, w=680, h=520,
                    ax=dict(x=[1929.5, 1953.5], y=[0, 2.0], gx=[1930, 1935, 1940, 1945, 1950], gy=[0.5, 1.0, 1.5],
                            lx="année", ly="millions de détenus"),
                    el=[dict(type="droite", pts=[[1947, 1.5], [1953, 1.5]], c="iv", tir=True, lbl="1,5 million", lp=[1944, 1.62], dur=1.0),
                        dict(type="texte", x=1932, y=0.25, t="1931-1933 : le canal de la mer Blanche", c="sa"),
                        dict(type="point", x=1952, y=1.6, c="ca", lbl="début des années 1950", lp=[1948.5, 1.82])]),
        "tri": dict(type="liste", titre="Camps nazis · les triangles de couleur", petit=True,
                    marques=["R", "V", "Ro", "N", "Vi", "J"], items=[
            "Rouge : détenus politiques", "Vert : criminels", "Rose : homosexuels", "Noir : « asociaux »",
            "Violet : Témoins de Jéhovah", "Jaune, ajouté : Juifs"], x=170, y=100, w=940),
        "phr": dict(type="note", terme="Le cours le résume", cles=["inventé", "gaz"],
                    t="Les nazis n'ont pas inventé le camp…",
                    etape="… ce qu'ils ont ajouté, c'est la chambre à gaz", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 5 : au nom de la biologie
    dict(id="biologie", chap="II.3 · Des Allemands frappés au nom de la biologie", fond="nuit", humeur="mystere",
         retenir="1933 : loi de stérilisation forcée (neuf affections, ex. cécité, surdité, schizophrénie) : ≈ 400 000 stérilisés, 1933-1945. Propagande : 5,50 Reichsmarks par jour. T4 (1939-1941) : ≈ 70 000 Allemands handicapés tués, surtout par gaz.",
         beats=[
        "{g6}{g6.1}Cinquième idée. La violence nazie frappe aussi les Allemands eux-mêmes, au nom de la biologie. "
        "La doctrine raciale produit de la violence à l'intérieur même de la population allemande.",
        "{-g6}{bio}{bio.1}En mille neuf cent trente-trois, une loi autorise la stérilisation forcée. Elle vise des Allemands atteints d'affections supposées héréditaires. "
        "{bio.2}La loi en énumère neuf. Parmi elles : la cécité, la surdité, et la schizophrénie. "
        "Entre mille neuf cent trente-trois et mille neuf cent quarante-cinq, environ {!400 000}quatre cent mille personnes sont stérilisées.",
        "{bio.3}La propagande la justifie par le coût. Une affiche montrait ce que coûtait chaque jour un malade : cinq Reichsmarks cinquante. "
        "Et elle opposait cette somme au coût d'une famille en bonne santé.",
        "{bio.4}En mille neuf cent trente-neuf, la logique va plus loin : jusqu'au meurtre. "
        "De mille neuf cent trente-neuf à mille neuf cent quarante et un, les médecins du programme T4, appelé euthanasie, "
        "tuent environ {!70 000}soixante-dix mille Allemands handicapés. La plupart meurent dans des chambres à gaz construites à cet effet.",
        "{-bio}{lien}Remarque le lien avec l'épisode quatre. L'homme nouveau allemand, c'était une race purifiée. "
        "{lien.1}La stérilisation et T4, c'est cette idéologie appliquée aux corps. "
        "Et remarque les chambres à gaz. Elles ont été construites ici, en Allemagne, avant la guerre à l'Est.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[23]),
        "bio": dict(type="liste", titre="La violence au nom de la biologie", cles=["stérilisation", "400 000", "coût", "70 000"], items=[
            "1933 : une loi sur la stérilisation forcée", "Neuf affections : cécité, surdité, schizophrénie… → ≈ 400 000 stérilisés, 1933-1945",
            "Propagande par le coût : 5,50 Reichsmarks par jour pour un malade", "T4, 1939-1941 : ≈ 70 000 Allemands handicapés tués, surtout par le gaz"],
            x=150, y=130, w=980),
        "lien": dict(type="def", cles=["purifiée", "corps"], terme="Lien · l'homme nouveau (épisode 4)",
                     t="L'homme nouveau allemand était une race purifiée : la stérilisation et T4 appliquent l'idéologie aux corps.",
                     etape="Des chambres à gaz construites en Allemagne pour T4, dès 1939", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 6 : la terreur dévore les siens
    dict(id="siens", chap="II.3 · La terreur frappe les hommes du régime", fond="guerre", humeur="tension",
         retenir="Personne n'est à l'abri : nuit des Longs Couteaux (1934, 85 assassinés, chefs SA) · Iejov, chef du NKVD, remplacé par Beria, exécuté en 1940 · Trotski assassiné au Mexique (1940). Quand la loyauté ne protège plus, on devance l'obéissance.",
         beats=[
        "{g7}{g7.1}La sixième idée est la plus révélatrice. La terreur se retourne contre les hommes du régime. "
        "{!Personne n'est à l'abri}Personne n'est à l'abri, pas même ceux qui le servent. Et c'est cela qui la rend totale.",
        "{own}{own.1}Allemagne, mille neuf cent trente-quatre : la nuit des Longs Couteaux. Le régime purge ses propres rangs paramilitaires. "
        "Quatre-vingt-cinq personnes sont assassinées, parmi lesquelles les chefs de la SA. "
        "{own.2}En Union soviétique, la Grande Purge finit par dévorer le chef de la police lui-même. "
        "Iejov était le chef de la police en qui Staline avait le plus confiance. Il est remplacé par Beria, et exécuté en mille neuf cent quarante. "
        "{own.3}La terreur atteint même l'étranger. Léon Trotski, le rival le plus influent de Staline, est assassiné au Mexique en mille neuf cent quarante. "
        "Le meurtrier est un agent de la police soviétique.",
        "{-own}{-g7}{ber}Une précision sur Beria, hors du cours. Il dirige le NKVD de mille neuf cent trente-huit à mille neuf cent quarante-cinq. "
        "Puis il reste parmi les hommes les plus puissants autour de Staline, jusqu'à sa chute en mille neuf cent cinquante-trois.",
        "{-ber}{eff}Alors, pourquoi est-ce si important ? {eff.1}Quand la loyauté ne te protège plus, obéir ne suffit pas. "
        "{eff.2}Il faut deviner ce que veut le chef, avant même qu'il le demande. {eff.3}Et c'est exactement l'effet que recherche le régime. "
        "Tu te souviens de la photographie de l'épisode quatre ? Iejov à côté de Staline. Puis effacé de la même image.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[38]),
        "own": dict(type="liste", titre="La terreur dévore les siens", petit=True, bande=True, x=60, y=130, w=620, items=[
            "1934 · nuit des Longs Couteaux : 85 assassinés", "1940 · Iejov, chef du NKVD, exécuté",
            "1940 · Trotski assassiné au Mexique"]),
        "ber": dict(type="note", terme="Une précision · hors du cours", cles=["1938", "1945", "1953"],
                    t="Beria dirige le NKVD de 1938 à 1945, puis reste l'un des hommes les plus puissants autour de Staline jusqu'à sa chute en 1953.",
                    etape="Le cours dit qu'il « occupe le poste jusqu'en 1953 »", x=170, y=200, w=940),
        "eff": dict(type="liste", titre="L'effet recherché", items=[
            "La loyauté ne protège plus", "L'obéissance doit être devancée, pas seulement donnée", "Exactement ce que veut le régime"],
            x=170, y=150, w=940),
    }),

    # ================================================================ II.3, idée 7 : l'Italie
    dict(id="italie", chap="II.3 · La terreur italienne : une autre échelle", fond="nuit", humeur="calme",
         retenir="Matteotti assassiné (1924) → l'État totalitaire. Loi de défense de l'État (1926) : peine de mort, Tribunal spécial · OVRA (1927). Moins de condamnations à mort ; opposants au confino (îles). Répression légalisée plus qu'industrialisée.",
         beats=[
        "{g8}{g8.1}Septième idée. La terreur italienne était réelle. Mais son échelle était différente, et une comparaison honnête doit le respecter. "
        "La violence fasciste a fondé le régime, puis elle est devenue routinière. Elle n'a jamais atteint l'échelle des deux autres.",
        "{-g8}{it}{it.1}Le tournant, c'est mille neuf cent vingt-quatre, avec l'assassinat du député socialiste Matteotti. "
        "Après lui, Mussolini abandonne le parlement et construit l'État totalitaire. La presse d'opposition est supprimée. "
        "Les ministres non fascistes sont écartés. "
        "{it.2}En mille neuf cent vingt-six, la loi de défense de l'État rétablit la peine de mort. "
        "Elle crée aussi un Tribunal spécial pour les ennemis de l'État. "
        "{it.3}L'OVRA suit, en mille neuf cent vingt-sept. "
        "{it.4}Mais le Tribunal spécial prononce bien moins de condamnations à mort que les systèmes soviétique ou allemand. "
        "Les opposants sont envoyés au confino : la relégation, sur des îles éloignées.",
        "{-it}{form}Retiens donc cette formule. En Italie, la répression est {!légalisée plutôt qu'industrialisée}légalisée plutôt qu'industrialisée. "
        "D'où la question du cours : une terreur moins oppressive ?",
        "{-form}{lib}Maintenant, une correction. Le cours dit que l'Italie n'avait pas de camps de concentration. "
        "C'est vrai de la manière dont on punissait les opposants en Italie avant la guerre : on les envoyait au confino. "
        "{lib.1}Mais voici un fait hors du cours. Dans sa colonie de Libye, l'Italie fasciste a enfermé la population de la Cyrénaïque "
        "dans des camps de concentration, de mille neuf cent trente à mille neuf cent trente-trois. "
        "Écris-le donc avec précision : pas de camps pour les opposants en Italie même.",
    ], vis={
        "g8": dict(type="globe", code="H2", sc=[14]),
        "it": dict(type="liste", titre="Italie : la terreur rendue légale", items=[
            "1924 · Matteotti assassiné → l'État totalitaire", "1926 · loi de défense de l'État : peine de mort, Tribunal spécial",
            "1927 · l'OVRA", "Bien moins de condamnations à mort · opposants envoyés au confino"], x=150, y=130, w=980),
        "form": dict(type="mot", t="Légalisée, pas industrialisée", g="« Une terreur moins oppressive ? » · le point d'interrogation du cours", y=250, taille=78),
        "lib": dict(type="note", terme="Attention · une correction", cles=["opposants", "Libye", "Cyrénaïque"],
                    t="Pas de camps pour les opposants en Italie même : on les envoyait au confino.",
                    etape="Hors du cours : en Libye, l'Italie enferme la population de la Cyrénaïque dans des camps, 1930-1933", x=170, y=200, w=940),
    }),

    # ================================================================ II.3, idée 8 : la logique commune
    dict(id="ennemi", chap="II.3 · La logique commune : désigner un ennemi", fond="nuit", humeur="tension",
         retenir="Les trois : une police secrète, des opposants réduits au silence ou tués, surtout un ennemi de la nation qui justifie la violence. URSS : les koulaks · Allemagne : Juifs, Roms, homosexuels, handicapés · Italie : les « ennemis de l'État ».",
         beats=[
        "{g9}{g9.1}Huitième idée : la logique commune des trois terreurs. Toutes trois utilisent une police secrète pour menacer la population. "
        "Toutes trois réduisent au silence ou tuent leurs opposants. Et surtout, toutes trois {!désignent un ennemi de la nation}désignent un ennemi de la nation.",
        "{-g9}{en}Une fois l'ennemi désigné, la violence contre lui paraît justifiée au reste de la population. "
        "{en.1}En Union soviétique, l'ennemi, ce sont les koulaks, comme dans le dossier documentaire sur les koulaks. "
        "{en.2}En Allemagne : les Juifs, les Roms, les prostituées, les homosexuels, et les handicapés. Quatre cent mille personnes sont stérilisées de force. "
        "{en.3}En Italie : les ennemis de l'État, jugés par le Tribunal spécial.",
        "{-en}{cons}En Allemagne, tout cela repose sur une théorie du complot. La nation serait minée par {!des ennemis de l'intérieur}des ennemis de l'intérieur. "
        "{cons.1}Tu sais d'où cela vient : c'est le mythe du coup de poignard dans le dos, de mille neuf cent dix-huit, vu dans l'épisode deux.",
    ], vis={
        "g9": dict(type="globe", code="H2", sc=[15]),
        "en": dict(type="liste", titre="Un ennemi de la nation par régime", cles=["koulaks", "Juifs", "ennemis"], items=[
            "URSS : les koulaks (dossier documentaire)", "Allemagne : Juifs, Roms, prostituées, homosexuels, handicapés",
            "Italie : les « ennemis de l'État » (Tribunal spécial)"], x=150, y=150, w=980),
        "cons": dict(type="def", cles=["complot", "intérieur"], terme="Allemagne · une théorie du complot",
                     t="La nation serait minée par des ennemis de l'intérieur.",
                     etape="Sa racine : le mythe du coup de poignard dans le dos, 1918 (épisode 2)", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : le dossier documentaire sur la terreur
    dict(id="ws4", chap="À toi · le dossier documentaire sur la terreur", fond="aube", humeur="calme",
         retenir="Six similitudes : police au-dessus des lois · terreur d'apparence légale · ennemis par catégorie · camps et travail forcé · terreur contre les siens · même fonction : gouverner. Différences : échelle, critère, contre-pouvoirs en Italie.",
         beats=[
        "{ex1}À toi. Voici la consigne du dossier documentaire. {!trouve les similitudes}Trouve les similitudes dans l'usage de la violence "
        "par les trois régimes. Vise cinq ou six. Pour chacune, donne un exemple pour chaque régime.",
        "{-ex1}{pa1}",
        ("P", 2.0),
        "{-pa1}{sim}Voici les six similitudes. "
        "{sim.1}Un. Une police politique au-dessus des lois : l'OVRA, la Gestapo et la SS, le NKVD. "
        "{sim.2}Deux. Une terreur qui prend le masque de la légalité. Pense à la loi de défense de l'État de mille neuf cent vingt-six, "
        "aux lois de Nuremberg de mille neuf cent trente-cinq, et aux procès de Moscou. "
        "{sim.3}Trois. Des ennemis désignés par catégorie, et non pour ce qu'ils ont fait : les ennemis de l'État, les Juifs, les koulaks. La violence devient préventive. "
        "{sim.4}Quatre. Le camp comme système, et le travail forcé comme ressource : Dachau, le Goulag. "
        "{sim.5}Cinq. Une terreur qui frappe les hommes du régime : la nuit des Longs Couteaux, et Iejov. "
        "{sim.6}Et six. La même fonction : gouverner. Éliminer les rivaux. Détruire toute organisation autonome. "
        "Produire la peur qui rend docile.",
        "{-sim}{dif}Mais une bonne réponse ne s'arrête jamais aux similitudes. "
        "{dif.1}D'abord, l'échelle. L'Italie est de loin la moins meurtrière. "
        "{dif.2}Ensuite, le critère. Il est social en Union soviétique, biologique en Allemagne, et politique en Italie. "
        "{dif.3}Enfin, l'Italie a laissé subsister des contre-pouvoirs : la monarchie, et l'Église, avec le concordat de mille neuf cent vingt-neuf.",
        "{-dif}{ccl}La conclusion proposée par le cours : les trois terreurs étaient "
        "{!identiques par la méthode, inégales par l'ampleur}identiques par la méthode et par le but. Mais elles étaient inégales par l'ampleur, "
        "et par le principe qui désigne la victime.",
    ], vis={
        "ex1": dict(type="exo", niveau="quiz", titre="Trouve les similitudes dans l'usage de la violence par les trois régimes",
                    src="Le dossier documentaire sur la terreur", enonce=["Cinq ou six similitudes", "Un exemple par régime pour chacune"]),
        "pa1": dict(type="pause", t="Fais la liste des similitudes, avec un exemple par régime pour chacune.",
                    sous="Mets la vidéo en pause, écris ta liste, puis relance pour voir les réponses."),
        "sim": dict(type="liste", titre="Le dossier documentaire · six similitudes", petit=True, items=[
            "Une police politique au-dessus des lois : OVRA · Gestapo et SS · NKVD",
            "Une terreur à l'apparence légale : loi de défense de l'État 1926 · lois de Nuremberg 1935 · procès de Moscou",
            "Des ennemis par catégorie, non par leurs actes : « ennemis de l'État » · Juifs · koulaks",
            "Le camp comme système, le travail forcé comme ressource : Dachau · le Goulag",
            "Une terreur qui frappe les hommes du régime : Longs Couteaux 1934 · Iejov 1940",
            "La même fonction : gouverner, par la peur"], x=110, y=90, w=1060),
        "dif": dict(type="liste", titre="… mais trois différences", items=[
            "L'échelle : l'Italie, de loin la moins meurtrière", "Le critère : social (URSS) · biologique (Allemagne) · politique (Italie)",
            "Des contre-pouvoirs en Italie : la monarchie, l'Église (concordat, 1929)"], x=150, y=150, w=980),
        "ccl": dict(type="mot", t="Même méthode, ampleur inégale", g="identiques par la méthode et le but · inégales par l'ampleur et par le principe qui désigne la victime", y=240, taille=76),
    }),

    # ================================================================ le tableau des totalitarismes (1)
    dict(id="tableau1", chap="Le tableau des totalitarismes · prise du pouvoir et idéologie", fond="aube", humeur="calme",
         retenir="Prise du pouvoir : Italie oct. 1922 (squadristi, le roi) · Allemagne 30 janv. 1933 (élections, Hindenburg, décret du Reichstag, pleins pouvoirs) · URSS dès 1924, lutte au sein du parti. Idéologie : même méthode ; nation · race · classe.",
         beats=[
        "{tb}Rassemblons tout dans le tableau des totalitarismes du cours, rempli jusqu'où le cours est allé. "
        "Il a cinq blocs. {tb.1}La prise du pouvoir. {tb.2}L'idéologie. {tb.3}La dictature. {tb.4}Le terrorisme d'État. {tb.5}Une société contrôlée. "
        "C'est une synthèse des parties un et deux. Si tu sais le remplir de mémoire, tu es prêt.",
        "{-tb}{t1}Premier bloc : la prise du pouvoir. D'abord, la date. {t1.1}L'Italie : octobre mille neuf cent vingt-deux. "
        "Après la marche sur Rome, Mussolini est nommé président du Conseil. L'État devient totalitaire à partir de mille neuf cent vingt-cinq. "
        "{t1.2}L'Allemagne : le trente janvier mille neuf cent trente-trois. Hitler devient chancelier. Il obtient les pleins pouvoirs en mars. "
        "{t1.3}L'Union soviétique : tout commence en mille neuf cent vingt-quatre, à la mort de Lénine. "
        "Le pouvoir de Staline est consolidé vers mille neuf cent vingt-huit ou vingt-neuf.",
        "{-t1}{t2}Ensuite, les causes. {t2.1}En Italie : la victoire mutilée, le Biennio Rosso, la peur du communisme, et un parlement faible. "
        "{t2.2}En Allemagne : la défaite de mille neuf cent dix-huit, le diktat de Versailles, et le mythe du coup de poignard dans le dos. "
        "Puis la crise de mille neuf cent vingt-neuf, avec environ six millions de chômeurs. "
        "{t2.3}En Union soviétique : l'État tsariste s'effondre dans la guerre. Viennent ensuite les révolutions de mille neuf cent dix-sept, "
        "et une guerre civile qui dure jusqu'en mille neuf cent vingt-deux.",
        "{-t2}{t3}Puis, le processus. {t3.1}L'Italie : d'abord la violence des squadristi, puis une nomination légale par le roi. "
        "{t3.2}L'Allemagne : les élections, avec trente-sept pour cent des voix en juillet mille neuf cent trente-deux. "
        "Puis la nomination par Hindenburg, le décret pris après l'incendie du Reichstag, et la loi des pleins pouvoirs. "
        "{t3.3}L'Union soviétique : une lutte au sein du parti, et Trotski expulsé en mille neuf cent vingt-neuf. Aucune voie électorale.",
        "{-t3}{t4}Deuxième bloc : l'idéologie. {t4.1}Ici, les points communs sont les mêmes pour les trois. Une seule vérité. "
        "Le rejet de la démocratie libérale. Le contrôle total. Un homme nouveau. Et une violence tenue pour légitime. "
        "Ces traits communs, c'est exactement ce que veut dire le mot totalitarisme. "
        "{t4.2}Puis, les spécificités. L'Italie : la nation et l'État absolu, et pas de racisme avant mille neuf cent trente-huit. "
        "{t4.3}L'Allemagne : la lutte des races, l'antisémitisme, et le Lebensraum. "
        "{t4.4}L'Union soviétique : la lutte des classes, l'abolition de la propriété privée, et le socialisme dans un seul pays.",
    ], vis={
        "tb": dict(type="liste", titre="Le tableau du cours · cinq blocs", items=[
            "Prise du pouvoir : date, causes, processus", "Idéologie : points communs, spécificités",
            "Dictature : culte, soutiens, parti, symboles, slogans", "Terrorisme d'État : police, opposants",
            "Une société contrôlée : jeunesse, pensée, économie, administration"], x=150, y=110, w=980),
        "t1": dict(type="liste", titre="Tableau · prise du pouvoir : la date", marques=["IT", "DE", "SU"], items=[
            "Oct. 1922 : marche sur Rome, nommé président du Conseil ; État totalitaire dès 1925",
            "30 janv. 1933 : chancelier ; pleins pouvoirs en mars 1933",
            "À partir de 1924 (mort de Lénine) ; pouvoir consolidé vers 1928-1929"], x=150, y=140, w=980),
        "t2": dict(type="liste", titre="Tableau · prise du pouvoir : les causes", marques=["IT", "DE", "SU"], petit=True, items=[
            "« Victoire mutilée », Biennio Rosso, peur du communisme, parlement faible",
            "Défaite de 1918, « diktat » de Versailles, mythe du coup de poignard dans le dos, crise de 1929, ≈ 6 millions de chômeurs",
            "Effondrement de l'État tsariste dans la guerre, révolutions de 1917, guerre civile jusqu'en 1922"], x=130, y=150, w=1020),
        "t3": dict(type="liste", titre="Tableau · prise du pouvoir : le processus", marques=["IT", "DE", "SU"], petit=True, items=[
            "Violence des squadristi, puis nomination légale par le roi",
            "Élections (37 % en juillet 1932), Hindenburg, décret de l'incendie du Reichstag, loi des pleins pouvoirs",
            "Lutte au sein du parti, Trotski expulsé en 1929 : aucune voie électorale"], x=130, y=150, w=1020),
        "t4": dict(type="liste", titre="Tableau · l'idéologie", marques=["=", "IT", "DE", "SU"], petit=True, items=[
            "Commun aux trois : une seule vérité, pas de démocratie libérale, contrôle total, un homme nouveau, violence légitime",
            "La nation et l'État absolu ; pas raciste avant 1938",
            "Lutte des races, antisémitisme, Lebensraum",
            "Lutte des classes, pas de propriété privée, « socialisme dans un seul pays »"], x=130, y=120, w=1020),
    }),

    # ================================================================ le tableau des totalitarismes (2)
    dict(id="tableau2", chap="Le tableau des totalitarismes · dictature, terreur, société", fond="aube", humeur="calme",
         retenir="Dictature : Duce / Führer / petit père · PNF / NSDAP / PCUS · faisceau / croix gammée / faucille et marteau. Terreur : OVRA, Tribunal spécial / Gestapo, SS / NKVD, Goulag. Société : Balilla / Hitlerjugend / Komsomol. Partie III à remplir.",
         beats=[
        "{t5}Troisième bloc : la dictature. {t5.1}Le culte de la personnalité. Il Duce. Der Führer. "
        "Et le petit père des peuples, avec une ville rebaptisée Stalingrad en mille neuf cent vingt-cinq. "
        "{t5.2}Le parti unique. En Italie, le Parti national fasciste. En Allemagne, le Parti nazi. En Union soviétique, le Parti communiste. "
        "{t5.3}Les symboles : le faisceau romain, la croix gammée, la faucille et le marteau. "
        "{t5.4}Et les slogans. Il Duce ha sempre ragione : le Duce a toujours raison. Heil Hitler. "
        "Et : Merci, camarade Staline, pour notre enfance heureuse.",
        "{-t5}{t6}Ensuite, les soutiens. Ces régimes ne reposaient pas sur la seule terreur. "
        "{t6.1}En Italie : les propriétaires terriens, les commerçants, les anciens combattants, la monarchie, et l'Église. "
        "{t6.2}En Allemagne : les classes moyennes, les élites conservatrices, les industriels, et l'armée. "
        "{t6.3}En Union soviétique : l'appareil du parti, la bureaucratie, et une partie de la classe ouvrière.",
        "{-t6}{t7}Quatrième bloc, le terrorisme d'État : la leçon d'aujourd'hui. {t7.1}La police politique. "
        "En Italie, l'OVRA et le Tribunal spécial. En Allemagne, la Gestapo et la SS, toutes deux sous Himmler. "
        "En Union soviétique, l'OGPU, puis le NKVD, et le Goulag. "
        "{t7.2}Les opposants. En Italie : les socialistes et les communistes, comme Matteotti. Et les Juifs, à partir de mille neuf cent trente-huit. "
        "{t7.3}En Allemagne : les communistes, les socialistes, les Juifs, les Roms, les homosexuels, les handicapés, et les Témoins de Jéhovah. "
        "{t7.4}En Union soviétique : les koulaks, les ennemis de classe, les vieux bolcheviks, et les officiers de l'armée.",
        "{-t7}{t8}Cinquième bloc : une société contrôlée, vue dans l'épisode quatre. {t8.1}La jeunesse : les Balilla, les Jeunesses hitlériennes de dix à dix-huit ans, et le Komsomol. "
        "{t8.2}La pensée et la culture. En Italie, la presse d'opposition est supprimée. "
        "En Allemagne, l'enseignement racial est obligatoire à partir de mille neuf cent trente-trois. "
        "En Union soviétique, le réalisme socialiste, et les photographies retouchées. "
        "{t8.3}L'économie. Le corporatisme et l'autarcie en Italie. Le réarmement et le plan de quatre ans en Allemagne. "
        "Les plans quinquennaux et la collectivisation en Union soviétique. "
        "{t8.4}Et l'administration. Dans les trois, le parti double ou contrôle l'État.",
        "{-t8}{rest}Deux blocs du tableau sont encore vides : les enjeux internationaux, et la marche à la guerre. "
        "Ils appartiennent à la partie trois, dans les deux prochains épisodes.",
    ], vis={
        "t5": dict(type="liste", titre="Tableau · la dictature", marques=["★", "P", "S", "“"], petit=True, items=[
            "Culte : il Duce · der Führer · « le petit père des peuples » (Stalingrad, 1925)",
            "Parti unique : PNF · NSDAP · Parti communiste (PCUS)",
            "Symboles : le faisceau romain · la croix gammée · la faucille et le marteau",
            "Slogans : « Il Duce ha sempre ragione » · « Heil Hitler » · « Merci, camarade Staline, pour notre enfance heureuse »"],
            x=130, y=120, w=1020),
        "t6": dict(type="liste", titre="Tableau · la dictature : les soutiens", marques=["IT", "DE", "SU"], items=[
            "Propriétaires terriens, commerçants, anciens combattants, la monarchie, l'Église (1929)",
            "Classes moyennes, élites conservatrices, industriels, l'armée",
            "Appareil du parti, bureaucratie, une partie de la classe ouvrière"], x=150, y=140, w=980),
        "t7": dict(type="liste", titre="Tableau · le terrorisme d'État", marques=["⚑", "IT", "DE", "SU"], petit=True, items=[
            "Police : OVRA (1927), Tribunal spécial (1926) · Gestapo et SS sous Himmler · OGPU, NKVD, le Goulag",
            "Opposants : socialistes, communistes (Matteotti, 1924) ; Juifs à partir de 1938",
            "Communistes, socialistes, Juifs, Roms, homosexuels, handicapés, Témoins de Jéhovah",
            "Koulaks, « ennemis de classe », vieux bolcheviks, officiers de l'armée"], x=130, y=120, w=1020),
        "t8": dict(type="liste", titre="Tableau · une société contrôlée", marques=["J", "P", "€", "A"], petit=True, items=[
            "Jeunesse : Balilla · Jeunesses hitlériennes, 10 à 18 ans · Komsomol",
            "Pensée : presse d'opposition supprimée · enseignement racial 1933 · réalisme socialiste, photos retouchées",
            "Économie : corporatisme, autarcie · réarmement, plan de quatre ans · plans quinquennaux, collectivisation",
            "Administration : parti et État confondus · des cadres du parti doublent l'État · le parti contrôle chaque échelon"],
            x=130, y=120, w=1020),
        "rest": dict(type="note", terme="Encore à remplir · partie III", cles=["internationaux", "guerre"],
                     t="Enjeux internationaux (volonté d'expansion, sentiment de supériorité) · Marche à la guerre (nationalisme militaire, alliances).",
                     etape="Épisodes 6 et 7", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : une réponse à une question problématisée
    dict(id="essai", chap="À toi · une question problématisée", fond="aube", humeur="calme",
         retenir="Terreur, principal instrument ? I. Oui, central et permanent (police, camps) · II. Jamais seule : propagande, culte, homme nouveau, masses (Arendt) · III. Inégale : en Italie, légalisée plus qu'industrialisée. Essentielle, pas la seule.",
         beats=[
        "{ex2}Maintenant, une question problématisée. {!Dans quelle mesure}Dans quelle mesure la terreur a-t-elle été le principal instrument des régimes totalitaires ?",
        "{-ex2}{met}Rappelle-toi la méthode. {met.1}Dans quelle mesure, cela veut dire peser. Jamais totalement. Jamais pas du tout. "
        "{met.2}Définis le mot clé dès l'introduction. {met.3}Construis trois parties : ce qui va dans le sens du sujet, ce qui le limite, et la nuance. "
        "{met.4}Et donne une réponse nette, annoncée dans l'introduction, confirmée dans la conclusion.",
        "{-met}{pa2}",
        ("P", 2.0),
        "{-pa2}{plan2}Voici un plan modèle. {plan2.1}Première partie. Oui, la terreur est un instrument central, et permanent. "
        "Pense à la police politique au-dessus des lois. Aux procès de Moscou, et à la Grande Purge, avec ses six cent quatre-vingt mille exécutions. "
        "Aux camps, de Dachau au Goulag. Et à la terreur qui frappe même les hommes du régime. "
        "{plan2.2}Deuxième partie. Mais la terreur n'agit jamais seule. Le totalitarisme, c'est la contrainte par la terreur et la propagande à la fois : "
        "le culte du chef, les rassemblements, les organisations de jeunesse, l'homme nouveau. "
        "Et Hannah Arendt nous prévient : Hitler et Staline avaient besoin de la confiance des masses. "
        "{plan2.3}Troisième partie. La terreur est inégale. L'Italie légalise la répression plutôt que de l'industrialiser. "
        "Et Mussolini doit accepter le roi et l'Église.",
        "{-plan2}{intro}Et voici une introduction modèle. "
        "{intro.1}Le totalitarisme est un régime qui cherche le contrôle total de la société, par la contrainte, pour transformer l'homme selon une idéologie. "
        "Dans l'Italie fasciste, l'Allemagne nazie et l'Union soviétique de Staline, la terreur était partout : la police, les procès, les camps, les purges. "
        "{intro.2}Mais était-elle leur principal instrument ? Ou un instrument parmi d'autres ? "
        "{intro.3}Nous montrerons que la terreur fut un instrument essentiel pour les trois régimes, mais jamais le seul. "
        "Elle agissait avec la propagande et le soutien populaire. Et son ampleur variait beaucoup d'un régime à l'autre.",
    ], vis={
        "ex2": dict(type="exo", niveau="essay", titre="Dans quelle mesure la terreur a-t-elle été le principal instrument des régimes totalitaires ?",
                    src="Question écrite pour cette vidéo, sur les parties I et II", enonce=["Un plan en trois parties", "Puis rédige l'introduction"]),
        "met": dict(type="liste", titre="« Dans quelle mesure » : la méthode", cles=["peser", "Définis", "parties", "réponse"], items=[
            "Peser : jamais « totalement », jamais « pas du tout »", "Définis le mot clé dès l'introduction",
            "Trois parties : dans le sens du sujet · ses limites · la nuance", "Une réponse nette, de l'introduction à la conclusion"],
            x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Rédige ton plan en trois parties, puis ton introduction : définition, problématique, réponse.",
                    sous="Mets la vidéo en pause, rédige sur une feuille, puis relance pour voir un modèle."),
        "plan2": dict(type="liste", titre="Un plan modèle", petit=True, items=[
            "Oui : un instrument central, permanent · police au-dessus des lois, procès de Moscou, Grande Purge (680 000 exécutions), camps, les hommes du régime",
            "Mais jamais seule : terreur + propagande · culte, rassemblements, jeunesse, homme nouveau · Arendt : « la confiance des masses »",
            "Inégale : l'Italie a légalisé plutôt qu'industrialisé · le roi et l'Église sont restés"], x=110, y=120, w=1060),
        "intro": dict(type="liste", titre="Une introduction modèle", petit=True, items=[
            "Définition : le contrôle total de la société, par la contrainte, pour transformer l'homme selon une idéologie",
            "Problématique : le principal instrument, ou un instrument parmi d'autres ?",
            "Réponse : un instrument essentiel des trois régimes, jamais le seul ; avec la propagande et le soutien ; d'ampleur inégale"],
            x=110, y=130, w=1060),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}La terreur est une méthode de gouvernement. Elle est permanente, organisée et planifiée, pour que chacun se censure lui-même. "
        "{carte.2}Ses instruments : une police politique au-dessus des lois, des procès spectacles, et le camp comme institution permanente, de Dachau au Goulag. "
        "{carte.3}Ses victimes : des ennemis désignés par catégorie. Les koulaks, les Juifs, les handicapés. Et même les hommes du régime. "
        "{carte.4}Ses limites : l'Italie a légalisé sa répression plutôt que de l'industrialiser. Et nulle part la terreur n'a régné seule.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : des ambitions hégémoniques. La guerre comme valeur : l'Éthiopie, le Lebensraum, et le Japon.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="LA TERREUR DE MASSE", branches=[
            dict(t="Une méthode", items=["permanente, planifiée", "Arendt : « de l'intérieur »", "l'autocensure"]),
            dict(t="Les instruments", items=["OVRA · Gestapo, SS · NKVD", "procès de Moscou · Grande Purge", "Dachau · le Goulag"]),
            dict(t="Les victimes", items=["koulaks · Juifs · handicapés", "400 000 stérilisés · T4", "Longs Couteaux · Iejov"]),
            dict(t="Les limites", items=["Italie : légalisée", "confino, Tribunal spécial", "terreur + soutien"])]),
        "fin": dict(type="mot", t="Ensuite : des ambitions hégémoniques", g="Épisode 6 · l'Éthiopie, le Lebensraum, le Japon", y=270, taille=64),
    }),
]

QUIZ = [
    dict(q="D'après le cours, qu'est-ce que la terreur dans un régime totalitaire ?",
         r=["Une méthode de gouvernement permanente, organisée et planifiée", "Une réponse exceptionnelle à une crise",
            "Le signe que le régime perd le contrôle", "Un outil utilisé seulement en temps de guerre"], ok=0, voir="def1",
         ex="Arendt : « un moyen de dominer et de terroriser les êtres humains de l'intérieur »."),
    dict(q="Qui dirige à la fois la Gestapo et la SS ?",
         r=["Heinrich Himmler", "Nikolaï Iejov", "Joseph Goebbels", "Ernst Röhm"], ok=0, voir="him",
         ex="À partir de 1936, Himmler tient les deux polices allemandes : la police d'État et la police du parti."),
    dict(q="Combien d'exécutions le dossier compte-t-il pour la Grande Purge de 1937-1938 ?",
         r=["680 000", "85", "70 000", "400 000"], ok=0, voir="purge",
         ex="85 : la nuit des Longs Couteaux · 70 000 : T4 · 400 000 : les stérilisations forcées."),
    dict(q="Qu'était le canal mer Blanche-Baltique ?",
         r=["Le premier grand chantier soviétique réalisé par les détenus du Goulag (1931-1933)", "Un camp nazi près de Munich",
            "Le lieu des procès de Moscou", "Un canal creusé par des opposants italiens relégués"], ok=0, voir="g5",
         ex="227 km creusés en grande partie avec des outils à main : la terreur produisait aussi."),
    dict(q="Dans les camps nazis, quel triangle désignait les détenus politiques ?",
         r=["Rouge", "Vert", "Rose", "Violet"], ok=0, voir="tri",
         ex="Vert : criminels · rose : homosexuels · noir : « asociaux » · violet : Témoins de Jéhovah · jaune ajouté pour les Juifs."),
    dict(q="Qu'a fait le programme T4 entre 1939 et 1941 ?",
         r=["Tuer environ 70 000 Allemands handicapés, surtout dans des chambres à gaz", "Stériliser 400 000 Allemands",
            "Déporter les koulaks", "Organiser les procès de Moscou"], ok=0, voir="bio",
         ex="La loi de stérilisation date de 1933 : environ 400 000 personnes stérilisées, 1933-1945."),
    dict(q="Quel chef de la police soviétique est exécuté en 1940 ?",
         r=["Nikolaï Iejov", "Lavrenti Beria", "Léon Trotski", "Alexeï Rykov"], ok=0, voir="own",
         ex="Beria l'a remplacé ; Trotski est assassiné au Mexique la même année ; Rykov a été fusillé en 1938."),
    dict(q="Comment le cours décrit-il la répression italienne ?",
         r=["Légalisée plutôt qu'industrialisée", "Plus vaste que la terreur soviétique",
            "Fondée sur un critère racial dès 1922", "Organisée dans des camps de concentration en Italie"], ok=0, voir="form",
         ex="Loi de défense de l'État (1926), Tribunal spécial, OVRA (1927), le confino sur des îles éloignées."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 2 « Les régimes totalitaires », partie II.3, avec le dossier documentaire sur la terreur, le tableau des totalitarismes et Hannah Arendt (introduction du chapitre), tel qu'il est rédigé sur le site ; réponses au dossier proposées par le site ; hors du cours : les camps fascistes de Libye (Cyrénaïque, 1930-1933) et les dates de Beria à la tête du NKVD (1938-1945) ; question et modèles écrits pour cette vidéo ; carte animée du chapitre 2 (site).",
    "Citations en traduction française : Hannah Arendt, Les Origines du totalitarisme (1951) ; Grigori Zinoviev et Lev Kamenev, procès de Moscou (1936).",
    "Photographies (via Wikimedia Commons) : Hannah Arendt en 1958 (Barbara Niggl Radloff, Münchner Stadtmuseum, CC BY-SA 4.0) ; les accusés du deuxième procès de Moscou, janvier 1937 (photographe inconnu, domaine public) ; des détenus du Goulag creusant le canal mer Blanche-Baltique, 1932 (photographe inconnu, domaine public).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
