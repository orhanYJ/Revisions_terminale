"""La conscience, épisode 4 : « Conscience, monde et autrui »

Même format que les séries « La liberté », « Le devoir » et « Le bonheur » (voir liberte_1.py, devoir_3.py).
Citations : Husserl, Méditations cartésiennes, § 14 (1929 ; trad. G. Peiffer et E. Levinas, 1931) ;
Sartre, « Une idée fondamentale de la phénoménologie de Husserl : l'intentionnalité » (1939, repris dans Situations I),
et L'Être et le Néant, IIIᵉ partie, chap. I, « Le regard » (1943) : citations courtes ;
Hegel, Esthétique, Introduction (cours de 1818-1829), trad. S. Jankélévitch : citation approchée ;
Bergson, « La conscience et la vie » (conférence Huxley, Birmingham, 1911), dans L'Énergie spirituelle (1919),
vérifié sur Wikisource.
"""

CODE = "conscience-4"
NOTION = "La conscience"
NUM = 4
TITRE = "Conscience, monde et autrui"
SUIVANT = "Épisode 5 · La conscience morale"
PRONONCIATION = {"Husserl": "Houssèrl", "noèse": "noèze", "noème": "noème", "cogitatum": "coguitatoum",
                 "intendere": "inntèndéré", "Huxley": "Hukslé", "Birmingham": "Birmingueme"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_fen}{q1}Fais une petite expérience. Ferme les yeux, et essaie, pendant trois secondes, d'être conscient… "
        "de rien. Pas d'une image, pas d'un bruit, pas d'une pensée. De rien du tout.",
        ("P", 1.2),
        "{-q1}{ech}Alors ? {ech.1}Tu as entendu le frigo, ou la rue. {ech.2}Tu as senti ton souffle. "
        "{ech.3}Ou tu t'es surpris à penser : je ne pense à rien. Raté : c'était encore penser à quelque chose.",
        ("Personne n'y arrive. Et ce petit échec cache une grande découverte.", {"rate": "-5%"}),
        "{-ech}{rap}Jusqu'ici, nous avons surtout regardé la conscience du dedans : Descartes qui se retire en lui-même "
        "pour douter, puis l'inconscient qui déborde le moi. Mais si la conscience n'était pas une chambre fermée ? "
        "Si c'était plutôt… une fenêtre ?",
        ("P", 0.3),
        "{-rap}{-tab_fen}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_fen": dict(type="tableau", img="cs4-fenetre", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Caspar David Friedrich, Femme à la fenêtre, 1822 (Alte Nationalgalerie, Berlin)"),
        "q1": dict(type="question", t="Essaie d'être conscient… de rien."),
        "ech": dict(type="liste", titre="Trois secondes plus tard", items=[
            "Un bruit : le frigo, la rue", "Une sensation : ton souffle", "Une pensée : « je ne pense à rien »"],
                    marques=["1", "2", "3"], x=170, y=170, w=940),
        "rap": dict(type="cols", g="Une chambre fermée ?", gq="la conscience regardée du dedans",
                    d="Une fenêtre ?", dq="la conscience tournée vers le monde", vs="→"),
        "titre": dict(type="titre", sur="La conscience · Épisode 4", t="Conscience, monde et autrui",
                      sous="Husserl, Sartre, Hegel, Bergson"),
    }),

    # ------------------------------------------------------------------ I. Husserl
    dict(id="husserl", chap="Conscience de quelque chose", fond="aube", humeur="lumiere",
         notions=["la vérité", "la science"],
         retenir="Husserl : toute conscience est conscience de quelque chose. C'est l'intentionnalité : la conscience vise un objet.",
         beats=[
        "{husserl}{tab_cez}Au début du vingtième siècle, en Allemagne, un mathématicien devenu philosophe veut refonder "
        "la philosophie comme une science rigoureuse. Il s'appelle Edmund Husserl. {n_hus}Son mot d'ordre : revenir aux choses "
        "mêmes. Décrire ce qui apparaît, exactement comme cela apparaît.",
        "Et la première chose qu'il décrit, c'est la conscience. Dans les Méditations cartésiennes, en 1929, "
        "il formule ce que ton petit exercice vient de montrer.",
        "{-n_hus}",
        ("C", "Le mot intentionnalité ne signifie rien d'autre que cette particularité foncière et générale qu'a la conscience "
              "d'être conscience de quelque chose.", "c_hus"),
        "{-husserl}{-c_hus}{int}Retiens ce mot : l'intentionnalité. Du latin intendere : tendre vers, viser. "
        "{int.1}La conscience n'est pas une boîte qui contiendrait des images. C'est un mouvement, une flèche, "
        "toujours tournée vers autre chose qu'elle-même.",
        "{-int}{-tab_cez}{tab_arb}{vis}Prends un arbre. {vis.1}Je peux le percevoir, là, devant moi. "
        "{vis.2}Me souvenir de lui, l'été dernier. {vis.3}L'imaginer couvert de neige. "
        "{vis.4}Le désirer pour mon jardin, ou craindre qu'il tombe sur ma maison.",
        "{-vis}{noe}Chaque fois, c'est le même arbre, visé de façons différentes. Pour aller plus loin : "
        "{noe.g}Husserl appelle l'acte de viser la noèse, {noe.d}et l'objet tel qu'il est visé, le noème. "
        "Pas de perception sans perçu, pas de souvenir sans souvenu, pas de peur sans quelque chose qui fait peur.",
        "{-noe}{-tab_arb}{tab_desc}{cog}Mesure ce que cela change par rapport à Descartes. "
        "{cog.g}Descartes disait : je pense, donc je suis. {cog.d}Husserl précise : je pense… quelque chose. "
        "Le cogito ne va jamais sans son cogitatum, sans ce qui est pensé.",
        "{-cog}{ouv}Conséquence : on ne peut plus séparer, d'un côté, une conscience enfermée en elle-même, et de l'autre "
        "un monde dont il faudrait prouver l'existence. {ouv.1}La conscience est, d'emblée, ouverture au monde. "
        "Et la {#la vérité}vérité commence par une description fidèle de ce qui nous apparaît.",
        "{-ouv}{-tab_desc}",
    ], vis={
        "n_hus": dict(type="note", titre="La phénoménologie", cles=["choses", "décrire"],
                     t="Revenir aux choses mêmes : décrire ce qui apparaît, exactement comme cela apparaît.",
                     etape="Et d'abord la conscience elle-même.", x=640, y=150, w=570),
        "husserl": dict(type="portrait", annee=1859, img="husserl", nom="Edmund Husserl", dates="1859 – 1938",
                        legende="Méditations cartésiennes (1929)", x=110, y=120, w=330, h=420),
        "tab_cez": dict(type="tableau", img="cs4-cezanne", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .4],
                        legende="Paul Cézanne, La Montagne Sainte-Victoire, années 1880"),
        "c_hus": dict(type="cit", a="Husserl", o="Méditations cartésiennes, § 14 (1929), trad. Peiffer et Levinas",
                      x=640, y=170, w=570),
        "int": dict(type="def", cles=["intentionnalité", "flèche"], terme="L'intentionnalité",
                    t="Toute conscience est conscience de quelque chose : elle vise un objet hors d'elle.",
                    etape="Pas une boîte qui contient des images : une flèche tournée vers le monde.", x=170, y=200, w=940),
        "tab_arb": dict(type="tableau", img="cs4-arbre", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Piet Mondrian, L'Arbre gris, 1911 (Kunstmuseum, La Haye)"),
        "vis": dict(type="liste", titre="Un même arbre, visé de quatre façons", items=[
            "Le percevoir, là, devant moi", "M'en souvenir, l'été dernier", "L'imaginer couvert de neige",
            "Le désirer, ou le craindre"], marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "noe": dict(type="cols", g="La noèse", gq="l'acte de viser : percevoir, imaginer, se souvenir…",
                    d="Le noème", dq="l'objet tel qu'il est visé : l'arbre perçu, imaginé…", vs="↔", plus=True),
        "tab_desc": dict(type="tableau", img="t-christine", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .6],
                         legende="Nils Forsberg, Descartes à la cour de la reine Christine (d'après P.-L. Dumesnil), XIXᵉ siècle"),
        "cog": dict(type="cols", g="Descartes", gq="« je pense, donc je suis »", d="Husserl",
                    dq="je pense… quelque chose : pas de cogito sans cogitatum", vs="→"),
        "ouv": dict(type="def", cles=["ouverture"], terme="La conscience selon la phénoménologie",
                    t="Ni chambre fermée ni miroir du monde : une ouverture au monde.",
                    etape="La vérité commence par décrire fidèlement ce qui apparaît.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. Sartre : pas de dedans
    dict(id="sartre", chap="Une conscience sans dedans", fond="nuit", humeur="tension", notions=["la liberté", "la vérité"],
         retenir="Sartre : la conscience n'a pas de dedans, elle éclate vers le monde. N'étant pas une chose, elle peut se mentir : la mauvaise foi.",
         beats=[
        "{sartre}{tab_del}En 1933, un jeune professeur de philosophie du Havre part étudier un an à Berlin, pour lire Husserl "
        "dans le texte. C'est Jean-Paul Sartre. Il en revient ébloui, et écrit un article court, publié en 1939, "
        "qui sonne comme un manifeste.",
        "{n_sar}Il s'en prend à une vieille image : la conscience comme un estomac, qui avalerait les choses pour les digérer "
        "en idées. Contre cette philosophie digestive, comme il l'appelle, il lance une formule.",
        "{-n_sar}",
        ("C", "La conscience n'a pas de « dedans ».", "c_sar1"),
        "{-sartre}{-c_sar1}{ecl}Être conscient, c'est {!s'éclater vers}s'éclater vers le monde : {ecl.1}s'arracher à soi, "
        "filer là-bas, vers ce qui n'est pas soi. {ecl.2}Si tu pouvais entrer dans une conscience, dit-il en substance, "
        "tu serais pris dans un tourbillon, et rejeté dehors, près de l'arbre, en pleine poussière.",
        "{-ecl}{-tab_del}{tab_rue}{n_sent}Même nos sentiments sont dehors. Si je trouve une personne aimable, ce n'est pas "
        "une petite émotion rangée en moi, comme un objet dans un tiroir : c'est une manière dont cette personne m'apparaît, "
        "dans le monde. Et Sartre conclut.",
        "{-n_sent}",
        ("C", "Ce n'est pas dans je ne sais quelle retraite que nous nous découvrirons : c'est sur la route, dans la ville, "
              "au milieu de la foule, chose parmi les choses, homme parmi les hommes.", "c_sar2"),
        "{-c_sar2}{-tab_rue}{tab_cha}{neant}Pour aller plus loin. Si la conscience n'est rien d'autre que ce mouvement vers le monde, "
        "alors elle n'est pas une chose. Une cruche est une cruche, une pierre est une pierre : elles sont ce qu'elles sont, "
        "sans distance. {neant.1}Moi, je ne coïncide jamais tout à fait avec moi-même. Je suis toujours en train de me projeter, "
        "de choisir ce que je vais être.",
        "{-neant}{mf}C'est ce qui rend possible la mauvaise foi, qu'on a vue dans la série sur la {#la liberté}liberté, "
        "avec le garçon de café. {mf.1}On ne peut se mentir à soi-même que parce qu'on est une conscience : une chose ne se ment pas. "
        "{mf.2}Se dire « je suis timide, c'est comme ça », c'est vouloir être une chose, pour ne plus avoir à choisir.",
        "{-mf}{-tab_cha}",
    ], vis={
        "n_sar": dict(type="note", titre="Contre la philosophie digestive", cles=["estomac", "digestive"],
                     t="La conscience n'est pas un estomac qui avalerait les choses pour les digérer en idées.", x=640, y=150, w=570),
        "sartre": dict(type="portrait", annee=1905, img="sartre", nom="Jean-Paul Sartre", dates="1905 – 1980",
                       legende="« Une idée fondamentale de la phénoménologie de Husserl » (1939)", x=110, y=120, w=330, h=420),
        "tab_del": dict(type="tableau", img="cs4-delaunay", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Robert Delaunay, Les Fenêtres simultanées sur la ville, 1912"),
        "c_sar1": dict(type="cit", a="Sartre", o="« Une idée fondamentale de la phénoménologie de Husserl : l'intentionnalité » (1939)",
                       x=640, y=200, w=570),
        "ecl": dict(type="def", cles=["arracher", "tourbillon"], terme="« S'éclater vers » le monde",
                    t="Être conscient, c'est s'arracher à soi pour filer vers ce qui n'est pas soi.",
                    etape="Entrer dans une conscience ? On serait rejeté dehors, près de l'arbre.", x=170, y=200, w=940),
        "tab_rue": dict(type="tableau", img="cs4-rue", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .55],
                        legende="Gustave Caillebotte, Rue de Paris, temps de pluie, 1877 (Art Institute of Chicago)"),
        "n_sent": dict(type="note", titre="Les sentiments sont dehors", cles=["aimable", "tiroir"],
                      t="Trouver quelqu'un aimable : non pas une émotion rangée en moi comme dans un tiroir…",
                      etape="… mais une manière dont cette personne m'apparaît, dans le monde.", x=170, y=150, w=940),
        "c_sar2": dict(type="cit", a="Sartre", o="« Une idée fondamentale de la phénoménologie de Husserl » (1939), Situations I",
                       x=170, y=180, w=940),
        "tab_cha": dict(type="tableau", img="cs4-chardin", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .5],
                        legende="Jean Siméon Chardin, La Tabagie (Pipes et vase à boire), vers 1737 (musée du Louvre)"),
        "neant": dict(type="def", cles=["chose", "coïncide"], terme="La conscience n'est pas une chose", plus=True,
                      t="Une chose est ce qu'elle est ; la conscience ne coïncide jamais avec elle-même.",
                      etape="Elle se projette : elle choisit ce qu'elle va être.", x=170, y=190, w=940),
        "mf": dict(type="liste", titre="La mauvaise foi (série « La liberté », épisode 2)", items=[
            "Se mentir à soi-même : seule une conscience le peut", "« Je suis timide, c'est comme ça » : se faire chose"],
                   marques=["1", "2"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ III. le regard d'autrui
    dict(id="regard", chap="Le regard d'autrui", fond="aube", humeur="mystere", notions=["la liberté"],
         retenir="Sartre : autrui est le médiateur entre moi et moi-même. Sous son regard, j'ai honte de moi tel que je lui apparais.",
         beats=[
        "{tab_eco}{q_ser}Voici maintenant l'une des scènes les plus célèbres de la philosophie. Elle se trouve dans L'Être et le Néant, "
        "en 1943. Imagine : par jalousie, ou par curiosité, tu colles ton œil au trou d'une serrure.",
        "{-q_ser}{ser}{ser.1}Tu es tout entier dans ce que tu vois, derrière la porte. Tu ne penses pas à toi : "
        "il n'y a que la scène, et ton désir de voir. Ta conscience, comme dirait Husserl, est toute tournée vers son objet.",
        ("{ser.2}Soudain… des pas dans le couloir. Quelqu'un te regarde.", {"rate": "-8%"}),
        "{ser.3}Et tout bascule. Le rouge te monte au visage. D'un coup, tu existes pour toi-même… "
        "mais tel qu'un autre te voit : un voyeur, penché sur une serrure.",
        "{-ser}{-tab_eco}{sartre2}{tab_ada}Sartre décrit ce sentiment avec une précision redoutable.",
        ("C", "Autrui est le médiateur indispensable entre moi et moi-même. J'ai honte de moi tel que j'apparais à autrui.",
         "c_honte"),
        "{-sartre2}{-c_honte}{hon}Regarde bien la structure de la {!honte}honte. {hon.1}Elle est honte de moi : "
        "c'est bien moi qui suis visé. {hon.2}Mais elle est honte devant autrui : seul, je ne l'éprouverais pas. "
        "Le regard de l'autre me révèle une part de moi que je ne pouvais pas voir seul.",
        "{-hon}{-tab_ada}{tab_bar}{obj}{obj.g}Sous le regard d'autrui, je deviens un objet : il me juge, il me fige, "
        "il me prête une nature. {obj.d}Mais sans lui, je ne saurais pas qui je suis aux yeux du monde. "
        "Autrui me vole un peu de ma liberté… et me donne en même temps une part de moi-même.",
        "{-obj}{huis}Pour aller plus loin. Dans sa pièce Huis clos, en 1944, trois morts sont enfermés pour l'éternité "
        "dans un salon. Pas de bourreaux, pas de flammes : seulement les regards des autres, auxquels on n'échappe jamais. "
        "D'où la réplique célèbre : l'enfer, c'est les autres.",
        "{huis.1}Attention au contresens. Sartre l'a expliqué lui-même : il ne veut pas dire que nos relations avec les autres "
        "sont toujours infernales. Mais que, si elles sont faussées, l'autre devient un enfer, parce que nous dépendons "
        "de son jugement pour nous connaître nous-mêmes.",
        ("Le regard des autres m'apprend qui je suis. À moi de ne pas m'y laisser enfermer.", {"rate": "-5%"}),
        "{-huis}{-tab_bar}",
    ], vis={
        "tab_eco": dict(type="tableau", img="cs4-ecouteuse", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.35, .38, .5],
                        legende="Nicolaes Maes, L'Écouteuse, 1657 (Dordrechts Museum)"),
        "q_ser": dict(type="question", t="Un œil collé au trou d'une serrure…"),
        "ser": dict(type="liste", titre="La scène de la serrure (L'Être et le Néant, 1943)", items=[
            "Absorbé dans ce que je vois : je ne pense pas à moi", "Des pas dans le couloir : quelqu'un me regarde",
            "La honte : j'existe pour moi… tel qu'un autre me voit"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "sartre2": dict(type="portrait", annee=1905, img="sartre", nom="Jean-Paul Sartre", dates="1905 – 1980",
                        legende="L'Être et le Néant (1943) · Huis clos (1944)", x=110, y=120, w=330, h=420),
        "tab_ada": dict(type="tableau", img="cs4-adam", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .25],
                        legende="Masaccio, Adam et Ève chassés du Paradis, vers 1425 (chapelle Brancacci, Florence)"),
        "c_honte": dict(type="cit", a="Sartre", o="L'Être et le Néant, IIIᵉ partie, chap. I (1943)", x=640, y=170, w=570),
        "hon": dict(type="liste", titre="La structure de la honte", items=[
            "Honte de moi : c'est moi qui suis visé", "Devant autrui : seul, je ne l'éprouverais pas"],
                    marques=["1", "2"], cles=["honte"], x=170, y=190, w=940),
        "tab_bar": dict(type="tableau", img="cs4-bar", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .35],
                        legende="Édouard Manet, Un bar aux Folies Bergère, 1882 (Courtauld Gallery, Londres)"),
        "obj": dict(type="cols", g="Il me fige", gq="sous son regard, je deviens un objet",
                    d="Il me révèle", dq="sans lui, je ne saurais pas qui je suis aux yeux du monde", vs="↔"),
        "huis": dict(type="note", titre="Pour aller plus loin · Huis clos (1944)", cles=["faussées"],
                     t="« L'enfer, c'est les autres » : non que les autres soient mauvais…",
                     etape="… mais, quand nos relations sont faussées, nous dépendons de leur jugement pour nous connaître.",
                     x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ IV. Hegel
    dict(id="hegel", chap="Se reconnaître dans ses œuvres", fond="nuit", humeur="lumiere",
         notions=["l'art", "le travail", "la technique"],
         retenir="Hegel : l'homme a une double existence. Il se connaît par la pensée, et par l'action qui transforme le monde. Il veut être reconnu.",
         beats=[
        "{hegel}{tab_ron}Remontons un siècle plus tôt. Dans ses cours d'esthétique, donnés à Berlin dans les années 1820, "
        "Hegel s'arrête sur un geste d'enfant. {n_heg}{n_heg.1}Un petit garçon jette des pierres dans l'eau… {n_heg.2}puis il regarde, fasciné, "
        "les cercles qui s'élargissent à la surface.",
        "{n_heg.3}Pourquoi est-ce si fascinant ? Parce que ces cercles, c'est lui qui les a faits. Dans l'eau, il contemple "
        "quelque chose qui vient de lui : il voit son propre pouvoir, au dehors.",
        "{-n_heg}{-tab_ron}{tab_cours}Hegel en tire une thèse sur ce qui distingue l'homme des choses.",
        ("C", "Les choses de la nature n'existent qu'immédiatement et d'une seule façon, tandis que l'homme, "
              "parce qu'il est esprit, a une double existence.", "c_heg"),
        "{-hegel}{-c_heg}{dbl}{dbl.g}D'abord, l'homme se connaît par la pensée : il se contemple, se représente à lui-même. "
        "C'est la conscience de soi théorique. {dbl.d}Mais il se connaît aussi par l'action : il transforme le monde extérieur "
        "pour y imprimer sa marque, et s'y retrouver. C'est la conscience de soi pratique.",
        "{-dbl}{-tab_cours}{tab_mai}{ex_h}Le geste de l'enfant, on le retrouve partout. {ex_h.1}Dans les mains peintes "
        "sur les parois des grottes, il y a des milliers d'années. {ex_h.2}Dans la chambre qu'un adolescent décore à sa façon. "
        "{ex_h.3}Et dans l'{#l'art}art, surtout, où l'esprit se voit lui-même sous une forme sensible.",
        "{-ex_h}{-tab_mai}{tab_cas}{ms}Pour aller plus loin. Dans la Phénoménologie de l'esprit, en 1807, Hegel montre que "
        "cela ne suffit pas : la conscience de soi ne trouve sa satisfaction que dans une autre conscience de soi. "
        "Je ne veux pas seulement me voir dans les choses. Je veux être reconnu.",
        "{ms.1}D'où la célèbre lutte du maître et de l'esclave. Deux consciences s'affrontent pour être reconnues ; "
        "celle qui a peur de mourir cède, et devient l'esclave. Mais retournement : c'est l'esclave qui, en "
        "{#le travail}travaillant la matière, finit par se reconnaître dans ses œuvres. Le maître, lui, ne fait que consommer.",
        ("Celui qui fabrique apprend qui il est. Celui qui consomme reste dépendant.", {"rate": "-5%"}),
        "{-ms}{-tab_cas}",
    ], vis={
        "n_heg": dict(type="liste", titre="Les ricochets (Esthétique)", items=[
            "L'enfant jette des pierres dans l'eau",
            "Il regarde les cercles s'élargir",
            "Il y voit son œuvre : son propre pouvoir, au dehors"], marques=["1", "2", "3"], x=640, y=150, w=570),
        "hegel": dict(type="portrait", annee=1770, img="hegel", nom="G. W. F. Hegel", dates="1770 – 1831",
                      legende="Cours d'esthétique (1818-1829)", x=110, y=120, w=330, h=420),
        "tab_ron": dict(type="tableau", img="cs4-ronds", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .5, .5],
                        legende="Ronds dans l'eau (photo Roger McLassus, CC BY-SA 3.0)"),
        "tab_cours": dict(type="tableau", img="cs4-hegel-cours", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                          legende="Franz Kugler, Hegel et ses étudiants, lithographie, 1828"),
        "c_heg": dict(type="cit", a="Hegel", o="Esthétique, Introduction (1818-1829), trad. S. Jankélévitch", para=True,
                      x=640, y=170, w=570),
        "dbl": dict(type="cols", g="Par la pensée", gq="il se contemple, se représente à lui-même : conscience de soi théorique",
                    d="Par l'action", dq="il transforme le monde pour s'y retrouver : conscience de soi pratique", vs="+",
                    repere="Une double existence"),
        "tab_mai": dict(type="tableau", img="cs4-mains", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Cueva de las Manos, Patagonie, entre 7300 et 700 av. J.-C. (photo Mariano, domaine public)"),
        "ex_h": dict(type="liste", titre="Se reconnaître dans ses œuvres", items=[
            "Les mains peintes sur les parois des grottes", "La chambre qu'on décore à sa façon",
            "L'art : l'esprit qui se voit sous une forme sensible"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "tab_cas": dict(type="tableau", img="cs4-casseurs", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .5],
                        legende="Gustave Courbet, Les Casseurs de pierres, 1849 (détruit en 1945, photographie)"),
        "ms": dict(type="def", cles=["reconnu", "travail"], terme="Le maître et l'esclave · Phénoménologie de l'esprit (1807)",
                   plus=True, t="La conscience de soi veut être reconnue par une autre conscience de soi.",
                   etape="Retournement : l'esclave, par le travail, se reconnaît dans ses œuvres.", x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ V. Bergson
    dict(id="bergson", chap="Conscience signifie mémoire", fond="aube", humeur="calme",
         notions=["le temps", "la liberté", "la nature"],
         retenir="Bergson : conscience signifie mémoire et anticipation, donc choix. Quand un geste devient automatique, la conscience s'en retire.",
         beats=[
        "{bergson}{tab_sou}Dernière voix : Henri Bergson. En 1911, il donne une conférence en Angleterre, à Birmingham, "
        "sur la conscience et la vie. {n_berg}Il refuse d'abord de la définir : c'est la chose la plus concrète qui soit. "
        "Mais il en donne le trait le plus apparent.",
        "{-n_berg}",
        ("C", "Conscience signifie d'abord mémoire.", "c_berg1"),
        "{-c_berg1}{oubli}Imagine une conscience qui oublierait tout, à chaque instant. Elle mourrait et renaîtrait sans cesse : "
        "ce ne serait plus une conscience du tout. Et Bergson ajoute aussitôt une seconde idée.{-oubli}",
        ("C", "Toute conscience est donc mémoire — conservation et accumulation du passé dans le présent. "
              "Mais toute conscience est anticipation de l'avenir.", "c_berg2"),
        "{-bergson}{-c_berg2}{-tab_sou}{tab_tur}{pont}{pont.1}Retenir ce qui n'est déjà plus. {pont.2}Anticiper ce qui n'est pas encore. "
        "Quand tu écoutes cette phrase, tu te souviens de son début, et tu attends déjà sa fin : sinon, elle n'aurait aucun sens. "
        "{pont.3}La conscience est un pont jeté entre le passé et l'avenir. Une affaire de {#le temps}temps, de durée.",
        "{-pont}{-tab_tur}{tab_dan}{auto}Bergson en donne une preuve, que chacun peut vérifier. {auto.1}Quand tu apprends un geste, "
        "le vélo, un morceau de piano, tu es conscient de chaque mouvement : chacun résulte d'une décision. "
        "{auto.2}Puis le geste devient automatique… et la conscience s'en retire. Tu peux pédaler en pensant à autre chose.{-auto}",
        ("C", "Si conscience signifie mémoire et anticipation, c'est que conscience est synonyme de choix.", "c_berg3"),
        "{-c_berg3}{deg}D'où une idée vertigineuse. {deg.1}La conscience serait présente, à des degrés divers, dans tout le vivant : "
        "elle s'endort chez la plante fixée au sol, elle s'éveille chez l'animal qui se déplace et doit choisir. "
        "{deg.2}Et toi, quand es-tu le plus conscient ? Dans les moments d'hésitation, de crise, quand ton avenir dépend "
        "de ce que tu vas décider.",
        ("Plus je choisis, plus je suis conscient. La conscience a partie liée avec la liberté.", {"rate": "-5%"}),
        "{-deg}{-tab_dan}",
    ], vis={
        "n_berg": dict(type="note", titre="« La conscience et la vie » (1911)", cles=["concrète"],
                      t="Inutile de la définir : c'est la chose la plus concrète qui soit.", x=640, y=150, w=570),
        "bergson": dict(type="portrait", annee=1859, img="bergson", nom="Henri Bergson", dates="1859 – 1941",
                        legende="L'Énergie spirituelle (1919)", x=110, y=120, w=330, h=420),
        "tab_sou": dict(type="tableau", img="cs4-souvenir", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .45],
                        legende="Camille Corot, Souvenir de Mortefontaine, 1864 (musée du Louvre)"),
        "c_berg1": dict(type="cit", a="Bergson", o="« La conscience et la vie » (1911), L'Énergie spirituelle", x=640, y=220, w=570),
        "oubli": dict(type="note", titre="Une conscience sans mémoire ?", cles=["renaîtrait"],
                      t="Elle mourrait et renaîtrait à chaque instant : ce ne serait plus une conscience.",
                      x=640, y=200, w=570),
        "c_berg2": dict(type="cit", a="Bergson", o="« La conscience et la vie » (1911), L'Énergie spirituelle", x=640, y=150, w=570),
        "tab_tur": dict(type="tableau", img="cs4-turner", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .5],
                        legende="William Turner, Pluie, vapeur et vitesse, 1844, détail (National Gallery, Londres)"),
        "pont": dict(type="liste", titre="La conscience, un pont", items=[
            "Retenir ce qui n'est déjà plus : la mémoire", "Anticiper ce qui n'est pas encore : l'attente",
            "Un pont entre le passé et l'avenir : la durée"], marques=["←", "→", "="], x=170, y=170, w=940),
        "tab_dan": dict(type="tableau", img="cs4-danse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .55],
                        legende="Edgar Degas, La Classe de danse, 1874 (Metropolitan Museum of Art, New York, CC0)"),
        "auto": dict(type="liste", titre="L'apprentissage d'un geste", items=[
            "Au début : conscient de chaque mouvement, chacun est une décision",
            "Devenu automatique : la conscience s'en retire"], marques=["1", "2"], x=170, y=180, w=940),
        "c_berg3": dict(type="cit", a="Bergson", o="« La conscience et la vie » (1911), L'Énergie spirituelle", x=170, y=200, w=940),
        "deg": dict(type="liste", titre="Des degrés de conscience", items=[
            "Dans tout le vivant : endormie chez la plante, éveillée chez l'animal qui choisit",
            "Chez moi : plus vive dans l'hésitation, quand mon avenir se décide"], marques=["1", "2"],
                    x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_fen2}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Husserl. Toute conscience est conscience de quelque chose : "
        "c'est l'intentionnalité.",
        "{rec.2}Deux : Sartre. La conscience n'a pas de dedans ; elle éclate vers le monde. "
        "Et sous le regard d'autrui, j'ai honte de moi tel que je lui apparais.",
        "{rec.3}Trois : Hegel. L'homme se reconnaît dans ses œuvres, et il a besoin d'être reconnu par une autre conscience.",
        "{rec.4}Quatre : Bergson. Conscience signifie mémoire, anticipation… et choix.",
        "{-rec}{-tab_fen2}{tab_fin}{q_suite}Mais la conscience ne se contente pas de percevoir et de se souvenir. Elle juge aussi. "
        "Quelle est cette voix qui, en nous, accuse ou approuve ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : la conscience morale. Socrate, Rousseau, Kant, Arendt et Pascal.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_fen2": dict(type="tableau", img="cs4-fenetre", fond=True, sombre=True, de=[1.3, .5, .25], a=[1.0, .5, .4],
                         legende="Caspar David Friedrich, Femme à la fenêtre, 1822 (Alte Nationalgalerie, Berlin)"),
        "rec": dict(type="carte", centre="CONSCIENCE, MONDE, AUTRUI", branches=[
            dict(t="Husserl", items=["conscience de quelque chose", "l'intentionnalité", "noèse / noème"]),
            dict(t="Sartre", items=["pas de « dedans »", "la mauvaise foi", "la honte, le regard d'autrui"]),
            dict(t="Hegel", items=["une double existence", "se reconnaître dans ses œuvres", "le maître et l'esclave"]),
            dict(t="Bergson", items=["mémoire et anticipation", "conscience = choix", "l'automatisme"])]),
        "tab_fin": dict(type="tableau", img="cs4-justice", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Pierre-Paul Prud'hon, La Justice et la Vengeance divine poursuivant le Crime, 1808 (musée du Louvre)"),
        "q_suite": dict(type="question", t="Quelle est cette voix qui, en nous, accuse ou approuve ?"),
        "fin": dict(type="titre", sur="À suivre", t="La conscience morale", sous="Épisode 5 · Socrate, Rousseau, Kant, Arendt, Pascal"),
    }),
]

QUIZ = [
    dict(q="Que veut dire Husserl par « intentionnalité » ?",
         r=["La volonté de bien faire", "Le fait que toute conscience est conscience de quelque chose",
            "La capacité de prévoir l'avenir", "Le fait d'agir exprès"], ok=1,
         voir="c_hus", ex="Méditations cartésiennes, § 14 : la conscience n'est pas une boîte, elle vise toujours un objet hors d'elle (percevoir, imaginer, se souvenir…)."),
    dict(q="Qu'ajoute Husserl au « je pense » de Descartes ?",
         r=["Rien : il le répète", "Je pense… quelque chose : pas de cogito sans cogitatum",
            "Je pense, donc Dieu existe", "Je ne pense jamais vraiment"], ok=1,
         voir="cog", ex="La conscience est d'emblée ouverture au monde : on ne sépare plus un sujet enfermé en lui-même et un monde à prouver."),
    dict(q="« La conscience n'a pas de dedans. » Que veut dire Sartre ?",
         r=["Que nous n'avons pas de conscience", "Que la conscience est tout entière mouvement vers le monde",
            "Que nos sentiments sont cachés en nous", "Que la conscience est un estomac"], ok=1,
         voir="ecl", ex="Contre la « philosophie digestive » : être conscient, c'est « s'éclater vers » le monde, chose parmi les choses, homme parmi les hommes."),
    dict(q="Dans la scène de la serrure, que révèle la honte ?",
         r=["Que je suis seul au monde", "Qu'autrui est le médiateur entre moi et moi-même",
            "Que j'ai commis un crime", "Que la conscience est transparente"], ok=1,
         voir="c_honte", ex="J'ai honte de moi tel que j'apparais à autrui : son regard me révèle une part de moi que je ne voyais pas seul."),
    dict(q="« L'enfer, c'est les autres » (Huis clos) signifie…",
         r=["qu'il faut fuir les autres", "que, si nos relations sont faussées, nous dépendons du jugement des autres pour nous connaître",
            "que les autres sont méchants", "que l'enfer existe"], ok=1,
         voir="huis", ex="Sartre l'a précisé : la réplique ne condamne pas toute relation à autrui, elle décrit des relations viciées."),
    dict(q="Pourquoi l'enfant de Hegel aime-t-il jeter des pierres dans l'eau ?",
         r=["Pour mesurer la profondeur", "Parce qu'il contemple dans les cercles quelque chose qui vient de lui",
            "Pour faire peur aux poissons", "Parce qu'il s'ennuie"], ok=1,
         voir="dbl", ex="L'homme a une double existence : il se connaît par la pensée et par l'action, en imprimant sa marque au monde."),
    dict(q="Selon Bergson, que devient la conscience quand un geste devient automatique ?",
         r=["Elle augmente", "Elle s'en retire", "Elle devient inconsciente et coupable", "Elle ne change pas"], ok=1,
         voir="auto", ex="« Conscience est synonyme de choix » : on est conscient de ce qu'on décide ; l'automatisme dispense de choisir."),
    dict(q="« Conscience signifie d'abord… »",
         r=["raison", "mémoire", "liberté", "perception"], ok=1,
         voir="c_berg1", ex="Une conscience qui oublierait tout à chaque instant ne serait plus une conscience : elle est mémoire et anticipation."),
]

CREDITS = [
    "Portraits : Edmund Husserl (photographie, années 1910, domaine public) ; Jean-Paul Sartre (photographie) ; "
    "Hegel (Jakob Schlesinger, 1831) ; Henri Bergson (photographie Henri Manuel, domaine public)",
    "Tableaux et gravures : Caspar David Friedrich, Femme à la fenêtre (1822) ; Paul Cézanne, La Montagne Sainte-Victoire (années 1880) ; "
    "Piet Mondrian, L'Arbre gris (1911) ; Nils Forsberg, Descartes à la cour de la reine Christine (XIXᵉ s.) ; "
    "Robert Delaunay, Les Fenêtres simultanées sur la ville (1912) ; Gustave Caillebotte, Rue de Paris, temps de pluie (1877) ; "
    "Jean Siméon Chardin, La Tabagie (vers 1737) ; Nicolaes Maes, L'Écouteuse (1657) ; Masaccio, Adam et Ève chassés du Paradis (vers 1425) ; "
    "Édouard Manet, Un bar aux Folies Bergère (1882) ; Franz Kugler, Hegel et ses étudiants (1828) ; "
    "Gustave Courbet, Les Casseurs de pierres (1849) ; Camille Corot, Souvenir de Mortefontaine (1864) ; "
    "William Turner, Pluie, vapeur et vitesse (1844) ; Edgar Degas, La Classe de danse (1874, Met, CC0) ; "
    "Pierre-Paul Prud'hon, La Justice et la Vengeance divine poursuivant le Crime (1808) : domaine public",
    "Photographies : ronds dans l'eau (Roger McLassus, CC BY-SA 3.0) ; Cueva de las Manos, Argentine (Mariano, domaine public)",
    "Citations : Husserl, Méditations cartésiennes, § 14 (1929), trad. G. Peiffer et E. Levinas ; Sartre, « Une idée fondamentale "
    "de la phénoménologie de Husserl : l'intentionnalité » (1939, Situations I) et L'Être et le Néant (1943), citations courtes ; "
    "Hegel, Esthétique, Introduction, trad. S. Jankélévitch, citation approchée ; Bergson, « La conscience et la vie » (1911), "
    "L'Énergie spirituelle (1919), Wikisource.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
