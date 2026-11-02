"""La conscience, épisode 3 : « La conscience est-elle transparente ? »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la nature} dans le texte lu.
Citations : Leibniz, Nouveaux Essais sur l'entendement humain, préface (écrits en 1704, publiés en 1765), texte français
de Leibniz ; Freud, Métapsychologie, « L'inconscient » (1915), trad. courante, citation courte ; Nietzsche, Le Gai Savoir,
§ 11 et § 354 (1882-1887), trad. Henri Albert (1901), vérifiées sur Wikisource.
Résumés par le narrateur : l'oubli du nom de Signorelli (Psychopathologie de la vie quotidienne, 1901) ; l'antichambre,
le salon et le gardien (Introduction à la psychanalyse, 19ᵉ leçon, 1917) ; le cavalier et le cheval (Le Moi et le Ça,
1923) ; « là où était le ça, le moi doit advenir » (Nouvelles conférences, 1933) ; Alain (Éléments de philosophie, 1916,
et Propos) : la critique de l'inconscient comme « autre moi ».
"""

CODE = "conscience-3"
NOTION = "La conscience"
NUM = 3
TITRE = "La conscience est-elle transparente ?"
SUIVANT = "Épisode 4 · Conscience, monde et autrui"
PRONONCIATION = {"Nietzsche": "Nitche", "Leibniz": "Laïbnitz", "Signorelli": "Signorèlli", "Boltraffio": "Boltrafio",
                 "Orvieto": "Orviéto", "Chartier": "Chartié"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_int}{q_pluie}Tu révises dans ta chambre. Dehors, la pluie tombe depuis une heure. Tu lis, tu prends des notes. "
        "Et soudain, la pluie s'arrête.",
        ("Et tu entends… le silence.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-q_pluie}{pluie}Étrange. {pluie.1}Pendant une heure, ce bruit était là, et tu ne l'entendais pas. "
        "{pluie.2}Pourtant, tu l'entendais bien un peu : sinon, comment remarquerais-tu qu'il s'est tu ?",
        "{-pluie}{q_tout}Alors, ta conscience te dit-elle tout ce qui se passe en toi ?",
        "{-q_tout}{trans}Dans l'épisode précédent, Descartes affirmait que rien ne m'est plus facile à connaître que mon esprit. "
        "Une conscience transparente, qui verrait tout d'elle-même, jusqu'au fond.",
        "{-trans}{trois_s}Aujourd'hui, trois penseurs vont troubler cette eau claire. {trois_s.1}Un mathématicien, "
        "{trois_s.2}un médecin, {trois_s.3}et un philologue qui philosophait à coups de marteau.",
        ("P", 0.3),
        "{-trois_s}{-tab_int}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_int": dict(type="tableau", img="cs3-interieur", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .4],
                        legende="Vilhelm Hammershøi, Intérieur, Strandgade 30, 1900 (domaine public)"),
        "q_pluie": dict(type="question", t="La pluie s'arrête… et tu entends le silence."),
        "pluie": dict(type="liste", titre="Un bruit qu'on n'entendait pas", items=[
            "Pendant une heure, tu ne l'entendais pas", "Pourtant tu remarques qu'il s'est tu"],
                      marques=["?", "!"], x=170, y=190, w=940),
        "q_tout": dict(type="question", t="Ta conscience te dit-elle tout ce qui se passe en toi ?"),
        "trans": dict(type="mot", t="Transparente ?", g="Descartes : rien ne m'est plus facile à connaître que mon esprit",
                      y=260, taille=104),
        "trois_s": dict(type="nuage", items=["un mathématicien", "un médecin", "un philologue"]),
        "titre": dict(type="titre", sur="La conscience · Épisode 3", t="La conscience est-elle transparente ?",
                      sous="Leibniz, Freud, Nietzsche… et Alain"),
    }),

    # ------------------------------------------------------------------ I. Leibniz
    dict(id="leibniz", chap="Leibniz : les petites perceptions", fond="aube", humeur="calme", notions=["l'inconscient", "la nature"],
         retenir="Leibniz : à tout moment, une infinité de petites perceptions, sans aperception. Le bruit de la mer est fait du bruit de chaque vague, que je n'entends pas séparément.",
         beats=[
        "{leib}{tab_vag}Le premier, c'est Leibniz : mathématicien, inventeur du calcul infinitésimal, diplomate, philosophe. "
        "Vers 1704, il lit l'Essai de Locke, celui de l'épisode précédent, et lui répond page après page, "
        "dans les Nouveaux Essais sur l'entendement humain.",
        "Leibniz écrit ce livre en français, la langue savante de l'Europe d'alors. "
        "Locke, comme Descartes, pensait qu'il n'y a pas de pensée sans conscience. Leibniz répond : si, il y en a. "
        "Et il en donne une preuve restée célèbre. Écoute la mer.",
        ("C", "Pour entendre ce bruit comme l'on fait, il faut bien qu'on entende les parties qui composent ce tout, "
              "c'est-à-dire les bruits de chaque vague…", "c_mer"),
        "{-c_mer}{-leib}{mer}Chaque vague, seule, je ne l'entendrais pas. {mer.1}Et pourtant, il faut bien qu'elle m'affecte un peu. "
        "{mer.2}Sinon, cent mille vagues ne feraient aucun bruit, {mer.3}car, dit Leibniz, cent mille riens ne sauraient "
        "faire quelque chose.",
        "{-mer}{-tab_vag}{tab_mou}{acc}Même chose pour celui qui habite près d'un moulin, ou d'une chute d'eau. "
        "{acc.1}À force d'habitude, il ne prend plus garde au bruit. {acc.2}Mais le bruit frappe toujours ses oreilles, "
        "et quelque chose, en lui, y répond. Ta pluie de tout à l'heure, en somme.",
        "{-acc}{appel}Autre exemple, tiré du même texte. {appel.1}Tu es absorbé par un jeu, quelqu'un te parle, tu ne réagis pas. "
        "{appel.2}Deux secondes plus tard, tu lèves la tête : quoi ? Et pourtant, tu peux répéter ce qu'on t'a dit. "
        "Tu l'avais donc perçu… sans t'en apercevoir.",
        "{-appel}{pa}D'où une distinction capitale. {pa.g}La perception : tout ce qui m'affecte, même sans que j'y prenne garde. "
        "{pa.d}L'aperception : la perception dont j'ai conscience, que je remarque, sur laquelle je peux réfléchir.",
        "{-pa}{-tab_mou}{tab_vag2}{petites}Il y a donc en nous, à chaque instant, une infinité de petites perceptions. "
        "{petites.1}Elles sont trop petites, ou trop nombreuses, pour être distinguées. {petites.2}Mais elles agissent : "
        "elles font nos goûts, nos humeurs, nos inquiétudes sans raison apparente. Et la conscience naît d'elles par degrés, "
        "car, dit Leibniz, la {#la nature}nature ne fait jamais de sauts.",
        "{-petites}{cont}Retiens bien la nuance. {cont.1}Leibniz est le premier à penser une vie de l'esprit sans conscience. "
        "{cont.2}Mais chez lui, rien de menaçant : entre l'obscur et le clair, il y a une continuité, comme entre la nuit et l'aube.",
        "{-cont}{-tab_vag2}",
    ], vis={
        "leib": dict(type="portrait", annee=1646, img="leibniz", nom="Gottfried Wilhelm Leibniz", dates="1646 – 1716",
                     legende="Nouveaux Essais sur l'entendement humain (1704, publiés en 1765)", x=110, y=120, w=330, h=420),
        "tab_vag": dict(type="tableau", img="cs3-vague", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .45, .6],
                        legende="Gustave Courbet, La Vague, vers 1869 (domaine public)"),
        "c_mer": dict(type="cit", a="Leibniz", o="Nouveaux Essais sur l'entendement humain, préface (1704)", x=640, y=170, w=570),
        "mer": dict(type="liste", titre="Le bruit de la mer", items=[
            "Chaque vague m'affecte un peu, sans que je l'entende seule", "Sinon, cent mille vagues ne feraient aucun bruit",
            "« Cent mille riens ne sauraient faire quelque chose »"], marques=["1", "2", "→"], x=170, y=150, w=940),
        "tab_mou": dict(type="tableau", img="cs3-moulin", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .65, .4],
                        legende="Jacob van Ruisdael, Le Moulin de Wijk bij Duurstede, vers 1670 (Rijksmuseum, Amsterdam)"),
        "acc": dict(type="liste", titre="Le moulin, la chute d'eau", items=[
            "L'habitude : on ne prend plus garde au bruit", "Mais le bruit nous affecte toujours"],
                    marques=["1", "2"], x=170, y=190, w=940),
        "pa": dict(type="cols", g="Perception", gq="tout ce qui m'affecte, même sans que j'y prenne garde",
                   d="Aperception", dq="la perception dont j'ai conscience, que je remarque", vs="≠"),
        "appel": dict(type="liste", titre="On te parle, tu es absorbé", items=[
            "Sur le moment, tu ne réagis pas", "Deux secondes plus tard, tu peux répéter ce qu'on t'a dit"],
                      marques=["1", "2"], x=170, y=190, w=940),
        "cont": dict(type="cols", g="Leibniz", gq="une vie de l'esprit sans conscience", d="Mais",
                     dq="sans conflit : une continuité de l'obscur au clair", vs="→"),
        "tab_vag2": dict(type="tableau", img="cs3-vague", fond=True, sombre=True, de=[1.3, .3, .5], a=[1.05, .5, .5],
                         legende="Gustave Courbet, La Vague, vers 1869 (domaine public)"),
        "petites": dict(type="def", cles=["petites perceptions", "agissent"], terme="Les petites perceptions",
                        t="Une infinité de perceptions, trop petites ou trop nombreuses pour être remarquées.",
                        etape="Elles agissent : goûts, humeurs, inquiétudes. La conscience naît d'elles par degrés.",
                        x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. Freud : l'hypothèse
    dict(id="freud", chap="Freud : l'hypothèse de l'inconscient", fond="nuit", humeur="tension", notions=["l'inconscient", "la science"],
         retenir="Freud : les données de la conscience sont lacunaires. Oublis, lapsus, rêves supposent des pensées refoulées : l'inconscient est une hypothèse nécessaire et légitime.",
         beats=[
        "{freud}{tab_ber}Deux siècles plus tard, à Vienne, un médecin va beaucoup plus loin : Sigmund Freud. "
        "On l'a vu dans la série sur la liberté : {rapp}{rapp.1}les trois blessures de l'amour-propre, {rapp.2}le lapsus, "
        "{rapp.3}et cette phrase : le moi n'est pas maître dans sa propre maison.",
        "{-rapp}Aujourd'hui, allons plus loin. Les petites perceptions de Leibniz étaient simplement trop faibles pour être remarquées. "
        "L'inconscient de Freud, lui, n'est pas faible : il est {!refoulé}refoulé. Tenu à l'écart, activement, parce qu'il dérange.",
        "{-freud}{-tab_ber}{tab_sig}{sig}Un exemple, raconté par Freud lui-même. {sig.1}En voyage, il veut citer le peintre "
        "des fresques d'Orvieto, celles-ci. Impossible de retrouver son nom. {sig.2}Il lui vient Botticelli, Boltraffio… "
        "jamais le bon. {sig.3}Le nom était Signorelli. Et en remontant le fil, Freud découvre que l'oubli touchait "
        "des pensées qu'il voulait écarter : la mort, et la sexualité.",
        "{-sig}{-tab_sig}{tab_tra}{lac}Voilà l'argument. {lac.1}Les données de la conscience sont pleines de trous : "
        "un nom oublié, un mot qui en remplace un autre, un rêve absurde, une idée qui surgit d'on ne sait où. "
        "{lac.2}Pour que ces trous prennent un sens, il faut supposer des pensées que la conscience ne voit pas.",
        "{-lac}",
        ("C", "L'hypothèse de l'inconscient est nécessaire et légitime.", "c_hyp"),
        "{-c_hyp}{hyp}{hyp.1}Nécessaire : sans elle, ces trous resteraient inexplicables. "
        "{hyp.2}Légitime : on ne fait rien d'autre, remarque Freud, quand on prête une conscience aux autres. "
        "On ne la voit jamais ; on la suppose, d'après ce qu'ils font. C'est une hypothèse, comme en {#la science}science.",
        "{-hyp}{pop}Pour aller plus loin, une objection célèbre. {pop.1}Au vingtième siècle, le philosophe Karl Popper remarque "
        "que la psychanalyse explique tout : que le patient accepte l'interprétation, ou qu'il la refuse… c'est encore la résistance. "
        "{pop.2}Or une théorie qu'aucun fait ne peut jamais démentir est-elle encore une science ?",
        "{-pop}{-tab_tra}",
    ], vis={
        "pop": dict(type="liste", titre="L'objection de Popper", items=[
            "La psychanalyse explique tout, même le refus de l'interprétation",
            "Une théorie qu'aucun fait ne peut démentir est-elle une science ?"], marques=["1", "?"], x=170, y=180, w=940, plus=True),
        "freud": dict(type="portrait", annee=1856, img="freud", nom="Sigmund Freud", dates="1856 – 1939",
                      legende="Métapsychologie (1915)", x=110, y=120, w=330, h=420),
        "tab_ber": dict(type="tableau", img="bh4-berggasse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Plaque au 19, Berggasse, Vienne, où Freud vécut de 1891 à 1938 (photo GuentherZ, CC BY 3.0)"),
        "rapp": dict(type="liste", titre="Vu dans la série sur la liberté", items=[
            "Les trois blessures : Copernic, Darwin, Freud", "Le lapsus, le rêve, l'acte manqué",
            "« Le moi n'est pas maître dans sa propre maison »"], marques=["1", "2", "3"], x=640, y=170, w=570),
        "tab_sig": dict(type="tableau", img="cs3-signorelli", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .6],
                        legende="Luca Signorelli, Les Damnés, fresque, 1499-1502 (cathédrale d'Orvieto)"),
        "sig": dict(type="liste", titre="L'oubli d'un nom (Freud, 1901)", items=[
            "Le peintre des fresques d'Orvieto ? Impossible de s'en souvenir", "Botticelli ? Boltraffio ?",
            "Signorelli : un oubli lié à des pensées écartées"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_tra": dict(type="tableau", img="cs3-traumdeutung", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .3],
                        legende="Freud, Die Traumdeutung (L'Interprétation du rêve), Vienne, 1900 (daté 1900, paru fin 1899)"),
        "lac": dict(type="liste", titre="Les trous de la conscience", items=[
            "Un nom oublié, un lapsus, un rêve absurde, une idée qui surgit",
            "Pour leur donner un sens : supposer des pensées inconscientes"], marques=["?", "→"], x=170, y=180, w=940),
        "c_hyp": dict(type="cit", a="Freud", o="Métapsychologie, « L'inconscient » (1915), trad. courante", x=170, y=220, w=940),
        "hyp": dict(type="liste", titre="Une hypothèse", items=[
            "Nécessaire : sans elle, ces trous restent inexplicables",
            "Légitime : la conscience des autres, on la suppose aussi"], marques=["1", "2"],
                    cles=["Nécessaire", "Légitime"], x=170, y=190, w=940),
    }),

    # ------------------------------------------------------------------ III. les deux topiques
    dict(id="topiques", chap="Les deux topiques", fond="aube", humeur="mystere", notions=["l'inconscient", "le devoir"],
         retenir="Première topique : inconscient, préconscient, conscient (l'antichambre, le gardien, le salon). Seconde topique : le ça, le moi, le surmoi. Le moi, cavalier d'un cheval plus fort que lui.",
         beats=[
        "{tab_hm}{top1}Pour se représenter l'esprit, Freud dessine des cartes. Il les appelle des topiques, du grec topos, le lieu. "
        "{top1.1}La première distingue trois lieux : l'inconscient, le préconscient, et le conscient.",
        "{-top1}{anti}Il en donne une image. {anti.1}Imagine une grande antichambre, où se bousculent les désirs, comme une foule. "
        "{anti.2}Sur le seuil, un gardien examine chacun, et repousse ceux qui lui déplaisent. "
        "{anti.3}À côté, un salon plus étroit, où se tient la conscience. Ceux qui y entrent ne sont pas aussitôt aperçus : "
        "ils attendent d'être remarqués. C'est le préconscient.",
        "{-anti}{-tab_hm}{tab_cau}{cens}Ce gardien, c'est la censure. {cens.1}La nuit, il somnole un peu. Les désirs refoulés "
        "en profitent, mais déguisés, pour ne pas être reconnus : c'est le rêve, que Freud appelle la voie royale vers l'inconscient.",
        "{-cens}{-tab_cau}{tab_top}{top2}En 1923, Freud propose une seconde carte. {top2.1}Le ça : le réservoir des pulsions, "
        "qui ne connaît ni le temps, ni la contradiction, ni la morale. {top2.2}Le surmoi : les interdits des parents "
        "et de la société, devenus une voix intérieure, sévère, une sorte de {#le devoir}conscience morale. "
        "{top2.3}Et, entre les deux, le moi, qui doit composer avec eux… et avec la réalité.",
        "{-top2}{voix}Tu connais cette petite voix qui te reproche d'avoir mangé le dernier gâteau, même quand personne ne t'a vu ? "
        "{voix.1}Pour Freud, elle n'est pas tombée du ciel : c'est celle de tes parents, devenue la tienne. "
        "Nous la retrouverons dans l'épisode cinq, consacré à la conscience morale.",
        "{-voix}{-tab_top}{tab_cav}{cav}Freud compare le moi à un cavalier. {cav.1}Il doit tenir un cheval bien plus fort que lui. "
        "{cav.2}Et souvent, il ne lui reste qu'à le conduire là où le cheval veut aller.",
        ("La conscience n'est plus la maîtresse de maison. Elle n'en est qu'une pièce.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-cav}{-tab_cav}",
    ], vis={
        "tab_hm": dict(type="tableau", img="cs3-interieur", fond=True, sombre=True, de=[1.3, .7, .5], a=[1.05, .5, .5],
                       legende="Vilhelm Hammershøi, Intérieur, Strandgade 30, 1900 (domaine public)"),
        "top1": dict(type="liste", titre="La première topique (1900)", items=[
            "Trois lieux : l'inconscient, le préconscient, le conscient"], marques=["1"], x=170, y=200, w=940),
        "anti": dict(type="liste", titre="L'antichambre et le salon", items=[
            "L'antichambre : les désirs se bousculent (l'inconscient)",
            "Le gardien sur le seuil : il repousse ce qui déplaît (la censure)",
            "Le salon : ils attendent d'être remarqués (le préconscient), devant la conscience"],
                     marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_cau": dict(type="tableau", img="t3-cauchemar", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Johann Heinrich Füssli, Le Cauchemar, 1781"),
        "cens": dict(type="def", cles=["censure", "déguisés"], terme="La censure et le rêve",
                     t="Le gardien qui repousse les désirs gênants hors de la conscience.",
                     etape="La nuit, il somnole : les désirs passent, déguisés. Le rêve, voie royale vers l'inconscient.",
                     x=170, y=200, w=940),
        "tab_top": dict(type="tableau", img="cs3-topique", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .5],
                        legende="Freud, schéma du moi (Ich) et du ça (Es), Le Moi et le Ça, 1923"),
        "top2": dict(type="liste", titre="La seconde topique (1923)", items=[
            "Le ça : les pulsions, sans temps, sans contradiction, sans morale",
            "Le surmoi : les interdits intériorisés, une voix sévère",
            "Le moi : entre les deux, et face à la réalité"], marques=["1", "2", "3"],
                     cles=["ça", "surmoi", "moi"], x=170, y=150, w=940),
        "voix": dict(type="note", titre="Le surmoi au quotidien", cles=["voix", "parents"],
                     t="La petite voix qui te reproche le dernier gâteau, même sans témoin.",
                     etape="Pour Freud : la voix des parents, devenue la tienne (voir l'épisode 5).", x=170, y=200, w=940),
        "tab_cav": dict(type="tableau", img="cs3-cavalier", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Théodore Géricault, Officier de chasseurs à cheval chargeant, 1812 (musée du Louvre)"),
        "cav": dict(type="note", titre="Le cavalier et le cheval", cles=["cavalier", "cheval"],
                    t="Le moi doit tenir un cheval plus fort que lui : le ça.",
                    etape="Souvent, il le conduit là où le cheval veut aller.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. Nietzsche
    dict(id="nietzsche", chap="Nietzsche : une conscience de surface", fond="nuit", humeur="tension", notions=["le langage", "la vérité"],
         retenir="Nietzsche : la conscience est le plus tardif et le moins achevé de nos organes ; elle s'est développée pour communiquer. Ce qui devient conscient devient superficiel et commun.",
         beats=[
        "{nietz}{tab_sil}Le troisième soupçon est le plus radical. Friedrich Nietzsche, philologue devenu philosophe, "
        "écrit Le Gai Savoir dans les années 1880, entre l'Italie et les montagnes suisses de Sils-Maria. "
        "Pour lui, nous surestimons de beaucoup notre conscience.",
        ("C", "Le conscient est l'évolution dernière et tardive du système organique, et par conséquent aussi ce qu'il y a "
              "dans ce système de moins achevé et de moins fort.", "c_tard"),
        "{-c_tard}{-nietz}{-tab_sil}{tab_gs}{tard}Nous croyons que la conscience est le centre, le noyau de l'homme. "
        "{tard.1}Erreur, dit Nietzsche : la vie a fonctionné très longtemps sans elle. {tard.2}C'est l'instinct qui nous conserve ; "
        "la conscience arrive tard, et se trompe souvent.",
        "{-tard}À quoi sert-elle, alors ? Sa réponse, au paragraphe trois cent cinquante-quatre, est saisissante.",
        ("C", "… la conscience s'est seulement développée sous la pression du besoin de communication.", "c_comm"),
        "{-c_comm}{-tab_gs}{tab_tro}{comm}{comm.1}L'homme, animal fragile, a eu besoin des autres : il a fallu dire ce qu'il sentait, "
        "ce qu'il voulait. {comm.2}Devenir conscient, c'est donc traduire ce qu'on vit en signes communs : "
        "le {#le langage}langage de tous.",
        "{comm.3}Conséquence troublante : ce qui devient conscient devient du même coup superficiel, général, "
        "ce que tout le monde peut comprendre. Le point de vue du troupeau, dit Nietzsche.",
        ("Ce que j'ai de plus singulier… c'est justement ce que ma conscience laisse échapper.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-comm}{-tab_tro}{tab_ens}{surf}Regarde ces masques. {surf.1}Pour Nietzsche, la conscience n'est pas une fenêtre "
        "ouverte sur notre fond. {surf.2}C'est une surface, un masque commode, tourné vers les autres.",
        "{-surf}{inconnus}Nietzsche en tire une conclusion amère, quelques années plus tard : {inconnus.1}nous sommes "
        "inconnus à nous-mêmes. {inconnus.2}Le vieux précepte de Socrate, connais-toi toi-même, devient presque impossible : "
        "chacun est, pour soi-même, le plus lointain.",
        "{-inconnus}{-tab_ens}",
    ], vis={
        "nietz": dict(type="portrait", annee=1844, img="nietzsche", nom="Friedrich Nietzsche", dates="1844 – 1900",
                      legende="Le Gai Savoir (1882 ; livre V, 1887)", x=110, y=120, w=330, h=420),
        "tab_sil": dict(type="tableau", img="dv4-sils", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Sils-Maria, où Nietzsche passait ses étés (photo Hansueli Krapf, CC BY-SA 4.0)"),
        "c_tard": dict(type="cit", a="Nietzsche", o="Le Gai Savoir, § 11 (1882), trad. Henri Albert", x=640, y=150, w=570),
        "tab_gs": dict(type="tableau", img="cs3-gaisavoir", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                       legende="Nietzsche, Die fröhliche Wissenschaft (Le Gai Savoir), Chemnitz, 1882, page de titre"),
        "tard": dict(type="liste", titre="Une conscience tardive", items=[
            "La vie a fonctionné très longtemps sans elle", "L'instinct nous conserve ; la conscience se trompe souvent"],
                     marques=["1", "2"], x=170, y=190, w=940),
        "c_comm": dict(type="cit", a="Nietzsche", o="Le Gai Savoir, § 354 (1887), trad. Henri Albert", x=170, y=200, w=940),
        "tab_tro": dict(type="tableau", img="bh5-troupeau", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .55],
                        legende="Anton Mauve, Le Retour du troupeau, Laren, XIXᵉ siècle"),
        "comm": dict(type="liste", titre="Une conscience pour communiquer", items=[
            "L'homme fragile a besoin des autres", "Devenir conscient : traduire en signes communs",
            "Ce qui devient conscient devient superficiel : le point de vue du troupeau"],
                     marques=["1", "2", "→"], x=170, y=150, w=940),
        "tab_ens": dict(type="tableau", img="cs3-intrigue", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .4],
                        legende="James Ensor, L'Intrigue, 1890 (musée royal des Beaux-Arts, Anvers, CC0)"),
        "inconnus": dict(type="liste", titre="Généalogie de la morale, préface (1887)", items=[
            "Nous sommes inconnus à nous-mêmes", "« Connais-toi toi-même » : presque impossible"],
                         marques=["1", "→"], x=170, y=190, w=940),
        "surf": dict(type="cols", g="Une fenêtre ?", gq="ouverte sur notre fond, transparente", d="Une surface",
                     dq="un masque commode, tourné vers les autres", vs="≠"),
    }),

    # ------------------------------------------------------------------ V. Alain
    dict(id="alain", chap="Alain contre l'inconscient", fond="aube", humeur="calme", notions=["la liberté", "le devoir"],
         retenir="Alain : l'homme est obscur à lui-même, mais l'inconscient conçu comme un autre moi devient une excuse. La conscience est un effort ; Freud : là où était le ça, le moi doit advenir.",
         beats=[
        "{alain}{tab_h4}{plus3}Pour aller plus loin, écoutons un contradicteur. Alain, de son vrai nom Émile Chartier, "
        "professeur de philosophie au lycée Henri-Quatre, à Paris, pendant plus de vingt ans.",
        "Alain ne nie pas que l'homme soit obscur à lui-même : nos humeurs, nos gestes, notre corps nous échappent sans cesse. "
        "Mais il se méfie de l'inconscient de Freud.",
        "{-alain}{-plus3}{al}Ce qui le gêne, c'est l'idée d'un autre moi, caché, qui penserait et voudrait à ma place. "
        "{al.1}Un double, un petit diable intérieur. {al.2}Car alors, tout devient commode : ce n'est pas moi, c'est mon inconscient.",
        "{-tab_h4}{tab_cl}{al.3}Pour Alain, penser, c'est justement dire non, juger, se reprendre. La conscience est toujours, "
        "au fond, morale : un effort, une {#la liberté}liberté qui choisit de se tenir éveillée.",
        "{-al}{rep}Alors, qui a raison ? Il faut peut-être les entendre ensemble. {rep.g}Freud montre que la conscience "
        "n'est pas transparente : elle ne voit pas tout. {rep.d}Alain rappelle qu'elle reste le seul lieu où l'on peut se reprendre.",
        "{-rep}{sartre_l}Sartre, on l'a vu dans la série sur la liberté, ira plus loin encore : invoquer l'inconscient, "
        "pour lui, c'est de la mauvaise foi : une façon de se cacher sa propre liberté.",
        "{-sartre_l}{-tab_cl}{tab_voy}{tache}Freud lui-même fixait ce but à la psychanalyse : {tache.1}là où était le ça, "
        "le moi doit advenir. Rendre conscient ce qui ne l'était pas.",
        ("La conscience n'est pas un donné, transparent dès le départ. C'est une tâche.", {"rate": "-5%"}),
        "{-tache}{copie}Retiens-le pour tes copies. Sur un sujet comme « Peut-on se connaître soi-même ? », "
        "Leibniz, Freud et Nietzsche forment la partie qui doute. Alain, et Freud lui-même, ouvrent la dernière : "
        "se connaître n'est pas un fait, c'est un travail.",
        "{-copie}{-tab_voy}",
    ], vis={
        "alain": dict(type="portrait", annee=1868, img="alain", nom="Alain (Émile Chartier)", dates="1868 – 1951",
                      legende="Éléments de philosophie (1916) · Propos", x=110, y=120, w=330, h=420),
        "tab_h4": dict(type="tableau", img="cs3-henri4", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .45],
                       legende="Jules David, Paris, la cour d'honneur du lycée Henri-IV, photographie, 1902-1910"),
        "plus3": dict(type="tag", style="plus", t="Pour aller plus loin", x=640, y=560, w=420),
        "al": dict(type="liste", titre="Ce qu'Alain reproche à l'inconscient", items=[
            "Un autre moi, caché, qui penserait à ma place", "Une excuse commode : « c'est mon inconscient »",
            "Penser, c'est dire non, juger, se reprendre"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_cl": dict(type="tableau", img="cs3-alain-classe", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .48, .5],
                       legende="Alain et ses élèves au lycée Henri-IV, 1914 (photographie, domaine public)"),
        "rep": dict(type="cols", g="Freud", gq="la conscience n'est pas transparente", d="Alain",
                    dq="elle reste le seul lieu où l'on se reprend", vs="+"),
        "tab_voy": dict(type="tableau", img="cs3-voyageur", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .5, .4],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, vers 1817 (Kunsthalle, Hambourg)"),
        "sartre_l": dict(type="tag", style="lien", t="Sartre : invoquer l'inconscient, c'est de la mauvaise foi (épisode 4)",
                         x=170, y=560, w=940),
        "copie": dict(type="def", cles=["doute", "travail"], terme="Réflexe copie · « Peut-on se connaître soi-même ? »",
                      t="Leibniz, Freud, Nietzsche : la partie qui doute de la transparence de la conscience.",
                      etape="Alain, et Freud lui-même : se connaître n'est pas un fait, c'est un travail.", x=170, y=200, w=940),
        "tache": dict(type="def", cles=["tâche", "conscient"], terme="Une tâche",
                      t="Là où était le ça, le moi doit advenir (Freud, 1933).",
                      etape="Rendre conscient ce qui ne l'était pas : la conscience est un travail de lucidité.",
                      x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ret}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Leibniz. Il y a en nous une infinité de petites perceptions "
        "sans aperception : le bruit de la mer est fait de vagues que je n'entends pas.",
        "{rec.2}Deux : Freud. L'inconscient est une hypothèse nécessaire et légitime. Le moi n'est qu'une partie de la maison : "
        "le ça, le moi, le surmoi.",
        "{rec.3}Trois : Nietzsche. La conscience est tardive, faite pour communiquer : elle ne saisit que la surface, ce qui est commun.",
        "{rec.4}Quatre : Alain. L'homme est obscur à lui-même, mais la conscience reste un effort, un devoir de lucidité. "
        "Et deux couples à garder pour tes copies : perception et aperception ; conscience et inconscient.",
        "{-rec}{-tab_ret}{tab_fin}{q_suite}Depuis le début, nous regardons la conscience comme une chambre fermée, "
        "à explorer de l'intérieur. Et si elle n'avait pas d'intérieur ? Si elle était tout entière tournée vers le monde, "
        "et vers les autres ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : conscience, monde et autrui. Husserl, Sartre, Hegel, et Bergson.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ret": dict(type="tableau", img="cs3-moulin", fond=True, sombre=True, de=[1.3, .4, .5], a=[1.0, .5, .5],
                        legende="Jacob van Ruisdael, Le Moulin de Wijk bij Duurstede, vers 1670 (Rijksmuseum, Amsterdam)"),
        "rec": dict(type="carte", centre="TRANSPARENTE ?", branches=[
            dict(t="Leibniz", items=["les petites perceptions", "perception ≠ aperception", "le bruit de la mer"]),
            dict(t="Freud", items=["une hypothèse nécessaire", "antichambre, gardien, salon", "le ça, le moi, le surmoi"]),
            dict(t="Nietzsche", items=["une conscience tardive", "faite pour communiquer", "une surface"]),
            dict(t="Alain", items=["l'inconscient, une excuse ?", "penser, c'est se reprendre", "une tâche de lucidité"])]),
        "tab_fin": dict(type="tableau", img="cs3-voyageur", fond=True, sombre=True, de=[1.3, .5, .35], a=[1.0, .5, .5],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, vers 1817 (Kunsthalle, Hambourg)"),
        "q_suite": dict(type="question", t="Et si la conscience était tout entière tournée vers le monde, et vers les autres ?"),
        "fin": dict(type="titre", sur="À suivre", t="Conscience, monde et autrui",
                    sous="Épisode 4 · Husserl, Sartre, Hegel, Bergson"),
    }),
]

QUIZ = [
    dict(q="Que veut montrer Leibniz avec le bruit de la mer ?",
         r=["Que la mer est consciente", "Qu'il y a en nous des perceptions dont nous n'avons pas conscience",
            "Que les sens nous trompent", "Que l'inconscient est refoulé"], ok=1,
         voir="c_mer", ex="Nouveaux Essais, préface : j'entends le bruit de chaque vague sans le remarquer, sinon cent mille vagues ne feraient aucun bruit."),
    dict(q="Chez Leibniz, l'« aperception », c'est…",
         r=["une perception dont j'ai conscience", "une perception trop petite pour être remarquée",
            "un désir refoulé", "une erreur des sens"], ok=0,
         voir="pa", ex="Perception : tout ce qui m'affecte ; aperception : la perception remarquée, réfléchie. Les petites perceptions restent sans aperception."),
    dict(q="Qu'est-ce qui distingue l'inconscient freudien des petites perceptions de Leibniz ?",
         r=["Il est plus faible", "Il est refoulé : tenu à l'écart parce qu'il dérange", "Il n'agit pas sur nous",
            "Il est conscient"], ok=1,
         voir="lac", ex="Les petites perceptions sont trop faibles ; l'inconscient freudien est activement repoussé (le refoulement), et se trahit par les oublis, lapsus et rêves."),
    dict(q="Pourquoi Freud juge-t-il l'hypothèse de l'inconscient « légitime » ?",
         r=["Parce qu'on peut voir l'inconscient au microscope",
            "Parce qu'on fait de même en supposant une conscience chez les autres, d'après ce qu'ils font",
            "Parce que tous les médecins l'admettent", "Parce que les rêves sont toujours clairs"], ok=1,
         voir="hyp", ex="La conscience d'autrui n'est jamais vue, seulement supposée. De même, on suppose des pensées inconscientes pour donner sens aux trous de la conscience."),
    dict(q="Dans la seconde topique de Freud, le surmoi est…",
         r=["le réservoir des pulsions", "les interdits des parents et de la société devenus une voix intérieure",
            "la partie consciente du moi", "le gardien de l'antichambre"], ok=1,
         voir="top2", ex="Le ça (pulsions), le surmoi (interdits intériorisés), et le moi, qui compose entre eux et avec la réalité, comme un cavalier sur un cheval plus fort que lui."),
    dict(q="Selon Nietzsche (Le Gai Savoir, § 354), la conscience s'est développée…",
         r=["pour connaître la vérité", "sous la pression du besoin de communication", "pour maîtriser les instincts",
            "grâce à Dieu"], ok=1,
         voir="c_comm", ex="Devenir conscient, c'est traduire en signes communs : ce qui devient conscient devient superficiel, général, le point de vue du troupeau."),
    dict(q="Que reproche Alain à l'idée d'inconscient ?",
         r=["D'être trop scientifique", "D'en faire un autre moi caché, et une excuse commode",
            "De nier le corps", "D'oublier les rêves"], ok=1,
         voir="al", ex="Pour Alain, penser, c'est juger et se reprendre : la conscience est un effort moral. Freud lui-même : là où était le ça, le moi doit advenir."),
]

CREDITS = [
    "Portraits : Gottfried Wilhelm Leibniz (Christoph Bernhard Francke, vers 1695) ; Sigmund Freud (Max Halberstadt, vers 1921) ; "
    "Friedrich Nietzsche (Gustav Schultze, 1882) ; Alain (photographie, auteur inconnu) : domaine public",
    "Tableaux : Vilhelm Hammershøi, Intérieur, Strandgade 30 (1900) ; Gustave Courbet, La Vague (vers 1869) ; "
    "Jacob van Ruisdael, Le Moulin de Wijk bij Duurstede (vers 1670) ; Luca Signorelli, Les Damnés (Orvieto, 1499-1502) ; "
    "Johann Heinrich Füssli, Le Cauchemar (1781) ; Théodore Géricault, Officier de chasseurs à cheval chargeant (1812) ; "
    "Anton Mauve, Le Retour du troupeau ; James Ensor, L'Intrigue (1890) ; Caspar David Friedrich, Le Voyageur contemplant "
    "une mer de nuages (vers 1817) : domaine public",
    "Documents et photographies : Freud, Die Traumdeutung (1900) et schéma du Moi et du Ça (1923) ; Nietzsche, Die fröhliche "
    "Wissenschaft (1882) ; lycée Henri-IV (Jules David) ; Alain et ses élèves (1914) : domaine public ; "
    "plaque de la Berggasse (GuentherZ, CC BY 3.0) ; Sils-Maria (Hansueli Krapf, CC BY-SA 4.0)",
    "Citations : Leibniz, Nouveaux Essais sur l'entendement humain (préface) ; Nietzsche, Le Gai Savoir, trad. Henri Albert (1901) ; "
    "Freud, Métapsychologie (1915), traduction courante. Freud (Signorelli, l'antichambre, le cavalier) et Alain sont résumés "
    "par le narrateur.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
