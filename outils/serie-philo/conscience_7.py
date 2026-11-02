"""La conscience, épisode 7 : « Récap »

Récapitulatif de la série (épisodes 1 à 6), même format que devoir_7.py. Ne reprend que ce que disent les épisodes :
formules et citations déjà vérifiées dans les épisodes précédents (Descartes, Discours de la méthode, IV ;
Husserl, Méditations cartésiennes, § 14 ; Pascal, Pensées, fr. 347).
"""

CODE = "conscience-7"
NOTION = "La conscience"
NUM = 7
TITRE = "Récap"
SUIVANT = ""
PRONONCIATION = {"Husserl": "Houssèrl", "Leibniz": "Laïbnitz", "Nietzsche": "Nitche", "Hume": "Hioume",
                 "Arendt": "Arènnte", "daimôn": "daïmône", "Nagel": "Naguel", "Signorelli": "Siniorelli"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="calme", carton=False, beats=[
        "{tab_orr}{q_veil}La veille de l'épreuve. Une lampe, un cahier, et une question : que faut-il vraiment retenir "
        "de la conscience ?",
        "{-q_veil}{deb}Souviens-toi du début. {deb.1}Un masque sur le visage. {deb.2}Dix… neuf… huit… "
        "{deb.3}Et puis plus rien. Ton corps vivait, mais il n'y avait personne pour le vivre.",
        "{-deb}{six}Six épisodes ont essayé de comprendre ce qui, ce jour-là, s'était éteint puis rallumé. "
        "Une vingtaine d'auteurs, des dizaines d'exemples. Voici tout le parcours, en quelques minutes.",
        ("P", 0.3),
        "{-six}{-tab_orr}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_orr": dict(type="tableau", img="cs7-orrery", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Joseph Wright of Derby, Un philosophe faisant une conférence sur le planétaire, vers 1766 (Derby Museum)"),
        "q_veil": dict(type="question", t="Que faut-il retenir de la conscience ?"),
        "deb": dict(type="liste", titre="Épisode 1 · Le point de départ", items=[
            "Un masque sur le visage", "Dix… neuf… huit…", "Plus rien : personne pour vivre ce corps"],
                    marques=["1", "2", "3"], x=170, y=170, w=940),
        "six": dict(type="mot", t="6 épisodes", g="ce qui s'éteint, puis se rallume", y=270),
        "titre": dict(type="titre", sur="La conscience · Épisode 7", t="Récap", sous="Toute la série en un épisode"),
    }),

    # ------------------------------------------------------------------ I. le mot et les degrés
    dict(id="mot", chap="Qu'est-ce que la conscience ?", fond="aube", humeur="lumiere", notions=["le langage", "la nature"],
         retenir="Conscientia : savoir avec. Conscience psychologique / morale ; spontanée / réfléchie. Le miroir, puis le « je ». Animaux : nature ou degré ?",
         beats=[
        "{tab_eth}{def1}D'abord, le mot. Conscientia : cum scientia, savoir avec. La conscience, c'est le savoir qui accompagne "
        "tout ce que je vis. {def1.1}Mais le même mot désigne aussi la voix qui juge : « L'œil était dans la tombe et regardait Caïn. »",
        "{-def1}{deux}Retiens deux couples. {deux.g}La conscience spontanée, tournée vers le monde, comme le joueur tout entier "
        "dans son geste. {deux.d}La conscience réfléchie, qui revient sur elle-même, comme le même joueur qui revoit l'action.",
        "{-deux}{-tab_eth}{tab_mir}{moi}Puis la conscience de soi. {moi.1}Vers dix-huit mois, l'enfant se reconnaît dans le miroir. "
        "{moi.2}Un peu plus tard, il dit « je » : avant, il se sentait ; désormais, dit Kant, il se pense. "
        "Et c'est le {#le langage}langage qui scelle ce passage.",
        "{-moi}{ani}Et les animaux ? {ani.g}Pour Descartes, une différence de nature : l'animal est une machine, il ne parle pas. "
        "{ani.d}Pour Darwin, une différence de degré. Et Nagel rappelle qu'on ne saura jamais l'effet que cela fait "
        "d'être une chauve-souris.",
        "{-ani}{-tab_mir}",
    ], vis={
        "tab_eth": dict(type="tableau", img="cs1-ether", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Robert C. Hinckley, La Première Opération sous éther (Boston, 16 octobre 1846), 1882-1893"),
        "def1": dict(type="def", cles=["savoir", "juge"], terme="Conscientia · cum scientia, « savoir avec »",
                     t="Le savoir qui accompagne tout ce que je vis : la conscience psychologique.",
                     etape="Le même mot pour la voix qui juge : la conscience morale (Hugo, « La Conscience »).",
                     x=170, y=190, w=940),
        "deux": dict(type="cols", g="Spontanée", gq="tournée vers le monde : elle vit", d="Réfléchie",
                     dq="revenue sur elle-même : elle se regarde vivre", vs="≠", repere="Repère · immédiat / médiat"),
        "tab_mir": dict(type="tableau", img="cs1-miroir-ovale", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="Mary Cassatt, Mère et enfant (le miroir ovale), 1899 (Metropolitan Museum of Art, New York)"),
        "moi": dict(type="liste", titre="La conscience de soi", items=[
            "Le miroir : vers 18 mois, l'enfant se reconnaît", "Le « je » : avant, il se sentait ; désormais, il se pense (Kant)"],
                    marques=["1", "2"], x=170, y=180, w=940),
        "ani": dict(type="cols", g="Descartes", gq="l'animal-machine : une différence de nature",
                    d="Darwin", dq="une différence de degré", vs="≠", repere="Nagel : l'effet que cela fait d'être une chauve-souris"),
    }),

    # ------------------------------------------------------------------ II. le cogito
    dict(id="cogito", chap="La certitude du moi", fond="nuit", humeur="mystere", notions=["la vérité", "la raison"],
         retenir="Descartes : le doute méthodique mène au cogito, première vérité. Locke : la mémoire fait la personne. Hume : le moi, un faisceau de perceptions.",
         beats=[
        "{tab_che}{dou}Épisode deux. Descartes décide de douter de tout. {dou.1}Les sens, qui nous trompent parfois. "
        "{dou.2}Le rêve, qui imite la veille. {dou.3}Et jusqu'au malin génie, qui pourrait me tromper même dans les calculs.",
        "{-dou}{-tab_che}{desc}Mais pour être trompé, il faut être. Et le doute s'arrête sur une première {#la vérité}vérité.",
        ("C", "Cette vérité, je pense, donc je suis, était si ferme et si assurée, que toutes les plus extravagantes suppositions "
              "des sceptiques n'étaient pas capables de l'ébranler.", "c_cog"),
        "{-desc}{-c_cog}{tab_cor}{per}Je suis une chose qui pense. Et le morceau de cire le montre : l'esprit est plus facile "
        "à connaître que le corps. {per.1}Mais suis-je la même personne qu'il y a dix ans ? Locke : oui, aussi loin que ma conscience "
        "remonte par la mémoire. Le prince dans le corps du savetier. Mais Reid objecte le cas du vieux général, qui a oublié l'enfant fouetté pour des pommes. {per.2}Hume, lui, rentre en lui-même et ne trouve jamais "
        "un moi : seulement des perceptions. Le moi serait un faisceau.",
        "{-per}{-tab_cor}",
    ], vis={
        "tab_che": dict(type="tableau", img="cs2-chevalier", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Raphaël, Le Songe du chevalier, vers 1504 (National Gallery, Londres)"),
        "dou": dict(type="liste", titre="Épisode 2 · Le doute méthodique", items=[
            "Les sens nous trompent parfois", "Le rêve imite la veille", "Le malin génie, jusque dans les mathématiques"],
                    marques=["1", "2", "3"], x=170, y=170, w=940),
        "desc": dict(type="portrait", annee=1596, img="descartes", nom="René Descartes", dates="1596 – 1650",
                     legende="Discours de la méthode (1637) · Méditations (1641)", x=110, y=120, w=330, h=420),
        "c_cog": dict(type="cit", a="Descartes", o="Discours de la méthode, IVᵉ partie (1637)", x=640, y=150, w=570),
        "tab_cor": dict(type="tableau", img="cs2-cordonnier", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="David Ryckaert III, L'Atelier du cordonnier, XVIIᵉ siècle (Rijksmuseum, Amsterdam)"),
        "per": dict(type="liste", titre="Le moi qui dure ?", items=[
            "Locke : la mémoire fait la personne (le prince et le savetier)",
            "Hume : je ne trouve que des perceptions, le moi est un faisceau"], marques=["1", "2"],
                    x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ III. l'inconscient
    dict(id="opaque", chap="Une conscience opaque", fond="aube", humeur="tension", notions=["l'inconscient", "le langage"],
         retenir="Leibniz : perception / aperception. Freud : l'inconscient, hypothèse nécessaire et légitime ; ça, moi, surmoi. Nietzsche : une conscience de surface. Alain : une tâche.",
         beats=[
        "{tab_vag}{tro}Épisode trois : la conscience voit-elle tout ? {tro.1}Leibniz écoute la mer. Chaque vague, seule, "
        "je ne l'entends pas ; et pourtant il faut qu'elle m'affecte. Ce sont les petites perceptions, sans aperception.",
        "{-tab_vag}{tab_cav}{tro.2}Freud va plus loin. Un nom oublié, Signorelli, un lapsus, un rêve : pour combler ces trous, "
        "l'{#l'inconscient}inconscient est une hypothèse nécessaire et légitime. Le ça, le moi, le surmoi : le moi est un cavalier, "
        "qui doit tenir un cheval plus fort que lui. Et le rêve, déguisé pour tromper le gardien, est la voie royale vers l'inconscient.",
        "{tro.3}Nietzsche, lui, voit dans la conscience l'organe le plus tardif, développé pour communiquer. Ce qui devient conscient "
        "devient superficiel, commun : nous sommes inconnus à nous-mêmes.",
        "{-tro}{tac}Alain répond : l'homme est obscur à lui-même, mais l'inconscient ne doit pas devenir une excuse. "
        "{tac.1}Et Freud lui-même le disait : là où était le ça, le moi doit advenir. La conscience n'est pas un donné. C'est une tâche.",
        "{-tac}{-tab_cav}",
    ], vis={
        "tab_vag": dict(type="tableau", img="cs3-vague", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Gustave Courbet, La Vague, vers 1869 (domaine public)"),
        "tro": dict(type="liste", titre="Épisode 3 · Trois soupçons", items=[
            "Leibniz : les petites perceptions, sans aperception",
            "Freud : l'inconscient, hypothèse nécessaire et légitime · ça, moi, surmoi",
            "Nietzsche : une conscience tardive, faite pour communiquer"], marques=["1", "2", "3"],
                    x=170, y=140, w=940),
        "tab_cav": dict(type="tableau", img="cs3-cavalier", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Théodore Géricault, Officier de chasseurs à cheval chargeant, 1812 (musée du Louvre)"),
        "tac": dict(type="def", cles=["excuse", "tâche"], terme="Alain, et Freud lui-même",
                    t="L'homme est obscur à lui-même, mais l'inconscient ne doit pas devenir une excuse.",
                    etape="« Là où était le ça, le moi doit advenir » : la conscience est une tâche.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. monde et autrui
    dict(id="monde", chap="Ouverte au monde et aux autres", fond="nuit", humeur="lumiere", notions=["la liberté", "l'art"],
         retenir="Husserl : toute conscience est conscience de quelque chose. Sartre : pas de dedans ; la honte sous le regard d'autrui. Hegel : se reconnaître dans ses œuvres. Bergson : mémoire et choix.",
         beats=[
        "{tab_fen}{husserl}Épisode quatre : et si la conscience n'était pas une chambre fermée ?",
        ("C", "Le mot intentionnalité ne signifie rien d'autre que cette particularité foncière et générale qu'a la conscience "
              "d'être conscience de quelque chose.", "c_hus"),
        "{-husserl}{-c_hus}{arb}Un même arbre peut être perçu, imaginé, regretté, désiré : chaque fois, la conscience le vise. "
        "Elle n'est pas une boîte, c'est une flèche.",
        "{-arb}{-tab_fen}{tab_eco}{mon}{mon.1}Sartre en tire que la conscience n'a pas de dedans : elle éclate "
        "vers le monde. {mon.2}Et l'œil collé à la serrure découvre, sous le regard d'autrui, la honte : "
        "j'ai honte de moi tel que j'apparais à autrui.",
        "{mon.3}Hegel montre l'enfant qui jette des pierres dans l'eau : l'homme se reconnaît dans ses œuvres, dans l'{#l'art}art, "
        "dans le travail, et il veut être reconnu. {mon.4}Bergson, enfin : conscience signifie mémoire, anticipation, et donc choix. "
        "Quand un geste devient automatique, la conscience s'en retire.",
        "{-mon}{-tab_eco}",
    ], vis={
        "tab_fen": dict(type="tableau", img="cs4-fenetre", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Caspar David Friedrich, Femme à la fenêtre, 1822 (Alte Nationalgalerie, Berlin)"),
        "arb": dict(type="def", cles=["flèche"], terme="L'intentionnalité",
                    t="Un même arbre, perçu, imaginé, regretté, désiré : la conscience le vise.",
                    etape="Pas une boîte : une flèche tournée vers le monde.", x=170, y=200, w=940),
        "husserl": dict(type="portrait", annee=1859, img="husserl", nom="Edmund Husserl", dates="1859 – 1938",
                        legende="Méditations cartésiennes (1929)", x=110, y=120, w=330, h=420),
        "c_hus": dict(type="cit", a="Husserl", o="Méditations cartésiennes, § 14 (1929), trad. Peiffer et Levinas",
                      x=640, y=170, w=570),
        "tab_eco": dict(type="tableau", img="cs4-ecouteuse", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.3, .38, .5],
                        legende="Nicolaes Maes, L'Écouteuse, 1657 (Dordrechts Museum)"),
        "mon": dict(type="liste", titre="Épisode 4 · Conscience, monde et autrui", items=[
            "Sartre : la conscience n'a pas de dedans", "Sartre : la honte, sous le regard d'autrui",
            "Hegel : se reconnaître dans ses œuvres, être reconnu", "Bergson : mémoire, anticipation, choix"],
                    marques=["1", "2", "3", "4"], x=170, y=130, w=940),
    }),

    # ------------------------------------------------------------------ V. la conscience morale
    dict(id="morale", chap="La conscience morale", fond="aube", humeur="mystere", notions=["le devoir", "la religion"],
         retenir="Socrate : une voix qui retient. Rousseau : un instinct divin. Kant : un tribunal intérieur. Arendt : penser, c'est dialoguer avec soi. Pascal : le roseau pensant.",
         beats=[
        "{tab_ore}{mor}Épisode cinq : la voix qui juge. Raskolnikov, que personne n'accuse, sauf lui-même. "
        "{mor.1}Socrate entendait depuis l'enfance une voix qui le retenait, son daimôn ; et il voulait une vie qui s'examine. "
        "{mor.2}Rousseau y entend un instinct divin, plus sûr que la raison ; mais les morales varient, et Freud y soupçonne le surmoi.",
        "{mor.3}Kant y voit un tribunal intérieur, qui nous suit comme notre ombre, et se représente un juge idéal. "
        "{mor.4}Arendt : penser, c'est dialoguer avec soi-même ; qui ne pense pas peut tout faire, comme Eichmann.",
        "{-mor}{-tab_ore}{pascal}{tab_ros}Et Pascal donne la clé de toute la notion.",
        ("C", "L'homme n'est qu'un roseau, le plus faible de la nature ; mais c'est un roseau pensant.", "c_ros"),
        "{-c_ros}{dig}Il sait qu'il meurt, et l'univers n'en sait rien. Toute notre dignité consiste donc en la pensée. "
        "{dig.1}Travaillons donc à bien penser : voilà le principe de la morale, et du {#le devoir}devoir.",
        "{-pascal}{-dig}{-tab_ros}",
    ], vis={
        "tab_ore": dict(type="tableau", img="cs5-oreste", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .45, .4],
                        legende="William-Adolphe Bouguereau, Les Remords d'Oreste, 1862 (Chrysler Museum, Norfolk)"),
        "mor": dict(type="liste", titre="Épisode 5 · Quatre figures de la voix qui juge", items=[
            "Socrate : le daimôn qui retient, une vie qui s'examine", "Rousseau : « instinct divin » · objection : la coutume, le surmoi",
            "Kant : un tribunal intérieur", "Arendt : penser, c'est dialoguer avec soi-même"],
                    marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "pascal": dict(type="portrait", annee=1623, img="pascal", nom="Blaise Pascal", dates="1623 – 1662",
                       legende="Pensées (1670)", x=110, y=120, w=330, h=420),
        "tab_ros": dict(type="tableau", img="cs5-roseaux", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Roseaux communs au bord d'un lac (photo Joshua Mayer, CC BY-SA 2.0)"),
        "c_ros": dict(type="cit", a="Pascal", o="Pensées, fr. 347 (éd. Brunschvicg ; 1670)", x=640, y=200, w=570),
        "dig": dict(type="note", titre="La dignité selon Pascal", cles=["dignité", "morale"],
                    t="Toute notre dignité consiste en la pensée.",
                    etape="« Travaillons donc à bien penser : voilà le principe de la morale. »", x=640, y=190, w=570),
    }),

    # ------------------------------------------------------------------ VI. le jour J
    dict(id="jourj", chap="Le jour J", fond="nuit", humeur="lumiere",
         retenir="Définir, problématiser, distinguer pour dépasser. Une idée, un auteur, un exemple précis.", beats=[
        "{tab_ecr}{meth}Épisode six : le jour J. {meth.1}Définir chaque mot du sujet. {meth.2}Problématiser : une tension, "
        "pas une reformulation. {meth.3}Trois parties, dont la dernière déplace la question grâce à une distinction. "
        "{meth.4}Et pour l'explication : six éléments d'introduction, puis quoi, comment, pourquoi.",
        "{-meth}{dis}Trois distinctions qui dépassent. {dis.1}Être, comme une chose, et exister, en se faisant. "
        "{dis.2}Se connaître, et se comprendre. {dis.3}Avoir conscience, en fait, et être une personne, en droit.",
        "{-dis}{suj}Des sujets qui reviennent. {suj.1}Suis-je ce que j'ai conscience d'être ? {suj.2}Peut-on se connaître soi-même ? "
        "{suj.3}La conscience fait-elle la dignité de l'homme ? Et le texte du roseau pensant, à expliquer phrase par phrase.",
        "{-suj}{-tab_ecr}{tab_nar}{ex}Et des exemples précis : l'anesthésie, le miroir, le malin génie, le prince et le savetier, "
        "le bruit de la mer, la serrure, Raskolnikov, le roseau pensant.",
        "{-ex}{piege}Le piège : réciter Descartes contre Freud sans répondre à la question. Un auteur est un outil pour penser, "
        "pas un argument d'autorité.",
        "{-piege}{-tab_nar}",
    ], vis={
        "tab_ecr": dict(type="tableau", img="cs6-ecriture", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Albert Anker, La Leçon d'écriture, XIXᵉ siècle"),
        "meth": dict(type="liste", titre="Épisode 6 · Le jour de l'épreuve", items=[
            "Définir chaque mot du sujet", "Problématiser : une tension",
            "Trois parties : la dernière déplace la question", "Explication : six éléments, puis quoi · comment · pourquoi"],
                     marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "dis": dict(type="liste", titre="Trois distinctions qui dépassent", items=[
            "Être / exister", "Se connaître / se comprendre", "Avoir conscience (en fait) / être une personne (en droit)"],
                    marques=["1", "2", "3"], x=170, y=170, w=940),
        "suj": dict(type="liste", titre="Des sujets qui reviennent", items=[
            "Suis-je ce que j'ai conscience d'être ?", "Peut-on se connaître soi-même ?",
            "La conscience fait-elle la dignité de l'homme ?"], marques=["?", "?", "?"], x=170, y=160, w=940),
        "tab_nar": dict(type="tableau", img="cs6-narcisse", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .45, .55],
                        legende="Le Caravage, Narcisse, 1597-1599 (Galerie nationale d'art ancien, Rome)"),
        "ex": dict(type="nuage", items=["l'anesthésie", "le miroir", "le malin génie", "le prince et le savetier",
                                        "le bruit de la mer", "la serrure", "Raskolnikov", "le roseau pensant"]),
        "piege": dict(type="note", titre="Le piège", cles=["outil"],
                      t="Réciter Descartes contre Freud sans répondre à la question. Un auteur est un outil pour penser."),
    }),

    # ------------------------------------------------------------------ VII. fin
    dict(id="fin", chap="Toute la notion", fond="nuit", humeur="lumiere", beats=[
        "{rec}Voici toute la notion, sur une seule carte. {rec.1}Le mot et ses degrés : savoir avec, spontanée ou réfléchie. "
        "{rec.2}La certitude du moi : Descartes, Locke, Hume. {rec.3}Les limites : l'inconscient, et l'ouverture au monde "
        "et aux autres. {rec.4}La conscience morale, du daimôn au roseau pensant.",
        "{-rec}{frise}Et voici ceux qui t'ont accompagné, de Socrate à Hannah Arendt : vingt-cinq siècles de pensée.",
        "{-frise}{trois}Si tu ne dois garder que trois phrases : {trois.1}Descartes, je pense, donc je suis. "
        "{trois.2}Husserl, toute conscience est conscience de quelque chose. "
        "{trois.3}Et Pascal, toute notre dignité consiste en la pensée.",
        ("Un dernier mot. La conscience n'est pas seulement un sujet de dissertation. C'est ce qui s'est rallumé, ce matin, "
         "quand tu as ouvert les yeux. Tu sais maintenant l'interroger.", {"rate": "-5%"}),
        ("Demain, devant ta copie, garde-la bien éveillée. Bonne chance.", {"rate": "-6%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-trois}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LA CONSCIENCE", branches=[
            dict(t="Le mot, les degrés", items=["cum scientia : savoir avec", "spontanée / réfléchie", "le miroir, le « je »"]),
            dict(t="La certitude du moi", items=["Descartes : le cogito", "Locke : la mémoire", "Hume : un faisceau"]),
            dict(t="Les limites", items=["Leibniz, Freud, Nietzsche", "Husserl : conscience de…", "Sartre : autrui, la honte"]),
            dict(t="La conscience morale", items=["Socrate, Rousseau", "Kant : le tribunal", "Arendt, Pascal"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Socrate", d=-470, img="socrate"), dict(nom="Descartes", d=1596, img="descartes"),
            dict(nom="Pascal", d=1623, img="pascal"), dict(nom="Locke", d=1632, img="locke"),
            dict(nom="Leibniz", d=1646, img="leibniz"), dict(nom="Hume", d=1711, img="hume"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Kant", d=1724, img="kant"),
            dict(nom="Hegel", d=1770, img="hegel"), dict(nom="Nietzsche", d=1844, img="nietzsche"),
            dict(nom="Freud", d=1856, img="freud"), dict(nom="Husserl", d=1859, img="husserl"),
            dict(nom="Bergson", d=1859, img="bergson"), dict(nom="Alain", d=1868, img="alain"),
            dict(nom="Sartre", d=1905, img="sartre"), dict(nom="Arendt", d=1906, img="arendt")]),
        "trois": dict(type="liste", titre="Trois phrases à garder", items=[
            "« Je pense, donc je suis » · Descartes",
            "« Toute conscience est conscience de quelque chose » · Husserl",
            "« Toute notre dignité consiste donc en la pensée » · Pascal"], marques=["1", "2", "3"],
                      x=170, y=170, w=940),
        "tab_fin": dict(type="tableau", img="cs1-soleil", fond=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Claude Monet, Impression, soleil levant, 1872 (musée Marmottan Monet, Paris)"),
        "fin": dict(type="titre", sur="La conscience", t="Fin de la série", sous="Six épisodes et un récap · bonne épreuve !"),
    }),
]

QUIZ = [
    dict(q="Que signifie, en latin, conscientia ?",
         r=["La science des choses", "Savoir avec", "La voix de Dieu", "L'attention"], ok=1,
         voir="def1", ex="Cum scientia : le savoir qui accompagne tout ce que je vis ; le même mot désigne la conscience morale (épisode 1)."),
    dict(q="Pour Darwin, la différence entre l'esprit de l'homme et celui des animaux est…",
         r=["une différence de nature", "une différence de degré", "inexistante", "une question de langage seulement"], ok=1,
         voir="ani", ex="Descartes : l'animal-machine, une différence de nature. Darwin : une différence de degré (épisode 1)."),
    dict(q="Pourquoi le cogito résiste-t-il au malin génie ?",
         r=["Parce que le malin génie n'existe pas", "Parce que, pour être trompé, il faut être",
            "Parce que les sens ne trompent jamais", "Parce que Dieu le garantit"], ok=1,
         voir="c_cog", ex="Même si je doute de tout, je ne peux pas douter que je pense : je pense, donc je suis (épisode 2)."),
    dict(q="Que trouve Hume quand il rentre en lui-même ?",
         r=["Un moi substantiel", "Toujours une perception particulière, jamais un moi", "Dieu", "Rien du tout"], ok=1,
         voir="per", ex="Le moi n'est qu'un faisceau de perceptions ; son identité, une fiction de l'imagination (épisode 2)."),
    dict(q="Le bruit de la mer, chez Leibniz, prouve…",
         r=["que la mer pense", "qu'il y a en nous des petites perceptions sans aperception",
            "que l'inconscient est refoulé", "que les sens nous trompent"], ok=1,
         voir="tro", ex="Chaque vague m'affecte un peu sans que je la remarque : perception ≠ aperception (épisode 3)."),
    dict(q="« Toute conscience est conscience de quelque chose » : qui le dit, et comment s'appelle cette idée ?",
         r=["Descartes : le cogito", "Husserl : l'intentionnalité", "Freud : la topique", "Bergson : la durée"], ok=1,
         voir="c_hus", ex="La conscience n'est pas une boîte fermée : elle vise toujours un objet hors d'elle (épisode 4)."),
    dict(q="Pour Kant, la conscience morale est…",
         r=["un instinct divin", "un tribunal intérieur", "la voix des parents", "une illusion"], ok=1,
         voir="mor", ex="Doctrine de la vertu, § 13 : un tribunal où nos pensées s'accusent ou se justifient ; il nous suit comme notre ombre (épisode 5)."),
    dict(q="Dans « Suis-je ce que j'ai conscience d'être ? », quelle distinction dépasse le problème ?",
         r=["Légal / légitime", "Être (comme une chose) / exister (se faire)", "Prix / dignité", "Corps / esprit"], ok=1,
         voir="dis", ex="Je ne suis jamais tout à fait ce que j'ai conscience d'être, parce que je suis toujours en train de le devenir (épisode 6)."),
]

CREDITS = [
    "Portraits : voir les épisodes 1 à 6",
    "Tableaux : Joseph Wright of Derby, Un philosophe faisant une conférence sur le planétaire (vers 1766) ; "
    "Robert C. Hinckley, La Première Opération sous éther (1882-1893) ; Mary Cassatt, Mère et enfant (le miroir ovale) (1899) ; "
    "Raphaël, Le Songe du chevalier (vers 1504) ; David Ryckaert III, L'Atelier du cordonnier (XVIIᵉ s.) ; "
    "Gustave Courbet, La Vague (vers 1869) ; Théodore Géricault, Officier de chasseurs à cheval chargeant (1812) ; "
    "Caspar David Friedrich, Femme à la fenêtre (1822) ; Nicolaes Maes, L'Écouteuse (1657) ; "
    "William-Adolphe Bouguereau, Les Remords d'Oreste (1862) ; Albert Anker, La Leçon d'écriture (XIXᵉ s.) ; "
    "Le Caravage, Narcisse (1597-1599) ; Claude Monet, Impression, soleil levant (1872) : domaine public",
    "Photographie : roseaux (Joshua Mayer, CC BY-SA 2.0)",
    "Citations : Descartes, Discours de la méthode, IVᵉ partie (1637) ; Husserl, Méditations cartésiennes, § 14 (1929), "
    "trad. G. Peiffer et E. Levinas ; Pascal, Pensées, éd. Brunschvicg, fr. 347",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
