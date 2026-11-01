"""Le devoir, épisode 5 : « Conflits de devoirs »

Texte lu (beats) et visuels de chaque scène ; même format que liberte_1.py (voir son en-tête).
Antigone (Sophocle ; Hegel pour aller plus loin), la désobéissance civile (Thoreau, Rosa Parks, Martin Luther King ;
Socrate et le Criton en contrepoint), Eichmann et Arendt (obéir n'excuse pas), Milgram (sans image),
le jeune homme de Sartre (renvoi à la série « La liberté »), Javert, Weber pour aller plus loin.
Notions abordées : champ notions des scènes et repères {#…}.
"""

CODE = "devoir-5"
NOTION = "Le devoir"
NUM = 5
TITRE = "Conflits de devoirs"
SUIVANT = "Épisode 6 · Le devoir à l'épreuve du bac"

PRONONCIATION = {"Polynice": "Polinice", "Étéocle": "Étéocle", "Hémon": "Émon", "Thoreau": "Toro",
                 "Eichmann": "Aïkmane", "Arendt": "Arènnte", "Milgram": "Milgrame", "Walden": "Ouôldenne",
                 "Montgomery": "Montgomeri", "Birmingham": "Birmingueme", "Tirésias": "Tirésiasse"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_lyt}Thèbes, il y a vingt-cinq siècles. La guerre vient de finir. Deux frères, Étéocle et Polynice, "
        "se sont entretués devant les portes de la ville : l'un la défendait, l'autre l'attaquait.",
        "Le nouveau roi, Créon, a pris sa décision. Étéocle aura des funérailles de héros. "
        "Polynice, le traître, restera sans sépulture, abandonné aux chiens et aux oiseaux. "
        "Quiconque l'enterrera sera puni de mort.",
        "{q_ant}Mais Polynice a une sœur : Antigone. Cette nuit, elle sort de la ville. "
        "Et, de ses mains, elle jette sur le corps de son frère une poignée de poussière.",
        "{-q_ant}{deux}Elle sait ce qu'elle risque. Elle a deux devoirs, et ils se contredisent. "
        "{deux.1}Obéir à la loi du roi. {deux.2}Ou rendre à son frère les honneurs que les dieux exigent pour les morts.",
        ("Que faire, quand deux devoirs s'opposent ?", {"rate": "-6%", "pitch": "-2Hz"}),
        "Jusqu'ici, le devoir semblait simple : savoir ce qu'il faut faire, puis avoir le courage de le faire. "
        "Aujourd'hui, la vraie difficulté apparaît : savoir quel devoir l'emporte.",
        ("P", 0.3),
        "{-deux}{-tab_lyt}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_lyt": dict(type="tableau", img="dv5-lytras", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .45],
                        legende="Nikiphoros Lytras, Antigone devant le corps de Polynice, 1865 (photo Francesco Bini, CC BY-SA 4.0)"),
        "q_ant": dict(type="question", t="Obéir au roi, ou enterrer son frère ?"),
        "deux": dict(type="cols", g="La loi du roi", gq="Polynice restera sans sépulture",
                     d="La loi des dieux", dq="on doit enterrer ses morts", vs="⚡",
                     repere="Sophocle, Antigone (vers 441 av. J.-C.)"),
        "titre": dict(type="titre", sur="Le devoir · Épisode 5", t="Conflits de devoirs",
                      sous="Antigone, la désobéissance, l'obéissance"),
    }),

    # ------------------------------------------------------------------ I. Antigone
    dict(id="antigone", chap="Antigone : la loi contre la loi", fond="aube", humeur="mystere",
         notions=["la justice", "l'État", "la religion"],
         retenir="Antigone oppose aux décrets de Créon les « lois non écrites » des dieux. Hegel : deux droits légitimes, chacun partiel.",
         beats=[
        "{soph}{tab_dio}C'est l'histoire que raconte Sophocle, dans sa tragédie Antigone, jouée à Athènes vers 441 avant notre ère. "
        "Antigone est arrêtée et conduite devant Créon. Le roi lui demande si elle connaissait son décret. "
        "Elle répond : oui. Et elle ajoute :",
        ("C", "Je ne pensais pas que tes décrets fussent assez forts pour permettre à un mortel de passer outre "
              "aux lois non écrites et immuables des dieux.", "c_ant"),
        "{-soph}{-c_ant}{lois}Voilà le conflit. {lois.1}D'un côté, la loi écrite : celle de la cité, proclamée par le roi. "
        "{lois.2}De l'autre, des lois non écrites, que personne n'a votées, et qui pourtant obligent : "
        "enterrer ses morts, respecter les liens du sang.",
        "Antigone ne désobéit pas par caprice. Elle désobéit au nom d'une {#la justice}justice plus haute que la loi. "
        "C'est pourquoi on a fait d'elle, depuis, le symbole de la résistance. En 1944, dans Paris occupé, "
        "Jean Anouilh fait jouer sa propre Antigone : le public y entend, à mots couverts, le refus de plier.",
        "{-lois}{cre}Mais Créon n'est pas un simple tyran. Lui aussi défend un devoir. Polynice a pris les armes contre "
        "sa propre patrie. Si le roi honore le traître comme le héros, il n'y a plus de cité. "
        "Pour Créon, le devoir du citoyen, c'est d'obéir à la loi commune, même quand elle est dure.",
        "Et Créon s'entête. Céder à une jeune fille, pense-t-il, ce serait ruiner l'autorité de la loi. "
        "Son fils le supplie, le peuple murmure : il n'écoute personne.",
        "{-cre}{-tab_dio}{tab_dio2}La pièce finit en catastrophe. Créon fait enfermer Antigone vivante dans un tombeau de pierre. "
        "Le devin Tirésias l'avertit : les dieux sont offensés. Trop tard. Antigone s'est pendue. "
        "Hémon, le fils de Créon, qui l'aimait, se tue sur son corps. La reine se donne la mort à son tour.",
        "La loi de la cité et la loi de la {#la religion}religion se sont broyées l'une l'autre.",
        "{-tab_dio2}{heg}{hegn}Pour aller plus loin, Hegel a proposé de cette tragédie une lecture devenue célèbre. "
        "Selon lui, il n'y a pas ici un bon et un méchant. Il y a deux droits, aussi légitimes l'un que l'autre : "
        "le droit de la famille et des dieux, et le droit de l'État.",
        "Le malheur vient de ce que chacun ne voit que le sien. Antigone et Créon ont tous deux raison, "
        "et tous deux tort : leur faute est d'être unilatéraux.",
        ("Le tragique, ce n'est pas le bien contre le mal. C'est le bien contre le bien.", {"rate": "-5%", "pitch": "-1Hz"}),
        "{-heg}{-hegn}",
        ("P", 0.5),
    ], vis={
        "soph": dict(type="portrait", annee=-496, img="sophocle", nom="Sophocle", dates="vers 496 – 406 av. J.-C.",
                     legende="Antigone (vers 441 av. J.-C.)", x=110, y=120, w=330, h=420),
        "tab_dio": dict(type="tableau", img="dv5-diotti", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Giuseppe Diotti, Antigone condamnée à mort par Créon, 1845"),
        "c_ant": dict(type="cit", a="Antigone", o="Sophocle, Antigone, v. 453-455 (citation approchée, trad. courante)",
                      x=640, y=150, w=570),
        "lois": dict(type="liste", titre="Deux lois", items=[
            "La loi écrite : le décret du roi, la loi de la cité",
            "Les lois non écrites : enterrer ses morts, respecter les liens du sang"],
                     marques=["1", "2"], cles=["écrite", "non écrites"], x=170, y=190, w=940),
        "cre": dict(type="note", titre="Le devoir de Créon", cles=["traître", "loi commune"],
                    t="Polynice a attaqué sa patrie. Honorer le traître comme le héros, c'est ruiner la cité.",
                    etape="Le devoir du citoyen : obéir à la loi commune, même quand elle est dure.", x=170, y=190, w=940),
        "tab_dio2": dict(type="tableau", img="dv5-diotti", fond=True, sombre=True, de=[1.3, .6, .45], a=[1.6, .45, .4],
                         legende="Giuseppe Diotti, Antigone condamnée à mort par Créon, 1845"),
        "heg": dict(type="portrait", annee=1770, img="hegel", nom="G. W. F. Hegel", dates="1770 – 1831",
                    legende="Phénoménologie de l'esprit (1807), Esthétique", x=110, y=120, w=330, h=420),
        "hegn": dict(type="note", titre="Pour aller plus loin", cles=["deux droits", "unilatéraux"],
                     t="Hegel : la famille et les dieux contre l'État. Deux droits légitimes, chacun aveugle à l'autre.",
                     etape="Le tragique : le bien contre le bien.", x=640, y=170, w=570),
    }),

    # ------------------------------------------------------------------ II. la désobéissance civile
    dict(id="desobeir", chap="Désobéir à la loi", fond="nuit", humeur="tension",
         notions=["l'État", "la justice", "la liberté"],
         retenir="Désobéissance civile : enfreindre publiquement une loi injuste, sans violence, en acceptant la sanction (Thoreau, Parks, King).",
         beats=[
        "{thor}{tab_wal}Vingt-trois siècles plus tard, dans le Massachusetts. En 1846, un écrivain, Henry David Thoreau, "
        "vit seul dans une cabane, au bord du lac de Walden. Depuis des années, il refuse de payer un impôt.",
        "La raison ? Son {#l'État}État admet l'esclavage, et il mène contre le Mexique une guerre qu'il juge injuste. "
        "Thoreau ne veut pas financer cela. Il passe une nuit en prison, puis écrit un texte qui fera le tour du monde : "
        "La Désobéissance civile.",
        ("C", "Je pense que nous devons être hommes d'abord, et sujets ensuite.", "c_tho"),
        "{-c_tho}{-thor}{-tab_wal}{tab_gan}Ce texte, Gandhi le lira en Afrique du Sud. En 1930, en Inde, il marche "
        "pendant vingt-quatre jours jusqu'à la mer, pour y ramasser du sel : un geste interdit par la loi coloniale britannique.",
        "{-tab_gan}{tab_par}Et le premier décembre 1955, à Montgomery, en Alabama, une couturière de quarante-deux ans, Rosa Parks, "
        "refuse de céder sa place à un passager blanc dans un bus. Elle est arrêtée. "
        "Toute la communauté noire de la ville boycotte alors les bus, pendant plus d'un an. "
        "On marche à pied, on partage les voitures, jusqu'à ce que la Cour suprême déclare la ségrégation des bus contraire à la Constitution.",
        "{-tab_par}{king}{tab_cel}Le jeune pasteur qui mène ce boycott s'appelle Martin Luther King. "
        "En 1963, emprisonné à Birmingham, il écrit une lettre qui pose le principe :",
        ("C", "On a la responsabilité morale de désobéir aux lois injustes.", "c_kin"),
        "{-c_kin}Mais pas n'importe comment. Il ajoute que celui qui enfreint une loi injuste doit le faire "
        "ouvertement, avec amour, et en acceptant la sanction.",
        "{-king}{-tab_cel}{civ}C'est ce qui distingue la {!désobéissance civile}désobéissance civile de la simple délinquance. "
        "{civ.1}Elle est publique : on ne se cache pas. {civ.2}Elle est non violente. "
        "{civ.3}Elle se fait au nom de principes que tous peuvent comprendre, pas d'un intérêt privé. "
        "{civ.4}Et on accepte la peine : on reconnaît la loi en général, on n'en refuse qu'une.",
        "{-civ}{tab_soc}{crit}Reste une objection sérieuse. Si chacun peut désobéir dès qu'il juge une loi injuste, "
        "que reste-t-il de la loi ? Socrate, condamné à mort injustement, refusa de s'enfuir de sa prison. "
        "Dans le Criton de Platon, il imagine les Lois d'Athènes venant lui demander : veux-tu donc nous détruire ?",
        "Voilà pourquoi la désobéissance doit rester une exception, pesée, assumée, et non une habitude.",
        "{-crit}{-tab_soc}{tab_mar}En 1963, deux cent cinquante mille personnes marchent sur Washington. "
        "Un an plus tard, la ségrégation est abolie par la loi. La désobéissance d'hier est devenue le droit d'aujourd'hui.",
        "{-tab_mar}",
        ("P", 0.5),
    ], vis={
        "thor": dict(type="portrait", annee=1817, img="thoreau", nom="Henry David Thoreau", dates="1817 – 1862",
                     legende="La Désobéissance civile (1849)", x=110, y=120, w=330, h=420),
        "tab_wal": dict(type="tableau", img="dv5-walden", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                        legende="Réplique de la cabane de Thoreau à Walden, Concord (photo John Phelan, CC BY 4.0)"),
        "c_tho": dict(type="cit", a="Thoreau", o="La Désobéissance civile (1849), trad. courante", x=640, y=200, w=570),
        "tab_gan": dict(type="tableau", img="dv5-gandhi", fond=True, de=[1.0, .5, .5], a=[1.2, .45, .45],
                        legende="Gandhi pendant la marche du sel, 1930 (domaine public)"),
        "tab_par": dict(type="tableau", img="dv5-parks", de=[1.0, .5, .4], a=[1.25, .7, .35],
                        legende="Rosa Parks au bureau du shérif, Montgomery, 1956 (photo Gene Herrick, AP, domaine public)"),
        "king": dict(type="portrait", annee=1929, img="king", nom="Martin Luther King", dates="1929 – 1968",
                     legende="Lettre de la prison de Birmingham (1963)", x=110, y=120, w=330, h=420),
        "tab_cel": dict(type="tableau", img="dv5-cellule", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .4, .5],
                        legende="Reconstitution de la cellule de King à Birmingham (photo Adam Jones, CC BY-SA 3.0)"),
        "c_kin": dict(type="cit", a="Martin Luther King", o="Lettre de la prison de Birmingham (1963), trad. de l'anglais",
                      x=640, y=200, w=570),
        "civ": dict(type="liste", titre="La désobéissance civile", items=[
            "Publique : on agit à visage découvert", "Non violente",
            "Au nom de principes communs, pas d'un intérêt privé", "On accepte la sanction : on ne rejette pas toute loi"],
                    marques=["1", "2", "3", "4"], cles=["publique", "non violente", "principes", "sanction"],
                    x=170, y=150, w=940),
        "tab_soc": dict(type="tableau", img="t-socrate", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Jacques-Louis David, La Mort de Socrate, 1787 (Criton est assis à ses pieds)"),
        "crit": dict(type="note", titre="L'objection de Socrate", cles=["Lois", "détruire"],
                     t="Condamné injustement, Socrate refuse de fuir : désobéir, ce serait détruire les Lois qui l'ont fait citoyen.",
                     etape="Platon, Criton (vers 399 av. J.-C.)", x=170, y=190, w=940),
        "tab_mar": dict(type="tableau", img="dv5-marche", de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Marche sur Washington, 28 août 1963 (photo Marion S. Trikosko, Library of Congress, domaine public)"),
    }),

    # ------------------------------------------------------------------ III. obéir n'excuse pas
    dict(id="obeir", chap="Obéir n'excuse pas", fond="nuit", humeur="mystere", notions=["la conscience", "la raison"],
         retenir="Arendt : Eichmann « faisait son devoir ». La banalité du mal, c'est obéir sans penser. Obéir n'est pas faire son devoir.",
         beats=[
        "{tab_nur}Il existe aussi le cas inverse : ceux qui ont trop obéi. À Nuremberg, en 1945, les dignitaires nazis "
        "répètent tous la même phrase : j'ai obéi aux ordres.",
        "{tab_eic}Seize ans plus tard, à Jérusalem, s'ouvre le procès d'Adolf Eichmann. Il a organisé la déportation "
        "de millions de Juifs vers les camps de la mort. Dans sa cage de verre, il se défend : il n'a rien contre personne. "
        "Il a fait son devoir. Il ose même dire qu'il a vécu selon la morale de Kant.",
        "{-tab_eic}{are}{tab_eic2}Une philosophe assiste au procès : Hannah Arendt. Elle s'attendait à voir un monstre. "
        "Elle découvre un fonctionnaire ordinaire, appliqué, soucieux de sa carrière, qui parle en formules toutes faites.",
        "{ban}Elle en tire une expression qui fera scandale : la {!banalité du mal}banalité du mal. "
        "{ban.1}Le pire peut être commis par des gens ordinaires. {ban.2}Non par méchanceté, mais par absence de pensée : "
        "ils ne se demandent jamais ce qu'ils font.",
        "{-are}{-ban}{-tab_eic2}{mil}Une expérience de psychologie l'a confirmé. Au début des années soixante, à l'université Yale, "
        "Stanley Milgram demande à des volontaires d'envoyer des décharges électriques à un inconnu, "
        "chaque fois qu'il se trompe. Les décharges sont fausses, mais ils l'ignorent.",
        "{mil.1}La victime crie, supplie. {mil.2}Un homme en blouse grise répète calmement : l'expérience exige que vous continuiez. "
        "{mil.3}Près des deux tiers des participants vont jusqu'au bout : quatre cent cinquante volts.",
        ("Ils n'étaient pas cruels. Ils avaient simplement remis leur {#la conscience}conscience à un autre.",
         {"rate": "-5%", "pitch": "-1Hz"}),
        "Milgram a fait varier l'expérience. Quand l'expérimentateur donne ses ordres par téléphone, au lieu d'être "
        "dans la pièce, l'obéissance s'effondre. Quand deux autres participants refusent de continuer, presque tous "
        "les imitent. L'obéissance tient à la présence d'une autorité ; la désobéissance, au courage d'un premier qui dit non.",
        "{-mil}{kant}Alors, Eichmann était-il kantien ? Évidemment pas, et c'est très instructif. "
        "{-kant}{eick}{eick.g}Pour Kant, le devoir est la loi que ma propre raison se donne : il faut juger, penser par soi-même. "
        "{eick.d}Eichmann, lui, a remplacé sa raison par la volonté du chef.",
        "Obéir n'est donc pas faire son devoir. Celui qui obéit sans penser n'est pas fidèle au devoir : il l'a abandonné. "
        "Depuis Nuremberg, le droit international le dit aussi : l'ordre d'un supérieur n'efface pas la responsabilité.",
        "{-eick}",
        ("P", 0.5),
    ], vis={
        "tab_nur": dict(type="tableau", img="dv5-nuremberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .4],
                        legende="Le banc des accusés au procès de Nuremberg, 1945-1946 (photo Ray D'Addario, domaine public)"),
        "tab_eic": dict(type="tableau", img="dv5-eichmann", de=[1.0, .5, .3], a=[1.2, .45, .3],
                        legende="Adolf Eichmann à son procès, Jérusalem, 1961 (Israel Government Press Office, domaine public)"),
        "are": dict(type="portrait", annee=1906, img="arendt", nom="Hannah Arendt", dates="1906 – 1975",
                    legende="Eichmann à Jérusalem. Rapport sur la banalité du mal (1963)", x=110, y=120, w=330, h=420),
        "tab_eic2": dict(type="tableau", img="dv5-eichmann", fond=True, sombre=True, de=[1.2, .45, .3], a=[1.4, .5, .25],
                         legende="Adolf Eichmann à son procès, Jérusalem, 1961 (Israel Government Press Office, domaine public)"),
        "ban": dict(type="liste", titre="La banalité du mal", items=[
            "Le pire commis par des gens ordinaires", "Par absence de pensée, non par méchanceté"],
                    marques=["1", "2"], cles=["ordinaires", "absence de pensée"], x=640, y=200, w=570),
        "mil": dict(type="liste", titre="L'expérience de Milgram · Yale, 1961-1963", items=[
            "La victime (un acteur) crie et supplie", "« L'expérience exige que vous continuiez »",
            "Près des deux tiers vont jusqu'à 450 volts"], marques=["1", "2", "3"], cles=["exige", "450"],
                    x=170, y=170, w=940),
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Le devoir : la loi que ma raison se donne", x=110, y=120, w=330, h=420),
        "eick": dict(type="cols", g="Kant", gq="juger, penser par soi-même : l'autonomie", d="Eichmann",
                     dq="la volonté du chef à la place de la raison", vs="≠", repere="Obéir n'est pas faire son devoir"),
    }),

    # ------------------------------------------------------------------ IV. quand aucune règle ne tranche
    dict(id="dilemme", chap="Quand aucune règle ne tranche", fond="aube", humeur="calme", notions=["la liberté", "la justice"],
         retenir="Aucune règle ne tranche tous les conflits : il faut juger. Weber : conviction et responsabilité doivent se compléter.",
         beats=[
        "{sar}{tab_par40}Et quand les deux devoirs sont également respectables ? Tu connais déjà ce cas : "
        "nous l'avons vu dans la série sur la liberté. Pendant l'Occupation, un élève de Sartre vient lui demander conseil.",
        "{-sar}{choix}{choix.g}Partir en Angleterre rejoindre les Forces françaises libres, pour combattre. "
        "{choix.d}Ou rester auprès de sa mère, seule, qui ne vit plus que pour lui.",
        "{-choix}Aucune morale toute faite ne peut trancher à sa place. Sartre lui répond :",
        ("C", "Vous êtes libre, choisissez, c'est-à-dire inventez.", "c_sar"),
        "{-c_sar}{-tab_par40}{tab_jav}Victor Hugo a imaginé un autre déchirement. Javert, dans Les Misérables, "
        "est le policier parfait : la loi, toute la loi. Il poursuit Jean Valjean, l'ancien forçat, pendant des années.",
        "Un jour, Valjean lui sauve la vie. Javert, pour la première fois, laisse partir un coupable. "
        "Et il ne le supporte pas : un homme qui n'a jamais connu qu'un seul devoir ne sait pas vivre entre deux. "
        "Il se jette dans la Seine.",
        "{-tab_jav}{web}Pour aller plus loin, le sociologue Max Weber a distingué deux façons d'agir. "
        "{-web}{wcol}{wcol.g}L'éthique de conviction : faire ce qui est juste, quoi qu'il arrive. "
        "{wcol.d}L'éthique de responsabilité : répondre des conséquences prévisibles de ses actes.",
        "Pour Weber, l'homme accompli n'est pas celui qui choisit l'une contre l'autre, mais celui qui les tient ensemble, "
        "et qui peut dire, au moment décisif : je ne puis faire autrement.",
        "{-wcol}Kant, lui, soutenait qu'un vrai conflit de devoirs est impensable : l'un des deux, bien examiné, "
        "se révèle n'être qu'apparent. Mais pour le découvrir, encore faut-il examiner.",
        "{jug}Retiens la leçon. Un conflit de devoirs ne se résout pas en appliquant une règle : "
        "il exige de juger. Et juger, c'est l'exercice même de notre {#la liberté}liberté.",
        "{-jug}",
        ("P", 0.5),
    ], vis={
        "sar": dict(type="portrait", annee=1905, img="sartre", nom="Jean-Paul Sartre", dates="1905 – 1980",
                    legende="L'existentialisme est un humanisme (1946)", x=110, y=120, w=330, h=420),
        "tab_par40": dict(type="tableau", img="t2-paris40", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                          legende="Paris sous l'Occupation (Bundesarchiv, photo Friedrich, CC BY-SA 3.0 DE)"),
        "choix": dict(type="cols", g="Partir", gq="rejoindre la France libre, combattre", d="Rester",
                      dq="soutenir sa mère, qui n'a plus que lui", vs="?",
                      repere="Série « La liberté », épisode 2"),
        "c_sar": dict(type="cit", a="Sartre", o="L'existentialisme est un humanisme (1946)", x=170, y=230, w=940),
        "tab_jav": dict(type="tableau", img="dv5-javert", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="Gustave Brion, Javert, pour Les Misérables de Victor Hugo, 1862"),
        "web": dict(type="portrait", annee=1864, img="weber", nom="Max Weber", dates="1864 – 1920",
                    legende="Le Savant et le Politique (1919)", x=110, y=120, w=330, h=420),
        "wcol": dict(type="cols", g="Conviction", gq="faire ce qui est juste, quoi qu'il arrive",
                     d="Responsabilité", dq="répondre des conséquences prévisibles", vs="+",
                     repere="Pour aller plus loin · Weber"),
        "jug": dict(type="mot", t="Juger", g="aucune règle ne tranche à notre place", y=250, taille=90),
    }),

    # ------------------------------------------------------------------ V. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir. {rec.1}Un : Antigone. Les lois non écrites contre le décret du roi. "
        "Et, avec Hegel, l'idée que le tragique, c'est le bien contre le bien.",
        "{rec.2}Deux : la désobéissance civile. Thoreau, Rosa Parks, Martin Luther King : désobéir à une loi injuste, "
        "publiquement, sans violence, en acceptant la sanction. Mais Socrate rappelle qu'on ne détruit pas les lois à la légère.",
        "{rec.3}Trois : Eichmann. Obéir n'excuse pas. La banalité du mal naît de l'absence de pensée.",
        "{rec.4}Quatre : le jeune homme de Sartre et Javert. Quand aucune règle ne tranche, il faut juger, "
        "en tenant ensemble conviction et responsabilité.",
        "{-rec}{tab_lyt2}{fin_q}Revenons à Antigone, une poignée de poussière à la main. "
        "Elle n'a pas choisi entre le devoir et l'absence de devoir. Elle a choisi entre deux devoirs. "
        "Et c'est peut-être cela, la situation morale par excellence.",
        ("La prochaine fois, nous passons à la pratique : le devoir, le jour du bac.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-fin_q}{-tab_lyt2}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="CONFLITS DE DEVOIRS", branches=[
            dict(t="Antigone", items=["lois non écrites / décret du roi", "Créon : le devoir civique", "Hegel : le bien contre le bien"]),
            dict(t="Désobéir", items=["Thoreau, Gandhi", "Rosa Parks, M. L. King", "Socrate : respecter les lois"]),
            dict(t="Obéir n'excuse pas", items=["Eichmann, Nuremberg", "Arendt : la banalité du mal", "Milgram : 450 volts"]),
            dict(t="Juger", items=["le jeune homme de Sartre", "Javert", "Weber : conviction et responsabilité"])]),
        "tab_lyt2": dict(type="tableau", img="dv5-lytras", fond=True, sombre=True, de=[1.3, .3, .45], a=[1.0, .5, .5],
                         legende="Nikiphoros Lytras, Antigone devant le corps de Polynice, 1865 (photo Francesco Bini, CC BY-SA 4.0)"),
        "fin_q": dict(type="question", t="Choisir, non entre le devoir et rien, mais entre deux devoirs"),
        "tab_fin": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                        legende="Salle d'examen"),
        "fin": dict(type="titre", sur="À suivre", t="Le devoir à l'épreuve du bac",
                    sous="Épisode 6 · Dissertations et explication de texte"),
    }),
]

QUIZ = [
    dict(q="Au nom de quoi Antigone désobéit-elle à Créon ?",
         r=["De son intérêt personnel", "Des « lois non écrites et immuables des dieux »", "D'une loi votée par le peuple",
            "De l'ordre d'un autre roi"], ok=1, voir="c_ant",
         ex="Elle oppose au décret du roi les lois non écrites : enterrer ses morts, respecter les liens du sang."),
    dict(q="Comment Hegel lit-il la tragédie d'Antigone ?",
         r=["Antigone a raison, Créon a tort", "Créon a raison, Antigone a tort",
            "Deux droits légitimes s'affrontent, chacun unilatéral", "C'est une simple histoire de famille"], ok=2, voir="hegn",
         ex="Le droit de la famille et des dieux contre celui de l'État : le tragique, c'est le bien contre le bien."),
    dict(q="Laquelle de ces conditions ne définit PAS la désobéissance civile ?",
         r=["Agir publiquement", "Agir sans violence", "Agir en secret pour échapper à la sanction",
            "Agir au nom de principes communs"], ok=2, voir="civ",
         ex="King : enfreindre une loi injuste « ouvertement, avec amour, et en acceptant la sanction »."),
    dict(q="Pourquoi Thoreau refuse-t-il de payer l'impôt ?",
         r=["Il le trouve trop élevé", "Son État admet l'esclavage et mène une guerre qu'il juge injuste",
            "Il veut vivre sans argent", "Il conteste l'élection du président"], ok=1, voir="c_tho",
         ex="La Désobéissance civile (1849) : « être hommes d'abord, et sujets ensuite »."),
    dict(q="Que signifie la « banalité du mal » selon Arendt ?",
         r=["Que le mal n'est pas grave", "Que le pire peut être commis par des gens ordinaires, par absence de pensée",
            "Que tout le monde est méchant", "Que le mal est toujours puni"], ok=1, voir="ban",
         ex="Eichmann n'était pas un monstre mais un fonctionnaire qui ne se demandait jamais ce qu'il faisait."),
    dict(q="Pourquoi Eichmann ne pouvait-il pas se réclamer de Kant ?",
         r=["Parce que Kant interdit tout ordre", "Parce que pour Kant le devoir suppose de penser par soi-même",
            "Parce que Kant était allemand", "Parce que Kant ne parle jamais de devoir"], ok=1, voir="eick",
         ex="Le devoir kantien est autonomie : la loi que ma raison se donne. Eichmann a mis la volonté du chef à la place."),
    dict(q="Que distingue Max Weber ?",
         r=["La loi et la coutume", "L'éthique de conviction et l'éthique de responsabilité",
            "Le devoir et le bonheur", "La morale et la religion"], ok=1, voir="wcol",
         ex="Le Savant et le Politique (1919) : faire ce qui est juste, et répondre des conséquences ; les deux doivent se compléter."),
]

CREDITS = [
    "Portraits : Sophocle (buste, musées du Capitole) ; Hegel (Jakob Schlesinger, 1831) ; Thoreau (daguerréotype de B. D. Maxham, 1856) ; "
    "Martin Luther King (photo Dick DeMarsico, New York World-Telegram, 1964) ; Hannah Arendt (photographie anonyme, 1933) ; "
    "Kant (portrait anonyme, XVIIIᵉ s.) ; Max Weber (photo Ernst Gottmann, 1918) : domaine public ; "
    "Sartre : photographie de 1965, Nationaal Archief / Anefo (CC BY-SA 3.0 NL)",
    "Tableaux et gravures : Nikiphoros Lytras, Antigone devant le corps de Polynice (1865 ; photo Francesco Bini, CC BY-SA 4.0) ; "
    "Giuseppe Diotti, Antigone condamnée à mort par Créon (1845) ; J.-L. David, La Mort de Socrate (1787) ; "
    "Gustave Brion, Javert (1862) : domaine public",
    "Photographies : Rosa Parks au bureau du shérif (Gene Herrick, AP, 1956) ; marche du sel (1930) ; marche sur Washington "
    "(Marion S. Trikosko, 1963) ; procès de Nuremberg (Ray D'Addario) ; Eichmann (Israel Government Press Office, 1961) : "
    "domaine public. Paris sous l'Occupation (Bundesarchiv, Friedrich, CC BY-SA 3.0 DE) ; Cabane de Walden (John Phelan, CC BY 4.0) ; cellule de Birmingham (Adam Jones, CC BY-SA 3.0)",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
