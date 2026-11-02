"""La conscience, épisode 2 : « Je pense, donc je suis »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la vérité} dans le texte lu.
Citations de Descartes : Discours de la méthode, IV (1637) et Méditations métaphysiques, I et II (1641 ; trad. Luynes,
1647), vérifiées sur le texte du Projet Gutenberg (édition établie d'après la BnF), orthographe modernisée.
Hume : Traité de la nature humaine, I, IV, 6 (1739), traduction courante de « For my part, when I enter most
intimately into what I call myself, I always stumble on some particular perception or other… ».
Résumés par le narrateur : Tchouang-tseu (le rêve du papillon), Locke (Essai sur l'entendement humain, II, 27 :
le prince et le savetier, les jumeaux), Thomas Reid (Essais sur les facultés intellectuelles de l'homme, III, 6, 1785 :
l'officier courageux), Hume (le faisceau, le théâtre, le navire).
"""

CODE = "conscience-2"
NOTION = "La conscience"
NUM = 2
TITRE = "Je pense, donc je suis"
SUIVANT = "Épisode 3 · La conscience est-elle transparente ? Leibniz, Freud, Nietzsche"
PRONONCIATION = {"cogito": "kojito", "Reid": "Rid", "Hume": "Hioume", "Locke": "Lok"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_exa}{q_rev}Cette nuit, tu passais ton bac. La salle, les copies, le silence. Tu ne trouvais plus ton stylo, "
        "l'heure tournait… Et pendant tout ce temps, tu en étais absolument certain : c'était réel.",
        ("Puis le réveil a sonné.", {"rate": "-6%", "pitch": "-1Hz"}),
        "{-q_rev}{-tab_exa}{tab_pap}{zhu}Il y a plus de deux mille ans, le sage chinois Tchouang-tseu rêva qu'il était un papillon. "
        "À son réveil, il se demanda : {zhu.1}suis-je Tchouang-tseu, qui a rêvé qu'il était un papillon… "
        "{zhu.2}ou un papillon qui rêve, en ce moment, qu'il est Tchouang-tseu ?",
        "{-zhu}{q_mtn}Alors, pose-toi la question. Comment sais-tu que tu ne rêves pas, en ce moment même ?",
        "{-q_mtn}{-tab_pap}{tab_rap}{an}Au dix-septième siècle, un philosophe français a pris cette question tout à fait au sérieux. "
        "Il a décidé de douter de tout, pour trouver une seule chose dont il ne pourrait plus douter. "
        "Il s'appelait René Descartes.",
        "{-an}Et ce qu'il a trouvé, c'est… la conscience.",
        ("P", 0.3),
        "{-tab_rap}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "q_rev": dict(type="question", t="Tu en étais certain : c'était réel."),
        "tab_pap": dict(type="tableau", img="cs2-papillon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .6],
                        legende="Lu Zhi, Tchouang-tseu rêvant d'un papillon, XVIᵉ siècle (domaine public)"),
        "zhu": dict(type="liste", titre="Le rêve du papillon (Tchouang-tseu, IVᵉ s. av. J.-C.)", items=[
            "Tchouang-tseu a-t-il rêvé qu'il était un papillon ?",
            "Ou un papillon rêve-t-il qu'il est Tchouang-tseu ?"], marques=["?", "?"], x=170, y=190, w=940),
        "q_mtn": dict(type="question", t="Comment sais-tu que tu ne rêves pas, en ce moment même ?"),
        "tab_rap": dict(type="tableau", img="cs2-chevalier", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .5, .65],
                        legende="Raphaël, Le Songe du chevalier, vers 1504 (National Gallery, Londres)"),
        "an": dict(type="mot", t="Douter de tout", g="pour trouver une seule chose certaine", y=260, taille=100),
        "titre": dict(type="titre", sur="La conscience · Épisode 2", t="Je pense, donc je suis",
                      sous="Descartes, Locke, Hume"),
    }),

    # ------------------------------------------------------------------ I. le doute
    dict(id="doute", chap="Douter de tout", fond="aube", humeur="tension", notions=["la vérité", "la science"],
         retenir="Le doute méthodique : volontaire, radical, provisoire. Les sens trompent, le rêve imite la veille, le malin génie pourrait me tromper jusque dans les mathématiques.",
         beats=[
        "{desc}{tab_dam}Descartes a quarante ans passés. Il vit retiré en Hollande, loin de Paris, pour penser en paix. "
        "On l'a vu dans la série sur la liberté : depuis une nuit de 1619, il rêve de rebâtir tout le savoir sur des bases solides.",
        "Car ce qu'on lui a appris au collège, il s'en méfie. Tant d'opinions, tant de disputes, si peu de certitudes ! "
        "Une maison bâtie sur du sable, il faut la reprendre depuis les fondations.",
        "{-desc}{-tab_dam}{tab_dis}{meth}D'où sa méthode, exposée en 1637 dans le Discours de la méthode, puis approfondie en 1641 "
        "dans les Méditations. {meth.1}Rejeter comme absolument faux tout ce qui laisse place au moindre doute. "
        "{meth.2}Pour voir s'il reste, à la fin, quelque chose d'entièrement certain.",
        "{-meth}{-tab_dis}{tab_cra}{raisons}Premier motif de doute : {raisons.1}les sens. Ils nous trompent parfois. "
        "Un crayon plongé dans l'eau paraît brisé ; une tour carrée, de loin, paraît ronde. "
        "Or il n'est pas prudent de se fier à qui nous a trompés, même une seule fois.",
        "{-tab_cra}{tab_che}{raisons.2}Deuxième motif : le rêve. Les mêmes pensées que j'ai éveillé peuvent me venir quand je dors. "
        "Et il n'y a aucun signe sûr pour distinguer la veille du sommeil.",
        "{raisons.3}Mais les mathématiques ? Endormi ou éveillé, deux et trois font cinq, et le carré a quatre côtés. "
        "Cela, au moins, résiste ?",
        ("Pas encore. Descartes pousse le doute jusqu'au bout.", {"rate": "-5%"}),
        "{-raisons}{-tab_che}{tab_sat}Il imagine une hypothèse vertigineuse.",
        ("C", "Je supposerai donc… qu'un certain mauvais génie, non moins rusé et trompeur que puissant, "
              "a employé toute son industrie à me tromper.", "c_genie"),
        "{-c_genie}{mg}On l'appelle souvent le malin génie. {mg.1}Le ciel, la terre, les couleurs, mon corps même : "
        "tout ne serait qu'illusion. Et jusqu'aux calculs les plus simples, qu'il me ferait fausser à chaque fois.",
        "{-mg}{dm}Attention : ce doute n'est pas celui du sceptique, qui doute pour douter. {dm.1}Il est volontaire. "
        "{dm.2}Il est radical : il va jusqu'au bout. {dm.3}Et il est provisoire : il sert à trouver la {#la vérité}vérité, "
        "comme on vide un panier de pommes pour en ôter les pourries. {rep_cs}Il ne s'agit plus de croire, mais de savoir.",
        "{-dm}{-rep_cs}{-tab_sat}",
    ], vis={
        "desc": dict(type="portrait", annee=1596, img="descartes", nom="René Descartes", dates="1596 – 1650",
                     legende="Discours de la méthode (1637) · Méditations (1641)", x=110, y=120, w=330, h=420),
        "tab_dam": dict(type="tableau", img="cs2-dam", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .6],
                        legende="Gerrit Berckheyde, L'Hôtel de ville sur le Dam, Amsterdam, 1672 (Rijksmuseum)"),
        "tab_dis": dict(type="tableau", img="cs2-discours", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Descartes, Discours de la méthode, Leyde, Jan Maire, 1637, page de titre"),
        "meth": dict(type="liste", titre="La méthode", items=[
            "Rejeter comme faux tout ce qui laisse place au moindre doute",
            "Voir s'il reste quelque chose d'entièrement certain"], marques=["1", "2"], x=170, y=190, w=940),
        "tab_cra": dict(type="tableau", img="cs2-crayon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Un crayon dans un verre d'eau (photo Meganbeckett27, CC BY-SA 3.0)"),
        "raisons": dict(type="liste", titre="Pourquoi douter ?", items=[
            "Les sens nous trompent parfois", "Le rêve imite la veille", "Et les mathématiques ?"],
                        marques=["1", "2", "?"], x=170, y=170, w=940),
        "tab_che": dict(type="tableau", img="cs2-chevalier", fond=True, sombre=True, de=[1.3, .5, .65], a=[1.0, .5, .5],
                        legende="Raphaël, Le Songe du chevalier, vers 1504 (National Gallery, Londres)"),
        "tab_sat": dict(type="tableau", img="cs2-satan", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Gustave Doré, Satan, illustration du Paradis perdu de Milton, 1866"),
        "c_genie": dict(type="cit", a="Descartes", o="Méditations métaphysiques, I (1641 ; trad. 1647)", x=170, y=170, w=940),
        "mg": dict(type="note", titre="Le malin génie", cles=["illusion", "calculs"],
                   t="Le ciel, la terre, mon corps même : tout ne serait qu'illusion.",
                   etape="Jusqu'aux calculs les plus simples.", x=170, y=190, w=940),
        "dm": dict(type="liste", titre="Le doute méthodique", items=[
            "Volontaire : je décide de douter", "Radical : jusqu'au bout", "Provisoire : pour trouver la vérité"],
                   marques=["1", "2", "3"], cles=["Volontaire", "Radical", "Provisoire"], x=170, y=150, w=940),
        "rep_cs": dict(type="tag", style="repere", t="Repère · croire / savoir", x=170, y=560, w=420),
    }),

    # ------------------------------------------------------------------ II. le cogito
    dict(id="cogito", chap="Je pense, donc je suis", fond="nuit", humeur="lumiere", notions=["la vérité", "la raison"],
         retenir="Même si je doute de tout, je ne peux pas douter que je doute : je pense, donc je suis. La première vérité est celle de la conscience.",
         beats=[
        "{tab_arc}{q_reste}Reste-t-il quelque chose ? Descartes se compare à Archimède, qui ne demandait qu'un point fixe "
        "pour soulever la Terre. Un seul point fixe. Une seule certitude.",
        "{-q_reste}{inv}Et soudain, il le trouve. {inv.1}Je doute de tout ? Soit. {inv.2}Mais douter, c'est penser. "
        "{inv.3}Et pour penser, il faut être. Même si le malin génie me trompe… il faut bien que je sois, pour être trompé.",
        "{-inv}{-tab_arc}{desc2}{tab_med}",
        ("C", "Qu'il me trompe tant qu'il voudra, il ne saura jamais faire que je ne sois rien, "
              "tant que je penserai être quelque chose.", "c_trompe"),
        "{-c_trompe}Dans le Discours de la méthode, la découverte tient en quatre mots, les plus célèbres de la philosophie.",
        ("C", "Cette vérité, je pense, donc je suis, était si ferme et si assurée, que toutes les plus extravagantes "
              "suppositions des sceptiques n'étaient pas capables de l'ébranler.", "c_cog"),
        "{-c_cog}{-desc2}En latin, on dit : {!cogito}cogito.",
        "{intu}Et attention : ce n'est pas un raisonnement en trois temps, comme un calcul. {intu.1}C'est une intuition : "
        "je le saisis d'un seul regard, dans l'acte même de penser.",
        ("Et cela ne vaut qu'au présent, à la première personne : je pense, maintenant.", {"rate": "-5%"}),
        "{-intu}{prem}Mesure ce qui vient de se passer. {prem.1}La première vérité n'est ni le monde, ni Dieu, ni les mathématiques. "
        "{prem.2}C'est la conscience que j'ai de moi-même. Tout le reste du savoir sera rebâti, par la {#la raison}raison, "
        "à partir d'elle. C'est pourquoi on fait de Descartes le père de la philosophie du sujet.",
        "{-prem}{-tab_med}",
    ], vis={
        "tab_arc": dict(type="tableau", img="cs2-archimede", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .6, .5],
                        legende="Archimède soulevant le monde avec un levier, gravure du Mechanics Magazine, Londres, 1824"),
        "q_reste": dict(type="question", t="Reste-t-il une seule certitude ?"),
        "inv": dict(type="liste", titre="Le point fixe", items=[
            "Je doute de tout", "Mais douter, c'est penser", "Et pour penser, il faut être"],
                    marques=["1", "2", "3"], x=170, y=150, w=940),
        "desc2": dict(type="portrait", annee=1596, img="descartes", nom="René Descartes", dates="1596 – 1650",
                      legende="Méditations métaphysiques (1641)", x=110, y=120, w=330, h=420),
        "tab_med": dict(type="tableau", img="t2-meditations", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.25, .5, .3],
                        legende="Descartes, Meditationes de prima philosophia, page de titre, Paris, 1641"),
        "c_trompe": dict(type="cit", a="Descartes", o="Méditations métaphysiques, II (1641 ; trad. 1647)", x=640, y=170, w=570),
        "c_cog": dict(type="cit", a="Descartes", o="Discours de la méthode, IVe partie (1637)", x=640, y=150, w=570),
        "intu": dict(type="def", cles=["intuition", "regard"], terme="Le cogito",
                     t="Je pense, donc je suis : la première certitude, qui résiste au doute le plus radical.",
                     etape="Une intuition, non un raisonnement. Repère · intuitif / discursif", x=170, y=200, w=940),
        "prem": dict(type="liste", titre="La première vérité", items=[
            "Ni le monde, ni Dieu, ni les mathématiques", "La conscience que j'ai de moi-même : le sujet"],
                     marques=["✗", "✓"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ III. une chose qui pense
    dict(id="chose", chap="Une chose qui pense", fond="aube", humeur="calme", notions=["la raison", "la science"],
         retenir="Je suis une chose qui pense : penser, c'est tout ce dont j'ai conscience. Le morceau de cire : c'est l'esprit, non les sens, qui connaît les corps. L'esprit est plus facile à connaître que le corps.",
         beats=[
        "{tab_ver}{q_qui}Je suis. Mais que suis-je ? Pas un corps : j'ai pu douter d'en avoir un. "
        "Ce dont je ne peux pas douter, c'est de ma pensée.",
        "{-q_qui}",
        ("C", "Mais qu'est-ce donc que je suis ? une chose qui pense. Qu'est-ce qu'une chose qui pense ? c'est une chose qui doute, "
              "qui entend, qui conçoit, qui affirme, qui nie, qui veut, qui ne veut pas, qui imagine aussi, et qui sent.", "c_chose"),
        "{-c_chose}{pens}Note bien : pour Descartes, penser ne veut pas dire seulement raisonner. "
        "{pens.1}Douter, vouloir, imaginer, sentir : tout ce dont j'ai conscience est pensée. {pens.2}Penser, c'est avoir conscience.",
        "{-pens}{-tab_ver}{tab_ray}{cire}Pour aller plus loin, Descartes prend un objet tout simple : un morceau de cire, "
        "qui vient d'être tiré de la ruche. {cire.1}Il a encore le goût du miel, l'odeur des fleurs. "
        "Il est dur, froid ; si on frappe dessus, il rend un son.",
        "{-tab_ray}{tab_vei}{cire.2}Approchons-le du feu. L'odeur s'évapore, la couleur change, il devient liquide, chaud, "
        "il ne rend plus aucun son. {cire.3}Tout ce que mes sens en savaient a changé. Et pourtant… c'est la même cire.",
        ("Alors, qu'est-ce qui me le dit ?", {"pitch": "+2Hz"}),
        "{-cire}{ent}Pas mes yeux, ni mes mains : tout ce qu'ils percevaient a disparu. {ent.1}C'est mon entendement, "
        "la {#la raison}raison, qui saisit que la cire demeure. Une inspection de l'esprit, dit Descartes.",
        "{-ent}{-tab_vei}{tab_fen}{chap_m}Et c'est pareil pour les passants que je vois de ma fenêtre. Que vois-je, au juste ? "
        "{chap_m.1}Des chapeaux et des manteaux, qui pourraient cacher des automates. {chap_m.2}Mais je juge que ce sont des hommes.",
        "{-chap_m}D'où la conclusion de la deuxième méditation.",
        ("C", "Je vois clairement qu'il n'y a rien qui me soit plus facile à connaître que mon esprit.", "c_esprit"),
        "{-c_esprit}{dual}{dual.g}D'un côté, l'esprit, la chose qui pense : connu le premier, et le plus sûrement. "
        "{dual.d}De l'autre, le corps, la chose étendue : connu ensuite, et par l'esprit. On appelle cela le dualisme.",
        ("Et la conscience devient… transparente à elle-même. Retiens ce mot : c'est lui que l'on va mettre en doute.",
         {"rate": "-6%", "pitch": "-2Hz"}),
        "{-dual}{-tab_fen}",
    ], vis={
        "tab_ver": dict(type="tableau", img="t2-rembrandt", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .6, .45],
                        legende="Rembrandt, Philosophe en méditation, 1632 (musée du Louvre)"),
        "q_qui": dict(type="question", t="Je suis. Mais que suis-je ?"),
        "c_chose": dict(type="cit", a="Descartes", o="Méditations métaphysiques, II (1641 ; trad. 1647)", x=170, y=130, w=940),
        "pens": dict(type="def", cles=["conscience"], terme="Penser, selon Descartes",
                     t="Douter, vouloir, imaginer, sentir : tout ce dont j'ai conscience.",
                     etape="Penser, c'est avoir conscience.", x=170, y=200, w=940),
        "tab_ray": dict(type="tableau", img="cs2-rayon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Rayon de cire d'abeille (photo Migco, domaine public)"),
        "cire": dict(type="liste", titre="Le morceau de cire", items=[
            "Tiré de la ruche : goût de miel, odeur de fleurs, dur, froid, sonore",
            "Près du feu : liquide, chaud, sans odeur, sans son",
            "Tout a changé… et c'est la même cire"], marques=["1", "2", "→"], x=170, y=150, w=940),
        "tab_vei": dict(type="tableau", img="dv7-veilleuse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Georges de La Tour, La Madeleine à la veilleuse, vers 1640 (LACMA, Los Angeles)"),
        "ent": dict(type="def", cles=["entendement", "esprit"], terme="Une inspection de l'esprit",
                    t="Ce ne sont pas les sens, mais l'entendement qui saisit que la cire demeure.",
                    etape="Ce qui change, les qualités sensibles ; ce qui demeure, une chose étendue. Repère · essentiel / accidentel",
                    x=170, y=190, w=940),
        "tab_fen": dict(type="tableau", img="cs2-fenetre", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .55, .6],
                        legende="Gustave Caillebotte, Jeune homme à sa fenêtre, 1876 (Getty Museum, Los Angeles)"),
        "chap_m": dict(type="liste", titre="À la fenêtre", items=[
            "Je vois des chapeaux et des manteaux", "Je juge que ce sont des hommes"], marques=["1", "→"], x=170, y=190, w=940),
        "c_esprit": dict(type="cit", a="Descartes", o="Méditations métaphysiques, II (1641 ; trad. 1647)", x=170, y=200, w=940),
        "dual": dict(type="cols", g="L'esprit", gq="la chose qui pense : connue la première, et le plus sûrement",
                     d="Le corps", dq="la chose étendue : connue ensuite, par l'esprit", vs="≠"),
    }),

    # ------------------------------------------------------------------ IV. Locke
    dict(id="locke", chap="Locke : la mémoire et la personne", fond="nuit", humeur="calme", notions=["la justice", "le temps"],
         retenir="Locke : ce qui fait que je suis la même personne, ce n'est ni le corps ni une âme cachée, c'est la conscience, qui s'étend dans le passé par la mémoire. Objection de Reid : l'officier courageux.",
         beats=[
        "{locke}{tab_ess}Je suis une chose qui pense, soit. Mais suis-je la même qu'il y a dix ans ? "
        "{plus2}Un demi-siècle après Descartes, l'Anglais John Locke pose la question dans son Essai sur l'entendement humain, en 1690.",
        "{-locke}{-tab_ess}{-plus2}{tab_rj}{ident}Regarde ces deux visages. {ident.1}À vingt-deux ans, Rembrandt se peint, jeune et inquiet. "
        "{-tab_rj}{tab_rv}{ident.2}À soixante-trois ans, le même peintre, quelques mois avant sa mort. "
        "Pas un trait n'est resté identique. Est-ce la même personne ?",
        "{-ident}{rep_loc}La réponse de Locke est neuve. {rep_loc.1}Ce n'est pas le corps qui fait la personne : il change sans cesse. "
        "{rep_loc.2}Ce n'est pas non plus une âme cachée, dont nous ne savons rien. "
        "{rep_loc.3}C'est la conscience. Je suis la même personne aussi loin que ma conscience peut remonter dans le passé, "
        "par la mémoire.",
        "{-rep_loc}{-tab_rv}{tab_pri}{pc}Locke invente alors une petite fiction. {pc.1}Imagine que l'âme d'un prince, "
        "avec tous les souvenirs de sa vie de prince, passe dans le corps d'un savetier, {-tab_pri}{tab_cor}un cordonnier, "
        "dont l'âme vient de partir. {pc.2}Qui est cet homme qui se réveille dans l'échoppe ? Pour tout le monde, c'est le savetier. "
        "Mais pour Locke, c'est le prince : il en a la conscience.",
        "{-pc}{-tab_cor}{tab_jus}{forens}Et l'enjeu n'est pas seulement théorique. Pour Locke, la personne est d'abord une affaire "
        "de {#la justice}justice. {forens.1}On ne peut répondre que des actes dont on peut avoir conscience. "
        "{forens.2}Punir quelqu'un pour ce qu'il ne sait pas avoir fait, ce serait comme punir un jumeau pour la faute de son frère.",
        "{-forens}{reid}Mais un philosophe écossais, Thomas Reid, a trouvé la faille. {reid.1}Un petit garçon est fouetté "
        "pour avoir volé des pommes. {reid.2}Devenu jeune officier, il se souvient de cette punition, le jour où il prend un drapeau "
        "à l'ennemi. {reid.3}Vieux général, il se souvient de sa bravoure… mais il a tout oublié du verger.",
        ("Selon Locke, le général est l'officier, l'officier est l'enfant… mais le général n'est pas l'enfant. Absurde.",
         {"rate": "-5%"}),
        "{-reid}{-tab_jus}",
    ], vis={
        "locke": dict(type="portrait", annee=1632, img="locke", nom="John Locke", dates="1632 – 1704",
                      legende="Essai sur l'entendement humain (1690)", x=110, y=120, w=330, h=420),
        "tab_ess": dict(type="tableau", img="cs2-essai", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Locke, An Essay Concerning Humane Understanding, Londres, 1690, page de titre"),
        "plus2": dict(type="tag", style="plus", t="Pour aller plus loin", x=640, y=560, w=420),
        "tab_rj": dict(type="tableau", img="cs2-rembrandt-jeune", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                       legende="Rembrandt, Autoportrait, vers 1628 (Rijksmuseum, Amsterdam)"),
        "tab_rv": dict(type="tableau", img="cs2-rembrandt-vieux", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.25, .5, .3],
                       legende="Rembrandt, Autoportrait à l'âge de 63 ans, 1669 (National Gallery, Londres)"),
        "ident": dict(type="liste", titre="La même personne ?", items=[
            "Rembrandt à 22 ans", "Rembrandt à 63 ans"], marques=["1", "2"], x=640, y=200, w=570),
        "rep_loc": dict(type="liste", titre="Qu'est-ce qui fait la personne ?", items=[
            "Le corps ? Il change sans cesse", "Une âme cachée ? Nous n'en savons rien",
            "La conscience, qui remonte le passé par la mémoire"], marques=["✗", "✗", "✓"], x=170, y=150, w=940),
        "tab_pri": dict(type="tableau", img="cs2-prince", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.25, .6, .3],
                        legende="Diego Velázquez, Le Prince Baltasar Carlos avec un nain, 1631 (Museum of Fine Arts, Boston)"),
        "tab_cor": dict(type="tableau", img="cs2-cordonnier", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .35, .45],
                        legende="David Ryckaert III, L'Atelier du cordonnier, XVIIᵉ siècle (Rijksmuseum, Amsterdam)"),
        "pc": dict(type="liste", titre="Le prince et le savetier", items=[
            "L'âme du prince, avec ses souvenirs, passe dans le corps du savetier",
            "Le même homme pour tous… mais la personne du prince"], marques=["1", "→"], x=170, y=170, w=940),
        "tab_jus": dict(type="tableau", img="dv4-justitia", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Pieter Bruegel l'Ancien (d'après), La Justice, gravure, 1559 (Rijksmuseum, CC0)"),
        "forens": dict(type="liste", titre="La personne : une affaire de justice", items=[
            "On ne répond que des actes dont on peut avoir conscience",
            "Sinon, ce serait punir un jumeau pour la faute de son frère"], marques=["1", "2"], x=170, y=180, w=940),
        "reid": dict(type="liste", titre="L'objection de Reid (1785)", items=[
            "L'enfant fouetté pour des pommes volées", "L'officier se souvient de l'enfant",
            "Le général se souvient de l'officier… pas de l'enfant"], marques=["1", "2", "3"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ V. Hume
    dict(id="hume", chap="Hume : un faisceau de perceptions", fond="aube", humeur="mystere", notions=["la science", "le temps"],
         retenir="Hume : quand je rentre en moi-même, je ne trouve jamais un moi, seulement des perceptions. Le moi est un faisceau de perceptions ; son identité, une fiction de l'imagination.",
         beats=[
        "{hume}{tab_edi}Et si, à force de chercher ce moi qui dure, on ne trouvait… rien ? En 1739, à moins de trente ans, "
        "l'Écossais David Hume publie son Traité de la nature humaine. Il veut faire de l'esprit humain une {#la science}science "
        "d'observation, comme Newton l'a fait pour la nature.",
        "Alors il observe. Il rentre en lui-même, et il cherche ce fameux moi.",
        ("C", "Pour moi, quand je pénètre le plus intimement dans ce que j'appelle moi-même, je tombe toujours sur une perception "
              "particulière ou sur une autre, de chaud ou de froid, de lumière ou d'ombre, d'amour ou de haine, "
              "de douleur ou de plaisir.", "c_hume"),
        "{-c_hume}{-hume}{-tab_edi}{tab_dra}{fais}Jamais un moi tout seul : {fais.1}toujours une sensation, une image, une émotion. "
        "{fais.2}Retire-les toutes, comme dans le sommeil profond, et il ne reste… rien. "
        "{fais.3}Le moi n'est donc qu'un faisceau de perceptions, qui se succèdent avec une rapidité inconcevable, "
        "dans un flux perpétuel.",
        "{-fais}{theat}Hume le compare à un théâtre, où les perceptions entrent, passent, repassent et se mêlent. "
        "{theat.1}Mais attention, ajoute-t-il : il n'y a pas de théâtre. Seulement la pièce qui se joue.",
        "{-theat}{-tab_dra}{tab_tem}{nav}Pourquoi croyons-nous alors à un moi identique ? Par habitude. Comme pour un navire "
        "dont on remplace, réparation après réparation, presque toutes les pièces : {nav.1}on continue de dire que c'est le même. "
        "{nav.2}L'identité du moi serait une fiction de l'imagination, qui relie ce qui change lentement.",
        "{-nav}{comp}{comp.g}Descartes : je suis une chose qui pense, une substance qui demeure. "
        "{comp.d}Hume : il n'y a que des pensées qui passent, sans personne derrière.",
        ("Alors, la conscience nous fait-elle vraiment connaître ce que nous sommes ?", {"rate": "-6%"}),
        "{-comp}{-tab_tem}",
    ], vis={
        "hume": dict(type="portrait", annee=1711, img="hume", nom="David Hume", dates="1711 – 1776",
                     legende="Traité de la nature humaine (1739)", x=110, y=120, w=330, h=420),
        "tab_edi": dict(type="tableau", img="cs2-edimbourg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Alexander Nasmyth, Édimbourg vu de Calton Hill, début du XIXᵉ siècle (City Art Centre, Édimbourg)"),
        "c_hume": dict(type="cit", a="Hume", o="Traité de la nature humaine, I, IV, 6 (1739), trad. courante", x=640, y=120, w=570),
        "tab_dra": dict(type="tableau", img="cs2-drame", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .4],
                        legende="Honoré Daumier, Le Drame, vers 1860 (Neue Pinakothek, Munich)"),
        "fais": dict(type="liste", titre="Ce que je trouve en moi", items=[
            "Toujours une perception : chaud, froid, amour, douleur…", "Sans perceptions, plus rien",
            "Le moi : un faisceau de perceptions, en flux perpétuel"], marques=["1", "2", "→"], x=170, y=150, w=940),
        "theat": dict(type="note", titre="Le théâtre de l'esprit", cles=["théâtre", "pièce"],
                      t="Les perceptions entrent, passent, repassent et se mêlent.",
                      etape="Mais il n'y a pas de théâtre : seulement la pièce qui se joue.", x=170, y=190, w=940),
        "tab_tem": dict(type="tableau", img="dv7-temeraire", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .35, .45],
                        legende="J. M. W. Turner, Le Dernier Voyage du Téméraire, 1839 (National Gallery, Londres)"),
        "nav": dict(type="liste", titre="Le navire réparé", items=[
            "On remplace presque toutes les pièces… et on le dit « le même »",
            "L'identité du moi : une fiction de l'imagination"], marques=["1", "→"], x=170, y=180, w=940),
        "comp": dict(type="cols", g="Descartes", gq="une chose qui pense : une substance qui demeure", d="Hume",
                     dq="des perceptions qui passent, sans personne derrière", vs="≠"),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ret}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : le doute méthodique. Les sens, le rêve, le malin génie : "
        "Descartes doute de tout pour trouver une certitude.",
        "{rec.2}Deux : le cogito. Je pense, donc je suis. La première vérité est celle de la conscience ; "
        "et, le morceau de cire le montre, l'esprit est plus facile à connaître que le corps.",
        "{rec.3}Trois : Locke. La personne, c'est la conscience qui s'étend par la mémoire : le prince dans le corps du savetier.",
        "{rec.4}Quatre : Hume. En moi, je ne trouve que des perceptions : le moi est un faisceau.",
        "{-rec}{-tab_ret}{tab_fin}{q_suite}Descartes pensait que rien ne m'est plus facile à connaître que mon esprit. "
        "Et s'il y avait en moi des pensées… que je ne connais pas ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : la conscience est-elle transparente ? Leibniz, Freud, et Nietzsche.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ret": dict(type="tableau", img="cs2-dam", fond=True, sombre=True, de=[1.3, .6, .5], a=[1.0, .5, .5],
                        legende="Gerrit Berckheyde, L'Hôtel de ville sur le Dam, Amsterdam, 1672 (Rijksmuseum)"),
        "rec": dict(type="carte", centre="JE PENSE, DONC JE SUIS", branches=[
            dict(t="Le doute", items=["les sens, le rêve", "le malin génie", "volontaire, radical, provisoire"]),
            dict(t="Le cogito", items=["première vérité", "une chose qui pense", "le morceau de cire"]),
            dict(t="Locke", items=["la personne = la conscience", "la mémoire", "le prince et le savetier"]),
            dict(t="Hume", items=["toujours une perception", "un faisceau", "l'identité, une fiction"])]),
        "tab_fin": dict(type="tableau", img="bh4-vague", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .35, .4],
                        legende="Katsushika Hokusai, La Grande Vague de Kanagawa, vers 1831 (estampe)"),
        "q_suite": dict(type="question", t="Et s'il y avait en moi des pensées que je ne connais pas ?"),
        "fin": dict(type="titre", sur="À suivre", t="La conscience est-elle transparente ?",
                    sous="Épisode 3 · Leibniz, Freud, Nietzsche"),
    }),
]

QUIZ = [
    dict(q="Pourquoi Descartes doute-t-il de ce que lui apprennent les sens ?",
         r=["Parce qu'ils nous trompent parfois, et qu'il n'est pas prudent de s'y fier",
            "Parce qu'ils n'existent pas", "Parce que la religion le lui interdit", "Parce qu'il est aveugle"], ok=0,
         voir="raisons", ex="Le crayon dans l'eau paraît brisé, la tour carrée paraît ronde : on ne se fie pas à qui nous a trompés une fois."),
    dict(q="Quel est le rôle de l'hypothèse du malin génie ?",
         r=["Prouver que Dieu existe", "Pousser le doute jusqu'aux vérités mathématiques",
            "Expliquer les rêves", "Montrer que les animaux pensent"], ok=1,
         voir="c_genie", ex="Méditations, I : un trompeur tout-puissant pourrait me tromper même quand je calcule. Le doute devient radical."),
    dict(q="Le doute de Descartes est dit « méthodique » parce qu'il est…",
         r=["définitif et désespéré", "volontaire, radical et provisoire", "fondé sur la foi", "limité aux sens"], ok=1,
         voir="dm", ex="Il ne doute pas pour douter, comme le sceptique : il vide le panier pour ne garder que les pommes saines."),
    dict(q="Pourquoi le cogito résiste-t-il même au malin génie ?",
         r=["Parce que le malin génie n'existe pas", "Parce que, pour être trompé, il faut être : je pense, donc je suis",
            "Parce que les mathématiques sont certaines", "Parce que Dieu est bon"], ok=1,
         voir="c_trompe", ex="« Qu'il me trompe tant qu'il voudra, il ne saura jamais faire que je ne sois rien, tant que je penserai être quelque chose. »"),
    dict(q="Que montre l'analyse du morceau de cire ?",
         r=["Que les sens nous font connaître l'essence des corps", "Que c'est l'esprit, et non les sens, qui saisit ce qu'est la cire",
            "Que la cire n'existe pas", "Que le corps est plus facile à connaître que l'esprit"], ok=1,
         voir="ent", ex="Toutes les qualités sensibles changent, la cire demeure : c'est une inspection de l'esprit. D'où : rien n'est plus facile à connaître que mon esprit."),
    dict(q="Pour Locke, qu'est-ce qui fait que je suis la même personne au fil du temps ?",
         r=["Mon corps", "Une âme invisible", "La conscience, qui s'étend dans le passé par la mémoire", "Mon nom"], ok=2,
         voir="rep_loc", ex="Essai, II, 27 : le prince qui passe, avec ses souvenirs, dans le corps du savetier reste le prince. Reid objectera l'officier courageux."),
    dict(q="Que trouve Hume quand il « rentre en lui-même » ?",
         r=["Un moi simple et permanent", "Toujours une perception particulière, jamais un moi", "Dieu", "Rien du tout, jamais"], ok=1,
         voir="c_hume", ex="Traité, I, IV, 6 : le moi n'est qu'un faisceau de perceptions en flux perpétuel ; son identité est une fiction de l'imagination."),
]

CREDITS = [
    "Portraits : René Descartes (d'après Frans Hals) ; John Locke (Godfrey Kneller, 1697) ; David Hume (Allan Ramsay, 1766) : domaine public",
    "Tableaux : Raphaël, Le Songe du chevalier (vers 1504) ; Lu Zhi, Tchouang-tseu rêvant d'un papillon (XVIᵉ s.) ; "
    "Gerrit Berckheyde, L'Hôtel de ville sur le Dam (1672) ; Rembrandt, Philosophe en méditation (1632), Autoportrait (vers 1628) "
    "et Autoportrait à 63 ans (1669) ; Georges de La Tour, La Madeleine à la veilleuse (vers 1640) ; Gustave Caillebotte, "
    "Jeune homme à sa fenêtre (1876) ; Diego Velázquez, Le Prince Baltasar Carlos avec un nain (1631) ; David Ryckaert III, "
    "L'Atelier du cordonnier ; Alexander Nasmyth, Édimbourg vu de Calton Hill ; Honoré Daumier, Le Drame (vers 1860) ; "
    "J. M. W. Turner, Le Dernier Voyage du Téméraire (1839) ; Katsushika Hokusai, La Grande Vague (vers 1831) : domaine public",
    "Gravures et documents : Gustave Doré, Satan (Paradis perdu, 1866) ; Archimède et son levier (Mechanics Magazine, 1824) ; "
    "Bruegel (d'après), La Justice (1559, Rijksmuseum, CC0) ; pages de titre du Discours de la méthode (1637), des Meditationes (1641), "
    "de l'Essay de Locke (1690) : domaine public",
    "Photographies : un crayon dans un verre d'eau (Meganbeckett27, CC BY-SA 3.0) ; rayon de cire (Migco, domaine public) ; "
    "salle d'examen (domaine public)",
    "Citations : Descartes, Discours de la méthode (1637) et Méditations métaphysiques (trad. Luynes, 1647) ; "
    "Hume, Traité de la nature humaine (1739), traduction courante. Tchouang-tseu, Locke, Reid sont résumés par le narrateur.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
