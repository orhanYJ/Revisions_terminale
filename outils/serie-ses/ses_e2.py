"""SES, É2 : « Quels sont les fondements du commerce international et de l'internationalisation de la production ? » —
le chapitre en vidéo.

Même chaîne que le pilote ses_e1.py (outils/serie-philo/generer.py, voix clonée, calage des visuels sur les mots) ;
moteur ses/serie/moteur.js ; illustrations propres à la vidéo dans ses/serie/illu-ses-e2.js (courbe de l'éléphant,
chaîne de valeur de l'A320).
Contenu : le chapitre É2 du site « Faits & Courbes » (outils/specialites/ses/src/data-e2.js, data-anim-e2.js), rien
au-delà. Graphiques, chaînes causales et animations lus dans les sources du site (site_ses.py). Les sujets corrigés sont
ceux du site ; le sujet de partie 3 est celui du bac 2026 (jour 1), avec le corrigé du site. Le coût salarial unitaire
est illustré par un exemple chiffré inventé, signalé comme tel. Les nombres lus par la voix sont écrits en lettres.
Usage : python3 outils/serie-philo/verifier.py ses_e2 ; SERIE_MOTEUR=muet python3 outils/serie-philo/generer.py ses_e2
(brouillon sans voix) ; chevauchements.py ses-e2.
"""
import site_ses

SITE = "ses"
CODE = "ses-e2"
NOTION = "Le commerce international"
NUM = 2
TITRE = "Quels sont les fondements du commerce international et de l'internationalisation de la production ?"
SUIVANT = "É3 · Comment lutter contre le chômage ?"
RYTHME = "vivant"
PRONONCIATION = {"Stolper-Samuelson": "Stolpeur-Samuelsonne", "Smoot-Hawley": "Smoute-Hôlé", "Smith": "Smisse",
                 "Heckscher": "Èkchère", "Ohlin": "Ouline", "Samuelson": "Samuelsonne", "Wassily": "Vassili",
                 "Leontief": "Léontiéf", "Krugman": "Krougmane", "Melitz": "Mélitz", "Milanovic": "Milanovitch",
                 "Christoph": "Christophe", "Lakner": "Lakneur", "Autor": "Otor", "Dorn": "Dorne", "Hanson": "Hannsonne",
                 "Friedrich": "Fridrik", "List": "Liste", "Stellantis": "Stélanntisse", "Volkswagen": "Volkswagène", "Airbus": "Èrbusse", "pays A": "pays ah", "pays B": "pays bé", "§A": "ah",
                 "Mercedes": "Mèrcédèsse", "BMW": "bé-èm-vé", "Apple": "Apeul", "iPhone": "aïe-faune", "iSuppli": "aïe-Soupplaï",
                 "Xing": "Ching", "Detert": "Détèrte", "Tianjin": "Tiène-djine", "Bangladesh": "Banngladèche",
                 "GATT": "Gatte", "OMC": "o-èm-cé", "OCDE": "o-cé-dé-eu", "IDE": "i-dé-eu", "HOS": "ache-o-èss",
                 "dumping": "deumpingue", "design": "dizaïne", "marketing": "markètingue", "PIB": "pé-i-bé",
                 "SES": "èss-eu-èss"}

D = site_ses.donnees()
G, CHN, CH = D["graphes"], D["chaines"], D["ch"]["e2"]
CHIF = CH["chiffres"]          # les trois « En chiffres » du chapitre : 24 430 · 3,6 % · −69,2

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="canard", humeur="mystere", carton=False, beats=[
        "{q_auto}Une voiture française vendue en Allemagne. Une voiture allemande vendue en France. "
        "Les deux pays fabriquent la même chose… et pourtant, ils l'échangent. Pourquoi ?",
        "{-q_auto}{q_iph}Autre énigme. Un smartphone « fabriqué en Chine ». Quelle part de sa valeur est vraiment produite en Chine ?",
        "{-q_iph}{cf_iph}{cf_iph.1}Pour l'iPhone trois G, en deux mille neuf : trois virgule six pour cent. "
        "Six dollars cinquante, sur cent soixante-dix-huit dollars quatre-vingt-seize. Et pourtant, tout l'appareil est compté comme une exportation chinoise.",
        "{-cf_iph}{q_ouv}Alors, sur quoi repose le commerce mondial ? Qui y gagne, qui y perd ? Et que valent les droits de douane ?",
        "{-q_ouv}{plan}Voilà le chemin. {plan.1}D'abord, le commerce mondial en chiffres. "
        "{plan.2}Puis les avantages comparatifs : Ricardo, et les dotations en facteurs. {plan.3}Le commerce entre pays qui se ressemblent. "
        "{plan.4}La productivité des firmes, et la compétitivité. {plan.5}La chaîne de valeur mondiale. "
        "{plan.6}Les gagnants et les perdants, et le débat entre libre-échange et protectionnisme. "
        "{plan.7}Et pour finir, le bac : un calcul, les trois parties de l'épreuve composée, et la dissertation.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q_auto": dict(type="question", t="Pourquoi la France et l'Allemagne s'échangent-elles des voitures ?"),
        "q_iph": dict(type="question", t="Un smartphone fabriqué en Chine : quelle part de sa valeur est chinoise ?"),
        "cf_iph": dict(type="chiffres", titre="En chiffres", x=110, y=150, w=1060, items=[dict(n=CHIF[1]["n"], l=CHIF[1]["l"], s=CHIF[1]["s"])]),
        "q_ouv": dict(type="question", t="Qui y gagne, qui y perd ? Et que valent les droits de douane ?"),
        "plan": dict(type="liste", titre="Le chemin", x=170, y=70, w=940, items=[
            "Le commerce mondial en chiffres", "Les avantages comparatifs : Ricardo, les dotations",
            "Le commerce entre pays comparables", "Productivité des firmes et compétitivité",
            "La chaîne de valeur mondiale", "Gagnants, perdants ; libre-échange ou protectionnisme",
            "Au bac : calcul, épreuve composée, dissertation"]),
        "titre": dict(type="titre", sur="SES · Terminale · É2", t="Les fondements du commerce international",
                      sous="Le chapitre complet, de zéro au bac"),
    }),

    # ================================================================ I. en chiffres
    dict(id="chiffres", chap="Le commerce mondial en chiffres", fond="nuit", humeur="lumiere",
         retenir="Commerce mondial 2024 (OMC) : 24 430 milliards $ de marchandises, 8 690 milliards $ de services ; Chine : 3 580 milliards $. "
                 "Solde commercial = exportations − importations de biens ; France 2025 : −69,2 milliards € (Douane).",
         beats=[
        "{def_ci}Commençons par les mots. Le commerce international, c'est l'échange de biens et de services entre pays. "
        "{def_ci.1}Une {!exportation}exportation, c'est une vente à un non-résident. Une importation, un achat à un non-résident.",
        "{-def_ci}{gr_monde}Et ça pèse combien ? {gr_monde.1}En deux mille vingt-quatre, selon l'Organisation mondiale du commerce, "
        "les exportations mondiales de marchandises atteignent vingt-quatre mille quatre cent trente milliards de dollars : plus de vingt-quatre mille milliards ! Plus deux pour cent sur un an.",
        "{gr_monde.2}Les services commerciaux : huit mille six cent quatre-vingt-dix milliards. Plus neuf pour cent : ils progressent bien plus vite.",
        "{gr_monde.3}Et la Chine, à elle seule ? Trois mille cinq cent quatre-vingts milliards de dollars de marchandises. "
        "Environ quinze pour cent du total : c'est le premier exportateur mondial de marchandises. Le premier importateur, ce sont les États-Unis.",
        "{-gr_monde}{def_solde}Deuxième outil : le {!solde commercial}solde commercial. Les exportations, moins les importations de biens. "
        "{def_solde.1}Négatif, c'est un déficit. Positif, un excédent. Et le taux de couverture, ce sont les exportations divisées par les importations, fois cent.",
        "{-def_solde}{gr_fr}Et la France ? {gr_fr.1}En deux mille vingt-cinq, d'après la Douane, elle exporte six cent quatorze virgule sept milliards d'euros de biens. "
        "{gr_fr.2}Elle en importe sept cent trois virgule six milliards. {gr_fr.3}Et le solde officiel : moins soixante-neuf virgule deux milliards. Un déficit.",
        "Attention : la différence des deux barres ne donne pas ce solde. Les importations sont mesurées à l'arrivée, transport et assurance compris. "
        "Le solde officiel compare exportations et importations sur la même base.",
        "Ce déficit s'améliore : environ moins soixante-dix-neuf milliards en deux mille vingt-quatre. Grâce aux matériels de transport, l'aéronautique et l'automobile, "
        "aux produits pharmaceutiques, et à une facture énergétique plus faible.",
        "{-gr_fr}{note_def}Mais ne dramatise pas. Un déficit n'est pas en soi une {!perte}perte. Il traduit aussi un pays qui consomme et investit plus qu'il ne produit. "
        "Et qui achète des biens intermédiaires, utiles à ses entreprises.",
        "{-note_def}",
    ], vis={
        "def_ci": dict(type="def", terme="Commerce international", cles=["exportation", "importation"],
                       t="L'échange de biens et de services entre pays.",
                       etape="Exportation : une vente à un non-résident · importation : un achat à un non-résident.", x=170, y=180, w=940),
        "gr_monde": dict(type="donnees", g=G["e2-monde"], dec=2, signe=False, x=110, y=100, w=1060, h=500),
        "def_solde": dict(type="def", terme="Solde commercial", cles=["déficit", "excédent"],
                          t="Exportations moins importations de biens : négatif, un déficit ; positif, un excédent.",
                          etape="Taux de couverture = exportations ÷ importations × 100.", x=170, y=180, w=940),
        "gr_fr": dict(type="donnees", g=G["e2-france"], signe=False, x=110, y=100, w=1060, h=500),
        "note_def": dict(type="note", titre="Un déficit n'est pas une perte", cles=["consomme", "intermédiaires"],
                         t="Le pays consomme et investit plus qu'il ne produit, et achète des biens intermédiaires utiles à ses entreprises.",
                         x=170, y=200, w=940),
    }),

    # ================================================================ II. Ricardo
    dict(id="ricardo", chap="L'avantage comparatif", fond="canard", humeur="lumiere",
         retenir="Avantage absolu (Smith, 1776) : produire avec moins de travail. Avantage comparatif (Ricardo, 1817) : produire avec un "
                 "coût d'opportunité plus faible. Même le pays moins productif en tout gagne à l'échange.",
         beats=[
        "{q_ric}Voici la grande question du chapitre. Pourquoi les pays échangent-ils ? Et surtout : est-ce que tout le monde y gagne ?",
        "{-q_ric}{au_smith}Première réponse : Adam Smith, en mille sept cent soixante-seize, dans La Richesse des nations. "
        "Chaque pays doit se spécialiser dans les biens pour lesquels il a un {!avantage absolu}avantage absolu : ceux qu'il produit avec moins de travail que les autres.",
        "Logique. Mais il y a un problème. Un pays moins productif en tout, sans aucun avantage absolu… serait exclu de l'échange ?",
        "{-au_smith}{au_ric}David Ricardo répond non, en mille huit cent dix-sept. Même un pays moins productif en tout gagne à l'échange, "
        "s'il se spécialise là où son désavantage est le plus faible. C'est l'{!avantage comparatif}avantage comparatif. "
        "Et chez Ricardo, il repose sur des différences de technologie : de productivité du travail.",
        "{-au_ric}{an_ric}Prenons son exemple, le plus célèbre de l'économie. {an_ric.1}Deux pays, deux biens : le drap et le vin. "
        "Pour produire une unité, l'Angleterre a besoin de cent heures de travail pour le drap, et de cent vingt pour le vin. "
        "Le Portugal : quatre-vingt-dix heures pour le drap, quatre-vingts pour le vin.",
        "{an_ric.2}Regarde : le Portugal est plus productif dans les deux biens. Il a un avantage absolu partout. Alors, l'échange est-il inutile ?",
        "{an_ric.3}Non. Comparons les coûts relatifs. En Angleterre, produire un drap, c'est renoncer à cent sur cent vingt : environ zéro virgule quatre-vingt-trois unité de vin. "
        "Au Portugal, quatre-vingt-dix sur quatre-vingts : un virgule cent vingt-cinq. Le drap coûte relativement moins cher en Angleterre. "
        "Avantage comparatif anglais : le drap. Portugais : le vin.",
        "{an_ric.4}Sans échange, chaque pays produit une unité de chaque bien. Le monde dispose de deux draps, et de deux unités de vin.",
        "{an_ric.5}Maintenant, chacun se spécialise. L'Angleterre met ses deux cent vingt heures dans le drap : deux virgule deux draps. "
        "Le Portugal met ses cent soixante-dix heures dans le vin : deux virgule cent vingt-cinq unités de vin.",
        "{an_ric.6}Avec exactement le même travail, le monde produit zéro virgule deux drap, et zéro virgule cent vingt-cinq unité de vin, en plus. "
        "L'échange partage ce gain. Les deux pays y gagnent.",
        ("P", 0.8),
        "{-an_ric}{def_co}Retiens la notion clé : le {!coût d'opportunité}coût d'opportunité. C'est ce à quoi on renonce pour produire un bien : "
        "la quantité de l'autre bien qu'on aurait pu produire à la place. "
        "{def_co.1}Avoir un avantage comparatif, c'est produire un bien avec un coût d'opportunité plus faible que les autres pays.",
        "{-def_co}{ch_ric}{ch_ric.1}La chaîne causale. Chaque pays compare ses coûts relatifs. "
        "{ch_ric.2}Donc il se spécialise là où son avantage est le plus grand, ou son désavantage le plus faible. "
        "{ch_ric.3}Donc, avec les mêmes heures de travail, la production mondiale augmente. "
        "{ch_ric.4}Donc, en échangeant, chaque pays consomme plus qu'en autarcie.",
        "{ch_ric.tout}",
        ("P", 1.4),
        "{-ch_ric}",
    ], vis={
        "q_ric": dict(type="question", t="Pourquoi échanger ? Et tout le monde y gagne-t-il ?"),
        "au_smith": dict(type="auteur", mono="AS", nom="Adam Smith", info="1723-1790 · La Richesse des nations, 1776", cles=["absolu"],
                         t="Chaque pays doit se spécialiser là où il a un avantage absolu : produire avec moins de travail que les autres.",
                         x=170, y=210, w=940),
        "au_ric": dict(type="auteur", mono="DR", nom="David Ricardo", info="1772-1823 · Des principes de l'économie politique et de l'impôt, 1817",
                       cles=["comparatif", "technologie"],
                       t="Même un pays moins productif en tout gagne à l'échange s'il se spécialise là où son désavantage est le plus faible : l'avantage comparatif, fondé sur la technologie.",
                       x=170, y=210, w=940),
        "an_ric": dict(type="sanim", nom="e2-ricardo", x=60, y=88, h=520, w=1160),
        "def_co": dict(type="def", terme="Coût d'opportunité", cles=["renonce"],
                       t="Ce à quoi on renonce pour produire un bien : la quantité de l'autre bien qu'on aurait pu produire.",
                       etape="Avantage comparatif : produire un bien avec un coût d'opportunité plus faible que les autres pays.", x=170, y=180, w=940),
        "ch_ric": dict(type="chaine", c=CHN["e2-ricardo"], x=190, w=900),
    }),

    # ================================================================ III. dotations
    dict(id="dotations", chap="Les dotations factorielles", fond="moutarde", humeur="lumiere",
         retenir="HOS : un pays se spécialise dans les biens qui utilisent intensément son facteur relativement abondant. "
                 "Paradoxe de Leontief (1953) : le travail qualifié compte. Les avantages comparatifs se construisent (Corée du Sud).",
         beats=[
        "{q_hos}Ricardo explique l'avantage comparatif par la technologie. Mais il existe une autre source de différences entre pays.",
        "{-q_hos}{def_dot}Leurs {!dotations factorielles}dotations factorielles : les quantités de facteurs de production dont un pays dispose. "
        "Du travail plus ou moins qualifié, du capital, des terres, des ressources naturelles.",
        "{-def_dot}{au_hos}C'est le modèle H, O, S : Heckscher, Ohlin et Samuelson. Un pays se spécialise dans les biens qui utilisent intensément "
        "le facteur dont il est {!relativement abondant}relativement abondant. Parce que ce facteur y est relativement bon marché.",
        "{-au_hos}{ch_hos}{ch_hos.1}Prenons le Bangladesh. Il est relativement abondant en travail peu qualifié. "
        "{ch_hos.2}Donc ce facteur y est relativement bon marché. {ch_hos.3}Donc les biens qui en utilisent beaucoup, le textile, l'habillement, "
        "y sont produits à bas coût. {ch_hos.4}Donc il se spécialise dans ces biens, il les exporte, et il importe des biens intensifs en capital, ou en travail qualifié.",
        "{-ch_hos}{cols_dot}Deux exemples à retenir. {cols_dot.g}Le Bangladesh, riche en travail peu qualifié, est devenu l'un des premiers exportateurs mondiaux de vêtements. "
        "{cols_dot.d}L'Australie, riche en terres et en minerais, exporte surtout des matières premières, du minerai de fer, du charbon, et des produits agricoles.",
        "{-cols_dot}{au_leo}Mais en mille neuf cent cinquante-trois, Wassily Leontief fait une découverte gênante. "
        "Les États-Unis sont riches en capital. Ils devraient donc exporter des biens intensifs en capital. "
        "Or leurs exportations sont plus intensives en travail que leurs importations ! C'est le {!paradoxe}paradoxe de Leontief.",
        "{-au_leo}{note_leo}L'explication ? Il faut distinguer le travail {!qualifié}qualifié. Les États-Unis en sont très bien dotés. "
        "Les dotations comprennent donc aussi le capital humain, et la technologie.",
        "{-note_leo}{li_coree}Dernière idée, importante : les avantages comparatifs ne sont pas figés. Ils se {!construisent}construisent. "
        "{li_coree.1}Par l'investissement, l'éducation, les politiques industrielles. "
        "{li_coree.2}Dans les années mille neuf cent soixante, la Corée du Sud exportait surtout des produits textiles. "
        "{li_coree.3}Aujourd'hui, c'est un grand exportateur de semi-conducteurs, d'automobiles et de navires.",
        "{-li_coree}",
    ], vis={
        "q_hos": dict(type="question", t="D'où vient l'avantage comparatif, en dehors de la technologie ?"),
        "def_dot": dict(type="def", terme="Dotations factorielles", cles=["facteurs"],
                        t="Les quantités de facteurs de production dont dispose un pays : travail plus ou moins qualifié, capital, terres, ressources naturelles.",
                        x=170, y=190, w=940),
        "au_hos": dict(type="auteur", mono="HOS", nom="Heckscher, Ohlin et Samuelson", info="1919, 1933, années 1940 · le modèle HOS",
                       cles=["abondant", "marché"],
                       t="Un pays se spécialise dans les biens qui utilisent intensément le facteur dont il est relativement abondant, donc relativement bon marché.",
                       x=170, y=210, w=940),
        "ch_hos": dict(type="chaine", c=CHN["e2-hos"], x=170, w=940),
        "cols_dot": dict(type="cols", g="Bangladesh", gq="Abondant en travail peu qualifié : l'un des premiers exportateurs mondiaux de vêtements.",
                         d="Australie", dq="Abondante en terres et en minerais : minerai de fer, charbon, produits agricoles.", vs="≠",
                         repere="Chacun exporte ce qu'il produit avec son facteur abondant"),
        "au_leo": dict(type="auteur", mono="WL", nom="Wassily Leontief", info="1905-1999 · Nobel 1973", cles=["paradoxe"],
                       t="1953 : les exportations des États-Unis, pays riche en capital, sont plus intensives en travail que leurs importations : le « paradoxe de Leontief ».",
                       x=170, y=210, w=940),
        "note_leo": dict(type="note", titre="La clé du paradoxe", cles=["qualifié", "humain"],
                         t="Les États-Unis sont abondants en travail qualifié : les dotations comprennent aussi le capital humain et la technologie.",
                         x=170, y=200, w=940),
        "li_coree": dict(type="liste", titre="Des avantages qui se construisent", x=170, y=170, w=940, items=[
            "Par l'investissement, l'éducation, les politiques industrielles",
            "Corée du Sud, années 1960 : surtout des produits textiles",
            "Aujourd'hui : semi-conducteurs, automobiles, navires"], marques=["→", "1960", "auj."]),
    }),

    # ================================================================ IV. pays comparables
    dict(id="comparables", chap="Le commerce entre pays comparables", fond="corail", humeur="calme",
         retenir="Commerce intra-branche : des pays semblables échangent des produits semblables. Différenciation horizontale (variété) "
                 "et verticale (qualité), économies d'échelle (Krugman, Nobel 2008), fragmentation de la chaîne de valeur.",
         beats=[
        "{q_comp}Mais Ricardo et HOS ont un angle mort. Ils expliquent bien les échanges entre pays différents : des vêtements contre des avions. "
        "Or une grande partie du commerce mondial se fait entre pays riches et semblables… qui échangent des produits semblables.",
        "{-q_comp}{def_intra}On appelle ça le {!commerce intra-branche}commerce intra-branche : l'échange de produits d'une même branche entre deux pays. "
        "La France exporte des voitures en Allemagne, et en importe. {def_intra.1}À l'inverse, le commerce inter-branche échange des produits de branches différentes.",
        "{-def_intra}{ca_raisons}Le programme en cite trois raisons. {ca_raisons.1}La différenciation des produits : les consommateurs aiment la variété. "
        "C'est la différenciation horizontale : même qualité, mais des marques, des styles, des modèles différents.",
        "{ca_raisons.2}La qualité des produits : c'est la différenciation verticale, des gammes de qualité et de prix différentes. "
        "Un même pays importe de l'entrée de gamme, et exporte du haut de gamme.",
        "{ca_raisons.3}Et la fragmentation de la chaîne de valeur : les pays s'échangent des pièces et des composants d'un même produit. On y revient tout à l'heure.",
        "{-ca_raisons}{au_krug}La théorie, c'est Paul Krugman, prix Nobel deux mille huit. Sa nouvelle théorie du commerce international, en mille neuf cent soixante-dix-neuf "
        "et mille neuf cent quatre-vingt, repose sur deux idées : les {!économies d'échelle}économies d'échelle, et le goût pour la variété.",
        "{-au_krug}{ch_krug}{ch_krug.1}Déroulons. Des rendements croissants : plus une firme produit, plus son coût unitaire baisse. "
        "{ch_krug.2}Donc chaque firme se concentre sur quelques variétés, produites en grande série. "
        "{ch_krug.3}Or les consommateurs aiment la variété : ils veulent choisir entre plusieurs marques, plusieurs modèles. "
        "{ch_krug.4}Donc des pays semblables échangent des variétés d'un même produit. "
        "{ch_krug.5}Résultat : plus de choix, et des prix plus bas, pour les consommateurs des deux pays.",
        "{-ch_krug}{cols_auto}L'exemple type : l'automobile, entre la France et l'Allemagne. Renault et Stellantis vendent des voitures en Allemagne. "
        "Volkswagen, BMW et Mercedes en vendent en France. {cols_auto.g}Les modèles diffèrent par le style et l'image : c'est horizontal. "
        "{cols_auto.d}Et par la gamme : beaucoup de modèles allemands sont positionnés sur le haut de gamme. C'est vertical.",
        "{-cols_auto}{note_ue}Et le marché unique européen, en supprimant les obstacles aux échanges entre pays proches, "
        "a fortement développé ce {!intra-branche}commerce intra-branche.",
        "{-note_ue}",
    ], vis={
        "q_comp": dict(type="question", t="Pourquoi des pays semblables échangent-ils des produits semblables ?"),
        "def_intra": dict(type="def", terme="Commerce intra-branche", cles=["même"],
                          t="L'échange de produits d'une même branche entre deux pays : la France exporte des voitures en Allemagne et en importe.",
                          etape="Commerce inter-branche : des produits de branches différentes.", x=170, y=180, w=940),
        "ca_raisons": dict(type="cartes", items=[
            dict(ic="humain", t="Variété", q="Différenciation horizontale : même qualité, marques et styles différents."),
            dict(ic="brevet", t="Qualité", q="Différenciation verticale : gammes de qualité et de prix différentes."),
            dict(ic="usine", t="Fragmentation", q="Les pays s'échangent les pièces et composants d'un même produit.")]),
        "au_krug": dict(type="auteur", mono="PK", nom="Paul Krugman", info="né en 1953 · Nobel 2008", cles=["échelle", "variété"],
                        t="Nouvelle théorie du commerce international (1979-1980) : les économies d'échelle et le goût pour la variété expliquent le commerce intra-branche.",
                        x=170, y=210, w=940),
        "ch_krug": dict(type="chaine", c=CHN["e2-krugman"], x=170, w=940),
        "cols_auto": dict(type="cols", g="Horizontale", gq="Des modèles qui diffèrent par le style et l'image : Renault, Stellantis ↔ Volkswagen, BMW, Mercedes.",
                          d="Verticale", dq="Des gammes différentes : beaucoup de modèles allemands sont positionnés sur le haut de gamme.", vs="+",
                          repere="L'automobile entre la France et l'Allemagne"),
        "note_ue": dict(type="note", titre="Le marché unique européen", cles=["intra-branche"],
                        t="En supprimant les obstacles aux échanges entre pays proches, il a fortement développé le commerce intra-branche.",
                        x=170, y=200, w=940),
    }),

    # ================================================================ V. compétitivité
    # exemple inventé : 40 / 50 = 0,80 € par objet ; 20 / 20 = 1,00 € par objet
    dict(id="competitivite", chap="Productivité et compétitivité", fond="nuit", humeur="tension",
         retenir="Compétitivité : aptitude à exporter. Prix (coût unitaire, marges, change) et hors-prix (qualité, innovation, marque). "
                 "C'est le coût salarial unitaire qui compte. Seules les firmes les plus productives exportent (Melitz, 2003).",
         beats=[
        "{q_cpt}Pourquoi certains pays exportent-ils plus que d'autres ? Tout commence… dans les entreprises.",
        "{-q_cpt}{def_cpt}La {!compétitivité}compétitivité, c'est l'aptitude d'une entreprise ou d'un pays à vendre ses produits face à la concurrence. "
        "{def_cpt.1}Pour un pays : son aptitude à exporter. À gagner, ou à garder, des parts de marché.",
        "{-def_cpt}{cols_cpt}Elle a deux visages. {cols_cpt.g}La compétitivité-prix : vendre moins cher que les concurrents, à qualité égale. "
        "Elle dépend du coût unitaire de production, donc des salaires et de la productivité, des marges, et du taux de change. "
        "{cols_cpt.d}Et la compétitivité hors-prix : vendre grâce à autre chose que le prix. La qualité, l'innovation, l'image de marque, le design, "
        "le service après-vente, les délais.",
        "{-cols_cpt}{ch_cpt}{ch_cpt.1}Voici le mécanisme central du chapitre. La productivité des firmes augmente : innovation, équipement, organisation, qualification. "
        "{ch_cpt.2}Donc le coût unitaire de production baisse. {ch_cpt.3}Et là, deux voies. La compétitivité-prix : elles peuvent vendre moins cher à l'étranger. "
        "Ou bien des marges plus élevées, qu'elles investissent en recherche, en qualité, dans la marque : la compétitivité hors-prix.",
        "{ch_cpt.4}Dans les deux cas, elles gagnent des parts de marché à l'étranger. {ch_cpt.5}Et les exportations du pays augmentent : il est plus compétitif.",
        "{ch_cpt.tout}",
        ("P", 1.0),
        "{-ch_cpt}{f_csu}Un piège classique : « les salaires sont trop élevés, donc le pays n'est pas compétitif ». Pas si vite. "
        "{f_csu.1}Ce qui compte, c'est le {!coût salarial unitaire}coût salarial unitaire : le coût du travail par unité produite.",
        "{f_csu.2}Prenons un exemple inventé. Dans un pays A, une heure de travail coûte quarante euros, et produit cinquante objets : quatre-vingts centimes par objet. "
        "{f_csu.3}Dans un pays B, l'heure coûte vingt euros, mais ne produit que vingt objets : un euro par objet.",
        "{f_csu.4}Le pays aux salaires deux fois plus élevés produit moins cher ! Un salaire plus élevé n'augmente pas le coût unitaire, si la productivité augmente autant.",
        "{-f_csu}{au_mel}Allons plus loin, à l'intérieur d'un pays. Marc Melitz, en deux mille trois, montre que les firmes d'une même branche ont des productivités très différentes. "
        "On parle de {!firmes hétérogènes}firmes hétérogènes. Et seules les plus productives exportent.",
        "{-au_mel}{ch_mel}{ch_mel.1}Pourquoi ? Parce qu'exporter coûte cher : prospecter, respecter les normes, organiser la logistique, bâtir un réseau commercial. "
        "Ce sont des coûts fixes. {ch_mel.2}Donc seules les firmes les plus productives peuvent les payer, et rester rentables. "
        "{ch_mel.3}Avec l'ouverture, elles grandissent. Les moins productives reculent, ou disparaissent. {ch_mel.4}Donc la productivité moyenne du pays augmente.",
        "{-ch_mel}{ex_aero}Un exemple français : l'aéronautique. {ex_aero.1}Un avion se vend sur sa fiabilité, sa consommation de carburant, le service… bien plus que sur son prix. "
        "C'est de la compétitivité hors-prix. {ex_aero.2}Et en deux mille vingt-cinq, selon la Douane, l'amélioration du solde commercial de la France "
        "est portée par les matériels de transport, en particulier l'aéronautique, et par les produits pharmaceutiques.",
        "{ex_aero.3}Retiens bien ce mécanisme : il est tombé au bac en deux mille vingt-six, en partie trois de l'épreuve composée. On le corrige à la fin.",
        "{-ex_aero}",
    ], vis={
        "q_cpt": dict(type="question", t="Pourquoi certains pays exportent-ils plus que d'autres ?"),
        "def_cpt": dict(type="def", terme="Compétitivité", cles=["aptitude", "exporter"],
                        t="L'aptitude d'une entreprise ou d'un pays à vendre ses produits face à la concurrence.",
                        etape="Pour un pays : son aptitude à exporter, à gagner ou garder des parts de marché.", x=170, y=190, w=940),
        "cols_cpt": dict(type="cols", g="Compétitivité-prix", gq="Vendre moins cher à qualité égale : coût unitaire (salaires, productivité), marges, taux de change.",
                         d="Compétitivité hors-prix", dq="Vendre grâce à autre chose : qualité, innovation, image de marque, design, service, délais.", vs="+"),
        "ch_cpt": dict(type="chaine", c=CHN["e2-compet"], x=170, w=940),
        "f_csu": dict(type="formule", titre="Le coût salarial unitaire · exemple inventé", x=170, y=110, w=940, lignes=[
            dict(f="coût salarial unitaire = coût d'une heure ÷ production par heure", taille=32, cadre=True),
            dict(f="Pays A : 40 € ÷ 50 objets = 0,80 € par objet", taille=34),
            dict(f="Pays B : 20 € ÷ 20 objets = 1,00 € par objet", taille=34),
            dict(f="Salaire deux fois plus élevé, mais coût unitaire plus bas : la productivité compense.", txt=True, pt=True)]),
        "au_mel": dict(type="auteur", mono="MM", nom="Marc Melitz", info="né en 1968 · modèle des firmes hétérogènes, 2003", cles=["hétérogènes", "productives"],
                       t="Au sein d'une même branche, les firmes ont des productivités très différentes : seules les plus productives exportent.",
                       x=170, y=210, w=940),
        "ch_mel": dict(type="chaine", c=CHN["e2-melitz"], x=190, w=900),
        "ex_aero": dict(type="liste", titre="Exemple · l'aéronautique française", x=150, y=150, w=980, items=[
            "Un avion se vend sur sa fiabilité, sa consommation, le service : du hors-prix",
            "2025 : matériels de transport et pharmacie portent l'amélioration du solde (Douane)",
            "Ce mécanisme : partie 3 de l'épreuve composée du bac 2026"], marques=["1", "2", "→"]),
    }),

    # ================================================================ VI. chaîne de valeur
    dict(id="chaine", chap="La chaîne de valeur mondiale", fond="moutarde", humeur="mystere",
         retenir="Chaîne de valeur internationalisée : FMN, IDE (au moins 10 % du capital), sous-traitance. Environ 70 % du commerce passe par "
                 "des chaînes de valeur mondiales (OCDE). iPhone 3G : 6,50 $ d'assemblage chinois sur 178,96 $.",
         beats=[
        "{q_cv}Revenons à notre smartphone « fabriqué en Chine ». Qui le fabrique, vraiment ?",
        "{-q_cv}{def_cv}D'abord, une définition. La {!chaîne de valeur}chaîne de valeur, c'est l'ensemble des étapes qui ajoutent de la valeur à un produit. "
        "La conception, la recherche, la fabrication des composants, l'assemblage, la logistique, le marketing, la vente, les services.",
        "{-def_cv}{def_fmn}Ces étapes, ce sont souvent des firmes multinationales qui les organisent. Une {!firme multinationale}firme multinationale "
        "possède au moins une filiale de production à l'étranger. {def_fmn.1}Elle la crée, ou la rachète, par un investissement direct à l'étranger, un IDE : "
        "une prise de contrôle durable. Par convention, au moins dix pour cent du capital.",
        "{-def_fmn}{ch_cvm}{ch_cvm.1}Le mécanisme. Une firme multinationale découpe sa production en étapes : conception, composants, assemblage, vente. "
        "{ch_cvm.2}Elle place chaque étape là où elle est la plus rentable : selon les coûts, les compétences, l'accès aux marchés, les ressources. "
        "{ch_cvm.3}Soit par des filiales qu'elle contrôle. Soit par des sous-traitants indépendants.",
        "{ch_cvm.4}Donc les biens intermédiaires franchissent plusieurs frontières, avant de devenir un produit final. "
        "{ch_cvm.5}Et les exportations d'un pays contiennent de la valeur ajoutée venue d'autres pays.",
        "{-ch_cvm}{li_pourq}On parle de décomposition internationale des processus productifs. Pourquoi les firmes y recourent-elles ? "
        "{li_pourq.1}Pour réduire leurs coûts : la main-d'œuvre, les impôts. {li_pourq.2}Pour accéder à des compétences. "
        "{li_pourq.3}Pour se rapprocher de leurs marchés. {li_pourq.4}Ou pour contourner des barrières douanières.",
        "{-li_pourq}{cf_70}{cf_70.1}Et c'est massif. Selon l'OCDE, environ soixante-dix pour cent du commerce international fait intervenir des chaînes de valeur mondiales.",
        "{-cf_70}{an_iph}Suivons le voyage d'un iPhone trois G, en deux mille neuf. {an_iph.1}Apple le conçoit aux États-Unis. "
        "Ses composants viennent de fournisseurs de plusieurs pays, notamment le Japon, l'Allemagne, la Corée du Sud, les États-Unis.",
        "{an_iph.2}Ces composants, cent soixante-douze dollars quarante-six par appareil, sont expédiés vers l'usine d'assemblage, en Chine.",
        "{an_iph.3}En Chine, l'usine assemble le téléphone. Valeur ajoutée : six dollars cinquante. Trois virgule six pour cent du coût de fabrication.",
        "{an_iph.4}Puis l'iPhone part vers les États-Unis. Et là, la statistique douanière enregistre une importation de cent soixante-dix-huit dollars "
        "quatre-vingt-seize… en provenance de Chine.",
        "{an_iph.5}Tu vois le problème ? En valeur ajoutée, la Chine n'a produit que six dollars cinquante. Le commerce mesuré en valeur brute exagère son rôle. "
        "D'où l'idée de mesurer le {!valeur ajoutée}commerce en valeur ajoutée.",
        "{-an_iph}{ill_airbus}Un autre exemple, plus proche de nous : l'Airbus A trois cent vingt. "
        "{ill_airbus.1}Des éléments produits en France, en Allemagne, en Espagne, et au Royaume-Uni, où sont fabriquées les ailes. "
        "{ill_airbus.2}Et des lignes d'assemblage final à Toulouse, à Hambourg, à Tianjin en Chine, et à Mobile, aux États-Unis.",
        "{-ill_airbus}{note_reloc}Mais ces chaînes très longues ont un point faible. Les pénuries de deux mille vingt et deux mille vingt et un, les masques, "
        "puis les semi-conducteurs, ont montré leur fragilité. Certaines entreprises, et certains États, cherchent désormais à {!relocaliser}relocaliser, "
        "ou à diversifier leurs fournisseurs.",
        "{-note_reloc}",
    ], vis={
        "q_cv": dict(type="question", t="Fabriqué en Chine : qui le fabrique, vraiment ?"),
        "def_cv": dict(type="def", terme="Chaîne de valeur", cles=["étapes"],
                       t="L'ensemble des étapes qui ajoutent de la valeur à un produit : conception, recherche, composants, assemblage, logistique, marketing, vente, services.",
                       x=170, y=180, w=940),
        "def_fmn": dict(type="def", terme="Firme multinationale (FMN)", cles=["filiale"],
                        t="Une entreprise qui possède au moins une filiale de production à l'étranger.",
                        etape="Créée ou rachetée par un investissement direct à l'étranger (IDE) : une prise de contrôle durable, au moins 10 % du capital par convention.",
                        x=170, y=180, w=940),
        "ch_cvm": dict(type="chaine", c=CHN["e2-cvm"], x=170, w=940),
        "li_pourq": dict(type="liste", titre="Pourquoi découper la production ?", x=170, y=170, w=940, items=[
            "Réduire les coûts : main-d'œuvre, impôts", "Accéder à des compétences", "Se rapprocher des marchés",
            "Contourner des barrières douanières"]),
        "cf_70": dict(type="chiffres", x=170, y=200, w=940, items=[
            dict(n="70 %", l="du commerce international fait intervenir des chaînes de valeur mondiales (environ).", s="OCDE")]),
        "an_iph": dict(type="sanim", nom="e2-iphone", x=60, y=96, h=500, w=1160),
        "ill_airbus": dict(type="illu", nom="airbus", x=80, y=96, w=1120, h=540),
        "note_reloc": dict(type="note", titre="Des chaînes fragiles", cles=["relocaliser", "diversifier"],
                           t="Pénuries de 2020-2021 (masques, puis semi-conducteurs) : certaines entreprises et certains États veulent relocaliser ou diversifier leurs fournisseurs.",
                           x=170, y=190, w=940),
    }),

    # ================================================================ VII. gagnants et perdants
    dict(id="effets", chap="Gagnants et perdants", fond="corail", humeur="mystere",
         retenir="Trois effets : baisse des prix et variété (gains moyens) ; inégalités entre pays en baisse (courbe de l'éléphant) ; "
                 "inégalités au sein des pays riches en hausse (Stolper-Samuelson, choc chinois).",
         beats=[
        "{q_gp}Le commerce international enrichit-il tout le monde ? Le programme attend trois effets.",
        "{-q_gp}{ca_eff}{ca_eff.1}Des gains moyens : la baisse des prix. {ca_eff.2}Une réduction des inégalités entre pays. "
        "{ca_eff.3}Et une hausse des inégalités au sein de chaque pays.",
        "{-ca_eff}{note_prix}Un : la baisse des prix. La spécialisation, les économies d'échelle et la concurrence étrangère abaissent les coûts, et les marges. "
        "Et l'ouverture élargit la variété des produits. {note_prix.1}On parle de gains {!moyens}moyens : ils profitent à l'ensemble des consommateurs… "
        "même s'ils sont inégalement répartis.",
        "{-note_prix}{li_chine}Deux : les inégalités entre pays se réduisent. {li_chine.1}Les pays émergents qui se sont ouverts, et intégrés aux chaînes de valeur, "
        "ont rattrapé une partie de leur retard. {li_chine.2}La Chine, membre de l'OMC depuis décembre deux mille un, est devenue le premier exportateur mondial de marchandises. "
        "{li_chine.3}Leur croissance a fait sortir des centaines de millions de personnes de la pauvreté, et réduit l'écart de revenu moyen avec les pays riches.",
        "{-li_chine}{ill_ele}Cette image, tu dois la connaître : la {!éléphant}courbe de l'éléphant, de Christoph Lakner et Branko Milanovic. "
        "Tous les habitants du monde, rangés du plus pauvre au plus riche. Et en hauteur, la hausse de leur revenu, entre mille neuf cent quatre-vingt-huit et deux mille huit.",
        "{ill_ele.1}Ici, le dos de l'éléphant : les classes moyennes des pays émergents. Leurs revenus ont fortement progressé. "
        "{ill_ele.2}Là, au creux : les classes populaires et moyennes des pays riches. Leurs revenus ont peu progressé. "
        "{ill_ele.3}Et au bout de la trompe, tout en haut : les plus riches du monde. Eux aussi ont beaucoup gagné.",
        "{-ill_ele}{def_ss}Trois : les inégalités au sein de chaque pays peuvent augmenter. Le théorème de Stolper-Samuelson, issu du modèle HOS, "
        "prévoit que l'ouverture profite au facteur abondant… et nuit au facteur {!rare}rare. "
        "{def_ss.1}Et dans un pays riche, le facteur rare, c'est le travail peu qualifié.",
        "{-def_ss}{ch_ineg}{ch_ineg.1}La chaîne. Un pays riche importe davantage de biens intensifs en travail peu qualifié. "
        "{ch_ineg.2}Donc le prix de ces biens baisse sur le marché intérieur. "
        "{ch_ineg.3}Donc les secteurs nationaux concurrencés réduisent leur production et leur emploi. Certaines activités sont délocalisées.",
        "{ch_ineg.4}Donc la demande de travail peu qualifié baisse, et celle de travail qualifié augmente, dans les secteurs exportateurs. "
        "{ch_ineg.5}Et les écarts de salaires et d'emploi, entre qualifiés et peu qualifiés, se creusent.",
        "{-ch_ineg}{au_adh}La démonstration la plus célèbre : le {!choc chinois}choc chinois. Autor, Dorn et Hanson, en deux mille treize. "
        "Les zones des États-Unis les plus exposées à la concurrence des importations chinoises ont perdu durablement des emplois industriels. "
        "Avec des salaires plus bas, et davantage de prestations sociales.",
        "{-au_adh}{note_auto}Une nuance, pour finir. Ces effets se cumulent avec ceux du progrès technique biaisé, l'automatisation. "
        "Et il est difficile de séparer ce qui vient du {!commerce}commerce, et ce qui vient des machines.",
        "{-note_auto}",
    ], vis={
        "q_gp": dict(type="question", t="Le commerce international enrichit-il tout le monde ?"),
        "ca_eff": dict(type="cartes", items=[
            dict(ic="loi", t="Prix", q="Des gains moyens : baisse des prix et plus de variété."),
            dict(ic="infra", t="Entre pays", q="Les inégalités entre pays se réduisent."),
            dict(ic="humain", t="Dans chaque pays", q="Les inégalités au sein des pays peuvent augmenter.")]),
        "note_prix": dict(type="note", titre="Des gains « moyens »", cles=["moyens", "inégalement"],
                          t="Spécialisation, économies d'échelle et concurrence font baisser les prix pour tous les consommateurs, même si ces gains sont inégalement répartis.",
                          x=170, y=190, w=940),
        "li_chine": dict(type="liste", titre="Le rattrapage des pays émergents", x=150, y=150, w=980, items=[
            "Ouverts et intégrés aux chaînes de valeur, ils rattrapent une partie de leur retard",
            "La Chine, membre de l'OMC depuis décembre 2001 : premier exportateur de marchandises",
            "Des centaines de millions de personnes sorties de la pauvreté"]),
        "ill_ele": dict(type="illu", nom="elephant", x=80, y=96, w=1120, h=540),
        "def_ss": dict(type="def", terme="Théorème de Stolper-Samuelson", cles=["abondant", "rare"],
                       t="Issu du modèle HOS : l'ouverture profite au facteur abondant et nuit au facteur rare.",
                       etape="Dans un pays riche, le facteur rare est le travail peu qualifié.", x=170, y=180, w=940),
        "ch_ineg": dict(type="chaine", c=CHN["e2-ineg"], x=170, w=940),
        "au_adh": dict(type="auteur", mono="ADH", nom="Autor, Dorn et Hanson", info="« The China Syndrome », 2013", cles=["chinois", "durablement"],
                       t="Les zones des États-Unis les plus exposées aux importations chinoises ont perdu durablement des emplois industriels : le « choc chinois ».",
                       x=170, y=210, w=940),
        "note_auto": dict(type="note", titre="Commerce ou automatisation ?", cles=["commerce", "machines"],
                          t="Ces effets se cumulent avec ceux du progrès technique biaisé : difficile de séparer le commerce des machines.",
                          x=170, y=200, w=940),
    }),

    # ================================================================ VIII. libre-échange ou protectionnisme
    dict(id="protection", chap="Libre-échange ou protectionnisme ?", fond="canard", humeur="tension",
         retenir="Protectionnisme : droits de douane, quotas, barrières non tarifaires, subventions ; protectionnisme éducateur (List, 1841). "
                 "Un droit de douane protège certains emplois mais renchérit les biens et risque des représailles (Smoot-Hawley, 1930).",
         beats=[
        "{q_le}Alors, faut-il ouvrir les frontières, ou protéger ?",
        "{-q_le}{cols_le}{cols_le.g}Le {!libre-échange}libre-échange, c'est une politique qui supprime les obstacles aux échanges internationaux. "
        "{cols_le.d}Le protectionnisme, une politique qui protège la production nationale de la concurrence étrangère.",
        "{-cols_le}{li_instr}Le protectionnisme a quatre instruments. {li_instr.1}Les droits de douane : des taxes sur les importations. "
        "{li_instr.2}Les quotas : des quantités maximales importées. {li_instr.3}Les barrières non tarifaires : des normes techniques ou sanitaires, des procédures. "
        "{li_instr.4}Et les subventions aux producteurs nationaux.",
        "{-li_instr}{ville_dd}Regardons ce que fait un droit de douane, dans une petite économie. Des entreprises nationales, des ménages, un magasin. "
        "Et le reste du monde, qui vend et qui achète. {ville_dd.1}Le pays relève ses droits de douane. Le prix des biens importés augmente.",
        "{ville_dd.2}Les importations reculent. Les producteurs nationaux protégés vendent davantage : l'emploi est préservé dans ces secteurs.",
        "{ville_dd.3}Mais les consommateurs, et les entreprises qui achètent ces biens, paient plus cher.",
        "{ville_dd.4}Et les partenaires ripostent : ils taxent à leur tour les exportations du pays. "
        "{ville_dd.5}C'est le risque de guerre commerciale. Les échanges, l'emploi exportateur et la croissance reculent.",
        "{-ville_dd}{ch_prot}{ch_prot.1}En chaîne causale, pour ta copie. Un pays relève ses droits de douane. {ch_prot.2}Donc le prix des biens importés augmente. "
        "{ch_prot.3}Les producteurs protégés vendent plus… mais les acheteurs paient plus cher. {ch_prot.4}Et les partenaires ripostent. "
        "{ch_prot.5}D'où le risque de guerre commerciale.",
        "{ch_prot.tout}",
        ("P", 1.0),
        "{-ch_prot}{cmp_arg}Le débat, maintenant, argument contre argument. {cmp_arg.1}Pour le libre-échange : les gains de la spécialisation, "
        "Ricardo et HOS, la baisse des prix, la variété. En face : protéger les industries naissantes, le temps qu'elles deviennent compétitives. "
        "C'est le {!éducateur}protectionnisme éducateur de Friedrich List, en mille huit cent quarante et un.",
        "{cmp_arg.2}Pour le libre-échange : la concurrence pousse les firmes à innover, et seules les plus productives prospèrent. "
        "En face : protéger l'emploi et les territoires frappés par la concurrence, comme lors du choc chinois, et limiter les inégalités internes.",
        "{cmp_arg.3}Pour le libre-échange : la diffusion des technologies, et le rattrapage des pays pauvres. "
        "En face : l'indépendance stratégique. La santé, l'énergie, la défense, les semi-conducteurs.",
        "{cmp_arg.4}Et enfin : le protectionnisme entraîne des représailles, et coûte aux consommateurs. "
        "En face : répondre à une concurrence jugée déloyale. Des subventions, du dumping social ou environnemental.",
        "{-cmp_arg}{fr_hist}L'histoire donne des leçons. {fr_hist.1}Juin mille neuf cent trente : les États-Unis adoptent le tarif Smoot-Hawley. "
        "Les représailles suivent. Et tout cela accompagne l'effondrement du commerce mondial pendant la Grande Dépression.",
        "{fr_hist.2}Après la guerre, le GATT, en mille neuf cent quarante-sept, {fr_hist.3}puis l'OMC, créée le premier janvier mille neuf cent quatre-vingt-quinze, "
        "organisent la baisse négociée des droits de douane.",
        "{fr_hist.4}Et le deux avril deux mille vingt-cinq, les États-Unis annoncent des droits de douane dits « réciproques » : "
        "au moins dix pour cent sur la plupart des importations, et des taux plus élevés pour de nombreux partenaires. "
        "Le protectionnisme est redevenu un instrument politique majeur.",
        "{-fr_hist}{note_inter}Entre les deux, il existe des positions {!intermédiaires}intermédiaires. Un protectionnisme ciblé et temporaire. "
        "Des accords régionaux, comme l'Union européenne. Des clauses sociales et environnementales dans les traités. "
        "Ou le mécanisme d'ajustement carbone aux frontières de l'Union européenne.",
        "{-note_inter}",
    ], vis={
        "q_le": dict(type="question", t="Ouvrir les frontières, ou protéger ?"),
        "cols_le": dict(type="cols", g="Libre-échange", gq="Supprimer les obstacles aux échanges internationaux.",
                        d="Protectionnisme", dq="Protéger la production nationale de la concurrence étrangère.", vs="ou"),
        "li_instr": dict(type="liste", titre="Les instruments du protectionnisme", x=170, y=160, w=940, items=[
            "Droits de douane : des taxes sur les importations", "Quotas : des quantités maximales importées",
            "Barrières non tarifaires : normes techniques ou sanitaires, procédures", "Subventions aux producteurs nationaux"]),
        "ville_dd": dict(type="ville", titre="Les effets d'un droit de douane", kicker="Mécanisme",
                         noms=dict(usine="Producteurs nationaux", monde="Reste du monde"),
                         base=["usine", "magasin", "maisons", "monde"],
                         flux=[dict(de="monde", a="magasin", k="biens", l="importations"), dict(de="usine", a="magasin", k="biens"),
                               dict(de="maisons", a="magasin", k="achats"), dict(de="usine", a="monde", k="biens", l="exportations")],
                         etapes=[
                             dict(prix=dict(sur="magasin", t="PRIX ↑", c="corail"),
                                  etiquette=dict(h="Droit de douane", s="le prix des biens importés augmente", sur="monde")),
                             dict(flux=[dict(de="monde", a="magasin", k="biens", n=.35), dict(de="usine", a="magasin", k="biens", n=1.6),
                                        dict(de="usine", a="maisons", k="revenus", l="salaires", n=1.2)],
                                  etiquette=dict(h="Producteurs protégés", s="ils vendent plus : emploi préservé", sur="usine")),
                             dict(foule=.6, etiquette=dict(h="Acheteurs pénalisés", s="consommateurs et entreprises paient plus cher", sur="maisons")),
                             dict(flux=[dict(de="usine", a="monde", k="biens", n=.25)],
                                  etiquette=dict(h="Représailles", s="les partenaires taxent ses exportations", sur="monde")),
                             dict(etiquette=dict(h="Guerre commerciale", s="échanges, emploi exportateur et croissance reculent", sur="usine"), cam="tout")]),
        "ch_prot": dict(type="chaine", c=CHN["e2-protect"], x=170, w=940),
        "cmp_arg": dict(type="compare", titre="Libre-échange ou protectionnisme : les arguments", x=70, y=86, w=1140,
                        cols=["Libre-échange", "Protectionnisme"], lignes=[
                            ["Gains", "Spécialisation (Ricardo, HOS), baisse des prix, variété.", "Protéger les industries naissantes (List, 1841 : protectionnisme éducateur)."],
                            ["Emploi", "La concurrence pousse à innover ; les plus productives prospèrent (Melitz).", "Protéger l'emploi et les territoires (choc chinois) ; limiter les inégalités."],
                            ["Monde", "Diffusion des technologies, rattrapage des pays pauvres.", "Indépendance stratégique : santé, énergie, défense, semi-conducteurs."],
                            ["Coûts", "Représailles ; un coût pour les consommateurs.", "Répondre à une concurrence jugée déloyale (subventions, dumping)."]]),
        "fr_hist": dict(type="frise", de=1920, a=2035, items=[
            dict(d=1930, nom="Smoot-Hawley", q="tarif américain, représailles"), dict(d=1947, nom="GATT", q="baisse négociée des droits"),
            dict(d=1995, nom="OMC", q="créée le 1er janvier"), dict(d=2025, nom="Droits « réciproques »", q="2 avril : au moins 10 %")]),
        "note_inter": dict(type="note", titre="Des positions intermédiaires", cles=["ciblé", "carbone"],
                           t="Protectionnisme ciblé et temporaire, accords régionaux, clauses sociales et environnementales, ajustement carbone aux frontières de l'UE.",
                           x=170, y=190, w=940),
    }),

    # ================================================================ IX. pièges
    dict(id="pieges", chap="Les pièges à éviter", fond="nuit", humeur="tension", beats=[
        "{cmp_p1}Avant le bac, sept pièges qui coûtent des points. {cmp_p1.1}Un : « un pays moins productif en tout ne peut pas gagner à l'échange ». "
        "Faux ! C'est tout l'apport de Ricardo : il gagne en se spécialisant là où son désavantage est le plus faible.",
        "{cmp_p1.2}Deux : confondre avantage absolu et avantage comparatif. Absolu : produire avec moins de travail que l'autre pays. "
        "Comparatif : produire avec un coût d'opportunité plus faible.",
        "{cmp_p1.3}Trois : « Ricardo explique la spécialisation par les dotations en facteurs ». Non. Ricardo, c'est la technologie, la productivité du travail. "
        "Les dotations, c'est HOS.",
        "{cmp_p1.4}Quatre : « la compétitivité, c'est seulement vendre moins cher ». Il y a aussi le hors-prix. Et c'est le coût unitaire qui compte, pas le salaire seul.",
        "{-cmp_p1}{cmp_p2}{cmp_p2.1}Cinq : « un iPhone importé de Chine, c'est de la valeur ajoutée chinoise ». "
        "En valeur ajoutée, la Chine n'apporte qu'une petite part : trois virgule six pour cent pour l'iPhone trois G.",
        "{cmp_p2.2}Six : « le commerce international augmente les inégalités ». Précise toujours ! Il tend à réduire les inégalités entre pays, "
        "et peut accroître celles au sein de chaque pays.",
        "{cmp_p2.3}Et sept : « le protectionnisme protège l'emploi ». Il protège les emplois des secteurs protégés. Mais il renchérit les biens importés, "
        "pénalise les entreprises qui les utilisent, et peut entraîner des représailles qui détruisent des emplois exportateurs.",
        "{-cmp_p2}",
    ], vis={
        "cmp_p1": dict(type="compare", titre="Les pièges · 1 à 4", x=70, y=86, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["1 · Ricardo", "« Moins productif en tout, il ne gagne rien à l'échange. »", "Faux : il se spécialise là où son désavantage est le plus faible."],
            ["2 · Avantages", "Confondre avantage absolu et comparatif.", "Absolu : moins de travail. Comparatif : un coût d'opportunité plus faible."],
            ["3 · Sources", "« Ricardo, ce sont les dotations. »", "Ricardo : la technologie. HOS : les dotations factorielles."],
            ["4 · Compétitivité", "« C'est seulement vendre moins cher. »", "Il y a aussi le hors-prix ; c'est le coût unitaire qui compte."]]),
        "cmp_p2": dict(type="compare", titre="Les pièges · 5 à 7", x=70, y=96, w=1140, cols=["L'erreur", "Ce qu'il faut écrire"], lignes=[
            ["5 · Valeur ajoutée", "« Un iPhone importé de Chine : de la valeur ajoutée chinoise. »", "En valeur ajoutée, la Chine n'apporte que 3,6 % (iPhone 3G)."],
            ["6 · Inégalités", "« Le commerce augmente les inégalités. »", "Il réduit les inégalités entre pays, peut accroître celles au sein des pays."],
            ["7 · Protection", "« Le protectionnisme protège l'emploi. »", "Ceux des secteurs protégés ; mais prix plus hauts, représailles, emplois exportateurs détruits."]]),
    }),

    # ================================================================ X. au bac
    dict(id="epreuve", chap="Ce chapitre au bac", fond="canard", humeur="lumiere", beats=[
        "{li_ep}Passons au bac. L'écrit de SES dure quatre heures, au coefficient seize. Et tu choisis entre deux sujets. "
        "Soit l'épreuve composée, en trois parties : {li_ep.1}la mobilisation des connaissances, sur trois virgule cinq points, "
        "{li_ep.2}l'étude d'un document, sur cinq virgule cinq points, {li_ep.3}et le raisonnement sur un dossier documentaire, sur neuf points. "
        "{li_ep.4}Soit la dissertation, appuyée sur un dossier documentaire.",
        "Ce barème s'applique à partir de la session deux mille vingt-sept. Et dans les deux sujets, deux points sur vingt sont réservés à l'orthographe et à la syntaxe.",
        "Et le commerce international fait partie des neuf questions du programme qui peuvent tomber à l'écrit.",
        "{-li_ep}{li_aei}Une méthode revient partout : le paragraphe {!AEI}A, E, I. "
        "{li_aei.1}A : affirmer l'idée. {li_aei.2}E : expliquer le mécanisme, avec une chaîne causale, comme celles de ce chapitre. "
        "{li_aei.3}I : illustrer, par un exemple précis, chiffré ou daté.",
        "Mais d'abord, un savoir-faire : calculer des avantages comparatifs.",
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

    # ================================================================ XI. savoir-faire : avantages comparatifs
    # 120/100 = 1,2 ; 80/90 = 0,889 ; 220/100 = 2,2 ; 170/80 = 2,125 ; 1/1,2 = 0,833 ; 1/0,889 = 1,125 (exercice du site)
    dict(id="calcul", chap="Savoir-faire · les avantages comparatifs", fond="nuit", humeur="calme", beats=[
        "{ex_c}Voici l'exercice, sur l'exemple de Ricardo. Pour une unité de drap : cent heures en Angleterre, quatre-vingt-dix au Portugal. "
        "Pour une unité de vin : cent vingt heures en Angleterre, quatre-vingts au Portugal.",
        "{ex_c.1}Un : quel pays a un avantage absolu dans chaque bien ? {ex_c.2}Deux : calcule le coût d'opportunité du vin dans chaque pays, "
        "et déduis-en les avantages comparatifs. {ex_c.3}Trois : montre que la spécialisation augmente la production totale.",
        "Attention au piège : cette fois, on te demande le coût d'opportunité du vin, pas celui du drap.",
        "{-ex_c}{pa_c}À toi. Mets la vidéo sur pause, prends une feuille, et fais les calculs.",
        "{pa_c.stop}{-pa_c}{ex_cc}{ex_cc.q1}Correction. {s_c1}{s_c1.1}Un : le Portugal a un avantage absolu dans les deux biens. "
        "{s_c1.2}Quatre-vingt-dix heures contre cent pour le drap. Quatre-vingts contre cent vingt pour le vin.",
        "{-s_c1}{ex_cc.q2}{s_c2}{s_c2.1}Deux : le coût d'opportunité du vin, ce sont les heures du vin, divisées par les heures du drap. "
        "{s_c2.2}En Angleterre : cent vingt sur cent, un virgule deux unité de drap. {s_c2.3}Au Portugal : quatre-vingts sur quatre-vingt-dix, environ zéro virgule quatre-vingt-neuf.",
        "{s_c2.4}Le vin coûte relativement moins cher au Portugal. Avantage comparatif du Portugal : le vin. Et de l'Angleterre : le drap.",
        "{-s_c2}{ex_cc.q3}{s_c3}{s_c3.1}Trois : sans échange, une unité de chaque bien dans chaque pays : deux draps, et deux unités de vin. "
        "{s_c3.2}Spécialisés : l'Angleterre produit deux cent vingt divisé par cent, deux virgule deux draps. "
        "Le Portugal, cent soixante-dix divisé par quatre-vingts, deux virgule cent vingt-cinq unités de vin.",
        "{s_c3.3}Avec le même travail : plus zéro virgule deux drap, et plus zéro virgule cent vingt-cinq unité de vin.",
        "{s_c3.4}Et une vérification utile. Le coût d'opportunité du drap, c'est l'inverse de celui du vin. Un divisé par un virgule deux : "
        "environ zéro virgule quatre-vingt-trois, comme dans l'animation tout à l'heure. Tout est cohérent.",
        "{-s_c3}{-ex_cc}",
    ], vis={
        "ex_c": dict(type="exo", niveau="calcul", titre="Calculer des avantages comparatifs", src="Exercice du site (exemple de Ricardo)", y=80,
                     enonce=["Pour une unité de drap : 100 h en Angleterre, 90 h au Portugal. Pour une unité de vin : 120 h en Angleterre, 80 h au Portugal."],
                     questions=["Quel pays a un avantage absolu dans chaque bien ?",
                                "Calcule le coût d'opportunité du vin dans chaque pays ; déduis-en les avantages comparatifs.",
                                "Montre que la spécialisation augmente la production totale."]),
        "pa_c": dict(type="pause", t="Avantages absolus, coûts d'opportunité du vin, gain de la spécialisation."),
        "ex_cc": dict(type="exo", mode="coin", niveau="calcul", titre="Les avantages comparatifs",
                      donnees=["Drap : Angleterre 100 h, Portugal 90 h", "Vin : Angleterre 120 h, Portugal 80 h"],
                      questions=["Avantages absolus ?", "Coûts d'opportunité du vin ?", "Gain de la spécialisation ?"]),
        "s_c1": dict(type="formule", titre="1 · Les avantages absolus", x=540, y=170, w=700, lignes=[
            dict(f="Le Portugal : avantage absolu dans les deux biens", txt=True),
            dict(f="drap : 90 h < 100 h · vin : 80 h < 120 h", taille=34)]),
        "s_c2": dict(type="formule", titre="2 · Le coût d'opportunité du vin", x=540, y=120, w=700, lignes=[
            dict(f="CO du vin = heures du vin ÷ heures du drap", taille=32),
            dict(f="Angleterre : 120 ÷ 100 = 1,2 drap", taille=34),
            dict(f="Portugal : 80 ÷ 90 ≈ 0,89 drap", taille=34),
            dict(f="Portugal → vin · Angleterre → drap", cadre=True, taille=34)]),
        "s_c3": dict(type="formule", titre="3 · Le gain de la spécialisation", x=540, y=110, w=700, lignes=[
            dict(f="Sans échange : 2 draps et 2 vins", taille=32),
            dict(f="Angleterre : 220 ÷ 100 = 2,2 draps · Portugal : 170 ÷ 80 = 2,125 vins", taille=28),
            dict(f="+0,2 drap et +0,125 vin, avec le même travail", cadre=True, taille=32),
            dict(f="Vérification : 1 ÷ 1,2 ≈ 0,83 vin, le coût d'opportunité du drap en Angleterre.", txt=True, pt=True)]),
    }),

    # ================================================================ XII. partie 1
    dict(id="partie1", chap="Partie 1 · mobiliser ses connaissances", fond="canard", humeur="tension", beats=[
        "{ex_p1}Partie un de l'épreuve composée : la mobilisation des connaissances. Une question, sans document. Le sujet : "
        "« Présentez deux effets du commerce international sur les inégalités. » Trois virgule cinq points.",
        "{ex_p1.1}La méthode. « Deux effets » : deux paragraphes, nettement séparés. "
        "{ex_p1.2}Et l'astuce, ici : distinguer les échelles. Les inégalités entre pays, qui baissent. Et les inégalités au sein des pays, qui augmentent. "
        "{ex_p1.3}Chaque paragraphe en A, E, I.",
        "{-ex_p1}{pa_p1}À toi. Mets sur pause, et rédige : une phrase d'introduction, deux mécanismes, deux exemples.",
        "{pa_p1.stop}{-pa_p1}{ex_p1c}{ex_p1c.q1}{s_p11}Correction. {s_p11.1}En introduction, une phrase suffit. Le commerce international, l'échange de biens et de services entre pays, "
        "{s_p11.2}a des effets opposés sur les inégalités, selon l'échelle retenue.",
        "{-s_p11}{ex_p1c.q2}{s_p12}Premier paragraphe. {s_p12.1}A : le commerce réduit les inégalités entre pays. "
        "{s_p12.2}E : en s'ouvrant et en s'intégrant aux chaînes de valeur mondiales, des pays émergents exploitent leurs avantages comparatifs, "
        "attirent des investissements étrangers et accélèrent leur croissance. Ils rattrapent une partie de leur retard.",
        "{s_p12.3}I : la Chine, entrée à l'OMC en deux mille un, est devenue le premier exportateur mondial de marchandises : trois mille cinq cent quatre-vingts milliards "
        "de dollars en deux mille vingt-quatre, selon l'OMC. Et Milanovic montre que de mille neuf cent quatre-vingt-huit à deux mille huit, les classes moyennes des pays émergents "
        "ont eu parmi les plus forts gains de revenu au monde.",
        "{-s_p12}{ex_p1c.q3}{s_p13}Deuxième paragraphe. {s_p13.1}A : il peut accroître les inégalités au sein des pays riches. "
        "{s_p13.2}E : selon Stolper-Samuelson, l'ouverture nuit au facteur relativement rare, ici le travail peu qualifié. Les importations et les délocalisations "
        "réduisent la demande de ce travail, donc son emploi et son salaire relatif. Tandis que les qualifiés des secteurs exportateurs gagnent.",
        "{s_p13.3}I : Autor, Dorn et Hanson montrent que les zones américaines les plus exposées aux importations chinoises ont perdu durablement des emplois industriels.",
        "{-s_p13}{-ex_p1c}",
    ], vis={
        "ex_p1": dict(type="exo", niveau="p1", titre="Présentez deux effets du commerce international sur les inégalités.",
                      src="Sujet inventé pour le site · 3,5 points · sans document",
                      enonce=["Une vingtaine de lignes, qui répondent exactement à la consigne."],
                      questions=["« Deux effets » : deux paragraphes nettement séparés",
                                 "Distinguer les échelles : entre pays / au sein des pays", "Chaque paragraphe en AEI"]),
        "pa_p1": dict(type="pause", t="Une phrase d'introduction, deux mécanismes, deux exemples."),
        "ex_p1c": dict(type="exo", mode="coin", niveau="p1", titre="Commerce et inégalités",
                       questions=["Introduire", "Paragraphe 1 : entre pays", "Paragraphe 2 : au sein des pays"]),
        "s_p11": dict(type="liste", titre="Introduire", x=540, y=180, w=700, petit=True, items=[
            "Commerce international : l'échange de biens et de services entre pays",
            "Des effets opposés selon l'échelle retenue"]),
        "s_p12": dict(type="liste", titre="Paragraphe 1 · entre pays", x=540, y=120, w=700, petit=True, items=[
            "A · Le commerce réduit les inégalités entre pays",
            "E · Ouverture, chaînes de valeur, avantages comparatifs, IDE → croissance → rattrapage",
            "I · Chine (OMC 2001) : 3 580 milliards $ en 2024 ; Milanovic, 1988-2008"], marques=["A", "E", "I"]),
        "s_p13": dict(type="liste", titre="Paragraphe 2 · au sein des pays", x=540, y=120, w=700, petit=True, items=[
            "A · Il peut accroître les inégalités au sein des pays riches",
            "E · Stolper-Samuelson : le facteur rare (peu qualifié) perd ; les qualifiés exportateurs gagnent",
            "I · Choc chinois : Autor, Dorn et Hanson"], marques=["A", "E", "I"]),
    }),

    # ================================================================ XIII. partie 2
    # 6,50 / 178,96 = 3,63 % ; 172,46 / 178,96 = 96,37 % ; 1 % de 178,96 ≈ 1,79
    dict(id="partie2", chap="Partie 2 · étudier un document", fond="nuit", humeur="tension", beats=[
        "{ex_p2}Partie deux : l'étude d'un document. Cinq virgule cinq points. Le document : qui produit la valeur d'un iPhone trois G, en deux mille neuf ? Deux questions. "
        "{ex_p2.1}Un : calcule la part de l'assemblage chinois dans le coût de fabrication. "
        "{ex_p2.2}Deux : à l'aide du document et de tes connaissances, montre que la production de l'iPhone illustre l'internationalisation de la chaîne de valeur.",
        "{-ex_p2}{gr_doc}Avant tout chiffre : le titre, la source, l'unité. {gr_doc.1}Les composants achetés aux fournisseurs : cent soixante-douze dollars quarante-six. "
        "{gr_doc.2}L'assemblage en Chine : six dollars cinquante. Pour un total de cent soixante-dix-huit dollars quatre-vingt-seize. "
        "La source : Xing et Detert, en deux mille dix, d'après les estimations du cabinet iSuppli.",
        "{-gr_doc}{pa_p2}À toi. Mets sur pause : un calcul pour la question un, un raisonnement relié au document pour la question deux.",
        "{pa_p2.stop}{-pa_p2}{ex_p2c}{ex_p2c.q1}{s_p21}Correction. {s_p21.1}Un : une part, c'est la partie divisée par le tout, fois cent. "
        "{s_p21.2}Six virgule cinquante, divisé par cent soixante-dix-huit virgule quatre-vingt-seize. À la main : un pour cent du total, c'est environ un dollar quatre-vingts. "
        "Six dollars cinquante, c'est un peu plus de trois fois et demie un dollar quatre-vingts. Donc environ trois virgule six pour cent.",
        "{s_p21.3}La phrase : « Selon Xing et Detert, d'après iSuppli, l'assemblage en Chine représente environ trois virgule six pour cent du coût de fabrication "
        "d'un iPhone trois G en deux mille neuf ; les composants, quatre-vingt-seize virgule quatre pour cent. »",
        "{-s_p21}{ex_p2c.q2}{s_p22}Deux : un raisonnement, relié au document. {s_p22.1}On définit : l'internationalisation de la chaîne de valeur, "
        "c'est la répartition des étapes de production entre plusieurs pays.",
        "{s_p22.2}Pour l'iPhone, la conception est américaine. Les composants, cent soixante-douze dollars quarante-six sur cent soixante-dix-huit dollars quatre-vingt-seize, "
        "viennent de fournisseurs de plusieurs pays, notamment le Japon, l'Allemagne, la Corée du Sud, les États-Unis. "
        "Et l'assemblage, intensif en main-d'œuvre, se fait en Chine, où ce travail est abondant et relativement bon marché.",
        "{s_p22.3}Chaque étape est placée là où elle est la plus rentable : c'est la logique des avantages comparatifs, appliquée non plus à des produits, mais à des tâches. "
        "{s_p22.4}Enfin, le commerce mesuré en valeur brute attribue tout l'appareil à la Chine, alors que sa valeur ajoutée y est faible. "
        "D'où l'intérêt du commerce en valeur ajoutée.",
        "{-s_p22}{-ex_p2c}",
    ], vis={
        "ex_p2": dict(type="exo", niveau="p2", titre="La chaîne de valeur de l'iPhone", src="Exercice du site, données Xing et Detert (2010) · 5,5 points",
                      enonce=["Document : « Qui produit la valeur d'un iPhone 3G ? (2009) » : coût total 178,96 $ ; composants 172,46 $ ; assemblage en Chine 6,50 $."],
                      questions=["Calculez la part de l'assemblage chinois dans le coût de fabrication.",
                                 "À l'aide du document et de vos connaissances, montrez que la production de l'iPhone illustre l'internationalisation de la chaîne de valeur."]),
        "gr_doc": dict(type="donnees", g=dict(G["e2-iphone"], cats=["Composants (fournisseurs étrangers)", "Assemblage en Chine"]), dec=2, signe=False, lab=340, kicker="Document · partie 2", x=110, y=100, w=1060, h=500),
        "pa_p2": dict(type="pause", t="Question 1 : un calcul. Question 2 : un raisonnement relié au document."),
        "ex_p2c": dict(type="exo", mode="coin", niveau="p2", titre="L'iPhone 3G",
                       donnees=["Total : 178,96 $", "Composants : 172,46 $", "Assemblage en Chine : 6,50 $"],
                       questions=["Part de l'assemblage chinois ?", "L'internationalisation de la chaîne de valeur"]),
        "s_p21": dict(type="formule", titre="1 · La part de l'assemblage", x=540, y=140, w=700, lignes=[
            dict(f="part = [[partie|tout]] × 100", taille=36),
            dict(f="[[6,50|178,96]] × 100 ≈ 3,6 %", cadre=True, taille=36),
            dict(f="Les composants : environ 96,4 % du coût de fabrication.", txt=True)]),
        "s_p22": dict(type="liste", titre="2 · Le raisonnement", x=540, y=110, w=700, petit=True, items=[
            "Définir : répartir les étapes de production entre plusieurs pays",
            "Conception américaine ; composants (172,46 $) du Japon, d'Allemagne, de Corée du Sud, des États-Unis ; assemblage en Chine",
            "Chaque étape là où elle est la plus rentable : les avantages comparatifs appliqués aux tâches",
            "La valeur brute attribue tout à la Chine : d'où le commerce en valeur ajoutée"]),
    }),

    # ================================================================ XIV. partie 3 (bac 2026)
    dict(id="partie3", chap="Partie 3 · raisonner sur un dossier", fond="moutarde", humeur="tension", beats=[
        "{ex_p3}Partie trois : le raisonnement sur un dossier documentaire, neuf points à partir de deux mille vingt-sept. Et cette fois, un vrai sujet : celui du bac deux mille vingt-six, jour un. "
        "« Montrez que la productivité des firmes sous-tend la compétitivité d'un pays, c'est-à-dire son aptitude à exporter. »",
        "Les documents du sujet officiel ne sont pas reproduits ici. Entraîne-toi avec les exemples du chapitre : le solde commercial de deux mille vingt-cinq, "
        "l'aéronautique, l'iPhone. Et chaque paragraphe doit s'appuyer sur au moins un document, cité précisément.",
        "{-ex_p3}{pa_p3}À toi. Mets sur pause et construis le plan : trois idées, chacune avec son mécanisme et un exemple.",
        "{pa_p3.stop}{-pa_p3}{li_p3}Correction. {li_p3.1}L'introduction. La productivité mesure l'efficacité de la production : la production par unité de facteur. "
        "La compétitivité d'un pays, c'est son aptitude à exporter, à gagner des parts de marché face à la concurrence étrangère. Puis on annonce les trois idées.",
        "{li_p3.2}Un : la productivité améliore la compétitivité-prix. Plus de productivité, c'est un coût salarial unitaire plus bas. "
        "Les firmes peuvent baisser leurs prix à l'exportation sans réduire leurs marges, et gagner des parts de marché. "
        "Un salaire élevé n'est pas un handicap, si la productivité l'est aussi.",
        "{li_p3.3}Deux : la productivité finance la compétitivité hors-prix. Des coûts plus bas dégagent des marges. Elles financent la recherche, la qualité, la marque, le service. "
        "Les produits sont différenciés, et moins sensibles au prix. Exemple : l'aéronautique et la pharmacie portent l'amélioration du solde des biens de la France en deux mille vingt-cinq.",
        "{li_p3.4}Trois : les exportations reposent sur les firmes les plus productives. C'est Melitz : exporter a des coûts fixes, donc seules les plus productives exportent. "
        "L'ouverture les fait grandir, et élève la productivité moyenne.",
        "{li_p3.5}En conclusion : la productivité des firmes est le socle de la compétitivité du pays, par les prix comme hors prix. "
        "Et elle dépend elle-même de l'innovation et du capital humain : c'est le lien avec le chapitre sur la croissance.",
        "{-li_p3}{note_p3}Et toujours la règle d'or : pas de partie « limites ». Un « montrez que » ne se {!discute}discute pas : il se démontre.",
        "{-note_p3}",
    ], vis={
        "ex_p3": dict(type="exo", niveau="p3", titre="Montrez que la productivité des firmes sous-tend la compétitivité d'un pays, c'est-à-dire son aptitude à exporter.",
                      src="Sujet officiel : bac 2026, jour 1 · 9 points au barème 2027", y=80,
                      enonce=["Documents du sujet officiel non reproduits : entraîne-toi avec les exemples du chapitre (solde commercial 2025, aéronautique, iPhone)."],
                      questions=["Une introduction qui définit et annonce", "Trois idées : mécanisme + document",
                                 "Une conclusion"]),
        "pa_p3": dict(type="pause", t="Trois idées, chacune avec un mécanisme et un exemple."),
        "li_p3": dict(type="liste", titre="Le plan corrigé", x=110, y=90, w=1060, items=[
            "Introduction : définir productivité et compétitivité, annoncer les idées",
            "I. La productivité améliore la compétitivité-prix : coût salarial unitaire ↓, prix à l'export ↓",
            "II. Elle finance la compétitivité hors-prix : marges → R&D, qualité, marque · aéronautique, pharmacie 2025",
            "III. Les exportations reposent sur les firmes les plus productives (Melitz)",
            "Conclusion : le socle de la compétitivité, lié à l'innovation et au capital humain"],
            marques=["→", "I", "II", "III", "✓"]),
        "note_p3": dict(type="note", titre="Règle d'or de la partie 3", cles=["démontre"],
                        t="Pas de partie « limites » : un « montrez que » ne se discute pas, il se démontre.", x=170, y=220, w=940),
    }),

    # ================================================================ XV. dissertation
    dict(id="dissertation", chap="La dissertation", fond="corail", humeur="tension", beats=[
        "{ex_d}Et la dissertation. Le sujet : « Le protectionnisme peut-il être une réponse efficace aux effets du commerce international ? »",
        "{ex_d.1}Analyse les mots. Le protectionnisme, et ses instruments. Les effets du commerce : les gains, et les perdants. "
        "{ex_d.2}« Peut-il » appelle une réponse nuancée. {ex_d.3}Et mobilise tes connaissances, sans commenter le dossier document par document.",
        "{-ex_d}{pa_d}À toi. Mets sur pause : écris la problématique, puis le plan détaillé, en trois parties.",
        "{pa_d.stop}{-pa_d}{def_pb}Correction. La problématique. Le commerce international procure des gains moyens, mais il fait des perdants. "
        "Taxer les importations permet-il de corriger ces effets… sans détruire les gains de l'échange ?",
        "{-def_pb}{cm_d}Le plan. {cm_d.1}Un : le protectionnisme peut répondre à certains effets du commerce. Protéger les secteurs et les territoires exposés : "
        "le choc chinois, Stolper-Samuelson. Laisser le temps à des industries naissantes ou stratégiques de devenir compétitives : List, la Corée du Sud. "
        "Et réduire la dépendance à des chaînes de valeur trop longues : les pénuries de deux mille vingt et deux mille vingt et un.",
        "{cm_d.2}Deux : mais il est souvent inefficace, voire contre-productif. Il renchérit les biens importés : moins de pouvoir d'achat, "
        "et des coûts plus élevés pour les entreprises qui utilisent des composants importés. Il provoque des représailles : les années trente, Smoot-Hawley, "
        "et les tensions commerciales de deux mille vingt-cinq. Et il protège des firmes peu productives, ce qui freine l'innovation : Melitz.",
        "{cm_d.3}Trois : d'autres réponses peuvent être plus efficaces. Accompagner les perdants : la formation, la reconversion, les aides aux territoires. "
        "Redistribuer une partie des gains de l'échange, par la fiscalité et la protection sociale. Et réguler l'échange plutôt que le fermer : "
        "des normes sociales et environnementales, l'ajustement carbone aux frontières, une protection ciblée et temporaire.",
        ("P", 1.0),
        "Pourquoi ce plan ? Parce que « peut-il » appelle d'abord un oui, puis ses limites, puis une réponse construite.",
        "{-cm_d}",
    ], vis={
        "ex_d": dict(type="exo", niveau="dissert", titre="Le protectionnisme peut-il être une réponse efficace aux effets du commerce international ?",
                     src="Sujet inventé pour le site",
                     enonce=["Construis la problématique et le plan détaillé."],
                     questions=["Analyser les mots : protectionnisme, effets du commerce", "« Peut-il » appelle une réponse nuancée",
                                "Mobiliser ses connaissances, sans commenter le dossier document par document"]),
        "pa_d": dict(type="pause", t="La problématique, puis le plan détaillé : trois parties, trois sous-parties chacune."),
        "def_pb": dict(type="def", terme="Problématique", cles=["gains", "perdants", "corriger"],
                       t="Le commerce procure des gains moyens mais fait des perdants. Taxer les importations permet-il de corriger ces effets sans détruire les gains de l'échange ?",
                       x=150, y=170, w=980),
        "cm_d": dict(type="plan", titre="Le protectionnisme, une réponse efficace aux effets du commerce ?", x=70, y=120, w=1140, parties=[
            dict(t="I. Il peut répondre à certains effets", items=["A. Protéger secteurs et territoires (choc chinois)",
                                                                  "B. Industries naissantes ou stratégiques (List, Corée du Sud)",
                                                                  "C. Moins dépendre de chaînes trop longues (2020-2021)"]),
            dict(t="II. Souvent inefficace, voire contre-productif", items=["A. Biens importés plus chers : pouvoir d'achat, coûts",
                                                                            "B. Représailles : Smoot-Hawley, tensions de 2025",
                                                                            "C. Protège des firmes peu productives (Melitz)"]),
            dict(t="III. D'autres réponses plus efficaces", items=["A. Accompagner les perdants : formation, reconversion",
                                                                  "B. Redistribuer les gains de l'échange",
                                                                  "C. Réguler : normes, ajustement carbone, protection ciblée"])]),
    }),

    # ================================================================ XVI. récap
    dict(id="recap", chap="Pour le bac", fond="canard", humeur="lumiere", beats=[
        "{cm_r}On récapitule. {cm_r.1}Pourquoi échanger : les avantages comparatifs. La technologie avec Ricardo, les dotations avec HOS, "
        "et des avantages qui se construisent. {cm_r.2}Entre pays comparables : la différenciation, horizontale et verticale, et les économies d'échelle de Krugman.",
        "{cm_r.3}La compétitivité : prix et hors-prix, portée par les firmes les plus productives. Et la chaîne de valeur mondiale : les multinationales, l'iPhone. "
        "{cm_r.4}Enfin, les effets : des prix plus bas, moins d'inégalités entre pays, davantage au sein des pays. Et le débat entre libre-échange et protectionnisme.",
        "{-cm_r}{fr_r}Les auteurs, dans l'ordre. {fr_r.1}Smith, mille sept cent soixante-seize. {fr_r.2}Ricardo, mille huit cent dix-sept. "
        "{fr_r.3}List, mille huit cent quarante et un. {fr_r.4}Ohlin, mille neuf cent trente-trois : le modèle HOS. {fr_r.5}Leontief, mille neuf cent cinquante-trois. "
        "{fr_r.6}Krugman, mille neuf cent soixante-dix-neuf. {fr_r.7}Melitz, deux mille trois. {fr_r.8}Et Autor, Dorn et Hanson, deux mille treize.",
        ("P", 4.0),
        "{-fr_r}{cf_r}{cf_r.1}Et trois chiffres à citer. Vingt-quatre mille quatre cent trente milliards de dollars d'exportations mondiales de marchandises, en deux mille vingt-quatre. "
        "{cf_r.2}Trois virgule six pour cent : la part de l'assemblage chinois dans le coût d'un iPhone trois G. "
        "{cf_r.3}Et moins soixante-neuf virgule deux milliards d'euros : le solde des échanges de biens de la France en deux mille vingt-cinq.",
        ("P", 1.5),
        "{-cf_r}{fin}Les fiches à imprimer, le quiz, les cartes de révision et les animations de ce chapitre sont sur le site Faits et Courbes. "
        "Le lien est dans la description. Prochain dossier : le chômage.",
        ("P", 2.5),
        "{-fin}",
    ], vis={
        "cm_r": dict(type="plan", titre="Le commerce international : pourquoi, comment, pour qui ?", x=60, y=140, w=1160, parties=[
            dict(t="Pourquoi échanger", items=["Avantage comparatif : Ricardo (technologie)", "Dotations : HOS ; Leontief ; avantages construits"]),
            dict(t="Pays comparables", items=["Différenciation horizontale et verticale", "Économies d'échelle (Krugman)"]),
            dict(t="Firmes et chaînes", items=["Compétitivité prix / hors-prix ; Melitz", "FMN, IDE ; iPhone : 3,6 % chinois"]),
            dict(t="Effets et débat", items=["Prix ↓ ; inégalités entre pays ↓, au sein ↑", "Libre-échange ou protectionnisme (List)"])]),
        "fr_r": dict(type="frise", de=1750, a=2030, items=[
            dict(d=1776, nom="Smith", q="avantage absolu"), dict(d=1817, nom="Ricardo", q="avantage comparatif"),
            dict(d=1841, nom="List", q="protectionnisme éducateur"), dict(d=1933, nom="Ohlin", q="le modèle HOS"),
            dict(d=1953, nom="Leontief", q="le paradoxe"), dict(d=1979, nom="Krugman", q="commerce intra-branche"),
            dict(d=2003, nom="Melitz", q="firmes hétérogènes"), dict(d=2013, nom="Autor et al.", q="le choc chinois")]),
        "cf_r": dict(type="chiffres", titre="Trois chiffres à citer", x=90, y=150, w=1100,
                     items=[dict(n=c["n"], l=c["l"], s=c["s"]) for c in CHIF]),
        "fin": dict(type="titre", sur="Faits & Courbes · SES Terminale", t="Fiches, quiz et animations",
                    sous="Le lien est dans la description · prochain dossier : le chômage"),
    }),
]

QUIZ = [
    dict(q="Dans l'exemple de Ricardo, le Portugal produit drap et vin avec moins de travail que l'Angleterre. Il a donc…",
         r=["un avantage comparatif dans les deux biens", "un avantage absolu dans les deux biens, mais un avantage comparatif seulement dans le vin",
            "intérêt à ne pas échanger"], ok=1,
         ex="Le coût d'opportunité du vin est plus faible au Portugal (80/90 ≈ 0,89 drap contre 1,2 en Angleterre) : il se spécialise dans le vin.", voir="an_ric"),
    dict(q="L'avantage comparatif repose sur…",
         r=["le niveau absolu des salaires", "le coût d'opportunité relatif d'un bien", "la taille du pays"], ok=1,
         ex="On compare ce que coûte un bien en termes de l'autre bien sacrifié, d'un pays à l'autre.", voir="def_co"),
    dict(q="Selon le modèle HOS, un pays abondant en travail peu qualifié exporte…",
         r=["des biens intensifs en travail peu qualifié", "des biens intensifs en capital", "uniquement des matières premières"], ok=0,
         ex="Le facteur abondant est relativement bon marché : les biens qui l'utilisent beaucoup y sont moins chers.", voir="ch_hos"),
    dict(q="Krugman explique le commerce entre pays comparables par…",
         r=["les différences de dotations factorielles", "les économies d'échelle et le goût pour la variété", "le protectionnisme"], ok=1,
         ex="Nouvelle théorie du commerce international (1979-1980), Nobel 2008.", voir="ch_krug"),
    dict(q="La différenciation verticale des produits porte sur…",
         r=["la couleur et le style", "le pays d'origine", "la qualité et la gamme"], ok=2,
         ex="Verticale : niveaux de qualité différents ; horizontale : variétés de même qualité.", voir="ca_raisons"),
    dict(q="Selon Melitz, pourquoi seules certaines firmes exportent-elles ?",
         r=["Exporter a un coût fixe que seules les plus productives peuvent couvrir", "Les petites firmes n'ont pas le droit d'exporter",
            "Les firmes exportatrices sont subventionnées"], ok=0,
         ex="D'où le lien entre productivité des firmes et compétitivité du pays.", voir="ch_mel"),
    dict(q="Un investissement direct à l'étranger correspond à…",
         r=["un achat d'actions étrangères pour quelques jours", "une prise de contrôle durable d'une entreprise à l'étranger (au moins 10 % du capital)",
            "un prêt à un État étranger"], ok=1,
         ex="L'IDE crée ou rachète une filiale : c'est l'outil de la firme multinationale.", voir="def_fmn"),
    dict(q="Pour un iPhone 3G de 2009, l'assemblage en Chine représentait environ…",
         r=["3,6 % du coût de fabrication", "50 % du coût de fabrication", "90 % du coût de fabrication"], ok=0,
         ex="6,50 $ sur 178,96 $ (Xing et Detert, 2010) : la valeur ajoutée chinoise était très faible.", voir="an_iph"),
    dict(q="Selon le théorème de Stolper-Samuelson, dans un pays riche, l'ouverture…",
         r=["profite à tous les travailleurs de la même façon", "nuit au facteur rare, le travail peu qualifié", "nuit au capital"], ok=1,
         ex="Le facteur abondant gagne, le facteur rare perd : d'où une hausse des inégalités internes.", voir="def_ss"),
    dict(q="Le protectionnisme éducateur de List (1841) consiste à…",
         r=["fermer définitivement les frontières", "supprimer tous les droits de douane", "protéger temporairement les industries naissantes"], ok=2,
         ex="Une protection provisoire, le temps que l'industrie devienne compétitive.", voir="cmp_arg"),
]

CREDITS = [
    "Données : OMC, Perspectives et statistiques du commerce mondial (avril 2025) ; Douane, résultats du commerce extérieur pour l'année 2025 "
    "(9 février 2026) ; Y. Xing et N. Detert, ADBI Working Paper n° 257 (2010), d'après iSuppli ; OCDE (chaînes de valeur mondiales).",
    "Graphiques, chaînes causales, animations et sujets : site Faits & Courbes (SES Terminale) ; les sujets sont inventés pour le site, "
    "sauf la partie 3 (bac 2026, jour 1), corrigée par le site. Courbe de l'éléphant : schéma de principe d'après Lakner et Milanovic.",
    "Polices : IBM Plex Sans Condensed, Archivo, Spectral, JetBrains Mono (SIL Open Font License).",
]
