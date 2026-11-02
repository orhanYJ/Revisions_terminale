"""La conscience, épisode 1 : « Qu'est-ce que la conscience ? »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#le devoir} dans le texte lu.
Citations : Victor Hugo, « La Conscience », La Légende des siècles (1859) ; Kant, Anthropologie du point de vue
pragmatique, § 1 (1798), trad. A. Renaut (1993), citation courte ; Descartes, Discours de la méthode, V (1637),
texte de l'édition Cousin (Gutenberg), orthographe modernisée.
Résumés par le narrateur : Pierre Coste (note de sa traduction de Locke, 1700), Darwin (La Descendance de l'homme,
chap. III, 1871), la Déclaration de Cambridge sur la conscience (7 juillet 2012), Thomas Nagel (1974), le test du
miroir (Gallup, 1970 ; Amsterdam, 1972).
"""

CODE = "conscience-1"
NOTION = "La conscience"
NUM = 1
TITRE = "Qu'est-ce que la conscience ?"
SUIVANT = "Épisode 2 · Je pense, donc je suis : Descartes, Locke, Hume"
PRONONCIATION = {"conscientia": "konsciennetsia", "scientia": "sciennetsia", "conscius": "konscious",
                 "conscii": "konscii", "consciousness": "konchesnesse", "Gallup": "Galeupe", "Nagel": "Naguel"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_eth}{q_comp}Imagine. Tu es allongé sur une table d'opération. On pose un masque sur ton visage, "
        "et on te demande de compter à rebours, à partir de dix. Dix… neuf… huit…",
        ("Et puis… plus rien.", {"rate": "-8%", "pitch": "-2Hz"}),
        "{-q_comp}{reveil}Tu ouvres les yeux. Une autre salle, une autre lumière. On t'apprend que l'opération a duré deux heures. "
        "{reveil.1}Deux heures ? Pour toi, il ne s'est rien passé. Pas même du noir : rien. "
        "{reveil.2}Pendant ce temps, pourtant, ton cœur battait, tes poumons respiraient. Ton corps vivait.",
        ("Mais il n'y avait personne pour le vivre.", {"rate": "-6%", "pitch": "-2Hz"}),
        "{-reveil}{-tab_eth}{tab_sol}{q_quoi}Qu'est-ce qui s'est éteint, puis rallumé ? Pas la vie : elle n'a jamais cessé. "
        "Autre chose. Ce qui fait que, pour toi, il y a un monde… et un toi qui le voit.",
        "{-q_quoi}Ce quelque chose, les philosophes l'appellent la {!conscience}conscience.",
        "{serie}Rien ne nous est plus proche : nous ne la quittons jamais, sauf dans le sommeil profond. "
        "Et pourtant, rien n'est plus difficile à dire. Cette série va essayer, avec Descartes, Locke, Leibniz, Freud, "
        "Sartre, Kant… Six épisodes, et un récapitulatif. {-serie}Celui-ci commence par le commencement.",
        ("P", 0.3),
        "{-tab_sol}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_eth": dict(type="tableau", img="cs1-ether", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .55],
                        legende="Robert C. Hinckley, La Première Opération sous éther (Boston, 16 octobre 1846), 1882-1893"),
        "q_comp": dict(type="question", t="Dix… neuf… huit… et puis plus rien."),
        "reveil": dict(type="liste", titre="Au réveil", items=[
            "Deux heures ont passé : pour toi, rien. Pas même du noir",
            "Pourtant, ton cœur battait, tes poumons respiraient"], marques=["?", "✓"], x=170, y=170, w=940),
        "tab_sol": dict(type="tableau", img="cs1-soleil", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .45],
                        legende="Claude Monet, Impression, soleil levant, 1872 (musée Marmottan Monet, Paris)"),
        "q_quoi": dict(type="question", t="Qu'est-ce qui s'est éteint, puis rallumé ?"),
        "serie": dict(type="mot", t="6 épisodes + 1 récap", g="ce qui nous est le plus proche… et le plus difficile à dire", y=270),
        "titre": dict(type="titre", sur="La conscience · Épisode 1", t="Qu'est-ce que la conscience ?",
                      sous="Le mot, les degrés, le miroir, les animaux"),
    }),

    # ------------------------------------------------------------------ I. le mot
    dict(id="mot", chap="Le mot", fond="aube", humeur="mystere", notions=["le devoir", "le langage"],
         retenir="Conscience : cum scientia, « savoir avec ». Un seul mot pour deux sens : la conscience psychologique (savoir ce que je vis) et la conscience morale (juger ce que je fais).",
         beats=[
        "{tab_cic}Commençons par le mot. {etym}En latin : conscientia. {etym.1}Cum, c'est « avec ». "
        "{etym.2}Scientia, c'est « le savoir ». La conscience, c'est littéralement un savoir… avec.",
        "{etym.3}Mais avec qui ? D'abord, avec d'autres. À Rome, celui qui est conscius partage un secret : c'est le témoin, "
        "et parfois le complice. Quand Cicéron dénonce la conjuration de Catilina, en 63 avant notre ère, "
        "ceux qui sont dans le secret, ce sont les conscii.",
        "{-etym}{-tab_cic}{tab_lec}{avec}Puis le mot se replie vers l'intérieur. Le témoin, désormais, c'est moi-même. "
        "{avec.1}Je lis cette phrase… {avec.2}et, en même temps, je sais que je la lis. "
        "La conscience, c'est ce savoir qui accompagne tout ce que je vis.",
        "{-avec}{def_c}Retiens une définition simple. La conscience, c'est {def_c.1}la connaissance, plus ou moins claire, "
        "que j'ai de mes pensées, de mes actes, et du monde qui m'entoure.",
        "{-def_c}{-tab_lec}{tab_cain}Mais en français, ce mot a un double. Écoute ce vers de {hugo_t}Victor Hugo. "
        "Après le meurtre de son frère, Caïn s'enfuit avec les siens. Il court des jours et des nuits, il se cache derrière "
        "des murailles, il descend même dans une tombe…",
        "{-hugo_t}",
        ("C", "L'œil était dans la tombe et regardait Caïn.", "c_hugo"),
        "{-c_hugo}{deux}Ici, la conscience ne se contente pas de savoir : {#le devoir}elle juge. "
        "{deux.g}D'un côté, la conscience psychologique : savoir ce que je vis. "
        "{deux.d}De l'autre, la conscience morale : la voix qui me dit que j'ai bien, ou mal, agi.",
        "{-deux}{-tab_cain}{tab_lec2}{ang}L'anglais a deux mots : {ang.1}consciousness, pour la première ; "
        "{ang.2}conscience, pour la seconde. Le français n'en a qu'un. {ang.3}Et ce sens psychologique est assez récent : "
        "en 1700, quand Pierre Coste traduit le philosophe anglais John Locke, il prévient son lecteur qu'il emploie "
        "le mot « conscience » dans un sens nouveau, faute de mieux.",
        ("Un seul mot, donc… mais deux questions très différentes.", {"rate": "-5%"}),
        "{-ang}{plan_cm}Cette série commencera par la première : que sais-je de moi ? "
        "Et elle retrouvera la seconde dans l'épisode cinq : cette voix intérieure qui juge.",
        "{-plan_cm}{-tab_lec2}",
    ], vis={
        "tab_cic": dict(type="tableau", img="cs1-ciceron", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .3, .55],
                        legende="Cesare Maccari, Cicéron dénonce Catilina, 1882-1888 (palais Madame, Rome)"),
        "etym": dict(type="liste", titre="CONSCIENTIA", items=[
            "cum : avec", "scientia : le savoir", "conscius : celui qui partage un secret, le témoin, le complice"],
                     marques=["1", "2", "→"], cles=["avec", "savoir", "témoin"], x=170, y=170, w=940),
        "tab_lec": dict(type="tableau", img="cs1-liseuse", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .35, .45],
                        legende="Jean-Honoré Fragonard, Jeune fille lisant, vers 1769 (National Gallery of Art, Washington)"),
        "avec": dict(type="liste", titre="Un savoir qui accompagne", items=[
            "Je lis cette phrase", "… et je sais que je la lis"], marques=["1", "2"], x=170, y=200, w=940),
        "def_c": dict(type="def", cles=["connaissance", "claire"], terme="La conscience",
                      t="Un savoir « avec » : le témoin intérieur de tout ce que je vis.",
                      etape="La connaissance, plus ou moins claire, que j'ai de mes pensées, de mes actes et du monde.",
                      x=170, y=200, w=940),
        "tab_cain": dict(type="tableau", img="cs1-cain", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .4, .45],
                         legende="Fernand Cormon, Caïn, 1880 (musée d'Orsay, Paris)"),
        "hugo_t": dict(type="mot", t="Victor Hugo", g="« La Conscience », dans La Légende des siècles (1859)", y=250, taille=96),
        "c_hugo": dict(type="cit", a="Victor Hugo", o="« La Conscience », La Légende des siècles (1859)", x=170, y=210, w=940),
        "deux": dict(type="cols", g="Conscience psychologique", gq="savoir ce que je vis, ce que je pense",
                     d="Conscience morale", dq="juger ce que je fais : bien ou mal", vs="≠"),
        "tab_lec2": dict(type="tableau", img="cs1-liseuse", fond=True, sombre=True, de=[1.3, .3, .5], a=[1.05, .5, .5],
                         legende="Jean-Honoré Fragonard, Jeune fille lisant, vers 1769 (National Gallery of Art, Washington)"),
        "ang": dict(type="liste", titre="Un mot, deux sens", items=[
            "Anglais : consciousness, la conscience psychologique", "Anglais : conscience, la conscience morale",
            "Français : un seul mot (sens psychologique fixé vers 1700, Coste traduisant Locke)"],
                    marques=["EN", "EN", "FR"], x=170, y=160, w=940),
        "plan_cm": dict(type="cols", g="Épisodes 1 à 4", gq="que sais-je de moi ? la conscience psychologique",
                        d="Épisode 5", dq="la voix qui juge : la conscience morale", vs="→"),
    }),

    # ------------------------------------------------------------------ II. spontanée / réfléchie
    dict(id="degres", chap="Spontanée ou réfléchie", fond="nuit", humeur="lumiere", notions=["l'inconscient", "la raison"],
         retenir="Conscience spontanée : tournée vers le monde, elle vit. Conscience réfléchie : elle revient sur elle-même, elle se regarde vivre (repère : médiat / immédiat).",
         beats=[
        "{tab_foot}{q_but}Prends un joueur, à l'instant où il frappe le ballon. Est-il conscient ? Bien sûr : il voit le but, "
        "le gardien, l'angle. Mais pense-t-il à lui-même ? Pas une seconde. Il est tout entier dans son geste.",
        "{-q_but}{spon}C'est la conscience spontanée, ou immédiate. {spon.1}Elle est tournée vers le monde, vers ce que je fais. "
        "{spon.2}Je suis conscient du ballon… sans me regarder être conscient.",
        "{-spon}{-tab_foot}{tab_nar}{refl}Après le match, le même joueur revoit l'action et se demande : pourquoi ai-je tiré si vite ? "
        "Là, quelque chose a changé. {refl.1}Il revient sur lui-même. {refl.2}Il fait de sa propre pensée un objet : "
        "il peut la juger, la corriger. C'est là que commence la {#la raison}raison.",
        "{-refl}C'est la conscience réfléchie. Et le mot est bien choisi : réfléchir, c'est d'abord ce que fait un miroir. "
        "{cols_sr}{cols_sr.g}D'un côté, la conscience spontanée, qui vit. {cols_sr.d}De l'autre, la conscience réfléchie, "
        "qui se regarde vivre. La première est immédiate ; la seconde est médiate : elle passe par un retour, un détour.",
        "{-cols_sr}{-tab_nar}{tab_som}{degr}On peut même distinguer des degrés. {degr.1}D'abord, la simple vigilance : "
        "être éveillé, et non endormi ou anesthésié. {degr.2}Ensuite, la conscience du monde : percevoir, sentir, être attentif. "
        "{degr.3}Enfin, la conscience de soi : savoir que c'est moi qui perçois.",
        "{-degr}{auto}Et au-dessous ? {auto.1}Tout ce que je fais sans y penser : marcher, nouer mes lacets, "
        "taper un message sans regarder le clavier. Des gestes appris, devenus des automatismes.",
        ("Conscients ? Pas vraiment. Inconscients ? Pas tout à fait non plus.", {"rate": "-5%"}),
        "{-auto}{-tab_som}{tab_noc}{lien3}Entre la pleine lumière et la nuit, il y a donc toute une pénombre. "
        "Mais y a-t-il en nous, plus bas encore, un {#l'inconscient}inconscient au sens fort, qui pense et désire sans nous ? "
        "Ce sera la question de l'épisode trois.",
        "{-lien3}{-tab_noc}",
    ], vis={
        "tab_foot": dict(type="tableau", img="cs1-football", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .35],
                         legende="Henri Rousseau, Les Joueurs de football, 1908 (musée Guggenheim, New York)"),
        "q_but": dict(type="question", t="Au moment de frapper, pense-t-il à lui-même ?"),
        "spon": dict(type="def", cles=["monde", "immédiate"], terme="La conscience spontanée",
                     t="Immédiate : tournée vers le monde, vers ce que je fais.",
                     etape="Je suis conscient du ballon, sans me regarder être conscient.", x=170, y=200, w=940),
        "tab_nar": dict(type="tableau", img="cs1-narcisse", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .5, .7],
                        legende="Caravage, Narcisse, vers 1597-1599 (Galerie nationale d'art ancien, Rome)"),
        "refl": dict(type="liste", titre="La conscience réfléchie", items=[
            "Je reviens sur moi-même", "Ma pensée devient un objet : je peux la juger, la corriger"],
                     marques=["↺", "→"], x=170, y=190, w=940),
        "cols_sr": dict(type="cols", g="Spontanée", gq="immédiate : elle vit, tournée vers le monde", d="Réfléchie",
                        dq="médiate : elle revient sur soi, elle se regarde vivre", vs="≠", repere="Repère · médiat / immédiat"),
        "tab_som": dict(type="tableau", img="cs1-bohemienne", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .6],
                        legende="Henri Rousseau, La Bohémienne endormie, 1897 (Museum of Modern Art, New York)"),
        "degr": dict(type="liste", titre="Des degrés de conscience", items=[
            "La vigilance : être éveillé", "La conscience du monde : percevoir, être attentif",
            "La conscience de soi : savoir que c'est moi qui perçois"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "auto": dict(type="note", titre="Au-dessous", cles=["automatismes"],
                     t="Marcher, nouer ses lacets, taper sans regarder : des automatismes.",
                     etape="Ni vraiment conscients, ni tout à fait inconscients.", x=170, y=200, w=940),
        "tab_noc": dict(type="tableau", img="cs1-nocturne", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .5],
                        legende="James McNeill Whistler, Nocturne en bleu et or : le vieux pont de Battersea, vers 1872-1875 (Tate, Londres)"),
        "lien3": dict(type="question", t="Y a-t-il en nous un inconscient qui pense sans nous ?"),
    }),

    # ------------------------------------------------------------------ III. le miroir et le « je »
    dict(id="miroir", chap="Le miroir et le « je »", fond="aube", humeur="lumiere", notions=["le langage", "la raison"],
         retenir="Vers 18 mois à 2 ans, l'enfant se reconnaît dans le miroir. Un peu plus tard, il dit « je » : avant, il se sentait ; désormais, il se pense (Kant).",
         beats=[
        "{tab_mir}Comment savoir si un être a conscience de lui-même ? En 1970, un psychologue américain, Gordon Gallup, "
        "imagine un test d'une simplicité géniale.",
        "{test}{test.1}Pendant qu'un chimpanzé est endormi, on lui peint une petite tache rouge au-dessus de l'œil. "
        "{test.2}À son réveil, on lui présente un miroir. {test.3}Que fait-il ? Il touche la tache… sur son propre visage.",
        ("Il a compris : ce singe, dans le miroir… c'est moi.", {"rate": "-5%"}),
        "{-test}{-tab_mir}{tab_mo}{bebe}Le même test, avec un peu de rouge sur le nez, a été fait avec des bébés. "
        "{bebe.1}Avant un an, l'enfant sourit à son reflet comme à un autre bébé. "
        "{bebe.2}Vers dix-huit mois, deux ans, il porte la main à son nez. Il se reconnaît.",
        "{-bebe}{-tab_mo}{kant}{tab_tot}Près de deux siècles plus tôt, Kant avait remarqué une autre étape, plus décisive encore : "
        "le moment où l'enfant commence à dire « je ».",
        "Avant, il parle de lui à la troisième personne : Charles veut manger, Charles veut marcher. "
        "Puis, un jour, il dit : je veux. Et, note Kant, il ne revient jamais en arrière.",
        ("C", "Avant de dire Je, l'enfant avait simplement le sentiment de lui-même ; désormais, il en a la pensée.", "c_kant"),
        "{-c_kant}{-kant}{sentir}Toute la différence est là. {sentir.g}Se sentir : un animal, un bébé, se sentent vivre. "
        "{sentir.d}Se penser : se saisir comme un « je », un sujet unique, le même d'hier à demain. "
        "Et c'est le {#le langage}langage qui scelle ce passage.",
        "{-sentir}{pers}Pour Kant, ce pouvoir de dire « je » élève l'homme infiniment au-dessus des autres vivants. "
        "{pers.1}Il fait de lui une personne : un être qui a une dignité, et qu'on ne traite pas comme une chose. "
        "On l'a vu dans la série sur le devoir.",
        ("P", 0.5),
        "{-pers}{-tab_tot}",
    ], vis={
        "tab_mir": dict(type="tableau", img="cs1-babouin", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .55],
                        legende="Un babouin devant un miroir (photo Moshe Blank, CC BY-SA 3.0)"),
        "test": dict(type="liste", titre="Le test du miroir (Gallup, 1970)", items=[
            "Une tache rouge, peinte pendant le sommeil", "Au réveil, un miroir",
            "L'animal touche la tache sur son propre visage"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_mo": dict(type="tableau", img="cs1-miroir-ovale", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .45, .3],
                       legende="Mary Cassatt, Mère et enfant (le miroir ovale), 1899 (Metropolitan Museum of Art, New York)"),
        "bebe": dict(type="liste", titre="Et les bébés ?", items=[
            "Avant un an : il sourit à « un autre bébé »", "Vers 18 mois – 2 ans : il touche son propre nez"],
                     marques=["✗", "✓"], x=170, y=190, w=940),
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Anthropologie du point de vue pragmatique (1798)", x=110, y=120, w=330, h=420),
        "tab_tot": dict(type="tableau", img="dv4-toton", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .55, .4],
                        legende="Jean Siméon Chardin, L'Enfant au toton, 1738 (musée du Louvre)"),
        "c_kant": dict(type="cit", a="Kant", o="Anthropologie du point de vue pragmatique, § 1 (1798), trad. A. Renaut",
                       x=640, y=170, w=570),
        "sentir": dict(type="cols", g="Se sentir", gq="l'animal, le bébé : se sentir vivre", d="Se penser",
                       dq="se saisir comme un « je », le même d'hier à demain", vs="→"),
        "pers": dict(type="def", cles=["personne", "dignité"], terme="La personne",
                     t="Pouvoir dire « je » élève l'homme au-dessus des autres vivants (Kant).",
                     etape="Une personne a une dignité : on ne la traite pas comme une chose.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. les animaux
    dict(id="animaux", chap="Et les animaux ?", fond="nuit", humeur="mystere", notions=["la nature", "la science", "le langage"],
         retenir="Descartes : l'animal-machine, une différence de nature (l'animal ne parle pas). Darwin : une différence de degré. Déclaration de Cambridge (2012) : les mammifères, les oiseaux, la pieuvre ont les bases de la conscience.",
         beats=[
        "{tab_chi}{q_ani}Le chimpanzé se reconnaît dans le miroir. Ton chat, non. Alors : les animaux ont-ils une conscience ? "
        "{plus_tag}C'est une question pour aller plus loin. Mais elle éclaire toute la notion.",
        "{-q_ani}{-plus_tag}{desc}Au dix-septième siècle, Descartes répond non. Pour lui, l'animal est une machine : "
        "un mécanisme admirable, mais sans pensée. Sa preuve ? La parole.",
        "Une pie, un perroquet peuvent prononcer des mots. Mais aucun animal ne répond à propos, en montrant qu'il pense "
        "ce qu'il dit. Ce que fait pourtant l'homme le plus simple, et même le sourd-muet, qui invente des signes.",
        ("C", "Et ceci ne témoigne pas seulement que les bêtes ont moins de raison que les hommes, "
              "mais qu'elles n'en ont point du tout.", "c_desc"),
        "{-c_desc}{-desc}{-tab_chi}{tab_can}{horl}Et si l'animal fait certaines choses mieux que nous, ajoute Descartes, "
        "cela ne prouve rien. {horl.1}Une horloge, avec ses roues et ses ressorts, compte les heures plus justement que nous. "
        "Elle ne sait pas l'heure pour autant.",
        "{-horl}{am}{am.1}C'est la thèse de l'animal-machine. Un siècle plus tard, l'ingénieur Vaucanson exhibe un canard mécanique "
        "qui bat des ailes, avale du grain… et fait semblant de le digérer. {am.2}Toute l'Europe vient voir la machine qui imite la vie.",
        "{-am}{-tab_can}{darwin}{tab_bea}Deux siècles après Descartes, Charles Darwin renverse la perspective. "
        "Si l'homme descend d'autres espèces, son esprit aussi a une histoire. En 1871, dans La Descendance de l'homme, "
        "il soutient que la différence entre l'esprit de l'homme et celui des animaux supérieurs, si grande soit-elle, "
        "est une différence de degré, et non de nature.",
        "{-darwin}{deg}{deg.g}Descartes : une différence de nature. {deg.d}Darwin : une différence de degré. "
        "Retiens ce couple : il revient souvent en copie.",
        "{-deg}{-tab_bea}{tab_pou}{decl}Et la {#la science}science d'aujourd'hui ? Le 7 juillet 2012, à Cambridge, "
        "des neuroscientifiques signent une déclaration solennelle. {decl.1}Les mammifères, les oiseaux, "
        "et d'autres créatures comme la pieuvre, possèdent les structures nerveuses qui produisent la conscience. "
        "{decl.2}L'homme n'est donc pas le seul à les avoir.",
        "{-decl}{-tab_pou}{tab_chv}{nagel}Mais savoir qu'un animal est conscient, est-ce savoir ce qu'il vit ? "
        "En 1974, le philosophe américain Thomas Nagel pose une question restée célèbre. "
        "{nagel.1}Quel effet cela fait-il d'être une chauve-souris ? {nagel.2}Elle perçoit le monde par l'écho de ses cris. "
        "Nous pouvons tout savoir de son cerveau… sans jamais savoir ce que c'est, de l'intérieur.",
        ("La conscience, c'est peut-être cela : un point de vue que personne ne peut occuper à ma place.",
         {"rate": "-6%", "pitch": "-2Hz"}),
        "{-nagel}{-tab_chv}",
    ], vis={
        "tab_chi": dict(type="tableau", img="cs1-chimpanze", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .45],
                        legende="Jos Schippers, Portrait d'un chimpanzé, fin du XIXᵉ siècle (domaine public)"),
        "q_ani": dict(type="question", t="Les animaux ont-ils une conscience ?"),
        "plus_tag": dict(type="tag", style="plus", t="Pour aller plus loin", x=170, y=560, w=420),
        "desc": dict(type="portrait", annee=1596, img="descartes", nom="René Descartes", dates="1596 – 1650",
                     legende="Discours de la méthode (1637)", x=110, y=120, w=330, h=420),
        "c_desc": dict(type="cit", a="Descartes", o="Discours de la méthode, Ve partie (1637)", x=640, y=150, w=570),
        "tab_can": dict(type="tableau", img="cs1-canard", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.2, .5, .4],
                        legende="Le canard digérateur de Vaucanson (1739), vue intérieure imaginée, gravure du XIXᵉ siècle"),
        "horl": dict(type="note", titre="L'horloge", cles=["horloge", "heure"],
                     t="Une horloge compte les heures mieux que nous… sans savoir l'heure.",
                     etape="Faire mieux qu'un homme ne prouve pas qu'on pense.", x=170, y=170, w=940),
        "am": dict(type="liste", titre="L'animal-machine", items=[
            "L'animal : un mécanisme sans pensée (Descartes)", "Le canard de Vaucanson (1739) : la machine qui imite la vie"],
                   marques=["1", "2"], x=170, y=190, w=940),
        "darwin": dict(type="portrait", annee=1809, img="darwin", nom="Charles Darwin", dates="1809 – 1882",
                       legende="La Descendance de l'homme (1871)", x=110, y=120, w=330, h=420),
        "tab_bea": dict(type="tableau", img="cs1-beagle", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .7, .45],
                        legende="Conrad Martens, Le Beagle, navire de Darwin, en Terre de Feu, 1833"),
        "deg": dict(type="cols", g="Descartes", gq="une différence de nature : l'animal ne pense pas", d="Darwin",
                    dq="une différence de degré : l'esprit a une histoire", vs="≠"),
        "tab_pou": dict(type="tableau", img="cs1-poulpe", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .5, .5],
                        legende="Comingio Merculiano, Octopus vulgaris, planche de G. Jatta, I Cefalopodi, 1896"),
        "decl": dict(type="liste", titre="Déclaration de Cambridge (7 juillet 2012)", items=[
            "Mammifères, oiseaux, pieuvre : les structures nerveuses de la conscience",
            "L'homme n'est pas le seul à les avoir"], marques=["1", "→"], x=170, y=170, w=940),
        "tab_chv": dict(type="tableau", img="cs1-chauvesouris", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .45],
                        legende="Ernst Haeckel, Chiroptera, Kunstformen der Natur, planche 67, 1904"),
        "nagel": dict(type="liste", titre="Thomas Nagel (1974)", items=[
            "Quel effet cela fait-il d'être une chauve-souris ?",
            "Tout savoir de son cerveau… sans savoir ce que c'est, de l'intérieur"],
                      marques=["?", "→"], x=170, y=180, w=940, plus=True),
    }),

    # ------------------------------------------------------------------ V. les grandes questions
    dict(id="questions", chap="Les grandes questions", fond="aube", humeur="tension", notions=["la vérité", "la liberté"],
         retenir="La conscience est ce qui nous est le plus proche… et le plus difficile à connaître. Sans elle, ni vérité pour moi, ni liberté, ni responsabilité.",
         beats=[
        "{tab_neu}{para}Résumons le paradoxe. {para.1}La conscience est ce qu'il y a de plus proche : éveillé, je ne la quitte jamais. "
        "{para.2}Et pourtant, je ne peux ni la voir, ni la toucher, ni la montrer. Ouvre un cerveau : tu y trouves des neurones. "
        "Pas des pensées.",
        "{-para}{enjeu}Et l'enjeu est immense. {enjeu.1}Sans conscience, pas de vérité pour moi : rien ne m'apparaît. "
        "{enjeu.2}Pas de {#la liberté}liberté non plus, ni de responsabilité : on ne juge pas un somnambule comme un homme éveillé.",
        "{-enjeu}{-tab_neu}{tab_moi}{qs}D'où les grandes questions de cette série. "
        "{qs.1}Puis-je être certain de quelque chose, et d'abord de moi ? C'est l'épisode deux, avec Descartes, Locke et Hume. "
        "{qs.2}Ma conscience me dit-elle tout de moi ? L'épisode trois : Leibniz, Freud, Nietzsche. "
        "{qs.3}Suis-je enfermé en moi, ou d'emblée ouvert au monde et aux autres ? L'épisode quatre : Husserl, Sartre, Hegel, Bergson. "
        "{qs.4}Que vaut la voix de la conscience morale ? L'épisode cinq : Socrate, Rousseau, Kant, Arendt, Pascal. "
        "{qs.5}Et l'épisode six : ta copie.",
        ("P", 0.8),
        "{-qs}{-tab_moi}",
    ], vis={
        "tab_neu": dict(type="tableau", img="cs1-neurones", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.35, .3, .4],
                        legende="Santiago Ramón y Cajal, neurones du cervelet, dessin, vers 1894 (domaine public)"),
        "para": dict(type="liste", titre="Le paradoxe de la conscience", items=[
            "Ce qu'il y a de plus proche : je ne la quitte jamais", "Et pourtant : invisible, intouchable, impossible à montrer"],
                     marques=["+", "?"], x=170, y=180, w=940),
        "enjeu": dict(type="liste", titre="L'enjeu", items=[
            "Sans conscience, rien ne m'apparaît : pas de vérité pour moi",
            "Ni liberté, ni responsabilité : le somnambule n'est pas jugé"], marques=["1", "2"], x=170, y=190, w=940),
        "tab_moi": dict(type="tableau", img="cs1-moine", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.0, .7, .5],
                        legende="Caspar David Friedrich, Le Moine au bord de la mer, 1808-1810 (Alte Nationalgalerie, Berlin)"),
        "qs": dict(type="liste", titre="La suite de la série", items=[
            "Ép. 2 · Je pense, donc je suis : Descartes, Locke, Hume",
            "Ép. 3 · La conscience est-elle transparente ? Leibniz, Freud, Nietzsche",
            "Ép. 4 · Conscience, monde et autrui : Husserl, Sartre, Hegel, Bergson",
            "Ép. 5 · La conscience morale : Socrate, Rousseau, Kant, Arendt, Pascal",
            "Ép. 6 · La conscience à l'épreuve du bac"], marques=["2", "3", "4", "5", "6"], x=170, y=120, w=940),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_ret}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : le mot. Conscientia, savoir avec : "
        "la conscience est le savoir qui accompagne tout ce que je vis. Et le même mot désigne la conscience morale.",
        "{rec.2}Deux : la conscience spontanée vit, tournée vers le monde ; la conscience réfléchie revient sur elle-même.",
        "{rec.3}Trois : la conscience de soi. Le miroir, vers dix-huit mois ; le « je », un peu plus tard. "
        "Avant, l'enfant se sentait ; désormais, il se pense.",
        "{rec.4}Quatre : les animaux. Une différence de nature, pour Descartes ; de degré, pour Darwin et pour la science d'aujourd'hui.",
        "{-rec}{-tab_ret}{tab_fin}{q_suite}Reste la question de départ : de quoi puis-je être absolument certain ? "
        "Un homme a décidé un jour de douter de tout… pour le savoir.",
        "{-q_suite}{fin}",
        ("La prochaine fois : je pense, donc je suis. Descartes, Locke, et Hume.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_ret": dict(type="tableau", img="cs1-soleil", fond=True, sombre=True, de=[1.3, .6, .4], a=[1.0, .5, .5],
                        legende="Claude Monet, Impression, soleil levant, 1872 (musée Marmottan Monet, Paris)"),
        "rec": dict(type="carte", centre="LA CONSCIENCE", branches=[
            dict(t="Le mot", items=["cum scientia : savoir avec", "psychologique / morale", "consciousness / conscience"]),
            dict(t="Deux formes", items=["spontanée : elle vit", "réfléchie : elle se regarde", "médiat / immédiat"]),
            dict(t="La conscience de soi", items=["le miroir (18 mois)", "dire « je » (Kant)", "se sentir → se penser"]),
            dict(t="Les animaux", items=["Descartes : l'animal-machine", "Darwin : une différence de degré", "Cambridge (2012), Nagel"])]),
        "tab_fin": dict(type="tableau", img="t2-rembrandt", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .5],
                        legende="Rembrandt, Philosophe en méditation, 1632 (musée du Louvre)"),
        "q_suite": dict(type="question", t="De quoi puis-je être absolument certain ?"),
        "fin": dict(type="titre", sur="À suivre", t="Je pense, donc je suis", sous="Épisode 2 · Descartes, Locke, Hume"),
    }),
]

QUIZ = [
    dict(q="Que signifie, en latin, le mot conscientia ?",
         r=["La lumière intérieure", "Le savoir avec (cum scientia)", "La voix de Dieu", "L'oubli de soi"], ok=1,
         voir="etym", ex="Cum : avec ; scientia : le savoir. Le conscius est d'abord celui qui partage un secret, le témoin ; puis le témoin, c'est moi-même."),
    dict(q="« L'œil était dans la tombe et regardait Caïn. » De quelle conscience parle Victor Hugo ?",
         r=["La conscience psychologique", "La conscience morale", "La conscience spontanée", "La vigilance"], ok=1,
         voir="deux", ex="La conscience qui juge le bien et le mal : en anglais, conscience ; la conscience psychologique se dit consciousness."),
    dict(q="Le joueur absorbé par son geste, qui voit le but sans penser à lui-même, a une conscience…",
         r=["réfléchie", "spontanée", "morale", "inexistante"], ok=1,
         voir="cols_sr", ex="Spontanée, ou immédiate : tournée vers le monde. La conscience réfléchie revient sur elle-même (repère : médiat / immédiat)."),
    dict(q="Que montre le test du miroir de Gallup (1970) ?",
         r=["Que les singes aiment leur reflet", "Qu'un animal peut se reconnaître lui-même",
            "Que les bébés se reconnaissent dès la naissance", "Que la conscience est une illusion"], ok=1,
         voir="test", ex="Le chimpanzé touche la tache sur son propre visage : il se reconnaît. Les bébés y parviennent vers 18 mois – 2 ans."),
    dict(q="Selon Kant, que change le moment où l'enfant commence à dire « je » ?",
         r=["Rien : c'est une habitude de langage", "Avant, il se sentait ; désormais, il se pense",
            "Il devient capable de marcher", "Il perd sa spontanéité"], ok=1,
         voir="c_kant", ex="Anthropologie, § 1 : dire « je », c'est se saisir comme un sujet, une personne, le même à travers les changements."),
    dict(q="Pourquoi Descartes refuse-t-il la pensée aux animaux ?",
         r=["Parce qu'ils n'ont pas de cerveau", "Parce qu'aucun ne parle à propos, en montrant qu'il pense ce qu'il dit",
            "Parce qu'ils ne se reconnaissent pas dans un miroir", "Parce que Dieu le lui a révélé"], ok=1,
         voir="c_desc", ex="Discours de la méthode, V : la pie et le perroquet prononcent des mots, sans parler vraiment. C'est la thèse de l'animal-machine."),
    dict(q="Pour Darwin, la différence entre l'esprit de l'homme et celui des animaux est…",
         r=["une différence de nature", "une différence de degré", "inexistante", "une question de langage seulement"], ok=1,
         voir="deg", ex="La Descendance de l'homme (1871) : si l'homme descend d'autres espèces, son esprit aussi a une histoire. Descartes, lui, y voyait une différence de nature."),
]

CREDITS = [
    "Portraits : Emmanuel Kant (portrait anonyme, XVIIIᵉ s.) ; René Descartes (d'après Frans Hals) ; "
    "Charles Darwin (photographie de Julia Margaret Cameron, vers 1868) : domaine public",
    "Tableaux : Robert C. Hinckley, La Première Opération sous éther (1882-1893) ; Claude Monet, Impression, soleil levant (1872) ; "
    "Cesare Maccari, Cicéron dénonce Catilina (1882-1888) ; Jean-Honoré Fragonard, Jeune fille lisant (vers 1769) ; "
    "Fernand Cormon, Caïn (1880) ; Henri Rousseau, Les Joueurs de football (1908) et La Bohémienne endormie (1897) ; "
    "Caravage, Narcisse (vers 1597-1599) ; James McNeill Whistler, Nocturne en bleu et or (vers 1872-1875) ; "
    "Mary Cassatt, Mère et enfant, le miroir ovale (1899) ; Jean Siméon Chardin, L'Enfant au toton (1738) ; "
    "Jos Schippers, Portrait d'un chimpanzé ; Conrad Martens, Le Beagle en Terre de Feu (1833) ; "
    "Caspar David Friedrich, Le Moine au bord de la mer (1808-1810) ; Rembrandt, Philosophe en méditation (1632) : domaine public",
    "Gravures et dessins : le canard de Vaucanson (gravure du XIXᵉ s.) ; Comingio Merculiano, Octopus vulgaris (1896) ; "
    "Ernst Haeckel, Chiroptera (1904) ; Santiago Ramón y Cajal, neurones du cervelet : domaine public",
    "Photographie : un babouin devant un miroir (Moshe Blank, CC BY-SA 3.0)",
    "Citations : Victor Hugo, La Légende des siècles (1859) ; Kant, Anthropologie du point de vue pragmatique, trad. A. Renaut "
    "(Flammarion, 1993) ; Descartes, Discours de la méthode (1637). Darwin, Nagel, la Déclaration de Cambridge et la note "
    "de Pierre Coste sont résumés par le narrateur.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
