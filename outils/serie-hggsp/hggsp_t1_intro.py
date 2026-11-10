"""HGGSP, thème 1, introduction : « Océans et espace : quelles spécificités ? » — le chapitre en vidéo (pilote HGGSP).

Même chaîne que les vidéos de cours PC et SVT (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les
mots) ; moteur hggsp/serie/moteur.js (identité « salle de crise » du site Ligne rouge), qui ajoute les types scene
(animations et cartes du site jouées par le temps : l'étape k au repère {id.k}, caméra qui zoome), chiffres, chrono
(frise de dates au télétype) et document (pièce surlignée), et les illustrations orbites et kessler.
Contenu : le chapitre « t1-intro » du site (outils/specialites/hggsp/src/data-t1.js), rien au-delà ; les données de
l'épreuve viennent de la page « L'épreuve » du site (data-commun.js) ; le document de l'étude critique est celui du
dossier du thème 1 (data-dossiers.js). Ce qui dépasse le programme est dit « hors programme ».

Avant la voix (déjà fait, à refaire seulement si une animation du site ou une carte de la vidéo change) :
    node outils/serie-hggsp/scenes.js hggsp-t1-intro        → hggsp/serie/illu-hggsp-t1-intro.js
Contrôles : python3 outils/serie-philo/verifier.py hggsp_t1_intro ;
brouillon sans voix : SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py hggsp_t1_intro ;
puis chevauchements.py hggsp-t1-intro et fermer.py hggsp_t1_intro.
"""

SITE = "hggsp"
CODE = "hggsp-t1-intro"
NOTION = "De nouveaux espaces de conquête"
NUM = 1
TITRE = "Océans et espace : quelles spécificités ?"
SUIVANT = "Thème 1 · Axe 1 · Conquêtes, affirmations de puissance et rivalités"
RYTHME = "vivant"
PRONONCIATION = {"Kármán": "Karmane", "Starlink": "Star-linque", "SpaceX": "Spèïce X", "Seabed": "Sibède",
                 "Challenger": "Tchalèndjeur", "Deep": "Dipe", "Galileo": "Galiléo", "Beidou": "Béï-dou",
                 "Falcon": "Falkone", "Crew": "Crou", "Dragon": "Dragonne", "Turner": "Teurneur", "Rice": "Raïsse",
                 "Houston": "Houstonne", "CNUCED": "Cnucède", "BBNJ": "B B N J", "FAO": "F A O", "Iridium": "Iridiomme",
                 "Kosmos": "Kosmosse", "Kessler": "Kesslère", "Montego": "Montégo", "Bay": "Bèï", "Jackson": "Djackson",
                 "Frederick": "Frédérik", "New Space": "Niou Spèïce", "Grotius": "Grotiusse", "V2": "V deux",
                 "Trieste": "Triestte", "Cameron": "Caméronne", "Kingston": "Kinngstonne",
                 "James": "Djèïmse", "John F. Kennedy": "Djonne Èf Kennedy", "URSS": "U R S S", "ZEE": "Z E E",
                 "GPS": "G P S"}

# ---------------------------------------------------------------- étapes de cartes propres à la vidéo
ARCT_DRAPEAU = [dict(date="2 août 2007", titre="Un drapeau sous le pôle Nord", montre=["drapeau", "drapeaut", "pole"], accent=["drapeau"])]
ARCT_FRONT = [
    dict(date="Autrefois", titre="Une banquise d'été étendue", montre=["glace1", "glace1t"]),
    dict(date="Aujourd'hui", titre="La fonte rend l'Arctique plus accessible", montre=["glace2", "glace2t"], cache=["glace1", "glace1t"], accent=["glace2"]),
    dict(date="2 août 2007", titre="Un drapeau russe sous le pôle Nord", montre=["drapeau", "drapeaut", "pole"], cache=["glace2t"], accent=["drapeau"]),
]
ZONES = [
    dict(date="12 milles", titre="Mer territoriale : l'État est souverain", montre=["mt"], accent=["mt"]),
    dict(date="24 milles", titre="Zone contiguë : des contrôles", montre=["zc"], accent=["zc"]),
    dict(date="200 milles", titre="ZEE : des droits sur les ressources", montre=["zee"], accent=["zee"]),
    dict(date="350 milles", titre="Plateau continental, sur dossier", montre=["pc"], accent=["pc"]),
    dict(date="Au-delà", titre="La haute mer et « la Zone »", montre=["zone"], accent=["zone"]),
    dict(date="17 janv. 2026", titre="Traité BBNJ : protéger la haute mer", montre=["amp"], accent=["amp"]),
]
SCS = [
    dict(date="Revendication", titre="La « ligne en neuf traits »", montre=["ligne", "lignet", "cn", "vn", "ph"], accent=["ligne"]),
    dict(date="12 juil. 2016", titre="La sentence arbitrale : pas de « droits historiques »", montre=["pca"], accent=["ligne"]),
]
MONDE = [
    dict(date="1960", titre="Le fond de l'océan atteint", montre=["mariannes"], accent=["mariannes"]),
    dict(date="1962", titre="« Nous choisissons d'aller sur la Lune »", montre=["houston"], accent=["houston"]),
    dict(date="1982", titre="Le droit de la mer", montre=["jamaique", "hm"], accent=["jamaique"]),
    dict(date="2007", titre="Un drapeau sous le pôle", montre=["arctique"], accent=["arctique"]),
    dict(date="2015-2017", titre="Les ressources de l'espace", montre=["lux", "canaveral"], accent=["lux", "canaveral"]),
    dict(date="2016", titre="Une mer disputée", montre=["scs"], accent=["scs"]),
    dict(date="Partout", titre="Qui peut y aller ? Qui peut prendre ? Qui fixe les règles ?"),
]

DOC_RICE = [
    "Nous mettons les voiles sur cette nouvelle mer parce qu'il y a de nouvelles connaissances à acquérir et de nouveaux "
    "droits à conquérir […]. C'est seulement si les États-Unis occupent une position de prééminence que nous pourrons aider "
    "à décider si ce nouvel océan sera une mer de paix ou un nouveau et terrifiant théâtre de guerre. […]",
    "Nous choisissons d'aller sur la Lune. Nous choisissons d'aller sur la Lune au cours de cette décennie, et de faire les "
    "autres choses, non parce qu'elles sont faciles, mais parce qu'elles sont difficiles […].",
]
REF_RICE = ("John F. Kennedy, président des États-Unis, discours à l'université Rice, Houston (Texas), 12 septembre 1962 "
            "(extraits, traduction française ; discours officiel, domaine public).")

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="ocean", humeur="mystere", carton=False, beats=[
        "{arct}Le 2 août 2007. Sous la banquise de l'océan Arctique. "
        "{arct.1}À plus de quatre mille mètres de profondeur, à la verticale exacte du pôle Nord, un bras articulé plante "
        "dans la vase un petit drapeau russe. En titane.",
        ("P", 0.6),
        "{-arct}{q1}Un drapeau… au fond de la mer. Presque personne ne le verra jamais. Alors, pourquoi faire ça ?",
        "{-q1}{q2}Parce que planter un drapeau, c'est dire : cet endroit compte. Et il est à moi.",
        "{-q2}{f0}Sauf que ça ne marche pas comme ça. Ce drapeau n'a {!aucune valeur}aucune valeur juridique.",
        ("P", 0.5),
        "{-f0}{oe}{oe.g}L'océan {oe.d}et l'espace. Deux mondes où l'on ne survit pas. Deux mondes que les États, et maintenant les entreprises, "
        "se disputent. Et deux mondes qui obéissent à des règles très différentes. "
        "{-oe}{plan}{plan.1}On va voir d'abord deux milieux extrêmes, que l'on maîtrise de mieux en mieux. "
        "{plan.2}Puis deux statuts juridiques opposés. "
        "{plan.3}Ensuite, l'expression qui fera ta dissertation : les « dernières frontières ». "
        "{plan.4}Et pour finir, le bac : une dissertation et une étude critique, corrigées.",
        "{-plan}{bac0}Un mot sur l'examen, tout de suite. Ce thème n'est pas à l'écrit en 2027 : il y revient en 2028. "
        "Et il reste un excellent terrain pour le Grand oral. Donc on le travaille sérieusement.",
        "{-bac0}{titre}",
        ("P", 3.4),
    ], vis={
        "arct": dict(type="scene", anim="arctique", etapes=ARCT_DRAPEAU, cam={"0": [0, 0, 700, 700], "1": [170, 150, 360, 360]}, vol=3.2),
        "q1": dict(type="question", t="Un drapeau au fond de la mer : pourquoi faire ?"),
        "q2": dict(type="mot", t="Cet endroit compte.", g="… et il est à moi.", taille=88, y=250),
        "f0": dict(type="note", titre="Droit international", t="Planter un drapeau ne donne aucun droit : ce geste n'a aucune valeur juridique.", y=230),
        "oe": dict(type="cols", g="L'océan", gq="hostile, convoité, découpé en zones", d="L'espace",
                   dq="hostile, convoité, non appropriable", vs="≠"),
        "plan": dict(type="liste", titre="Le dossier", items=[
            "Deux milieux extrêmes, une maîtrise en constante évolution", "Deux statuts juridiques opposés",
            "Les « dernières frontières » ?", "Au bac : une dissertation et une étude critique corrigées"],
            marques=["I", "II", "III", "IV"], x=170, y=140, w=940),
        "bac0": dict(type="note", titre="Au bac", t="Thème 1 : pas à l'écrit en 2027, à l'écrit en 2028. Et toujours au Grand oral.", y=230),
        "titre": dict(type="titre", sur="HGGSP · Thème 1 · Introduction", t="Océans et espace : quelles spécificités ?",
                      sous="De nouveaux espaces de conquête"),
    }),

    # ================================================================ I. deux milieux hostiles
    dict(id="milieux", chap="Deux milieux hostiles", fond="ocean", humeur="mystere",
         retenir="Deux milieux hostiles : on n'y survit qu'enfermé dans une machine. Océan : 71 % du globe, 3 700 m de profondeur moyenne, Challenger Deep ≈ 10 900 m (1960).",
         beats=[
        "{chif}Commençons par un chiffre. {chif.1}L'océan couvre soixante et onze pour cent de la surface du globe. "
        "Soixante et onze ! Et pourtant, c'est un milieu où tu ne survis pas.",
        "{-chif}{alt}Descends avec moi. {alt.1}Au niveau de la mer, tout va bien. "
        "{alt.2}Mais la pression augmente d'environ un bar tous les dix mètres. Et passé deux cents mètres, la lumière a presque disparu. "
        "C'est la nuit. Pour toujours.",
        "{alt.3}En moyenne, l'océan fait environ trois mille sept cents mètres de profondeur.",
        "{alt.4}Et le point le plus profond, Challenger Deep, dans la fosse des Mariannes, descend vers dix mille neuf cents mètres. "
        "{-alt}{tab_tri}Il n'est atteint qu'en 1960, le 23 janvier, par un bathyscaphe, le Trieste. Puis en 2012, par le cinéaste James Cameron, seul.",
        "{-tab_tri}{cmp}Tiens-toi bien. Jusqu'en 2019, {cmp.g}trois personnes seulement étaient descendues au fond de Challenger Deep. "
        "{cmp.d}Sur la Lune, entre 1969 et 1972, douze hommes ont marché.",
        ("P", 0.6),
        "{-cmp}{esp}Et l'espace ? Ce n'est pas mieux. {esp.1}Le vide. {esp.2}Des rayonnements dangereux. "
        "{esp.3}Des écarts de température extrêmes.",
        "{-esp}{def1}Dans les deux cas, même conclusion : l'être humain n'y survit qu'enfermé dans une machine. "
        "Voilà la première spécificité de ces deux espaces : ce sont des {!milieux extrêmes}milieux extrêmes.",
    ], vis={
        "chif": dict(type="chiffres", items=[dict(v=71, apres=" %", t="de la surface du globe est couverte par l'océan", jauge=.71)], y=180),
        "alt": dict(type="scene", anim="t1alt", pas=[0, 1, 2, 3], cam={"0": [0, 150, 640, 230]}, fs=21),
        "tab_tri": dict(type="tableau", img="t1-trieste", de=[1.0, .5, .45], a=[1.18, .45, .4],
                        legende="Le bathyscaphe Trieste hissé hors de l'eau, photographie de l'US Navy (domaine public, Wikimedia Commons)"),
        "cmp": dict(type="cols", g="3", gq="personnes au fond de Challenger Deep (jusqu'en 2019)", d="12",
                    dq="hommes sur la Lune (1969-1972)", vs="≠"),
        "esp": dict(type="liste", titre="L'espace, un milieu hostile", items=["Le vide", "Des rayonnements dangereux",
                                                                           "Des écarts de température extrêmes"], x=230, y=190, w=820),
        "def1": dict(type="def", terme="Milieux extrêmes", t="Océan et espace : l'être humain n'y survit qu'enfermé dans une machine.", y=230),
    }),

    # ================================================================ II. où commence l'espace ?
    dict(id="karman", chap="Où commence l'espace ?", fond="orbite", humeur="mystere",
         retenir="Aucun traité ne fixe la limite de l'espace : la ligne de Kármán (100 km) n'est qu'une convention. Premier objet au-delà : un missile V2 (1944).",
         beats=[
        "{q3}Petite question piège. À quelle altitude commence l'espace ?",
        ("P", 0.8),
        "{-q3}{alt2}Réponse : {!aucun traité}aucun traité ne l'a fixé. Aucun texte international ne trace la limite entre l'air et l'espace. "
        "{alt2.1}La convention la plus utilisée, c'est la ligne de Kármán, à cent kilomètres d'altitude. "
        "Elle est retenue par la Fédération aéronautique internationale. L'armée de l'air américaine, elle, retient quatre-vingts kilomètres.",
        "{-alt2}{cols2}Et ce flou n'a rien d'anodin. Pourquoi ? {cols2.g}Parce que dans l'air, au-dessus de son territoire, l'État est souverain : "
        "c'est son espace aérien. {cols2.d}Dans l'espace, en revanche, personne ne peut s'approprier quoi que ce soit. "
        "Alors, où s'arrête la souveraineté sur les très hautes altitudes ? La question reste ouverte.",
        "{-cols2}{alt3}Maintenant, un détail qui en dit long. {alt3.1}Le premier objet fabriqué par l'homme à dépasser cent kilomètres, "
        "c'est un missile allemand V2, le 20 juin 1944. Il monte à environ cent soixante-seize kilomètres.",
        "{-alt3}{f1}La conquête de l'espace est née d'une {!arme}arme. Retiens bien ça : tu le retrouveras dans tout le thème.",
    ], vis={
        "q3": dict(type="question", t="À quelle altitude commence l'espace ?"),
        "alt2": dict(type="scene", anim="t1alt", pas=[4], cam={"0": [0, 0, 640, 215]}, fs=21),
        "cols2": dict(type="cols", g="Espace aérien", gq="l'État y est souverain", d="Espace extra-atmosphérique",
                      dq="personne ne peut se l'approprier", vs="?"),
        "alt3": dict(type="scene", anim="t1alt", pas=[5], cam={"0": [0, 0, 640, 215]}, fs=21),
        "f1": dict(type="note", titre="À retenir", t="La conquête de l'espace naît d'une arme : le missile V2 (20 juin 1944, environ 176 km).", y=230),
    }),

    # ================================================================ III. une connaissance qui progresse
    dict(id="fonds", chap="Une connaissance qui progresse", fond="ocean", humeur="calme",
         retenir="La connaissance progresse vite mais reste partielle : 6 % des fonds cartographiés en 2017, 27,3 % en juin 2025 (Seabed 2030).",
         beats=[
        "{m2}Deuxième idée : ces milieux, on les connaît mal. Mais de mieux en mieux.",
        "{-m2}{tech}Prends les fonds marins. On navigue sur les océans depuis des siècles, et pourtant leur fond reste en grande partie inconnu. "
        "{tech.1}Le sonar, au vingtième siècle, {tech.2}puis les satellites {tech.3}et les robots sous-marins font avancer la cartographie.",
        "{-tech}{sea}{sea.1}En 2017, six pour cent seulement des fonds étaient cartographiés aux normes modernes. "
        "{sea.2}En juin 2025 : vingt-sept virgule trois pour cent. "
        "Ces chiffres viennent du projet international Seabed 2030, qui veut cartographier tout le plancher océanique d'ici 2030.",
        "{-sea}{par}Et voici le paradoxe. Nous connaissons mieux la surface de Mars, et celle de la Lune, que nos propres fonds marins.",
    ], vis={
        "m2": dict(type="mot", t="Mal connus…", g="… mais de mieux en mieux.", taille=96, y=250),
        "tech": dict(type="cartes", items=[
            dict(ic="radar", t="Le sonar", q="au XXe siècle, l'écho dessine le relief du fond"),
            dict(ic="satellite", t="Les satellites", q="ils mesurent la mer depuis l'orbite"),
            dict(ic="vague", t="Les robots sous-marins", q="ils descendent là où l'humain ne va pas")]),
        "sea": dict(type="chiffres", titre="Fonds marins cartographiés aux normes modernes", items=[
            dict(v=6, apres=" %", t="en 2017", jauge=.06),
            dict(v=27.3, dec=1, apres=" %", t="en juin 2025", jauge=.273, src="Source : Seabed 2030")], y=170),
        "par": dict(type="note", titre="Le paradoxe", t="Les surfaces de Mars et de la Lune sont mieux connues que nos propres fonds marins.", y=230),
    }),

    # ================================================================ IV. l'espace, une ressource
    dict(id="orbites", chap="Les orbites, une ressource", fond="orbite", humeur="lumiere",
         retenir="Trois orbites : basse (200 à 2 000 km), moyenne (≈ 20 000 km : GPS, Galileo, Beidou), géostationnaire (35 786 km). Starlink : plus de 10 000 satellites (mars 2026).",
         beats=[
        "{orb}Dans l'espace, la maîtrise technique a transformé le ciel en ressource. Tout commence avec Spoutnik, en 1957. "
        "Depuis, les satellites se rangent sur trois étages.",
        "{orb.1}L'orbite basse, de deux cents à deux mille kilomètres : les stations spatiales, les satellites d'observation, "
        "et les constellations qui fournissent Internet.",
        "{orb.2}L'orbite moyenne, vers vingt mille kilomètres : les satellites de positionnement. Le GPS américain, "
        "Galileo l'européen, Beidou le chinois.",
        "{orb.3}Et l'orbite géostationnaire, à trente-cinq mille sept cent quatre-vingt-six kilomètres, au-dessus de l'équateur. "
        "Là-haut, un satellite tourne exactement à la vitesse de la Terre. Vu du sol, il paraît immobile : "
        "parfait pour les télécommunications et la météo.",
        "Et l'orbite basse se remplit à toute vitesse. {-orb}{star}{star.1}La constellation Starlink, de l'entreprise SpaceX, "
        "compte à elle seule plus de dix mille satellites en orbite en mars 2026. "
        "Une seule entreprise, des milliers d'engins : c'est du jamais vu.",
    ], vis={
        "orb": dict(type="illu", nom="orbites", x=150, y=86, w=980, h=560),
        "star": dict(type="chiffres", items=[dict(v=10000, avant="plus de ", t="satellites Starlink en orbite en mars 2026",
                                                  src="une seule entreprise : SpaceX")], y=190),
    }),

    # ================================================================ V. des espaces vitaux
    dict(id="vitaux", chap="Deux espaces vitaux", fond="crise", humeur="lumiere", beats=[
        "{q4}Pourquoi tout ça compte autant ? Parce que l'économie mondiale repose sur ces deux espaces.",
        "{-q4}{eco}{eco.1}Plus de quatre-vingts pour cent des échanges mondiaux de marchandises, en volume, passent par la mer. "
        "{eco.2}Et sous la surface courent les câbles sous-marins, qui portent presque toutes les communications entre les continents. "
        "La mer fournit aussi la pêche, les hydrocarbures, des minerais.",
        "{eco.3}Côté espace : le positionnement, les télécommunications, l'observation de la Terre, la météo. "
        "Des services devenus vitaux. L'économie spatiale mondiale dépasse six cents milliards de dollars en 2024.",
        "{-eco}{bil1}Bilan de cette première partie, en trois mots. {bil1.1}Des milieux extrêmes. "
        "{bil1.2}Une maîtrise qui progresse, grâce à la technique. "
        "{bil1.3}Et des espaces devenus vitaux, donc stratégiques. Pour les économies… et pour les armées.",
    ], vis={
        "q4": dict(type="question", t="Pourquoi tout ça compte autant ?"),
        "eco": dict(type="chiffres", items=[
            dict(v=80, avant="+ de ", apres=" %", t="des échanges de marchandises (en volume) passent par la mer", src="CNUCED", taille=84),
            dict(v="Câbles", t="presque toutes les communications intercontinentales", taille=72),
            dict(v=600, avant="+ de ", apres=" Md$", t="pour l'économie spatiale mondiale (2024)", src="Space Foundation", taille=84)], x=50, w=1180, y=200),
        "bil1": dict(type="cartes", items=[
            dict(ic="vague", t="Milieux extrêmes", q="On n'y survit qu'enfermé dans une machine."),
            dict(ic="radar", t="Une maîtrise en progrès", q="Sonar, satellites, robots : on connaît de mieux en mieux."),
            dict(ic="globe", t="Des espaces vitaux", q="Commerce, câbles, satellites : l'économie en dépend.")]),
    }),

    # ================================================================ VI. la mer découpée en zones
    dict(id="mer", chap="La mer, découpée en zones", fond="ocean", humeur="calme",
         retenir="Montego Bay (1982) : mer territoriale 12 milles, zone contiguë 24, ZEE 200, plateau jusqu'à 350 ; au-delà, la haute mer et « la Zone », patrimoine commun de l'humanité (AIFM).",
         beats=[
        "{m3}Passons au droit. Et là, océan et espace s'opposent complètement.",
        "{-m3}{his}Commençons par la mer. Pendant longtemps, la question était simple : à qui appartient-elle ? "
        "{his.1}En 1609, le juriste hollandais Grotius défend la liberté des mers : la mer n'appartient à personne. "
        "C'est hors programme, mais c'est une excellente accroche d'introduction.",
        "{his.2}Peu à peu, une étroite bande côtière revient à l'État riverain : trois milles marins, la portée supposée d'un boulet de canon.",
        "{his.3}Puis, au vingtième siècle, tout s'accélère. En 1945, les États-Unis revendiquent les ressources de leur plateau continental. "
        "{his.4}En 1952, le Chili, le Pérou et l'Équateur réclament deux cents milles, pour protéger leur pêche.",
        "{his.5}Il faut mettre de l'ordre. Ce sera la convention des Nations unies sur le droit de la mer, signée à Montego Bay, "
        "en Jamaïque, le 10 décembre 1982. Elle entre en vigueur en 1994.",
        "{-his}{zon}Regarde bien ce schéma : c'est le cœur du chapitre. Plus on s'éloigne de la côte, moins l'État a de droits. "
        "Les distances se comptent en milles marins, à partir de la ligne de base. Un mille, c'est mille huit cent cinquante-deux mètres.",
        "{zon.1}D'abord la mer territoriale, jusqu'à douze milles, environ vingt-deux kilomètres. Là, l'État est souverain. "
        "Avec une exception : les navires étrangers ont un droit de passage inoffensif.",
        "{zon.2}Ensuite la zone contiguë, jusqu'à vingt-quatre milles. L'État peut y faire des contrôles douaniers et sanitaires.",
        "{zon.3}Puis la grande : la ZEE, la zone économique exclusive, jusqu'à deux cents milles, environ trois cent soixante-dix kilomètres. "
        "Attention, ce n'est plus de la souveraineté ! Ce sont des droits souverains sur les ressources : la pêche, les hydrocarbures, les minerais. "
        "La navigation, elle, reste libre.",
        "{zon.4}Le plateau continental peut aller jusqu'à trois cent cinquante milles, sur dossier, quand le plateau géologique se prolonge.",
        "{zon.5}Et au-delà ? La haute mer. Libre pour tous : navigation, pêche, survol, pose de câbles. "
        "Elle couvre près des deux tiers de la surface des océans. Et les grands fonds, au-delà des plateaux continentaux des États, s'appellent « la Zone ». "
        "Ils sont déclarés {!patrimoine commun}patrimoine commun de l'humanité. Leurs ressources minérales sont gérées par l'Autorité "
        "internationale des fonds marins, installée à Kingston, en Jamaïque.",
        "{zon.6}Pendant des décennies, aucun texte ne permettait de protéger la haute mer. C'est l'objet du traité BBNJ, "
        "entré en vigueur le 17 janvier 2026 : on peut désormais y créer des aires marines protégées. Tu le retrouveras dans l'axe 2.",
        "{-zon}{p1}Et voici le piège numéro un des copies. Ne confonds jamais mer territoriale et ZEE. "
        "Dans la mer territoriale, l'État est souverain. Dans sa ZEE, il a seulement des droits sur les ressources : "
        "les navires étrangers y circulent librement.",
    ], vis={
        "m3": dict(type="cols", g="La mer", gq="découpée en zones", d="L'espace", dq="non appropriable", vs="≠"),
        "his": dict(type="scene", anim="mer", pas=[0, 1, 2, 3, 4], fs=20),
        "zon": dict(type="scene", anim="mer", etapes=ZONES, fs=20),
        "p1": dict(type="note", titre="Piège", t="Mer territoriale (12 milles) : souveraineté. ZEE (200 milles) : droits sur les ressources seulement ; la navigation y est libre.", y=210),
    }),

    # ================================================================ VII. l'espace non appropriable
    dict(id="traite", chap="L'espace, non appropriable", fond="orbite", humeur="calme", beats=[
        "{m67}Dans l'espace, la logique est inverse. Le traité sur l'espace extra-atmosphérique est ouvert à la signature "
        "le 27 janvier 1967, et il entre en vigueur le 10 octobre de la même année. {-m67}{l67}Il pose quatre principes.",
        "{l67.1}Un : la liberté d'exploration et d'utilisation, pour tous les États. "
        "{l67.2}Deux, le plus important : l'article deux interdit toute appropriation nationale. Ni de l'espace, ni de la Lune, ni des corps célestes. "
        "{l67.3}Trois : l'article quatre interdit de placer des armes nucléaires en orbite. "
        "{l67.4}Quatre : l'article six rend les États responsables des activités de leurs entreprises.",
        "Mais pourquoi un tel traité, en 1967 ? Remets-le dans son contexte : on est en pleine {!guerre froide}guerre froide. "
        "{-l67}{gf}{gf.g}Les États-Unis craignent que l'URSS s'empare de la Lune. {gf.d}L'URSS craint la même chose des États-Unis. "
        "Et chacun redoute des armes nucléaires en orbite.",
        "{-gf}{def67}Alors, c'est d'abord un traité de limitation des rivalités. Pas d'abord un traité de coopération. "
        "Une nuance que le correcteur appréciera.",
    ], vis={
        "m67": dict(type="mot", t="1967", g="Traité de l'espace : ouvert à la signature le 27 janvier, en vigueur le 10 octobre", taille=150, y=210),
        "l67": dict(type="liste", titre="Traité de l'espace · 27 janvier 1967", items=[
            "Liberté d'exploration et d'utilisation pour tous les États",
            "Article II : aucune appropriation nationale, ni de la Lune, ni des corps célestes",
            "Article IV : pas d'armes nucléaires en orbite",
            "Article VI : les États répondent des activités de leurs entreprises"], x=150, y=130, w=980),
        "gf": dict(type="cols", g="États-Unis", gq="Et si l'URSS s'emparait de la Lune ?", d="URSS",
                   dq="Et si les États-Unis s'emparaient de la Lune ?", vs="1967"),
        "def67": dict(type="def", terme="Le traité de 1967", t="D'abord un traité de limitation des rivalités, négocié en pleine guerre froide.", y=230),
    }),

    # ================================================================ VIII. des zones grises
    dict(id="gris", chap="Des zones grises", fond="crise", humeur="tension",
         retenir="Mer : des zones de souveraineté décroissante (1982). Espace : non appropriable (1967). Mais des zones grises : lois américaine (2015) et luxembourgeoise (2017) sur les ressources spatiales.",
         beats=[
        "{q5}Alors, le droit règle tout ? Pas vraiment. Il reste des zones grises, et la puissance s'y engouffre.",
        "{-q5}{zg}{zg.1}Le traité de 1967 n'interdit pas les armes conventionnelles en orbite. "
        "{zg.2}Il ne dit pas clairement si l'on peut exploiter les ressources des corps célestes. "
        "{zg.3}Et en mer, les revendications se chevauchent ; certains États refusent les décisions de justice.",
        "{-zg}{lux}Un exemple très concret. {lux.1}En 1967, le traité interdit toute appropriation. "
        "{lux.2}Mais le 25 novembre 2015, une loi américaine autorise les entreprises américaines à posséder les ressources "
        "qu'elles extraient d'un astéroïde, ou de la Lune. {lux.3}En 2017, le Luxembourg adopte une loi semblable.",
        "Ces lois ne violent pas ouvertement l'article deux. Elles en contournent l'esprit.",
        "{-lux}{f2}Le droit existe, oui. Mais il dépend de la {!volonté des États}volonté des États de le respecter.",
    ], vis={
        "q5": dict(type="question", t="Le droit règle-t-il tout ?"),
        "zg": dict(type="liste", titre="Les zones grises du droit", items=[
            "Pas d'interdiction des armes conventionnelles en orbite",
            "Exploiter les ressources des corps célestes : rien de clair",
            "En mer : des revendications qui se chevauchent, des décisions de justice refusées"], marques=["?", "?", "?"], x=150, y=150, w=980),
        "lux": dict(type="chrono", titre="Les ressources de l'espace", items=[
            dict(d="1967", t="Traité de l'espace : aucune appropriation (art. II)", c="droit"),
            dict(d="25 nov. 2015", t="Loi américaine : les ressources extraites d'un astéroïde ou de la Lune", c="espace"),
            dict(d="2017", t="Le Luxembourg adopte une loi semblable", c="espace")], x=150, w=980, y=150, h=420),
        "f2": dict(type="note", titre="À retenir", t="Le droit existe, mais il dépend de la volonté des États de le respecter.", y=230),
    }),

    # ================================================================ IX. « dernières frontières »
    dict(id="frontiere", chap="« Dernières frontières » ?", fond="archive", humeur="lumiere", beats=[
        "{m4}On arrive à l'expression la plus importante pour ta dissertation : les « dernières frontières ».",
        "{-m4}{fr}Attention : en français, une frontière, c'est une limite. Mais dans la tradition américaine, la frontière, "
        "c'est autre chose. {fr.1}C'est un front pionnier qui avance. L'idée vient de l'historien Frederick Jackson Turner, en 1893.",
        "{fr.2}En 1960, le président Kennedy la reprend : c'est la « Nouvelle Frontière », et l'espace y occupe une grande place. "
        "{fr.3}Le 12 septembre 1962, à l'université Rice, à Houston, {-fr}{tab_rice}il lance :",
        ("C", "Nous choisissons d'aller sur la Lune au cours de cette décennie, et de faire les autres choses, non parce qu'elles sont faciles, mais parce qu'elles sont difficiles.", "cit62"),
        "{-cit62}{-tab_rice}{dfr}Parler de « dernières frontières », c'est donc suggérer que l'océan et l'espace sont les derniers espaces "
        "à conquérir, après les terres émergées.",
    ], vis={
        "m4": dict(type="mot", t="« Dernières frontières »", g="l'expression clé de ta dissertation", taille=80, y=250),
        "tab_rice": dict(type="tableau", img="t1-rice", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.15, .45, .35],
                         legende="J. F. Kennedy à l'université Rice, 12 septembre 1962, NASA (domaine public)"),
        "fr": dict(type="chrono", titre="Une idée américaine", items=[
            dict(d="1893", t="Turner : la frontière, un front pionnier qui avance", c="droit"),
            dict(d="1960", t="Kennedy : la « Nouvelle Frontière »", c="espace"),
            dict(d="12 sept. 1962", t="Discours de l'université Rice, à Houston", c="espace")], x=170, w=940, y=140, h=420),
        "cit62": dict(type="cit", a="John F. Kennedy", o="université Rice, Houston, 12 septembre 1962", y=200),
        "dfr": dict(type="def", terme="« Dernières frontières »", t="Les derniers espaces à conquérir après les terres émergées : des fronts pionniers. Une représentation à discuter.", y=200),
    }),

    # ================================================================ X. de nouveaux fronts pionniers
    dict(id="pionniers", chap="De nouveaux fronts pionniers", fond="ocean", humeur="tension", beats=[
        "{fp}Et ces fronts pionniers existent bel et bien. {fp.1}Les grands fonds marins, pour leurs minerais. "
        "{fp.2}L'Arctique, que la fonte de la banquise rend plus accessible. {fp.3}La Lune, avec la glace d'eau de son pôle Sud.",
        "Qu'est-ce qui décide qu'un espace devient exploitable ? Deux choses : la technique, et le prix des ressources.",
        "{-fp}{arc2}Revenons à notre drapeau. {arc2.1}Autrefois, l'été, la banquise couvrait une grande partie de l'océan Arctique. "
        "{arc2.2}Avec sa fonte, l'océan devient plus accessible. "
        "{arc2.3}Et le 2 août 2007, une expédition russe plante son drapeau en titane au fond de l'océan, sous le pôle Nord, "
        "à plus de quatre mille mètres.",
        "{-arc2}{sym}Un geste symbolique d'appropriation. Mais sans aucune valeur juridique : on ne s'approprie pas le fond de la mer avec un drapeau.",
    ], vis={
        "fp": dict(type="cartes", items=[
            dict(ic="vague", t="Les grands fonds", q="des minerais convoités"),
            dict(ic="radar", t="L'Arctique", q="plus accessible avec la fonte de la banquise"),
            dict(ic="fusee", t="La Lune", q="la glace d'eau de son pôle Sud")]),
        "arc2": dict(type="scene", anim="arctique", etapes=ARCT_FRONT, cam={"0": [0, 0, 700, 700], "3": [130, 110, 440, 440]}, fs=20),
        "sym": dict(type="note", titre="Symbole", t="Un geste d'appropriation… sans aucune valeur juridique.", y=240),
    }),

    # ================================================================ XI. des frontières au sens politique
    dict(id="lignes", chap="Des lignes disputées", fond="crise", humeur="tension", beats=[
        "{lp}Mais le mot frontière garde aussi son sens habituel : une ligne disputée entre États. "
        "{lp.1}La délimitation des ZEE. {lp.2}Les revendications sur des îlots. {lp.3}Le partage des orbites et des fréquences.",
        "{-lp}{scs}L'exemple le plus brûlant, c'est la mer de Chine méridionale. "
        "{scs.1}La Chine y revendique la plus grande partie de la mer, à l'intérieur d'une ligne en neuf traits.",
        "{scs.2}Les Philippines saisissent un tribunal arbitral. Le 12 juillet 2016, il juge ces « droits historiques » chinois "
        "sans fondement. Pékin rejette la sentence.",
        "{-scs}{bil2}Conclusion : ces espaces ne sont ni vides, ni sans règles. L'expression « dernières frontières » est donc à discuter. "
        "Et c'est exactement ce qu'on te demandera de faire.",
    ], vis={
        "lp": dict(type="liste", titre="Des frontières, au sens politique", items=[
            "La délimitation des ZEE", "Les revendications sur des îlots", "Le partage des orbites et des fréquences"], x=200, y=170, w=880),
        "scs": dict(type="scene", anim="scs", etapes=SCS, x=160, y=86, w=960, h=500, fs=19),
        "bil2": dict(type="note", titre="Bilan", t="Ni des espaces vides, ni des espaces sans règles : « dernières frontières » est une expression à discuter.", y=210),
    }),

    # ================================================================ XII. les entreprises privées
    dict(id="prives", chap="Les entreprises entrent en jeu", fond="orbite", humeur="lumiere", beats=[
        "{m5}Autre nouveauté : les États ne sont plus seuls.",
        "{-m5}{np}{np.g}En mer, les armateurs, les compagnies pétrolières et minières, les opérateurs de câbles, dont les géants du numérique, "
        "pèsent lourd. {np.d}Dans l'espace, on parle de {!New Space}New Space : l'arrivée d'entreprises privées innovantes, "
        "qui font baisser le coût d'accès à l'orbite.",
        "{-np}{tab_fal}Deux dates à retenir. Le 21 décembre 2015, SpaceX réussit pour la première fois à faire revenir se poser "
        "le premier étage d'une fusée Falcon 9. Une fusée qui revient peut resservir.",
        "{-tab_fal}{ch2}{ch2.1}Note bien cette date. {ch2.2}Et le 30 mai 2020, une capsule Crew Dragon de SpaceX emmène deux astronautes de la NASA vers la Station spatiale "
        "internationale : c'est la première mission habitée d'une entreprise privée vers la station.",
        "{-ch2}{monde}Prends du recul, et regarde la carte. {monde.1}Le fond de l'océan, atteint en 1960. "
        "{monde.2}La Lune, promise depuis Houston en 1962. {monde.3}Le droit de la mer, signé en Jamaïque en 1982. "
        "{monde.4}Le drapeau sous le pôle, en 2007. {monde.5}Les lois sur les ressources de l'espace, et les fusées privées de Floride. "
        "{monde.6}Et la mer de Chine méridionale, disputée. {monde.7}Partout, les mêmes questions : qui peut y aller, qui peut prendre, et qui fixe les règles ?",
    ], vis={
        "m5": dict(type="mot", t="Les États ne sont plus seuls", taille=76, y=280),
        "tab_fal": dict(type="tableau", img="t1-falcon", de=[1.0, .5, .5], a=[1.15, .5, .45],
                        legende="Premier étage de Falcon 9 revenu sur sa zone d'atterrissage, décembre 2015, SpaceX (CC0)"),
        "np": dict(type="cols", g="En mer", gq="armateurs, pétroliers, miniers, opérateurs de câbles", d="Dans l'espace",
                   dq="le New Space : des entreprises qui font baisser les coûts", vs="+"),
        "ch2": dict(type="chrono", titre="Le New Space", items=[
            dict(d="21 déc. 2015", t="Le premier étage d'une Falcon 9 revient se poser", c="prive"),
            dict(d="30 mai 2020", t="Crew Dragon : la première mission habitée privée vers la station", c="prive")], x=290, w=700, y=150, h=420),
        "monde": dict(type="scene", anim="frontieres", etapes=MONDE, fs=19,
                      cam={"0": [0, 20, 1000, 420], "1": [600, 100, 400, 172], "2": [80, 60, 400, 172], "3": [100, 90, 400, 172],
                           "4": [380, 0, 400, 172], "5": [110, 0, 500, 215], "6": [600, 110, 400, 172], "7": [0, 20, 1000, 420]}),
    }),

    # ================================================================ XIII. des milieux fragiles
    dict(id="fragiles", chap="Des milieux fragiles et encombrés", fond="orbite", humeur="tension",
         retenir="Des milieux fragiles : plus d'un tiers des stocks de poissons évalués surexploités (FAO, 2024) ; débris en orbite (collision du 10 février 2009, syndrome de Kessler).",
         beats=[
        "{fra}{fra.1}Mais la conquête a un prix. Dans les océans : surpêche, pollution, réchauffement, acidification. "
        "Plus d'un tiers des stocks de poissons évalués sont surexploités, selon la FAO, en 2024.",
        "{-fra}{kes}Et dans l'espace, les débris s'accumulent. Le 10 février 2009, le satellite américain Iridium 33 et le satellite russe "
        "hors service Kosmos 2251 {kes.1}se percutent. C'est la première collision accidentelle entre deux satellites. Des milliers de débris.",
        "{kes.2}Ce danger, le scientifique Donald Kessler l'avait décrit dès 1978 : une réaction en chaîne. Chaque collision crée des débris, "
        "qui provoquent d'autres collisions… jusqu'à rendre certaines orbites inutilisables. C'est le {!syndrome de Kessler}syndrome de Kessler.",
    ], vis={
        "fra": dict(type="chiffres", items=[dict(v="1/3", avant="plus d'", t="des stocks de poissons évalués sont surexploités", src="FAO, 2024")], y=190),
        "kes": dict(type="illu", nom="kessler", x=40, y=90, w=1200, h=540),
    }),

    # ================================================================ XIV. la question directrice
    dict(id="question", chap="La question du thème", fond="crise", humeur="calme", beats=[
        "{m6}Faisons le point. Ces espaces attisent les rivalités de puissance. Mais ils obligent aussi à coopérer, "
        "parce que certains intérêts sont communs.",
        "{-m6}{qd}D'où la question qui guide tout le thème : le droit international peut-il réguler les rivalités nées de l'affirmation "
        "de la puissance, dans les espaces océaniques et extra-atmosphériques ?",
        ("P", 0.8),
        "{-qd}{ax}{ax.1}L'axe 1 étudie les conquêtes, les affirmations de puissance et les rivalités. "
        "{ax.2}L'axe 2, les enjeux diplomatiques et les coopérations. "
        "{ax.3}Et l'objet de travail conclusif en fait une étude de cas : la Chine, à la conquête de l'espace, des mers et des océans.",
        "{-ax}{coop}Et voici un premier indice pour la réponse. {coop.1}Même au plus fort de la guerre froide, Washington et Moscou "
        "signent le traité de 1967. {coop.2}Et même pendant la guerre en Ukraine, Américains et Russes continuent de s'échanger "
        "des sièges vers la Station spatiale internationale : c'est un accord de juillet 2022.",
        "{-coop}{f3}Le droit ne supprime pas les rivalités. Mais il peut les {!encadrer}encadrer.",
    ], vis={
        "m6": dict(type="cols", g="Rivalités", gq="des espaces qui attisent la puissance", d="Coopérations",
                   dq="des intérêts communs", vs="et"),
        "qd": dict(type="question", t="Le droit international peut-il réguler les rivalités de puissance dans les océans et l'espace ?"),
        "ax": dict(type="cartes", items=[
            dict(ic="fusee", t="Axe 1", q="Conquêtes, affirmations de puissance et rivalités"),
            dict(ic="balance", t="Axe 2", q="Enjeux diplomatiques et coopérations"),
            dict(ic="drapeau", t="Objet conclusif", q="La Chine, à la conquête de l'espace, des mers et des océans")]),
        "coop": dict(type="chrono", titre="Coopérer malgré les rivalités", items=[
            dict(d="1967", t="En pleine guerre froide : le traité de l'espace", c="droit"),
            dict(d="Juillet 2022", t="Pendant la guerre en Ukraine : un échange de sièges vers la station", c="espace")], x=290, w=700, y=150, h=420),
        "f3": dict(type="note", titre="Premier indice", t="Le droit ne supprime pas les rivalités, mais il peut les encadrer.", y=230),
    }),

    # ================================================================ XV. les pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="crise", humeur="calme", beats=[
        "{pg}Avant de passer au bac, les cinq pièges qui coûtent des points. "
        "{pg.1}Un : confondre mer territoriale et ZEE. On l'a vu. "
        "{pg.2}Deux : écrire que l'espace n'a pas de règles. Il a un traité depuis 1967… simplement, ce traité est incomplet. "
        "{pg.3}Trois : présenter la ligne de Kármán comme une frontière juridique. C'est une convention technique. "
        "{pg.4}Quatre : prendre l'expression « dernières frontières » pour une évidence. C'est une représentation, à discuter. "
        "{pg.5}Et cinq : oublier les acteurs privés. Le programme les cite explicitement.",
    ], vis={
        "pg": dict(type="liste", titre="Les cinq pièges", items=[
            "Confondre mer territoriale (souveraineté) et ZEE (ressources)",
            "Écrire que l'espace « n'a pas de règles » : il a un traité depuis 1967",
            "Prendre la ligne de Kármán pour une frontière juridique",
            "Prendre « dernières frontières » pour une évidence",
            "Oublier les acteurs privés"], marques=["✗", "✗", "✗", "✗", "✗"], x=150, y=110, w=980),
    }),

    # ================================================================ XVI. la dissertation
    dict(id="dissert", chap="Au bac : la dissertation", fond="archive", humeur="calme", beats=[
        "{m7}Passons à l'épreuve écrite. Quatre heures, et deux exercices. {-m7}{ep}{ep.g}Une dissertation, au choix entre deux sujets. "
        "{ep.d}Et une étude critique d'un ou deux documents, sur un autre thème.",
        "{-ep}{rot}Et la rotation des thèmes ? {rot.1}En 2027, l'écrit porte sur les thèmes 2, 4, 5 et 6 : le thème 1 n'y est pas. "
        "{rot.2}En 2028, il revient, avec les thèmes 2, 3 et 5. "
        "{rot.3}Et au Grand oral, coefficient 8, ce thème reste un excellent terrain, chaque année.",
        "{-rot}{sujet}Entraînons-nous sur un sujet de dissertation, inventé pour l'occasion. "
        "« Les océans et l'espace sont-ils encore des dernières frontières ? »",
        "{sujet.1}Première étape : analyser les termes. « Encore » : le sujet invite à comparer hier et aujourd'hui. "
        "« Dernières frontières », entre guillemets : une expression à discuter. "
        "{sujet.2}Deuxième étape : trouver une problématique, une vraie tension. "
        "{sujet.3}Troisième étape : un plan en deux ou trois parties, avec des exemples datés.",
        "{-sujet}{pz}À toi ! Mets la vidéo sur pause. Prends cinq minutes, une feuille, et cherche une problématique et un plan.{pz.stop}",
        ("P", 2.0),
        "{-pz}{pb}Voici une proposition. La problématique : en quoi l'océan et l'espace, longtemps hors d'atteinte, sont-ils devenus "
        "des espaces convoités et encadrés… ce qui oblige à nuancer l'idée de dernière frontière ?",
        "{-pb}{pl}Et le plan, en trois parties. "
        "{pl.1}Un : des espaces longtemps hors d'atteinte, conquis par la technique. Les milieux hostiles, Challenger Deep en 1960, "
        "Gagarine en 1961 ; une connaissance partielle, vingt-sept pour cent des fonds cartographiés en 2025 ; "
        "et l'ouverture par la technique, de Spoutnik à Starlink.",
        "{pl.2}Deux : des fronts pionniers convoités par les États et les entreprises. Les grands fonds, l'Arctique et le drapeau "
        "russe de 2007, la Lune et son pôle Sud, le New Space.",
        "{pl.3}Trois : des espaces déjà encadrés et partagés, ce qui nuance l'idée de frontière. Montego Bay, le traité de 1967, "
        "le traité BBNJ en vigueur en 2026… mais aussi des zones grises : la loi américaine de 2015, la mer de Chine méridionale.",
        "{-pl}{me}Un conseil : chaque partie répond à une étape de ta problématique. Et chaque paragraphe tient en quatre temps : "
        "une idée, une explication, un exemple précis, daté, chiffré, et une phrase de liaison.",
    ], vis={
        "m7": dict(type="mot", t="L'épreuve écrite", g="4 heures · 2 exercices", taille=96, y=250),
        "ep": dict(type="cols", g="Dissertation", gq="au choix entre deux sujets", d="Étude critique",
                   dq="d'un ou deux documents, sur un autre thème", vs="4 h"),
        "rot": dict(type="liste", titre="Le thème 1 au bac", items=[
            "2027 : pas à l'écrit (thèmes 2, 4, 5 et 6)", "2028 : à l'écrit (thèmes 1, 2, 3 et 5)",
            "Grand oral (coefficient 8) : un excellent terrain, chaque année"], marques=["✗", "✓", "✓"], x=170, y=170, w=940),
        "sujet": dict(type="exo", niveau="dissert", titre="Les océans et l'espace sont-ils encore des « dernières frontières » ?",
                      src="Sujet inventé pour l'entraînement (thème 1, introduction)",
                      questions=["Analyse les termes du sujet", "Trouve une problématique", "Construis un plan en deux ou trois parties"]),
        "pz": dict(type="pause", t="Une problématique et un plan en trois parties pour ce sujet.",
                   sous="Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."),
        "pb": dict(type="def", terme="Problématique", t="En quoi l'océan et l'espace, longtemps hors d'atteinte, sont-ils devenus des espaces convoités et encadrés, ce qui oblige à nuancer l'idée de « dernière frontière » ?", y=170),
        "pl": dict(type="liste", titre="Un plan possible", items=[
            "Des espaces longtemps hors d'atteinte, conquis par la technique — Challenger Deep (1960), 27 % des fonds cartographiés, de Spoutnik à Starlink",
            "Des fronts pionniers convoités par les États et les entreprises — grands fonds, Arctique (2007), pôle Sud lunaire, New Space",
            "Des espaces déjà encadrés et partagés : une frontière à nuancer — Montego Bay, traité de 1967, BBNJ (2026), zones grises"],
            marques=["I", "II", "III"], x=130, y=120, w=1020),
        "me": dict(type="note", titre="Méthode", t="Un paragraphe = une idée, une explication, un exemple daté et chiffré, une phrase de liaison.", y=230),
    }),

    # ================================================================ XVII. l'étude critique
    dict(id="etude", chap="Au bac : l'étude critique", fond="archive", humeur="calme", beats=[
        "{m8}Deuxième exercice : l'étude critique. Entraîne-toi sur un document que tu connais déjà : le discours de Kennedy "
        "à l'université Rice.",
        "{-m8}{doc}Le voici, en deux extraits. Prends le temps de le lire.",
        ("P", 7.0),
        "{-doc}{cons}La consigne : montre comment l'espace devient un enjeu de puissance pour les États-Unis pendant la guerre froide, "
        "puis discute la vision de l'espace que présente le président Kennedy.",
        "{-cons}{met}La méthode tient en trois gestes. {met.1}Présenter : la nature du document, son auteur, la date, le contexte, "
        "le destinataire. {met.2}Analyser : citer un passage court, l'expliquer, apporter une connaissance. "
        "{met.3}Porter un regard critique : qui parle, pour qui, pour quoi faire ? Ce que le document montre… et ce qu'il tait.",
        "{-met}{pz2}À toi ! Présente ce document en trois phrases, et repère deux passages à analyser.{pz2.stop}",
        ("P", 2.0),
        "{-pz2}{docc}{cor}Correction. {cor.1}On présente d'abord. C'est un discours, prononcé par John F. Kennedy, président des États-Unis, "
        "le 12 septembre 1962, à l'université Rice, à Houston. Il s'adresse aux Américains… mais aussi au monde, et à l'URSS.",
        "{cor.2}Le contexte, c'est la guerre froide. Depuis Spoutnik, en 1957, la course à l'espace oppose les deux Grands.",
        "{cor.3}Ensuite, on analyse. Kennedy veut une {docc.1}« position de prééminence » pour les États-Unis : être le premier, "
        "c'est pouvoir décider des règles. Et il redoute que l'espace devienne {docc.2}« un nouveau et terrifiant théâtre de guerre ». "
        "Normal : la conquête de l'espace est née d'une arme.",
        "{cor.4}Enfin, le regard critique. Kennedy parle d'une {docc.3}« mer de paix »… mais à condition que les États-Unis dominent. "
        "Et la suite lui donne en partie raison : en 1967, le traité de l'espace interdit l'appropriation et les armes nucléaires en orbite. "
        "Puis douze hommes marchent sur la Lune, entre 1969 et 1972.",
    ], vis={
        "m8": dict(type="mot", t="L'étude critique", g="un document que tu connais déjà", taille=96, y=250),
        "doc": dict(type="document", titre="Document · le discours de l'université Rice", paras=DOC_RICE, ref=REF_RICE, x=150, w=980, y=96),
        "cons": dict(type="exo", niveau="etude", titre="L'espace, un enjeu de puissance pendant la guerre froide",
                     src="Étude critique d'un document : discours de J. F. Kennedy, 12 septembre 1962",
                     enonce=["Montre comment l'espace devient un enjeu de puissance pour les États-Unis pendant la guerre froide, "
                             "puis discute la vision de l'espace que présente le président Kennedy."]),
        "met": dict(type="liste", titre="La méthode", items=[
            "Présenter : nature, auteur, date, contexte, destinataire",
            "Analyser : citer, expliquer, apporter une connaissance",
            "Porter un regard critique : ce que le document montre… et ce qu'il tait"], x=150, y=170, w=980),
        "pz2": dict(type="pause", t="Présente le document en trois phrases et repère deux passages à analyser.",
                    sous="Mets la vidéo sur pause, cherche sur une feuille, puis reprends pour la correction."),
        "docc": dict(type="document", mode="coin", titre="Le document", paras=DOC_RICE, ref=REF_RICE, x=40, w=520,
                     marques=["position de prééminence", "un nouveau et terrifiant théâtre de guerre", "mer de paix"]),
        "cor": dict(type="liste", titre="Corrigé express", petit=True, items=[
            "Présenter : un discours de J. F. Kennedy, 12 septembre 1962, université Rice",
            "Contexte : la guerre froide, la course à l'espace depuis Spoutnik (1957)",
            "Analyser : la « prééminence » américaine ; l'espace, « théâtre de guerre » possible",
            "Critiquer : une « mer de paix »… sous domination américaine ; le traité de 1967"], x=600, y=110, w=640),
    }),

    # ================================================================ XVIII. récap
    dict(id="recap", chap="Récap pour le bac", fond="crise", humeur="lumiere", beats=[
        "{dat}Il est temps de tout ranger. Les dates, d'abord. {dat.1}1944, le V2. {dat.2}1960, le Trieste au fond de Challenger Deep. "
        "{dat.3}1962, le discours de Rice. {dat.4}1967, le traité de l'espace. {dat.5}1982, Montego Bay. "
        "{dat.6}2007, le drapeau russe sous le pôle. {dat.7}2009, la première collision de satellites. "
        "{dat.8}2015, le retour du Falcon 9. {dat.9}2016, la sentence sur la mer de Chine méridionale. "
        "{dat.10}Et 2026, le traité BBNJ en vigueur.",
        ("P", 1.8),
        "{-dat}{cm}Et la carte du chapitre. {cm.1}Des milieux extrêmes. {cm.2}Une maîtrise qui progresse. "
        "{cm.3}Deux statuts juridiques opposés. {cm.4}Et des « dernières frontières »… à discuter.",
        ("P", 1.2),
        "{-cm}{qd2}Garde toujours en tête la question du thème : le droit international peut-il réguler les rivalités de puissance "
        "dans ces espaces ?",
        "{-qd2}{fin}Les fiches, les QCM, la frise et les animations du chapitre t'attendent sur le site Ligne rouge : "
        "le lien est dans la description. Prochain dossier : la conquête, et les rivalités de puissance. À très vite.",
        ("P", 2.5),
    ], vis={
        "dat": dict(type="chrono", titre="Les dates du chapitre", items=[
            dict(d="1944", t="Un V2 dépasse 100 km", c="conflit"), dict(d="1960", t="Le Trieste au fond de Challenger Deep", c="mer"),
            dict(d="1962", t="Discours de Rice", c="espace"), dict(d="1967", t="Traité de l'espace", c="droit"),
            dict(d="1982", t="Montego Bay", c="droit"), dict(d="2007", t="Drapeau russe sous le pôle", c="conflit"),
            dict(d="2009", t="Première collision de satellites", c="espace"), dict(d="2015", t="Le Falcon 9 revient se poser", c="prive"),
            dict(d="2016", t="Sentence sur la mer de Chine", c="conflit"), dict(d="2026", t="Traité BBNJ en vigueur", c="mer")],
            x=60, w=1160, y=120, h=470),
        "cm": dict(type="carte", centre="Océan et espace", branches=[
            dict(t="Milieux extrêmes", items=["71 % du globe", "Challenger Deep (1960)", "Kármán : 100 km"]),
            dict(t="Une maîtrise qui progresse", items=["27,3 % des fonds (2025)", "trois orbites", "Starlink : plus de 10 000"]),
            dict(t="Deux statuts opposés", items=["Montego Bay (1982)", "traité de l'espace (1967)", "zones grises (2015)"]),
            dict(t="Dernières frontières ?", items=["fronts pionniers", "lignes disputées (2016)", "New Space, débris"])]),
        "qd2": dict(type="question", t="Le droit international peut-il réguler les rivalités de puissance dans ces espaces ?"),
        "fin": dict(type="mot", t="Ligne rouge", g="Fiches, QCM, frise et animations : le lien est dans la description.", taille=110, y=250),
    }),
]

QUIZ = [
    dict(q="Quelle part des fonds marins était cartographiée aux normes modernes en juin 2025 ?",
         r=["Environ 6 %", "Environ 27 %", "Environ 60 %", "Plus de 90 %"], ok=1,
         ex="27,3 % en juin 2025 selon Seabed 2030, contre 6 % en 2017 : la connaissance progresse vite, mais reste très incomplète.", voir="sea"),
    dict(q="La ligne de Kármán (100 km) est…", r=["la limite fixée par le traité de 1967", "une convention technique, sans valeur juridique",
                                                  "la limite de la ZEE", "l'altitude de l'orbite géostationnaire"], ok=1,
         ex="Aucun traité ne fixe la limite de l'espace ; les 100 km sont une convention de la Fédération aéronautique internationale.", voir="alt2"),
    dict(q="Quel est le premier objet humain à avoir dépassé 100 km d'altitude ?", r=["Spoutnik (1957)", "Un missile allemand V2 (1944)",
                                                                                  "La capsule de Gagarine (1961)", "Une fusée Falcon 9 (2015)"], ok=1,
         ex="Un V2 lancé le 20 juin 1944 monte à environ 176 km : la conquête de l'espace est née d'une arme.", voir="alt3"),
    dict(q="À quelle altitude se trouve l'orbite géostationnaire ?", r=["400 km", "2 000 km", "20 000 km", "35 786 km"], ok=3,
         ex="À 35 786 km, au-dessus de l'équateur, un satellite tourne à la vitesse de la Terre et paraît immobile.", voir="orb"),
    dict(q="Dans sa ZEE, un État côtier…", r=["exerce une souveraineté totale", "peut interdire tout passage de navire étranger",
                                             "a des droits souverains sur les ressources", "n'a aucun droit particulier"], ok=2,
         ex="La ZEE (200 milles) donne des droits sur les ressources, pas la souveraineté : la navigation y reste libre.", voir="zon"),
    dict(q="Qui gère les ressources minérales des fonds de la haute mer (« la Zone ») ?",
         r=["L'Organisation maritime internationale", "L'Autorité internationale des fonds marins", "Le Conseil de sécurité", "Chaque État riverain"], ok=1,
         ex="L'Autorité internationale des fonds marins, installée à Kingston (Jamaïque), gère ce patrimoine commun de l'humanité.", voir="zon"),
    dict(q="Que dit l'article II du traité de l'espace de 1967 ?", r=["L'espace appartient aux premiers arrivés",
                                                                      "Aucune appropriation nationale de l'espace et des corps célestes",
                                                                      "Les satellites militaires sont interdits", "Seules les entreprises peuvent exploiter la Lune"], ok=1,
         ex="Article II : non-appropriation. Les satellites militaires ne sont pas interdits ; seules les armes nucléaires en orbite le sont (article IV).", voir="l67"),
    dict(q="Qu'a fait une expédition russe le 2 août 2007 ?", r=["Elle a revendiqué la Lune", "Elle a planté un drapeau au fond de l'Arctique, sous le pôle Nord",
                                                                 "Elle a coupé un câble sous-marin", "Elle a lancé le premier satellite russe"], ok=1,
         ex="Un geste symbolique d'appropriation, sans valeur juridique, qui illustre les nouveaux fronts pionniers.", voir="arc2"),
    dict(q="Qu'appelle-t-on le « New Space » ?", r=["La station spatiale chinoise", "L'arrivée d'entreprises privées innovantes dans le spatial",
                                                    "Le retour des États-Unis sur la Lune", "Une zone de la haute mer"], ok=1,
         ex="Des entreprises comme SpaceX font baisser le coût d'accès à l'orbite : premier retour d'un étage de Falcon 9 le 21 décembre 2015.", voir="np"),
    dict(q="Quelle est la question directrice du thème 1 ?", r=["Faut-il interdire la conquête spatiale ?",
                                                                "Le droit international peut-il réguler les rivalités de puissance dans les océans et l'espace ?",
                                                                "Les océans sont-ils plus importants que l'espace ?", "La Chine est-elle la première puissance spatiale ?"], ok=1,
         ex="Elle relie les rivalités (axe 1) et les coopérations (axe 2) ; la Chine en offre une étude de cas.", voir="qd"),
]

CREDITS = [
    "Cartes : fond Natural Earth (domaine public), projections d3-geo (licence ISC) ; banquise de l'Arctique et ligne en neuf traits : tracés schématiques.",
    "Document : discours de John F. Kennedy à l'université Rice, 12 septembre 1962 (discours officiel, domaine public), extraits traduits.",
    "Chiffres : Seabed 2030, CNUCED, Space Foundation, FAO ; sujet de dissertation et étude critique inventés pour l'entraînement.",
    "Photographies : le bathyscaphe Trieste, US Navy (domaine public) ; J. F. Kennedy à l'université Rice, NASA (domaine public) ; "
    "premier étage de Falcon 9 revenu se poser, décembre 2015, SpaceX (CC0) ; via Wikimedia Commons.",
]
