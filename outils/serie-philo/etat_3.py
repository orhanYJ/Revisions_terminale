"""L'État, épisode 3 : « L'État et la liberté »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la vérité} dans le texte lu. Prolonge la série « La liberté », épisode 5 (Montesquieu, Mill) sans la refaire ;
le texte de Spinoza (TTP, XX) est expliqué pas à pas dans l'épisode 6.
Citations : Montesquieu, De l'esprit des lois, XI, 4 et XI, 6 (1748), Wikisource, orthographe modernisée ;
Spinoza, Traité théologico-politique, XX (1670), trad. É. Saisset (1842), Wikisource ; Mussolini, discours de la Scala
(28 octobre 1925), trad. courante ; Orwell, 1984 (1949), I, 7, citation courte, trad. courante.
Résumés par le narrateur : Arendt (Les Origines du totalitarisme, 1951), Orwell (1984 : télécran, ministère de la Vérité,
novlangue), l'affaire du Watergate (1974), l'habeas corpus (1679), les lettres de cachet, le meunier de Sans-Souci.
"""

CODE = "etat-3"
NOTION = "L'État"
NUM = 3
TITRE = "L'État et la liberté"
SUIVANT = "Épisode 4 · Contre l'État ? La Boétie, Marx, les anarchistes, Nietzsche"
PRONONCIATION = {"Arendt": "Arènnte", "Orwell": "Orouel", "Winston": "Ouinnstone", "Watergate": "Ouatergueït",
                 "Nixon": "Nixone", "Spinoza": "Spinoza", "Brède": "Brède", "Sans-Souci": "Sans-Souci",
                 "corpus": "corpusse", "habeas": "abéasse", "Mussolini": "Moussolini", "Kelsen": "Kèlsène"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_lon}{an}Londres, un jour d'avril froid et clair. Les horloges sonnent treize heures. "
        "Un homme de trente-neuf ans, Winston Smith, rentre chez lui. Dans l'escalier, sur chaque palier, la même affiche : "
        "un visage moustachu, et une phrase.",
        "{-an}{bb}",
        ("Big Brother te regarde.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-bb}{tel}Dans son appartement, un écran ne s'éteint jamais : le télécran. Il diffuse, et il écoute. "
        "{tel.1}Il voit tout ce qui se passe dans son champ. {tel.2}Winston s'est donc assis dans un coin, hors de sa vue. "
        "{tel.3}Et dans un cahier, il écrit, en capitales : à bas Big Brother. Un crime qui peut lui coûter la vie.",
        "{-tel}{-tab_lon}{tab_cct}{q_men}C'est le début de 1984, le roman de George Orwell, publié en 1949 : "
        "tu le lis peut-être en anglais. Une fiction, bien sûr. Mais elle pose la question de cet épisode.",
        "{-q_men}{para}On l'a vu : nous avons besoin de l'État pour être en sécurité, pour être libres. "
        "{para.1}Mais un État assez puissant pour nous protéger est aussi assez puissant pour nous écraser. "
        "{para.2}Comment faire pour que le gardien de nos libertés n'en devienne pas le geôlier ?",
        ("P", 0.3),
        "{-para}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_lon": dict(type="tableau", img="et3-londres", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Cecil Beaton, Londres sous le Blitz, 1940 (Imperial War Museum, domaine public) : la ville d'Orwell"),
        "an": dict(type="mot", t="1984", g="George Orwell, roman publié en 1949", y=270, taille=120),
        "bb": dict(type="mot", t="BIG BROTHER IS WATCHING YOU", g="« Big Brother te regarde » · 1984, I, 1", y=270, taille=56),
        "tel": dict(type="liste", titre="Le télécran", items=[
            "Il diffuse, il écoute, il voit", "Winston se cache dans un coin, hors de sa vue",
            "Il écrit : DOWN WITH BIG BROTHER"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "tab_cct": dict(type="tableau", img="et3-cameras", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Caméra de surveillance (photo Ivan Radic, CC BY 2.0)"),
        "q_men": dict(type="question", t="Une fiction… ou un avertissement ?"),
        "para": dict(type="liste", titre="Le paradoxe", items=[
            "Assez puissant pour nous protéger… donc assez puissant pour nous écraser",
            "Comment empêcher le gardien de devenir le geôlier ?"], marques=["!", "?"], x=170, y=190, w=940),
        "titre": dict(type="titre", sur="L'État · Épisode 3", t="L'État et la liberté",
                      sous="Montesquieu, l'État de droit, Spinoza, le totalitarisme"),
    }),

    # ------------------------------------------------------------------ I. Montesquieu
    dict(id="montesquieu", chap="Le pouvoir arrête le pouvoir", fond="aube", humeur="lumiere", notions=["la justice", "la liberté"],
         retenir="Montesquieu : tout pouvoir tend à l'abus. Les trois pouvoirs (faire les lois, les exécuter, juger) doivent être séparés : le pouvoir arrête le pouvoir.",
         beats=[
        "{tab_bre}{mont}Première réponse, et la plus célèbre. Elle vient d'un magistrat de Bordeaux, Montesquieu, qui publie en 1748 "
        "De l'esprit des lois. Son point de départ est d'un réalisme sans illusion.",
        ("C", "… c'est une expérience éternelle, que tout homme qui a du pouvoir est porté à en abuser ; "
              "il va jusqu'à ce qu'il trouve des limites.", "c_abus"),
        "{-mont}{-c_abus}{rap}Tu connais sa solution : on l'a vue dans la série sur la liberté. "
        "Il faut que, par la disposition des choses, le pouvoir arrête le pouvoir. Allons plus loin : comment ?",
        "{-rap}{ang}Il a trouvé le modèle en Angleterre, où il a séjourné près de deux ans : un pays où le roi gouverne, mais où le Parlement fait les lois et où les juges ne dépendent pas du roi. {-ang}{-tab_bre}{tab_edl}{trois}Montesquieu distingue {trois.1}le pouvoir de faire les lois, {trois.2}celui de les exécuter, "
        "{trois.3}et celui de juger. Et il prévient.{-trois}",
        ("C", "Tout serait perdu, si le même homme, ou le même corps des principaux, ou des nobles, ou du peuple, exerçaient "
              "ces trois pouvoirs ; celui de faire des lois, celui d'exécuter les résolutions publiques, et celui de juger "
              "les crimes ou les différends des particuliers.", "c_perdu"),
        "{-c_perdu}{-tab_edl}{tab_par}{fr}Concrètement, en France : {fr.1}le Parlement vote les lois ; {fr.2}le gouvernement les exécute ; "
        "{fr.3}les juges tranchent les litiges. Aucun ne peut faire le métier des deux autres. "
        "Celui qui fait la loi ne juge pas ; celui qui juge ne gouverne pas. C'est à ce prix que la {#la liberté}liberté de chacun est protégée.",
        "{-fr}{-tab_par}{tab_nix}{nix}Ce mécanisme marche-t-il ? Washington, 1974. Le président Richard Nixon est soupçonné d'avoir "
        "couvert l'espionnage de ses adversaires, dans l'affaire du Watergate. Il refuse de livrer les enregistrements de son bureau.",
        "{nix.1}Le 24 juillet, la Cour suprême, à l'unanimité, lui ordonne de les remettre. {nix.2}Le Congrès prépare sa destitution. "
        "{nix.3}Le 9 août, l'homme le plus puissant du monde démissionne.",
        ("Un juge a arrêté un président. C'est exactement ce que voulait Montesquieu.", {"rate": "-5%"}),
        "{-nix}{-tab_nix}",
    ], vis={
        "tab_bre": dict(type="tableau", img="et3-labrede", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Le château de La Brède, près de Bordeaux, demeure de Montesquieu (carte postale, vers 1900-1920)"),
        "mont": dict(type="portrait", annee=1689, img="montesquieu", nom="Montesquieu", dates="1689 – 1755",
                     legende="De l'esprit des lois (1748)", x=110, y=120, w=330, h=420),
        "c_abus": dict(type="cit", a="Montesquieu", o="De l'esprit des lois, XI, 4 (1748)", x=640, y=170, w=570),
        "rap": dict(type="mot", t="Le pouvoir arrête le pouvoir", g="De l'esprit des lois, XI, 4 · voir la série « La liberté », épisode 5",
                    y=260, taille=66),
        "tab_edl": dict(type="tableau", img="et3-esprit-lois", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Montesquieu, De l'esprit des loix, Genève, Barrillot, 1748, tome I, page de titre"),
        "ang": dict(type="mot", t="Le modèle anglais", g="Montesquieu en Angleterre, 1729-1731", y=270, taille=88),
        "trois": dict(type="cartes", items=[
            dict(ic="colonnes", t="Législatif", q="faire les lois"),
            dict(ic="porte", t="Exécutif", q="les exécuter"),
            dict(ic="chemins", t="Judiciaire", q="juger")]),
        "c_perdu": dict(type="cit", a="Montesquieu", o="De l'esprit des lois, XI, 6 (1748)", x=170, y=140, w=940),
        "tab_par": dict(type="tableau", img="t5-hemicycle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="L'hémicycle de l'Assemblée nationale, Paris (photo Coucouoeuf, CC BY-SA 3.0)"),
        "fr": dict(type="liste", titre="En France", items=[
            "Le Parlement vote les lois", "Le gouvernement les exécute", "Les juges tranchent les litiges"],
                   marques=["1", "2", "3"], x=170, y=170, w=940),
        "tab_nix": dict(type="tableau", img="et3-nixon", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .4],
                        legende="Richard Nixon fait ses adieux au personnel de la Maison-Blanche, 9 août 1974 (photographie officielle, domaine public)"),
        "nix": dict(type="liste", titre="L'affaire du Watergate (1974)", items=[
            "24 juillet : la Cour suprême ordonne de livrer les enregistrements",
            "Le Congrès prépare la destitution", "9 août : Nixon démissionne"], marques=["1", "2", "3"], x=170, y=160, w=940),
    }),

    # ------------------------------------------------------------------ II. l'État de droit
    dict(id="droit", chap="L'État de droit", fond="nuit", humeur="calme", notions=["la justice", "la liberté"],
         retenir="L'État de droit : l'État lui-même est soumis au droit. Des juges indépendants, des droits garantis, une hiérarchie des normes. Un État peut être légal sans être un État de droit.",
         beats=[
        "{tab_bas}{ldc}Pour mesurer le progrès, remonte en France avant 1789. Une simple lettre signée du roi, la lettre de cachet, "
        "peut envoyer n'importe qui en prison, sans procès, sans durée fixée. En 1717, le jeune Voltaire passe ainsi onze mois "
        "à la Bastille, pour quelques vers moqueurs.",
        "{-ldc}{hab}L'Angleterre, elle, a déjà sa parade : depuis 1679, la loi d'habeas corpus. "
        "Toute personne arrêtée doit être présentée à un juge, qui vérifie si sa détention est légale. "
        "Sinon, on la libère.",
        "{-hab}{-tab_bas}{tab_mou}{meu}Une histoire, peut-être légendaire, résume cet esprit. Au dix-huitième siècle, à Potsdam, "
        "le roi de Prusse, Frédéric le Grand, veut se débarrasser d'un moulin, trop proche de son château. "
        "{meu.1}Le meunier refuse de vendre. {meu.2}Le roi menace de le prendre de force. "
        "{meu.3}Et le meunier répond : il y a des juges à Berlin.",
        ("Même le roi doit compter avec le droit.", {"rate": "-5%"}),
        "{-meu}{edd}C'est cela, l'État de droit. {edd.1}Non pas seulement un État qui fait des lois : tous les États en font. "
        "{edd.2}Mais un État qui est lui-même soumis au droit, avec des juges indépendants, et des droits que nul ne peut violer.",
        "{-edd}{-tab_mou}{tab_nur}{leg}Car un État peut être parfaitement légal… et monstrueux. "
        "En 1935, l'Allemagne nazie vote en bonne et due forme les lois de Nuremberg, qui privent les Juifs de leurs droits de citoyens. "
        "{leg.g}Légal, oui. {leg.d}État de droit, non : la loi n'y protège plus les personnes, elle les livre.",
        "{-leg}{-tab_nur}{tab_cc}{kel}Pour aller plus loin, le juriste Hans Kelsen a donné à l'État de droit son architecture : la hiérarchie des normes. "
        "{kel.1}En haut, la Constitution et les droits fondamentaux. {kel.2}Au-dessous, les lois, qui doivent les respecter. "
        "{kel.3}Plus bas, les décrets et les décisions. Et des juges pour le vérifier, comme chez nous le Conseil constitutionnel. Le 16 juillet 1971, il censure une loi votée par le Parlement, parce qu'elle restreignait la liberté de fonder une association.",
        "{-kel}{-tab_cc}",
    ], vis={
        "tab_bas": dict(type="tableau", img="t-bastille", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .5],
                        legende="Jean-Pierre Houël, La Prise de la Bastille, 1789"),
        "ldc": dict(type="def", cles=["sans procès"], terme="La lettre de cachet",
                    t="Un ordre du roi : la prison sans procès, sans durée fixée.",
                    etape="Voltaire, 1717 : onze mois à la Bastille pour des vers moqueurs.", x=170, y=200, w=940),
        "hab": dict(type="def", cles=["juge", "libère"], terme="Habeas corpus (Angleterre, 1679)",
                    t="Toute personne arrêtée doit être présentée à un juge.",
                    etape="Si la détention n'est pas légale, on la libère.", x=170, y=200, w=940),
        "tab_mou": dict(type="tableau", img="et3-moulin", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .4],
                        legende="Le moulin historique de Sans-Souci, à Potsdam (photo H. Zell, CC BY-SA 3.0)"),
        "meu": dict(type="dialogue", lignes=["Le meunier refuse de vendre.", "Le roi menace de prendre le moulin de force.",
                                             "« Il y a des juges à Berlin ! »"],
                    src="anecdote rendue célèbre par le poème d'Andrieux, Le Meunier de Sans-Souci (1797) · peut-être légendaire",
                    x=170, y=180, w=940),
        "edd": dict(type="liste", titre="L'État de droit", items=[
            "Pas seulement un État qui fait des lois : tous en font",
            "Un État soumis lui-même au droit : juges indépendants, droits garantis"], marques=["✗", "✓"],
                    x=170, y=190, w=940),
        "tab_nur": dict(type="tableau", img="et3-nuremberg-lois", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .45],
                        legende="Tableau officiel des lois de Nuremberg, Allemagne, 1935 (domaine public)"),
        "leg": dict(type="cols", g="Un État légal", gq="il vote ses lois en bonne et due forme",
                    d="Un État de droit", dq="la loi protège les personnes, même contre l'État", vs="≠"),
        "tab_cc": dict(type="tableau", img="et3-conseil", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                       legende="L'entrée du Conseil constitutionnel, Palais-Royal, Paris (photo Jebulon, CC0)"),
        "kel": dict(type="liste", titre="La hiérarchie des normes (Kelsen)", items=[
            "La Constitution et les droits fondamentaux", "Les lois, qui doivent les respecter",
            "Les décrets et les décisions"], marques=["1", "2", "3"], x=170, y=160, w=940, plus=True),
    }),

    # ------------------------------------------------------------------ III. Spinoza
    dict(id="spinoza", chap="Spinoza : la fin de l'État, c'est la liberté", fond="aube", humeur="lumiere",
         notions=["la raison", "la vérité", "la religion"],
         retenir="Spinoza : la fin de l'État est la liberté. On ne commande pas aux esprits : l'État doit laisser chacun penser et dire ce qu'il pense, tant qu'il obéit aux lois dans ses actes.",
         beats=[
        "{tab_ams}{spino}{n_spi}Remontons à Amsterdam, au dix-septième siècle. La ville est la plus tolérante d'Europe ; "
        "pourtant, en 1656, la communauté juive y a exclu un jeune homme pour ses idées : Baruch Spinoza.",
        "{-spino}{-n_spi}{tab_ttp}{ttp}En 1670, il publie un livre sans nom d'auteur, sous une fausse adresse d'éditeur : "
        "le Traité théologico-politique. Le livre sera interdit quatre ans plus tard. "
        "{ttp.1}Le titre de son dernier chapitre dit tout : dans un État libre, chacun a le droit de penser ce qu'il veut, "
        "et de dire ce qu'il pense.",
        "{-ttp}{arg}Son argument est simple. {arg.1}On peut contraindre les corps ; on ne peut pas commander aux esprits. "
        "Personne ne peut croire sur ordre. {arg.2}Un État qui prétend régler les pensées ne fabrique pas des croyants : "
        "il fabrique des hypocrites, qui disent une chose et en pensent une autre, et des rebelles.",
        "{-arg}{-tab_ttp}{tab_ams2}{q_fin}Alors, à quoi sert l'État ? Spinoza répond : non pas à transformer les hommes en bêtes "
        "ou en automates, mais à leur permettre de vivre en sécurité, et d'user librement de leur {#la raison}raison.{-q_fin}",
        ("C", "La fin de l'État, c'est donc véritablement la liberté.", "c_spi"),
        "{-c_spi}{nuance}Attention, nuance capitale. {nuance.1}Spinoza ne dit pas que chacun peut faire ce qu'il veut. "
        "Dans ses actes, le citoyen obéit aux lois. {nuance.2}Mais il garde le droit de juger, de critiquer, de dire tout haut "
        "qu'une loi est mauvaise, pour qu'on la change par les voies légales.",
        "{-nuance}{tag_ep6}Ce texte est un grand classique du bac : nous l'expliquerons pas à pas dans l'épisode six.",
        "{-tag_ep6}{mill}Deux siècles plus tard, John Stuart Mill en tirera le principe de non-nuisance, vu dans la série sur la liberté : "
        "l'État ne peut contraindre un individu que pour l'empêcher de nuire aux autres.",
        "{-mill}{-tab_ams2}",
    ], vis={
        "tab_ams": dict(type="tableau", img="et3-amsterdam", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Gerrit Berckheyde, La Place du Dam et l'hôtel de ville d'Amsterdam, 1672"),
        "spino": dict(type="portrait", annee=1632, img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                      legende="Traité théologico-politique (1670)", x=110, y=120, w=330, h=420),
        "n_spi": dict(type="note", titre="Amsterdam, 1656", cles=["idées"],
                      t="La ville la plus tolérante d'Europe… exclut pourtant Spinoza pour ses idées.", x=640, y=200, w=570),
        "tab_ttp": dict(type="tableau", img="et3-ttp", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .3],
                        legende="Tractatus theologico-politicus, « Hambourg » (en réalité Amsterdam), 1670, page de titre"),
        "ttp": dict(type="def", cles=["penser", "dire"], terme="Traité théologico-politique, chapitre XX",
                    t="Dans un État libre, chacun a le droit de penser ce qu'il veut et de dire ce qu'il pense.",
                    etape="1670 : publié sans nom d'auteur, interdit en 1674.", x=170, y=200, w=940),
        "arg": dict(type="liste", titre="On ne commande pas aux esprits", items=[
            "On contraint les corps, pas les pensées : personne ne croit sur ordre",
            "Régler les pensées fabrique des hypocrites… et des rebelles"], marques=["1", "2"], x=170, y=190, w=940),
        "tab_ams2": dict(type="tableau", img="et3-amsterdam", fond=True, sombre=True, de=[1.4, .3, .45], a=[1.1, .5, .5],
                         legende="Gerrit Berckheyde, La Place du Dam et l'hôtel de ville d'Amsterdam, 1672"),
        "q_fin": dict(type="question", t="À quoi sert l'État ?"),
        "c_spi": dict(type="cit", a="Spinoza", o="Traité théologico-politique, chap. XX (1670), trad. Saisset", x=170, y=220, w=940),
        "nuance": dict(type="cols", g="Dans ses actes", gq="le citoyen obéit aux lois", d="Dans ses paroles",
                       dq="il garde le droit de juger, de critiquer", vs="≠"),
        "tag_ep6": dict(type="tag", style="copie", t="Explication de texte pas à pas : épisode 6", x=170, y=560, w=600),
        "mill": dict(type="note", titre="Mill (1859) · rappel", cles=["nuire"],
                     t="L'État ne peut contraindre un individu que pour l'empêcher de nuire aux autres.",
                     etape="Le principe de non-nuisance : voir la série « La liberté », épisode 5.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. le totalitarisme
    dict(id="totalitarisme", chap="Le totalitarisme", fond="nuit", humeur="tension", notions=["la liberté", "la vérité", "la conscience"],
         retenir="Arendt : le totalitarisme n'est pas une simple tyrannie. Idéologie, terreur, parti unique : il veut l'homme tout entier et détruit la vie privée, la pensée, la solitude même.",
         beats=[
        "{tab_ral}{mot_t}Au vingtième siècle, l'inverse de Spinoza devient réalité. Un mot nouveau apparaît en Italie : totalitaire. "
        "Mussolini le revendique, dans un discours de 1925.",
        "{-mot_t}",
        ("C", "Tout dans l'État, rien hors de l'État, rien contre l'État.", "c_mus"),
        "{-c_mus}{arendt}Hannah Arendt, juive allemande qui a fui le nazisme, publie en 1951 Les Origines du totalitarisme. "
        "{n_tot}Elle y montre que le totalitarisme n'est pas une tyrannie de plus. C'est un régime d'un genre nouveau, "
        "dont l'Allemagne nazie et l'Union soviétique de Staline sont les deux exemples.",
        "{-arendt}{-n_tot}{tyr}Quelle différence ? {tyr.g}Le tyran veut qu'on lui obéisse. Une fois l'impôt payé et la bouche fermée, "
        "on peut vivre tranquille chez soi. {tyr.d}Le régime totalitaire, lui, veut l'homme tout entier : ses actes, ses amis, "
        "sa famille, ses loisirs, et jusqu'à ses pensées.",
        "{-tyr}{-tab_ral}{tab_ter}{trois_t}Il repose sur trois piliers. {trois_t.1}Une idéologie, qui prétend tout expliquer "
        "par une seule loi : la race, ou la lutte des classes. {trois_t.2}Un parti unique, et un chef. "
        "{trois_t.3}Et la terreur : la police secrète, les dénonciations, les camps.",
        "{-trois_t}{iso}Mais le plus profond, selon Arendt, est ailleurs. {iso.1}Le totalitarisme {!isole}isole les individus : "
        "plus de confiance, plus d'amis sûrs, plus d'espace entre les hommes où l'on puisse parler librement. "
        "{iso.2}Seule, une masse d'hommes désolés se laisse tout dicter, même ce qu'il faut tenir pour {#la vérité}vrai.",
        ("Là où l'État est tout, l'homme n'est plus rien.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-iso}{-tab_ter}{tab_sta}{sta}Ce cauchemar a survécu à Staline. En Allemagne de l'Est, jusqu'en 1989, la police politique, la Stasi, s'appuie sur près de deux cent mille informateurs : des voisins, des collègues, parfois des époux. Ses archives, ouvertes après la chute du mur, font plus de cent kilomètres de dossiers.",
        "{-sta}{-tab_sta}",
    ], vis={
        "tab_ral": dict(type="tableau", img="et3-nuremberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Congrès du parti nazi à Nuremberg, appel des SA et des SS (Bundesarchiv, Bild 102-16196, CC BY-SA 3.0 de)"),
        "mot_t": dict(type="mot", t="Totalitaire", g="un mot né en Italie, au début des années 1920", y=260, taille=100),
        "c_mus": dict(type="cit", a="Benito Mussolini", o="discours de la Scala de Milan, 28 octobre 1925 (trad. courante)",
                      x=170, y=230, w=940),
        "n_tot": dict(type="note", titre="Les Origines du totalitarisme (1951)", cles=["tyrannie", "nouveau"],
                     t="Pas une tyrannie de plus : un régime d'un genre nouveau.",
                     etape="Deux exemples : l'Allemagne nazie, l'Union soviétique de Staline.", x=640, y=150, w=570),
        "arendt": dict(type="portrait", annee=1906, img="arendt", nom="Hannah Arendt", dates="1906 – 1975",
                       legende="Les Origines du totalitarisme (1951)", x=110, y=120, w=330, h=420),
        "tyr": dict(type="cols", g="La tyrannie", gq="elle veut qu'on obéisse : la vie privée reste à soi",
                    d="Le totalitarisme", dq="il veut l'homme tout entier, jusqu'à ses pensées", vs="≠",
                    repere="Arendt, Les Origines du totalitarisme (1951)"),
        "tab_ter": dict(type="tableau", img="et3-panoptique", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .55],
                        legende="Le Presidio Modelo, prison bâtie sur le plan du Panoptique, île de la Jeunesse, Cuba (photo Friman, CC BY-SA 3.0)"),
        "trois_t": dict(type="liste", titre="Les trois piliers", items=[
            "Une idéologie qui prétend tout expliquer : la race, la lutte des classes",
            "Un parti unique, et un chef", "La terreur : police secrète, dénonciations, camps"],
                        marques=["1", "2", "3"], cles=["idéologie", "parti unique", "terreur"], x=170, y=150, w=940),
        "tab_sta": dict(type="tableau", img="et3-stasi", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="L'ancien siège de la Stasi à Berlin, aujourd'hui musée (photo Prof.Quatermass, CC BY 3.0)"),
        "sta": dict(type="mot", t="111 km", g="les dossiers de la Stasi, police politique de l'Allemagne de l'Est", y=270, taille=110),
        "iso": dict(type="liste", titre="Le plus profond (Arendt)", items=[
            "Isoler les individus : plus d'espace entre les hommes pour parler librement",
            "Des hommes seuls se laissent tout dicter, même le vrai"], marques=["1", "2"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ V. Orwell
    dict(id="orwell", chap="1984 : le cauchemar d'Orwell", fond="aube", humeur="mystere", notions=["la vérité", "le langage", "la liberté"],
         retenir="Orwell : surveiller les actes (le télécran), réécrire le passé (le ministère de la Vérité), appauvrir la langue (le novlangue). Être libre, c'est pouvoir dire que deux et deux font quatre.",
         beats=[
        "{tab_sen}{min}Orwell a vu tout cela de près. Pendant la guerre, il a travaillé à la BBC, et sa femme au service de la censure "
        "du ministère de l'Information, installé dans ce bâtiment de Londres. Il en fera le ministère de la Vérité.",
        "{-min}{slog}Sur sa façade, trois slogans. {slog.1}La guerre, c'est la paix. {slog.2}La liberté, c'est l'esclavage. "
        "{slog.3}L'ignorance, c'est la force.",
        "{-slog}{mv}Le métier de Winston, au ministère de la Vérité ? {mv.1}Réécrire les vieux journaux. Quand le Parti s'est trompé, "
        "on corrige le passé, et l'original part au feu. {mv.2}Qui contrôle le passé, dit le Parti, contrôle l'avenir ; "
        "qui contrôle le présent contrôle le passé.",
        "{-mv}{nov}Plus loin encore : le novlangue. On supprime des mots, par centaines. {nov.1}S'il n'y a plus de mot pour dire liberté, "
        "comment penser la liberté ? {nov.2}Le but, explique un linguiste du Parti, est de restreindre les limites de la pensée. "
        "Le {#le langage}langage devient une prison.",
        "{-nov}{-tab_sen}{tab_pan}{opp}Tu vois l'opposition avec Spinoza. {opp.g}Pour Spinoza, on ne peut pas commander aux esprits. "
        "{opp.d}Le pouvoir de 1984 a trouvé comment : non pas en forçant les gens à croire, mais en détruisant les mots, "
        "la mémoire, et la vérité elle-même.",
        "{-opp}Dans la première partie du roman, Winston écrit dans son cahier une phrase qui résume tout l'épisode.",
        ("C", "La liberté, c'est la liberté de dire que deux et deux font quatre. Lorsque cela est accordé, le reste suit.", "c_orw"),
        "{-c_orw}{fin_o}À la fin, brisé par la torture, Winston tracera du doigt : deux et deux font {!cinq}cinq. {fin_o.1}Le roman ne dit pas "
        "que l'État est toujours un monstre. {fin_o.2}Il montre ce qu'il devient quand rien ne l'arrête : ni juges, ni lois, "
        "ni presse libre, ni ce petit coin de soi que personne ne doit pouvoir atteindre.",
        "{-fin_o}{-tab_pan}",
    ], vis={
        "tab_sen": dict(type="tableau", img="et3-senate", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .3],
                        legende="Senate House, Londres : le ministère de l'Information pendant la guerre, modèle du ministère de la Vérité (photo David Dixon, CC BY-SA 2.0)"),
        "min": dict(type="mot", t="Ministry of Truth", g="le ministère de la Vérité · « Minivrai »", y=270, taille=86),
        "slog": dict(type="liste", titre="Les slogans du Parti", items=[
            "WAR IS PEACE · la guerre, c'est la paix", "FREEDOM IS SLAVERY · la liberté, c'est l'esclavage",
            "IGNORANCE IS STRENGTH · l'ignorance, c'est la force"], marques=["1", "2", "3"], x=170, y=170, w=940),
        "mv": dict(type="liste", titre="Le ministère de la Vérité", items=[
            "Réécrire les vieux journaux : le passé se corrige",
            "« Qui contrôle le passé contrôle l'avenir ; qui contrôle le présent contrôle le passé »"],
                   marques=["1", "2"], x=170, y=170, w=940),
        "nov": dict(type="liste", titre="Le novlangue (Newspeak)", items=[
            "Plus de mot pour dire liberté : comment la penser ?",
            "But : restreindre les limites de la pensée"], marques=["1", "2"], x=170, y=190, w=940),
        "tab_pan": dict(type="tableau", img="et2-panoptique", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.4, .5, .55],
                        legende="Willey Reveley, plan du Panoptique de Jeremy Bentham, 1791 : voir sans être vu"),
        "opp": dict(type="cols", g="Spinoza", gq="on ne peut pas commander aux esprits", d="1984",
                    dq="détruire les mots, la mémoire, la vérité", vs="≠"),
        "c_orw": dict(type="cit", a="George Orwell", o="1984, I, 7 (1949), trad. courante", x=170, y=200, w=940),
        "fin_o": dict(type="liste", titre="La leçon de 1984", items=[
            "Non pas : l'État est toujours un monstre",
            "Mais : voilà ce qu'il devient quand rien ne l'arrête"], marques=["✗", "✓"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ret}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Montesquieu. Tout pouvoir tend à l'abus ; "
        "il faut séparer les pouvoirs, pour que le pouvoir arrête le pouvoir.",
        "{rec.2}Deux : l'État de droit. L'État lui-même est soumis au droit, et des juges indépendants le rappellent. "
        "Légal ne veut pas dire juste.",
        "{rec.3}Trois : Spinoza. La fin de l'État, c'est la liberté ; on ne commande pas aux esprits.",
        "{rec.4}Quatre : le totalitarisme, avec Arendt et Orwell. Un État qui veut tout, jusqu'à nos pensées, détruit la liberté "
        "à sa racine.",
        "{-rec}{-tab_ret}{tab_fin}{q_suite}Mais si le danger n'était pas seulement tel ou tel État… "
        "et si c'était l'État lui-même ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : contre l'État ? La Boétie, Marx, les anarchistes, et Nietzsche.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ret": dict(type="tableau", img="et3-labrede", fond=True, sombre=True, de=[1.3, .4, .45], a=[1.0, .5, .5],
                        legende="Le château de La Brède, demeure de Montesquieu (carte postale, vers 1900-1920)"),
        "rec": dict(type="carte", centre="L'ÉTAT ET LA LIBERTÉ", branches=[
            dict(t="Montesquieu", items=["tout pouvoir tend à l'abus", "trois pouvoirs séparés", "Watergate (1974)"]),
            dict(t="L'État de droit", items=["habeas corpus", "des juges à Berlin", "légal ≠ État de droit"]),
            dict(t="Spinoza", items=["la fin de l'État : la liberté", "on ne commande pas aux esprits", "obéir, mais pouvoir critiquer"]),
            dict(t="Le totalitarisme", items=["Arendt : idéologie, terreur", "l'homme tout entier", "Orwell : 2 + 2 = 4"])]),
        "tab_fin": dict(type="tableau", img="et3-vendome", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .55],
                        legende="Auguste Braquehais, la colonne Vendôme abattue par la Commune de Paris, 16 mai 1871 (musée Carnavalet, CC0)"),
        "q_suite": dict(type="question", t="Et si le danger, c'était l'État lui-même ?"),
        "fin": dict(type="titre", sur="À suivre", t="Contre l'État ?", sous="Épisode 4 · La Boétie, Marx, les anarchistes, Nietzsche"),
    }),
]

QUIZ = [
    dict(q="Selon Montesquieu, pourquoi faut-il séparer les pouvoirs ?",
         r=["Parce que le peuple l'a voté", "Parce que tout homme qui a du pouvoir est porté à en abuser",
            "Parce que le roi est trop occupé", "Parce que les juges sont plus sages"], ok=1,
         voir="c_abus", ex="De l'esprit des lois, XI, 4 : « une expérience éternelle ». D'où la règle : le pouvoir arrête le pouvoir."),
    dict(q="Quels sont les trois pouvoirs que distingue Montesquieu ?",
         r=["Le roi, la noblesse, le clergé", "Faire les lois, les exécuter, juger", "L'armée, la police, la justice",
            "Le peuple, le Parlement, le président"], ok=1,
         voir="trois", ex="Législatif, exécutif, judiciaire (XI, 6) : « tout serait perdu » s'ils étaient réunis dans les mêmes mains."),
    dict(q="Qu'est-ce qu'un État de droit ?",
         r=["Un État qui fait beaucoup de lois", "Un État où l'État lui-même est soumis au droit, sous le contrôle de juges indépendants",
            "Un État de droite", "Un État sans police"], ok=1,
         voir="edd", ex="Tous les États font des lois ; l'Allemagne nazie était légale. L'État de droit protège les personnes, même contre l'État (habeas corpus, « des juges à Berlin »)."),
    dict(q="Selon Spinoza, quelle est la fin de l'État ?",
         r=["La sécurité seule", "L'obéissance", "La liberté", "La richesse"], ok=2,
         voir="c_spi", ex="Traité théologico-politique, XX : l'État doit permettre aux hommes d'user librement de leur raison. On ne commande pas aux esprits."),
    dict(q="Pour Spinoza, que garde le citoyen dans un État libre ?",
         r=["Le droit de désobéir à toutes les lois", "Le droit de penser et de dire ce qu'il pense, en obéissant aux lois dans ses actes",
            "Le droit de se faire justice", "Rien : il a tout donné au souverain"], ok=1,
         voir="nuance", ex="Obéir dans ses actes, mais pouvoir juger et critiquer, pour qu'on change les lois par les voies légales."),
    dict(q="Selon Arendt, qu'est-ce qui distingue le totalitarisme de la tyrannie ?",
         r=["Il est moins violent", "Il veut l'homme tout entier, jusqu'à sa vie privée et ses pensées",
            "Il n'a pas de chef", "Il respecte les élections"], ok=1,
         voir="tyr", ex="Idéologie, parti unique, terreur ; et surtout l'isolement des individus (Les Origines du totalitarisme, 1951)."),
    dict(q="Dans 1984, à quoi sert le novlangue ?",
         r=["À communiquer avec l'étranger", "À restreindre les limites de la pensée en supprimant des mots",
            "À écrire de la poésie", "À enseigner le latin"], ok=1,
         voir="nov", ex="Sans mot pour dire liberté, plus moyen de la penser. Le contraire de Spinoza : le pouvoir commande enfin aux esprits."),
]

CREDITS = [
    "Portraits : Montesquieu (anonyme, 1728, château de Versailles) ; Baruch Spinoza (portrait anonyme, vers 1665) ; "
    "Hannah Arendt (photographie anonyme, 1933) : domaine public",
    "Tableaux : Jean-Pierre Houël, La Prise de la Bastille (1789) ; Gerrit Berckheyde, La Place du Dam à Amsterdam (1672) : domaine public",
    "Photographies et documents : Cecil Beaton, Londres sous le Blitz (1940, IWM) ; château de La Brède (cartes postales, vers 1900-1920) ; "
    "Nixon quittant la Maison-Blanche (1974, White House Photo Office) ; tableau des lois de Nuremberg (1935) ; Tractatus theologico-politicus (1670) ; "
    "Auguste Braquehais, la colonne Vendôme abattue (1871, musée Carnavalet) : domaine public. "
    "Caméra de surveillance (Ivan Radic, CC BY 2.0) ; moulin de Sans-Souci (H. Zell, CC BY-SA 3.0) ; "
    "congrès de Nuremberg (Bundesarchiv, Bild 102-16196, CC BY-SA 3.0 de) ; Presidio Modelo (Friman, CC BY-SA 3.0) ; "
    "Senate House (David Dixon, CC BY-SA 2.0) ; hémicycle de l'Assemblée nationale (Coucouoeuf, CC BY-SA 3.0) ; "
    "Willey Reveley, plan du Panoptique (1791) ; De l'esprit des loix (1748), page de titre ; "
    "Conseil constitutionnel (Jebulon, CC0) ; siège de la Stasi (Prof.Quatermass, CC BY 3.0)",
    "Citations : Montesquieu, De l'esprit des lois (1748) ; Spinoza, Traité théologico-politique (1670), trad. Émile Saisset (1842) ; "
    "Mussolini, discours du 28 octobre 1925 ; George Orwell, 1984 (1949), citation courte. Arendt, Kelsen, l'affaire du Watergate "
    "et l'anecdote du meunier de Sans-Souci sont résumés par le narrateur.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
