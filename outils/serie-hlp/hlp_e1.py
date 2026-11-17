"""HLP, entrée I (semestre 1) : « Éducation, transmission et émancipation » — le cours en vidéo (site « Ex libris »).

Vidéo pilote des vidéos de HLP. Même chaîne que les vidéos de maths, SES et HGGSP : outils/serie-philo/generer.py,
voix clonée, calage des visuels sur les mots ; moteur hlp/serie/moteur.js (identité « le livre ancien enluminé » :
la page d'un livre ouvert, lettrines peintes, manicules, fleurons, page qui se tourne entre deux parties) ;
illustrations propres à la vidéo dans hlp/serie/illu-hlp-e1.js (balance de Montaigne, trois maîtres de l'Émile,
arbrisseau, minorité selon Kant, frises de dates, courbes du roman d'apprentissage, épreuve, tableau du brouillon).
Contenu : l'entrée « e1 » du site (outils/specialites/hlp/src/data-e1.js), rien au-delà ; la méthode de l'épreuve vient
de la page « L'épreuve » (data-pages.js), le sujet type bac et son corrigé, de l'onglet « Sujet type bac » de l'entrée.
Citations : celles du site, mot pour mot (textes du domaine public d'après Wikisource ; Beauvoir : citation courte ;
Arendt : thèse résumée, l'ouvrage étant protégé). Ce qui dépasse le programme est dit « pour aller plus loin ».

Usage : PYTHONPATH=outils/serie-hlp python3 outils/serie-philo/verifier.py hlp_e1
        SERIE_MOTEUR=muet PYTHONPATH=outils/serie-hlp python3 outils/serie-philo/generer.py hlp_e1   (brouillon sans voix)
        python3 outils/serie-philo/chevauchements.py hlp-e1 ; python3 outils/serie-philo/fermer.py hlp_e1

POINTS À FAIRE VÉRIFIER PAR LE CONTRÔLEUR (repris du site, non revérifiés à la source dans cette session) :
- Montaigne : chapitre I, 26 publié en 1580 (texte cité d'après l'édition de 1595, orthographe modernisée) ; « étamine »
  du jugement (formule du site, paraphrase de Montaigne : la vidéo ne la présente pas comme une citation exacte).
- Rabelais, Gargantua daté 1534 (le site dit 1534 ; certaines éditions disent 1534 ou 1535).
- Émile : « de jeunes docteurs et de vieux enfants » (livre II) ; la leçon de la forêt de Montmorency est au livre III ;
  Robinson Crusoé « le seul livre » qu'Émile lira longtemps (livre III) ; condamné et brûlé à Paris et à Genève en 1762.
- Kant, Traité de pédagogie : « publié en 1803 », trad. Barni ; « Il n'est que ce qu'elle le fait ».
- Condorcet : premier mémoire et sa section « L'instruction doit être la même pour les femmes et pour les hommes » ;
  rapport d'avril 1792 à l'Assemblée législative ; mort en prison en 1794.
- Lois : Guizot 1833 (écoles primaires de garçons), Camille Sée 1880, gratuité 1881, obligation de 6 à 13 ans et
  laïcité le 28 mars 1882 ; Lettre aux instituteurs du 17 novembre 1883 (texte de la citation, « je dis un seul »).
- Durkheim, Éducation et sociologie « publié en 1922 » (recueil posthume) ; Bourdieu et Passeron, Les Héritiers, 1964.
- Kant 1784 : article de décembre 1784 dans la Berlinische Monatsschrift ; citations dans la traduction Barni (1853),
  y compris la phrase des trois tuteurs (« un médecin qui juge pour moi du régime qui me convient »).
- Vallès : L'Enfant en feuilleton en 1878 sous pseudonyme, dédicace signée « Londres » (exil) ; Le Bachelier 1881,
  L'Insurgé 1886. Renan, Souvenirs d'enfance et de jeunesse, 1883 ; Colette, Claudine à l'école, 1900.
- Goethe, Wilhelm Meister 1795-1796 ; Flaubert : la scène finale avec Deslauriers et la phrase « C'est là ce que nous
  avons eu de meilleur ! » ; « Ce fut comme une apparition ».
- Nietzsche, Sur l'avenir de nos établissements d'enseignement (1872) ; Gai Savoir § 270, trad. Henri Albert.
- Épreuve (note de service du 11/09/2026) : 4 h, interprétation et essai sur 10 points chacun, deux copies ;
  l'une littéraire, l'autre philosophique (« sur les sujets de 2023 à 2026 les deux combinaisons sont tombées »).
- Portraits (crédits ci-dessous) : Condorcet « peintre non identifié, autrefois attribué à Greuze » ; Ferry par Bonnat
  (1888) ; Vallès par Courbet (vers 1861, d'après Commons) ; Flaubert par Nadar ; les autres repris de la série philo.
"""

SITE = "hlp"
CODE = "hlp-e1"
NOTION = "Éducation, transmission et émancipation"
NUM = 1
TITRE = "Éducation, transmission et émancipation"
SUIVANT = "Entrée II · Les expressions de la sensibilité"
RYTHME = "vivant"
# noms propres et mots rares : graphie donnée à la voix seulement (texte affiché et sous-titres inchangés)
PRONONCIATION = {"Montaigne": "Montègne", "Rabelais": "Rablè", "Gargantua": "Gargantua", "Ponocrates": "Ponocratèsse",
                 "Kant": "Kante", "Sapere": "Sapéré", "aude": "aoudé", "Condorcet": "Condorssè", "Guizot": "Guizo",
                 "Durkheim": "Durkème", "Passeron": "Passeron", "Bourdieu": "Bourdieu", "Dewey": "Diouï", "Freinet": "Frénè",
                 "Montmorency": "Monmorancy", "Robinson Crusoé": "Robinson Cruzoé", "Vallès": "Valèsse", "Vingtras": "Vintrass",
                 "Chateaubriand": "Chatobrian", "Combourg": "Combour", "Renan": "Renan", "Ernaux": "Erno", "Goethe": "Gueute",
                 "Wilhelm Meister": "Vilhèlm Maïsteur", "Bildungsroman": "Bildoungsroman", "Stendhal": "Stindal",
                 "Julien Sorel": "Julien Sorèl", "Flaubert": "Flobère", "Deslauriers": "Délorié", "Arnoux": "Arnou",
                 "Nietzsche": "Nitche", "Beauvoir": "Bovoir", "Arendt": "Arènnt", "Hannah": "Ana", "Barni": "Barni",
                 "Berlinische Monatsschrift": "Berlinicheu Monatsschrifte", "Camille Sée": "Camille Sé",
                 "étamine": "étamine", "emancipatio": "émancipatsio", "hétéronome": "étéronome", "Émile": "Émile"}

PORTRAITS = "Portraits : "

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="livre", humeur="mystere", carton=False, beats=[
        "{q1}Que faut-il apprendre à un enfant pour qu'il devienne libre ?",
        "Drôle de question, non ? Apprendre, c'est recevoir. On écoute un maître, on lit des livres, on suit des règles. "
        "Et être libre, c'est justement penser par soi-même. Sans maître.",
        ("P", 0.5),
        "{-q1}{par}Voilà tout le problème de cette entrée. {par.1}Sans éducation, personne ne devient capable de juger seul. "
        "{par.2}Mais l'éducation peut aussi dresser, formater, enfermer. "
        "{par.3}Alors, elle libère… ou elle conforme ?",
        "{-par}{plan}Pour y voir clair, on va suivre un chemin. {plan.1}D'abord Montaigne, et sa tête bien faite. "
        "{plan.2}Puis Rousseau, qui invente l'enfance, et son paradoxe : éduquer, est-ce dénaturer ? "
        "{plan.3}Ensuite, l'école devient une affaire politique : Condorcet, puis les lois Ferry. "
        "{plan.4}Kant, et la sortie de la minorité. "
        "{plan.5}Les écrivains qui racontent leur éducation, de Vallès à Flaubert. "
        "{plan.6}Les débats du vingtième siècle. "
        "{plan.7}Et pour finir, le bac : la méthode, un sujet corrigé, et les pièges.",
        "{-plan}{titre}",
        ("P", 3.4),
    ], vis={
        "q1": dict(type="question", t="Que faut-il apprendre à un enfant pour qu'il devienne libre ?"),
        "par": dict(type="liste", titre="Le problème", items=[
            "Sans éducation, personne n'apprend à juger seul", "Mais l'éducation peut dresser, conformer",
            "Libérer ou conformer ?"], marques=["I", "II", "☞"], x=170, y=170, w=940),
        "plan": dict(type="liste", titre="Le chemin", items=[
            "Montaigne : une tête bien faite", "Rousseau : l'enfance, et le paradoxe de l'éducation",
            "Condorcet, puis l'école de la République", "Kant : sortir de la minorité",
            "Raconter son éducation : Vallès, Flaubert", "Transmettre ou rompre ? Le XX^{e} siècle",
            "Le bac : méthode, sujet corrigé, pièges"], x=190, y=96, w=900),
        "titre": dict(type="titre", sur="HLP · Semestre 1 · Entrée I", t="Éducation, transmission et émancipation",
                      sous="Le cours complet, de Montaigne au bac"),
    }),

    # ================================================================ I. Montaigne
    dict(id="montaigne", chap="L'héritage humaniste : une tête bien faite", fond="livre", humeur="lumiere",
         retenir="Montaigne (*Essais*, I, 26, 1580) : mieux vaut former le jugement que remplir la mémoire. Mais l'éducation humaniste passe encore par les textes anciens : la « culture des mots ».",
         beats=[
        "{mont}Pour comprendre une rupture, il faut savoir avec quoi l'on rompt. Alors remontons à la Renaissance.",
        "Mille cinq cent quatre-vingts. Michel de Montaigne publie ses Essais. Dans un chapitre intitulé « De l'institution des enfants », "
        "il réfléchit à l'éducation d'un jeune noble. Et il donne un conseil pour choisir son précepteur.",
        ("C", "Je voudrais aussi qu'on fût soigneux de lui choisir un conducteur qui eût plutôt la tête bien faite que bien pleine", "c_mont"),
        "Une tête bien faite, plutôt que bien pleine. La formule est devenue un proverbe.",
        "{-mont}{-c_mont}{bal}Regarde comment elle est construite. {bal.1}D'un côté, la tête bien faite : on forme le jugement. "
        "{bal.2}De l'autre, la tête bien pleine : on remplit la mémoire, comme un vase. "
        "{bal.3}Et la balance penche. Mais attention : plutôt… que. Montaigne ne jette pas le savoir. Il le met à sa place, derrière le jugement.",
        "{bal.4}Il a même une image pour ça : faire passer les idées des livres par l'étamine, c'est-à-dire le tamis, du jugement de l'élève. "
        "On ne recrache pas ce qu'on a lu. On le trie.",
        "{-bal}{n_mont}Un détail que les correcteurs adorent. La formule porte sur le choix du précepteur, que Montaigne appelle le conducteur. "
        "Pas sur l'élève lui-même.",
        "{-n_mont}{rab}Un demi-siècle plus tôt, Rabelais faisait déjà le procès de l'école. Dans Gargantua, en mille cinq cent trente-quatre, "
        "l'éducation du géant commence par des récitations mécaniques. {rab.1}Puis son nouveau maître, Ponocrates, lui impose un emploi du temps encyclopédique : "
        "des lectures, l'observation de la nature, des exercices du corps.",
        "{-rab}{mots}Mais attention : l'éducation humaniste reste une éducation par les textes anciens. {mots.1}Le latin, le grec. "
        "{mots.2}La rhétorique. {mots.3}L'imitation des modèles. {mots.4}Bref, une {!culture des mots}culture des mots. "
        "C'est elle que les Lumières vont contester.",
        "{-mots}",
    ], vis={
        "mont": dict(type="portrait", annee=1533, img="montaigne", nom="Michel de Montaigne", dates="1533 – 1592",
                     legende="*Essais* (1580)"),
        "c_mont": dict(type="cit", a="Montaigne", o="Essais", ref="I, 26 (orthographe modernisée)", x=620, y=150, w=540,
                       hl="tête bien faite"),
        "bal": dict(type="illu", nom="balance", x=150, y=110, w=980, h=540),
        "n_mont": dict(type="note", titre="Attention", t="La formule porte sur le choix du précepteur (le « conducteur »), pas sur l'élève lui-même.",
                       x=230, y=230, w=860),
        "rab": dict(type="cols", g="Récitations", gq="une éducation mécanique, par cœur", d="Ponocrates",
                    dq="lectures, observation de la nature, exercices du corps", vs="puis", repere="Rabelais, *Gargantua* (1534)"),
        "mots": dict(type="liste", titre="L'éducation humaniste : la « culture des mots »", items=[
            "Le latin, le grec", "La rhétorique", "L'imitation des modèles", "Ce que les Lumières vont contester"],
            marques=["I", "II", "III", "☞"], x=190, y=170, w=920),
    }),

    # ================================================================ II. Rousseau
    dict(id="rousseau", chap="Rousseau : l'enfant n'est pas un adulte en petit", fond="livre", humeur="lumiere",
         retenir="*Émile* (1762) : l'enfance a sa propre logique. Éducation négative (protéger du vice et de l'erreur) ; les choses avant les mots ; « Vivre est le métier que je lui veux apprendre ».",
         beats=[
        "{rou}Deux siècles plus tard, en mille sept cent soixante-deux, Jean-Jacques Rousseau publie Émile, ou De l'éducation. "
        "Un livre étrange : Rousseau y imagine l'éducation d'un enfant fictif, Émile, confié à un gouverneur, de sa naissance à son mariage.",
        "Sa grande idée tient en une phrase.",
        ("C", "La nature veut que les enfants soient enfants avant que d'être hommes.", "c_nat"),
        "{-rou}{-c_nat}{tab_emi}L'enfance n'est pas un brouillon de l'âge adulte. C'est un âge à part, avec sa propre logique. "
        "Vouloir des enfants qui raisonnent comme des grandes personnes, dit Rousseau, c'est fabriquer « de jeunes docteurs et de vieux enfants ».",
        "{-tab_emi}{cp_neg}D'où deux principes. Le premier : l'{!éducation négative}éducation négative.",
        "{-cp_neg}",
        ("C", "La première éducation doit donc être purement négative. Elle consiste, non point à enseigner la vertu ni la vérité, mais à garantir le cœur du vice et l'esprit de l'erreur.", "c_neg"),
        "{-c_neg}{neg}Négative, ça ne veut pas dire rien du tout. {neg.1}On ne bourre pas l'enfant de leçons de morale. "
        "{neg.2}On le protège, et on le laisse faire ses expériences.",
        "{-neg}{cho}Deuxième principe : {cho.g}les choses avant les mots. L'enfant apprend par l'expérience et par le besoin, {cho.d}pas par des leçons abstraites.",
        "{-cho}{mont3}Un exemple célèbre, au livre trois. {mont3.1}Émile trouve inutiles ses leçons de géographie et d'astronomie. "
        "{mont3.2}Un jour, près de la forêt de Montmorency, il faut retrouver son chemin. {mont3.3}Et là, il comprend à quoi servent ces observations.",
        "{mont3.4}Et le seul livre qu'il lira longtemps ? Robinson Crusoé. Un homme seul, qui pourvoit lui-même à ses besoins.",
        "Le but de tout cela n'est pas un métier. C'est l'humanité.",
        "{-mont3}",
        ("C", "Vivre est le métier que je lui veux apprendre.", "c_viv"),
        "{-c_viv}{post}Ces idées ont une longue postérité. {post.1}Jusqu'au vingtième siècle, elles nourrissent les mouvements d'éducation nouvelle. "
        "{post.2}L'Américain John Dewey, avec Mon credo pédagogique, en mille huit cent quatre-vingt-dix-sept. "
        "{post.3}Ou Célestin Freinet, qui installe une imprimerie dans sa classe, et fait écrire aux élèves des textes libres.",
        "{-post}{tm}Rousseau a même une image pour résumer tout ça. Trois maîtres nous éduquent. {tm.1}La nature, qui développe nos organes. "
        "{tm.2}Les hommes, qui nous apprennent à nous en servir. {tm.3}Et les choses, par l'expérience. "
        "{tm.4}L'élève est au croisement. {tm.5}S'ils s'accordent, il est bien élevé. "
        "{tm.6}Or un seul de ces maîtres dépend vraiment de nous : les hommes. C'est leur éducation qu'il faut régler sur les deux autres.",
        "{-tm}",
    ], vis={
        "rou": dict(type="portrait", annee=1712, img="rousseau", nom="Jean-Jacques Rousseau", dates="1712 – 1778",
                    legende="*Émile ou De l'éducation* (1762)"),
        "c_nat": dict(type="cit", a="Rousseau", o="Émile", ref="livre II", x=620, y=190, w=540),
        "tab_emi": dict(type="tableau", img="e1-emile", de=[1.0, .5, .12], a=[1.1, .5, .3],
                        legende="Rousseau, *Émile ou De l'éducation*, page de titre, 1762 (domaine public)"),
        "cp_neg": dict(type="def", terme="Éducation négative", t="La première éducation n'enseigne ni la vertu ni la vérité : elle protège.",
                       x=190, y=250, w=900),
        "c_neg": dict(type="cit", a="Rousseau", o="Émile", ref="livre II", x=200, y=130, w=900),
        "neg": dict(type="cols", g="Pas de leçons", gq="ni morale ni vérités imposées", d="Protéger",
                    dq="garder du vice et de l'erreur, laisser faire l'expérience", vs="mais"),
        "cho": dict(type="cols", g="Les choses", gq="l'expérience, le besoin", d="Les mots", dq="les leçons abstraites",
                    vs="avant", repere="Apprendre en faisant"),
        "mont3": dict(type="liste", titre="*Émile*, livre III", items=[
            "Émile trouve inutiles la géographie et l'astronomie", "Près de la forêt de Montmorency…",
            "Il faut retrouver son chemin : il comprend à quoi elles servent", "Son seul livre : *Robinson Crusoé*"],
            marques=["I", "II", "III", "☞"], x=170, y=150, w=960),
        "c_viv": dict(type="cit", a="Rousseau", o="Émile", ref="livre I", x=200, y=220, w=880),
        "post": dict(type="liste", titre="Une longue postérité", items=[
            "L'« éducation nouvelle », jusqu'au XX^{e} siècle", "John Dewey, *Mon credo pédagogique* (1897)",
            "Célestin Freinet : l'imprimerie à l'école, les textes libres"], x=170, y=170, w=960),
        "tm": dict(type="illu", nom="maitres", x=170, y=150, w=940, h=520),
    }),

    # ================================================================ III. le paradoxe
    dict(id="paradoxe", chap="Éduquer, est-ce dénaturer ?", fond="livre", humeur="tension",
         retenir="L'éducation est une menace (elle peut dresser, conformer) et une nécessité (sans elle, la société défigure l'enfant). Kant : « L'homme ne peut devenir homme que par l'éducation ».",
         beats=[
        "{mp}Mais Rousseau ne fait pas que proposer une méthode. Son livre s'ouvre sur un paradoxe. Écoute la première phrase.",
        "{-mp}",
        ("C", "Tout est bien, sortant des mains de l'Auteur des choses : tout dégénère entre les mains de l'homme.", "c_tout"),
        "{-c_tout}{acc}Puis Rousseau accumule les verbes violents. {acc.1}L'homme mutile. {acc.2}Il défigure. "
        "{acc.3}Il veut tout dresser à sa mode, même l'homme, comme un cheval de manège.",
        "Alors, faut-il renoncer à éduquer ? Non ! Rousseau ajoute aussitôt : « Sans cela, tout irait plus mal encore ». "
        "{acc.4}Un enfant abandonné à lui-même au milieu de la société serait, dit-il, « le plus défiguré de tous ».",
        "{-acc}{arb}Pour le comprendre, Rousseau prend une image végétale. {arb.1}Il y a l'arbre qu'on contourne à sa mode, comme dans un jardin : c'est le dressage. "
        "{arb.2}Il y a l'arbrisseau né par hasard au milieu d'un chemin : les passants le heurtent, le plient dans tous les sens, et il meurt. "
        "{arb.3}Et il y a la bonne culture : une enceinte qui protège la pousse. Pas un moule.",
        "{-arb}",
        ("C", "On façonne les plantes par la culture, et les hommes par l'éducation.", "c_cult"),
        "{-c_cult}{men}L'éducation est donc à la fois {men.g}un danger, le conformisme, {men.d}et une nécessité : protéger la nature contre la société.",
        "{-men}{kant1}Quelques années plus tard, Kant radicalise cette nécessité.",
        ("C", "L'homme ne peut devenir homme que par l'éducation. Il n'est que ce qu'elle le fait.", "c_kant1"),
        "{-c_kant1}Cette phrase vient de ses leçons de pédagogie, publiées en mille huit cent trois, sous le titre de Traité de pédagogie.",
        "{-kant1}{disc}Kant distingue deux moments. {disc.g}La discipline, qui arrache l'homme à la sauvagerie. "
        "{disc.d}Et l'instruction, qui le cultive. {disc.1}Et il ajoute une remarque décisive : on ne peut être éduqué que par d'autres hommes, eux-mêmes éduqués. "
        "Toute éducation est donc une {!transmission}transmission.",
        "{-disc}{perf}Pour aller plus loin : Rousseau parle ailleurs de la perfectibilité, dans son Discours sur l'origine de l'inégalité, en mille sept cent cinquante-cinq. "
        "C'est ce qui distingue l'homme de l'animal : sa capacité à se transformer. En bien… comme en mal.",
        "{-perf}",
    ], vis={
        "mp": dict(type="mot", t="Un paradoxe", g="la première phrase d'*Émile*", taille=110, y=230),
        "c_tout": dict(type="cit", a="Rousseau", o="Émile", ref="livre I, première phrase", x=200, y=190, w=880, hl="tout dégénère"),
        "acc": dict(type="liste", titre="L'homme qui « défigure tout »", items=[
            "« il mutile »", "« il défigure tout »", "le « dresser », « comme un cheval de manège »",
            "Mais : « Sans cela, tout irait plus mal encore »"], marques=["I", "II", "III", "☞"], x=190, y=160, w=920),
        "arb": dict(type="illu", nom="arbrisseau", x=150, y=96, w=980, h=500,
                    titres=["Dresser", "Abandonner", "Cultiver"],
                    legs=["« contourner à sa mode, comme un arbre de son jardin »", "heurté par les passants, « au milieu d'un chemin »",
                          "une enceinte qui protège, pas un moule"]),
        "c_cult": dict(type="cit", a="Rousseau", o="Émile", ref="livre I", x=210, y=220, w=860),
        "men": dict(type="cols", g="Une menace", gq="dresser, conformer, « défigurer »", d="Une nécessité",
                    dq="protéger la nature contre la société", vs="et"),
        "kant1": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                      legende="*Traité de pédagogie* (publié en 1803)"),
        "c_kant1": dict(type="cit", a="Kant", o="Traité de pédagogie", ref="trad. Barni", x=620, y=180, w=540, hl="que par l'éducation"),
        "disc": dict(type="cols", g="La discipline", gq="arracher l'homme à la sauvagerie", d="L'instruction",
                     dq="le cultiver", vs="puis", repere="On n'est éduqué que par des hommes eux-mêmes éduqués"),
        "perf": dict(type="def", terme="Perfectibilité", plus=True,
                     t="Rousseau (1755) : la faculté propre à l'homme de se perfectionner, et de se corrompre. Elle rend l'éducation possible et nécessaire.",
                     x=190, y=230, w=900),
    }),

    # ================================================================ IV. Condorcet
    dict(id="condorcet", chap="Condorcet : instruire pour rendre libres", fond="livre", humeur="lumiere",
         retenir="Condorcet (1791) : l'instruction publique rend l'égalité des droits réelle ; elle doit rendre les citoyens capables de juger et de corriger la loi. Instruction (État) ≠ éducation (familles).",
         beats=[
        "{con}Avec la Révolution, la question change de nature. Elle devient politique.",
        "En mille sept cent quatre-vingt-onze, le mathématicien et philosophe Condorcet écrit ses Cinq mémoires sur l'instruction publique. Première idée :",
        ("C", "l'instruction publique est un devoir de la société à l'égard des citoyens", "c_dev"),
        "{-con}{-c_dev}{pq}Pourquoi un devoir ? {pq.1}Parce que l'égalité des droits resterait vaine si l'inégalité dans les facultés morales empêchait le plus grand nombre d'en jouir. "
        "{pq.2}Celui qui ne sait pas écrire, qui ignore l'arithmétique, dépend réellement de l'homme plus instruit. "
        "{pq.3}Il a des droits sur le papier. Mais il ne peut pas les exercer avec la même indépendance.",
        "{-pq}{mot_eg}Retiens bien cet argument : sans instruction, l'égalité reste {!théorique}théorique.",
        "Et attention : instruire, pour Condorcet, ce n'est pas faire réciter les lois. Écoute.",
        "{-mot_eg}",
        ("C", "Le but de l'instruction n'est pas de faire admirer aux hommes une législation toute faite, mais de les rendre capables de l'apprécier et de la corriger.", "c_but"),
        "{-c_but}{crit}Tu entends la construction ? {crit.1}Ne pas… mais : le texte réfute une idée pour en imposer une autre. "
        "{crit.2}L'école ne doit pas fabriquer une religion politique. Elle doit former l'esprit critique, même contre la loi qu'elle enseigne.",
        "{-crit}{ie}D'où une distinction capitale, au cœur du raisonnement. {ie.g}L'instruction : transmettre des vérités et leurs preuves. "
        "Elle revient à la puissance publique. {ie.d}L'éducation, morale et religieuse : elle revient aux familles.",
        "{-ie}{fem}Un dernier détail, très en avance pour l'époque. {fem.1}Dans le premier mémoire, une section s'intitule : "
        "« L'instruction doit être la même pour les femmes et pour les hommes ». Nous sommes en mille sept cent quatre-vingt-onze.",
        "{fem.2}En avril mille sept cent quatre-vingt-douze, Condorcet présente un rapport sur l'instruction publique à l'Assemblée législative. "
        "Il ne sera pas appliqué. Proscrit pendant la Terreur, il meurt en prison en mille sept cent quatre-vingt-quatorze.",
        "{-fem}",
    ], vis={
        "con": dict(type="portrait", annee=1743, img="condorcet", nom="Condorcet", dates="1743 – 1794",
                    legende="*Cinq mémoires sur l'instruction publique* (1791)"),
        "c_dev": dict(type="cit", a="Condorcet", o="Cinq mémoires sur l'instruction publique", ref="premier mémoire", x=620, y=200, w=540),
        "pq": dict(type="liste", titre="Pourquoi un devoir ?", items=[
            "Sans instruction, l'égalité des droits reste vaine", "Celui qui ne sait pas écrire « dépend réellement de l'homme plus instruit »",
            "Des droits sur le papier, mais pas « la même indépendance »"], marques=["I", "II", "III"], x=170, y=170, w=960),
        "mot_eg": dict(type="mot", t="L'égalité réelle", g="l'instruction est une condition de la liberté", taille=84, y=250),
        "c_but": dict(type="cit", a="Condorcet", o="Cinq mémoires sur l'instruction publique", ref="premier mémoire", x=200, y=170, w=900,
                      hl="l'apprécier et de la corriger"),
        "crit": dict(type="liste", titre="Une école de l'esprit critique", items=[
            "« ne… pas… mais » : réfuter, puis affirmer", "Pas de « religion politique » : apprendre à juger la loi"],
            marques=["I", "II"], x=170, y=200, w=960),
        "ie": dict(type="cols", g="Instruction", gq="des vérités et leurs preuves : la puissance publique", d="Éducation",
                   dq="la morale, la religion : les familles", vs="≠"),
        "fem": dict(type="liste", titre="Un projet en avance", items=[
            "« L'instruction doit être la même pour les femmes et pour les hommes » (1791)",
            "Rapport à l'Assemblée législative (avril 1792) : jamais appliqué"], marques=["❦", "☞"], x=170, y=200, w=960),
    }),

    # ================================================================ V. l'école de la République
    dict(id="ecole", chap="L'école de la République : instruire, unir, émanciper", fond="livre", humeur="calme",
         retenir="Lois Ferry : gratuité de l'école primaire publique (1881), instruction obligatoire de 6 à 13 ans et laïcité (1882). Durkheim : l'école socialise autant qu'elle émancipe.",
         beats=[
        "{tab_tache}Le plan de Condorcet n'est pas appliqué. Mais le dix-neuvième siècle construit peu à peu une école publique.",
        "{-tab_tache}{jal}Suis les dates. {jal.1}En mille huit cent trente-trois, la loi Guizot organise les écoles primaires de garçons. "
        "{jal.2}En mille huit cent quatre-vingts, la loi Camille Sée crée l'enseignement secondaire public des jeunes filles. "
        "{jal.3}Puis viennent les lois Ferry. En mille huit cent quatre-vingt-un, l'école primaire publique devient gratuite. "
        "{jal.4}En mille huit cent quatre-vingt-deux, l'instruction devient obligatoire, de six à treize ans, et l'enseignement public devient laïque.",
        "{-jal}{piege_rev}Retiens bien ce piège : l'école gratuite, obligatoire et laïque ne date pas de la Révolution. "
        "Le plan de Condorcet n'a pas été appliqué. Ce sont les lois Ferry, en mille huit cent quatre-vingt-un et quatre-vingt-deux.",
        "{-piege_rev}{fer}Un an plus tard, le dix-sept novembre mille huit cent quatre-vingt-trois, Jules Ferry écrit aux instituteurs. "
        "Il leur confie l'enseignement moral. Et il leur donne une règle de prudence.",
        ("C", "Demandez-vous si un père de famille, je dis un seul, présent à votre classe et vous écoutant, pourrait de bonne foi refuser son assentiment à ce qu'il vous entendrait dire.", "c_fer"),
        "{-c_fer}{-fer}{reg}Observe l'incise : {reg.1}« je dis un seul ». Il suffit d'un seul désaccord sincère pour se taire. "
        "{reg.2}Si oui, abstiens-toi de le dire ; sinon, parle hardiment. Une méthode simple, presque juridique. "
        "{reg.3}L'instituteur devient, dit Ferry, l'auxiliaire et, à certains égards, le suppléant du père de famille.",
        "{-reg}{dur}Au début du vingtième siècle, le sociologue Émile Durkheim formule la fonction sociale de l'école.",
        ("C", "l'éducation consiste en une socialisation méthodique de la jeune génération", "c_dur"),
        "{-c_dur}{-dur}{tens}Et voilà toute la tension de l'entrée. {tens.g}L'école émancipe, {tens.d}mais elle intègre aussi à une société, avec ses règles.",
        "{tens.1}Pour aller plus loin : au vingtième siècle, la sociologie montre que l'école peut aussi reproduire les inégalités. "
        "C'est la thèse de Bourdieu et Passeron, dans Les Héritiers, en mille neuf cent soixante-quatre. La promesse d'émancipation n'est pas toujours tenue.",
        "{-tens}",
    ], vis={
        "tab_tache": dict(type="tableau", img="e1-tache", de=[1.0, .5, .5], a=[1.2, .45, .5],
                          legende="Albert Bettannier, *La Tache noire*, 1887 (musée d'Orsay, domaine public)"),
        "jal": dict(type="illu", nom="jalons", x=150, y=130, w=980, h=440, de=1825, a=1890, items=[
            [1833, "Loi Guizot", "écoles primaires de garçons"], [1880, "Loi Camille Sée", "le secondaire des jeunes filles"],
            [1881, "Ferry : gratuité", "école primaire publique"], [1882, "Obligation, laïcité", "de 6 à 13 ans · 28 mars"]],
            cote=[1, -1, 1, -1], regulier=True),
        "piege_rev": dict(type="note", titre="Le piège des dates", t="L'école gratuite, obligatoire et laïque ne date pas de la Révolution : ce sont les lois Ferry (1881-1882).",
                          x=230, y=230, w=860),
        "fer": dict(type="portrait", annee=1832, img="ferry", nom="Jules Ferry", dates="1832 – 1893",
                    legende="*Lettre aux instituteurs* (17 novembre 1883)"),
        "c_fer": dict(type="cit", a="Jules Ferry", o="Lettre aux instituteurs", ref="1883", x=620, y=120, w=540, hl="je dis un seul"),
        "reg": dict(type="liste", titre="La règle du « père de famille »", items=[
            "« je dis un seul » : un seul désaccord sincère suffit", "« Si oui, abstenez-vous de le dire ; sinon, parlez hardiment »",
            "L'instituteur, « auxiliaire » et « suppléant du père de famille »"], marques=["I", "II", "III"], x=170, y=170, w=960),
        "dur": dict(type="portrait", annee=1858, img="durkheim", nom="Émile Durkheim", dates="1858 – 1917",
                    legende="*Éducation et sociologie* (publié en 1922)"),
        "c_dur": dict(type="cit", a="Durkheim", o="Éducation et sociologie", x=620, y=210, w=540),
        "tens": dict(type="cols", g="Émanciper", gq="instruire, rendre libre", d="Intégrer", dq="socialiser, transmettre des règles",
                     vs="et", repere="Pour aller plus loin : *Les Héritiers* (1964)"),
    }),

    # ================================================================ VI. Kant
    dict(id="kant", chap="Kant : sortir de la minorité", fond="livre", humeur="tension",
         retenir="Kant (1784) : les Lumières font sortir l'homme de la minorité, l'incapacité de se servir de son intelligence sans être dirigé. Cause : paresse et lâcheté. Devise : *Sapere aude*.",
         beats=[
        "{kant2}Retour en mille sept cent quatre-vingt-quatre. Une revue berlinoise pose une question : qu'est-ce que les Lumières ? "
        "En décembre, Kant répond. Et sa réponse définit l'émancipation.",
        ("C", "Les lumières sont ce qui fait sortir l'homme de la minorité qu'il doit s'imputer à lui-même.", "c_lum"),
        "{-kant2}{-c_lum}{d_min}Qu'est-ce que la minorité ? C'est l'incapacité de se servir de son intelligence sans être dirigé par autrui. "
        "{d_min.1}Attention : ce n'est pas une question d'âge. Ni un défaut d'intelligence. C'est un défaut de courage.",
        "{-d_min}{minr}Alors pourquoi reste-t-on mineur ? Par paresse, et par lâcheté. C'est confortable. Kant l'écrit avec ironie : "
        "{minr.1}j'ai un livre qui a de l'esprit pour moi, {minr.2}un directeur qui a de la conscience pour moi, {minr.3}un médecin qui juge pour moi de mon régime.",
        "{minr.4}Je n'ai pas besoin de penser. Les tuteurs s'en chargent, et ils profitent de ce confort.",
        "{minr.5}Alors, comment en sortir ? Il faut du courage. D'où la devise des Lumières.",
        "{-minr}",
        ("C", "Sapere aude, aie le courage de te servir de ta propre intelligence !", "c_sap"),
        "{-c_sap}{pub}Mais attention : Kant ne demande pas la fin des maîtres. Un individu seul s'en sort difficilement. "
        "Un public, lui, peut s'éclairer, à une condition : la liberté de faire un usage public de sa raison.",
        "{-pub}{us}{us.g}Prends un officier. Dans son service, il reçoit un ordre : il doit obéir. C'est l'usage privé de la raison. "
        "{us.d}Mais le même homme, comme savant, peut écrire pour critiquer l'organisation de l'armée. C'est l'usage public.",
        "{us.1}L'émancipation passe donc par la liberté d'écrire et de publier.",
        "{-us}{d_eman}Au passage, retiens l'origine du mot {!émancipation}émancipation. En latin, emancipatio, c'est l'acte juridique par lequel un fils sortait de la puissance paternelle. "
        "Par extension : se libérer d'une tutelle, familiale, sociale, politique ou intellectuelle.",
        "{-d_eman}",
    ], vis={
        "kant2": dict(type="portrait", annee=1724, img="kant", nom="Emmanuel Kant", dates="1724 – 1804",
                      legende="*Qu'est-ce que les Lumières ?* (1784)"),
        "c_lum": dict(type="cit", a="Kant", o="Réponse à la question : Qu'est-ce que les Lumières ?", ref="trad. Barni", x=620, y=170, w=540,
                      hl="sortir l'homme de la minorité"),
        "d_min": dict(type="def", terme="La minorité", t="L'incapacité de se servir de son intelligence sans être dirigé par autrui.",
                      etape="Pas une question d'âge : un défaut de courage.", x=190, y=200, w=900, cles=["courage"]),
        "minr": dict(type="illu", nom="minorite", x=150, y=96, w=980, h=520),
        "c_sap": dict(type="cit", a="Kant", o="Qu'est-ce que les Lumières ?", ref="trad. Barni", x=210, y=220, w=880),
        "pub": dict(type="def", terme="Une condition", cles=["public"],
                    t="Un individu seul sort difficilement de la minorité ; un public peut s'éclairer, s'il a la liberté de faire un « usage public » de sa raison.",
                    x=190, y=200, w=900),
        "us": dict(type="cols", g="Usage privé", gq="l'officier, dans son service, obéit", d="Usage public",
                   dq="le même, comme savant, critique l'armée par écrit", vs="≠", repere="La liberté d'écrire et de publier"),
        "d_eman": dict(type="def", terme="Émancipation", cles=["tutelle"],
                       t="Du latin *emancipatio* : l'acte par lequel un fils sortait de la puissance paternelle. Par extension, la sortie d'une tutelle.",
                       x=190, y=220, w=900),
    }),

    # ================================================================ VII. raconter son éducation
    dict(id="recit", chap="Raconter son éducation : le récit d'enfance", fond="livre", humeur="mystere",
         retenir="Le récit d'enfance montre ce qu'un individu est devenu à partir de ce qu'il a reçu, et de ce avec quoi il a rompu. Vallès, *L'Enfant* (1878) : l'éducation comme violence, la révolte.",
         beats=[
        "{tab_steen}Au dix-neuvième siècle, l'école prend une place nouvelle. On le voit dans la littérature : les souvenirs d'écoliers se multiplient.",
        "Ces récits cherchent à comprendre ce qu'un individu est devenu, à partir de ce qu'il a reçu. Mais aussi de ce avec quoi il a rompu.",
        "{-tab_steen}{val}Le plus violent, c'est Jules Vallès. Journaliste, membre de la Commune de Paris en mille huit cent soixante et onze, il part en exil à Londres. "
        "Là, il commence une trilogie. Son héros s'appelle Jacques Vingtras.",
        "{-val}{tri}{tri.1}L'Enfant, en mille huit cent soixante-dix-huit. {tri.2}Le Bachelier, en mille huit cent quatre-vingt-un. {tri.3}L'Insurgé, en mille huit cent quatre-vingt-six.",
        "{tri.hl}De l'enfant humilié à l'insurgé de la Commune : la révolte politique prolonge la révolte contre l'éducation reçue.",
        "{-tri}Écoute la dédicace de L'Enfant.",
        ("C", "À tous ceux qui crevèrent d'ennui au collège ou qu'on fit pleurer dans la famille qui, pendant leur enfance, furent tyrannisés par leurs maîtres ou rossés par leurs parents, je dédie ce livre.", "c_ded"),
        "{-c_ded}{ded}Regarde comment c'est écrit. {ded.1}Le parallélisme : collège et famille, maîtres et parents. L'école et la famille sont mises sur le même plan. "
        "{ded.2}Le registre familier : crevèrent, rossés. Il tranche avec la forme solennelle d'une dédicace. "
        "{ded.3}C'est déjà de la révolte. L'enfant humilié est devenu l'écrivain qui juge.",
        "{-ded}{n_val}Attention, piège classique. L'Enfant n'est pas un simple témoignage. C'est un roman autobiographique : "
        "le narrateur s'appelle Jacques Vingtras, pas Jules Vallès. Il y a une construction, et une ironie.",
        "{-n_val}{autres}D'autres souvenirs d'école à connaître. {autres.1}Chateaubriand, dans les Mémoires d'outre-tombe : l'enfance à Combourg, et les collèges. "
        "{autres.2}Colette, Claudine à l'école, en mille neuf cent : une école de village, racontée avec insolence. "
        "{autres.3}Renan, Souvenirs d'enfance et de jeunesse, en mille huit cent quatre-vingt-trois. "
        "{autres.4}Et pour aller plus loin, au vingtième siècle : Annie Ernaux, La Place, en mille neuf cent quatre-vingt-trois. "
        "Elle y dit la distance que les études ont créée avec son père, ouvrier puis commerçant.",
        "{-autres}",
    ], vis={
        "tab_steen": dict(type="tableau", img="e1-steen", fond=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                          legende="Jan Steen, *L'École de village*, vers 1665 (National Gallery of Ireland, domaine public)"),
        "val": dict(type="portrait", annee=1832, img="valles", nom="Jules Vallès", dates="1832 – 1885",
                    legende="*L'Enfant* (1878)"),
        "tri": dict(type="cartes", items=[
            dict(ic="livre", t="*L'Enfant*", q="1878 : la famille, le collège"),
            dict(ic="plume", t="*Le Bachelier*", q="1881 : le deuxième volet"),
            dict(ic="voix", t="*L'Insurgé*", q="1886 : la Commune de 1871")]),
        "c_ded": dict(type="cit", a="Jules Vallès", o="L'Enfant", ref="dédicace", x=200, y=130, w=900),
        "ded": dict(type="liste", titre="Comment la dédicace est écrite", items=[
            "Le parallélisme : collège / famille, maîtres / parents", "Le registre familier : « crevèrent », « rossés »",
            "Déjà une révolte : l'enfant humilié devient l'écrivain qui juge"], marques=["I", "II", "III"], x=170, y=170, w=960),
        "n_val": dict(type="note", titre="Piège", t="*L'Enfant* est un roman autobiographique : le narrateur s'appelle Jacques Vingtras. Construction, ironie : pas un simple témoignage.",
                      x=230, y=210, w=860),
        "autres": dict(type="liste", titre="D'autres souvenirs d'école", petit=True, items=[
            "Chateaubriand, *Mémoires d'outre-tombe*, livres I à V", "Colette, *Claudine à l'école* (1900)",
            "Renan, *Souvenirs d'enfance et de jeunesse* (1883)", "Pour aller plus loin : Ernaux, *La Place* (1983)"],
            marques=["I", "II", "III", "+"], x=190, y=150, w=920),
    }),

    # ================================================================ VIII. le roman d'apprentissage
    dict(id="apprentissage", chap="Le roman d'apprentissage, ou l'éducation par la vie", fond="livre", humeur="calme",
         retenir="*Bildungsroman* : un jeune héros se forme au contact du monde (Goethe, Stendhal). Flaubert, *L'Éducation sentimentale* (1869) : un apprentissage raté.",
         beats=[
        "{d_bild}On peut aussi être éduqué… par la vie. C'est le sujet du roman d'apprentissage. En allemand : {!Bildungsroman}Bildungsroman, le roman de formation. "
        "Un jeune héros se forme au contact du monde.",
        "{-d_bild}{crb}{crb.1}Le modèle, c'est Goethe : Les Années d'apprentissage de Wilhelm Meister, en mille sept cent quatre-vingt-quinze et quatre-vingt-seize. "
        "En France, Stendhal écrit Le Rouge et le Noir, en mille huit cent trente. Julien Sorel, fils de charpentier, se forme par les livres et par l'ambition. "
        "Et Balzac multiplie les jeunes provinciaux qui montent à Paris.",
        "{crb.2}Puis Flaubert retourne le modèle. L'Éducation sentimentale, en mille huit cent soixante-neuf, c'est l'histoire d'un apprentissage raté.",
        "Le héros, Frédéric Moreau, rencontre Madame Arnoux. Flaubert écrit : « Ce fut comme une apparition ». "
        "Il traverse la révolution de mille huit cent quarante-huit. Et il ne devient rien.",
        "{crb.3}À la fin, avec son ami Deslauriers, il se souvient d'une visite manquée à une maison close, quand ils étaient adolescents. Et il conclut :",
        "{-crb}",
        ("C", "C'est là ce que nous avons eu de meilleur !", "c_fla"),
        "{-c_fla}{n_fla}Le titre est donc ironique : l'éducation ne mène à aucune sagesse. "
        "Dans une copie, ça te permet de nuancer une idée trop simple : non, l'expérience ne forme pas toujours.",
        "{-n_fla}",
    ], vis={
        "d_bild": dict(type="def", terme="Bildungsroman", cles=["formation"],
                       t="Le roman d'apprentissage, ou de formation : un jeune héros se forme au contact du monde.", x=190, y=230, w=900),
        "crb": dict(type="illu", nom="courbes", x=150, y=120, w=980, h=480),
        "c_fla": dict(type="cit", a="Flaubert", o="L'Éducation sentimentale", ref="dernier chapitre", x=230, y=230, w=860),
        "n_fla": dict(type="note", titre="Dans une copie", t="Flaubert permet de nuancer l'idée que l'expérience forme toujours : le titre est ironique.",
                      x=230, y=230, w=860),
    }),

    # ================================================================ IX. transmettre ou rompre ?
    dict(id="debats", chap="Transmettre ou rompre ?", fond="livre", humeur="tension",
         retenir="Nietzsche : devenir soi est une tâche. Beauvoir : l'éducation fabrique des rôles. Arendt : transmettre l'ancien pour protéger le nouveau. La transmission est la condition de l'émancipation.",
         beats=[
        "{q_tr}Dernière grande question : faut-il transmettre un héritage, ou laisser chacun s'inventer ?",
        "{-q_tr}{nie}Dès mille huit cent soixante-douze, Nietzsche attaque l'enseignement de son temps, dans Sur l'avenir de nos établissements d'enseignement. "
        "Pour lui, devenir soi est une tâche.",
        ("C", "Tu dois devenir celui que tu es.", "c_nie"),
        "L'éducation devient alors formation de soi. Parfois contre les institutions.",
        "{-nie}{-c_nie}{bea}Simone de Beauvoir, elle, montre que l'éducation fabrique aussi des rôles. En mille neuf cent quarante-neuf, dans Le Deuxième Sexe :",
        "{-bea}",
        ("C", "On ne naît pas femme : on le devient.", "c_bea"),
        "S'émanciper suppose donc de prendre conscience de ce qu'on a reçu comme une évidence.",
        "{-c_bea}{m61}Et à l'inverse, Hannah Arendt. Dans « La crise de l'éducation », en mille neuf cent soixante et un, elle soutient que l'école doit rester conservatrice. "
        "{-m61}{are}{are.g}Non pas pour empêcher le changement. Mais parce qu'elle transmet un monde ancien, {are.d}pour protéger ce que chaque enfant apporte de nouveau.",
        "{are.1}On ne peut renouveler que ce qu'on a reçu. Une éducation qui préparerait directement les enfants à changer le monde, selon les projets des adultes, leur volerait leur propre nouveauté.",
        "{-are}{dep}Et voilà la clé pour ta copie. {dep.1}L'opposition transmettre ou émanciper peut être dépassée. "
        "{dep.2}La transmission est la condition de l'émancipation. {dep.3}À condition de donner à l'élève les moyens de juger ce qu'il reçoit. Exactement ce que voulait Condorcet.",
        "{-dep}",
    ], vis={
        "q_tr": dict(type="question", t="Transmettre un héritage, ou laisser chacun s'inventer ?"),
        "nie": dict(type="portrait", annee=1844, img="nietzsche", nom="Friedrich Nietzsche", dates="1844 – 1900",
                    legende="*Le Gai Savoir* (1882)"),
        "c_nie": dict(type="cit", a="Nietzsche", o="Le Gai Savoir", ref="§ 270, trad. H. Albert", x=620, y=220, w=540),
        "bea": dict(type="mot", t="1949", g="Simone de Beauvoir, *Le Deuxième Sexe*", taille=130, y=220),
        "c_bea": dict(type="cit", a="Simone de Beauvoir", o="Le Deuxième Sexe", ref="t. II", x=230, y=230, w=820),
        "m61": dict(type="mot", t="Conservatrice ?", g="Hannah Arendt, « La crise de l'éducation » (1961)", taille=110, y=220),
        "are": dict(type="cols", g="Transmettre l'ancien", gq="un monde déjà là", d="Protéger le nouveau",
                    dq="ce que chaque enfant apporte", vs="pour", repere="Arendt, « La crise de l'éducation » (1961) : thèse résumée"),
        "dep": dict(type="liste", titre="Pour la copie : dépasser l'opposition", items=[
            "Transmettre *ou* émanciper ?", "La transmission est la condition de l'émancipation",
            "À condition de donner les moyens de juger ce qu'on reçoit (Condorcet)"], marques=["?", "I", "II"], x=170, y=170, w=960),
    }),

    # ================================================================ X. les notions à manier
    dict(id="notions", chap="Les mots à manier", fond="livre", humeur="calme",
         retenir="Instruction ≠ éducation ; autorité : pouvoir légitime, sans force ni persuasion ; autonomie : se donner sa propre loi ; tradition : ce qui est transmis et reçu comme ayant autorité.",
         beats=[
        "{nu}Avant de passer au bac, quelques mots à manier avec précision. Ce sont eux qui font la différence dans une copie.",
        "{-nu}{d_ie}Instruction et éducation. L'instruction transmet des connaissances et leurs preuves. L'éducation forme la personne entière : les mœurs, le caractère, les valeurs.",
        "{-d_ie}{d_aut}L'{!autorité}autorité. C'est un pouvoir reconnu comme légitime, qui obtient l'obéissance sans contrainte, et sans persuasion. "
        "{d_aut.1}À distinguer de la force, qui contraint, et de l'argumentation, qui convainc.",
        "{-d_aut}{d_auto}Autonomie et hétéronomie. Être autonome, c'est se donner à soi-même sa loi. Être hétéronome, c'est la recevoir d'un autre.",
        "{-d_auto}{d_trad}La tradition, enfin : ce qui est transmis, et reçu comme ayant autorité, parce que c'est ancien. "
        "{d_trad.1}Et la laïcité scolaire : la neutralité religieuse de l'enseignement public, posée par la loi du vingt-huit mars mille huit cent quatre-vingt-deux.",
        "{-d_trad}",
    ], vis={
        "nu": dict(type="nuage", items=["instruction", "éducation", "autorité", "autonomie", "tradition", "laïcité"]),
        "d_ie": dict(type="cols", g="Instruction", gq="des connaissances et leurs preuves", d="Éducation",
                     dq="la personne entière : mœurs, caractère, valeurs", vs="≠"),
        "d_aut": dict(type="def", terme="Autorité", cles=["légitime"],
                      t="Un pouvoir reconnu comme légitime, qui obtient l'obéissance sans contrainte ni persuasion.",
                      etape="≠ la force (contraindre) ≠ l'argumentation (convaincre)", x=190, y=200, w=900),
        "d_auto": dict(type="cols", g="Autonomie", gq="se donner à soi-même sa loi", d="Hétéronomie", dq="la recevoir d'un autre", vs="≠"),
        "d_trad": dict(type="def", terme="Tradition", t="Ce qui est transmis, et reçu comme ayant autorité parce qu'ancien.",
                       etape="Laïcité scolaire : neutralité religieuse de l'enseignement public (loi du 28 mars 1882).", x=190, y=200, w=900),
    }),

    # ================================================================ XI. l'épreuve
    dict(id="epreuve", chap="L'épreuve : un texte, deux questions", fond="livre", humeur="lumiere",
         retenir="Interprétation : répondre à une question précise en s'appuyant sur le texte (citer, analyser, interpréter). Essai : une réflexion argumentée qui part du texte et y revient.",
         beats=[
        "{epr}Passons à l'épreuve écrite. {epr.1}Quatre heures, un texte. {epr.2}Une première question, d'interprétation : littéraire, ou philosophique. Sur dix points. "
        "{epr.3}Une seconde question, l'essai : philosophique, ou littéraire. Sur dix points aussi. "
        "{epr.4}L'intitulé dit toujours quelle approche est attendue. Et si l'interprétation est littéraire, l'essai est philosophique, et inversement. "
        "{epr.5}Deux copies séparées, deux correcteurs.",
        "{-epr}{mint}Commençons par l'interprétation. Ce n'est ni un commentaire complet, ni une explication linéaire. "
        "Tu réponds à une question précise, avec les éléments du texte qui l'éclairent le mieux. "
        "{mint.1}D'abord, lis le texte trois fois : pour comprendre, pour repérer les mouvements avec les lignes, puis crayon en main. "
        "{mint.2}Ensuite, décortique la question. Comment appelle des moyens d'écriture, pourquoi appelle des raisons. Reformule-la en problème. "
        "{mint.3}Puis le brouillon, en tableau.",
        "{-mint}{brou}Trois colonnes : {brou.1}la citation, avec sa ligne ; ce que tu remarques ; ce que ça signifie pour la question. "
        "{brou.2}Une ligne, puis une autre. {brou.3}Puis une troisième. {brou.g}Ensuite, tu regroupes en deux ou trois idées : ce seront tes parties.",
        "{-brou}{par_r}Pour rédiger, chaque paragraphe suit le même mouvement. {par_r.1}Une idée. {par_r.2}Une citation courte, intégrée à ta phrase. "
        "{par_r.3}L'analyse : le procédé ou le concept, nommé avec précision. {par_r.4}Et l'interprétation : ce que ça apporte à la réponse.",
        "{-par_r}{li_ph}Une différence à connaître. {li_ph.g}En interprétation littéraire, on cherche comment le texte produit du sens et des effets : "
        "figures, rythme, lexique, composition. {li_ph.d}En interprétation philosophique, on cherche ce que le texte soutient, et comment il le justifie : "
        "thèse, concepts, distinctions, arguments.",
        "{-li_ph}{mess}Et l'essai ? C'est une réflexion argumentée, construite comme une dissertation courte. Elle part du texte, et elle y revient. "
        "{mess.1}Analyse les termes de la question. {mess.2}Trouve le problème : une tension entre deux réponses également défendables. "
        "{mess.3}Construis un plan qui progresse : la réponse la plus évidente, ses limites, une réponse plus juste. "
        "{mess.4}Et chaque argument a son exemple précis : une œuvre, un auteur, une scène, une date.",
        "{-mess}",
    ], vis={
        "epr": dict(type="illu", nom="epreuve", x=180, y=110, w=940, h=500),
        "mint": dict(type="liste", titre="L'interprétation : avant d'écrire", items=[
            "Lire le texte trois fois (les mouvements, les lignes)", "Décortiquer la question : « comment », « pourquoi »… ; en faire un problème",
            "Un brouillon en tableau"], marques=["I", "II", "III"], x=170, y=170, w=960),
        "brou": dict(type="illu", nom="brouillon", x=150, y=120, w=840, h=470, rh=118, lignes=[
            ["« tout dégénère entre les mains de l'homme » (l. 1)", "antithèse : « bien » / « dégénère »", "l'homme défait l'ordre naturel"],
            ["« Sans cela » (l. 8)", "connecteur : un retournement", "refuser l'éducation serait pire"],
            ["« un arbrisseau » (l. 13)", "métaphore végétale", "sans éducation, l'enfant est exposé"]]),
        "par_r": dict(type="liste", titre="Un paragraphe d'interprétation", items=[
            "Une idée", "Une citation courte, intégrée à ta phrase", "L'analyse : le procédé ou le concept, nommé",
            "L'interprétation : ce que ça apporte à la réponse"], x=170, y=160, w=960),
        "li_ph": dict(type="cols", g="Littéraire", gq="comment le texte produit sens et effets : figures, rythme, lexique",
                      d="Philosophique", dq="ce qu'il soutient et comment : thèse, concepts, arguments", vs="ou"),
        "mess": dict(type="liste", titre="L'essai : une réflexion qui part du texte", items=[
            "Analyser les termes de la question", "Trouver le problème : deux réponses défendables",
            "Un plan qui progresse : l'évidence, ses limites, une réponse plus juste", "Chaque argument, son exemple précis"],
            x=170, y=150, w=960),
    }),

    # ================================================================ XII. sujet type bac : l'interprétation
    dict(id="sujet", chap="Sujet type bac : l'interprétation", fond="livre", humeur="tension", beats=[
        "{doc}Place à l'entraînement. Voici un sujet type bac. Le texte, tu le connais déjà : l'ouverture d'Émile. Quinze lignes. "
        "{doc.1}Le réquisitoire, {doc.2}le retournement, {doc.3}et la formule finale.",
        "{-doc}{exo}Première question, d'interprétation philosophique : selon Rousseau, pourquoi l'éducation est-elle à la fois une menace et une nécessité ? "
        "Et la seconde, d'essai littéraire : la littérature montre-t-elle que l'on devient soi-même contre son éducation ? "
        "Commençons par la première.",
        "{-exo}{pa1}À toi. Mets la vidéo sur pause. Repère la thèse, découpe le texte avec les lignes, et prépare ton introduction et ton plan.",
        "{pa1.stop}{-pa1}{exc}{exc.q1}Correction. {intro}D'abord l'introduction. {intro.1}Une amorce liée au texte : la formule finale semble faire de l'éducation une simple technique, comme le jardinage. "
        "{intro.2}Pourtant, quelques lignes plus haut, Rousseau dénonçait l'homme qui veut tout dresser. "
        "{intro.3}D'où le problème : comment l'éducation, qui ressemble à la manière dont l'homme défigure la nature, peut-elle être aussi ce qui la sauve ? "
        "{intro.4}La thèse : dans une société corrompue, l'éducation est indispensable pour protéger la nature en l'homme, à condition de cultiver au lieu de dresser.",
        "{-intro}{p1}Première partie : une menace, lignes un à sept. {p1.1}L'antithèse oppose deux mains : celles de l'Auteur des choses, et celles de l'homme, qui défait l'ordre naturel. "
        "{p1.2}L'énumération des violences va de la terre à l'animal, puis à l'esclave. "
        "{p1.3}Sommet : pas même l'homme. L'éducation ordinaire est un dressage, comme un cheval de manège. La menace, c'est le conformisme.",
        "{-p1}{p2}Deuxième partie : une nécessité, lignes huit à quatorze. {p2.1}Le connecteur « Sans cela » marque un retournement. Et l'argument est historique : "
        "dans l'état où sont désormais les choses, on ne revient pas à la nature. "
        "{p2.2}La société n'est pas neutre : préjugés, autorité, exemple étoufferaient la nature. Un enfant sans éducation ne serait pas libre : il serait le plus défiguré de tous. "
        "{p2.3}L'arbrisseau au milieu du chemin le montre : l'absence d'éducation, ce n'est pas la liberté, c'est l'exposition.",
        "{-p2}{p3}Troisième partie : cultiver plutôt que dresser, ligne quinze. {p3.1}La métaphore végétale change de sens. Le jardinier contournait l'arbre ; la culture accompagne une croissance qui vient de la plante elle-même. "
        "{p3.2}D'où le projet de l'Émile : une éducation négative, qui protège l'enfant du vice et de l'erreur. "
        "{p3.3}Et une ouverture : Kant dira que l'homme ne devient homme que par l'éducation. La question n'est plus faut-il éduquer, mais comment éduquer sans asservir.",
        "{-p3}{-exc}",
    ], vis={
        "doc": dict(type="document", x=130, y=80, w=1060, taille=26, chapeau="Rousseau ouvre son traité d'éducation.",
                    ref="Jean-Jacques Rousseau, Émile ou De l'éducation, livre I (1762).",
                    lignes=[
                        "Tout est bien, sortant des mains de l'Auteur des choses : tout dégénère entre les",
                        "mains de l'homme. Il force une terre à nourrir les productions d'une autre, un arbre à",
                        "porter les fruits d'un autre : il mêle et confond les climats, les éléments, les saisons : il",
                        "mutile son chien, son cheval, son esclave : il bouleverse tout, il défigure tout : il aime la",
                        "difformité, les monstres : il ne veut rien, tel que l'a fait la nature, pas même l'homme ; il",
                        "le faut dresser pour lui, comme un cheval de manège ; il le faut contourner à sa mode,",
                        "comme un arbre de son jardin.",
                        "Sans cela, tout irait plus mal encore, et notre espèce ne veut pas être façonnée à",
                        "demi. Dans l'état où sont désormais les choses, un homme abandonné dès sa naissance",
                        "à lui-même parmi les autres, serait le plus défiguré de tous. Les préjugés, l'autorité, la",
                        "nécessité, l'exemple, toutes les institutions sociales dans lesquelles nous nous trouvons",
                        "submergés, étoufferaient en lui la nature, et ne mettraient rien à la place. Elle y serait",
                        "comme un arbrisseau que le hasard fait naître au milieu d'un chemin, et que les passants",
                        "font bientôt périr, en le heurtant de toutes parts et le pliant dans tous les sens.",
                        "[…] On façonne les plantes par la culture, et les hommes par l'éducation."],
                    hl=[[1, 7], [8, 14], [15, 15]]),
        "exo": dict(type="exo", niveau="bac", titre="Rousseau, *Émile*, livre I (1762)",
                    enonce=["Le texte : l'ouverture d'*Émile* (15 lignes)."],
                    questions=["Interprétation philosophique : selon Rousseau, pourquoi l'éducation est-elle à la fois une menace et une nécessité ?",
                               "Essai littéraire : la littérature montre-t-elle que l'on devient soi-même contre son éducation ?"]),
        "pa1": dict(type="pause", t="La thèse, le découpage (avec les lignes), l'introduction et le plan."),
        "exc": dict(type="exo", mode="coin", niveau="bac", titre="L'interprétation",
                    donnees=["*Émile*, livre I"],
                    questions=["Pourquoi l'éducation est-elle à la fois une menace et une nécessité ?"]),
        "intro": dict(type="liste", titre="L'introduction", items=[
            "Amorce : « On façonne les plantes par la culture… » : une technique ?", "Pourtant, l'homme qui veut tout « dresser »",
            "Problème : ce qui défigure peut-il sauver ?", "Thèse : protéger la nature en l'homme, cultiver au lieu de dresser"],
            x=560, y=120, w=620),
        "p1": dict(type="liste", titre="I. Une menace (l. 1-7)", items=[
            "L'antithèse des deux « mains »", "L'énumération : la terre, l'animal, l'« esclave »",
            "« pas même l'homme » : le dressage, le conformisme"], x=560, y=140, w=620),
        "p2": dict(type="liste", titre="II. Une nécessité (l. 8-14)", items=[
            "« Sans cela » : un retournement ; un argument historique", "La société n'est pas neutre : « le plus défiguré de tous »",
            "L'arbrisseau : l'absence d'éducation n'est pas la liberté"], x=560, y=140, w=620),
        "p3": dict(type="liste", titre="III. Cultiver plutôt que dresser (l. 15)", items=[
            "La métaphore végétale change de sens", "Le projet de l'*Émile* : l'éducation négative",
            "Ouverture : Kant ; comment éduquer sans asservir ?"], x=560, y=140, w=620),
    }),

    # ================================================================ XIII. sujet type bac : l'essai
    dict(id="essai", chap="Sujet type bac : l'essai", fond="livre", humeur="tension",
         retenir="On ne devient pas soi « contre » son éducation, mais en la reprenant pour son compte : la révolte se fait avec les armes de l'éducation, et l'écriture la transforme en œuvre.",
         beats=[
        "{q_es}Seconde question, l'essai littéraire. La littérature montre-t-elle que l'on devient soi-même contre son éducation ?",
        "{-q_es}{ana}D'abord, les termes. {ana.1}Devenir soi-même : c'est un processus, pas un état. "
        "{ana.2}Contre : ce peut être une opposition, une rupture… ou s'appuyer sur quelque chose pour s'en écarter. "
        "{ana.3}Montrer : la littérature représente, raconte, fait éprouver. Et c'est un essai littéraire : il faut des œuvres précises, des scènes, des dates.",
        "{-ana}{pa2}À toi. Mets sur pause, et cherche le problème et un plan en trois parties, avec un exemple par argument.",
        "{pa2.stop}{-pa2}{pb}Correction. Le problème : les récits d'enfance semblent raconter des ruptures. Mais ces ruptures doivent beaucoup à ce qui a été reçu.",
        "{-pb}{e1}Première partie : la littérature raconte des ruptures. {e1.1}Vallès, L'Enfant : la famille et le collège humilient, et la trilogie mène jusqu'à la Commune. "
        "{e1.2}Rimbaud, dans sa lettre à Paul Demeny du quinze mai mille huit cent soixante et onze, liquide les modèles scolaires : « Après Racine, le jeu moisit ». "
        "{e1.3}Et Julien Sorel, fils de charpentier, s'invente contre son milieu.",
        "{-e1}{e2}Deuxième partie : mais la révolte doit beaucoup à l'éducation qu'elle combat. {e2.1}Julien Sorel se forme par les livres, et par le latin que lui apprend le curé. "
        "{e2.2}Rimbaud est un élève brillant, nourri de vers latins : son dérèglement est raisonné. "
        "{e2.3}Et chez Flaubert, Frédéric Moreau rompt… et ne devient rien. Sans forme, la liberté tourne à vide.",
        "{-e2}{e3}Troisième partie : écrire son éducation, c'est devenir soi en la reprenant. {e3.1}Le récit d'enfance est un regard d'adulte : "
        "l'écrivain ne rejette pas son passé, il le transforme en œuvre, comme Chateaubriand. "
        "{e3.2}Rousseau, dans les Confessions, montre comment l'enfance forme les penchants de l'homme. "
        "{e3.3}Et pour aller plus loin, Annie Ernaux écrit avec la culture acquise à l'école, pour rendre justice au monde qu'elle a quitté.",
        "{-e3}{conc}Conclusion : on ne devient pas soi contre son éducation, mais en la reprenant pour son propre compte. "
        "Ce qui rejoint le vœu de Kant : penser par soi-même, après avoir appris à penser.",
        "{-conc}",
    ], vis={
        "q_es": dict(type="question", t="La littérature montre-t-elle que l'on devient soi-même contre son éducation ?"),
        "ana": dict(type="liste", titre="Analyser les termes", items=[
            "« devenir soi-même » : un processus, pas un état", "« contre » : rompre… ou s'appuyer pour s'écarter",
            "« montrer » : représenter, raconter, faire éprouver"], x=170, y=170, w=960),
        "pa2": dict(type="pause", t="Le problème, puis un plan en trois parties, un exemple précis par argument."),
        "pb": dict(type="def", terme="Le problème", t="Les récits d'enfance semblent raconter des ruptures ; mais ces ruptures doivent beaucoup à ce qui a été reçu.",
                   x=190, y=230, w=900),
        "e1": dict(type="liste", titre="I. Des ruptures : on devient soi contre ce qu'on a reçu", items=[
            "Vallès, *L'Enfant* (1878) : jusqu'à *L'Insurgé* et la Commune", "Rimbaud à Demeny (15 mai 1871) : « Après Racine, le jeu moisit »",
            "Julien Sorel, fils de charpentier, contre son milieu (1830)"], x=170, y=150, w=980),
        "e2": dict(type="liste", titre="II. Mais la révolte doit beaucoup à l'éducation", items=[
            "Julien Sorel : les livres, le latin du curé", "Rimbaud, élève brillant : un dérèglement « raisonné »",
            "Frédéric Moreau ne devient rien : la liberté sans forme tourne à vide"], x=170, y=150, w=980),
        "e3": dict(type="liste", titre="III. Écrire son éducation, c'est la reprendre", items=[
            "Chateaubriand : le passé transformé en œuvre", "Rousseau, *Confessions* : l'enfance forme les penchants",
            "Pour aller plus loin : Ernaux, *La Place* (1983)"], x=170, y=150, w=980),
        "conc": dict(type="def", terme="Conclusion", cles=["reprenant"],
                     t="On ne devient pas soi « contre » son éducation, mais en la reprenant pour son propre compte.",
                     etape="Kant : penser par soi-même, après avoir appris à penser.", x=190, y=210, w=900),
    }),

    # ================================================================ XIV. les pièges
    dict(id="pieges", chap="Les pièges classiques", fond="livre", humeur="tension",
         retenir="Éducation ≠ instruction ; Rousseau n'est pas le « laisser-faire » ; Kant ne rejette pas les maîtres ; *L'Enfant* est un roman ; l'école gratuite, obligatoire et laïque, ce sont les lois Ferry ; une citation s'explique.",
         beats=[
        "{pg}Faisons le tour des pièges. {pg.1}Un : confondre éducation et instruction. Chez Condorcet, cette distinction est le cœur du raisonnement.",
        "{pg.2}Deux : faire de Rousseau un partisan du laisser-faire. L'éducation négative est entièrement mise en scène par le gouverneur, qui organise les expériences d'Émile.",
        "{pg.3}Trois : croire que Kant rejette tout maître. Il critique la paresse de rester mineur, et il réclame la liberté de l'usage public de la raison. Pas la fin de l'enseignement.",
        "{pg.4}Quatre : lire L'Enfant comme un simple témoignage. C'est un roman autobiographique, avec une construction et une ironie.",
        "{pg.5}Cinq : dater l'école gratuite, obligatoire et laïque de la Révolution. Ce sont les lois Ferry, en mille huit cent quatre-vingt-un et quatre-vingt-deux.",
        "{pg.6}Et six : plaquer des citations sans les expliquer. Une citation de Kant ou de Rousseau doit être reliée au texte du sujet. Pas récitée.",
        "{-pg}",
    ], vis={
        "pg": dict(type="liste", titre="Les pièges classiques", items=[
            "Confondre éducation et instruction", "Rousseau, partisan du « laisser-faire » ? Non : le gouverneur organise tout",
            "Kant ne rejette pas les maîtres : il réclame l'usage public de la raison", "*L'Enfant* : un roman autobiographique, pas un témoignage",
            "L'école gratuite, obligatoire et laïque : les lois Ferry (1881-1882)", "Une citation s'explique, elle ne se récite pas"],
            marques=["☞"] * 6, x=150, y=110, w=1000),
    }),

    # ================================================================ XV. récapitulatif
    dict(id="recap", chap="Ce qu'il faut savoir pour le bac", fond="livre", humeur="lumiere", beats=[
        "{fr}Récapitulons, avec les auteurs de cette entrée. {fr.1}Montaigne, la tête bien faite. {fr.2}Rousseau, l'enfance et l'éducation négative. "
        "{fr.3}Kant, la minorité et le courage de penser. {fr.4}Condorcet, l'instruction qui rend libre. "
        "{fr.5}Flaubert, l'éducation qui ne forme rien. {fr.6}Vallès, la révolte. {fr.7}Jules Ferry, l'école gratuite, obligatoire et laïque. "
        "{fr.8}Nietzsche, devenir soi. {fr.9}Et Beauvoir, qui montre comment l'éducation fabrique des rôles.",
        "{-fr}{cm}En une image. {cm.1}Transmettre : Montaigne, Kant, Arendt. {cm.2}Libérer : Rousseau, Kant, Condorcet. "
        "{cm.3}Instruire des citoyens : Condorcet, Ferry, Durkheim. {cm.4}Et raconter : Vallès, Flaubert, le roman d'apprentissage.",
        "{-cm}{pb_f}Et le problème en une phrase. L'éducation est la condition de la liberté, car on ne pense pas seul sans avoir appris. "
        "Et elle en est la menace, car elle peut dresser. S'émanciper, c'est reprendre pour son compte ce que l'on a reçu.",
        "{-pb_f}{bac}Voici ce que le bac peut te demander, à cocher. {bac.1}Distinguer éducation et instruction. "
        "{bac.2}Expliquer le paradoxe de Rousseau, menace et nécessité. {bac.3}Définir la minorité selon Kant. "
        "{bac.4}Dire pourquoi une démocratie a besoin d'une école, avec Condorcet et les lois Ferry. "
        "{bac.5}Analyser un récit d'enfance, ou un roman d'apprentissage. {bac.6}Et rédiger une interprétation et un essai, textes à l'appui.",
        "Si tu sais faire ces six choses, cette entrée est à toi. Le cours, les textes clés, le QCM et la fiche à imprimer sont sur le site : "
        "le lien est dans la description. Et pour vérifier tout de suite, un quiz sur cette vidéo t'y attend aussi.",
        "{-bac}",
    ], vis={
        "fr": dict(type="frise", items=[
            dict(nom="Montaigne", d=1580, img="montaigne", q="la tête bien faite"),
            dict(nom="Rousseau", d=1762, img="rousseau", q="l'enfance"),
            dict(nom="Kant", d=1784, img="kant", q="*Sapere aude*"),
            dict(nom="Condorcet", d=1791, img="condorcet", q="instruire"),
            dict(nom="Flaubert", d=1869, img="flaubert", q="l'apprentissage raté"),
            dict(nom="Vallès", d=1878, img="valles", q="la révolte"),
            dict(nom="Ferry", d=1882, img="ferry", q="l'école laïque"),
            dict(nom="Nietzsche", d=1882, img="nietzsche", q="devenir soi"),
            dict(nom="Beauvoir", d=1949, q="les rôles appris")]),
        "cm": dict(type="carte", centre="ÉDUQUER · ÉMANCIPER", branches=[
            dict(t="Transmettre", items=["Montaigne : former le jugement", "Kant : discipline, instruction", "Arendt : l'ancien, pour le nouveau"]),
            dict(t="Libérer", items=["Rousseau : l'éducation négative", "Kant : *Sapere aude*", "Condorcet : corriger la loi"]),
            dict(t="Instruire des citoyens", items=["Condorcet (1791)", "Lois Ferry (1881-1882)", "Durkheim : socialiser"]),
            dict(t="Raconter", items=["Vallès, *L'Enfant* (1878)", "Flaubert (1869)", "le roman d'apprentissage"])]),
        "pb_f": dict(type="def", terme="Le problème en une phrase", cles=["condition", "menace"],
                     t="L'éducation est la condition de la liberté et sa menace : s'émanciper, c'est reprendre pour son compte ce que l'on a reçu.",
                     x=190, y=210, w=900),
        "bac": dict(type="liste", titre="Pour le bac · à cocher", items=[
            "Distinguer éducation et instruction", "Le paradoxe de Rousseau : menace et nécessité", "La minorité selon Kant",
            "Pourquoi une démocratie a besoin d'une école (Condorcet, Ferry)", "Analyser un récit d'enfance, un roman d'apprentissage",
            "Rédiger une interprétation et un essai, textes à l'appui"], marques=["✓"] * 6, x=170, y=110, w=980),
    }),
]

QUIZ = [
    dict(q="La « tête bien faite » de Montaigne (Essais, I, 26) désigne d'abord…", r=["la tête de l'élève, pleine de savoirs", "le précepteur à choisir, qui juge plutôt qu'il n'accumule", "un enfant de la noblesse bien élevé"],
         ok=1, ex="La formule porte sur le choix du « conducteur » (le précepteur) : former le jugement plutôt que remplir la mémoire.", voir="c_mont"),
    dict(q="L'« éducation négative » de Rousseau consiste à…", r=["ne rien apprendre à l'enfant", "protéger l'enfant du vice et de l'erreur au lieu de lui enseigner la vertu", "punir chaque faute"],
         ok=1, ex="« garantir le cœur du vice et l'esprit de l'erreur » (Émile, II) ; le gouverneur organise les expériences.", voir="c_neg"),
    dict(q="Le seul livre qu'Émile lira longtemps est…", r=["les Fables de La Fontaine", "Robinson Crusoé", "les Essais de Montaigne"],
         ok=1, ex="Un homme seul qui pourvoit à ses besoins : un livre d'expérience.", voir="mont3"),
    dict(q="« L'homme ne peut devenir homme que par l'éducation. » Qui l'écrit ?", r=["Rousseau", "Condorcet", "Kant"],
         ok=2, ex="Kant, dans les leçons de pédagogie publiées en 1803 (trad. Barni).", voir="c_kant1"),
    dict(q="Pour Condorcet, sans instruction publique…", r=["l'égalité des droits reste théorique", "la religion disparaît", "l'armée s'affaiblit"],
         ok=0, ex="Celui qui ne sait pas écrire « dépend réellement de l'homme plus instruit ».", voir="pq"),
    dict(q="Selon Condorcet, le but de l'instruction est de rendre les citoyens capables…", r=["d'admirer la Constitution", "d'apprécier et de corriger la loi", "d'obéir sans discuter"],
         ok=1, ex="« … non pas de faire admirer aux hommes une législation toute faite ».", voir="c_but"),
    dict(q="L'instruction primaire devient obligatoire (de 6 à 13 ans) et l'enseignement public laïque…", r=["en 1791", "en 1833", "en 1882"],
         ok=2, ex="Loi du 28 mars 1882 ; la gratuité date de 1881 (lois Ferry).", voir="jal"),
    dict(q="Pour Kant, la « minorité » vient surtout…", r=["du jeune âge", "de la paresse et de la lâcheté", "d'un manque d'intelligence"],
         ok=1, ex="Ce n'est ni une question d'âge ni d'intelligence, mais de courage.", voir="d_min"),
    dict(q="L'officier qui, comme savant, critique par écrit l'organisation de l'armée fait…", r=["un usage privé de la raison", "un usage public de la raison", "une faute"],
         ok=1, ex="Dans son service, il obéit (usage privé) ; comme savant, il publie (usage public).", voir="us"),
    dict(q="Pourquoi L'Éducation sentimentale renverse-t-elle le roman d'apprentissage ?", r=["Le héros ne devient rien", "Le roman se passe dans une école", "Le héros est un enfant"],
         ok=0, ex="Frédéric Moreau traverse l'amour et 1848 sans se former : « C'est là ce que nous avons eu de meilleur ! »", voir="crb"),
]

CREDITS = [
    "Textes cités d'après les éditions du domaine public (Wikisource), orthographe modernisée quand elle est ancienne ; "
    "Kant dans la traduction de Jules Barni, Nietzsche dans celle d'Henri Albert. Beauvoir : citation courte ; Arendt : thèse résumée.",
    "Portraits : Montaigne (portrait anonyme, musée Condé) ; Rousseau (Maurice Quentin de La Tour, 1753) ; Kant (portrait anonyme, XVIIIᵉ s.) ; "
    "Condorcet (peintre non identifié, autrefois attribué à Greuze) ; Jules Ferry (Léon Bonnat, 1888) ; Jules Vallès (Gustave Courbet) ; "
    "Gustave Flaubert (photographie de Nadar) ; Durkheim (photographie anonyme) ; Nietzsche (Gustav Schultze, 1882) : domaine public, Wikimedia Commons.",
    "Planches : Rousseau, Émile ou De l'éducation, page de titre (1762) ; Albert Bettannier, La Tache noire (1887, musée d'Orsay) ; "
    "Jan Steen, L'École de village (vers 1665, National Gallery of Ireland) : domaine public.",
    "Illustrations, schémas et sujet corrigé : faits pour le site. Polices : EB Garamond et Exlibris Titrage (d'après IM FELL), sous licence SIL OFL.",
]
