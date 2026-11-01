"""Le devoir, épisode 6 : « Le devoir à l'épreuve du bac »

Même format que liberte_6.py : trois sujets décortiqués, une explication de texte (Kant, Fondements, section I,
le marchand, trad. Delbos 1907, vérifiée sur Wikisource), pièges. Méthode cohérente avec le guide de l'explication
du site (six éléments de l'introduction, trois gestes, quoi / comment / pourquoi, avocat de l'auteur).
"""

CODE = "devoir-6"
NOTION = "Le devoir"
NUM = 6
TITRE = "Le devoir à l'épreuve du bac"
SUIVANT = "Épisode 7 · Récap"
PRONONCIATION = {"Régulus": "Régulusse", "Criton": "Kriton", "Eichmann": "Aïkmane", "Arendt": "Arènnte",
                 "Montgomery": "Montgomeri", "Birmingham": "Birmingueme", "Nietzsche": "Nitche"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_off}{q1}Un soir de juin. Un correcteur, cent vingt copies sur la table. Il ouvre la première : "
        "« Depuis la nuit des temps, l'homme a des devoirs. » La deuxième : « Selon Kant… » "
        "La troisième : « Selon Kant, Nietzsche et Freud… »",
        ("Il soupire.", {"rate": "-8%"}),
        "{-q1}{q2}Et puis une copie commence autrement : « Un enfant pose ses pièces sur le comptoir. "
        "Le marchand lui rend exactement sa monnaie. Est-il honnête ? » Le correcteur repose son stylo. "
        "Il a envie de lire la suite.",
        "{-q2}{-tab_off}{tab_eco}{reg}Toute la différence est là. {reg.1}Le correcteur ne note pas ce que tu sais, "
        "mais ce que tu en fais. {reg.2}Une scène précise, plutôt qu'une généralité. {reg.3}Un problème, plutôt qu'une récitation.",
        "{-reg}{lien}La méthode générale, on l'a vue dans la série sur la liberté, à l'épisode six. "
        "Ici, on l'applique au devoir : trois sujets décortiqués, puis l'explication d'un texte de Kant.",
        ("P", 0.3),
        "{-lien}{-tab_eco}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_off": dict(type="tableau", img="dv6-officier", fond=True, sombre=True, de=[1.1, .5, .5], a=[1.35, .5, .55],
                        legende="Gerard ter Borch, Officier écrivant une lettre, XVIIᵉ s. (Musée national de Varsovie)"),
        "q1": dict(type="question", t="Cent vingt copies… et toutes se ressemblent."),
        "q2": dict(type="question", t="« Le marchand lui rend exactement sa monnaie. Est-il honnête ? »"),
        "tab_eco": dict(type="tableau", img="dv6-ecole", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .4],
                        legende="Jan Steen, L'École de village, vers 1665 (National Gallery of Ireland, Dublin)"),
        "reg": dict(type="liste", titre="Ce que note le correcteur", items=[
            "Ce que tu fais de ce que tu sais", "Une scène précise, pas une généralité", "Un problème, pas une récitation"],
                    marques=["✎", "1", "2"], x=170, y=170, w=940),
        "lien": dict(type="tag", style="lien", t="La méthode générale : série « La liberté », épisode 6", x=170, y=560, w=700),
        "titre": dict(type="titre", sur="Le devoir · Épisode 6", t="Le devoir à l'épreuve du bac",
                      sous="Trois sujets, une explication de texte, les pièges"),
    }),

    # ------------------------------------------------------------------ I. sujet 1
    dict(id="sujet1", chap="Sujet 1 · Renoncer à sa liberté ?", fond="aube", humeur="mystere",
         notions=["la liberté", "la raison"],
         retenir="Devoir et liberté : le devoir limite l'indépendance, mais il suppose la liberté et l'accomplit comme autonomie.",
         beats=[
        "{tab_sav}{suj1}Premier sujet, le grand classique : faire son devoir, est-ce renoncer à sa liberté ?",
        "{-suj1}{mots}D'abord, les mots. {mots.1}« Faire son devoir » : obéir à une obligation, surtout morale. "
        "{mots.2}« Renoncer » : abandonner volontairement. Le mot est fort… et piégé : renoncer, c'est encore choisir. "
        "{mots.3}« La liberté » : faire ce que je veux ? Ou me donner ma propre loi ? Tout le sujet est là.",
        "{-mots}{prob}La problématique naît d'une tension. {prob.1}D'un côté, le devoir s'oppose à mes désirs : "
        "« tu dois », c'est le contraire de « je veux ». {prob.2}De l'autre, on ne donne pas de devoirs à une pierre : "
        "seul un être libre peut en avoir. {prob.3}Alors, le devoir est-il une chaîne… ou la preuve de ma liberté ?",
        "{-prob}{plan1}Le plan, en trois temps. {plan1.1}Un : oui, le devoir limite ma {#la liberté}liberté, "
        "si être libre, c'est faire ce qui me plaît. Freud y entendrait la voix du surmoi, Nietzsche une dette héritée. "
        "Exemple : rester réviser quand les amis sortent.",
        "{plan1.2}Deux : mais le devoir suppose la liberté. Je pourrais désobéir : c'est justement pour cela que je dois. "
        "Kant : tu dois, donc tu peux.",
        "{plan1.3}Trois : bien plus, le devoir accompli est la forme la plus haute de la liberté, l'autonomie. "
        "Rousseau l'avait dit.{-plan1}",
        ("C", "L'impulsion du seul appétit est esclavage, et l'obéissance à la loi qu'on s'est prescrite est liberté.", "c_rou"),
        "{-c_rou}{-tab_sav}{tab_reg}{reg_ex}L'exemple qui fait mouche : Régulus, général romain, prisonnier des Carthaginois. "
        "On l'envoie à Rome négocier un échange, sur parole. Il conseille au Sénat de refuser… "
        "puis, malgré les larmes des siens, il retourne à Carthage, où l'attend la mort. Parce qu'il l'avait promis.",
        ("Personne ne l'y forçait. C'est précisément pour cela qu'il était libre.", {"rate": "-5%"}),
        "{-reg_ex}{intro}Et voilà ton introduction toute trouvée. {intro.1}L'accroche : Régulus qui retourne à Carthage. "
        "{intro.2}L'analyse des mots. {intro.3}La problématique : une chaîne, ou la preuve de ma liberté ? {intro.4}L'annonce du plan.",
        "{-intro}{-tab_reg}{cp1}Note la méthode : la troisième partie ne dit jamais « tout dépend ». "
        "Elle déplace la question, grâce à une distinction.",
        "{-cp1}",
    ], vis={
        "tab_sav": dict(type="tableau", img="dv6-savant", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="Rembrandt, Lettré à sa table de travail, 1641 (Château royal de Varsovie)"),
        "suj1": dict(type="mot", t="« Faire son devoir, est-ce renoncer à sa liberté ? »", g="le grand classique",
                     y=240, taille=62),
        "mots": dict(type="liste", titre="Étape 1 · Définir chaque mot", items=[
            "« Faire son devoir » : obéir à une obligation, surtout morale",
            "« Renoncer » : abandonner volontairement… donc encore choisir",
            "« La liberté » : faire ce que je veux, ou me donner ma loi ?"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "prob": dict(type="liste", titre="Étape 2 · Problématiser", items=[
            "Le devoir s'oppose à mes désirs : « tu dois » ≠ « je veux »",
            "Mais seul un être libre peut avoir des devoirs",
            "Le devoir : une chaîne… ou la preuve de ma liberté ?"], marques=["si", "or", "?"], x=170, y=150, w=940),
        "plan1": dict(type="liste", titre="« Faire son devoir, est-ce renoncer à sa liberté ? »", items=[
            "I. Oui : le devoir limite l'indépendance (Freud, Nietzsche)",
            "II. Mais il suppose la liberté : tu dois, donc tu peux (Kant)",
            "III. Le devoir accompli, c'est l'autonomie (Rousseau, Kant)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "intro": dict(type="liste", titre="L'introduction en quatre temps", items=[
            "Accroche : Régulus retourne à Carthage", "Analyse : les mots du sujet",
            "Problématique : une chaîne, ou la preuve de ma liberté ?", "Annonce du plan"],
                      marques=["1", "2", "3", "4"], x=170, y=150, w=940),
        "cp1": dict(type="tag", style="copie", t="Copie · la partie III déplace la question, elle ne dit pas « tout dépend »",
                    x=170, y=540, w=900),
        "c_rou": dict(type="cit", a="Rousseau", o="Du contrat social, I, 8 (1762)", x=170, y=190, w=940),
        "tab_reg": dict(type="tableau", img="dv6-regulus", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .35],
                        legende="Andries Cornelis Lens, Régulus retournant à Carthage, 1791"),
        "reg_ex": dict(type="def", cles=["promis", "libre"], terme="L'exemple · Régulus (IIIᵉ s. av. J.-C.)",
                       t="Libéré sur parole, il retourne mourir à Carthage parce qu'il l'avait promis.",
                       etape="Récit de la tradition romaine (Cicéron, Des devoirs, III).", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ II. sujet 2
    dict(id="sujet2", chap="Sujet 2 · Le devoir contre le bonheur ?", fond="nuit", humeur="tension",
         notions=["le bonheur"],
         retenir="« Peut-il » : en fait, oui ; en droit, le devoir ne promet pas le bonheur, il en rend digne.", beats=[
        "{tab_bru}{suj2}Deuxième sujet : le devoir peut-il s'opposer au bonheur ? Ici, attention au verbe : "
        "{!peut-il}« peut-il ».",
        "{-suj2}{peut}Il ouvre deux questions. {peut.g}En fait : arrive-t-il que le devoir rende malheureux ? Évidemment, oui. "
        "{peut.d}En droit : le devoir est-il, par nature, l'ennemi du bonheur ? C'est là qu'est la vraie question.",
        "{-peut}{plan2}{plan2.1}Première partie : oui, le conflit est fréquent. Regarde ce tableau de David. Brutus, "
        "consul de Rome, a fait condamner ses propres fils, qui complotaient contre la République. Le devoir a écrasé le bonheur. "
        "Et chez Kant, on l'a vu, la valeur morale apparaît justement quand le devoir s'oppose à l'inclination.",
        "{-tab_bru}{tab_gal}{plan2.2}Deuxième partie : pourtant, devoir et {#le bonheur}bonheur ne sont pas toujours ennemis. "
        "Pour Aristote, la vertu fait partie du bonheur. Pour Épicure, on ne vit pas agréablement sans vivre sagement "
        "et justement. Et l'égoïste comblé, est-il vraiment heureux ?",
        "{-tab_gal}{plan2.3}Troisième partie : le devoir ne promet pas le bonheur… il en rend digne. "
        "C'est la solution de Kant, dès la première page des Fondements.{-plan2}",
        "{kant}",
        ("C", "… la bonne volonté paraît constituer la condition indispensable même de ce qui nous rend dignes d'être heureux.",
         "c_dign"),
        "{-kant}{-c_dign}{dist2}La distinction qui dépasse le problème : {dist2.g}être heureux, {dist2.d}et mériter de l'être. "
        "Le devoir ne garantit pas le premier. Il est la condition du second.",
        "{-dist2}",
    ], vis={
        "tab_bru": dict(type="tableau", img="dv6-brutus", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .3, .5],
                        legende="Jacques-Louis David, Les licteurs rapportent à Brutus les corps de ses fils, 1789 (Louvre)"),
        "suj2": dict(type="mot", t="« Le devoir peut-il s'opposer au bonheur ? »", g="tout se joue sur un verbe",
                     y=240, taille=66),
        "peut": dict(type="cols", g="En fait", gq="arrive-t-il que le devoir rende malheureux ?", d="En droit",
                     dq="le devoir est-il, par nature, l'ennemi du bonheur ?", vs="≠", repere="Repère · en fait / en droit"),
        "plan2": dict(type="liste", titre="« Le devoir peut-il s'opposer au bonheur ? »", items=[
            "I. Oui, en fait : Brutus, et Kant (le devoir contre l'inclination)",
            "II. Mais pas toujours : Aristote, Épicure (vertu et bonheur liés)",
            "III. Le devoir rend digne du bonheur (Kant)"], marques=["I", "II", "III"], x=170, y=130, w=940),
        "tab_gal": dict(type="tableau", img="dv6-galette", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Pierre-Auguste Renoir, Bal du moulin de la Galette, 1876 (musée d'Orsay)"),
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Fondements de la métaphysique des mœurs (1785)", x=110, y=120, w=330, h=420),
        "c_dign": dict(type="cit", a="Kant", o="Fondements, section I (1785), trad. Delbos", x=640, y=170, w=570),
        "dist2": dict(type="cols", g="Être heureux", gq="le devoir ne le garantit pas", d="Mériter de l'être",
                      dq="le devoir en est la condition", vs="≠", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ III. sujet 3
    dict(id="sujet3", chap="Sujet 3 · Toujours obéir aux lois ?", fond="aube", humeur="lumiere",
         notions=["l'État", "la justice"],
         retenir="« Toujours » : obéir aux lois protège de la violence, mais une loi peut être injuste. Désobéir, parfois, par devoir.",
         beats=[
        "{tab_soc}{suj3}Troisième sujet : doit-on toujours obéir aux lois ? Un mot porte tout le sujet : {!toujours}toujours.",
        "{-suj3}{dm}Et « doit-on » ne veut pas dire « est-on forcé par la police ». {dm.1}C'est une question morale : "
        "est-il juste d'obéir ? Repère : légal et légitime, vu dans l'épisode un.",
        "{-dm}{plan3}{plan3.1}Première partie : oui, il le faut. Sans lois, c'est la guerre de tous contre tous, dit Hobbes. "
        "Et Socrate, condamné à mort injustement, refuse de s'évader : on ne répond pas à une injustice en détruisant "
        "les lois de la cité. C'est le Criton de Platon.",
        "{-tab_soc}{tab_ant}{plan3.2}Deuxième partie : mais une loi peut être injuste. Antigone enterre son frère malgré l'interdit "
        "de Créon. Et Eichmann, on l'a vu avec Hannah Arendt, n'avait fait qu'obéir aux lois de son {#l'État}État. "
        "Obéir n'excuse pas.",
        "{-tab_ant}{plan3.3}Troisième partie : désobéir peut être un devoir… mais pas n'importe comment.{-plan3}",
        "{king}{dc}C'est l'exemple de Rosa Parks, qui refuse en 1955 de céder sa place dans un bus de Montgomery. "
        "Martin Luther King l'explique dans sa Lettre de la prison de Birmingham, en 1963 : on a le devoir moral "
        "d'obéir aux lois justes, et celui de désobéir aux lois injustes. {dc.1}Mais ouvertement, sans violence, "
        "et en acceptant la sanction.",
        "{-king}{-dc}{rep3}Le dépassement : {rep3.g}obéir à toutes les lois, {rep3.d}ou obéir à la loi juste. "
        "Celui qui désobéit ainsi ne méprise pas la loi : il la prend tellement au sérieux qu'il exige qu'elle soit "
        "conforme à la {#la justice}justice.",
        "{-rep3}",
    ], vis={
        "tab_soc": dict(type="tableau", img="t-socrate", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .45],
                        legende="Jacques-Louis David, La Mort de Socrate, 1787"),
        "suj3": dict(type="mot", t="« Doit-on toujours obéir aux lois ? »", g="un mot porte tout le sujet", y=240, taille=70),
        "dm": dict(type="def", cles=["morale", "juste"], terme="« Doit-on » : une question morale",
                   t="Non pas « est-on forcé ? », mais « est-il juste d'obéir ? »",
                   etape="Repère · légal / légitime (épisode 1).", x=170, y=200, w=940),
        "plan3": dict(type="liste", titre="« Doit-on toujours obéir aux lois ? »", items=[
            "I. Oui : sans lois, la violence (Hobbes) · Socrate refuse de s'évader (Criton)",
            "II. Mais une loi peut être injuste : Antigone, Eichmann (Arendt)",
            "III. Désobéir, parfois, par devoir : la désobéissance civile"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_ant": dict(type="tableau", img="dv1-antigone", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .45, .3],
                        legende="Frederic Leighton, Antigone, 1882"),
        "king": dict(type="portrait", annee=1929, img="king", nom="Martin Luther King", dates="1929 – 1968",
                     legende="Lettre de la prison de Birmingham (1963)", x=110, y=120, w=330, h=420),
        "dc": dict(type="def", cles=["ouvertement", "sanction"], terme="La désobéissance civile",
                   t="Un devoir moral : désobéir aux lois injustes.",
                   etape="Ouvertement, sans violence, en acceptant la sanction.", x=560, y=170, w=650),
        "rep3": dict(type="cols", g="Obéir à toutes les lois", gq="le légal", d="Obéir à la loi juste",
                     dq="le légitime", vs="→", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ IV. explication : l'introduction
    dict(id="texte", chap="L'explication · Le texte", fond="nuit", humeur="calme", notions=["la raison"],
         retenir="Introduction : thème, question, thèse adverse, thèse, enjeu, plan. Toujours avec les lignes du texte.", beats=[
        "{tab_epi}Et si tu choisis l'explication de texte ? Voici un texte possible, et court : Kant, "
        "Fondements de la métaphysique des mœurs, première section. Le marchand, que tu connais depuis l'épisode trois. "
        "Écoute-le en entier.",
        ("C", "Par exemple, il est sans doute conforme au devoir que le débitant n'aille pas surfaire le client inexpérimenté, "
              "et même c'est ce que ne fait jamais dans tout grand commerce le marchand avisé ; il établit au contraire un prix "
              "fixe, le même pour tout le monde, si bien qu'un enfant achète chez lui à tout aussi bon compte que n'importe qui.",
         "c_t1"),
        "{-c_t1}Puis vient le cœur de l'argument.",
        ("C", "On est donc loyalement servi ; mais ce n'est pas à beaucoup près suffisant pour qu'on en retire cette conviction "
              "que le marchand s'est ainsi conduit par devoir et par des principes de probité ; son intérêt l'exigeait, et l'on "
              "ne peut pas supposer ici qu'il dût avoir encore par surcroît pour ses clients une inclination immédiate de façon "
              "à ne faire, par affection pour eux en quelque sorte, de prix plus avantageux à l'un qu'à l'autre.", "c_t2"),
        "{-c_t2}Et la conclusion.",
        ("C", "Voilà donc une action qui était accomplie, non par devoir, ni par inclination immédiate, mais seulement "
              "dans une intention intéressée.", "c_t3"),
        "{-c_t3}{-tab_epi}{tab_mai}{six}Au brouillon, on cherche d'abord les six éléments de l'introduction. "
        "{six.1}Le thème : la valeur morale d'une action honnête. {six.2}La question : suffit-il qu'une action soit "
        "conforme au devoir pour avoir une valeur morale ? {six.3}La thèse adverse, ce qu'on penserait spontanément : "
        "oui, on juge quelqu'un sur ses actes, et le marchand qui ne vole personne est honnête.",
        "{six.4}La thèse de Kant : une action peut être conforme au devoir sans être faite par devoir, car son motif "
        "peut être l'intérêt ; elle n'a alors aucune valeur morale. {six.5}L'enjeu : savoir où se loge la moralité, "
        "dans l'acte visible, ou dans l'intention invisible. {six.6}Le plan : d'abord un exemple, le prix fixe ; "
        "puis la raison pour laquelle cela ne suffit pas ; enfin le classement de l'action, faite par intérêt.",
        "{-six}{-tab_mai}",
    ], vis={
        "tab_epi": dict(type="tableau", img="dv3-epicerie", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .5],
                        legende="Gerrit Dou, L'Épicière de village, 1647 (musée du Louvre)"),
        "c_t1": dict(type="cit", a="Kant", o="Fondements de la métaphysique des mœurs, section I (1785), trad. Delbos",
                     x=170, y=110, w=940),
        "c_t2": dict(type="cit", a="Kant", o="Fondements, section I (suite)", x=170, y=100, w=940),
        "c_t3": dict(type="cit", a="Kant", o="Fondements, section I (fin du passage)", x=170, y=170, w=940),
        "tab_mai": dict(type="tableau", img="dv6-maitresse", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .45],
                        legende="Jean Siméon Chardin, La Maîtresse d'école, vers 1735-1736 (National Gallery, Londres)"),
        "six": dict(type="liste", titre="Les six éléments de l'introduction", items=[
            "Thème : la valeur morale d'une action honnête",
            "Question : être conforme au devoir suffit-il ?",
            "Thèse adverse : on juge sur les actes",
            "Thèse : conforme au devoir ≠ par devoir ; l'intérêt ôte la valeur morale",
            "Enjeu : la moralité est-elle dans l'acte ou dans l'intention ?",
            "Plan : l'exemple · pourquoi il ne suffit pas · le classement"],
                    marques=["1", "2", "3", "4", "5", "6"], cles=["thèse adverse"], x=170, y=90, w=940),
    }),

    # ------------------------------------------------------------------ V. explication : le développement
    dict(id="developpement", chap="L'explication · Phrase par phrase", fond="aube", humeur="calme",
         notions=["la conscience", "la vérité"],
         retenir="Pour chaque phrase : quoi, comment, pourquoi. Trois gestes : reformuler, définir, illustrer. Discuter en avocat de l'auteur.",
         beats=[
        "{tab_bou}{qcp}Puis, phrase par phrase, un tableau : la citation, et trois colonnes. Prenons la phrase charnière : "
        "« On est donc loyalement servi ; mais ce n'est pas à beaucoup près suffisant… » "
        "{qcp.1}Quoi ? Kant concède que le client n'est pas trompé, mais refuse d'en conclure que le marchand agit par devoir.",
        "{qcp.2}Comment ? Par une concession, « donc… mais », et une insistance, « pas à beaucoup près ». "
        "{qcp.3}Pourquoi ? Pour séparer le résultat de l'action, qui est bon, de son motif, qui seul compte en morale.",
        "{-qcp}{ges}Pour expliquer, trois gestes. {ges.1}Reformuler : autrement dit, une conduite honnête peut cacher un calcul. "
        "{ges.2}Définir : par « inclination immédiate », il faut entendre un penchant spontané, comme l'affection pour ses clients. "
        "{ges.3}Illustrer : c'est ainsi que l'élève qui ne triche pas parce qu'un surveillant le regarde agit conformément "
        "au devoir, non par devoir.",
        "{-ges}{cinq}Chaque paragraphe du développement suit cinq temps : {cinq.1}annoncer ce que fait le texte, "
        "{cinq.2}citer, {cinq.3}expliquer, {cinq.4}interroger, {cinq.5}et relier à la thèse.",
        "{-cinq}{-tab_bou}{tab_phi}{av}Enfin, interroge le texte, mais en avocat de l'auteur. {av.1}Objection : on ne voit jamais "
        "les intentions. Comment savoir si le marchand est intéressé ? {av.2}Kant le reconnaît lui-même : notre propre "
        "{#la conscience}conscience peut se tromper sur ses motifs. Mais cela ne prouve pas que le devoir n'existe pas. "
        "Cela montre seulement que la moralité ne se voit pas.",
        "{-av}{-tab_phi}{tab_kt}{conc}Pour conclure, quatre temps. {conc.1}Le bilan : Kant distingue l'action conforme "
        "au devoir et l'action faite par devoir. {conc.2}La réponse à la question : non, être conforme au devoir ne suffit pas. "
        "{conc.3}L'intérêt du texte : il apprend à ne pas confondre la morale avec la bonne réputation. "
        "{conc.4}Et, si tu veux, une ouverture : les utilitaristes, qui jugent au contraire par les conséquences.",
        "{-conc}{-tab_kt}{tab_ave}{pie}Trois pièges à éviter. {pie.1}Réciter tout ce que tu sais sur Kant, en oubliant le texte. "
        "{pie.2}La paraphrase : répéter l'histoire du marchand avec d'autres mots. {pie.3}Et le contresens : faire dire à Kant "
        "que le marchand est malhonnête. Il ne l'est pas ! Il ne ment pas, il ne vole personne : son action respecte la "
        "{#la vérité}vérité des prix. Simplement, elle n'est pas morale.",
        ("Une action peut être irréprochable… et sans valeur morale. C'est tout le texte.", {"rate": "-5%"}),
        "{-pie}{-tab_ave}",
    ], vis={
        "tab_bou": dict(type="tableau", img="dv6-boulanger", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .45, .35],
                        legende="Jan Steen, Le Boulanger Arent Oostwaert et sa femme, vers 1658 (Rijksmuseum, Amsterdam)"),
        "qcp": dict(type="cartes", petit=True, items=[
            dict(ic="porte", t="Quoi ?", q="le client est bien servi… mais cela ne prouve rien"),
            dict(ic="chemins", t="Comment ?", q="« donc… mais » · « pas à beaucoup près »"),
            dict(ic="colonnes", t="Pourquoi ?", q="séparer le résultat et le motif")]),
        "ges": dict(type="liste", titre="Expliquer une phrase : trois gestes", items=[
            "Reformuler · « autrement dit » : l'honnêteté peut cacher un calcul",
            "Définir · « par… il faut entendre » : l'inclination immédiate",
            "Illustrer · « c'est ainsi que » : l'élève surveillé qui ne triche pas"], marques=["1", "2", "3"],
                    x=170, y=150, w=940),
        "cinq": dict(type="liste", titre="Un paragraphe en cinq temps", items=[
            "Annoncer ce que fait le texte", "Citer", "Expliquer", "Interroger", "Relier à la thèse"],
                     marques=["1", "2", "3", "4", "5"], x=170, y=110, w=940),
        "tab_kt": dict(type="tableau", img="t4-kant-table", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                       legende="Emil Doerstling, Kant et ses convives, 1892-1893 (reproduction)"),
        "conc": dict(type="liste", titre="La conclusion en quatre temps", items=[
            "Bilan : conforme au devoir ≠ par devoir", "Réponse : la conformité ne suffit pas",
            "Intérêt : la morale n'est pas la réputation", "Ouverture : les utilitaristes et les conséquences"],
                     marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "tab_phi": dict(type="tableau", img="dv6-philosophe", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .35],
                        legende="François-Bernard Lépicié, d'après Chardin, Le Souffleur, gravure, XVIIIᵉ s. (Met, CC0)"),
        "av": dict(type="liste", titre="Discuter en avocat de l'auteur", items=[
            "Objection : on ne voit jamais les intentions",
            "Réponse : la moralité ne se voit pas, mais elle existe"], marques=["?", "→"], x=170, y=180, w=940),
        "tab_ave": dict(type="tableau", img="dv6-aveugles", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .5],
                        legende="Pieter Bruegel l'Ancien, La Parabole des aveugles, 1568 (Capodimonte, Naples)"),
        "pie": dict(type="liste", titre="Trois pièges", items=[
            "Réciter Kant en oubliant le texte", "Paraphraser l'histoire du marchand",
            "Le contresens : le marchand n'est pas malhonnête"], marques=["✗", "✗", "✗"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : chaque sujet se joue sur un mot. Renoncer. Peut-il. Toujours.",
        "{rec.2}Deux : trois distinctions qui dépassent le problème. Indépendance et autonomie. Être heureux et mériter de l'être. "
        "Obéir aux lois, et obéir à la loi juste.",
        "{rec.3}Trois : des exemples travaillés. Régulus, Brutus, Socrate, Antigone, Martin Luther King.",
        "{rec.4}Quatre : l'explication. Six éléments d'introduction, puis quoi, comment, pourquoi, en avocat de l'auteur.",
        "{-rec}{q_fin}À toi : choisis l'un des trois sujets, et fais-en le plan en vingt minutes. "
        "Les questions t'attendent sous la vidéo.",
        ("La prochaine fois : le récapitulatif de toute la série.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-q_fin}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="LE DEVOIR AU BAC", branches=[
            dict(t="Lire le sujet", items=["renoncer · peut-il · toujours", "en fait / en droit"]),
            dict(t="Dépasser", items=["indépendance / autonomie", "heureux / digne de l'être", "légal / légitime"]),
            dict(t="Exemples", items=["Régulus, Brutus", "Socrate, Antigone", "Martin Luther King"]),
            dict(t="Expliquer Kant", items=["six éléments", "quoi, comment, pourquoi", "avocat de l'auteur"])]),
        "q_fin": dict(type="question", t="Un sujet, un plan, vingt minutes."),
        "tab_fin": dict(type="tableau", img="dv6-lune", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Caspar David Friedrich, Lever de lune sur la mer, 1822 (Alte Nationalgalerie, Berlin)"),
        "fin": dict(type="titre", sur="À suivre", t="Récap", sous="Épisode 7 · Toute la série en un épisode"),
    }),
]

QUIZ = [
    dict(q="Dans « Faire son devoir, est-ce renoncer à sa liberté ? », quelle distinction permet de dépasser le problème ?",
         r=["Légal / légitime", "Indépendance / autonomie", "Nécessaire / contingent", "Prix / dignité"], ok=1,
         voir="plan1", ex="Le devoir limite l'indépendance (faire ce qui me plaît), mais il accomplit l'autonomie (obéir à la loi que je me donne)."),
    dict(q="Pourquoi Régulus est-il un bon exemple pour ce sujet ?",
         r=["Parce qu'il est forcé de retourner à Carthage", "Parce qu'il tient sa promesse alors que personne ne l'y contraint",
            "Parce qu'il fuit son devoir", "Parce qu'il désobéit au Sénat"], ok=1,
         voir="reg_ex", ex="Libéré sur parole, il retourne mourir à Carthage : le devoir accompli librement, sans contrainte."),
    dict(q="Dans « Le devoir peut-il s'opposer au bonheur ? », le verbe « pouvoir » invite à distinguer…",
         r=["le légal et le légitime", "en fait et en droit", "le corps et l'esprit", "la cause et l'effet"], ok=1,
         voir="peut", ex="En fait, le devoir rend parfois malheureux ; en droit, est-il par nature l'ennemi du bonheur ? C'est la vraie question."),
    dict(q="Selon Kant, la bonne volonté est…",
         r=["le moyen le plus sûr d'être heureux", "la condition de ce qui nous rend dignes d'être heureux",
            "un obstacle au bonheur", "inutile au bonheur"], ok=1,
         voir="c_dign", ex="Le devoir ne promet pas le bonheur ; il rend digne de l'être (Fondements, section I)."),
    dict(q="Pourquoi Socrate refuse-t-il de s'évader de sa prison (Criton) ?",
         r=["Parce qu'il a peur de mourir en exil", "Parce qu'on ne répond pas à une injustice en détruisant les lois de la cité",
            "Parce que la loi qui le condamne est juste", "Parce que ses amis refusent de l'aider"], ok=1,
         voir="plan3", ex="Même condamné injustement, il ne veut pas ruiner les lois : un argument fort pour la partie I."),
    dict(q="Selon Martin Luther King, la désobéissance à une loi injuste doit se faire…",
         r=["en secret, pour éviter la prison", "ouvertement, sans violence, en acceptant la sanction",
            "par la force, si nécessaire", "seulement si tout le monde est d'accord"], ok=1,
         voir="dc", ex="Lettre de la prison de Birmingham (1963) : on a le devoir moral de désobéir aux lois injustes, au grand jour."),
    dict(q="Dans l'explication du marchand, quelle est la thèse adverse ?",
         r=["Le marchand agit par devoir", "On juge quelqu'un sur ses actes : celui qui ne vole personne est honnête",
            "Le commerce est immoral", "Les enfants paient plus cher"], ok=1,
         voir="six", ex="C'est ce qu'on penserait spontanément ; Kant montre qu'une action conforme au devoir peut n'avoir aucune valeur morale."),
    dict(q="Quel contresens éviter sur ce texte ?",
         r=["Dire que l'action est conforme au devoir", "Dire que le marchand est malhonnête",
            "Dire que son motif est l'intérêt", "Dire que la moralité tient à l'intention"], ok=1,
         voir="pie", ex="Le marchand ne trompe personne : son action est irréprochable, mais faite par intérêt, donc sans valeur morale."),
]

CREDITS = [
    "Portraits : Kant (portrait anonyme, XVIIIᵉ s.) ; Martin Luther King (photo Marion S. Trikosko, 1964, Library of Congress, domaine public)",
    "Tableaux et gravures : Gerard ter Borch, Officier écrivant une lettre (XVIIᵉ s.) ; Jan Steen, L'École de village (vers 1665) ; "
    "Rembrandt, Lettré à sa table de travail (1641) ; Andries Cornelis Lens, Régulus retournant à Carthage (1791) ; "
    "Jacques-Louis David, Les licteurs rapportent à Brutus les corps de ses fils (1789) et La Mort de Socrate (1787) ; "
    "Emil Doerstling, Kant et ses convives (1892-1893) ; "
    "Pierre-Auguste Renoir, Bal du moulin de la Galette (1876) ; Frederic Leighton, Antigone (1882) ; "
    "Gerrit Dou, L'Épicière de village (1647) ; Jean Siméon Chardin, La Maîtresse d'école (vers 1735-1736) ; "
    "Jan Steen, Le Boulanger Arent Oostwaert et sa femme (vers 1658) ; François-Bernard Lépicié d'après Chardin, Le Souffleur (gravure, XVIIIᵉ s., Met, CC0) ; "
    "Pieter Bruegel l'Ancien, La Parabole des aveugles (1568) ; Caspar David Friedrich, Lever de lune sur la mer (1822) : domaine public",
    "Texte expliqué : Kant, Fondements de la métaphysique des mœurs (1785), section I, trad. Victor Delbos (1907), Wikisource. "
    "Rousseau, Du contrat social, I, 8 (1762).",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
