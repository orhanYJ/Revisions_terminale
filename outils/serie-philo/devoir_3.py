"""Le devoir, épisode 3 : « Le devoir selon Kant »

Même format que la série « La liberté » (voir liberte_1.py). Notions abordées : champ notions d'une scène,
repère {#la liberté} dans le texte lu.
Citations de Kant : Fondements de la métaphysique des mœurs (1785), trad. Victor Delbos (1907), vérifiées sur Wikisource.
Benjamin Constant : Des réactions politiques, chap. VIII (1797). Péguy : Victor-Marie, comte Hugo (1910).
"""

CODE = "devoir-3"
NOTION = "Le devoir"
NUM = 3
TITRE = "Le devoir selon Kant"
SUIVANT = "Épisode 4 · Contre le devoir : Nietzsche, Freud, l'utilitarisme"
PRONONCIATION = {"Königsberg": "Keunigsberg"}

SCENES = [
    # ------------------------------------------------------------------ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{tab_epi}{q1}Un enfant de huit ans entre dans une épicerie. Il pose ses pièces sur le comptoir. "
        "Il ne sait pas bien compter, et le marchand le sait.",
        ("Le marchand lui rend sa monnaie. Exactement.", {"rate": "-6%"}),
        "{-q1}{q2}Voilà un honnête homme, pense-t-on. Mais attends. Et s'il ne le faisait que pour sa réputation ? "
        "Un enfant trompé, ça se raconte dans le quartier. Et un quartier qui se méfie, c'est une boutique qui ferme.",
        "{-q2}{-tab_epi}{tab_gru}{q3}Même geste, même monnaie rendue. Et pourtant, une question : "
        "cette action a-t-elle une valeur morale ?",
        "{-q3}{an}Cette question, un professeur de Königsberg l'a posée en 1785, dans un petit livre qui a changé la morale : "
        "les Fondements de la métaphysique des mœurs. Il s'appelait Emmanuel Kant.",
        "{-an}On l'a vu : pour lui, le devoir vient de la raison. Entrons dans sa morale, pas à pas.",
        ("P", 0.3),
        "{-tab_gru}{titre}",
        ("P", 3.2),
    ], vis={
        "tab_epi": dict(type="tableau", img="dv3-epicerie", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .5, .4],
                        legende="Gerrit Dou, L'Épicière de village, 1647 (musée du Louvre)"),
        "q1": dict(type="question", t="Le marchand rend la monnaie exacte à un enfant."),
        "q2": dict(type="question", t="Par honnêteté… ou pour sa réputation ?"),
        "tab_gru": dict(type="tableau", img="dv3-grundlegung", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.25, .5, .4],
                        legende="Kant, Grundlegung zur Metaphysik der Sitten, Riga, 1785, page de titre"),
        "q3": dict(type="question", t="Cette action a-t-elle une valeur morale ?"),
        "an": dict(type="mot", t="1785", g="Kant, Fondements de la métaphysique des mœurs", y=270, taille=104),
        "titre": dict(type="titre", sur="Le devoir · Épisode 3", t="Le devoir selon Kant",
                      sous="La bonne volonté, l'impératif catégorique, le mensonge"),
    }),

    # ------------------------------------------------------------------ I. la bonne volonté
    dict(id="volonte", chap="La bonne volonté", fond="aube", humeur="lumiere", notions=["le bonheur", "la raison"],
         retenir="Rien n'est bon sans restriction, sauf une bonne volonté. Elle vaut par elle-même, pas par ses résultats.", beats=[
        "{kant}{tab_kon}Kant ouvre son livre par une phrase célèbre. Écoute-la bien : tout le reste en découle.",
        ("C", "De tout ce qu'il est possible de concevoir dans le monde, et même en général hors du monde, il n'est rien "
              "qui puisse sans restriction être tenu pour bon, si ce n'est seulement une bonne volonté.", "c_bv"),
        "{-kant}{-c_bv}{-tab_kon}{tab_tri}{dons}Pourquoi seulement la volonté ? Fais la liste de ce qu'on admire d'habitude. "
        "{dons.1}L'intelligence. {dons.2}Le courage. {dons.3}Le sang-froid. {dons.4}La richesse, la santé… et même le {#le bonheur}bonheur.",
        "Tout cela est bon… sauf quand c'est mis au service du mal. Kant le dit d'une formule : "
        "le sang-froid d'un scélérat ne le rend pas seulement plus dangereux, il le rend plus détestable encore.",
        "Regarde ce tricheur : habile, calme, intelligent. Toutes ses qualités servent sa tricherie.",
        "{-dons}{-tab_tri}{tab_per}{q_ech}Une bonne volonté, au contraire, ne peut pas mal tourner. "
        "Et sa valeur ne dépend pas de ce qu'elle réussit. Imagine quelqu'un qui veut de toutes ses forces aider un autre, "
        "et qui échoue, par malchance. Sa volonté a-t-elle perdu sa valeur ? Non, répond Kant.{-q_ech}",
        ("C", "… elle n'en brillerait pas moins, ainsi qu'un joyau, de son éclat à elle, comme quelque chose qui a en soi "
              "sa valeur tout entière.", "c_joy"),
        "{-c_joy}{bv}{bv.1}Voilà le premier geste de Kant. Pour juger une action, ne regarde pas d'abord ses conséquences. "
        "Regarde l'intention.",
        ("Ce qui compte, ce n'est pas ce que tu obtiens. C'est ce que tu veux.", {"rate": "-5%"}),
        "{-bv}{-tab_per}",
    ], vis={
        "kant": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                     legende="Fondements de la métaphysique des mœurs (1785)", x=110, y=120, w=330, h=420),
        "tab_kon": dict(type="tableau", img="t4-konigsberg", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Königsberg, ville de Kant, photochrome, vers 1900 (domaine public)"),
        "c_bv": dict(type="cit", a="Kant", o="Fondements de la métaphysique des mœurs, section I (1785), trad. Delbos",
                     x=640, y=150, w=570),
        "tab_tri": dict(type="tableau", img="dv3-tricheur", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.3, .3, .45],
                        legende="Georges de La Tour, Le Tricheur à l'as de carreau, vers 1635 (musée du Louvre)"),
        "dons": dict(type="liste", titre="Bon… sans restriction ?", items=[
            "L'intelligence", "Le courage", "Le sang-froid", "La richesse, la santé, le bonheur"],
                     marques=["?", "?", "?", "?"], x=170, y=170, w=940),
        "tab_per": dict(type="tableau", img="dv3-perles", fond=True, sombre=True, de=[1.0, .6, .4], a=[1.3, .62, .35],
                        legende="Johannes Vermeer, La Femme au collier de perles, vers 1662-1665 (Gemäldegalerie, Berlin)"),
        "bv": dict(type="def", cles=["intention", "valeur"], terme="La bonne volonté",
                   t="Vouloir le bien, pour lui-même. Sa valeur ne dépend pas du résultat.",
                   etape="Juger une action : regarder l'intention, non les conséquences.", x=170, y=200, w=940),
        "q_ech": dict(type="question", t="Une bonne volonté qui échoue perd-elle sa valeur ?"),
        "c_joy": dict(type="cit", a="Kant", o="Fondements, section I (1785), trad. Delbos", x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ II. par devoir / conformément au devoir
    dict(id="pardevoir", chap="Par devoir, ou conformément au devoir ?", fond="nuit", humeur="tension",
         notions=["la conscience", "le bonheur"],
         retenir="Conforme au devoir : l'action est correcte. Par devoir : le motif est le respect de la loi. Seule la seconde a une valeur morale.",
         beats=[
        "{tab_epi2}Revenons à notre marchand. Il vient de Kant lui-même : c'est son premier exemple. "
        "Le marchand avisé fait un prix fixe, le même pour tout le monde, si bien qu'un enfant achète chez lui "
        "aussi bien que n'importe qui.",
        ("C", "On est donc loyalement servi ; mais ce n'est pas à beaucoup près suffisant pour qu'on en retire cette "
              "conviction que le marchand s'est ainsi conduit par devoir et par des principes de probité ; "
              "son intérêt l'exigeait…", "c_mar"),
        "{-c_mar}{dist}D'où la distinction la plus importante de l'épisode. "
        "{dist.g}Agir conformément au devoir : l'action est correcte, de l'extérieur. "
        "{dist.d}Agir par devoir : le motif lui-même est moral. On fait ce qu'on doit… parce qu'on le doit.",
        ("De l'extérieur, les deux se ressemblent. Toute la différence est à l'intérieur.", {"rate": "-5%"}),
        "{-dist}{-tab_epi2}{tab_gin}{ex}Kant donne deux autres exemples, plus troublants. "
        "{ex.1}Conserver sa vie est un devoir. Mais presque tout le monde aime vivre : ce n'est pas un grand mérite. "
        "Imagine au contraire un homme accablé de chagrin, qui désire la mort… et qui conserve pourtant sa vie, sans l'aimer, "
        "parce qu'il le doit. Là, dit Kant, sa maxime a une valeur morale.",
        "{-tab_gin}{tab_cha}{ex.2}De même, la bienfaisance. Celui qui aide les autres parce que cela lui fait plaisir "
        "agit bien, et il est aimable. Mais celui qui aide, alors que rien ne l'y pousse plus, "
        "uniquement par devoir, celui-là seulement agit moralement.",
        "{-ex}{-tab_cha}{obj}Attention au contresens, fréquent en copie. Kant ne dit pas qu'il faut agir à contrecœur, "
        "ni que le plaisir rend une action mauvaise. Il dit que le plaisir ne peut pas être ce qui fonde sa valeur morale.",
        "{-obj}{tab_gru2}{def_d}D'où sa définition du devoir.",
        ("C", "Le devoir est la nécessité d'accomplir une action par respect pour la loi.", "c_def"),
        "{-c_def}{def_d.1}Le respect : c'est le seul sentiment que Kant admet en morale. Ce n'est pas une envie. "
        "C'est ce que j'éprouve devant une loi qui s'impose à moi, et qui humilie un peu mon amour de moi-même.",
        "Et cela suppose une {#la conscience}conscience lucide : au fond, je ne suis jamais tout à fait sûr de mes motifs. "
        "Kant l'avoue : il n'est peut-être jamais arrivé qu'une action soit faite par pur devoir. "
        "Mais le devoir ne dit pas ce qui se fait. Il dit ce qui doit se faire.",
        "{-def_d}{-tab_gru2}",
    ], vis={
        "tab_epi2": dict(type="tableau", img="dv3-epicerie", fond=True, sombre=True, de=[1.2, .5, .5], a=[1.0, .5, .5],
                         legende="Gerrit Dou, L'Épicière de village, 1647 (musée du Louvre)"),
        "c_mar": dict(type="cit", a="Kant", o="Fondements, section I (1785), trad. Delbos", x=170, y=170, w=940),
        "dist": dict(type="cols", g="Conformément au devoir", gq="l'action est correcte : le marchand intéressé",
                     d="Par devoir", dq="le motif est moral : agir parce qu'on le doit", vs="≠",
                     repere="Repère · par devoir / conformément au devoir"),
        "tab_gin": dict(type="tableau", img="dv3-gin", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .5],
                        legende="William Hogarth, Gin Lane, 1751 (gravure)"),
        "ex": dict(type="liste", titre="Deux exemples de Kant", items=[
            "Conserver sa vie : l'homme accablé qui vit par devoir",
            "La bienfaisance : aider quand rien ne nous y pousse plus"], marques=["1", "2"], x=170, y=170, w=940),
        "tab_cha": dict(type="tableau", img="dv3-charite", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.25, .5, .35],
                        legende="William-Adolphe Bouguereau, La Charité, 1878"),
        "obj": dict(type="note", titre="Contresens à éviter", cles=["contrecœur", "fonde"],
                    t="Kant n'exige pas d'agir à contrecœur : le plaisir n'est pas mauvais, il ne fonde simplement pas la valeur morale."),
        "tab_gru2": dict(type="tableau", img="dv3-grundlegung", fond=True, sombre=True, de=[1.25, .5, .45], a=[1.0, .5, .5],
                         legende="Kant, Grundlegung zur Metaphysik der Sitten, Riga, 1785, page de titre"),
        "def_d": dict(type="def", cles=["respect", "loi"], terme="Le devoir selon Kant",
                      t="La nécessité d'accomplir une action par respect pour la loi.",
                      etape="Le respect : le seul sentiment moral, qui humilie l'amour de soi.", x=170, y=360, w=940),
        "c_def": dict(type="cit", a="Kant", o="Fondements, section I (1785), trad. Delbos", x=170, y=150, w=940),
    }),

    # ------------------------------------------------------------------ III. les impératifs
    dict(id="imperatifs", chap="Deux sortes d'impératifs", fond="aube", humeur="mystere", notions=["la raison", "la technique"],
         retenir="Impératif hypothétique : « si tu veux…, fais… ». Impératif catégorique : « fais », sans condition. Test : puis-je vouloir que ma maxime devienne une loi universelle ?",
         beats=[
        "{tab_ana}Mais comment savoir ce que je dois faire ? Kant part d'une remarque sur la grammaire des ordres.",
        ("C", "Or tous les impératifs commandent ou hypothétiquement ou catégoriquement.", "c_imp"),
        "{-c_imp}{hyp}Premier type : l'impératif hypothétique. Il pose une condition. "
        "Si tu veux réussir ton bac, révise. Si tu veux guérir, prends ce remède. "
        "C'est la logique de la {#la technique}technique : des moyens au service d'une fin.",
        "{hyp.1}Et ces règles sont indifférentes au bien et au mal. Kant le montre avec un exemple glaçant.{-hyp}",
        ("C", "Les prescriptions que doit suivre le médecin pour guérir radicalement son homme, celles que doit suivre "
              "un empoisonneur pour le tuer à coup sûr, sont d'égale valeur…", "c_med"),
        "{-c_med}{-tab_ana}{tab_hor}{imp}{imp.g}D'un côté, donc, l'impératif hypothétique : un moyen pour une fin. "
        "{imp.d}De l'autre, l'impératif catégorique. Lui ne pose aucune condition. "
        "Il ne dit pas : si tu veux être aimé, ne mens pas. Il dit : ne mens pas.",
        ("Point final.", {"rate": "-8%", "pitch": "-1Hz"}),
        "Seul ce commandement-là est moral, car il vaut pour tout être raisonnable, quels que soient ses désirs. "
        "C'est la {!raison}raison qui parle, et non l'envie.",
        "{-imp}Reste à savoir ce qu'il ordonne. Kant le formule ainsi.",
        ("C", "Il n'y a donc qu'un impératif catégorique, et c'est celui-ci : Agis uniquement d'après la maxime qui fait "
              "que tu peux vouloir en même temps qu'elle devienne une loi universelle.", "c_ic"),
        "{-c_ic}{prom}Une maxime, c'est la règle personnelle de mon action. Faisons le test avec l'exemple de Kant. "
        "{prom.1}Je suis dans l'embarras. Je demande de l'argent en promettant de le rendre… en sachant que je ne le rendrai pas.",
        "{prom.2}Ma maxime : quand je suis dans l'embarras, je fais une fausse promesse. "
        "{prom.3}Et si tout le monde faisait ainsi ? Plus personne ne croirait aux promesses. La promesse elle-même disparaîtrait.{-prom}",
        ("C", "Je m'aperçois bientôt ainsi que si je peux bien vouloir le mensonge, je ne peux en aucune manière vouloir "
              "une loi universelle qui commanderait de mentir…", "c_prom"),
        "{-c_prom}{tst}Retiens le test, il est très utile. Le mensonge ne marche que parce que les autres disent la vérité. "
        "Le menteur se fait une exception. Être moral, c'est refuser de faire de soi une exception.",
        "{-tst}{-tab_hor}",
    ], vis={
        "imp": dict(type="cols", g="Impératif hypothétique", gq="« Si tu veux…, fais… » : un moyen pour une fin",
                    d="Impératif catégorique", dq="« Fais » : sans condition, pour tout être raisonnable", vs="≠",
                    repere="Repère · hypothétique / catégorique"),
        "c_imp": dict(type="cit", a="Kant", o="Fondements, section II (1785), trad. Delbos", x=170, y=170, w=940),
        "hyp": dict(type="def", cles=["condition", "moyen"], terme="L'impératif hypothétique",
                    t="« Si tu veux…, fais… » : un moyen en vue d'une fin.",
                    etape="Les règles de l'habileté : indifférentes au bien et au mal.", x=170, y=200, w=940),
        "tab_ana": dict(type="tableau", img="dv3-anatomie", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .55, .5],
                        legende="Rembrandt, La Leçon d'anatomie du docteur Tulp, 1632 (Mauritshuis, La Haye)"),
        "c_med": dict(type="cit", a="Kant", o="Fondements, section II (1785), trad. Delbos", x=170, y=170, w=940),
        "tab_hor": dict(type="tableau", img="dv3-horaces", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.25, .45, .4],
                        legende="Jacques-Louis David, Le Serment des Horaces, 1784 (musée du Louvre)"),
        "c_ic": dict(type="cit", a="Kant", o="Fondements, section II (1785), trad. Delbos", x=170, y=170, w=940),
        "prom": dict(type="liste", titre="Le test de la fausse promesse", items=[
            "La situation : emprunter en promettant de rendre, sans le vouloir",
            "La maxime : « dans l'embarras, je fais une fausse promesse »",
            "Universalisée : plus personne ne croit aux promesses"], marques=["1", "2", "3"], x=170, y=120, w=940),
        "c_prom": dict(type="cit", a="Kant", o="Fondements, section I (1785), trad. Delbos", x=170, y=170, w=940),
        "tst": dict(type="note", titre="Le test de l'universalisation", cles=["exception"],
                    t="Et si tout le monde faisait comme moi ? Le menteur se fait une exception : la morale le lui refuse."),
    }),

    # ------------------------------------------------------------------ IV. l'humanité comme fin
    dict(id="humanite", chap="Jamais simplement comme un moyen", fond="nuit", humeur="lumiere",
         notions=["la justice", "le travail", "la liberté"],
         retenir="Traiter l'humanité toujours en même temps comme une fin, jamais simplement comme un moyen. Les choses ont un prix, les personnes une dignité.",
         beats=[
        "{tab_dau}Kant donne une deuxième formule du même impératif. C'est peut-être la plus belle phrase de la morale moderne.",
        ("C", "Agis de telle sorte que tu traites l'humanité aussi bien dans ta personne que dans la personne de tout autre "
              "toujours en même temps comme une fin, et jamais simplement comme un moyen.", "c_hum"),
        "{-c_hum}{fm}Pèse deux mots, que l'on oublie souvent en citant cette phrase : {fm.1}« simplement », "
        "et {fm.2}« en même temps ». Kant ne dit pas qu'on ne doit jamais se servir des autres.",
        "{-fm}{-tab_dau}{tab_rab}Quand j'achète mon pain, je me sers du boulanger, et son {#le travail}travail me sert de moyen. "
        "Rien de mal à cela… tant que je le respecte aussi comme une personne : je le paie, je ne le trompe pas, je ne l'humilie pas.",
        "Ce qui est interdit, c'est de traiter quelqu'un simplement comme un outil : l'esclavage, la manipulation, "
        "le chantage. L'autre n'est plus qu'une chose.",
        "{-tab_rab}{tab_whi}{pd}Pourquoi les personnes méritent-elles ce respect ? Parce qu'elles n'ont pas de prix.",
        ("C", "Ce qui a un prix peut être aussi bien remplacé par quelque chose d'autre, à titre d'équivalent ; au contraire, "
              "ce qui est supérieur à tout prix, ce qui par suite n'admet pas d'équivalent, c'est ce qui a une dignité.", "c_dig"),
        "{-c_dig}{pd.g}Un téléphone a un prix : on peut le remplacer. {pd.d}Une personne a une {!dignité}dignité : "
        "on ne la remplace pas, on ne l'achète pas. Voilà l'origine de notre idée des droits de l'homme, "
        "et d'une certaine idée de la justice.",
        "{-pd}{-tab_whi}{tab_kt}{q_dig}Et d'où vient cette dignité ? De ce que l'homme est capable de se donner sa propre loi. "
        "Kant l'écrit dès la première section.{-q_dig}",
        ("C", "L'objet du respect est donc simplement la loi, loi telle que nous nous l'imposons à nous-mêmes, "
              "et cependant comme nécessaire en soi.", "c_resp"),
        "{-c_resp}{aut}{aut.1}C'est l'autonomie. On l'a vue dans la série sur la liberté, avec l'expérience du gibet : "
        "obéir au devoir, ce n'est pas se soumettre à un maître, c'est obéir à sa propre raison.",
        ("Le devoir ne me retire pas ma liberté. Il en est la preuve.", {"rate": "-5%"}),
        "{-aut}{-tab_kt}",
    ], vis={
        "tab_dau": dict(type="tableau", img="dv3-daumier", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .4, .5],
                        legende="Honoré Daumier, Le Wagon de troisième classe, vers 1862-1864 (Metropolitan Museum, New York)"),
        "c_hum": dict(type="cit", a="Kant", o="Fondements, section II (1785), trad. Delbos", x=170, y=170, w=940),
        "fm": dict(type="liste", titre="Deux mots à peser", items=[
            "« simplement » : se servir des autres n'est pas interdit",
            "« en même temps » : à condition de les respecter aussi comme des personnes"],
                   marques=["1", "2"], cles=["simplement", "en même temps"], x=170, y=200, w=940),
        "tab_rab": dict(type="tableau", img="dv3-raboteurs", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.25, .5, .6],
                        legende="Gustave Caillebotte, Les Raboteurs de parquet, 1875 (musée d'Orsay)"),
        "tab_whi": dict(type="tableau", img="dv3-whitechapel", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.3, .5, .5],
                        legende="Gustave Doré, Wentworth Street, Whitechapel, dans London, a Pilgrimage, 1872"),
        "c_dig": dict(type="cit", a="Kant", o="Fondements, section II (1785), trad. Delbos", x=170, y=150, w=940),
        "pd": dict(type="cols", g="Un prix", gq="les choses : remplaçables, échangeables", d="Une dignité",
                   dq="les personnes : sans équivalent", vs="≠", repere="Repère · prix / dignité"),
        "tab_kt": dict(type="tableau", img="t4-kant-table", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                       legende="Emil Doerstling, Kant et ses convives, 1892-1893 (reproduction)"),
        "aut": dict(type="def", cles=["autonomie", "propre loi"], terme="L'autonomie",
                    t="Obéir à la loi que ma raison se donne : la source de la dignité.",
                    etape="Voir la série « La liberté », épisode 4 : l'expérience du gibet.", x=170, y=200, w=940),
        "q_dig": dict(type="question", t="D'où vient la dignité ?"),
        "c_resp": dict(type="cit", a="Kant", o="Fondements, section I (1785), trad. Delbos", x=170, y=170, w=940),
    }),

    # ------------------------------------------------------------------ V. le mensonge
    dict(id="mensonge", chap="Le droit de mentir ?", fond="aube", humeur="tension", notions=["la vérité", "l'État"],
         retenir="Constant : la vérité n'est due qu'à ceux qui y ont droit. Kant : jamais de droit de mentir. Objection : un rigorisme aux mains pures… sans mains.",
         beats=[
        "{tab_por}{q_ass}Voici le cas qui a valu à Kant le plus de critiques. "
        "Un ami poursuivi se cache chez toi. Un assassin frappe à ta porte et demande : est-il ici ?",
        ("Dois-tu mentir ?", {"rate": "-8%"}),
        "{-q_ass}{constant}En 1797, un jeune penseur libéral, Benjamin Constant, prend cet exemple contre, dit-il, "
        "« un philosophe allemand ». Pour lui, dire la vérité ne peut pas être un devoir absolu.",
        ("C", "Le principe moral que dire la vérité est un devoir, s'il était pris d'une manière absolue et isolée, "
              "rendrait toute société impossible.", "c_con"),
        "La {#la vérité}vérité, ajoute Constant, n'est due qu'à ceux qui y ont droit. Et l'assassin n'y a aucun droit.",
        "{-constant}{-c_con}{rep}Kant répond la même année, dans un court texte : Sur un prétendu droit de mentir par humanité. "
        "Sa réponse est intransigeante. {rep.1}La véracité est un devoir envers tous, quelles qu'en soient les conséquences.",
        "{rep.2}Car le mensonge, même pour le bien, ruine la confiance dont vit toute parole humaine, "
        "et donc la possibilité même des contrats et du droit.",
        "{rep.3}Et puis, je ne maîtrise pas les conséquences. Si je mens, et que mon ami, sans que je le sache, "
        "s'est enfui par la fenêtre, je peux l'envoyer droit vers son assassin. Alors, dit Kant, j'en suis responsable.",
        "{-rep}{-tab_por}{tab_dio}{rig}Beaucoup de lecteurs ont jugé cette réponse inhumaine. On parle de rigorisme : "
        "une morale si pure qu'elle refuse de se salir les mains, quitte à laisser faire le mal.",
        "Charles Péguy en a fait une formule cruelle.",
        ("C", "Le kantisme a les mains pures, mais il n'a pas de mains.", "c_peg"),
        "{-c_peg}{-rig}{def_k}Pourtant, Kant tient bon sur un point fort. Si chacun s'accorde le droit de mentir dès qu'il juge "
        "la cause bonne, qui décidera de ce qui est une bonne cause ? Le pouvoir, la propagande, et parfois {#l'État}l'État lui-même, "
        "mentent toujours au nom du bien.",
        "{-def_k}{q_fin}La question reste ouverte, et c'est un excellent sujet de dissertation : "
        "le devoir doit-il tenir compte des conséquences ? Les utilitaristes répondront oui, dans l'épisode suivant.",
        "{-q_fin}{-tab_dio}",
    ], vis={
        "tab_por": dict(type="tableau", img="dv3-portes", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.3, .45, .5],
                        legende="Vilhelm Hammershøi, Portes blanches, Strandgade 25, 1913"),
        "q_ass": dict(type="question", t="Un assassin demande où se cache ton ami. Dois-tu mentir ?"),
        "constant": dict(type="portrait", annee=1767, img="constant", nom="Benjamin Constant", dates="1767 – 1830",
                         legende="Des réactions politiques (1797)", x=110, y=120, w=330, h=420),
        "c_con": dict(type="cit", a="Benjamin Constant", o="Des réactions politiques, chap. VIII (1797)", x=640, y=170, w=570),
        "rep": dict(type="liste", titre="La réponse de Kant (1797)", items=[
            "La véracité : un devoir envers tous, quelles que soient les conséquences",
            "Le mensonge ruine la confiance, les contrats, le droit",
            "Je ne maîtrise pas les conséquences : j'en deviens responsable"], marques=["1", "2", "3"],
                    x=170, y=150, w=940),
        "tab_dio": dict(type="tableau", img="dv3-diogene", fond=True, sombre=True, de=[1.0, .5, .55], a=[1.3, .5, .65],
                        legende="John William Waterhouse, Diogène, 1882 (Art Gallery of New South Wales, Sydney)"),
        "rig": dict(type="def", cles=["rigorisme"], terme="Le rigorisme",
                    t="Appliquer la règle sans exception, quelles qu'en soient les conséquences.",
                    etape="L'objection classique adressée à Kant.", x=170, y=170, w=940),
        "c_peg": dict(type="cit", a="Charles Péguy", o="Victor-Marie, comte Hugo (1910)", x=170, y=430, w=940),
        "def_k": dict(type="note", titre="Pour défendre Kant", cles=["bonne cause"],
                      t="Si chacun peut mentir pour une « bonne cause », qui décide de ce qu'est une bonne cause ?"),
        "q_fin": dict(type="question", t="Le devoir doit-il tenir compte des conséquences ?"),
    }),

    # ------------------------------------------------------------------ VI. à retenir
    dict(id="retenir", chap="À retenir", fond="nuit", humeur="lumiere", beats=[
        "{tab_tom}{rec}Ce qu'il faut retenir de cet épisode. {rec.1}Un : rien n'est bon sans restriction, sauf une bonne volonté. "
        "On juge l'intention, pas le résultat.",
        "{rec.2}Deux : agir conformément au devoir n'est pas agir par devoir. Le marchand honnête par intérêt n'a pas de mérite moral.",
        "{rec.3}Trois : l'impératif catégorique. Agir d'après une maxime que je peux vouloir comme loi universelle, "
        "et traiter l'humanité toujours en même temps comme une fin, jamais simplement comme un moyen.",
        "{rec.4}Quatre : le mensonge. Kant refuse tout droit de mentir ; Constant et Péguy lui reprochent son rigorisme.",
        "{-rec}{-tab_tom}{tab_fin}Une morale exigeante, peut-être trop. Ses adversaires vont l'attaquer de front : "
        "et si le devoir n'était qu'une dette, une peur, ou un mauvais calcul ?",
        ("La prochaine fois : contre le devoir. Nietzsche, Freud, et l'utilitarisme.", {"rate": "-4%", "pitch": "+1Hz"}),
        ("P", 1.0),
        "{fin}",
        ("P", 4.5),
    ], vis={
        "tab_tom": dict(type="tableau", img="dv3-tombe", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                        legende="Tombeau de Kant contre la cathédrale de Königsberg, aujourd'hui Kaliningrad (photo J110, domaine public)"),
        "rec": dict(type="carte", centre="LE DEVOIR SELON KANT", branches=[
            dict(t="La bonne volonté", items=["seule bonne sans restriction", "l'intention, pas le résultat"]),
            dict(t="Par devoir", items=["≠ conformément au devoir", "le marchand intéressé", "le respect de la loi"]),
            dict(t="L'impératif catégorique", items=["loi universelle", "jamais simplement un moyen", "prix / dignité"]),
            dict(t="Le mensonge", items=["Constant (1797)", "aucun droit de mentir", "rigorisme (Péguy)"])]),
        "tab_fin": dict(type="tableau", img="dv3-voielactee", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .5, .55],
                        legende="Étienne Léopold Trouvelot, Une partie de la Voie lactée, 1881-1882 (domaine public)"),
        "fin": dict(type="titre", sur="À suivre", t="Contre le devoir", sous="Épisode 4 · Nietzsche, Freud, l'utilitarisme"),
    }),
]

QUIZ = [
    dict(q="Selon Kant, qu'est-ce qui seul peut être tenu pour bon sans restriction ?",
         r=["Le bonheur", "L'intelligence", "Une bonne volonté", "Le courage"], ok=2,
         voir="c_bv", ex="Les talents et même le bonheur peuvent servir le mal (le sang-froid du scélérat). Seule une bonne volonté est bonne en elle-même, comme un joyau."),
    dict(q="Le marchand qui ne trompe pas l'enfant parce que c'est son intérêt agit…",
         r=["par devoir", "conformément au devoir", "contre le devoir", "par inclination immédiate"], ok=1,
         voir="dist", ex="L'action est correcte de l'extérieur, mais son motif est l'intérêt : elle n'a pas de valeur morale. Repère : par devoir / conformément au devoir."),
    dict(q="« Si tu veux guérir, prends ce remède » est un impératif…",
         r=["catégorique", "hypothétique", "moral", "universel"], ok=1,
         voir="imp", ex="Il pose une condition (une fin à atteindre) : c'est une règle de l'habileté, valable aussi bien pour le médecin que pour l'empoisonneur."),
    dict(q="Pourquoi la fausse promesse ne passe-t-elle pas le test de l'universalisation ?",
         r=["Parce qu'elle a de mauvaises conséquences pour moi",
            "Parce que, si tout le monde mentait, plus personne ne croirait aux promesses",
            "Parce que la loi l'interdit", "Parce que Dieu l'interdit"], ok=1,
         voir="prom", ex="Universalisée, ma maxime se détruit elle-même : la promesse disparaîtrait. Le menteur se fait une exception."),
    dict(q="Payer le boulanger pour avoir du pain, est-ce contraire à la deuxième formule de l'impératif ?",
         r=["Oui : je me sers de lui comme d'un moyen", "Non : je ne le traite pas simplement comme un moyen",
            "Oui : tout échange est immoral", "Non : la morale ne concerne pas le commerce"], ok=1,
         voir="fm", ex="Kant dit « jamais simplement comme un moyen » et « toujours en même temps comme une fin » : se servir des autres n'est pas interdit si on les respecte comme personnes."),
    dict(q="Selon Kant, ce qui n'admet pas d'équivalent a…",
         r=["un prix", "une dignité", "une utilité", "une valeur marchande"], ok=1,
         voir="pd", ex="Les choses ont un prix, on peut les remplacer ; les personnes ont une dignité, supérieure à tout prix."),
    dict(q="Que reproche Benjamin Constant à Kant en 1797 ?",
         r=["De mentir trop souvent", "De faire de la véracité un devoir absolu, qui rendrait toute société impossible",
            "De ne pas croire en Dieu", "De fonder la morale sur le bonheur"], ok=1,
         voir="c_con", ex="Pour Constant, la vérité n'est due qu'à ceux qui y ont droit ; l'assassin n'y a pas droit. Kant répond qu'il n'existe aucun droit de mentir."),
    dict(q="« Le kantisme a les mains pures, mais il n'a pas de mains » : que reproche Péguy à Kant ?",
         r=["Son athéisme", "Son rigorisme : une morale si pure qu'elle n'agit plus dans le monde",
            "Son goût pour le bonheur", "Sa défense du mensonge"], ok=1,
         voir="c_peg", ex="L'objection du rigorisme : appliquer la règle sans exception, au risque de laisser faire le mal."),
]

CREDITS = [
    "Portraits : Kant (portrait anonyme, XVIIIᵉ s.) ; Benjamin Constant (Angèle Delasalle) : domaine public",
    "Tableaux et gravures : Gerrit Dou, L'Épicière de village (1647) ; Georges de La Tour, Le Tricheur à l'as de carreau (vers 1635) ; "
    "Johannes Vermeer, La Femme au collier de perles (vers 1662-1665) ; William Hogarth, Gin Lane (1751) ; "
    "William-Adolphe Bouguereau, La Charité (1878) ; Rembrandt, La Leçon d'anatomie du docteur Tulp (1632) ; "
    "Jacques-Louis David, Le Serment des Horaces (1784) ; Honoré Daumier, Le Wagon de troisième classe (vers 1862-1864) ; "
    "Gustave Caillebotte, Les Raboteurs de parquet (1875) ; Gustave Doré, Wentworth Street, Whitechapel (1872) ; "
    "Emil Doerstling, Kant et ses convives (1892-1893) ; Vilhelm Hammershøi, Portes blanches (1913) ; "
    "John William Waterhouse, Diogène (1882) ; Étienne Léopold Trouvelot, Une partie de la Voie lactée (1881-1882) : domaine public",
    "Documents et photographies : Grundlegung zur Metaphysik der Sitten, page de titre (1785) ; Königsberg, photochrome (vers 1900) ; "
    "tombeau de Kant à Kaliningrad (photo J110, domaine public)",
    "Citations de Kant : Fondements de la métaphysique des mœurs, trad. Victor Delbos (1907), Wikisource. "
    "Benjamin Constant, Des réactions politiques (1797). Charles Péguy, Victor-Marie, comte Hugo (1910).",
    "Images : Wikimedia Commons. Voix de synthèse créées pour la série (Qwen3-TTS, clonage local). Musique originale générée pour la série.",
]
