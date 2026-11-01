"""La liberté, épisode 2 : « Le libre arbitre » (Descartes, Sartre).

Même format que liberte_1.py (voir l'en-tête de ce fichier) : beats lus, repères {id} / {-id} / {id.k} / {!mot},
citations ("C", texte, id), visuels par scène.
Citations de Descartes vérifiées sur la Méditation quatrième (trad. du duc de Luynes, 1647, Wikisource) ;
citations de Sartre : L'existentialisme est un humanisme (1946) et L'Être et le néant (1943).
"""

CODE = "liberte-2"
NOTION = "La liberté"
NUM = 2
TITRE = "Le libre arbitre"
SUIVANT = "Épisode 3 · Et si c'était une illusion ? Spinoza, Freud"

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_par}Paris, au début des années quarante. La France est occupée. "
        "Un jeune homme frappe à la porte de son ancien professeur de philosophie. Ce professeur s'appelle Jean-Paul Sartre.",
        "{-tab_par}{tab_gau}Le jeune homme est déchiré. Son frère aîné a été tué en 1940. Il voudrait partir pour l'Angleterre, "
        "rejoindre les Forces françaises libres, et venger son frère.",
        "Mais sa mère vit seule avec lui. Elle a déjà perdu un fils ; {dil}{dil.1}s'il part, elle sombrera. "
        "{dil.2}S'il reste, il ne se battra pas.",
        ("Alors, que doit-il faire ?", {"rate": "-6%", "pitch": "+1Hz"}),
        "{-dil}{-tab_gau}{tab_her}Depuis l'Antiquité, les peintres ont représenté ce moment : le héros à la croisée des chemins. "
        "Hercule, entre le Vice qui lui promet le plaisir… et la Vertu qui lui montre la route escarpée.",
        "{q1}Mais au fond, quand nous hésitons ainsi, une question plus vertigineuse se cache derrière. "
        "Ce choix… est-ce vraiment moi qui le fais ?",
        "{-q1}Nous en avons parlé la dernière fois : c'est la question du libre arbitre. "
        "Aujourd'hui, deux philosophes vont répondre oui. Un oui total, sans réserve.",
        ("P", 0.3),
        "{-tab_her}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_par": dict(type="tableau", img="t2-paris40", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Paris sous l'Occupation (Bundesarchiv, photo Friedrich, CC BY-SA 3.0 DE)"),
        "tab_gau": dict(type="tableau", img="t2-degaulle", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .55, .35],
                        legende="Le général de Gaulle au micro de la BBC, Londres (photo Keystone, domaine public)"),
        "dil": dict(type="cols", g="Partir", gq="rejoindre la France libre, venger son frère", d="Rester",
                    dq="ne pas abandonner sa mère", vs="?"),
        "tab_her": dict(type="tableau", img="t2-hercule", de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Annibale Carracci, Hercule à la croisée des chemins, 1596"),
        "q1": dict(type="question", t="Ce choix… est-ce vraiment moi qui le fais ?"),
        "titre": dict(type="titre", sur="La liberté · Épisode 2", t="Le libre arbitre",
                      sous="Descartes, Sartre : la liberté absolue de la volonté"),
    }),

    # ------------------------------------------------------------------ I. le libre arbitre
    dict(id="defi", chap="Qu'est-ce que le libre arbitre ?", fond="aube", humeur="lumiere", notions=["la justice"],
         retenir="Libre arbitre : le pouvoir de se déterminer soi-même ; j'aurais pu vouloir autrement.", beats=[
        "{tab_che}{mot}Commençons par le mot. Arbitre vient du latin arbitrium : le jugement, la décision. "
        "Le libre arbitre, c'est le pouvoir de décider par soi-même.",
        "{-mot}{def1}Plus précisément : le pouvoir de se déterminer soi-même, sans y être forcé par aucune cause extérieure. "
        "{def1.1}Celui qui choisit est la vraie cause de son choix.",
        "{-def1}{trois}Pour qu'il y ait libre arbitre, il faut donc trois choses. "
        "{trois.1}Plusieurs possibles devant moi. {trois.2}Que ce soit moi qui tranche. "
        "{trois.3}Et que j'aie pu, réellement, vouloir autre chose.",
        ("C'est ce qu'on appelle parfois le pouvoir des contraires.", {"rate": "-4%"}),
        "{-trois}{ex}Prends un exemple tout simple. {ex.g}Ce soir, tu peux réviser ta philo… {ex.d}ou lancer une série. "
        "Si tu révises, tu as le sentiment très net que tu aurais pu faire l'inverse. "
        "C'est cette expérience-là, banale et pourtant mystérieuse, que le libre arbitre prend au sérieux.",
        "{-ex}{-tab_che}{rep}Tu reconnais le repère de l'épisode un : nécessaire et contingent. "
        "Si mon choix était nécessaire, s'il ne pouvait pas être autrement, il n'y aurait pas de libre arbitre. "
        "Le libre arbitre suppose du contingent.",
        "{-rep}{enjeu}Et l'enjeu est immense. {enjeu.1}Si je ne suis pas l'auteur de mes choix, de quoi suis-je responsable ? "
        "{enjeu.2}Peut-on féliciter, ou {#la justice}punir, quelqu'un qui ne pouvait pas faire autrement ?",
        ("Sans libre arbitre, la morale et le droit vacillent.", {"rate": "-6%", "pitch": "-2Hz"}),
        ("P", 0.6),
    ], vis={
        "tab_che": dict(type="tableau", img="t2-chemins", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .5, .5],
                        legende="Un chemin qui se divise (photo Alec MacKinnon, CC BY-SA 2.0)"),
        "mot": dict(type="mot", t="arbitrium", g="latin : le jugement, la décision", y=250, taille=100),
        "def1": dict(type="def", cles=["déterminer", "cause"], terme="Le libre arbitre",
                     t="Le pouvoir de se déterminer soi-même, sans y être forcé par aucune cause extérieure.",
                     etape="Celui qui choisit est la vraie cause de son choix.", x=170, y=190, w=940),
        "trois": dict(type="liste", titre="Trois conditions", items=[
            "Plusieurs possibles devant moi", "C'est moi qui tranche", "J'aurais pu vouloir autre chose"],
                      x=170, y=170, w=940),
        "ex": dict(type="cols", g="Réviser", gq="ce soir, je travaille ma philo", d="Lancer une série",
                   dq="j'aurais pu faire l'inverse… vraiment ?", vs="ou"),
        "rep": dict(type="cols", g="Nécessaire", gq="ne peut pas être autrement : pas de libre arbitre",
                    d="Contingent", dq="aurait pu être autrement : condition du libre arbitre", vs="≠",
                    repere="Repère · nécessaire / contingent"),
        "enjeu": dict(type="liste", titre="L'enjeu", items=[
            "La responsabilité : de quoi suis-je l'auteur ?", "Le mérite et la faute : féliciter, punir"],
                      marques=["?", "?"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ II. Descartes : une volonté infinie
    dict(id="descartes", chap="Descartes : une volonté infinie", fond="nuit", humeur="lumiere", notions=["la raison"],
         retenir="Descartes : volonté infinie, entendement fini. L'erreur vient de ce que je juge sans savoir.", beats=[
        "{desc}{tab_rem}Premier défenseur : René Descartes. Nous sommes en 1641. Dans les Méditations métaphysiques, "
        "il décide de tout mettre en doute, pour trouver enfin quelque chose de certain.",
        "Ce projet, il le porte depuis longtemps. Une nuit de novembre 1619, soldat en Allemagne, enfermé tout le jour "
        "dans une chambre chauffée par un poêle, il a conçu l'idée de reconstruire tout le savoir sur des bases sûres.",
        "Et au cœur de la quatrième méditation, il fait une découverte étonnante. Toutes ses facultés sont limitées : "
        "sa mémoire, son imagination, sa connaissance. Toutes… sauf une.",
        ("C", "Il n'y a que la volonté seule ou la seule liberté du franc arbitre que j'expérimente en moi être si grande, "
              "que je ne conçois point l'idée d'aucune autre plus ample et plus étendue.", "c_vol"),
        "{-desc}{-c_vol}{-tab_rem}{tab_med}{inf}Voilà la thèse. {inf.g}Mon entendement, ma capacité de comprendre, est fini : "
        "je ne sais pas tout. {inf.d}Mais ma volonté est infinie. Je peux vouloir, ou refuser, n'importe quoi.",
        "Elle est si grande, dit Descartes, que c'est par elle que je ressemble à Dieu. "
        "{!infinie}Infinie, au sens strict : on ne peut pas être un peu libre. On l'est, ou on ne l'est pas.",
        "{-inf}{err}Mais alors, une question surgit. Si ma volonté est si parfaite… pourquoi est-ce que je me trompe ?",
        "{-err}",
        ("C", "D'où est-ce donc que naissent mes erreurs ? c'est à savoir de cela seul que la volonté étant beaucoup "
              "plus ample et plus étendue que l'entendement, je ne la contiens pas dans les mêmes limites.", "c_err"),
        "{-err}{-c_err}{schema}La réponse est lumineuse. {schema.1}Je comprends peu de choses. "
        "{schema.2}Mais je juge de tout. {schema.3}L'erreur naît dans cet écart : quand je décide sur ce que je n'ai pas compris.",
        "{-schema}{-tab_med}{tab_pen}Regarde ce que cela implique. {#la vérité}Mes erreurs ne viennent ni de Dieu, ni du monde, ni d'un mauvais sort. "
        "Elles viennent de moi : de l'usage que je fais de ma liberté.",
        ("Je ne suis jamais forcé de juger trop vite. Je suis donc {!responsable}responsable de mes erreurs.", {"rate": "-5%"}),
        "{remede}Et le remède est simple : {remede.1}suspendre son jugement, tant qu'on ne voit pas clairement. "
        "{-tab_pen}C'est toute la méthode de Descartes.",
        "{copie}Retiens-le pour tes copies : dès qu'un sujet lie la liberté à la vérité, ou à la responsabilité, "
        "Descartes est ton allié.",
        ("P", 0.6),
    ], vis={
        "desc": dict(type="portrait", annee=1596, legende="Méditations métaphysiques (1641)", img="descartes",
                     nom="René Descartes", dates="1596 – 1650", x=110, y=120, w=330, h=420),
        "tab_rem": dict(type="tableau", img="t2-rembrandt", fond=True, de=[1.0, .5, .5], a=[1.3, .4, .5],
                        legende="Rembrandt, Philosophe en méditation, 1632 (musée du Louvre)"),
        "c_vol": dict(type="cit", a="Descartes", o="Méditations métaphysiques, IV (1641 ; trad. 1647)", x=640, y=150, w=570),
        "tab_med": dict(type="tableau", img="t2-meditations", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.25, .5, .3],
                        legende="Descartes, Meditationes de prima philosophia, page de titre, Paris, 1641"),
        "inf": dict(type="cols", g="Entendement", gq="fini : je ne comprends pas tout", d="Volonté",
                    dq="infinie : je peux tout vouloir ou refuser", vs="≠"),
        "err": dict(type="question", t="Si ma volonté est parfaite… pourquoi est-ce que je me trompe ?"),
        "c_err": dict(type="cit", a="Descartes", o="Méditations métaphysiques, IV (1641 ; trad. 1647)", x=170, y=170, w=940),
        "schema": dict(type="liste", cles=["comprends", "juge", "écart"], titre="D'où vient l'erreur", items=[
            "Entendement : je comprends peu de choses", "Volonté : je juge de tout",
            "L'erreur : décider sur ce que je n'ai pas compris"], marques=["1", "2", "→"], x=170, y=170, w=940),
        "tab_pen": dict(type="tableau", img="t-penseur", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Auguste Rodin, Le Penseur, détail de La Porte de l'Enfer, musée Rodin (photo Jebulon, CC0)"),
        "remede": dict(type="def", cles=["suspendre", "clairement"], terme="Le remède",
                       t="Ne juger que de ce que je vois clairement : sinon, suspendre mon jugement.",
                       etape="Je suis responsable de mes erreurs : je n'étais pas forcé de juger.", x=170, y=200, w=940),
        "copie": dict(type="tag", style="copie", t="Copie · liberté et vérité, liberté et responsabilité : Descartes",
                      x=240, y=560, w=800),
    }),

    # ------------------------------------------------------------------ III. indifférence et liberté éclairée
    dict(id="indifference", chap="Le plus bas degré de la liberté", fond="aube", humeur="calme", notions=["la raison", "la vérité"],
         retenir="L'indifférence est le plus bas degré de la liberté ; la vraie liberté est éclairée.", beats=[
        "{q2}Tu pourrais penser que la liberté la plus pure, c'est de choisir sans aucune raison. "
        "Pile ou face. Ni ceci ni cela ne m'attire : je tranche, comme ça.",
        "{-q2}{desc2}Descartes dit exactement le contraire. Cette indifférence, c'est le degré le plus faible de la liberté.",
        ("C", "Cette indifférence que je sens lorsque je ne suis point emporté vers un côté plutôt que vers un autre "
              "par le poids d'aucune raison, est le plus bas degré de la liberté.", "c_ind"),
        "{-c_ind}{-desc2}{tab_bur}{buri}Les philosophes du Moyen Âge en avaient fait une fable célèbre : l'âne de Buridan. "
        "Un âne, affamé et assoiffé, se tient à égale distance d'un seau d'eau et d'un tas d'avoine.",
        ("Rien ne le pousse plus d'un côté que de l'autre… et il meurt sur place, faute de pouvoir choisir.",
         {"rate": "-5%", "pitch": "-1Hz"}),
        "{-buri}{-tab_bur}{ecl}Pour Descartes, l'indifférence ne montre pas la force de ma volonté, mais {!ignorance}l'ignorance "
        "de mon esprit. Si je voyais clairement le vrai et le bien, je n'hésiterais jamais.",
        "{-ecl}",
        ("C", "Si je connaissais toujours clairement ce qui est vrai et ce qui est bon, je ne serais jamais en peine de délibérer "
              "quel jugement et quel choix je devrais faire ; et ainsi je serais entièrement libre, sans jamais être indifférent.",
         "c_ecl"),
        "{-c_ecl}{-ecl}{deux}Retiens donc deux libertés. {deux.g}La liberté d'indifférence : choisir sans raison. "
        "{deux.d}Et la liberté éclairée : choisir en connaissance de cause. Plus je comprends, plus je suis libre.",
        ("Paradoxe magnifique : la liberté grandit… quand l'hésitation disparaît.", {"rate": "-5%"}),
        "{-deux}{-ecl}{mes}Pourtant, Descartes garde une carte dans sa manche. {mes.1}Dans une lettre de 1645, au père Mesland, il précise : "
        "même devant une évidence, je garde le pouvoir de m'en détourner, ne serait-ce que pour prouver ma liberté.",
        "{mes.2}La volonté n'est donc jamais enchaînée, pas même par le vrai. C'est en cela qu'elle est absolue.",
        ("P", 0.6),
    ], vis={
        "q2": dict(type="question", t="Choisir sans raison, est-ce la liberté la plus pure ?"),
        "desc2": dict(type="portrait", annee=1596, legende="Méditations métaphysiques, IV", img="descartes",
                      nom="René Descartes", dates="1596 – 1650", x=110, y=120, w=330, h=420),
        "c_ind": dict(type="cit", a="Descartes", o="Méditations métaphysiques, IV (1641 ; trad. 1647)", x=640, y=150, w=570),
        "tab_bur": dict(type="tableau", img="t2-buridan", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .55],
                        legende="William Allen Rogers, l'âne de Buridan dans une caricature politique, v. 1902"),
        "buri": dict(type="mot", t="L'âne de Buridan", g="entre l'eau et l'avoine, il meurt de ne pas choisir",
                     y=230, taille=84, plus=True),
        "ecl": dict(type="def", cles=["ignorance", "clairement"], terme="Ce que montre l'indifférence",
                    t="Non la force de ma volonté, mais l'ignorance de mon esprit.", x=170, y=110, w=940),
        "c_ecl": dict(type="cit", a="Descartes", o="Méditations métaphysiques, IV (1641 ; trad. 1647)", x=170, y=290, w=940),
        "deux": dict(type="cols", g="Liberté d'indifférence", gq="choisir sans raison : le plus bas degré",
                     d="Liberté éclairée", dq="choisir en connaissance de cause", vs="<"),
        "mes": dict(type="note", cles=["évidence", "prouver", "enchaînée"], titre="Pour aller plus loin",
                    t="Lettre au père Mesland (9 février 1645) : même devant une évidence, je peux m'en détourner, pour prouver ma liberté.",
                    etape="La volonté n'est enchaînée par rien, pas même par le vrai.", x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ IV. Sartre : l'existence précède l'essence
    dict(id="sartre", chap="Sartre : condamné à être libre", fond="nuit", humeur="tension", notions=["la conscience"],
         retenir="Sartre : l'existence précède l'essence. L'homme n'est rien d'autre que ce qu'il se fait.", beats=[
        "{tab_flo}{sartre}Trois siècles plus tard, un autre Français pousse cette idée jusqu'au bout. "
        "Jean-Paul Sartre écrit au café de Flore, à Paris. En 1945, il donne une conférence qui fait salle comble : "
        "L'existentialisme est un humanisme.",
        "{-sartre}{-tab_flo}{coupe}Pour comprendre sa thèse, prends un {#la technique}objet fabriqué. Un coupe-papier. "
        "{coupe.1}Avant de le fabriquer, l'artisan en a l'idée : à quoi il sert, comment il est fait. Son essence.",
        "{coupe.2}Puis il le fabrique : le coupe-papier existe. {coupe.3}Pour lui, l'essence précède l'existence.",
        ("Et pour l'homme ? Sartre retourne la formule.", {"pitch": "+2Hz"}),
        "{-coupe}{tab_voy}{formule}Pour l'homme, {!existence}l'existence précède l'essence. "
        "Il n'y a pas de modèle de l'homme qui l'attendrait d'avance : ni Dieu pour le concevoir, ni nature humaine fixée.",
        "{-formule}",
        ("C", "Cela signifie que l'homme existe d'abord, se rencontre, surgit dans le monde, et qu'il se définit après.", "c_exi"),
        "{-c_exi}Tu n'es pas courageux ou lâche par nature. Tu le deviens, par tes actes.",
        "{-formule}",
        ("C", "L'homme n'est rien d'autre que ce qu'il se fait.", "c_fait"),
        "{-formule}{-c_fait}{-tab_voy}{sartre2}Mais cette liberté a un prix. Je ne peux pas ne pas choisir. "
        "Même ne pas choisir, c'est encore choisir.",
        ("C", "L'homme est condamné à être libre. Condamné, parce qu'il ne s'est pas créé lui-même, et par ailleurs "
              "cependant libre, parce qu'une fois jeté dans le monde, il est responsable de tout ce qu'il fait.", "c_cond"),
        "{-sartre2}{-c_cond}{comp}Compare avec Descartes. {comp.g}Pour Descartes, la liberté est une propriété de ma volonté, "
        "reçue de Dieu. {comp.d}Pour Sartre, {#la religion}sans Dieu, la liberté n'est pas quelque chose que j'ai : c'est ce que je suis.",
        "{-comp}{nob}Sartre a d'ailleurs pris sa philosophie au mot. En 1964, on lui décerne le prix Nobel de littérature. "
        "Il le refuse : un écrivain, explique-t-il, ne doit pas se laisser transformer en institution. "
        "Refuser, c'est encore choisir. Et il en assume les conséquences.",
        ("P", 0.6),
    ], vis={
        "tab_flo": dict(type="tableau", img="t2-flore", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                        legende="Le café de Flore, boulevard Saint-Germain, Paris (domaine public)"),
        "sartre": dict(type="portrait", annee=1905, legende="L'existentialisme est un humanisme (1946)", img="sartre",
                       nom="Jean-Paul Sartre", dates="1905 – 1980", x=110, y=120, w=330, h=420),
        "coupe": dict(type="liste", titre="L'objet fabriqué : le coupe-papier", items=[
            "L'artisan en a d'abord l'idée : son essence", "Puis il le fabrique : il existe",
            "Pour l'objet, l'essence précède l'existence"], marques=["1", "2", "→"], x=170, y=170, w=940),
        "tab_voy": dict(type="tableau", img="t2-voyageur", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, v. 1818"),
        "formule": dict(type="mot", t="L'existence précède l'essence", g="Sartre, L'existentialisme est un humanisme",
                        y=90, taille=60),
        "c_exi": dict(type="cit", a="Sartre", o="L'existentialisme est un humanisme (1946)", x=170, y=260, w=940),
        "c_fait": dict(type="cit", a="Sartre", o="L'existentialisme est un humanisme (1946)", x=170, y=260, w=940),
        "sartre2": dict(type="portrait", annee=1905, legende="L'existentialisme est un humanisme", img="sartre",
                        nom="Jean-Paul Sartre", dates="1905 – 1980", x=110, y=120, w=330, h=420),
        "c_cond": dict(type="cit", a="Sartre", o="L'existentialisme est un humanisme (1946)", x=640, y=130, w=570),
        "nob": dict(type="mot", t="1964 : le Nobel refusé", g="refuser, c'est encore choisir", y=250, taille=80),
        "comp": dict(type="cols", g="Descartes", gq="la liberté : une propriété de ma volonté, reçue de Dieu",
                     d="Sartre", dq="sans Dieu : la liberté n'est pas ce que j'ai, c'est ce que je suis", vs="↔"),
    }),

    # ------------------------------------------------------------------ V. angoisse et mauvaise foi
    dict(id="angoisse", chap="L'angoisse et la mauvaise foi", fond="aube", humeur="tension", notions=["la conscience"],
         retenir="Angoisse : le vertige de ma liberté. Mauvaise foi : me mentir pour la fuir.", beats=[
        "{tab_cri}{ang}Une liberté pareille donne le vertige. Sartre lui donne un nom : {!angoisse}l'angoisse. "
        "Pas la peur d'un danger extérieur, mais le vertige devant ma propre liberté.",
        "{ang.1}Car en choisissant, je ne choisis pas seulement pour moi. Pour Sartre, chacun de mes choix dit "
        "ce que l'homme doit être : je réponds de l'humanité tout entière.",
        "{-ang}{-tab_cri}{tab_har}{mf}Alors, pour échapper à ce vertige, nous trichons. Sartre appelle cela {!mauvaise foi}la mauvaise foi : "
        "se mentir à soi-même pour fuir sa liberté.",
        "{-mf}{-tab_har}{tab_mas}Son exemple le plus célèbre est un garçon de café. Il a le geste un peu trop vif, un peu trop précis. "
        "Il se penche avec trop d'empressement. Il en fait trop.",
        ("C", "Il joue à être garçon de café.", "c_gar"),
        "{-c_gar}{excuses}Il se fait chose, comme si sa fonction était sa nature. Et nous faisons tous pareil, "
        "avec nos excuses favorites : {excuses.1}« c'est mon caractère », {excuses.2}« je n'avais pas le choix », "
        "{excuses.3}« c'est comme ça ».",
        ("Pour Sartre, ce sont des mensonges. On a toujours le choix.", {"rate": "-5%", "pitch": "-1Hz"}),
        "Dire « je suis nul en maths », comme on dirait « j'ai les yeux bleus », c'est déjà de la mauvaise foi : "
        "c'est transformer en destin ce qui n'est qu'une série de choix.",
        "{-excuses}{-tab_mas}{tab_che2}Et notre jeune homme, alors ? Sartre ne lui donne aucune règle, aucune morale toute faite. "
        "Aucune ne pourrait trancher à sa place. Il lui répond simplement :",
        ("C", "Vous êtes libre, choisissez, c'est-à-dire inventez.", "c_inv"),
        "{-c_inv}{sit}Attention à un contresens fréquent. {sit.1}Sartre ne dit pas que je peux tout faire. "
        "Je suis toujours en situation : un corps, une époque, un passé.",
        "{sit.2}Mais c'est moi qui donne un sens à ma situation. Un rocher n'est un obstacle que pour celui qui veut l'escalader. "
        "{-tab_che2}Pour le promeneur qui contemple le paysage, c'est un point de vue.",
        ("P", 0.6),
    ], vis={
        "tab_cri": dict(type="tableau", img="t2-cri", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .4],
                        legende="Edvard Munch, Le Cri, 1893 (Galerie nationale d'Oslo)"),
        "ang": dict(type="def", cles=["vertige", "humanité"], terme="L'angoisse",
                    t="Le vertige devant ma propre liberté.",
                    etape="En me choisissant, je dis ce que l'homme doit être : je réponds de tous.", x=170, y=200, w=940),
        "tab_har": dict(type="tableau", img="t2-harcourt", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Henri Evenepoel, Au café d'Harcourt, 1897"),
        "mf": dict(type="mot", t="La mauvaise foi", g="se mentir à soi-même pour fuir sa liberté", y=250, taille=92),
        "tab_mas": dict(type="tableau", img="t2-masques", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Masques de la comédie et de la tragédie, Princess Theatre, Decatur (photo M. Kaufman, CC BY-SA 4.0)"),
        "c_gar": dict(type="cit", a="Sartre", o="L'Être et le néant, I, chap. 2 (1943)", x=170, y=230, w=940),
        "excuses": dict(type="liste", titre="Les excuses de la mauvaise foi", items=[
            "« C'est mon caractère »", "« Je n'avais pas le choix »", "« C'est comme ça »"],
                        marques=["✗", "✗", "✗"], x=170, y=170, w=940),
        "tab_che2": dict(type="tableau", img="t2-hercule", fond=True, sombre=True, de=[1.3, .5, .4], a=[1.0, .5, .5],
                         legende="Annibale Carracci, Hercule à la croisée des chemins, 1596"),
        "c_inv": dict(type="cit", a="Sartre", o="L'existentialisme est un humanisme (1946)", x=170, y=200, w=940),
        "sit": dict(type="liste", cles=["situation", "sens", "obstacle"], titre="La liberté en situation", items=[
            "Je suis toujours en situation : un corps, une époque, un passé",
            "Mais c'est moi qui lui donne un sens : le rocher est obstacle ou point de vue"],
                    x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ VI. les objections, à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Faisons le point. {rec.1}Le libre arbitre, c'est le pouvoir de se déterminer soi-même : j'aurais pu vouloir autrement.",
        "{rec.2}Pour Descartes, la volonté est infinie ; l'erreur vient de ce que je juge au-delà de ce que je comprends. "
        "Et l'indifférence n'est que le plus bas degré de la liberté.",
        "{rec.3}Pour Sartre, l'existence précède l'essence : je suis ce que je fais, condamné à être libre.",
        "{rec.4}Et deux attitudes face à cette liberté : l'angoisse, et la mauvaise foi.",
        "Dans une copie, Descartes t'aidera à penser la liberté comme expérience et comme responsabilité ; "
        "Sartre, comme condition humaine. Mais ne les cite jamais sans leur opposer les objections.",
        "{-rec}{obj}Mais une objection gronde déjà. {obj.1}Et si ce sentiment d'être libre n'était qu'une illusion ? "
        "{tab_eth}{obj.2}Spinoza, on l'a vu, compare l'homme à une pierre lancée qui se croirait libre. "
        "{obj.3}Et Freud ira plus loin : je ne suis même pas maître de ce qui se passe en moi.",
        "{-obj}{-tab_eth}{quiz}Avant cela, à toi de jouer : les questions t'attendent sous la vidéo.",
        ("Et la prochaine fois… nous mettrons la liberté en procès.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-quiz}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE LIBRE ARBITRE", branches=[
            dict(t="Définition", items=["se déterminer soi-même", "j'aurais pu vouloir autrement", "suppose du contingent"]),
            dict(t="Descartes", items=["volonté infinie, entendement fini", "l'erreur : juger sans comprendre",
                                       "l'indifférence, plus bas degré"]),
            dict(t="Sartre", items=["l'existence précède l'essence", "condamné à être libre", "je suis ce que je fais"]),
            dict(t="Face à la liberté", items=["l'angoisse", "la mauvaise foi", "la liberté en situation"])]),
        "obj": dict(type="liste", titre="L'objection : épisode 3", items=[
            "Et si le sentiment d'être libre était une illusion ?",
            "Spinoza : la pierre qui se croirait libre",
            "Freud : je ne suis pas maître en moi-même"], marques=["?", "→", "→"], x=170, y=150, w=940),
        "tab_eth": dict(type="tableau", img="t-ethica", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .45],
                        legende="Spinoza, Ethica, dans les Opera posthuma, 1677"),
        "quiz": dict(type="mot", t="À toi de jouer", g="les questions t'attendent sous la vidéo", y=260, taille=84),
        "tab_fin": dict(type="tableau", img="t2-voyageur", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, v. 1818"),
        "fin": dict(type="titre", sur="À suivre", t="Et si c'était une illusion ?", sous="Épisode 3 · Spinoza, Freud, les sciences humaines"),
    }),
]

QUIZ = [
    dict(q="Qu'est-ce que le libre arbitre ?",
         r=["L'absence d'obstacles extérieurs", "Le pouvoir de se déterminer soi-même, en ayant pu vouloir autrement",
            "L'obéissance à la loi qu'on s'est prescrite", "Les droits que la société garantit"], ok=1,
         voir="def1", ex="C'est la liberté de vouloir : celui qui choisit est la vraie cause de son choix. Il suppose du contingent."),
    dict(q="Pour Descartes, d'où viennent nos erreurs ?",
         r=["D'une volonté trop faible", "De Dieu, qui nous trompe", "De ce que la volonté, plus étendue que l'entendement, juge de ce qu'il n'a pas compris",
            "Des sens, toujours trompeurs"], ok=2,
         voir="c_err", ex="Méditation IV : volonté infinie, entendement fini. Je me trompe quand je juge au-delà de ce que je comprends : j'en suis responsable."),
    dict(q="Selon Descartes, la liberté d'indifférence est…",
         r=["la forme la plus haute de la liberté", "le plus bas degré de la liberté", "une illusion", "la liberté politique"], ok=1,
         voir="c_ind", ex="Choisir sans raison montre un défaut de connaissance. La vraie liberté est éclairée : plus je comprends, plus je suis libre."),
    dict(q="Que signifie « l'existence précède l'essence » ?",
         r=["Que l'homme a une nature fixée d'avance", "Que l'homme existe d'abord et se définit ensuite par ses actes",
            "Que les objets existent avant d'être pensés", "Que Dieu a créé l'homme libre"], ok=1,
         voir="formule", ex="Contrairement au coupe-papier, l'homme n'a pas de modèle préalable : il n'est rien d'autre que ce qu'il se fait."),
    dict(q="Le garçon de café de Sartre illustre…",
         r=["l'angoisse", "la mauvaise foi", "la liberté éclairée", "le libre arbitre selon Descartes"], ok=1,
         voir="c_gar", ex="Il « joue à être garçon de café » : il se fait chose, comme si sa fonction était sa nature, pour fuir sa liberté."),
    dict(q="« Je n'avais pas le choix. » Pour Sartre, cette phrase est le plus souvent…",
         r=["une vérité", "une marque de mauvaise foi", "une preuve d'angoisse", "un argument de Descartes"], ok=1,
         voir="excuses", ex="On est « condamné à être libre » : même ne pas choisir, c'est choisir. L'excuse fuit la responsabilité."),
    dict(q="Pourquoi Sartre ne donne-t-il pas de réponse à son élève ?",
         r=["Parce qu'il n'en sait rien", "Parce qu'aucune morale toute faite ne peut choisir à sa place", "Parce que l'élève n'est pas libre",
            "Parce que la réponse est évidente"], ok=1,
         voir="c_inv", ex="« Vous êtes libre, choisissez, c'est-à-dire inventez » : c'est en choisissant que l'élève donne un sens à sa situation."),
]

CREDITS = [
    "Descartes : d'après Frans Hals, XVIIᵉ siècle",
    "Sartre : photographie de 1965, Nationaal Archief / Anefo (CC BY-SA 3.0 NL)",
    "Spinoza, Ethica (1677)",
    "Photographies : Paris sous l'Occupation (Bundesarchiv, Friedrich, CC BY-SA 3.0 DE) ; de Gaulle au micro de la BBC (Keystone, domaine public) ; chemin forestier (Alec MacKinnon, CC BY-SA 2.0) ; café de Flore (domaine public) ; masques de théâtre (Marjorie Kaufman, CC BY-SA 4.0) ; Rodin, Le Penseur (Jebulon, CC0)",
    "Tableaux et gravures : Annibale Carracci, Hercule à la croisée des chemins (1596) ; Rembrandt, Philosophe en méditation (1632) ; Descartes, Meditationes (1641) ; W. A. Rogers, caricature (v. 1902) ; C. D. Friedrich, Le Voyageur contemplant une mer de nuages (v. 1818) ; E. Munch, Le Cri (1893) ; H. Evenepoel, Au café d'Harcourt (1897) : domaine public",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
