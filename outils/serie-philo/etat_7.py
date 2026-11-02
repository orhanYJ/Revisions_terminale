"""L'État, épisode 7 : « Récap »

Récapitulatif de la série (épisodes 1 à 6), même format que devoir_7.py. Formules et citations reprises des épisodes
précédents : Weber, Le Savant et le Politique (1919), trad. J. Freund (épisode 1) ; Montesquieu, De l'esprit des lois, XI, 4
(1748) (épisode 3) ; Spinoza, Traité théologico-politique, XX (1670), trad. Saisset (épisodes 3 et 6) ;
La Boétie, Discours de la servitude volontaire, orthographe modernisée (épisode 4).
"""

CODE = "etat-7"
NOTION = "L'État"
NUM = 7
TITRE = "Récap"
SUIVANT = ""
PRONONCIATION = {"Ceaușescu": "Tchaouchesscou", "Bucarest": "Bucaresste", "Clastres": "Klastre", "Sousa Mendes": "Souza Mèndèche",
                 "Machiavel": "Makiavel", "Rawls": "Rôlz", "Nietzsche": "Nitche", "Proudhon": "Proudon", "Hume": "Hioume",
                 "Arendt": "Arènnte", "Watergate": "Watèrguéte", "Césène": "Cézène"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="calme", carton=False, beats=[
        "{tab_bou}{q_veil}La veille de l'épreuve. Une bougie, un cahier, et une question : que faut-il vraiment retenir de l'État ?",
        "{-q_veil}{jour}Souviens-toi du début. {jour.1}Une journée ordinaire : le robinet, le bus, le lycée, un sandwich. "
        "{jour.2}Tu n'avais croisé aucun ministre. {jour.3}Et pourtant, l'État était partout.",
        "{-jour}{six}Six épisodes ont essayé de le comprendre. Qu'est-ce que l'État ? Pourquoi existe-t-il ? Protège-t-il "
        "notre liberté, ou la menace-t-il ? Peut-on s'en passer ? Peut-il être juste ? Voici tout le parcours, en quelques minutes.",
        ("P", 0.3),
        "{-six}{-tab_bou}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_bou": dict(type="tableau", img="et7-bougie", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .45],
                        legende="Gerrit Dou, Astronome à la chandelle, fin des années 1650 (J. Paul Getty Museum, Los Angeles)"),
        "q_veil": dict(type="question", t="Que faut-il retenir de l'État ?"),
        "jour": dict(type="liste", titre="Épisode 1 · Le point de départ", items=[
            "Le robinet, le bus, le lycée, un sandwich", "Aucun ministre croisé…", "… et pourtant, l'État partout"],
                     marques=["1", "2", "3"], x=170, y=170, w=940),
        "six": dict(type="mot", t="6 épisodes", g="définir · fonder · limiter · contester · juger · rédiger", y=270),
        "titre": dict(type="titre", sur="L'État · Épisode 7", t="Récap", sous="Toute la série en un épisode"),
    }),

    # ------------------------------------------------------------------ I. définir
    dict(id="definir", chap="Qu'est-ce que l'État ?", fond="aube", humeur="lumiere", notions=["la justice"],
         retenir="L'État : l'institution qui demeure. Le monopole de la violence physique légitime (Weber). Sans légitimité, une bande de brigands.",
         beats=[
        "{tab_lou}{sta}D'abord, le mot. État vient du latin status : ce qui se tient debout, ce qui demeure. "
        "Louis Quatorze, sur son lit de mort, l'aurait dit : je m'en vais, mais l'État demeurera toujours.",
        "{-sta}{dist}{dist.1}L'État n'est pas le gouvernement, qui passe. {dist.2}Ni la nation, un peuple qui veut vivre ensemble. "
        "{dist.3}Ni la société civile, tout ce que les hommes font sans lui. Et commander n'est pas seulement avoir la puissance : "
        "plus un pouvoir a besoin de frapper, moins il a d'autorité.",
        "{-dist}{-tab_lou}{weber}{tab_duel}Puis la définition de Max Weber, en 1919.",
        ("C", "… une communauté humaine qui, dans les limites d'un territoire déterminé, revendique avec succès pour son propre "
              "compte le monopole de la violence physique légitime.", "c_web"),
        "{-weber}{-c_web}{leg}Le mot décisif, c'est légitime. {leg.g}Sans {#la justice}justice, disait saint Augustin, "
        "les royaumes ne sont que de grandes bandes de brigands. {leg.d}Un État légitime est reconnu : on lui obéit par tradition, "
        "par charisme, ou par légalité.",
        "{-leg}{-tab_duel}",
    ], vis={
        "tab_lou": dict(type="tableau", img="et1-louis14", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .3],
                        legende="Hyacinthe Rigaud, Louis XIV en costume de sacre, 1701 (musée du Louvre)"),
        "sta": dict(type="mot", t="STATUS", g="latin : ce qui se tient debout, ce qui demeure", y=250, taille=104),
        "dist": dict(type="liste", titre="Épisode 1 · L'État n'est pas…", items=[
            "le gouvernement, qui passe", "la nation, un peuple qui veut vivre ensemble",
            "la société civile, ce qu'on fait sans lui"], marques=["≠", "≠", "≠"], x=170, y=170, w=940),
        "weber": dict(type="portrait", annee=1864, img="weber", nom="Max Weber", dates="1864 – 1920",
                      legende="Le Savant et le Politique (1919)", x=110, y=120, w=330, h=420),
        "tab_duel": dict(type="tableau", img="et1-duel", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .6],
                         legende="Jean-Léon Gérôme, Le Duel après le bal masqué, vers 1857-1859"),
        "c_web": dict(type="cit", a="Max Weber", o="Le Savant et le Politique (1919), trad. J. Freund", x=640, y=150, w=570),
        "leg": dict(type="cols", g="La force seule", gq="une bande de brigands (saint Augustin)", d="La légitimité",
                    dq="tradition, charisme, légalité (Weber)", vs="≠", repere="Repère · légal / légitime"),
    }),

    # ------------------------------------------------------------------ II. fonder
    dict(id="fonder", chap="Pourquoi l'État ?", fond="nuit", humeur="tension", notions=["la nature", "la raison"],
         retenir="Aristote : la cité est naturelle. Hobbes, Locke, Rousseau : l'État naît d'un contrat. Le contrat n'est pas un fait, mais une idée de la raison.",
         beats=[
        "{tab_gor}{mtl}Montréal, 1969 : seize heures sans police, et la ville bascule. Que serions-nous sans l'État ?",
        "{-mtl}{rep}Quatre réponses. {rep.1}Aristote : l'homme est un animal politique, doué de parole ; la cité est dans sa "
        "{#la nature}nature. {rep.2}Hobbes : sans pouvoir commun, la guerre de chacun contre chacun ; le pacte crée le Léviathan.",
        "{-tab_gor}{tab_lev}{rep.3}Locke : l'État est un juge impartial, gardien de la vie, de la liberté et des biens ; "
        "s'il trahit, on lui résiste. {rep.4}Rousseau : méfie-toi du faux contrat, inventé par le riche pour protéger ses biens ; "
        "dans le vrai, chacun se donne à tous, et le peuple, sous la volonté générale, est souverain.",
        "{-rep}{-tab_lev}{tab_bay}{hyp}Mais ce contrat, qui l'a signé ? Personne, répond Hume : les États naissent de la conquête. "
        "{hyp.1}Le contrat n'est donc pas un fait. C'est une idée, qui permet de juger si un État est légitime.",
        "{-hyp}{-tab_bay}",
    ], vis={
        "tab_gor": dict(type="tableau", img="et2-gordon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .55],
                        legende="John Seymour Lucas, Les Émeutes de Gordon (Londres, 1780), 1879"),
        "mtl": dict(type="question", t="Que serions-nous sans l'État ?"),
        "rep": dict(type="liste", titre="Épisode 2 · Quatre réponses", items=[
            "Aristote : l'homme, animal politique ; la cité est naturelle",
            "Hobbes : la guerre de chacun contre chacun, puis le Léviathan",
            "Locke : un juge impartial, gardien des droits ; le droit de résistance",
            "Rousseau : le peuple souverain, la volonté générale"], marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "tab_lev": dict(type="tableau", img="et2-leviathan", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.2, .5, .5],
                        legende="Abraham Bosse, frontispice du Léviathan de Hobbes, Londres, 1651 (British Library)"),
        "tab_bay": dict(type="tableau", img="et2-bayeux", fond=True, sombre=True, de=[1.0, .3, .5], a=[1.0, .7, .5],
                        legende="Tapisserie de Bayeux, la bataille d'Hastings (1066), vers 1070 (musée de la Tapisserie, Bayeux)"),
        "hyp": dict(type="def", cles=["idée", "légitime"], terme="Le contrat : un fait ?",
                    t="Hume : personne ne l'a signé, les États naissent de la conquête.",
                    etape="Réponse : c'est une idée de la raison, qui sert à juger la légitimité.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ III. limiter
    dict(id="limiter", chap="L'État et la liberté", fond="aube", humeur="mystere", notions=["la liberté", "la vérité"],
         retenir="Montesquieu : le pouvoir arrête le pouvoir. L'État de droit. Spinoza : la fin de l'État, c'est la liberté. Arendt et Orwell : le totalitarisme.",
         beats=[
        "{tab_nix}{mont}Un État assez fort pour nous protéger peut aussi nous écraser. Montesquieu l'a vu.",
        ("C", "… c'est une expérience éternelle, que tout homme qui a du pouvoir est porté à en abuser ; il va jusqu'à ce qu'il "
              "trouve des limites.", "c_mont"),
        "{-mont}{-c_mont}{lim}D'où les remèdes. {lim.1}Séparer les pouvoirs, pour que le pouvoir arrête le pouvoir : "
        "en 1974, un juge oblige un président, Nixon, à céder. {lim.2}L'État de droit, où l'État lui-même obéit au droit : "
        "il y a des juges à Berlin. Car une loi peut être légale… et monstrueuse.",
        "{-lim}{-tab_nix}{tab_ttp}{lim.3}Et Spinoza : on ne commande pas aux esprits. L'État doit laisser chacun penser "
        "et dire ce qu'il pense.{-lim}",
        ("C", "La fin de l'État, c'est donc véritablement la liberté.", "c_spi"),
        "{-c_spi}{-tab_ttp}{tab_sen}{tot}L'inverse, c'est le totalitarisme : tout dans l'État, rien hors de l'État, "
        "rien contre l'État, proclamait Mussolini. {tot.1}Pour Hannah Arendt, il ne veut pas seulement "
        "qu'on obéisse : il veut l'homme tout entier, par l'idéologie, le parti unique et la terreur. {tot.2}Orwell en a fait "
        "un roman, 1984 : le télécran, le ministère de la Vérité, le novlangue. Être libre, écrit Winston, c'est pouvoir dire "
        "que deux et deux font quatre : la {#la vérité}vérité elle-même est en jeu.",
        "{-tot}{-tab_sen}",
    ], vis={
        "tab_nix": dict(type="tableau", img="et3-nixon", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .4],
                        legende="Richard Nixon fait ses adieux au personnel de la Maison-Blanche, 9 août 1974 (photographie officielle, domaine public)"),
        "mont": dict(type="portrait", annee=1689, img="montesquieu", nom="Montesquieu", dates="1689 – 1755",
                     legende="De l'esprit des lois (1748)", x=110, y=120, w=330, h=420),
        "c_mont": dict(type="cit", a="Montesquieu", o="De l'esprit des lois, XI, 4 (1748)", x=640, y=170, w=570),
        "lim": dict(type="liste", titre="Épisode 3 · Limiter l'État", items=[
            "Séparer les pouvoirs : le pouvoir arrête le pouvoir (Watergate, 1974)",
            "L'État de droit : l'État lui-même soumis au droit",
            "Spinoza : on ne commande pas aux esprits"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "tab_ttp": dict(type="tableau", img="et3-ttp", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .35],
                        legende="Tractatus theologico-politicus, « Hambourg » (en réalité Amsterdam), 1670, page de titre"),
        "c_spi": dict(type="cit", a="Spinoza", o="Traité théologico-politique, chap. XX (1670), trad. Saisset", x=170, y=220, w=940),
        "tab_sen": dict(type="tableau", img="et3-senate", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .3],
                        legende="Senate House, Londres : le ministère de l'Information pendant la guerre, modèle du ministère de la Vérité (photo David Dixon, CC BY-SA 2.0)"),
        "tot": dict(type="liste", titre="Le totalitarisme", items=[
            "Arendt (1951) : l'homme tout entier · idéologie, parti unique, terreur",
            "Orwell, 1984 : le télécran, le ministère de la Vérité, « deux et deux font quatre »"],
                    marques=["1", "2"], x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ IV. contester
    dict(id="contester", chap="Contre l'État ?", fond="nuit", humeur="tension", notions=["la liberté", "le travail"],
         retenir="La Boétie : la servitude volontaire. Marx : l'instrument d'une classe. Proudhon, Bakounine : l'ordre sans maître. Nietzsche : le plus froid des monstres froids.",
         beats=[
        "{tab_bal}{boe}Puis les adversaires de l'État. La Boétie, d'abord : le tyran n'a que la force qu'on lui donne. "
        "Bucarest l'a prouvé, en décembre 1989. Et si l'on obéit, c'est par coutume, par divertissement, et parce que "
        "chacun est un peu acheté.",
        ("C", "Soyez résolus de ne servir plus, et vous voilà libres.", "c_boe"),
        "{-boe}{-c_boe}{-tab_bal}{tab_pyr}{con}{con.1}Marx et Engels : l'État est l'instrument de la classe qui possède le capital "
        "et vit du {#le travail}travail des autres ; sans classes, il devrait dépérir. Il n'a jamais dépéri. "
        "{con.2}Proudhon : l'anarchie, l'ordre sans le commandement. Et Bakounine prédit qu'un État ouvrier fabriquera de nouveaux maîtres.",
        "{-tab_pyr}{tab_voy}{con.3}Nietzsche : le plus froid des monstres froids, qui ment en disant : moi, l'État, je suis le peuple. "
        "{con.4}Et Clastres : des sociétés qui ont refusé l'État, où le chef parle mais ne commande pas.",
        "{-con}{-tab_voy}",
    ], vis={
        "tab_bal": dict(type="tableau", img="et4-balcon", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .3],
                        legende="Le balcon du dernier discours de Ceaușescu, envahi par la foule, décembre 1989 (Musée national d'histoire de la Roumanie, attribution)"),
        "boe": dict(type="portrait", annee=1530, img="boetie", nom="Étienne de La Boétie", dates="1530 – 1563",
                    legende="Discours de la servitude volontaire (vers 1548)", x=110, y=120, w=330, h=420),
        "c_boe": dict(type="cit", a="La Boétie", o="Discours de la servitude volontaire, orthographe modernisée", x=640, y=200, w=570),
        "tab_pyr": dict(type="tableau", img="et4-pyramide", fond=True, sombre=True, de=[1.0, .5, .25], a=[1.35, .5, .3],
                        legende="Pyramid of Capitalist System, affiche des Industrial Workers of the World, 1911 (domaine public)"),
        "con": dict(type="liste", titre="Épisode 4 · Contre l'État ?", items=[
            "Marx et Engels : l'instrument d'une classe, qui devrait dépérir",
            "Proudhon, Bakounine : l'ordre sans maître… et la peur de nouveaux maîtres",
            "Nietzsche : « le plus froid de tous les monstres froids »",
            "Clastres : des sociétés contre l'État"], marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "tab_voy": dict(type="tableau", img="et4-voyageur", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.3, .5, .3],
                        legende="Caspar David Friedrich, Le Voyageur contemplant une mer de nuages, vers 1818 (Kunsthalle, Hambourg)"),
    }),

    # ------------------------------------------------------------------ V. juger
    dict(id="juger", chap="L'État et la justice", fond="aube", humeur="lumiere", notions=["la justice", "la raison"],
         retenir="Platon : les philosophes rois. Machiavel : le lion et le renard. L'État-providence redistribue. Rawls : le voile d'ignorance.",
         beats=[
        "{tab_ath}{jus}Alors, un État juste est-il possible ? {jus.1}Platon : la cité juste, c'est chacun à sa place ; "
        "les philosophes devraient être rois. Mais qui gardera les gardiens ? {jus.2}Machiavel : la politique a sa propre logique, "
        "le prince doit être lion et renard. Et Weber demande de tenir ensemble conviction et responsabilité.",
        "{-tab_ath}{tab_doc}{jus.3}Hegel voit dans l'État la raison devenue institution. {jus.4}Et l'État-providence redistribue. Beveridge voulait terrasser cinq géants, "
        "le besoin, la maladie, l'ignorance, l'insalubrité, le chômage : soigner, instruire, protéger chacun, selon la justice distributive.{-jus}",
        "{-tab_doc}{tab_jus}{raw}Enfin Rawls : choisis les règles de la société derrière un voile d'ignorance, sans savoir qui tu seras. "
        "{raw.1}Tout être {#la raison}raisonnable choisirait les mêmes libertés pour tous, et des inégalités seulement "
        "si elles profitent aux plus défavorisés.",
        "{-raw}{-tab_jus}",
    ], vis={
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.6, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511 · au centre, Platon et Aristote"),
        "jus": dict(type="liste", titre="Épisode 5 · Un État juste ?", items=[
            "Platon : les philosophes rois · qui gardera les gardiens ?",
            "Machiavel : le lion et le renard · Weber : conviction et responsabilité",
            "Hegel : la raison devenue institution", "L'État-providence : la justice distributive"],
                    marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "tab_doc": dict(type="tableau", img="et5-docteur", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .5],
                        legende="Luke Fildes, Le Docteur, 1891 (Tate Britain, Londres)"),
        "tab_jus": dict(type="tableau", img="et5-justitia", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.35, .45, .25],
                        legende="Hans Gieng, Justitia, fontaine de la Justice, Berne, 1543 (photo JoachimKohler-HB, CC BY-SA 4.0)"),
        "raw": dict(type="def", cles=["voile d'ignorance", "plus défavorisés"], terme="Rawls · Théorie de la justice (1971)",
                    t="Choisir les règles sans savoir quelle place on occupera.",
                    etape="Les mêmes libertés pour tous ; des inégalités seulement au profit des plus défavorisés.",
                    x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ VI. le jour J
    dict(id="jourj", chap="Le jour J", fond="nuit", humeur="lumiere",
         retenir="Définir, problématiser, distinguer pour dépasser. Une idée, un auteur, un exemple précis.", beats=[
        "{tab_exa}{meth}Le jour J. {meth.1}Définir chaque mot du sujet. {meth.2}Problématiser : une tension, pas une reformulation. "
        "{meth.3}Trois parties, dont la dernière déplace la question grâce à une distinction. {meth.4}Et pour l'explication : "
        "six éléments d'introduction, puis quoi, comment, pourquoi, en avocat de l'auteur.",
        "{-meth}{suj}Des sujets qui reviennent. {suj.1}L'État est-il l'ennemi de la liberté ? {suj.2}Peut-on se passer de l'État ? "
        "{suj.3}Faut-il toujours obéir à l'État ? {suj.4}L'État peut-il être juste ?",
        "{-suj}{dis}Et des distinctions qui dépassent le problème : {dis.1}liberté naturelle et liberté civile, "
        "{dis.2}se passer de l'État et se passer d'un maître, {dis.3}obéissance et servitude.",
        "{-dis}{ex}Et des exemples précis : Montréal en 1969, le Watergate, Bucarest en 1989, le consul de Bordeaux, "
        "la place de Césène, le gâteau partagé.",
        "{-ex}{-tab_exa}{piege}Le piège : réciter Hobbes contre Marx sans répondre à la question. "
        "Un auteur est un outil pour penser, pas un argument d'autorité.",
        "{-piege}",
    ], vis={
        "tab_exa": dict(type="tableau", img="t-examen", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .6],
                        legende="Salle d'examen (domaine public)"),
        "meth": dict(type="liste", titre="Épisode 6 · Le jour de l'épreuve", items=[
            "Définir chaque mot du sujet", "Problématiser : une tension",
            "Trois parties : la dernière déplace la question", "Explication : six éléments, puis quoi · comment · pourquoi"],
                     marques=["1", "2", "3", "4"], x=170, y=130, w=940),
        "suj": dict(type="liste", titre="Des sujets qui reviennent", items=[
            "L'État est-il l'ennemi de la liberté ?", "Peut-on se passer de l'État ?",
            "Faut-il toujours obéir à l'État ?", "L'État peut-il être juste ?"], marques=["?", "?", "?", "?"],
                    x=170, y=150, w=940),
        "dis": dict(type="liste", titre="Trois distinctions qui dépassent", items=[
            "Liberté naturelle / liberté civile", "Se passer de l'État / se passer d'un maître", "Obéissance / servitude"],
                    marques=["≠", "≠", "≠"], x=170, y=170, w=940),
        "ex": dict(type="nuage", items=["Montréal 1969", "le Watergate", "Bucarest 1989", "le consul de Bordeaux",
                                        "la place de Césène", "le gâteau partagé"]),
        "piege": dict(type="note", titre="Le piège", cles=["outil"],
                      t="Réciter Hobbes contre Marx sans répondre à la question. Un auteur est un outil pour penser."),
    }),

    # ------------------------------------------------------------------ VII. fin
    dict(id="fin", chap="Toute la notion", fond="nuit", humeur="lumiere", beats=[
        "{rec}Voici toute la notion, sur une seule carte. {rec.1}Définir : une institution, un monopole, une légitimité. "
        "{rec.2}Fonder : la nature, ou le contrat. {rec.3}Limiter et contester : le pouvoir qui arrête le pouvoir, "
        "la servitude volontaire, les critiques radicales. {rec.4}Juger : un État juste est-il possible ?",
        "{-rec}{frise}Et voici ceux qui t'ont accompagné, de Platon à Rawls : vingt-quatre siècles de pensée.",
        "{-frise}{trois}Si tu ne dois garder que trois phrases : {trois.1}La Boétie, soyez résolus de ne servir plus, "
        "et vous voilà libres. {trois.2}Montesquieu, il faut que le pouvoir arrête le pouvoir. "
        "{trois.3}Et Spinoza : la fin de l'État, c'est la liberté.",
        ("Un dernier mot. Le soir du vingt et un décembre 1989, à Bucarest, il a suffi que des gens cessent d'applaudir. "
         "L'État n'est pas seulement au-dessus de nous. Il est aussi fait de nous.", {"rate": "-5%"}),
        ("Demain, devant ta copie, pense librement. Bonne chance.", {"rate": "-6%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{-trois}{fin}{tab_fin}",
        ("P", 4.5),
    ], vis={
        "rec": dict(type="carte", centre="L'ÉTAT", branches=[
            dict(t="Définir", items=["status : ce qui demeure", "le monopole de la violence légitime", "légal / légitime"]),
            dict(t="Fonder", items=["Aristote : la nature", "Hobbes, Locke, Rousseau : le contrat", "Hume : une fiction ?"]),
            dict(t="Limiter, contester", items=["Montesquieu, l'État de droit", "Spinoza ; Arendt, Orwell", "La Boétie, Marx, Nietzsche"]),
            dict(t="Juger", items=["Platon, Machiavel", "Hegel, l'État-providence", "Rawls : le voile d'ignorance"])]),
        "frise": dict(type="frise", items=[
            dict(nom="Platon", d=-428, img="platon"), dict(nom="Aristote", d=-384, img="aristote"),
            dict(nom="Machiavel", d=1469, img="machiavel"), dict(nom="La Boétie", d=1530, img="boetie"),
            dict(nom="Hobbes", d=1588, img="hobbes"), dict(nom="Spinoza", d=1632, img="spinoza"),
            dict(nom="Locke", d=1632, img="locke"), dict(nom="Montesquieu", d=1689, img="montesquieu"),
            dict(nom="Rousseau", d=1712, img="rousseau"), dict(nom="Hegel", d=1770, img="hegel"),
            dict(nom="Proudhon", d=1809, img="proudhon"), dict(nom="Marx", d=1818, img="marx"),
            dict(nom="Nietzsche", d=1844, img="nietzsche"), dict(nom="Weber", d=1864, img="weber"),
            dict(nom="Arendt", d=1906, img="arendt"), dict(nom="Rawls", d=1921)]),
        "trois": dict(type="liste", titre="Trois phrases à garder", items=[
            "« Soyez résolus de ne servir plus, et vous voilà libres » · La Boétie",
            "« Il faut que, par la disposition des choses, le pouvoir arrête le pouvoir » · Montesquieu",
            "« La fin de l'État, c'est donc véritablement la liberté » · Spinoza"], marques=["1", "2", "3"],
                      x=170, y=170, w=940),
        "tab_fin": dict(type="tableau", img="et4-lorenzetti", fond=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Ambrogio Lorenzetti, Allégorie du bon gouvernement, 1338-1339 (Palazzo Pubblico, Sienne)"),
        "fin": dict(type="titre", sur="L'État", t="Fin de la série", sous="Six épisodes et un récap · bonne épreuve !"),
    }),
]

QUIZ = [
    dict(q="Selon Weber, ce qui définit l'État, c'est…",
         r=["ses buts : la paix, les routes, l'école", "le monopole de la violence physique légitime sur un territoire",
            "le vote des citoyens", "la richesse de la nation"], ok=1,
         voir="c_web", ex="Le Savant et le Politique (1919) : un moyen, non des buts. Et ce monopole doit être reconnu comme légitime (épisode 1)."),
    dict(q="Pour Aristote, la cité est…",
         r=["un contrat entre individus", "naturelle : l'homme est un animal politique", "une invention des tyrans", "inutile"], ok=1,
         voir="rep", ex="La famille, le village, puis la cité : elle achève la nature de l'homme, doué de parole (épisode 2)."),
    dict(q="Que répond-on à Hume, qui objecte que personne n'a jamais signé le contrat social ?",
         r=["Qu'il a été signé en 1789", "Que le contrat est une idée de la raison, qui sert à juger la légitimité",
            "Que Hume a raison et que l'État est illégitime", "Qu'il faut le signer chaque année"], ok=1,
         voir="hyp", ex="Le contrat ne raconte pas la naissance des États : il permet de juger s'ils sont légitimes (Kant)."),
    dict(q="« Il faut que, par la disposition des choses, le pouvoir arrête le pouvoir. » Qui l'a écrit ?",
         r=["Hobbes", "Montesquieu", "Marx", "Platon"], ok=1,
         voir="lim", ex="De l'esprit des lois, XI, 4 : la séparation des pouvoirs. Le Watergate en montre l'efficacité (épisode 3)."),
    dict(q="Selon Spinoza, la fin de l'État est…",
         r=["la domination", "la liberté", "la richesse", "la gloire du prince"], ok=1,
         voir="c_spi", ex="Traité théologico-politique, XX : non pas faire des hommes des bêtes ou des automates, mais leur permettre d'user librement de leur raison."),
    dict(q="Pour La Boétie, pourquoi le peuple sert-il le tyran ?",
         r=["Parce qu'il y est forcé par une armée immense", "Par coutume, par divertissement, par intérêt : la servitude est volontaire",
            "Parce que Dieu l'ordonne", "Parce que le tyran est le plus sage"], ok=1,
         voir="c_boe", ex="« Soyez résolus de ne servir plus, et vous voilà libres » : le colosse privé de sa base s'effondre (épisode 4)."),
    dict(q="Machiavel conseille au prince d'être…",
         r=["toujours bon", "lion et renard", "philosophe", "invisible"], ok=1,
         voir="jus", ex="Le Prince, XVIII : la force du lion, la ruse du renard. La politique a sa logique propre (épisode 5)."),
    dict(q="Derrière le voile d'ignorance de Rawls, quelles inégalités accepterait-on ?",
         r=["Aucune", "Celles qui profitent aux plus défavorisés", "Celles qui enrichissent les plus riches", "Celles qu'on hérite"], ok=1,
         voir="raw", ex="Le principe de différence, après l'égalité des libertés fondamentales (Théorie de la justice, 1971)."),
]

CREDITS = [
    "Portraits : voir les épisodes 1 à 6",
    "Tableaux : Gerrit Dou, Astronome à la chandelle (fin des années 1650) ; Hyacinthe Rigaud, Louis XIV en costume de sacre (1701) ; "
    "Jean-Léon Gérôme, Le Duel après le bal masqué (vers 1857-1859) ; John Seymour Lucas, Les Émeutes de Gordon (1879) ; "
    "Abraham Bosse, frontispice du Léviathan (1651) ; tapisserie de Bayeux (vers 1070) ; Raphaël, L'École d'Athènes (1509-1511) ; "
    "Luke Fildes, Le Docteur (1891) ; Caspar David Friedrich, Le Voyageur contemplant une mer de nuages (vers 1818) ; "
    "Ambrogio Lorenzetti, Allégorie du bon gouvernement (1338-1339) : domaine public",
    "Documents et photographies : Richard Nixon, 9 août 1974 (photographie officielle, domaine public) ; Tractatus theologico-politicus (1670) ; "
    "Senate House, Londres (David Dixon, CC BY-SA 2.0) ; Bucarest, décembre 1989 (Musée national d'histoire de la Roumanie, attribution) ; "
    "Pyramid of Capitalist System (1911) ; Justitia, Berne (JoachimKohler-HB, CC BY-SA 4.0) ; salle d'examen (domaine public)",
    "Citations : Weber, Le Savant et le Politique (1919), trad. J. Freund ; Montesquieu, De l'esprit des lois, XI, 4 (1748) ; "
    "Spinoza, Traité théologico-politique, XX (1670), trad. Saisset ; La Boétie, Discours de la servitude volontaire, orthographe modernisée.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
