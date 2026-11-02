"""Le bonheur, épisode 5 : « Bonheur, morale et politique »

Même format que les séries « La liberté » et « Le devoir » (voir liberte_1.py, devoir_3.py).
Citations vérifiées sur Wikisource : Kant, Critique de la raison pratique (1788), I, II, chap. 2, V, trad. Barni ;
Kant, « Sur le proverbe : cela peut être juste en théorie… » (1793), II, trad. Barni ; Tocqueville, De la démocratie
en Amérique, II (1840), IV, 6. Saint-Just, rapport à la Convention du 13 ventôse an II (3 mars 1794).
Déclaration d'indépendance des États-Unis (1776), trad. courante. Dostoïevski et Huxley (œuvre protégée) : résumés par le narrateur.
"""

CODE = "bonheur-5"
NOTION = "Le bonheur"
NUM = 5
TITRE = "Bonheur, morale et politique"
SUIVANT = "Épisode 6 · Le bonheur à l'épreuve du bac"
PRONONCIATION = {"Huxley": "Euksslé", "Bentham": "Bentame", "Karamazov": "Karamazof",
                 "Tocqueville": "Tokvil", "Jefferson": "Djèfeursonne", "Bhoutan": "Boutan", "Nozick": "Nozik"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_ford}{q1}Imagine un monde où personne n'est malheureux. Pas de guerre, pas de pauvreté, pas de vieillesse. "
        "Chacun aime son travail : on l'a conditionné, dès avant sa naissance, à l'aimer.",
        "{-q1}{-tab_ford}{tab_pil}{soma}Et si un léger chagrin vous effleure ? {soma.1}Il suffit d'avaler un comprimé de soma : "
        "une drogue parfaite, sans effets secondaires, qui rend tout de suite heureux.",
        "{-soma}{hux}Ce monde, l'écrivain anglais Aldous Huxley l'a imaginé en 1932, dans un roman : Le Meilleur des mondes. "
        "Tout le monde y est heureux. Et pourtant, c'est l'un des livres les plus inquiétants du vingtième siècle.",
        ("Pourquoi ?", {"rate": "-6%"}),
        "{-hux}{q2}Parce qu'il pose une question vertigineuse : un État qui nous rendrait heureux… serait-il un bon État ?",
        "{-q2}{q3}Le bonheur est-il l'affaire de la morale ? Celle de la politique ? Ou seulement la mienne ?",
        ("P", 0.3),
        "{-q3}{-tab_pil}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_ford": dict(type="tableau", img="bh5-ford", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                         legende="Chaîne de montage Ford, Highland Park, 1913 (domaine public)"),
        "q1": dict(type="question", t="Un monde où personne n'est malheureux ?"),
        "tab_pil": dict(type="tableau", img="bh5-pilules", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .55],
                        legende="Gélules (photo Tom Varco, CC BY-SA 3.0)"),
        "soma": dict(type="def", cles=["soma"], terme="Le soma",
                     t="Une drogue parfaite, sans effets secondaires, qui rend tout de suite heureux.",
                     etape="Aldous Huxley, Le Meilleur des mondes (1932).", x=170, y=200, w=940),
        "hux": dict(type="mot", t="1932", g="Aldous Huxley, Le Meilleur des mondes", y=260, taille=110),
        "q2": dict(type="question", t="Un État qui nous rendrait heureux serait-il un bon État ?"),
        "q3": dict(type="question", t="Le bonheur : l'affaire de la morale, de la politique… ou la mienne ?"),
        "titre": dict(type="titre", sur="Le bonheur · Épisode 5", t="Bonheur, morale et politique",
                      sous="Kant, les utilitaristes, l'État"),
    }),

    # ------------------------------------------------------------------ I. Kant
    dict(id="kant", chap="Mériter d'être heureux", fond="aube", humeur="lumiere", notions=["le devoir", "la raison", "la religion"],
         retenir="Kant : le bonheur ne peut fonder la morale. La morale apprend à se rendre digne du bonheur ; l'espérance d'un accord entre vertu et bonheur relève de la religion.",
         beats=[
        "{kant}{tab_kon}Commençons par la morale. On l'a vu dans l'épisode un : pour Kant, le bonheur est un idéal de l'imagination. "
        "Chacun le rêve à sa façon ; personne ne sait dire exactement en quoi il consiste.",
        "{-kant}{-tab_kon}{tab_phi}{trois}D'où une thèse forte, rencontrée dans la série sur le devoir : le bonheur ne peut pas fonder la morale. "
        "Allons plus loin, et voyons pourquoi. {trois.1}D'abord, il est indéterminé : une morale du bonheur ne donnerait que des conseils, "
        "valables pour l'un, pas pour l'autre.",
        "{trois.2}Ensuite, il ne commande que sous condition : si tu veux être heureux, fais ceci. C'est un impératif hypothétique, "
        "pas un devoir. {trois.3}Enfin, il corrompt le motif : celui qui est honnête parce que cela le rend heureux agit par intérêt, "
        "comme le marchand de la série sur le devoir.",
        "{-trois}{-tab_phi}{tab_dore}Kant ne méprise pas le bonheur pour autant. Il le remet à sa place, dans la Critique de la raison pratique, en 1788.",
        ("C", "C'est pourquoi aussi la morale n'est pas proprement une doctrine qui nous apprenne à nous rendre heureux, "
              "mais seulement comment nous devons nous rendre dignes du bonheur.", "c_dig"),
        "{-c_dig}{dig}{dig.g}Être heureux : cela ne dépend pas entièrement de moi. {dig.d}Être digne de l'être : cela, je le peux toujours. "
        "Le devoir ne me promet rien. Il me rend digne.",
        "Pense à deux élèves. L'un triche, obtient une excellente note et s'en réjouit. L'autre travaille honnêtement "
        "et échoue de peu. Le premier est peut-être plus heureux, ce soir. Mais lequel des deux mérite de l'être ?",
        "{-dig}{sb}Pour aller plus loin, Kant pose pourtant une question troublante. {sb.1}Le bien complet, ce qu'il appelle le souverain bien, "
        "ce serait la vertu, accompagnée d'un bonheur à sa mesure. {sb.2}Or, sur cette terre, rien ne le garantit : le juste souffre, "
        "le méchant prospère.",
        "{sb.3}Alors la raison a le droit d'espérer : une vie après la mort, et un Dieu qui accordera un jour le bonheur à la vertu. "
        "C'est là que la morale conduit à la {#la religion}religion : non pour fonder le devoir, mais pour fonder l'espérance.",
        "{-sb}{-tab_dore}",
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Critique de la raison pratique (1788)", x=110, y=120, w=330, h=420),
        "tab_kon": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Königsberg, ville de Kant, photochrome, vers 1900 (domaine public)"),
        "tab_phi": dict(type="tableau", img="bh5-philosophe", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .45, .35],
                        legende="Jean Siméon Chardin, Le Philosophe lisant, 1734 (musée du Louvre)"),
        "trois": dict(type="liste", titre="Pourquoi le bonheur ne peut fonder la morale", items=[
            "Il est indéterminé : des conseils, pas des lois",
            "Il commande sous condition : un impératif hypothétique",
            "Il corrompt le motif : l'honnêteté par intérêt"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_dore": dict(type="tableau", img="bh5-paradis", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                         legende="Gustave Doré, La Rose céleste, illustration du Paradis de Dante, chant XXXI, 1868"),
        "c_dig": dict(type="cit", a="Kant", o="Critique de la raison pratique, I, livre II, chap. 2, V (1788), trad. Barni",
                      x=170, y=170, w=940),
        "dig": dict(type="cols", g="Être heureux", gq="ne dépend pas entièrement de moi", d="Être digne de l'être",
                    dq="je le peux toujours : c'est le devoir", vs="≠", repere="Repère · le bonheur et la dignité"),
        "sb": dict(type="liste", titre="Pour aller plus loin · le souverain bien", items=[
            "La vertu, accompagnée d'un bonheur à sa mesure",
            "Sur terre, rien ne le garantit : le juste souffre",
            "La raison espère : Dieu, l'immortalité de l'âme"], marques=["1", "2", "3"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ II. l'utilitarisme
    dict(id="utilite", chap="Le plus grand bonheur du plus grand nombre", fond="nuit", humeur="tension",
         notions=["la justice", "l'État"],
         retenir="Bentham : une loi est bonne si elle augmente le bonheur de tous, chacun comptant pour un. Objection : le bonheur collectif ne justifie pas de sacrifier un innocent.",
         beats=[
        "{bent}{tab_der}L'utilitarisme répond tout autrement : on l'a vu dans la série sur le devoir. Pour Bentham, une action est bonne "
        "si elle produit le plus grand bonheur du plus grand nombre. Le bonheur n'est plus l'ennemi de la morale : il en devient le critère.",
        "{-bent}{pol}Allons plus loin. Car Bentham n'est pas d'abord un moraliste : c'est un juriste, un réformateur. "
        "Ce qu'il cherche, c'est une boussole pour le législateur. {pol.1}Une loi est bonne si elle augmente la somme de bonheur "
        "dans la société.",
        "{pol.2}Et chacun compte pour un, personne pour plus d'un : le bonheur du mendiant pèse autant que celui du lord. "
        "{pol.3}C'est une idée profondément démocratique. Bentham et ses disciples défendront la réforme des prisons, "
        "l'abolition de l'esclavage, l'élargissement du droit de vote.",
        "{-pol}{-tab_der}{tab_tro}{dost}Mais une somme peut cacher un sacrifice. Dostoïevski l'a mis en scène en 1880, "
        "dans Les Frères Karamazov. Ivan pose à son jeune frère, Aliocha, une question terrible.",
        "{ivan}{ivan.1}Imagine que tu bâtis l'édifice du bonheur humain, pour donner enfin aux hommes la paix et le repos. "
        "Mais pour cela, il faudrait torturer un seul petit enfant, et fonder tout l'édifice sur ses larmes. "
        "{ivan.2}Accepterais-tu d'en être l'architecte ?",
        ("Aliocha répond doucement : non, je n'accepterais pas.", {"rate": "-6%"}),
        "{-dost}{-ivan}{lim}Voilà l'objection centrale. {lim.1}Le bonheur collectif n'est pas une simple addition. "
        "{lim.2}Il ne justifie pas de sacrifier un innocent. Il y a des choses qu'on ne fait pas à une personne, "
        "quel que soit le bonheur des autres : la {#la justice}justice passe avant le calcul.",
        "{-lim}{-tab_tro}",
    ], vis={
        "bent": dict(type="portrait", annee=1748, legende="Introduction aux principes de morale et de législation (1789)",
                     img="bentham", nom="Jeremy Bentham", dates="1748 – 1832", x=110, y=120, w=330, h=420),
        "tab_der": dict(type="tableau", img="bh5-derby", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.2, .65, .5],
                        legende="William Powell Frith, Le Jour du Derby, 1856-1858 (Tate, Londres)"),
        "pol": dict(type="liste", titre="Une boussole pour le législateur", items=[
            "Une loi est bonne si elle augmente la somme de bonheur",
            "Chacun compte pour un, personne pour plus d'un",
            "Réforme des prisons, abolition de l'esclavage, droit de vote"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_tro": dict(type="tableau", img="bh5-troika", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .55],
                        legende="Vassili Perov, Troïka, 1866 (galerie Tretiakov, Moscou)"),
        "dost": dict(type="portrait", annee=1821, img="dostoievski", nom="Fiodor Dostoïevski", dates="1821 – 1881",
                     legende="Les Frères Karamazov (1880)", x=110, y=120, w=330, h=420),
        "ivan": dict(type="dialogue", lignes=["« Le bonheur de tous… sur les larmes d'un seul enfant. »",
                                              "« En serais-tu l'architecte ? »"],
                     src="d'après Dostoïevski, Les Frères Karamazov, livre V, chap. 4 (1880)", x=640, y=110, w=570),
        "lim": dict(type="liste", titre="L'objection", items=[
            "Le bonheur collectif n'est pas une simple addition",
            "Il ne justifie pas de sacrifier un innocent"], marques=["1", "2"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ III. une idée neuve
    dict(id="neuve", chap="Une idée neuve", fond="aube", humeur="lumiere", notions=["l'État", "la liberté", "la justice"],
         retenir="1776 : le droit de rechercher le bonheur. 1793-1794 : le bonheur commun, but de la société (Saint-Just). Mais un pouvoir chargé du bonheur de tous peut devenir terrible.",
         beats=[
        "{tab_dec}{an}Passons à la politique. Le 4 juillet 1776, treize colonies anglaises d'Amérique déclarent leur indépendance. "
        "Le texte, rédigé pour l'essentiel par Thomas Jefferson, contient une phrase qui va faire le tour du monde.",
        "{-an}{jeff}Tous les hommes, dit-il, sont créés égaux, et dotés de droits inaliénables.",
        ("C", "… parmi ces droits se trouvent la vie, la liberté et la recherche du bonheur.", "c_jef"),
        "{-c_jef}{-jeff}{pur}Pèse bien les mots. {pur.1}Le texte ne promet pas le bonheur. Il garantit le droit de le chercher : "
        "en anglais, the pursuit of happiness. {pur.2}Le gouvernement est là pour protéger ces droits ; le bonheur, "
        "chacun le poursuit à sa manière.",
        "{-pur}{-tab_dec}{tab_conv}{sj}{decl}Quelques années plus tard, en France, la Révolution va plus loin. {decl.1}En 1793, la nouvelle "
        "Déclaration des droits commence ainsi : le but de la société est le bonheur commun. {decl.2}Celle de 1789 parlait déjà, "
        "dans son préambule, du bonheur de tous. {-decl}Et le 3 mars 1794, devant la Convention, "
        "un député de vingt-six ans, Saint-Just, lance une formule célèbre.",
        ("C", "Le bonheur est une idée neuve en Europe.", "c_sj"),
        "{-c_sj}{-sj}{-tab_conv}{tab_d93}{neuve}Neuve, pourquoi ? {neuve.1}Parce que jusque-là, le bonheur était une affaire privée, "
        "ou l'affaire du salut, dans l'autre monde. {neuve.2}Désormais, il devient un but politique : un droit, que l'{#l'État}État "
        "doit rendre possible pour tous, à commencer par les plus pauvres. Saint-Just propose d'ailleurs de distribuer "
        "aux patriotes indigents les biens confisqués aux suspects.",
        "{-neuve}{-tab_d93}{tab_rob}{terr}Mais regarde la date. Mars 1794 : c'est la Terreur. Moins de cinq mois plus tard, Saint-Just est guillotiné, "
        "avec Robespierre. {terr.1}Un pouvoir qui se charge du bonheur de tous… peut-il encore tolérer ceux qui ne le partagent pas ?",
        "{-terr}{-tab_rob}",
    ], vis={
        "tab_dec": dict(type="tableau", img="bh4-declaration", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="John Trumbull, La Déclaration d'indépendance, 1819 (Capitole des États-Unis, Washington)"),
        "an": dict(type="mot", t="4 juillet 1776", g="la Déclaration d'indépendance des États-Unis", y=260, taille=96),
        "jeff": dict(type="portrait", annee=1743, img="jefferson", nom="Thomas Jefferson", dates="1743 – 1826",
                     legende="Déclaration d'indépendance (1776)", x=110, y=120, w=330, h=420),
        "c_jef": dict(type="cit", a="Déclaration d'indépendance des États-Unis", o="4 juillet 1776, trad. courante", x=640, y=200, w=570),
        "pur": dict(type="def", cles=["chercher", "pursuit"], terme="The pursuit of happiness",
                    t="Non pas le bonheur garanti, mais le droit de le chercher.",
                    etape="L'État protège les droits ; chacun poursuit son bonheur à sa manière.", x=170, y=200, w=940),
        "tab_conv": dict(type="tableau", img="bh5-convention", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .4],
                         legende="Charles-Louis Müller, Lanjuinais à la tribune de la Convention, 2 juin 1793, XIXᵉ s."),
        "sj": dict(type="portrait", annee=1767, img="saint-just", nom="Louis Antoine de Saint-Just", dates="1767 – 1794",
                   legende="Rapport à la Convention, 3 mars 1794", x=110, y=120, w=330, h=420),
        "decl": dict(type="liste", titre="Le bonheur dans les Déclarations", items=[
            "1793 : « le but de la société est le bonheur commun »",
            "1789 : le préambule parle déjà du « bonheur de tous »"], marques=["1", "2"], x=640, y=150, w=570),
        "c_sj": dict(type="cit", a="Saint-Just", o="rapport à la Convention, 13 ventôse an II (3 mars 1794)", x=640, y=220, w=570),
        "tab_d93": dict(type="tableau", img="bh5-decl1793", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Déclaration des droits de l'homme et du citoyen de 1793, estampe (domaine public)"),
        "neuve": dict(type="liste", titre="« Une idée neuve »", items=[
            "Avant : une affaire privée, ou celle du salut", "Désormais : un but politique, un droit pour tous"],
                      marques=["1", "2"], x=170, y=180, w=940),
        "tab_rob": dict(type="tableau", img="bh5-robespierre", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="L'Exécution de Robespierre, 28 juillet 1794, gravure (domaine public)"),
        "terr": dict(type="note", titre="Mais regarde la date", cles=["Terreur", "tolérer"],
                     t="Mars 1794 : la Terreur. Saint-Just est guillotiné en juillet, avec Robespierre.",
                     etape="Un pouvoir chargé du bonheur de tous peut-il tolérer ceux qui ne le partagent pas ?", x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ IV. contre l'État paternel
    dict(id="paternel", chap="Le despotisme doux", fond="nuit", humeur="tension", notions=["la liberté", "l'État"],
         retenir="Kant : un gouvernement paternel est le pire despotisme ; nul ne peut me contraindre à être heureux à sa manière. Tocqueville : le pouvoir tutélaire nous fixe dans l'enfance.",
         beats=[
        "{kant2}{tab_bib}Kant a vu le danger dès 1793, dans un court essai sur le rapport entre la théorie et la pratique. "
        "Le pire des gouvernements, dit-il, serait un gouvernement paternel.",
        "Un pouvoir qui traiterait les citoyens comme des enfants mineurs, incapables de savoir ce qui est bon pour eux, "
        "et qui déciderait à leur place de leur bonheur. Ce serait le plus grand despotisme que l'on puisse concevoir.",
        ("C", "… nul ne peut me contraindre à être heureux d'une certaine manière…", "c_nul"),
        "{-kant2}{-c_nul}{pat}Car le bonheur, chacun l'imagine à sa façon. {pat.g}Le gouvernement paternel décide de mon bonheur "
        "à ma place. {pat.d}Le gouvernement patriotique, dit Kant, garantit ma {#la liberté}liberté, pour que je cherche moi-même "
        "mon bonheur, sans nuire à celle des autres.",
        "{-pat}{-tab_bib}{toc}{tab_mill}Un demi-siècle plus tard, Alexis de Tocqueville, rencontré dans la série sur la liberté, "
        "imagine une forme nouvelle de despotisme, propre aux démocraties. Pas un tyran cruel : quelque chose de bien plus doux. "
        "Un pouvoir immense, qui veille sur nous.",
        ("C", "Il travaille volontiers à leur bonheur ; mais il veut en être l'unique agent et le seul arbitre…", "c_toc"),
        "{-toc}{-c_toc}{doux}Ce pouvoir, dit Tocqueville, {doux.1}pourvoit à notre sécurité, facilite nos plaisirs. "
        "{doux.2}Il ressemblerait à l'autorité d'un père, s'il préparait les hommes à l'âge adulte. "
        "{doux.3}Mais il ne cherche qu'à les fixer dans l'enfance. Et Tocqueville finit par une question glaçante.{-doux}",
        ("C", "… que ne peut-il leur ôter entièrement le trouble de penser et la peine de vivre ?", "c_peine"),
        "{-c_peine}{-tab_mill}{tab_trp}{trp}Au bout du chemin, dit-il, chaque nation n'est plus qu'un {!troupeau}troupeau "
        "d'animaux timides et industrieux, dont le gouvernement est le berger. "
        "{trp.1}C'est le despotisme doux : on n'y est pas opprimé, on y est dispensé de penser.",
        "{-trp}{-tab_trp}{mill}{tab_mill2}Même un utilitariste refuse cette pente. John Stuart Mill, on l'a vu dans la série sur la liberté, "
        "ne permet à la société de contraindre un individu que pour empêcher qu'il nuise aux autres. "
        "{mill_n}Et il précise : son propre bien, physique ou moral, n'est pas une raison suffisante.",
        "{mill_n.1}On peut conseiller quelqu'un, le raisonner, le supplier. On ne peut pas le forcer à être heureux.",
        "{-mill}{-mill_n}{-tab_mill2}",
    ], vis={
        "kant2": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                      legende="Sur le proverbe : cela peut être juste en théorie… (1793)", x=110, y=120, w=330, h=420),
        "tab_bib": dict(type="tableau", img="bh5-bible", fond=True, sombre=True, de=[1.25, .5, .5], a=[1.45, .45, .5],
                        legende="Jean-Baptiste Greuze, La Lecture de la Bible, 1755 (musée du Louvre)"),
        "c_nul": dict(type="cit", a="Kant", o="Sur le proverbe : cela peut être juste en théorie… (1793), II, trad. Barni",
                      x=640, y=220, w=570),
        "pat": dict(type="cols", g="Gouvernement paternel", gq="décide de mon bonheur à ma place : le pire despotisme",
                    d="Gouvernement patriotique", dq="garantit ma liberté de chercher mon bonheur", vs="≠"),
        "toc": dict(type="portrait", annee=1805, img="tocqueville", nom="Alexis de Tocqueville", dates="1805 – 1859",
                    legende="De la démocratie en Amérique (1835-1840)", x=110, y=120, w=330, h=420),
        "tab_mill": dict(type="tableau", img="bh5-troupeau", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.2, .6, .5],
                         legende="Anton Mauve, Le Retour du troupeau, Laren, XIXᵉ siècle"),
        "c_toc": dict(type="cit", a="Tocqueville", o="De la démocratie en Amérique, II, IV, 6 (1840)", x=640, y=190, w=570),
        "doux": dict(type="liste", titre="Le pouvoir tutélaire", items=[
            "Il pourvoit à notre sécurité, facilite nos plaisirs",
            "Il ressemblerait à l'autorité d'un père…",
            "… mais il nous fixe dans l'enfance"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "c_peine": dict(type="cit", a="Tocqueville", o="De la démocratie en Amérique, II, IV, 6 (1840)", x=170, y=200, w=940),
        "tab_trp": dict(type="tableau", img="bh5-troupeau", fond=True, sombre=True, de=[1.3, .7, .55], a=[1.05, .5, .5],
                        legende="Anton Mauve, Le Retour du troupeau, Laren, XIXᵉ siècle"),
        "mill": dict(type="portrait", annee=1806, img="mill", nom="John Stuart Mill", dates="1806 – 1873",
                     legende="De la liberté (1859)", x=110, y=120, w=330, h=420),
        "tab_mill2": dict(type="tableau", img="t5-hemicycle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                          legende="L'hémicycle de l'Assemblée nationale, Paris (photo Coucouoeuf, CC BY-SA 3.0)"),
        "mill_n": dict(type="note", titre="Mill, De la liberté (1859)", cles=["nuire", "propre bien"],
                       t="Contraindre un individu ? Seulement pour l'empêcher de nuire aux autres. Son propre bien ne suffit pas.",
                       etape="On peut le conseiller, le raisonner. Pas le forcer à être heureux.", x=640, y=170, w=570),
        "trp": dict(type="def", cles=["opprimé", "penser"], terme="Le despotisme doux · Tocqueville",
                    t="Un troupeau d'animaux timides et industrieux, dont le gouvernement est le berger.",
                    etape="On n'y est pas opprimé : on y est dispensé de penser.", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ V. le meilleur des mondes
    dict(id="meilleur", chap="Le droit d'être malheureux", fond="aube", humeur="mystere",
         notions=["la liberté", "la technique", "la vérité"],
         retenir="Huxley : un bonheur fabriqué et imposé supprime la liberté. L'État ne doit pas faire notre bonheur, mais en garantir les conditions.",
         beats=[
        "{tab_ford2}{hux2}Revenons à Huxley. Son monde, c'est le despotisme doux poussé à la perfection. "
        "{hux2.1}Les enfants y sont fabriqués en série, et conditionnés pour aimer leur condition. "
        "On y compte même les années à partir d'Henry Ford, l'inventeur du travail à la chaîne.",
        "{hux2.2}Les plaisirs sont permanents, la tristesse est chimiquement supprimée. "
        "{hux2.3}Les livres anciens sont interdits : ils pourraient faire réfléchir. Tout le monde est heureux… et personne n'est libre.",
        "{-hux2}{-tab_ford2}{tab_fol}{john}Un seul personnage refuse : un « Sauvage », élevé loin de ce monde, qui a lu Shakespeare. "
        "Face à l'un des maîtres du monde, il réclame tout ce qu'on a supprimé : la poésie, le danger, la liberté… "
        "{john.1}et, pour finir, le droit d'être malheureux.",
        ("Le droit d'être malheureux. Voilà peut-être le prix de la liberté.", {"rate": "-5%"}),
        "Le maître du monde lui répond sans colère : on a choisi. On a sacrifié l'art, la science, la religion… au bonheur. "
        "La vérité trouble, la beauté inquiète : le bonheur exige qu'on y renonce.",
        "{-john}{noz}Souviens-toi de la machine à expérience, dans l'épisode un : nous ne voulons pas seulement nous sentir heureux. "
        "{noz.1}Nous voulons que ce soit vrai, et que ce soit nous. "
        "{noz.2}Un bonheur fabriqué par la {#la technique}technique, et imposé d'en haut, n'est plus le nôtre.",
        "{-noz}{-tab_fol}{tab_dec2}{rep}Alors, l'État doit-il faire le bonheur des citoyens ? Voici la distinction qui dépasse le problème. "
        "{rep.g}Faire le bonheur des gens à leur place : c'est le despotisme, même doux. "
        "{rep.d}Garantir les conditions du bonheur : la sécurité, la justice, l'éducation, la santé, les libertés. "
        "Le reste, c'est à chacun de le chercher.",
        "{-rep}{-tab_dec2}{tab_dz}{bh}Pour aller plus loin : en 2008, la Constitution du Bhoutan demande à l'État de promouvoir "
        "les conditions qui permettent de rechercher le « bonheur national brut ». {bh.1}Les deux mots clés sont encore là : "
        "les conditions, et la recherche.",
        "{-bh}{-tab_dz}",
    ], vis={
        "tab_ford2": dict(type="tableau", img="bh5-ford", fond=True, sombre=True, de=[1.3, .3, .5], a=[1.05, .55, .5],
                          legende="Chaîne de montage Ford, Highland Park, 1913 (domaine public)"),
        "hux2": dict(type="liste", titre="Le Meilleur des mondes (1932)", items=[
            "Des enfants fabriqués en série, conditionnés", "Des plaisirs permanents, la tristesse supprimée",
            "Les livres anciens interdits"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_fol": dict(type="tableau", img="bh5-folio", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .4],
                        legende="Shakespeare, Comedies, Histories & Tragedies, premier folio, 1623 (British Library)"),
        "john": dict(type="def", cles=["malheureux"], terme="Le « Sauvage » de Huxley",
                     t="Il réclame la poésie, le danger, la liberté…",
                     etape="… et le droit d'être malheureux.", x=170, y=200, w=940),
        "noz": dict(type="liste", titre="Rappel · la machine à expérience (épisode 1)", items=[
            "Nous voulons que ce soit vrai, et que ce soit nous",
            "Un bonheur fabriqué et imposé n'est plus le nôtre"], marques=["1", "→"], x=170, y=180, w=940),
        "tab_dec2": dict(type="tableau", img="bh4-declaration", fond=True, sombre=True, de=[1.3, .3, .5], a=[1.05, .5, .5],
                         legende="John Trumbull, La Déclaration d'indépendance, 1819 (Capitole des États-Unis, Washington)"),
        "rep": dict(type="cols", g="Faire le bonheur des gens", gq="à leur place : le despotisme, même doux",
                    d="Garantir ses conditions", dq="sécurité, justice, éducation, santé, libertés", vs="≠",
                    repere="La distinction qui dépasse"),
        "tab_dz": dict(type="tableau", img="bh5-dzong", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                       legende="Le dzong de Punakha, Bhoutan (photo Bernard Gagnon, CC BY-SA 4.0)"),
        "bh": dict(type="note", titre="Pour aller plus loin · le Bhoutan", cles=["conditions", "rechercher"],
                   t="Constitution de 2008 : l'État promeut les conditions qui permettent de rechercher le « bonheur national brut ».",
                   etape="Les mots clés : les conditions, la recherche.", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Kant. Le bonheur ne fonde pas la morale ; "
        "la morale apprend à se rendre digne du bonheur.",
        "{rec.2}Deux : l'utilitarisme fait du bonheur de tous le critère des lois. Mais la question d'Ivan Karamazov demeure : "
        "peut-on bâtir le bonheur sur les larmes d'un seul ?",
        "{rec.3}Trois : depuis 1776, le bonheur entre en politique. Mais Kant et Tocqueville mettent en garde : "
        "un pouvoir qui veut notre bonheur à notre place devient un despotisme, même doux.",
        "{rec.4}Quatre : la distinction pour ta copie. Faire le bonheur des citoyens, non ; en garantir les conditions, oui.",
        "{-rec}{tab_fin}{q_suite}Tu as maintenant toutes les pièces. Reste à les assembler, le jour de l'épreuve, "
        "devant un sujet que tu n'as pas choisi.",
        "{-q_suite}{fin}",
        ("La prochaine fois : le bonheur à l'épreuve du bac. Trois sujets, et un texte d'Épicure.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="BONHEUR, MORALE ET POLITIQUE", branches=[
            dict(t="Kant", items=["le bonheur ne fonde pas la morale", "se rendre digne du bonheur", "le souverain bien"]),
            dict(t="L'utilitarisme", items=["le plus grand bonheur du plus grand nombre", "chacun compte pour un", "Ivan Karamazov"]),
            dict(t="L'État et le bonheur", items=["1776 : la recherche du bonheur", "Saint-Just : une idée neuve", "Kant : l'État paternel"]),
            dict(t="Le despotisme doux", items=["Tocqueville : le troupeau", "Huxley : le soma", "garantir les conditions"])]),
        "tab_fin": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "q_suite": dict(type="question", t="Le bonheur est-il affaire de chance ?"),
        "fin": dict(type="titre", sur="À suivre", t="Le bonheur à l'épreuve du bac", sous="Épisode 6 · Trois sujets, un texte d'Épicure"),
    }),
]

QUIZ = [
    dict(q="Pourquoi, selon Kant, le bonheur ne peut-il pas fonder la morale ?",
         r=["Parce qu'il est mauvais", "Parce qu'il est indéterminé et ne donne que des conseils, non des lois",
            "Parce que Dieu l'interdit", "Parce qu'il est réservé aux riches"], ok=1,
         voir="trois", ex="Chacun l'imagine à sa façon ; il ne commande que sous condition (impératif hypothétique) et corrompt le motif."),
    dict(q="Pour Kant, la morale nous apprend…",
         r=["à nous rendre heureux", "à nous rendre dignes du bonheur", "à fuir le bonheur", "à calculer le plaisir"], ok=1,
         voir="c_dig", ex="Critique de la raison pratique (1788) : la morale n'est pas une doctrine du bonheur, mais de la dignité d'être heureux."),
    dict(q="Selon Bentham, une loi est bonne si…",
         r=["elle est voulue par Dieu", "elle augmente la somme de bonheur dans la société", "elle respecte la tradition",
            "elle plaît au roi"], ok=1,
         voir="pol", ex="Le principe d'utilité, boussole du législateur ; chacun compte pour un, personne pour plus d'un."),
    dict(q="Que montre la question d'Ivan Karamazov ?",
         r=["Que le bonheur est impossible", "Que le bonheur collectif ne justifie pas de sacrifier un innocent",
            "Que les enfants sont plus heureux", "Que l'utilitarisme a toujours raison"], ok=1,
         voir="ivan", ex="Les Frères Karamazov (1880) : bâtir le bonheur humain sur les larmes d'un seul enfant ? Aliocha refuse."),
    dict(q="Que garantit la Déclaration d'indépendance de 1776 ?",
         r=["Le bonheur de chaque citoyen", "Le droit de rechercher le bonheur", "Le bonheur commun", "Le bonheur national brut"], ok=1,
         voir="pur", ex="« The pursuit of happiness » : l'État protège le droit de chercher le bonheur, il ne le promet pas."),
    dict(q="« Le bonheur est une idée neuve en Europe. » Qui le dit, et quand ?",
         r=["Rousseau, en 1762", "Saint-Just, en 1794", "Tocqueville, en 1840", "Kant, en 1793"], ok=1,
         voir="c_sj", ex="Rapport à la Convention du 3 mars 1794 : le bonheur devient un but politique… en pleine Terreur."),
    dict(q="Pour Kant, le pire despotisme est…",
         r=["un gouvernement paternel, qui décide du bonheur des citoyens à leur place", "une république",
            "un gouvernement patriotique", "l'absence de gouvernement"], ok=0,
         voir="pat", ex="Théorie et pratique (1793) : nul ne peut me contraindre à être heureux à sa manière."),
    dict(q="Qu'appelle-t-on le despotisme doux, chez Tocqueville ?",
         r=["Un tyran cruel", "Un pouvoir tutélaire qui veut notre bonheur et nous fixe dans l'enfance",
            "Une démocratie directe", "Une anarchie heureuse"], ok=1,
         voir="trp", ex="De la démocratie en Amérique, II, IV, 6 : un troupeau d'animaux timides et industrieux, dont le gouvernement est le berger."),
]

CREDITS = [
    "Portraits : Kant (portrait anonyme, XVIIIᵉ s.) ; Jeremy Bentham ; John Stuart Mill (G. F. Watts, 1873) ; Fiodor Dostoïevski (Vassili Perov, 1872) ; "
    "Thomas Jefferson (Rembrandt Peale, 1800, Maison-Blanche) ; Saint-Just (anonyme, autrefois attribué à Pierre-Paul Prud'hon, "
    "musée des Beaux-Arts de Lyon) ; Tocqueville (Théodore Chassériau) : domaine public",
    "Tableaux et gravures : Jean Siméon Chardin, Le Philosophe lisant (1734) ; Gustave Doré, La Rose céleste (Paradis, chant XXXI, 1868) ; "
    "William Powell Frith, Le Jour du Derby (1856-1858) ; Vassili Perov, Troïka (1866) ; John Trumbull, La Déclaration d'indépendance (1819) ; "
    "Charles-Louis Müller, Lanjuinais à la tribune de la Convention (XIXᵉ s.) ; Déclaration des droits de 1793 (estampe) ; "
    "L'Exécution de Robespierre (gravure, 1794) ; Jean-Baptiste Greuze, La Lecture de la Bible (1755) ; "
    "Anton Mauve, Le Retour du troupeau (XIXᵉ s.) ; Shakespeare, premier folio (1623) : domaine public",
    "Photographies : chaîne de montage Ford, 1913 (domaine public) ; Königsberg, photochrome (domaine public) ; "
    "gélules (Tom Varco, CC BY-SA 3.0) ; hémicycle de l'Assemblée nationale (Coucouoeuf, CC BY-SA 3.0) ; dzong de Punakha (Bernard Gagnon, CC BY-SA 4.0) ; salle d'examen (domaine public)",
    "Citations : Kant, Critique de la raison pratique (1788) et Sur le proverbe… (1793), trad. Jules Barni, Wikisource ; "
    "Tocqueville, De la démocratie en Amérique, II, IV, 6 (1840), Wikisource ; Saint-Just, rapport du 3 mars 1794 ; "
    "Déclaration d'indépendance des États-Unis (1776), trad. courante. Dostoïevski, Les Frères Karamazov (1880) et "
    "Aldous Huxley, Le Meilleur des mondes (1932) : résumés.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
