"""L'État, épisode 6 : « L'État à l'épreuve du bac »

Même format que devoir_6.py : trois sujets décortiqués, une explication de texte, pièges. Méthode cohérente avec le guide
de l'explication du site (six éléments de l'introduction, trois gestes, quoi / comment / pourquoi, paragraphe en cinq temps,
avocat de l'auteur, conclusion en quatre temps).
Texte expliqué : Spinoza, Traité théologico-politique, chapitre XX (1670), trad. Émile Saisset (1842 ; nouvelle éd. 1861),
vérifié sur Wikisource. Aristides de Sousa Mendes (Bordeaux, juin 1940) : résumé par le narrateur.
"""

CODE = "etat-6"
NOTION = "L'État"
NUM = 6
TITRE = "L'État à l'épreuve du bac"
SUIVANT = "Épisode 7 · Récap"
PRONONCIATION = {"Ceaușescu": "Tchaouchesscou", "Bucarest": "Bucaresste", "Clastres": "Klastre", "Sousa Mendes": "Souza Mèndèche",
                 "Aristides": "Aristidèche", "Salazar": "Salazar", "Proudhon": "Proudon", "Saisset": "Sèssè"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_ank}{q1}Juin, huit heures du matin. Tu retournes la feuille. Premier sujet : peut-on se passer de l'État ?",
        "{-q1}{tete}Et dans ta tête, tout se bouscule. {tete.1}Hobbes et la guerre de chacun contre chacun. "
        "{tete.2}Ceaușescu au balcon. {tete.3}Proudhon, Marx, Nietzsche. {tete.4}Le voile d'ignorance… "
        "Tu as envie de tout écrire, dans l'ordre où tu l'as appris.",
        ("Surtout pas.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-tete}{reg}Le correcteur ne note pas ce que tu sais, {reg.1}mais ce que tu en fais : {reg.2}un problème posé, "
        "{reg.3}des auteurs mis au service d'une réponse, des exemples précis.",
        "{-reg}{lien}La méthode générale, on l'a vue dans la série sur la liberté, à l'épisode six. Ici, on l'applique à l'État : "
        "trois sujets décortiqués, puis l'explication d'un texte de Spinoza.",
        ("P", 0.3),
        "{-lien}{-tab_ank}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_ank": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "q1": dict(type="question", t="Peut-on se passer de l'État ?"),
        "tete": dict(type="nuage", items=["Hobbes", "Ceaușescu", "Proudhon", "Marx", "Nietzsche", "le voile d'ignorance"]),
        "reg": dict(type="liste", titre="Ce que note le correcteur", items=[
            "Ce que tu fais de ce que tu sais", "Un problème posé", "Des auteurs et des exemples au service d'une réponse"],
                    marques=["✎", "1", "2"], x=170, y=170, w=940),
        "lien": dict(type="tag", style="lien", t="La méthode générale : série « La liberté », épisode 6", x=170, y=560, w=700),
        "titre": dict(type="titre", sur="L'État · Épisode 6", t="L'État à l'épreuve du bac",
                      sous="Trois sujets, un texte de Spinoza, les pièges"),
    }),

    # ------------------------------------------------------------------ I. sujet 1
    dict(id="sujet1", chap="Sujet 1 · L'ennemi de la liberté ?", fond="aube", humeur="mystere",
         notions=["la liberté", "la justice"],
         retenir="L'État contraint, mais sans lui pas de liberté réelle. Il en est la condition quand il est limité : liberté naturelle ≠ liberté civile.",
         beats=[
        "{tab_lib}{suj1}Premier sujet : l'État est-il l'ennemi de la liberté ?",
        "{-suj1}{mots}D'abord, les mots. {mots.1}« L'État » : l'institution qui a le monopole de la violence légitime, "
        "comme dit Weber, pas le gouvernement du moment. {mots.2}« Ennemi » : le mot est fort. Un obstacle gêne ; "
        "un ennemi veut ma perte. Le sujet demande si l'État s'oppose à la liberté par nature. "
        "{mots.3}« La liberté » : faire ce que je veux, ou vivre en sécurité sous des lois que je reconnais ?",
        "{-mots}{prob}La tension : {prob.1}l'État m'impose des lois, des impôts, une police. {prob.2}Mais sans lui, "
        "qui protégerait ma {#la liberté}liberté contre le plus fort ? {prob.3}Est-il son ennemi… ou sa condition ?",
        "{-prob}{plan1}{plan1.1}Première partie : oui, l'État contraint, et il peut écraser. Proudhon le dit : être gouverné, "
        "c'est être gardé à vue, inspecté, espionné. Nietzsche y voit le plus froid des monstres froids.",
        "{-tab_lib}{tab_gor}{plan1.2}Deuxième partie : mais sans État, il n'y a pas de liberté du tout. "
        "Souviens-toi de Montréal, en 1969 : seize heures sans police, et la ville bascule. Locke l'a dit : l'État est le gardien "
        "de la vie, de la liberté, des biens.",
        "{plan1.3}Troisième partie : l'État n'est pas l'ennemi de la liberté, il en est la condition, à une condition : "
        "qu'il soit limité. Montesquieu l'a montré : pour qu'on ne puisse abuser du pouvoir, "
        "il faut que le pouvoir arrête le pouvoir. Ceux qui font les lois, ceux qui les exécutent et ceux qui jugent "
        "ne doivent jamais être les mêmes.{-plan1}",
        "{lnc}La distinction qui dépasse le problème : {lnc.g}la liberté naturelle, qui n'a pour limite que mes forces, "
        "{lnc.d}et la liberté civile, garantie par la loi. L'État retire la première… pour donner la seconde.",
        "{-lnc}{cp1}L'exemple qui fait mouche : Montréal, le sept octobre 1969. Un exemple précis vaut mieux "
        "que dix « depuis toujours ».",
        "{-cp1}{-tab_gor}",
    ], vis={
        "tab_lib": dict(type="tableau", img="t-liberte-peuple", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="Eugène Delacroix, La Liberté guidant le peuple, 1830"),
        "suj1": dict(type="mot", t="« L'État est-il l'ennemi de la liberté ? »", g="le grand classique", y=240, taille=64),
        "mots": dict(type="liste", titre="Étape 1 · Définir chaque mot", items=[
            "« L'État » : le monopole de la violence légitime (Weber), pas le gouvernement",
            "« Ennemi » : plus qu'un obstacle, une opposition par nature ?",
            "« La liberté » : faire ce que je veux, ou vivre sous des lois que je reconnais ?"],
                     marques=["1", "2", "3"], x=170, y=150, w=940),
        "prob": dict(type="liste", titre="Étape 2 · Problématiser", items=[
            "L'État m'impose lois, impôts, police", "Mais sans lui, qui me protège du plus fort ?",
            "Ennemi de la liberté… ou sa condition ?"], marques=["si", "or", "?"], x=170, y=150, w=940),
        "plan1": dict(type="liste", titre="« L'État est-il l'ennemi de la liberté ? »", items=[
            "I. Oui : il contraint, il peut écraser (Proudhon, Nietzsche)",
            "II. Mais sans lui, pas de liberté : Montréal 1969, Hobbes, Locke",
            "III. Il en est la condition, s'il est limité : le pouvoir arrête le pouvoir"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_gor": dict(type="tableau", img="et2-gordon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .55],
                        legende="John Seymour Lucas, Les Émeutes de Gordon (Londres, 1780), 1879"),
        "lnc": dict(type="cols", g="Liberté naturelle", gq="limitée par mes seules forces", d="Liberté civile",
                    dq="garantie par la loi", vs="→", repere="La distinction qui dépasse (Rousseau)"),
        "cp1": dict(type="tag", style="copie", t="Copie · un exemple précis : Montréal, 7 octobre 1969 (épisode 2)",
                    x=170, y=540, w=820),
    }),

    # ------------------------------------------------------------------ II. sujet 2
    dict(id="sujet2", chap="Sujet 2 · Se passer de l'État ?", fond="nuit", humeur="tension",
         notions=["la nature", "la liberté"],
         retenir="« Peut-on » : en fait (est-ce possible ?) et en droit (est-ce souhaitable ?). On ne se passe pas de l'État, mais on peut se passer de la servitude.",
         beats=[
        "{tab_bal}{suj2}Deuxième sujet, celui de la feuille : peut-on se passer de l'État ? D'abord, « se passer de » : vivre sans, ne pas en avoir besoin. "
        "Et l'État, ce n'est pas la société, ni le pouvoir en général : un chef sans pouvoir, ce n'est pas encore un État. "
        "Mais tout tient au verbe : « peut-on ».",
        "{-suj2}{peut}Il ouvre deux questions. {peut.g}En fait : est-ce possible ? Une société peut-elle vivre sans État ? "
        "{peut.d}En droit : est-ce souhaitable ? Serait-on plus libres, plus justes ?",
        "{-peut}{plan2}{plan2.1}Première partie : on le peut, semble-t-il. Clastres a décrit des sociétés contre l'État, "
        "où le chef parle mais ne commande pas. Proudhon rêve de contrats libres ; Marx et Engels, d'un État qui dépérit.",
        "{-tab_bal}{tab_pal}{plan2.2}Deuxième partie : mais en fait, l'État n'a jamais dépéri. Les régimes qui l'annonçaient "
        "l'ont rendu énorme, comme l'avait prédit Bakounine. Et pour Aristote, l'homme est par {#la nature}nature "
        "un animal politique : hors de la cité, une brute ou un dieu.",
        "{-tab_pal}{tab_bal2}{plan2.3}Troisième partie : on ne peut pas se passer de l'État… mais on peut se passer de la "
        "servitude. Car l'État repose sur notre consentement, dit La Boétie.{-plan2}",
        "{ets}La distinction qui dépasse : {ets.g}se passer de l'État, {ets.d}ou se passer d'un maître. "
        "À Bucarest, en 1989, la foule n'a pas aboli l'État. Elle a renvoyé un tyran, puis élu des représentants.",
        ("Le citoyen ne se passe pas de l'État. Il l'empêche de se passer de lui.", {"rate": "-5%"}),
        "{-ets}{-tab_bal2}",
    ], vis={
        "tab_bal": dict(type="tableau", img="et4-tupi", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .35],
                        legende="Albert Eckhout, Homme tupi, 1643 (Musée national du Danemark)"),
        "suj2": dict(type="mot", t="« Peut-on se passer de l'État ? »", g="tout se joue sur un verbe", y=240, taille=70),
        "peut": dict(type="cols", g="En fait", gq="est-ce possible ? une société sans État ?", d="En droit",
                     dq="est-ce souhaitable ? plus libres, plus justes ?", vs="≠", repere="Repère · en fait / en droit"),
        "plan2": dict(type="liste", titre="« Peut-on se passer de l'État ? »", items=[
            "I. On le peut, semble-t-il : Clastres, Proudhon, le dépérissement (Marx)",
            "II. Mais l'État n'a jamais dépéri (Bakounine) ; l'homme, animal politique (Aristote)",
            "III. On ne se passe pas de l'État, mais de la servitude (La Boétie)"], marques=["I", "II", "III"],
                      x=170, y=130, w=940),
        "tab_pal": dict(type="tableau", img="et4-palais", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .35],
                        legende="Le palais du Parlement (ancienne « Maison du peuple » de Ceaușescu), Bucarest, 1996 (photo Sludge G, CC BY-SA 2.0)"),
        "tab_bal2": dict(type="tableau", img="et4-balcon", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .3],
                         legende="Bucarest, décembre 1989 (Musée national d'histoire de la Roumanie, attribution)"),
        "ets": dict(type="cols", g="Se passer de l'État", gq="impossible, en fait", d="Se passer d'un maître",
                    dq="possible, et souhaitable : ne plus servir", vs="≠", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ III. sujet 3
    dict(id="sujet3", chap="Sujet 3 · Toujours obéir ?", fond="aube", humeur="lumiere",
         notions=["le devoir", "la justice"],
         retenir="« Faut-il » : nécessité ou devoir ? Obéir à l'État légitime, en actes ; garder le droit de juger et de parler. Obéissance ≠ servitude.",
         beats=[
        "{tab_bor}{suj3}Troisième sujet : faut-il toujours obéir à l'État ? Tu reconnais un sujet voisin, traité dans la série "
        "sur le devoir : doit-on toujours obéir aux lois ? On ne refait pas tout. On regarde ce qui change.",
        "{-suj3}{chg}{chg.1}« Faut-il » : est-ce une nécessité, sinon le chaos ? Ou un {#le devoir}devoir ? "
        "{chg.2}« À l'État » : pas seulement aux lois, mais aussi aux ordres d'un gouvernement, d'une administration, d'un chef.",
        "{-chg}{plan3}{plan3.1}Première partie : oui, il le faut. Sans obéissance, plus d'État, et Hobbes nous a montré "
        "ce qui vient ensuite. Socrate lui-même, condamné injustement, refusa de s'évader de sa prison : "
        "on l'a vu dans la série sur le devoir.",
        "{plan3.2}Deuxième partie : mais l'État peut trahir sa raison d'être. Locke reconnaît au peuple un droit de résistance.{-plan3}",
        "{-tab_bor}{tab_pla}{mendes}Un exemple. Bordeaux, juin 1940. La France s'effondre, des milliers de réfugiés fuient "
        "les nazis. Le consul du Portugal, Aristides de Sousa Mendes, a reçu de son gouvernement l'ordre de refuser les visas. "
        "Pendant quelques jours, il en signe des milliers. Rappelé, sanctionné, il mourra dans la misère. "
        "Il est aujourd'hui honoré comme Juste parmi les nations.",
        "{-mendes}{-tab_pla}{tab_dam}{plan3b}{plan3b.1}Troisième partie : obéir, en actes, à l'État légitime… sans jamais lui "
        "abandonner son jugement. Penser, parler, critiquer, c'est ce que l'État doit laisser libre. C'est la thèse de Spinoza, "
        "dans le texte qui va suivre.",
        "{-plan3b}{os}La distinction qui dépasse : {os.g}l'obéissance, qui suit la loi en gardant les yeux ouverts, "
        "{os.d}et la servitude, qui obéit sans penser.",
        "{-os}{-tab_dam}",
    ], vis={
        "tab_bor": dict(type="tableau", img="et6-bordeaux", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Réfugiés devant la mairie de Bordeaux, juin 1940 (domaine public)"),
        "suj3": dict(type="mot", t="« Faut-il toujours obéir à l'État ? »", g="un sujet voisin… mais pas identique", y=240, taille=66),
        "chg": dict(type="liste", titre="Ce qui change", items=[
            "« Faut-il » : nécessité, ou devoir ?", "« À l'État » : les lois, mais aussi les ordres d'un chef"],
                    marques=["1", "2"], x=170, y=170, w=940),
        "plan3": dict(type="liste", titre="« Faut-il toujours obéir à l'État ? »", items=[
            "I. Oui : sans obéissance, la guerre (Hobbes) ; Socrate refuse de s'évader",
            "II. Mais l'État peut trahir sa fin : le droit de résistance (Locke)"], marques=["I", "II"],
                      x=170, y=150, w=940),
        "tab_pla": dict(type="tableau", img="et6-plaque", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .4],
                        legende="Plaque en hommage à Aristides de Sousa Mendes, Bayonne (photo Michel Bakni, CC BY-SA 4.0)"),
        "mendes": dict(type="portrait", annee=1885, img="sousa-mendes", nom="Aristides de Sousa Mendes", dates="1885 – 1954",
                       legende="Consul du Portugal à Bordeaux (1940)", x=110, y=120, w=330, h=420),
        "tab_dam": dict(type="tableau", img="et3-amsterdam", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Gerrit Berckheyde, La Place du Dam et l'hôtel de ville d'Amsterdam, 1672"),
        "plan3b": dict(type="liste", titre="… et la troisième partie", items=[
            "III. Obéir en actes à l'État légitime, garder son jugement (Spinoza)"], marques=["III"], x=170, y=170, w=940),
        "os": dict(type="cols", g="L'obéissance", gq="suivre la loi, les yeux ouverts", d="La servitude",
                   dq="obéir sans penser", vs="≠", repere="La distinction qui dépasse"),
    }),

    # ------------------------------------------------------------------ IV. explication : le texte
    dict(id="texte", chap="L'explication · Le texte", fond="nuit", humeur="calme", notions=["la raison", "la liberté"],
         retenir="Introduction : thème, question, thèse adverse, thèse, enjeu, plan. Toujours avec les mots du texte.", beats=[
        "{spino}{tab_ttp}Le texte, maintenant. Spinoza, Traité théologico-politique, 1670, chapitre vingt. "
        "Le livre paraît sans nom d'auteur, avec une fausse adresse d'éditeur : il sera interdit quatre ans plus tard. "
        "Le titre du chapitre dit tout : dans un État libre, chacun a le droit de penser ce qu'il veut et de dire ce qu'il pense. "
        "Écoute le passage en entier.",
        ("C", "De la description que nous avons donnée ci-dessus des fondements de l'État, il suit avec une parfaite évidence "
              "que la fin dernière de l'État n'est pas de dominer les hommes, de les retenir par la crainte, de les soumettre "
              "à la volonté d'autrui, mais tout au contraire de permettre à chacun, autant que possible, de vivre en sécurité, "
              "c'est-à-dire de conserver intact le droit naturel qu'il a de vivre, sans dommage ni pour lui ni pour autrui.",
         "c_t1"),
        "{-spino}{-c_t1}Puis le cœur du texte.",
        ("C", "Non, dis-je, l'État n'a pas pour fin de transformer les hommes d'êtres raisonnables en animaux ou en automates, "
              "mais bien de faire en sorte que les citoyens développent en sécurité leur corps et leur esprit, fassent librement "
              "usage de leur raison, ne rivalisent point entre eux de haine, de fureur et de ruse, et ne se considèrent point "
              "d'un œil jaloux et injuste.", "c_t2"),
        "{-c_t2}Et la conclusion.",
        ("C", "La fin de l'État, c'est donc véritablement la liberté.", "c_t3"),
        "{-c_t3}{-tab_ttp}{tab_ver}{six}Au brouillon, les six éléments de l'introduction. {six.1}Le thème : la fin de l'État, "
        "c'est-à-dire son but. {six.2}La question : l'État existe-t-il pour dominer les hommes, ou pour les rendre libres ? "
        "{six.3}La thèse adverse, ce qu'on penserait spontanément : l'État, c'est la contrainte ; il sert à se faire obéir, "
        "par la peur s'il le faut.",
        "{six.4}La thèse de Spinoza : la fin de l'État n'est pas la domination mais la sécurité, et, plus encore, la liberté, "
        "car il est fait pour que chacun use librement de sa {#la raison}raison. {six.5}L'enjeu : si l'État a pour fin la liberté, "
        "un État qui gouverne par la terreur trahit sa propre raison d'être. {six.6}Le plan : d'abord ce que l'État n'est pas, "
        "puis ce qu'il doit permettre, enfin la conclusion, la liberté.",
        "{-six}{-tab_ver}",
    ], vis={
        "spino": dict(type="portrait", annee=1632, img="spinoza", nom="Baruch Spinoza", dates="1632 – 1677",
                      legende="Traité théologico-politique (1670)", x=110, y=120, w=330, h=420),
        "tab_ttp": dict(type="tableau", img="et3-ttp", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .35],
                        legende="Tractatus theologico-politicus, 1670 : sans nom d'auteur, adresse fictive « Hambourg »"),
        "c_t1": dict(type="cit", a="Spinoza", o="Traité théologico-politique, chap. XX (1670), trad. Saisset", x=640, y=90, w=570),
        "c_t2": dict(type="cit", a="Spinoza", o="Traité théologico-politique, chap. XX (suite)", x=170, y=110, w=940),
        "c_t3": dict(type="cit", a="Spinoza", o="Traité théologico-politique, chap. XX (fin du passage)", x=170, y=220, w=940),
        "tab_ver": dict(type="tableau", img="et6-vermeer", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .5],
                        legende="Johannes Vermeer, Femme écrivant une lettre et sa servante, vers 1670 (National Gallery of Ireland, Dublin)"),
        "six": dict(type="liste", titre="Les six éléments de l'introduction", items=[
            "Thème : la fin (le but) de l'État",
            "Question : dominer les hommes, ou les rendre libres ?",
            "Thèse adverse : l'État, c'est la contrainte et la peur",
            "Thèse : sa fin est la sécurité, et plus encore la liberté de la raison",
            "Enjeu : l'État qui gouverne par la terreur trahit sa raison d'être",
            "Plan : ce qu'il n'est pas · ce qu'il doit permettre · la liberté"],
                    marques=["1", "2", "3", "4", "5", "6"], cles=["thèse adverse"], x=170, y=90, w=940),
    }),

    # ------------------------------------------------------------------ V. explication : le développement
    dict(id="developpement", chap="L'explication · Phrase par phrase", fond="aube", humeur="calme",
         notions=["la raison", "la vérité"],
         retenir="Pour chaque phrase : quoi, comment, pourquoi. Trois gestes : reformuler, définir, illustrer. Discuter en avocat de l'auteur.",
         beats=[
        "{tab_rem}{qcp}Puis, phrase par phrase, un tableau : la citation, et trois colonnes. Prenons la phrase charnière : "
        "« Non, dis-je, l'État n'a pas pour fin de transformer les hommes d'êtres raisonnables en animaux ou en automates. » "
        "{qcp.1}Quoi ? L'État ne doit pas rabaisser les hommes : ni bêtes menées par la peur, ni machines qui obéissent sans penser.",
        "{qcp.2}Comment ? Par une insistance, « non, dis-je » : Spinoza s'engage en personne. Et par une opposition : "
        "« d'êtres raisonnables », « en animaux ou en automates ». {qcp.3}Pourquoi ? Pour montrer que gouverner par la crainte "
        "contredit la nature raisonnable de ceux qu'on gouverne.",
        "{-qcp}{ges}Pour expliquer, trois gestes. {ges.1}Reformuler : autrement dit, un État de terreur fabrique des bêtes dressées. "
        "{ges.2}Définir : par « automates », il faut entendre des êtres qui se meuvent sans penser, poussés du dehors. "
        "{ges.3}Illustrer : c'est ainsi que la foule de Bucarest applaudissait sur ordre… jusqu'au jour où elle a cessé.",
        "{-ges}{cinq}Chaque paragraphe suit cinq temps : {cinq.1}annoncer ce que fait le texte, {cinq.2}citer, "
        "{cinq.3}expliquer, {cinq.4}interroger, {cinq.5}et relier à la thèse.",
        "{-cinq}{-tab_rem}{tab_lev}{av}Interroge le texte, mais en avocat de l'auteur. {av.1}Objection : Hobbes, lui, fonde l'État "
        "sur la crainte. Et Spinoza reconnaît lui-même, juste après, que pour former un État, chacun doit renoncer à agir "
        "selon son propre décret. {av.2}Réponse : renoncer à agir à sa guise, oui ; renoncer à penser et à juger, jamais. "
        "L'État commande les actes, pas les esprits.",
        "{-av}{-tab_lev}{tab_eth}{conc}Pour conclure, quatre temps. {conc.1}Le bilan : Spinoza oppose la domination par la peur "
        "et la sécurité qui libère. {conc.2}La réponse : l'État existe pour la liberté. {conc.3}L'intérêt : un critère pour juger "
        "tout État, la liberté de penser et de dire ce qu'on pense. {conc.4}Et une ouverture : Rawls, qui place les libertés "
        "fondamentales avant tout le reste.",
        "{-conc}{-tab_eth}{tab_ave}{pie}Trois pièges. {pie.1}Faire de Spinoza un anarchiste : il ne veut pas moins d'État, "
        "il veut un État qui libère. {pie.2}Confondre la fin et l'origine : « fin » veut dire le but, pas le commencement. "
        "{pie.3}Réciter Hobbes contre Spinoza sans revenir aux mots du texte : la {#la vérité}vérité d'une explication, "
        "c'est le texte lui-même.",
        ("L'État le plus fort n'est pas celui qui fait peur. C'est celui qui laisse penser.", {"rate": "-5%"}),
        "{-pie}{-tab_ave}",
    ], vis={
        "tab_rem": dict(type="tableau", img="et6-rembrandt", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .45, .35],
                        legende="Rembrandt, Lettré dans son cabinet, 1634 (Galerie nationale, Prague)"),
        "qcp": dict(type="cartes", petit=True, items=[
            dict(ic="porte", t="Quoi ?", q="ni bêtes menées par la peur, ni machines"),
            dict(ic="chemins", t="Comment ?", q="« non, dis-je » · raisonnables / animaux, automates"),
            dict(ic="colonnes", t="Pourquoi ?", q="la crainte contredit la raison")]),
        "ges": dict(type="liste", titre="Expliquer une phrase : trois gestes", items=[
            "Reformuler · « autrement dit » : la terreur fabrique des bêtes dressées",
            "Définir · « par… il faut entendre » : l'automate, mû du dehors",
            "Illustrer · « c'est ainsi que » : la foule de Bucarest, applaudissant sur ordre"], marques=["1", "2", "3"],
                    x=170, y=150, w=940),
        "cinq": dict(type="liste", titre="Un paragraphe en cinq temps", items=[
            "Annoncer ce que fait le texte", "Citer", "Expliquer", "Interroger", "Relier à la thèse"],
                     marques=["1", "2", "3", "4", "5"], x=170, y=110, w=940),
        "tab_lev": dict(type="tableau", img="t-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.4, .5, .3],
                        legende="Abraham Bosse, frontispice du Léviathan de Hobbes, 1651"),
        "av": dict(type="liste", titre="Discuter en avocat de l'auteur", items=[
            "Objection : Hobbes fonde l'État sur la crainte ; chacun renonce à agir à sa guise",
            "Réponse : l'État commande les actes, pas les esprits"], marques=["?", "→"], x=170, y=170, w=940),
        "tab_eth": dict(type="tableau", img="t-ethica", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                        legende="Spinoza, Ethica, dans les Opera posthuma, 1677"),
        "conc": dict(type="liste", titre="La conclusion en quatre temps", items=[
            "Bilan : la peur qui domine ≠ la sécurité qui libère", "Réponse : l'État existe pour la liberté",
            "Intérêt : un critère, la liberté de penser et de dire", "Ouverture : Rawls, les libertés d'abord"],
                     marques=["1", "2", "3", "4"], x=170, y=140, w=940),
        "tab_ave": dict(type="tableau", img="dv6-aveugles", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .5],
                        legende="Pieter Bruegel l'Ancien, La Parabole des aveugles, 1568 (Capodimonte, Naples)"),
        "pie": dict(type="liste", titre="Trois pièges", items=[
            "Faire de Spinoza un anarchiste", "Confondre la fin (le but) et l'origine",
            "Réciter Hobbes sans revenir aux mots du texte"], marques=["✗", "✗", "✗"], x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_dam2}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : chaque sujet se joue sur un mot. Ennemi. Peut-on. "
        "Toujours.",
        "{rec.2}Deux : trois distinctions qui dépassent le problème. Liberté naturelle et liberté civile. Se passer de l'État "
        "et se passer d'un maître. Obéissance et servitude.",
        "{rec.3}Trois : des exemples précis. Montréal en 1969, Bucarest en 1989, le consul de Bordeaux en 1940.",
        "{rec.4}Quatre : l'explication de Spinoza. Six éléments d'introduction, puis quoi, comment, pourquoi, en avocat de l'auteur.",
        "{-rec}{-tab_dam2}{tab_fin}{q_fin}À toi : choisis l'un des trois sujets, et fais-en le plan en vingt minutes. "
        "Les questions t'attendent sous la vidéo.",
        "{-q_fin}{fin}",
        ("La prochaine fois : le récapitulatif de toute la série.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_dam2": dict(type="tableau", img="et3-amsterdam", fond=True, sombre=True, de=[1.3, .4, .5], a=[1.0, .5, .5],
                         legende="Gerrit Berckheyde, La Place du Dam et l'hôtel de ville d'Amsterdam, 1672"),
        "rec": dict(type="carte", centre="L'ÉTAT AU BAC", branches=[
            dict(t="Lire le sujet", items=["ennemi · peut-on · toujours", "en fait / en droit"]),
            dict(t="Dépasser", items=["liberté naturelle / civile", "l'État / un maître", "obéissance / servitude"]),
            dict(t="Exemples", items=["Montréal 1969", "Bucarest 1989", "Sousa Mendes 1940"]),
            dict(t="Expliquer Spinoza", items=["six éléments", "quoi, comment, pourquoi", "avocat de l'auteur"])]),
        "tab_fin": dict(type="tableau", img="et7-aube", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .55, .45],
                        legende="Caspar David Friedrich, Matin dans le Riesengebirge, 1810-1811 (château de Charlottenburg, Berlin)"),
        "q_fin": dict(type="question", t="Un sujet, un plan, vingt minutes."),
        "fin": dict(type="titre", sur="À suivre", t="Récap", sous="Épisode 7 · Toute la série en un épisode"),
    }),
]

QUIZ = [
    dict(q="Dans « L'État est-il l'ennemi de la liberté ? », quelle distinction permet de dépasser le problème ?",
         r=["Nécessaire / contingent", "Liberté naturelle / liberté civile", "Prix / dignité", "Croire / savoir"], ok=1,
         voir="lnc", ex="L'État retire la liberté naturelle (limitée par mes seules forces) et donne la liberté civile, garantie par la loi."),
    dict(q="Pourquoi Montréal, le 7 octobre 1969, est-il un bon exemple ?",
         r=["Parce que l'État y a interdit une manifestation", "Parce que seize heures sans police ont suffi à faire basculer la ville",
            "Parce que la ville a voté son indépendance", "Parce que l'armée s'y est révoltée"], ok=1,
         voir="cp1", ex="Un exemple précis pour la deuxième partie : sans État, la liberté de chacun n'est plus protégée (épisode 2)."),
    dict(q="Dans « Peut-on se passer de l'État ? », le verbe « pouvoir » invite à distinguer…",
         r=["le légal et le légitime", "en fait et en droit", "le corps et l'esprit", "la cause et l'effet"], ok=1,
         voir="peut", ex="En fait : est-ce possible ? En droit : est-ce souhaitable ?"),
    dict(q="Quelle troisième partie propose-t-on pour « Peut-on se passer de l'État ? » ?",
         r=["On peut se passer de l'État, il suffit de le vouloir", "On ne se passe pas de l'État, mais on peut se passer de la servitude",
            "Tout dépend des pays", "L'État n'existe pas"], ok=1,
         voir="ets", ex="La Boétie : l'État repose sur notre consentement. Bucarest, 1989 : on renvoie un tyran, on n'abolit pas l'État."),
    dict(q="Qu'a fait Aristides de Sousa Mendes en juin 1940 ?",
         r=["Il a fermé son consulat", "Il a signé des milliers de visas malgré l'ordre de son gouvernement",
            "Il a dénoncé des réfugiés", "Il a pris la tête de l'armée portugaise"], ok=1,
         voir="mendes", ex="Exemple pour la deuxième partie de « Faut-il toujours obéir à l'État ? » : désobéir à un ordre injuste, au prix de sa carrière."),
    dict(q="Selon Spinoza, quelle est la fin de l'État ?",
         r=["Dominer les hommes par la crainte", "La liberté", "La richesse du prince", "La victoire à la guerre"], ok=1,
         voir="c_t3", ex="Traité théologico-politique, XX : non pas faire des hommes des animaux ou des automates, mais leur permettre d'user librement de leur raison."),
    dict(q="Que veut dire « fin » dans « la fin de l'État » ?",
         r=["Sa disparition", "Son but", "Son origine", "Sa dernière loi"], ok=1,
         voir="pie", ex="Un piège classique : la fin, c'est le but, ce en vue de quoi l'État existe."),
    dict(q="Comment répondre, en avocat de Spinoza, à l'objection de Hobbes ?",
         r=["L'État ne doit rien commander", "L'État commande les actes, mais pas les esprits",
            "La crainte est toujours bonne", "Hobbes a toujours raison"], ok=1,
         voir="av", ex="On renonce à agir à sa guise, jamais à penser et à juger : d'où la liberté de penser et de dire ce qu'on pense."),
]

CREDITS = [
    "Portraits : Baruch Spinoza (portrait anonyme, vers 1665) ; Aristides de Sousa Mendes (photographie, 1940, domaine public)",
    "Tableaux et gravures : Eugène Delacroix, La Liberté guidant le peuple (1830) ; "
    "John Seymour Lucas, Les Émeutes de Gordon (1879) ; Albert Eckhout, Homme tupi (1643) ; Gerrit Berckheyde, La place du Dam (1672) ; "
    "Johannes Vermeer, Femme écrivant une lettre et sa servante (vers 1670) ; Rembrandt, Lettré dans son cabinet (1634) ; "
    "Abraham Bosse, frontispice du Léviathan (1651) ; Pieter Bruegel l'Ancien, La Parabole des aveugles (1568) ; Caspar David Friedrich, Matin dans le Riesengebirge (1810-1811) : domaine public",
    "Documents et photographies : Tractatus theologico-politicus (1670) ; Spinoza, Ethica (1677) ; réfugiés à Bordeaux, juin 1940 "
    "(domaine public) ; plaque Sousa Mendes, Bayonne (Michel Bakni, CC BY-SA 4.0) ; Bucarest, décembre 1989 (Musée national d'histoire "
    "de la Roumanie, attribution) ; palais du Parlement, Bucarest (Sludge G, CC BY-SA 2.0) ; salle d'examen (domaine public)",
    "Texte expliqué : Spinoza, Traité théologico-politique, chap. XX (1670), trad. Émile Saisset (Wikisource).",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
