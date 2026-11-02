"""La conscience, épisode 5 : « La conscience morale »

Même format que les séries « La liberté », « Le devoir » et « Le bonheur » (voir liberte_1.py, devoir_3.py).
Citations vérifiées sur Wikisource : Platon, Apologie de Socrate, 31c-d et 38a (trad. Victor Cousin, 1824) ;
Platon, Théétète, 190a, et Gorgias, 482b-c (trad. Émile Chambry) ; Rousseau, Émile, IV, « Profession de foi du vicaire
savoyard » (1762, éd. 1782) ; Kant, Doctrine de la vertu (1797), Iʳᵉ partie, livre I, § 13 (trad. Jules Barni, 1855) ;
Pascal, Pensées, éd. Brunschvicg, fr. 294, 347, 348, 397. Arendt : paraphrase (La Vie de l'esprit ; « Penser et
considérations morales », 1971). Dostoïevski, Crime et Châtiment (1866) : résumé.
"""

CODE = "conscience-5"
NOTION = "La conscience"
NUM = 5
TITRE = "La conscience morale"
SUIVANT = "Épisode 6 · La conscience à l'épreuve du bac"
PRONONCIATION = {"Raskolnikov": "Raskolnikof", "Dostoïevski": "Dostoïefski", "daimôn": "daïmône",
                 "Eichmann": "Aïkmane", "Arendt": "Arènnte", "Théétète": "Téétète", "Gorgias": "Gorguiasse"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="tension", carton=False, beats=[
        "{tab_ras}{q1}Saint-Pétersbourg, un été des années 1860. Un étudiant pauvre, Raskolnikov, tue une vieille usurière "
        "à coups de hache. Il s'est persuadé que les hommes supérieurs ont le droit de franchir les lois ordinaires.",
        "{-q1}{-tab_ras}{tab_spb}{rask}Personne ne le soupçonne. {rask.1}Pas de témoin. {rask.2}Pas de preuve. "
        "{rask.3}Et pourtant, il tombe malade, il délire, il ne supporte plus ni sa mère, ni ses amis, ni lui-même.",
        ("Personne ne l'accuse. Personne… sauf lui.", {"rate": "-8%"}),
        "{-rask}{-tab_spb}{dosto}C'est le roman de Dostoïevski, Crime et Châtiment, publié en 1866. Le vrai châtiment, "
        "ce n'est pas le bagne, qui viendra à la fin. C'est ce tribunal invisible qui siège en lui, jour et nuit.",
        "{-dosto}{q2}Quelle est cette voix qui nous juge, sans qu'on lui ait rien demandé ? On l'appelle la conscience morale.",
        ("P", 0.3),
        "{-q2}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_ras": dict(type="tableau", img="cs5-raskolnikov", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .45, .35],
                        legende="Mikhaïl Klodt, Raskolnikov et Marmeladov, illustration pour Crime et Châtiment, 1874"),
        "q1": dict(type="question", t="Un crime parfait : ni témoin, ni preuve."),
        "tab_spb": dict(type="tableau", img="cs5-petersbourg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .55, .5],
                        legende="Pont de la ligne Saint-Pétersbourg – Moscou, 1860 (photo Iosif Goffert, domaine public)"),
        "rask": dict(type="liste", titre="Raskolnikov, après le crime", items=[
            "Pas de témoin", "Pas de preuve", "… mais il ne se supporte plus lui-même"], marques=["✗", "✗", "!"],
                     x=170, y=170, w=940),
        "dosto": dict(type="portrait", annee=1821, img="dostoievski", nom="Fiodor Dostoïevski", dates="1821 – 1881",
                      legende="Crime et Châtiment (1866)", x=110, y=120, w=330, h=420),
        "q2": dict(type="question", t="Quelle est cette voix qui nous juge ?"),
        "titre": dict(type="titre", sur="La conscience · Épisode 5", t="La conscience morale",
                      sous="Socrate, Rousseau, Kant, Arendt, Pascal"),
    }),

    # ------------------------------------------------------------------ I. Socrate
    dict(id="socrate", chap="Le démon de Socrate", fond="aube", humeur="mystere", notions=["la religion", "la vérité"],
         retenir="Socrate : une voix intérieure qui retient, et une vie qui s'examine sans cesse. Se voir et se juger vont ensemble.",
         beats=[
        "{socrate}{tab_soc}Athènes, 399 avant notre ère. Socrate, soixante-dix ans, comparaît devant ses juges. "
        "On l'accuse de corrompre la jeunesse, et d'introduire des divinités nouvelles. Car Socrate prétend entendre, "
        "depuis toujours, une voix.",
        ("C", "Ce phénomène extraordinaire s'est manifesté en moi dès mon enfance ; c'est une voix qui ne se fait entendre "
              "que pour me détourner de ce que j'ai résolu ; car jamais elle ne m'exhorte à rien entreprendre.", "c_dem"),
        "{-socrate}{-c_dem}{dem}Les Grecs l'appelaient son daimôn : un génie, une sorte de divinité intérieure. "
        "Mais regarde comment elle agit. {dem.1}Elle ne dit jamais : fais ceci. {dem.2}Elle dit seulement : arrête. "
        "N'y va pas. Pas ça.",
        "Tu connais peut-être ce sentiment. Au moment de dire quelque chose de blessant, une petite résistance, "
        "un non silencieux. Socrate y voyait un signe {#la religion}divin. Beaucoup y verront la première figure "
        "de la conscience morale.",
        "{-dem}{-tab_soc}{tab_alc}Et cette voix ne vient pas seule. Sur le temple d'Apollon, à Delphes, on pouvait lire "
        "une inscription que Socrate avait faite sienne : {gnothi}connais-toi toi-même. Toute sa vie est un examen : il interroge "
        "les autres, il les met face à leurs contradictions, et il s'interroge lui-même, sans relâche. "
        "Devant ses juges, il le dit en une phrase.",
        "{-gnothi}",
        ("C", "Une vie sans examen n'est pas une vie.", "c_exa"),
        "{-c_exa}{exa}Voilà le lien entre les deux sens du mot conscience, distingués dans l'épisode un. "
        "{exa.g}Pour me juger, il faut d'abord que je me voie : c'est la conscience psychologique. "
        "{exa.d}Et me voir, c'est déjà me demander si j'agis bien : c'est la conscience morale.",
        ("On ne se juge pas sans se regarder. Et on ne se regarde jamais tout à fait sans se juger.", {"rate": "-5%"}),
        "{-exa}{-tab_alc}",
    ], vis={
        "socrate": dict(type="portrait", annee=-470, img="socrate", nom="Socrate", dates="v. 470 – 399 av. J.-C.",
                        legende="dans l'Apologie de Socrate de Platon", x=110, y=120, w=330, h=420),
        "tab_soc": dict(type="tableau", img="t-socrate", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .45],
                        legende="Jacques-Louis David, La Mort de Socrate, 1787 (Metropolitan Museum, New York)"),
        "c_dem": dict(type="cit", a="Platon", o="Apologie de Socrate, 31c-d, trad. V. Cousin", x=640, y=150, w=570),
        "dem": dict(type="liste", titre="Le daimôn de Socrate", items=[
            "Il ne dit jamais : « fais ceci »", "Il dit seulement : « arrête »"], marques=["✗", "✋"],
                    cles=["arrête"], x=170, y=190, w=940),
        "tab_alc": dict(type="tableau", img="cs5-alcibiade", fond=True, sombre=True, de=[1.0, .2, .4], a=[1.35, .15, .35],
                        legende="Jean-Baptiste Regnault, Socrate arrachant Alcibiade du sein de la Volupté, 1791 (musée du Louvre)"),
        "gnothi": dict(type="mot", t="Connais-toi toi-même", g="inscription du temple d'Apollon à Delphes", y=250, taille=76),
        "c_exa": dict(type="cit", a="Platon", o="Apologie de Socrate, 38a, trad. V. Cousin", x=170, y=230, w=940),
        "exa": dict(type="cols", g="Me voir", gq="la conscience psychologique : savoir ce que je fais",
                    d="Me juger", dq="la conscience morale : me demander si j'agis bien", vs="→",
                    repere="Un seul mot, deux sens liés"),
    }),

    # ------------------------------------------------------------------ II. Rousseau
    dict(id="rousseau", chap="Un instinct divin ?", fond="nuit", humeur="lumiere", notions=["la nature", "la raison", "la justice"],
         retenir="Rousseau : la conscience, principe inné de justice, ne trompe jamais. Objection : les morales varient (Pascal), la voix des parents (Freud).",
         beats=[
        "{rousseau}{tab_vic}Deux mille ans plus tard, Rousseau donne à cette voix ses lettres de noblesse. On a entendu, "
        "dans la série sur le devoir, sa célèbre apostrophe : Conscience ! conscience ! instinct divin. "
        "Allons plus loin. Pourquoi un instinct, et pas un raisonnement ?",
        "Parce que, pour Rousseau, nous sentons avant de penser. Le vicaire savoyard le dit : exister, pour nous, c'est sentir. "
        "Pense à ce qui se passe quand tu vois quelqu'un se faire humilier devant toi : avant tout raisonnement, "
        "quelque chose se serre. C'est au fond de cette sensibilité que Rousseau trouve la conscience.",
        ("C", "Il est donc au fond des âmes un principe inné de justice et de vertu, sur lequel, malgré nos propres maximes, "
              "nous jugeons nos actions et celles d'autrui comme bonnes ou mauvaises ; et c'est à ce principe que je donne "
              "le nom de conscience.", "c_prin"),
        "{-rousseau}{-c_prin}{rc}D'où une opposition frappante. {rc.g}La {#la raison}raison, dit Rousseau, nous trompe trop souvent : "
        "elle sait trouver de bonnes raisons à tout, même au pire. {rc.d}La conscience, elle, ne trompe jamais : "
        "elle est à l'âme ce que l'instinct est au corps.",
        "{-rc}{-tab_vic}{tab_pyr}Mais une objection redoutable se lève. Si la conscience était innée, elle dirait partout "
        "la même chose. Or les morales varient d'un peuple à l'autre, d'un siècle à l'autre. Pascal l'avait noté, avec ironie.",
        ("C", "Plaisante justice qu'une rivière borne ! Vérité au deçà des Pyrénées, erreur au delà.", "c_pyr"),
        "{-c_pyr}{obj}{obj.1}Ce qu'on appelle la voix de la conscience ne serait-il que la voix de l'éducation, de la coutume ? "
        "{obj.2}Freud ira plus loin, on l'a vu dans l'épisode trois : la voix des parents, intériorisée. Le surmoi.",
        "{obj.3}Rousseau répondrait : les coutumes varient, c'est vrai, mais partout on admire la bonne foi, et partout "
        "on méprise la trahison. Les règles changent ; le sentiment du juste et de l'injuste, lui, demeure.",
        "{-obj}{-tab_pyr}",
    ], vis={
        "rousseau": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                         legende="Émile, IV, « Profession de foi du vicaire savoyard » (1762)", x=110, y=120, w=330, h=420),
        "tab_vic": dict(type="tableau", img="cs5-vicaire", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .35],
                        legende="Jean-Michel Moreau le Jeune, Émile et le vicaire savoyard, gravure pour l'Émile, XVIIIᵉ siècle"),
        "c_prin": dict(type="cit", a="Rousseau", o="Émile, IV, « Profession de foi du vicaire savoyard » (1762)",
                       x=640, y=130, w=570),
        "rc": dict(type="cols", g="La raison", gq="nous trompe trop souvent : elle justifie tout",
                   d="La conscience", dq="ne trompe jamais : elle est à l'âme ce que l'instinct est au corps", vs="≠"),
        "tab_pyr": dict(type="tableau", img="cs5-pyrenees", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .6, .45],
                        legende="Stanislaus von Kalckreuth, Paysage de haute montagne dans les Pyrénées, XIXᵉ siècle"),
        "c_pyr": dict(type="cit", a="Pascal", o="Pensées, fr. 294 (éd. Brunschvicg)", x=170, y=220, w=940),
        "obj": dict(type="liste", titre="Une conscience innée ?", items=[
            "L'éducation, la coutume : la conscience varie-t-elle ?",
            "Freud : la voix des parents intériorisée, le surmoi",
            "Rousseau : les règles changent, le sentiment du juste demeure"], marques=["?", "?", "→"],
                    x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ III. Kant
    dict(id="kant", chap="Le tribunal intérieur", fond="aube", humeur="tension", notions=["le devoir", "la religion"],
         retenir="Kant : la conscience est un tribunal intérieur. Elle nous suit comme notre ombre ; on peut ne plus s'en soucier, jamais cesser de l'entendre.",
         beats=[
        "{kant}{tab_ore}Kant, lui, se méfie des instincts. Mais il reprend l'image de la voix, et lui donne une forme précise : "
        "celle d'un procès. Dans la Doctrine de la vertu, en 1797, il écrit :",
        ("C", "Ce tribunal intérieur que l'homme sent en lui (« devant lequel ses pensées s'accusent ou se justifient "
              "mutuellement ») est la conscience.", "c_trib"),
        "{-kant}{-c_trib}{-tab_ore}{tab_jug}{proc}Tout y est, comme dans une salle d'audience. {proc.1}Une loi : le {#le devoir}devoir, "
        "que ma raison connaît. {proc.2}Un accusé : moi, qui ai agi. {proc.3}Un accusateur, et un avocat : mes pensées, "
        "qui m'accusent ou m'excusent. {proc.4}Et un juge, qui rend la sentence : coupable, ou acquitté.",
        "{-proc}{dbl}Mais Kant voit une difficulté. Si l'accusé et le juge sont la même personne, le procès est truqué : "
        "l'accusé gagnerait toujours. {dbl.1}Alors la conscience doit se représenter un autre juge que moi-même : "
        "une personne idéale, que la raison se donne, et qui sonde les cœurs. C'est par là que l'idée de Dieu entre en morale.",
        "{-dbl}{-tab_jug}{tab_ore2}Et ce juge, on ne le fait pas taire. Écoute la suite : elle rappelle le Caïn de Victor Hugo, "
        "rencontré dans la série sur le devoir.",
        ("C", "Elle le suit comme son ombre quand il pense s'y soustraire. Il a beau s'étourdir ou s'endormir au sein des plaisirs "
              "et des distractions ; il ne saurait s'empêcher de faire parfois un retour sur lui-même, ou de se réveiller, "
              "dès qu'il entend sa voix terrible.", "c_ombre"),
        "{-c_ombre}{rask2}Raskolnikov avait beau fuir, la voix le rattrapait. {rask2.1}On peut devenir sourd à sa conscience, "
        "ajoute Kant, au point de ne plus s'en soucier. Mais jamais l'empêcher tout à fait de parler.",
        "{-rask2}{rr}Pour aller plus loin, une distinction utile en copie. {rr.g}Le regret porte sur ce qui est arrivé : "
        "je regrette la pluie, ou le train manqué. {rr.d}Le remords porte sur ce que j'ai fait : il suppose que je me reconnais "
        "l'auteur de l'acte, et que je le juge. Seul un être conscient et libre peut avoir des remords.",
        "{-rr}{-tab_ore2}",
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Doctrine de la vertu (1797)", x=110, y=120, w=330, h=420),
        "tab_ore": dict(type="tableau", img="cs5-oreste", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .45, .4],
                        legende="William-Adolphe Bouguereau, Les Remords d'Oreste, 1862 (Chrysler Museum, Norfolk)"),
        "c_trib": dict(type="cit", a="Kant", o="Doctrine de la vertu, I, livre I, § 13 (1797), trad. J. Barni",
                       x=640, y=170, w=570),
        "tab_jug": dict(type="tableau", img="cs5-juges", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .55, .4],
                        legende="Honoré Daumier, Robert Macaire devant ses juges, lithographie, années 1830 (CC0)"),
        "proc": dict(type="liste", titre="Le procès intérieur", items=[
            "La loi : le devoir, que ma raison connaît", "L'accusé : moi, qui ai agi",
            "L'accusateur et l'avocat : mes pensées", "Le juge : la sentence, coupable ou acquitté"],
                     marques=["§", "1", "2", "3"], x=170, y=140, w=940),
        "dbl": dict(type="def", cles=["truqué", "juge"], terme="Un autre juge que moi",
                    t="Si l'accusé était aussi le juge, le procès serait truqué : il gagnerait toujours.",
                    etape="La conscience se représente un juge idéal, qui sonde les cœurs : l'idée de Dieu.",
                    x=170, y=190, w=940),
        "tab_ore2": dict(type="tableau", img="cs5-oreste", fond=True, sombre=True, de=[1.3, .4, .35], a=[1.05, .5, .5],
                         legende="William-Adolphe Bouguereau, Les Remords d'Oreste, 1862 (Chrysler Museum, Norfolk)"),
        "rr": dict(type="cols", g="Le regret", gq="porte sur ce qui est arrivé : la pluie, le train manqué",
                   d="Le remords", dq="porte sur ce que j'ai fait : je m'en reconnais l'auteur, et je me juge", vs="≠", plus=True),
        "c_ombre": dict(type="cit", a="Kant", o="Doctrine de la vertu, § 13, trad. J. Barni", x=170, y=150, w=940),
        "rask2": dict(type="def", cles=["sourd"], terme="Une voix qu'on ne fait pas taire",
                      t="On peut devenir sourd à sa conscience, au point de ne plus s'en soucier…",
                      etape="… jamais l'empêcher tout à fait de parler.", x=170, y=200, w=940),
    }),

    # ------------------------------------------------------------------ IV. Arendt
    dict(id="arendt", chap="Penser, c'est se parler", fond="nuit", humeur="mystere", notions=["le langage", "la raison"],
         retenir="Arendt : penser, c'est dialoguer avec soi-même. La conscience, c'est ce compagnon avec qui je devrai vivre. Qui ne pense pas peut tout faire.",
         beats=[
        "{arendt}{tab_eic}Saute au vingtième siècle. Dans la série sur le devoir, on a suivi Hannah Arendt au procès "
        "d'Adolf Eichmann, en 1961, et sa formule : la banalité du mal. Le pire peut être commis par des gens ordinaires, "
        "qui ne pensent pas à ce qu'ils font.",
        "Mais qu'est-ce qui manquait à Eichmann ? Pas l'intelligence : c'était un organisateur efficace. "
        "Pas la connaissance des lois. Il lui manquait, dit Arendt, la capacité de penser. Et penser, pour elle, "
        "c'est d'abord un dialogue.",
        "{-arendt}{-tab_eic}{tab_phi}Elle reprend une définition de Platon, dans le Théétète.",
        ("C", "L'âme, quand elle pense, ne fait pas autre chose que s'entretenir avec elle-même, interrogeant et répondant, "
              "affirmant et niant.", "c_the"),
        "{-c_the}{deux}Quand je pense, je suis {!deux en un}deux en un. {deux.1}Je me parle, je me pose des questions, je me réponds. "
        "La pensée est un {#le langage}langage silencieux. {deux.2}Et ce compagnon intérieur, je ne peux pas le quitter : "
        "il est avec moi pour toujours.",
        "{-deux}{-tab_phi}{tab_ath}D'où une phrase de Socrate qu'Arendt aimait citer. Elle se trouve dans le Gorgias.",
        ("C", "Mieux vaudrait pour moi avoir une lyre mal accordée et dissonante, diriger un chœur discordant et me trouver "
              "en opposition et en contradiction avec la plupart des hommes que d'être seul en désaccord avec moi-même "
              "et de me contredire.", "c_lyr"),
        "{-c_lyr}{cons_a}Voilà, selon Arendt, ce qu'est la conscience. {cons_a.1}Celui qui pense ne veut pas devenir un assassin : "
        "il devrait vivre ensuite, nuit et jour, avec un assassin, lui-même. {cons_a.2}Celui qui ne pense jamais n'a pas "
        "ce compagnon. Il peut tout faire, et tout oublier aussitôt.",
        "{cons_a.3}Pour aller plus loin. Sous les dictatures, remarque Arendt, ceux qui ont refusé de participer au crime "
        "n'étaient pas toujours les plus instruits, ni les plus attachés aux règles. C'étaient ceux qui s'étaient demandé : "
        "si je fais cela, pourrai-je encore vivre en paix avec moi-même ?",
        ("Le pire n'est pas commis par des monstres. Il est commis par des gens qui ne se parlent plus.", {"rate": "-5%"}),
        "{-cons_a}{-tab_ath}",
    ], vis={
        "arendt": dict(type="portrait", annee=1906, img="arendt", nom="Hannah Arendt", dates="1906 – 1975",
                       legende="Eichmann à Jérusalem (1963) · La Vie de l'esprit (1978)", x=110, y=120, w=330, h=420),
        "tab_eic": dict(type="tableau", img="dv5-eichmann", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .45, .3],
                        legende="Adolf Eichmann à son procès, Jérusalem, 1961 (Israel Government Press Office, domaine public)"),
        "tab_phi": dict(type="tableau", img="cs5-philosophe", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .4, .6],
                        legende="Rembrandt, Philosophe en méditation, 1632 (musée du Louvre)"),
        "c_the": dict(type="cit", a="Platon", o="Théétète, 190a, trad. É. Chambry", x=170, y=200, w=940),
        "deux": dict(type="liste", titre="Penser : le deux-en-un", items=[
            "Je me parle : questions et réponses", "Ce compagnon intérieur ne me quitte jamais"],
                     marques=["1", "2"], cles=["parle", "compagnon"], x=170, y=190, w=940),
        "tab_ath": dict(type="tableau", img="t-athenes", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.5, .5, .47],
                        legende="Raphaël, L'École d'Athènes, 1509-1511 (Vatican)"),
        "c_lyr": dict(type="cit", a="Socrate, dans Platon", o="Gorgias, 482b-c, trad. É. Chambry", x=170, y=150, w=940),
        "cons_a": dict(type="liste", titre="La conscience selon Arendt", items=[
            "Qui pense ne veut pas vivre avec un assassin : lui-même",
            "Qui ne pense pas n'a pas ce compagnon : il peut tout faire, et tout oublier",
            "Sous la dictature : « pourrai-je encore vivre en paix avec moi-même ? »"], marques=["✓", "✗", "+"],
                       x=170, y=180, w=940),
    }),

    # ------------------------------------------------------------------ V. Pascal
    dict(id="pascal", chap="Un roseau pensant", fond="aube", humeur="lumiere", notions=["la nature", "la vérité"],
         retenir="Pascal : l'homme est un roseau pensant. Toute notre dignité consiste en la pensée. « Travaillons donc à bien penser : voilà le principe de la morale. »",
         beats=[
        "{pascal}{tab_ros}Reste une question. Pourquoi cette voix intérieure aurait-elle tant de prix ? Au dix-septième siècle, "
        "Blaise Pascal, mathématicien et physicien de génie, inventeur d'une machine à calculer, malade toute sa vie, "
        "mort à trente-neuf ans, laisse des notes qui deviendront les Pensées. "
        "Il y répond par l'une des plus belles pages de la langue française.",
        ("C", "L'homme n'est qu'un roseau, le plus faible de la nature ; mais c'est un roseau pensant.", "c_ros"),
        "{-pascal}{-c_ros}{-tab_ros}{tab_nui}{fai}Regarde la scène. {fai.1}D'un côté, l'univers immense, la {#la nature}nature entière : "
        "une vapeur, une goutte d'eau suffit à nous tuer. {fai.2}De l'autre, l'homme, minuscule. Et pourtant, dit Pascal, "
        "quand l'univers l'écraserait, l'homme serait encore plus noble que ce qui le tue. "
        "{fai.3}Parce qu'il sait qu'il meurt. L'univers, lui, n'en sait rien.",
        "{-fai}{dig}Toute notre {!dignité}dignité consiste donc en la pensée. Pas dans l'espace que nous occupons, "
        "ni dans les terres que nous possédons. {dig.1}Par l'espace, dit-il, l'univers me comprend et m'engloutit comme un point ; "
        "par la pensée, je le comprends.",
        "{-dig}{mor}Et Pascal en tire une conséquence qui relie tout cet épisode. {mor.1}Travaillons donc à bien penser : "
        "voilà le principe de la morale. {mor.2}La conscience morale n'est pas un sens à part : c'est la conscience tout court, "
        "quand elle s'applique à bien penser ce que nous faisons.",
        "{mor.3}Pour aller plus loin, une autre pensée : la grandeur de l'homme est grande en ce qu'il se connaît misérable. "
        "Un arbre ne se connaît pas misérable. Se savoir faible, c'est déjà s'élever au-dessus de sa faiblesse.",
        "{-mor}{six}Ce texte du roseau pensant, nous l'expliquerons pas à pas dans l'épisode six : c'est un grand classique du bac.",
        "{-six}{-tab_nui}",
    ], vis={
        "pascal": dict(type="portrait", annee=1623, img="pascal", nom="Blaise Pascal", dates="1623 – 1662",
                       legende="Pensées (1670)", x=110, y=120, w=330, h=420),
        "tab_ros": dict(type="tableau", img="cs5-roseaux", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Roseaux communs au bord d'un lac (photo Joshua Mayer, CC BY-SA 2.0)"),
        "c_ros": dict(type="cit", a="Pascal", o="Pensées, fr. 347 (éd. Brunschvicg ; 1670)", x=640, y=200, w=570),
        "tab_nui": dict(type="tableau", img="cs5-nuit", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .5, .35],
                        legende="Vincent van Gogh, La Nuit étoilée sur le Rhône, 1888 (musée d'Orsay)"),
        "fai": dict(type="liste", titre="Le roseau et l'univers", items=[
            "L'univers : une goutte d'eau suffit à nous tuer", "L'homme : minuscule… et plus noble que ce qui le tue",
            "Car il sait qu'il meurt ; l'univers n'en sait rien"], marques=["1", "2", "3"], x=170, y=150, w=940),
        "dig": dict(type="def", cles=["pensée", "comprends"], terme="La dignité selon Pascal",
                    t="Toute notre dignité consiste en la pensée, non dans l'espace ni dans nos biens.",
                    etape="Par l'espace, l'univers me comprend ; par la pensée, je le comprends.", x=170, y=200, w=940),
        "mor": dict(type="liste", titre="De la pensée à la morale", items=[
            "« Travaillons donc à bien penser : voilà le principe de la morale »",
            "La conscience morale : la conscience qui pense bien ce que nous faisons",
            "Pour aller plus loin : se connaître misérable, c'est être grand (fr. 397)"], marques=["1", "2", "+"],
                    x=170, y=150, w=940),
        "six": dict(type="tag", style="lien", t="Le roseau pensant expliqué pas à pas : épisode 6", x=170, y=560, w=700),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_rec}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : Socrate. Une voix intérieure qui retient, "
        "et une vie qui s'examine sans cesse.",
        "{rec.2}Deux : Rousseau. Un instinct divin, plus sûr que la raison. Mais attention à l'objection : les morales varient, "
        "et la voix de la conscience pourrait n'être que celle de l'éducation.",
        "{rec.3}Trois : Kant. Un tribunal intérieur, qui nous suit comme notre ombre.",
        "{rec.4}Quatre : Arendt et Pascal. Penser, c'est dialoguer avec soi-même ; et toute notre dignité consiste en la pensée.",
        "{-rec}{-tab_rec}{tab_fin}{q_suite}Il est temps de mettre tout cela au travail. Suis-je ce que j'ai conscience d'être ? "
        "Peut-on se connaître soi-même ?",
        "{-q_suite}{fin}",
        ("La prochaine fois : la conscience à l'épreuve du bac. Trois sujets, et le roseau pensant expliqué pas à pas.",
         {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        ("P", 4.5),
    ], vis={
        "tab_rec": dict(type="tableau", img="t-penseur", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.3, .5, .25],
                        legende="Auguste Rodin, Le Penseur, détail de La Porte de l'Enfer, musée Rodin (photo Jebulon, CC0)"),
        "rec": dict(type="carte", centre="LA CONSCIENCE MORALE", branches=[
            dict(t="Socrate", items=["le daimôn : une voix qui retient", "« une vie sans examen n'est pas une vie »"]),
            dict(t="Rousseau", items=["« instinct divin », principe inné", "objection : la coutume, le surmoi"]),
            dict(t="Kant", items=["un tribunal intérieur", "un juge idéal", "« comme son ombre »"]),
            dict(t="Arendt, Pascal", items=["penser : le deux-en-un", "le roseau pensant", "bien penser, principe de la morale"])]),
        "tab_fin": dict(type="tableau", img="cs5-ecole", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .45, .45],
                        legende="Jean Siméon Chardin, La Jeune Maîtresse d'école, vers 1735-1736 (National Gallery, Londres)"),
        "q_suite": dict(type="question", t="Suis-je ce que j'ai conscience d'être ?"),
        "fin": dict(type="titre", sur="À suivre", t="La conscience à l'épreuve du bac",
                    sous="Épisode 6 · Trois sujets, une explication de texte"),
    }),
]

QUIZ = [
    dict(q="Comment agit le daimôn de Socrate ?",
         r=["Il lui dicte ce qu'il doit faire", "Il le détourne de ce qu'il a résolu, sans jamais l'exhorter à agir",
            "Il lui prédit l'avenir", "Il lui donne du courage"], ok=1,
         voir="c_dem", ex="Apologie, 31c-d : une voix qui dit « arrête », jamais « fais ». On y voit la première figure de la conscience morale."),
    dict(q="« Une vie sans examen n'est pas une vie. » Quel lien cette phrase établit-elle ?",
         r=["Entre la conscience et le bonheur", "Entre se voir (conscience psychologique) et se juger (conscience morale)",
            "Entre la raison et la foi", "Entre le corps et l'esprit"], ok=1,
         voir="exa", ex="Pour me juger, il faut que je me voie ; me voir, c'est déjà me demander si j'agis bien."),
    dict(q="Pour Rousseau, la conscience est…",
         r=["un raisonnement appris à l'école", "un principe inné de justice, qui ne trompe jamais",
            "la voix de la société", "une illusion"], ok=1,
         voir="c_prin", ex="Émile, IV : nous sentons avant de penser ; la raison nous trompe souvent, la conscience jamais."),
    dict(q="« Vérité au deçà des Pyrénées, erreur au delà. » Quelle objection Pascal permet-il de faire à Rousseau ?",
         r=["Que la conscience est divine", "Que les morales varient selon les lieux : la conscience serait affaire de coutume",
            "Que les montagnes rendent heureux", "Que la vérité n'existe pas"], ok=1,
         voir="obj", ex="Si la conscience était innée, elle dirait partout la même chose ; Freud y verra la voix des parents intériorisée (le surmoi)."),
    dict(q="Pourquoi, selon Kant, la conscience doit-elle se représenter un autre juge que soi ?",
         r=["Parce que les tribunaux humains sont injustes", "Parce que si l'accusé était aussi le juge, il gagnerait toujours",
            "Parce que Dieu l'ordonne", "Parce que la raison se trompe"], ok=1,
         voir="dbl", ex="Doctrine de la vertu, § 13 : un juge idéal, qui sonde les cœurs ; c'est par là que l'idée de Dieu entre en morale."),
    dict(q="Selon Arendt, qu'est-ce qui manquait à Eichmann ?",
         r=["L'intelligence", "La connaissance des lois", "La capacité de penser, de dialoguer avec soi-même", "Le courage physique"], ok=2,
         voir="deux", ex="Penser, c'est être deux en un (Platon, Théétète) ; qui ne pense pas n'a pas de compagnon intérieur avec qui vivre."),
    dict(q="« L'homme n'est qu'un roseau… mais c'est un roseau pensant. » Pourquoi est-il plus noble que l'univers qui l'écrase ?",
         r=["Parce qu'il est plus fort", "Parce qu'il sait qu'il meurt, et l'univers n'en sait rien",
            "Parce qu'il possède des terres", "Parce qu'il est immortel"], ok=1,
         voir="fai", ex="Pensées, fr. 347 : toute notre dignité consiste en la pensée. « Travaillons donc à bien penser : voilà le principe de la morale. »"),
]

CREDITS = [
    "Portraits : Socrate (buste, copie romaine d'après Lysippe, musée du Louvre, domaine public) ; Dostoïevski (Vassili Perov, 1872) ; "
    "Rousseau (Maurice Quentin de La Tour, 1753) ; Kant (portrait anonyme, XVIIIᵉ s.) ; Hannah Arendt (photographie) ; "
    "Pascal (copie d'après François II Quesnel)",
    "Tableaux et gravures : Mikhaïl Klodt, Raskolnikov et Marmeladov (1874) ; Jacques-Louis David, La Mort de Socrate (1787) ; "
    "Jean-Baptiste Regnault, Socrate arrachant Alcibiade du sein de la Volupté (1791) ; Jean-Michel Moreau le Jeune, "
    "Émile et le vicaire savoyard (gravure) ; Stanislaus von Kalckreuth, Paysage dans les Pyrénées (XIXᵉ s.) ; "
    "William-Adolphe Bouguereau, Les Remords d'Oreste (1862) ; Honoré Daumier, Robert Macaire devant ses juges (lithographie, CC0) ; "
    "Rembrandt, Philosophe en méditation (1632) ; Raphaël, L'École d'Athènes (1509-1511) ; "
    "Vincent van Gogh, La Nuit étoilée sur le Rhône (1888) ; Jean Siméon Chardin, La Jeune Maîtresse d'école (vers 1735-1736) : domaine public",
    "Photographies : pont de la ligne Saint-Pétersbourg – Moscou (Iosif Goffert, 1860, domaine public) ; "
    "Eichmann à son procès (Israel Government Press Office, 1961, domaine public) ; roseaux (Joshua Mayer, CC BY-SA 2.0) ; "
    "Rodin, Le Penseur (Jebulon, CC0)",
    "Citations : Platon, Apologie de Socrate (trad. V. Cousin), Théétète et Gorgias (trad. É. Chambry) ; Rousseau, Émile, IV (1762) ; "
    "Kant, Doctrine de la vertu, § 13 (1797), trad. J. Barni ; Pascal, Pensées, éd. Brunschvicg, fr. 294, 347, 348, 397 : Wikisource. "
    "Arendt : idées résumées, sans citation.",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
