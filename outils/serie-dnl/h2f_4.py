"""Histoire · « Les régimes totalitaires » — édition française de la série vidéo, épisode 4 : « Le chef, le parti et
l'homme nouveau » (parties II.1 et II.2 du cours).

Traduction et adaptation de h2_4.py (édition anglaise, gardée intacte) selon outils/serie-dnl/EDITION_FR.md :
histoire-géographie classique de Terminale, sans mention de la DNL ni de l'épreuve en anglais ; mêmes scènes, mêmes
visuels, mêmes repères, mêmes cartes animées (sc = numéros de scènes de la carte, qui passe d'elle-même en français).
  H2 : 6 marche sur Rome · 8 la dictature rendue légale · 9 le culte du chef, villes rebaptisées · 11 la jeunesse
       d'abord, trois « hommes nouveaux » · 12 plan quinquennal et collectivisation · 20 Hitler chancelier ·
       23 nazisme, lutte des races · 24 rassemblements, médias, arts · 26 Stakhanov
Contenu : CHAPTERS.H2 du site, sections II.1 et II.2, schémas « Trois chefs, trois cultes » et « Fabriquer un homme
nouveau » ; Worksheet 3 → « le dossier documentaire sur la jeunesse » (source 2 → document 2) ; Worksheet 4 → « le
dossier documentaire sur la terreur ». Points de vigilance du site gardés (le géorgien n'a pas été interdit ; Iejov et
non Beria ou Molotov). Hors du cours, dit comme tel : date du décret de mars 1938 sur le russe, record de Stakhanov
préparé à l'avance, Jeunesses hitlériennes réellement obligatoires en 1939.
Adaptations : paragraphe d'essay « Explain » → paragraphe de réponse à une question problématisée ; DBQ a) « How useful »
→ analyse de document sur le discours de Hitler de 1938 (présenter, situer, expliquer, intérêt et limites, bilan
critique). Citations en traduction française : Mussolini (« Je prends les hommes au berceau… »), publicité du
Volksempfänger (traduction au plus près de la version citée par le cours).
Chaîne : outils/serie-philo/generer.py h2f_4 ; sortie dans dnl/serie/ (h2f-4.*).
Plan de la série : 1 Qu'est-ce que le totalitarisme ? · 2 De la Grande Guerre au pouvoir · 3 Trois régimes, trois
idéologies · 4 Le chef, le parti et l'homme nouveau · 5 La terreur de masse · 6 Des ambitions hégémoniques ·
7 L'apaisement et la marche à la guerre · 8 Les totalitarismes à l'épreuve · 9 Récapitulatif.
"""

SITE = "dnl"
LANGUE = "fr"
CODE = "h2f-4"
NOTION = "Les régimes totalitaires"
NUM = 4
TITRE = "Le chef, le parti et l'homme nouveau"
SUIVANT = "Épisode 5 · La terreur de masse"
PRONONCIATION = {"Il Duce ha sempre ragione": "Il Dou-tché a sèmm-pré ra-djo-né",
                 "Credere, obbedire, combattere": "Cré-dé-ré, ob-bé-di-ré, comm-ba-té-ré",
                 "Opera Nazionale Balilla": "O-pé-ra Na-tsio-na-lé Ba-lil-la",
                 "Heil Hitler": "Haïl Hitler", "Duce": "Dou-tché", "Führer": "Fu-reur",
                 "Volksempfänger": "Folks-èmm-pfèn-gueur", "Riefenstahl": "Rii-fenn-chtal", "Goebbels": "Gueu-bèlss",
                 "Moukhina": "Mou-ki-na", "Iejov": "Ié-jof", "Stakhanov": "Sta-ka-nof", "stakhanovisme": "sta-ka-no-visme",
                 "Balilla": "Ba-lil-la", "Komsomol": "Komm-so-mol", "Giftpilz": "Guift-pilts", "Mischling": "Mich-ling",
                 "Volk": "Folk", "Jungvolk": "Ioung-folk", "Lanzinger": "Lann-tsing-eur", "Hindenburg": "Hinn-denn-bourg",
                 "Matteotti": "Mat-té-ot-ti", "Wehrmacht": "Vèr-markt", "Hoffmann": "Hof-mann",
                 "NKVD": "èn-ka-vé-dé", "Donbass": "Donn-bass", "Alexeï": "A-lek-sè-ï", "Nikolaï": "Ni-ko-la-ï"}

REG = ["IT", "DE", "SU"]     # marques des listes de comparaison : Italie fasciste, Allemagne nazie, URSS de Staline

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Ouverture", fond="nuit", humeur="mystere", carton=False, beats=[
        "{g0}{g0.1}Nuremberg, septembre mille neuf cent trente-quatre. Des centaines de milliers d'hommes en uniforme, alignés à la perfection. "
        "Des projecteurs. Des drapeaux. Et un homme, sur une tribune. Une équipe de cinéma filme tout, pour que l'Allemagne entière le voie.",
        "{q1}Pourquoi bâtir un culte autour d'un seul homme ?",
        "{-q1}{q2}Et pourquoi ces régimes voulaient-ils prendre les enfants dès l'âge de dix ans ?",
        "{-q2}{-g0}{plan}Aujourd'hui, la deuxième partie du chapitre, points un et deux. {plan.1}D'abord, l'histoire sur la carte, de mille neuf cent vingt-deux à mille neuf cent trente-six. "
        "{plan.2}Puis le culte de la personnalité, et le culte du parti. Six idées. "
        "{plan.3}Puis le contrôle total de la société, et la fabrication d'un homme nouveau. Six autres idées, et un dossier documentaire. "
        "{plan.4}Et pour finir, l'entraînement : un paragraphe de réponse à une question problématisée, et une analyse de document.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H2", sc=[24]),
        "q1": dict(type="question", t="Pourquoi un culte autour d'un seul homme ?", bande=True),
        "q2": dict(type="question", t="Pourquoi prendre les enfants dès dix ans ?", bande=True),
        "plan": dict(type="liste", titre="Épisode 4 · le plan", items=[
            "Sur la carte : chefs, partis et jeunesse, 1922 – 1936", "II.1 · Culte de la personnalité et culte du parti",
            "II.2 · Contrôle total de la société et fabrication d'un « homme nouveau »",
            "Entraînement : une question problématisée et une analyse de document"], x=170, y=130, w=940),
        "titre": dict(type="titre", sur="Histoire · Les régimes totalitaires · Épisode 4", t="Le chef, le parti et l'homme nouveau",
                      sous="Culte, propagande, jeunesse · 1922 – 1936 · parties II.1 et II.2 du cours"),
    }),

    # ================================================================ la carte : 1922-1928
    dict(id="carte1", chap="Sur la carte : 1922 – 1928", fond="nuit", humeur="tension",
         retenir="Oct. 1922 marche sur Rome · 1925 la dictature rendue légale · 1924-1925 Leningrad, Stalingrad · 1926 Balilla · 1928 le premier plan quinquennal.",
         beats=[
        "{g1}{g1.1}Octobre mille neuf cent vingt-deux. En Italie, les fascistes marchent sur Rome, et Mussolini devient président du Conseil.",
        "{g1.2}En mille neuf cent vingt-quatre, le député socialiste Matteotti est assassiné. En mille neuf cent vingt-cinq, les lois fascistissimes rendent la dictature légale. "
        "Désormais, il n'y a plus qu'un parti. Et un homme : il Duce.",
        "{g1.3}Au même moment, en Union soviétique, Lénine meurt, et une ville prend son nom. "
        "En mille neuf cent vingt-quatre, Petrograd devient Leningrad. En mille neuf cent vingt-cinq, une autre ville est rebaptisée du nom du nouveau maître : Stalingrad. "
        "Le nom du chef s'inscrit sur la carte elle-même.",
        "{g1.4}La cible suivante, c'est la jeunesse. En mille neuf cent vingt-six, l'Italie crée l'Opera Nazionale Balilla. L'Union soviétique a déjà son Komsomol, "
        "créé en mille neuf cent dix-huit. L'Allemagne suivra.",
        "{g1.5}Et en mille neuf cent vingt-huit, Staline lance le premier plan quinquennal. Désormais, c'est le parti qui dirige l'économie.",
    ], vis={
        "g1": dict(type="globe", code="H2", sc=[6, 8, 9, 11, 12]),
    }),

    # ================================================================ la carte : 1933-1936
    dict(id="carte2", chap="Sur la carte : 1933 – 1936", fond="nuit", humeur="tension",
         retenir="30 janv. 1933 Hitler chancelier · sept. 1933 enseignement racial à l'école · 1934 le congrès de Nuremberg filmé · 1935 lois de Nuremberg · 1935 Stakhanov · 1936 loi sur les Jeunesses hitlériennes.",
         beats=[
        "{g2}{g2.1}Le trente janvier mille neuf cent trente-trois. À Berlin, le président Hindenburg nomme Hitler chancelier. "
        "En quelques mois, les nazis contrôlent l'État. Puis ils s'attaquent à la société.",
        "{g2.2}En septembre mille neuf cent trente-trois, l'enseignement racial devient obligatoire dans les écoles allemandes. "
        "En septembre mille neuf cent trente-cinq, les lois de Nuremberg décident qui est citoyen, et qui ne l'est pas. Selon l'ascendance.",
        "{g2.3}Nuremberg, c'est aussi la ville des grands rassemblements. En mille neuf cent trente-quatre, Leni Riefenstahl filme le congrès du parti. Le film s'appelle Le Triomphe de la volonté. "
        "Et une radio bon marché, le poste du peuple, fait entrer la voix du Führer dans chaque foyer.",
        "{g2.4}Pendant ce temps, dans le Donbass, en mille neuf cent trente-cinq, un mineur nommé Alexeï Stakhanov est célébré comme un héros. "
        "Il aurait extrait quatorze fois sa norme de charbon en une seule équipe. L'homme nouveau soviétique est un travailleur.",
        "{-g2}{fr1}Voici donc six dates à connaître. {fr1.1}Mille neuf cent vingt-quatre et vingt-cinq : Leningrad, puis Stalingrad. {fr1.2}Mille neuf cent vingt-six : les Balilla. "
        "{fr1.3}Septembre mille neuf cent trente-trois : l'enseignement racial dans les écoles allemandes. {fr1.4}Mille neuf cent trente-quatre : Riefenstahl filme le congrès de Nuremberg. "
        "{fr1.5}Mille neuf cent trente-cinq : les lois de Nuremberg, et Stakhanov. {fr1.6}Et mille neuf cent trente-six : la loi sur les Jeunesses hitlériennes.",
    ], vis={
        "g2": dict(type="globe", code="H2", sc=[20, 23, 24, 26]),
        "fr1": dict(type="frise", items=[
            dict(nom="Leningrad, Stalingrad", d=1924, q="1924-1925"), dict(nom="Balilla", d=1926, q="Italie"),
            dict(nom="Enseignement racial", d=1933, q="septembre"), dict(nom="Le Triomphe de la volonté", d=1934, q="congrès de Nuremberg"),
            dict(nom="Lois de Nuremberg · Stakhanov", d=1935, q="1935"),
            dict(nom="Jeunesses hitlériennes", d=1936, q="la loi")]),
    }),

    # ================================================================ II.1, idée 1 : le Guide
    dict(id="guide", chap="II.1 · Le chef, le Guide", fond="nuit", humeur="lumiere",
         retenir="Le chef = un homme idéal, le Guide, l'incarnation de la nation : « il Duce », « der Führer », « le petit père des peuples ». Leningrad (1924), Stalingrad (1925). Lanzinger, Le Porte-drapeau (1934-1936).",
         beats=[
        "{photo1}{def1}Passons au cours, idée par idée. Partie deux, point un : le culte de la personnalité, et le culte du parti. "
        "Première idée. La propagande totalitaire ne se contente pas de vanter un homme politique. Elle fabrique {!un être supérieur}un être supérieur : "
        "le Guide. Ses qualités sont celles que le peuple doit acquérir. "
        "{def1.1}Il est à la fois soldat, travailleur, père et visionnaire. Ce n'est pas un chef de gouvernement qu'on pourrait remplacer. "
        "C'est l'incarnation de la nation.",
        "{-def1}{noms}Alors le chef reçoit un titre. {noms.1}Mussolini, c'est il Duce, le chef. {noms.2}Hitler, c'est der Führer, le guide. "
        "{noms.3}Et Staline, c'est le petit père des peuples. {noms.4}Le peintre Hubert Lanzinger a même représenté Hitler en chevalier du Moyen Âge, "
        "en armure, portant le drapeau. Le tableau s'appelle Le Porte-drapeau, de mille neuf cent trente-quatre à trente-six.",
        "{-noms}{-photo1}{g3}{g3.1}Et le nom du chef s'inscrit sur la carte. Après la mort de Lénine, Petrograd devient Leningrad, en mille neuf cent vingt-quatre. "
        "En mille neuf cent vingt-cinq, une ville sur la Volga est rebaptisée Stalingrad. Une ville n'est plus seulement un lieu : c'est le monument d'un homme vivant.",
    ], vis={
        "photo1": dict(type="tableau", img="h2-stalin", fond=True, sombre=True, de=[1.0, .5, .35], a=[1.15, .5, .3],
                       legende="Joseph Staline sur une tribune, Moscou, 1937 · photographe inconnu, domaine public"),
        "def1": dict(type="def", cles=["supérieur", "Guide", "nation"], terme="Notion clé · le culte de la personnalité",
                     t="La glorification systématique du chef : un être supérieur, le Guide, présenté comme l'incarnation de la nation.",
                     etape="À la fois soldat, travailleur, père et visionnaire : pas un chef de gouvernement qu'on pourrait remplacer", x=170, y=190, w=940),
        "noms": dict(type="liste", titre="Trois chefs, trois titres", marques=REG + ["✻"], items=[
            "Mussolini : « il Duce », le chef", "Hitler : « der Führer », le guide",
            "Staline : « le petit père des peuples »",
            "Lanzinger : Hitler en chevalier portant le drapeau, Le Porte-drapeau (1934-1936)"], x=150, y=130, w=980),
        "g3": dict(type="globe", code="H2", sc=[9]),
    }),

    # ================================================================ II.1, idée 2 : rassemblements et rituels
    dict(id="rituels", chap="II.1 · Rassemblements et rituels", fond="guerre", humeur="tension",
         retenir="Rassemblements, défilés, saluts, devises : un lien émotionnel avec le chef. « Heil Hitler » · « Il Duce ha sempre ragione » · « Credere, obbedire, combattere » · Nuremberg 1934, Le Triomphe de la volonté · des discours de 3 à 4 heures.",
         beats=[
        "{g4}{g4.1}Deuxième idée. Ces régimes gouvernent par {!la mise en scène}la mise en scène. Rassemblements, défilés, saluts et devises font de l'adhésion politique "
        "une expérience physique, partagée par la foule. L'individu se sent fondu dans une masse disciplinée.",
        "{rit}{rit.1}En Allemagne, le salut officiel devient Heil Hitler, avec le salut nazi. "
        "{rit.2}En Italie, une devise dit tout : Il Duce ha sempre ragione. Mussolini a toujours raison. "
        "{rit.3}Le cours donne une autre devise fasciste : Credere, obbedire, combattere. Croire, obéir, combattre. "
        "{rit.4}Et Leni Riefenstahl filme le congrès de Nuremberg de mille neuf cent trente-quatre, dans Le Triomphe de la volonté.",
        "{-rit}{-g4}{photo2}{disc}Le cours ajoute un détail. Les discours de Hitler duraient trois à quatre heures. Et ils tenaient la foule sous le charme. "
        "{disc.1}Le rituel est répété jusqu'à devenir ordinaire. Un salut. Un geste. Une phrase apprise par cœur.",
        "{-disc}{mot1}L'obéissance naît {!de l'émotion}de l'émotion. Pas du raisonnement.{-photo2}",
    ], vis={
        "g4": dict(type="globe", code="H2", sc=[24]),
        "rit": dict(type="liste", titre="Les rituels de l'obéissance", petit=True, bande=True, x=60, y=120, w=600,
                    marques=["DE", "IT", "IT", "DE"], items=[
            "« Heil Hitler » et le salut nazi : le salut officiel", "« Il Duce ha sempre ragione » : Mussolini a toujours raison",
            "« Credere, obbedire, combattere » : croire, obéir, combattre", "Congrès de Nuremberg, 1934 : Riefenstahl, Le Triomphe de la volonté"]),
        "photo2": dict(type="tableau", img="h2-nuremberg-1936", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="La « cathédrale de lumière » au-dessus du Zeppelinfeld, congrès de Nuremberg, septembre 1936 · Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE"),
        "disc": dict(type="note", terme="Un détail de plus", cles=["trois", "charme"],
                     t="Les discours de Hitler duraient trois à quatre heures et tenaient la foule sous le charme.",
                     etape="Répété jusqu'à devenir ordinaire : un salut, un geste, une phrase apprise par cœur", x=170, y=200, w=940),
        "mot1": dict(type="mot", t="L'émotion, pas le raisonnement", g="le rituel fait obéir la foule", y=260, taille=84),
    }),

    # ================================================================ II.1, idée 3 : médias et arts
    dict(id="medias", chap="II.1 · Médias et arts au service du régime", fond="nuit", humeur="tension",
         retenir="La propagande partout : cinéma, radio, peinture, sculpture. Le Volksempfänger (publicité de 1938). Paris 1937 : L'Ouvrier et la Kolkhozienne de Moukhina face au pavillon allemand. Goebbels, Hoffmann, Riefenstahl.",
         beats=[
        "{def2}Troisième idée. La propagande fonctionne parce qu'elle est {!partout}partout. Le cinéma, la radio, la peinture et la sculpture servent tous le régime. "
        "{def2.1}L'art n'est pas jugé sur sa qualité, mais sur son utilité. Il doit montrer la société idéale, comme si elle existait déjà.",
        "Les techniques nouvelles sont vendues bon marché, exprès, pour que la voix du chef entre dans chaque foyer. "
        "En mille neuf cent trente-huit, une publicité allemande pour le poste radio du peuple, le Volksempfänger, faisait cette promesse.",
        "{-def2}",
        ("C", "L'Allemagne écoute le Führer grâce au poste du peuple", "c_radio"),
        "{-c_radio}{paris}{paris.g}Les arts deviennent eux aussi un champ de bataille. Prends l'Exposition universelle de Paris, en mille neuf cent trente-sept. Au sommet du pavillon soviétique "
        "se dressait la statue de Vera Moukhina, L'Ouvrier et la Kolkhozienne. {paris.d}Et elle faisait face, directement, au pavillon allemand. "
        "Deux régimes. Deux sociétés idéales, dans la pierre et dans l'acier.",
        "{-paris}{equipe}En Allemagne, toute cette machine avait son équipe. {equipe.1}Joseph Goebbels, le spécialiste de la propagande. "
        "{equipe.2}Heinrich Hoffmann, le photographe personnel de Hitler. {equipe.3}Et Leni Riefenstahl, pour les films.",
    ], vis={
        "def2": dict(type="def", cles=["partout", "utilité"], terme="Notion clé · la propagande",
                     t="Une information contrôlée, faite pour façonner l'opinion plutôt que pour l'informer : cinéma, radio, peinture, sculpture.",
                     etape="Partout, l'art jugé sur son utilité : la société idéale montrée comme si elle existait déjà", x=170, y=190, w=940),
        "c_radio": dict(type="cit", a="Publicité pour le Volksempfänger", o="Allemagne, 1938 (traduction)", x=200, y=210, w=880),
        "paris": dict(type="cols", g="URSS", gq="L'Ouvrier et la Kolkhozienne de Moukhina sur le pavillon soviétique",
                      d="Allemagne", dq="le pavillon allemand, juste en face", vs="↔",
                      repere="Exposition universelle de Paris, 1937"),
        "equipe": dict(type="liste", titre="Allemagne nazie · la machine de propagande", items=[
            "Joseph Goebbels, le spécialiste de la propagande", "Heinrich Hoffmann, le photographe personnel de Hitler",
            "Leni Riefenstahl, les films (Le Triomphe de la volonté, 1934)"], x=170, y=170, w=940),
    }),

    # ================================================================ II.1, idée 4 : la censure
    dict(id="censure", chap="II.1 · La censure réécrit le passé", fond="nuit", humeur="mystere",
         retenir="La presse contrôlée, la critique punie, les archives corrigées. Iejov, chef du NKVD, à côté de Staline au canal Moscou-Volga ; exécuté en 1940, effacé de la photographie.",
         beats=[
        "{photo3}{def3}Quatrième idée. Le culte ne tient que si rien ne le contredit. Alors la presse est contrôlée, et la critique est punie. "
        "{-photo3}{def3.1}Dans le cas soviétique, on corrige même les archives. Le régime ne se contente pas d'interdire les opinions contraires. "
        "Il cherche à les rendre {!impensables}impensables, en effaçant toute preuve qu'elles aient jamais existé.",
        "{-def3}{photo}L'exemple est célèbre. Une photographie montre Staline au bord du canal Moscou-Volga. À côté de lui se tient Nikolaï Iejov, "
        "le chef du NKVD, la police politique. {photo.d}Iejov est exécuté en mille neuf cent quarante. "
        "Et sur la même image, retouchée, il a tout simplement disparu. Il ne reste que l'eau du canal.",
        "{-photo}{err}Attention ici. Une erreur fréquente consiste à écrire que Beria et Molotov ont été exécutés. "
        "{err.1}En réalité, Molotov ne l'a jamais été. Et Beria ne l'a été qu'en mille neuf cent cinquante-trois. Le chef de la police politique exécuté en mille neuf cent quarante, c'est Iejov, comme le dit le dossier documentaire sur la terreur.",
    ], vis={
        "photo3": dict(type="tableau", img="h2-book-burning", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.15, .5, .4],
                       legende="Des étudiants nazis brûlent des livres sur l'Opernplatz, Berlin, 10-11 mai 1933 (hors du cours) · Bundesarchiv, Bild 102-14597 / Georg Pahl, CC BY-SA 3.0 DE"),
        "def3": dict(type="def", cles=["presse", "archives", "impensables"], terme="Notion clé · la censure",
                     t="La suppression de tout ce qui contredit le régime : la presse contrôlée, la critique punie, les archives corrigées.",
                     etape="Pas seulement interdites : les opinions contraires rendues impensables", x=170, y=190, w=940),
        "photo": dict(type="cols", g="Avant", gq="Staline au canal Moscou-Volga, avec à côté de lui Iejov, chef du NKVD",
                      d="Après 1940", dq="Iejov exécuté… et effacé de la même photographie", vs="→",
                      repere="Les archives elles-mêmes sont corrigées"),
        "err": dict(type="note", terme="Attention · une erreur fréquente", cles=["Iejov", "1940"],
                    t="Chef du NKVD exécuté : Iejov, en 1940. Ni Molotov (jamais exécuté), ni Beria (exécuté en 1953).",
                    etape="Le dossier documentaire sur la terreur donne Iejov, exécuté en 1940", x=170, y=200, w=940),
    }),

    # ================================================================ II.1, idée 5 : le but
    dict(id="but", chap="II.1 · Le but : la nation, le parti, le chef ne font qu'un", fond="aube", humeur="tension",
         retenir="Nation = parti = chef : l'opposition devient trahison, la légitimité ne vient plus des élections. Symboles : le faisceau (PNF, 1921), la croix gammée (NSDAP, 1920), la faucille et le marteau (emblème soviétique, 1923).",
         beats=[
        "{eq}Cinquième idée : le but. Le culte de la personnalité n'est pas de la vanité. C'est {!une technique de gouvernement}une technique de gouvernement. "
        "{eq.1}Le régime identifie la nation au parti. {eq.2}Et il identifie le parti à un seul homme.",
        "{eq.3}Alors toute opposition ressemble à une trahison du pays lui-même. Et le chef n'a plus besoin d'élections.",
        "{-eq}Chaque régime a résumé cette idée dans un symbole, adopté à la fondation du parti, ou peu après. "
        "{sym}{sym.1}Le faisceau romain, pour le Parti fasciste, en mille neuf cent vingt et un. {sym.2}La croix gammée, pour le Parti nazi, en mille neuf cent vingt. "
        "{sym.3}Et la faucille et le marteau, sur l'emblème de l'État soviétique, en mille neuf cent vingt-trois.",
        "{-sym}{mot2}Retiens la formule du schéma. Critiquer le chef, c'est {!trahir le pays}trahir le pays.",
    ], vis={
        "eq": dict(type="liste", titre="Une technique de gouvernement", cles=["nation", "parti", "trahison"], marques=["1", "2", "→"], items=[
            "La nation = le parti", "Le parti = un seul homme",
            "L'opposition = une trahison du pays ; plus besoin d'élections"], x=170, y=160, w=940),
        "sym": dict(type="liste", titre="Un symbole pour chaque parti", marques=REG, items=[
            "Le faisceau romain : Parti national fasciste, 1921", "La croix gammée : NSDAP, 1920",
            "La faucille et le marteau : emblème de l'État soviétique, 1923"], x=170, y=170, w=940),
        "mot2": dict(type="mot", t="Chef = parti = nation", g="critiquer le chef, c'est trahir le pays", y=260, taille=86),
    }),

    # ================================================================ II.1, idée 6 : le petit père des peuples
    dict(id="langue", chap="II.1 · Le « petit père des peuples »", fond="nuit", humeur="tension",
         retenir="Staline, père protecteur de toutes les nations de l'URSS… qui impose une langue : le russe, obligatoire dans toutes les écoles à partir de mars 1938 (date hors du cours). Le géorgien n'a pas été interdit.",
         beats=[
        "{g5}{g5.1}Sixième idée. Le culte de Staline le présentait comme le père protecteur de toutes les nations de l'Union soviétique. "
        "Une union de nombreuses nations, de l'Ukraine à l'Asie centrale.",
        "{-g5}{fam}{fam.g}Mais derrière l'image, le père imposait {!une seule culture}une seule culture. Staline lui-même était géorgien. "
        "{fam.d}Pourtant, il fit du russe la langue de toute l'Union. Les Géorgiens furent poussés à parler russe, et à étudier même leurs propres textes "
        "en russe. Le culte d'un homme allait de pair avec l'unification forcée de tout un empire.",
        "{-fam}{dat}Voici l'exemple. À partir de mars mille neuf cent trente-huit, l'apprentissage du russe devient obligatoire dans toutes les écoles soviétiques, "
        "y compris dans les républiques nationales, comme la Géorgie. La date de ce décret vient de l'extérieur du cours. "
        "{dat.1}Et une correction. Certaines fiches de révision disent que Staline a interdit la langue géorgienne. C'est faux. "
        "Le géorgien est resté la langue officielle de la république de Géorgie. Ce qui a été imposé, c'est le russe, comme langue commune.",
    ], vis={
        "g5": dict(type="globe", code="H2", sc=[9]),
        "fam": dict(type="cols", g="L'image", gq="un père protecteur de toutes les nations de l'URSS",
                    d="La réalité", dq="une seule langue pour tous : le russe, même pour les Géorgiens", vs="≠",
                    repere="Staline, un Géorgien, impose le russe"),
        "dat": dict(type="note", terme="Attention · une correction", cles=["obligatoire", "interdit"],
                    t="Mars 1938 : le russe obligatoire dans toutes les écoles de l'URSS (date hors du cours).",
                    etape="Le géorgien n'a pas été interdit : il est resté la langue officielle de la RSS de Géorgie", x=170, y=200, w=940),
    }),

    # ================================================================ h2cult : trois chefs, trois cultes
    dict(id="h2cult", chap="Schéma · Trois chefs, trois cultes", fond="aube", humeur="calme",
         retenir="Même machine, trois contenus : Duce / Führer / petit père · « Il Duce ha sempre ragione » / « Heil Hitler » / « Merci, camarade Staline… » · faisceau / croix gammée / faucille et marteau · aviateur / Riefenstahl / photos retouchées.",
         beats=[
        "{c1}Passons au schéma du cours. Trois chefs, trois cultes, comparés ligne par ligne. "
        "{c1.1}D'abord, le nom. Il Duce. {c1.2}Der Führer. {c1.3}Le petit père des peuples.",
        "{-c1}{c2}{c2.1}Ensuite, la devise. Il Duce ha sempre ragione. {c2.2}Heil Hitler. "
        "{c2.3}Et en Union soviétique : Merci, camarade Staline, pour notre enfance heureuse.",
        "{-c2}{c3}{c3.1}Puis le symbole. Le faisceau. {c3.2}La croix gammée. {c3.3}La faucille et le marteau.",
        "{-c3}{c4}{c4.1}Et la mise en scène. Mussolini peint en aviateur, par Ambrosi, en mille neuf cent trente. "
        "{c4.2}Les congrès de Nuremberg, et le poste du peuple. "
        "{c4.3}Le réalisme socialiste, les photographies retouchées, et Stalingrad.",
        "{-c4}{bil}Alors, que conclut le schéma ? {!Les contenus diffèrent, le procédé est identique}Les contenus diffèrent. "
        "Le procédé est identique. Identifier la nation au parti. Et le parti à un seul homme.",
        ("P", 2.5),
    ], vis={
        "c1": dict(type="liste", titre="1 · Le nom du chef", marques=REG, items=[
            "« il Duce »", "« der Führer »", "« le petit père des peuples »"], x=170, y=150, w=940),
        "c2": dict(type="liste", titre="2 · Salut / devise", marques=REG, items=[
            "« Il Duce ha sempre ragione » (Mussolini a toujours raison)", "« Heil Hitler » avec le salut nazi, le salut officiel",
            "« Merci, camarade Staline, pour notre enfance heureuse »"], x=150, y=150, w=980),
        "c3": dict(type="liste", titre="3 · Le symbole du parti", marques=REG, items=[
            "Le faisceau romain", "La croix gammée", "La faucille et le marteau"], x=170, y=150, w=940),
        "c4": dict(type="liste", titre="4 · La mise en scène", marques=REG, items=[
            "Portrait en aviateur (Ambrosi, 1930) ; défilés du parti",
            "Congrès de Nuremberg filmés par Riefenstahl (1934) ; le poste du peuple (1938)",
            "Réalisme socialiste ; photographies retouchées ; Stalingrad (1925)"], x=150, y=150, w=980),
        "bil": dict(type="note", terme="Trois chefs, trois cultes · la même machine", cles=["identique", "nation", "seul"],
                    t="Les contenus diffèrent, le procédé est identique : identifier la nation au parti, et le parti à un seul homme.",
                    etape="Pour que critiquer le chef devienne trahir le pays", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 1 : produire un homme nouveau
    dict(id="nouveau", chap="II.2 · Pas des sujets obéissants : un homme nouveau", fond="nuit", humeur="lumiere",
         retenir="Une dictature exige qu'on se taise ; un régime totalitaire exige qu'on change. Trois modèles : le Volk, race purifiée (stérilisation, 1933) · le travailleur soviétique (Stakhanov, 1935) · le fasciste, fort et cultivé, au service du Parti.",
         beats=[
        "{cmp}Partie deux, point deux : le contrôle total de la société, et la fabrication d'un homme nouveau. Première idée. "
        "Qu'est-ce qui sépare un régime totalitaire d'une dictature ordinaire ? "
        "Une dictature exige que tu {!te taises}te taises. {cmp.d}Un régime totalitaire exige que tu {!changes}changes.",
        "{-cmp}{def4}L'idéologie définit un modèle d'humanité. Et toute la machine de l'État est tournée vers sa fabrication : l'école, les loisirs, le travail, la famille, la loi. "
        "{def4.1}La vie privée n'a plus aucun espace protégé.",
        "{-def4}{mod}Et chaque régime avait son propre modèle. {mod.1}En Italie, un homme fort et cultivé, au service du Parti. "
        "{mod.2}En Allemagne, l'homme nouveau, c'était une race purifiée, le Volk. D'où la loi de stérilisation de mille neuf cent trente-trois. "
        "{mod.3}En Union soviétique, c'était un travailleur, célébré à partir de mille neuf cent trente-cinq à travers le mineur Stakhanov.",
    ], vis={
        "cmp": dict(type="cols", g="Dictature", gq="exige qu'on se taise", d="Totalitarisme", dq="exige qu'on change",
                    vs="≠", repere="L'homme nouveau : l'être humain refait par l'idéologie"),
        "def4": dict(type="def", cles=["modèle", "machine", "vie privée"], terme="Notion clé · l'« homme nouveau »",
                     t="Le modèle d'être humain que chaque idéologie prétend produire ; toute la machine de l'État est tournée vers lui.",
                     etape="École, loisirs, travail, famille, loi : la vie privée n'a plus d'espace protégé", x=170, y=190, w=940),
        "mod": dict(type="liste", titre="Trois modèles d'homme nouveau", marques=REG, items=[
            "Fort et cultivé, au service du Parti",
            "Une race purifiée, le Volk → la loi de stérilisation (1933)",
            "Un travailleur → célébré à travers Stakhanov (1935)"], x=150, y=160, w=980),
    }),

    # ================================================================ II.2, idée 2 : la jeunesse
    dict(id="jeunesse", chap="II.2 · La jeunesse d'abord", fond="guerre", humeur="tension",
         retenir="Balilla (1926) · Jeunesses hitlériennes, loi de 1936, ≈ 8 millions en 1939 · Komsomol (1918). Mussolini : « Je prends les hommes au berceau… ». Hitler, 1938 : dix ans → Jungvolk → Jeunesses hitlériennes → Service du travail → Wehrmacht.",
         beats=[
        "{g6}{g6.1}Deuxième idée. La jeunesse d'abord. Pourquoi ? Parce qu'on peut façonner les enfants {!avant qu'ils sachent juger}avant qu'ils sachent juger. "
        "Les trois régimes ont créé des organisations de jeunesse, qui prenaient en charge le temps hors de l'école : "
        "uniformes, camps, sport, chants, et formation politique.",
        "{org}{org.1}L'Italie crée l'Opera Nazionale Balilla, en mille neuf cent vingt-six. {org.2}L'Allemagne rend les Jeunesses hitlériennes obligatoires par une loi de mille neuf cent trente-six. "
        "En mille neuf cent trente-neuf, elles comptent environ huit millions de membres. {org.3}L'Union soviétique a le Komsomol, créé en mille neuf cent dix-huit. "
        "{org.4}Le but : façonner directement la génération suivante, en contournant la famille et l'Église.",
        "{-org}{-g6}{nuance}Une précision, hors du cours. La loi de mille neuf cent trente-six fait des Jeunesses hitlériennes la jeunesse officielle de l'État. "
        "Mais l'adhésion ne devient vraiment obligatoire qu'en mille neuf cent trente-neuf. {nuance.1}Mussolini a résumé l'ambition.",
        "{-nuance}",
        ("C", "Je prends les hommes au berceau, et je ne les rends au pape qu'après leur mort.", "c_muss"),
        "{-c_muss}Et Hitler a décrit la chaîne lui-même, dans un discours de mille neuf cent trente-huit. C'est le document deux du dossier documentaire sur la jeunesse. "
        "{chaine}{chaine.1}Les enfants entrent à dix ans. {chaine.2}Quatre ans dans le Jungvolk. {chaine.3}Quatre ans dans les Jeunesses hitlériennes. "
        "{chaine.4}Puis le Service du travail. {chaine.5}Et ce qui reste encore de conscience de classe ou d'orgueil de rang, "
        "la Wehrmacht s'en chargera. Dès l'âge de dix ans, le régime ne lâche plus personne.",
    ], vis={
        "g6": dict(type="globe", code="H2", sc=[11]),
        "org": dict(type="liste", titre="Les organisations de jeunesse", petit=True, bande=True, x=40, y=120, w=480,
                    marques=REG + ["→"], items=[
            "Opera Nazionale Balilla, 1926", "Jeunesses hitlériennes : loi de 1936, ≈ 8 millions de membres en 1939",
            "Komsomol, 1918", "En contournant la famille et l'Église"]),
        "nuance": dict(type="note", terme="Une précision · hors du cours", cles=["officielle", "1939"],
                       t="La loi de 1936 fait des Jeunesses hitlériennes la jeunesse officielle de l'État ; l'adhésion devient vraiment obligatoire en 1939.",
                       etape="Le cours écrit « obligatoires par la loi de 1936 » : les deux dates peuvent être citées", x=170, y=200, w=940),
        "c_muss": dict(type="cit", a="Benito Mussolini", o="cité dans le cours (traduction)", x=200, y=200, w=880),
        "chaine": dict(type="liste", titre="Hitler, 1938 · la chaîne (dossier documentaire, document 2)", items=[
            "10 ans : les enfants entrent", "4 ans dans le Jungvolk", "4 ans dans les Jeunesses hitlériennes", "Puis le Service du travail",
            "« La Wehrmacht s'en chargera » : de ce qui reste"], x=170, y=120, w=940),
    }),

    # ================================================================ II.2, idée 3 : l'école
    dict(id="ecole", chap="II.2 · L'école : l'idéologie enseignée comme une science", fond="nuit", humeur="tension",
         retenir="L'éducation réécrite : manuels, livres pour enfants, leçons portent l'idéologie. Allemagne : enseignement racial obligatoire dès septembre 1933 ; Der Giftpilz (Nuremberg, 1938). L'enfant apprend à voir l'ennemi avant d'en avoir rencontré un.",
         beats=[
        "{g7}{g7.1}Troisième idée. La pensée, la culture et l'information sont contrôlées. Et l'école enseigne l'idéologie {!comme une science}comme une science. "
        "L'éducation n'est pas seulement censurée. Elle est réécrite.",
        "{-g7}{eco1}{eco1.1}Les manuels, les livres pour enfants et les leçons portent tous l'idéologie, sous une forme adaptée aux plus jeunes. "
        "{eco1.2}En Allemagne, la doctrine raciale était enseignée comme une science naturelle. Avec des tableaux, des mesures, et des classifications. "
        "{eco1.3}L'enseignement racial devient obligatoire dans les écoles allemandes en septembre mille neuf cent trente-trois.",
        "{eco1.4}L'exemple du cours est un livre antisémite pour enfants : Der Giftpilz, Le Champignon vénéneux, publié à Nuremberg en mille neuf cent trente-huit. "
        "Il apprenait aux enfants à reconnaître les Juifs à des traits physiques inventés. {-eco1}{mot3}Ainsi, un enfant apprend {!à voir l'ennemi}à voir l'ennemi, "
        "avant même d'en avoir rencontré un.",
    ], vis={
        "g7": dict(type="globe", code="H2", sc=[23]),
        "eco1": dict(type="liste", titre="L'école de l'idéologie", cles=["enfants", "science", "obligatoire"], items=[
            "Manuels, livres pour enfants et leçons portent l'idéologie", "La doctrine raciale enseignée comme une science naturelle : tableaux, mesures",
            "Enseignement racial obligatoire dans les écoles allemandes, septembre 1933",
            "Der Giftpilz, « Le Champignon vénéneux » (Nuremberg, 1938)"], x=150, y=130, w=980),
        "mot3": dict(type="mot", t="L'ennemi, enseigné", g="vu avant même d'être rencontré", y=260, taille=96),
    }),

    # ================================================================ II.2, idée 4 : la loi
    dict(id="loi", chap="II.2 · La loi trie les êtres humains", fond="guerre", humeur="tension",
         retenir="Lois de Nuremberg, 15 sept. 1935 : ni mariage ni relations entre Juifs et « personnes de sang allemand » ; citoyenneté selon l'ascendance. Sang allemand · Mischling 2e degré (1/4) · 1er degré (1/2) · Juif (≥ 3/4) : citoyenneté refusée.",
         beats=[
        "{def5}Quatrième idée. Dans l'Allemagne nazie, l'idéologie devient {!la loi}la loi. Prends les lois de Nuremberg, du quinze septembre mille neuf cent trente-cinq. "
        "Elles interdisent le mariage et les relations sexuelles entre Juifs et ce qu'elles appellent les personnes de sang allemand. "
        "{def5.1}Elles interdisent aux foyers juifs d'employer de jeunes Allemandes. Et elles interdisent aux Juifs d'arborer le drapeau du Reich.",
        "L'État définit donc la citoyenneté selon l'ascendance. Et l'administration dresse les tableaux pour l'appliquer. "
        "{-def5}Un tableau officiel de mille neuf cent trente-cinq classe les personnes par fractions d'ascendance. {tab}{tab.1}Sang allemand. "
        "{tab.2}Mischling du second degré : un quart juif, c'est-à-dire un grand-parent juif. "
        "{tab.3}Mischling du premier degré : à moitié juif, deux grands-parents juifs. "
        "{tab.4}Et Juif : trois quarts ou plus. Les personnes de cette dernière catégorie se voient refuser toute citoyenneté du Reich.",
        "{-tab}{lien}À l'école, l'enfant apprend les catégories. Dans la loi, l'État les applique. "
        "{lien.1}Un être humain est défini par son ascendance.",
    ], vis={
        "def5": dict(type="def", cles=["mariage", "ascendance"], terme="Notion clé · les lois de Nuremberg (15 septembre 1935)",
                     t="Ni mariage ni relations sexuelles entre Juifs et « personnes de sang allemand » : la citoyenneté définie par l'ascendance.",
                     etape="Aussi : pas de jeunes Allemandes employées par des foyers juifs ; interdiction pour les Juifs d'arborer le drapeau du Reich", x=170, y=190, w=940),
        "tab": dict(type="liste", titre="Un tableau officiel de 1935", marques=["0", "¼", "½", "¾"], items=[
            "Sang allemand", "Mischling du 2e degré : un grand-parent juif", "Mischling du 1er degré : deux grands-parents juifs",
            "« Juif » : trois ou quatre grands-parents juifs → citoyenneté du Reich refusée"], x=150, y=140, w=980),
        "lien": dict(type="note", terme="Pour ta copie", cles=["école", "loi", "ascendance"],
                     t="À l'école, l'enfant apprend les catégories ; dans la loi, l'État les applique.",
                     etape="Un être humain défini par son ascendance, et non par ce qu'il fait", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 5 : travail, loisirs, économie
    dict(id="travail", chap="II.2 · Le travail, les loisirs et l'économie absorbés", fond="nuit", humeur="lumiere",
         retenir="Syndicats dissous, loisirs organisés par l'État, économie dirigée (URSS : plans quinquennaux, collectivisation ; Allemagne : réarmement, autarcie). Stakhanov, 1935 : 14 fois sa norme en une équipe → le stakhanovisme.",
         beats=[
        "{abs}Cinquième idée. Le travail, les loisirs et l'économie sont absorbés eux aussi. Pour que {!rien n'échappe au régime}rien n'échappe au régime. "
        "{abs.1}Les syndicats indépendants sont dissous. {abs.2}L'État crée ses propres organisations de loisirs. "
        "{abs.3}L'économie est orientée vers les buts du régime. En Union soviétique, la collectivisation et les plans quinquennaux. En Allemagne, le réarmement et l'autarcie. "
        "{abs.4}Même les clubs sportifs et les œuvres de charité sont absorbés, ou supprimés.",
        "{-abs}{g8}{g8.1}L'exemple : l'homme nouveau soviétique avait son héros. En mille neuf cent trente-cinq, dans le Donbass, le régime présente le mineur Alexeï Stakhanov "
        "comme ayant extrait quatorze fois sa norme de charbon, en une seule équipe.",
        "{-g8}{gs}Regarde l'échelle. {gs.1}{gs.2}Voici la norme pour une équipe. {gs.3}{gs.4}Et voici le record annoncé par le régime. Quatorze fois plus.",
        "{-gs}{photo4}{stak}Son nom devient un mot : {!le stakhanovisme}le stakhanovisme, le culte du travailleur qui bat les records. "
        "{stak.1}Des concours sont imposés dans toutes les usines. "
        "Un détail, hors du cours : le record avait été préparé à l'avance, avec d'autres mineurs qui l'aidaient.{-photo4}",
    ], vis={
        "abs": dict(type="liste", titre="Rien en dehors du régime", cles=["syndicats", "loisirs", "économie", "absorbée"], items=[
            "Les syndicats indépendants dissous", "Des organisations de loisirs créées par l'État",
            "L'économie dirigée : plans quinquennaux, collectivisation · réarmement, autarcie",
            "La société civile absorbée ou supprimée : plus rien entre l'individu et le parti"], x=150, y=130, w=980),
        "g8": dict(type="globe", code="H2", sc=[26]),
        "gs": dict(type="graphe", titre="Le record de Stakhanov, 1935 (tel que le régime le présente)", x=340, y=110, w=600, h=520,
                   ax=dict(x=[0.35, 2.65], y=[0, 16], gx=[], gy=[], lx="", ly=""),
                   el=[dict(type="texte", x=1.0, y=-1.1, t="La norme", c="iv"),
                       dict(type="droite", pts=[[1.0, 0.68], [1.0, 0.75]], c="el", ep=34, dur=0.6, lbl="× 1", lp=[1.0, 2.0]),
                       dict(type="texte", x=2.0, y=-1.1, t="L'équipe de Stakhanov", c="iv"),
                       dict(type="droite", pts=[[2.0, 0.68], [2.0, 13.3]], c="ca", ep=34, dur=1.4, lbl="× 14", lp=[2.0, 15.0])]),
        "photo4": dict(type="tableau", img="h2-stakhanov", fond=True, sombre=True, de=[1.0, .5, .45], a=[1.15, .5, .4],
                       legende="Alexeï Stakhanov (au centre) explique sa méthode à un autre mineur, URSS, années 1930 · Eleazar Langman, domaine public"),
        "stak": dict(type="def", cles=["record", "usines"], terme="Notion clé · le stakhanovisme",
                     t="Le culte soviétique du travailleur qui bat les records, du nom du mineur Stakhanov (1935).",
                     etape="Des concours imposés dans toutes les usines · un record préparé à l'avance (hors du cours)", x=170, y=200, w=940),
    }),

    # ================================================================ II.2, idée 6 : trois hommes nouveaux
    dict(id="trois", chap="II.2 · Trois hommes nouveaux pour trois buts suprêmes", fond="aube", humeur="calme",
         retenir="Même méthode (enfants pris tôt, uniformes, camps, idéologie), idéaux différents : la race (fort, obéissant, « aryen ») · la classe (un travailleur instruit, qui a étudié Marx et Lénine) · la nation (prêt à combattre, héritier de Rome).",
         beats=[
        "{nuage}Sixième idée. Trois hommes nouveaux, pour trois buts suprêmes. Le dossier documentaire sur la jeunesse compare les trois organisations. "
        "La méthode est la même. {nuage.1}Prendre les enfants tôt. {nuage.2}Des uniformes. {nuage.3}Des camps. {nuage.4}L'idéologie. Mais l'idéal diffère.",
        "{-nuage}{buts}{buts.1}Les nazis voulaient des enfants forts, obéissants, instruits et aryens, au service du Volk. "
        "Le fondement, c'est {!le darwinisme social}le darwinisme social : les races les plus fortes survivent. Le but, c'est donc {!la race}la race. "
        "{buts.2}L'homme nouveau soviétique était un travailleur instruit, qui avait étudié Marx et Lénine. Le but, c'est {!la classe}la classe. "
        "{buts.3}L'homme nouveau fasciste était prêt à combattre. Calme, de sang-froid, nourri de latin et de Plutarque, en héritier de Rome. "
        "Le but, c'est {!la nation}la nation.",
        "{-buts}{src}Voici les documents du dossier. {src.1}Une affiche des Jeunesses hitlériennes, de mille neuf cent trente-cinq : La jeunesse sert le Führer ! "
        "Tous les enfants de dix ans dans les Jeunesses hitlériennes. {src.2}Le programme du Komsomol de Smolensk, en mille neuf cent dix-neuf. Son but : faire des jeunes "
        "ouvriers et paysans des révolutionnaires. "
        "{src.3}Et une photographie de l'Opera Nazionale Balilla, de mille neuf cent trente-six. Des garçons en uniforme noir, le fusil à l'épaule.",
    ], vis={
        "nuage": dict(type="nuage", centre="La même méthode", items=["les enfants pris tôt", "des uniformes", "des camps", "l'idéologie"]),
        "buts": dict(type="liste", titre="Trois buts suprêmes", marques=["DE", "SU", "IT"], cles=["race", "classe", "nation"], items=[
            "La race : des enfants forts, obéissants, « aryens », pour le Volk (darwinisme social)",
            "La classe : un travailleur instruit, qui a étudié Marx et Lénine",
            "La nation : prêt à combattre, de sang-froid, latin et Plutarque, héritier de Rome"], x=150, y=150, w=980),
        "src": dict(type="liste", titre="Le dossier documentaire · les documents", marques=["DE", "SU", "IT"], items=[
            "Affiche des Jeunesses hitlériennes, 1935 : « La jeunesse sert le Führer ! Tous les enfants de dix ans dans les Jeunesses hitlériennes »",
            "Programme du Komsomol de Smolensk, 1919 : faire des jeunes ouvriers et paysans des « révolutionnaires »",
            "Opera Nazionale Balilla, photographie, 1936 : des garçons en uniforme noir, le fusil à l'épaule"], x=150, y=140, w=980),
    }),

    # ================================================================ h2newman : le modèle et les moyens
    dict(id="h2newman", chap="Schéma · Fabriquer un « homme nouveau »", fond="aube", humeur="calme",
         retenir="Modèle : Parti / Volk, eugénisme / travailleur, stakhanovisme · Jeunesse : Balilla / Hitlerjugend / Komsomol · École : race dès 1938 / race dès 1933 / réalisme socialiste · Économie : corporatisme / plan de quatre ans / plans quinquennaux.",
         beats=[
        "{n1}Le second schéma montre comment fabriquer un homme nouveau : le modèle, et les moyens. Là encore, ligne par ligne. "
        "{n1.1}D'abord, le modèle. Un serviteur du Parti. {n1.2}Une race purifiée, et l'eugénisme. {n1.3}Un travailleur, et le stakhanovisme.",
        "{-n1}{n2}{n2.1}Ensuite, la jeunesse. Les Balilla, puis la jeunesse fasciste, jusqu'à dix-huit ans. "
        "{n2.2}Les Jeunesses hitlériennes, de dix à dix-huit ans. {n2.3}Le Komsomol, jusque dans les villages.",
        "{-n2}{n3}{n3.1}Puis l'école et la culture. En Italie, la presse d'opposition est supprimée. Et à partir de mille neuf cent trente-huit, on enseigne la race. "
        "{n3.2}En Allemagne, l'enseignement racial dès mille neuf cent trente-trois. {n3.3}Et en Union soviétique, le réalisme socialiste est imposé aux arts.",
        "{-n3}{n4}{n4.1}Et enfin, l'économie. En Italie, le corporatisme, et l'autarcie après mille neuf cent trente-cinq. "
        "{n4.2}En Allemagne, le réarmement, et le plan de quatre ans de mille neuf cent trente-six. "
        "{n4.3}En Union soviétique, les plans quinquennaux, la collectivisation, les kolkhozes.",
        "{-n4}{bil2}Et le schéma conclut : {!une dictature exige le silence, le totalitarisme exige la transformation}"
        "une dictature exige le silence. Le totalitarisme exige la transformation.",
        ("P", 2.5),
    ], vis={
        "n1": dict(type="liste", titre="1 · Le modèle de l'homme nouveau", marques=REG, items=[
            "Fort et cultivé, au service du Parti", "Une race purifiée, le Volk → l'eugénisme", "Un travailleur → le stakhanovisme"],
            x=170, y=150, w=940),
        "n2": dict(type="liste", titre="2 · La jeunesse encadrée", marques=REG, items=[
            "Balilla, puis jeunesse fasciste jusqu'à 18 ans", "Jeunesses hitlériennes, obligatoires de 10 à 18 ans",
            "Komsomol, formation politique jusque dans les villages"], x=170, y=150, w=940),
        "n3": dict(type="liste", titre="3 · L'école et la culture", marques=REG, items=[
            "Presse d'opposition supprimée ; à partir de 1938, enseignement de la « race »",
            "Enseignement racial obligatoire dès sept. 1933 ; Der Giftpilz (1938)", "Réalisme socialiste imposé aux arts"],
            x=150, y=150, w=980),
        "n4": dict(type="liste", titre="4 · L'économie", marques=REG, items=[
            "Corporatisme, autarcie après 1935", "Réarmement, autarcie, plan de quatre ans (1936)",
            "Plans quinquennaux dès 1928, collectivisation, kolkhozes"], x=170, y=150, w=940),
        "bil2": dict(type="note", terme="Fabriquer un « homme nouveau » · la conclusion", cles=["silence", "transformation"],
                     t="Une dictature exige le silence ; le totalitarisme exige la transformation.",
                     etape="Mussolini : « Je prends les hommes au berceau… »", x=170, y=200, w=940),
    }),

    # ================================================================ à toi : un paragraphe de réponse à une question problématisée
    dict(id="essai", chap="À toi · un paragraphe de question problématisée", fond="aube", humeur="calme",
         retenir="Idée directrice (un seul but, un homme nouveau) · la jeunesse (Balilla, Jeunesses hitlériennes, Komsomol) · l'école et la loi (1933, Nuremberg) · le travail (Stakhanov) · conclusion : la transformation, pas seulement l'obéissance.",
         beats=[
        "{ex1}À toi. Voici une question problématisée, écrite pour cette vidéo : "
        "comment les régimes totalitaires ont-ils cherché à créer {!un homme nouveau}un homme nouveau ?",
        "{-ex1}{met}La méthode. {met.1}Commence par une phrase qui répond à la question : ton idée directrice. "
        "{met.2}Puis donne plusieurs moyens, chacun avec un exemple précis. {met.3}Et termine par une phrase qui revient à la question.",
        "{-met}{pa1}",
        ("P", 2.0),
        "{-pa1}{mod1}Voici un paragraphe modèle. "
        "{mod1.1}Les régimes totalitaires ne voulaient pas de sujets obéissants. Ils ont cherché à fabriquer un homme nouveau, façonné par leur idéologie. "
        "{mod1.2}D'abord, ils se sont emparés de la jeunesse avant qu'elle sache juger. Pense aux Balilla en mille neuf cent vingt-six, au Komsomol, "
        "et aux Jeunesses hitlériennes, avec environ huit millions de membres en mille neuf cent trente-neuf. "
        "{mod1.3}Ensuite, ils ont réécrit l'éducation et la loi. L'enseignement racial entre dans les écoles allemandes en septembre mille neuf cent trente-trois. "
        "Les lois de Nuremberg suivent, en mille neuf cent trente-cinq. "
        "{mod1.4}Enfin, ils ont absorbé le travail. En mille neuf cent trente-cinq, le mineur Stakhanov devient le modèle du travailleur soviétique. "
        "{mod1.5}Les idéaux diffèrent : la race, la classe ou la nation. Mais le but est le même : une transformation totale, et pas seulement l'obéissance.",
    ], vis={
        "ex1": dict(type="exo", niveau="essay", titre="Comment les régimes totalitaires ont-ils cherché à créer un « homme nouveau » ?",
                    src="Question écrite pour cette vidéo, sur la partie II.2", enonce=["Un paragraphe : idée directrice, moyens et exemples, phrase de conclusion"]),
        "met": dict(type="liste", titre="Un paragraphe argumenté", cles=["répond", "exemple", "revient"], items=[
            "Une phrase qui répond à la question : l'idée directrice", "Plusieurs moyens, chacun avec un exemple précis tiré des trois régimes",
            "Une phrase finale qui revient à la question"], x=150, y=150, w=980),
        "pa1": dict(type="pause", t="Rédige le paragraphe : une idée directrice, trois moyens avec exemples, une phrase de conclusion.",
                    sous="Mets la vidéo en pause, rédige sur une feuille, puis relance pour voir un modèle."),
        "mod1": dict(type="liste", titre="Un paragraphe modèle", petit=True, items=[
            "Pas des sujets obéissants : un homme nouveau façonné par l'idéologie",
            "La jeunesse : Balilla (1926), Komsomol, Jeunesses hitlériennes (≈ 8 millions en 1939) ; la chaîne de Hitler, 1938",
            "L'école et la loi : enseignement racial (sept. 1933) ; lois de Nuremberg (1935)",
            "Le travail : Stakhanov, modèle du travailleur soviétique (1935)",
            "Race, classe ou nation : le même but, la transformation"], x=130, y=110, w=1020),
    }),

    # ================================================================ à toi : une analyse de document
    dict(id="dbq", chap="À toi · une analyse de document", fond="guerre", humeur="tension",
         retenir="Analyse de document : présenter (nature, auteur, date) · contexte · intérêt (le dictateur lui-même, toute la chaîne, l'intention) · limites (un discours, pas la réalité ; un seul régime ; pas la voix des jeunes) · bilan critique.",
         beats=[
        "{ex2}Maintenant, une analyse de document, sur le document deux du dossier : le discours de Hitler de mille neuf cent trente-huit, qui décrit le parcours "
        "de la jeunesse allemande. La consigne : montrez ce que ce discours {!nous apprend}nous apprend sur l'encadrement des jeunes par le régime nazi, puis portez un regard critique sur ce document.",
        "{-ex2}{str}Rappelle-toi la démarche. {str.1}D'abord, présenter le document : sa nature, son auteur, sa date. "
        "{str.2}Puis le situer dans son contexte. {str.3}Ensuite, l'expliquer et montrer son intérêt. {str.4}Enfin, ses limites, et un bilan critique.",
        "{-str}{pa2}",
        ("P", 2.0),
        "{-pa2}{rep}Voici un modèle. {rep.1}Ce document est un discours prononcé par Hitler lui-même en mille neuf cent trente-huit. Il décrit le parcours d'un enfant allemand, "
        "de l'âge de dix ans jusqu'à l'armée. "
        "{rep.2}Le régime nazi est alors au pouvoir depuis cinq ans, et la loi de mille neuf cent trente-six a fait des Jeunesses hitlériennes la jeunesse officielle de l'État.",
        "{rep.3}Son intérêt. D'abord, il vient du dictateur lui-même : il montre l'intention du régime, au plus haut niveau. "
        "Ensuite, il décrit toute la chaîne, du Jungvolk à la Wehrmacht. "
        "Et ses derniers mots montrent le but : effacer toute autre fidélité, de classe ou de rang.",
        "{rep.4}Ses limites. C'est un discours : il montre ce que voulait le régime, pas ce que les jeunes ont réellement vécu. "
        "Il ne donne aucun chiffre ; il faut le cours pour cela : huit millions de membres en mille neuf cent trente-neuf. Il ne concerne que l'Allemagne. "
        "Et on n'y entend ni les familles, ni les jeunes. Bilan critique : très utile pour comprendre les buts, beaucoup moins pour la réalité.",
    ], vis={
        "ex2": dict(type="exo", niveau="dbq", titre="Montrez ce que le discours de Hitler de 1938 nous apprend sur l'encadrement des jeunes par le régime nazi, puis portez un regard critique sur ce document.",
                    src="Consigne écrite pour cette vidéo, sur le dossier documentaire (document 2, tel que le cours le résume)", enonce=["Analyse de document"],
                    donnees=["Hitler, 1938 : les enfants entrent à dix ans · 4 ans dans le Jungvolk · 4 ans dans les Jeunesses hitlériennes · le Service du travail · « la Wehrmacht s'en chargera » : de ce qui reste"]),
        "str": dict(type="liste", titre="L'analyse de document : la démarche", cles=["présenter", "situer", "intérêt", "limites"], items=[
            "Présenter le document : nature, auteur, date", "Le situer dans son contexte",
            "L'expliquer et montrer son intérêt : plusieurs arguments", "Ses limites : plusieurs arguments, puis un bilan critique"], x=150, y=130, w=980),
        "pa2": dict(type="pause", t="Présente et situe le document, puis rédige son intérêt et ses limites.",
                    sous="Mets la vidéo en pause, rédige ta réponse, puis relance pour voir un modèle."),
        "rep": dict(type="liste", titre="Un modèle de réponse", items=[
            "Présentation : un discours de Hitler lui-même, 1938 : le parcours d'un enfant allemand de dix ans jusqu'à l'armée",
            "Contexte : le régime au pouvoir depuis 1933 ; la loi de 1936 sur les Jeunesses hitlériennes",
            "Intérêt : l'intention du dictateur · toute la chaîne · effacer toute autre fidélité",
            "Limites : les buts, pas la réalité · pas de chiffres (8 millions) · l'Allemagne seule · pas la voix des jeunes · bilan : très utile pour les buts"], x=150, y=130, w=980),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Récapitulatif", fond="nuit", humeur="calme", beats=[
        "{carte}Résumons. {carte.1}Le chef est un Guide : il Duce, der Führer, le petit père des peuples. Des villes sont rebaptisées, "
        "Leningrad et Stalingrad. {carte.2}Le culte a ses moyens : les rassemblements et les rituels, les médias et les arts, et une censure qui réécrit le passé. "
        "Pense à Iejov, effacé. {carte.3}Le but : le chef, le parti et la nation ne font qu'un, pour que l'opposition devienne trahison. "
        "{carte.4}Et l'homme nouveau. La jeunesse prise à dix ans. L'école et la loi, avec les lois de Nuremberg de mille neuf cent trente-cinq. Le travail, et Stakhanov. La race, la classe, la nation.",
        ("P", 4.0),
        "{-carte}{fin}Prochain épisode : la terreur de masse. La police politique. Les procès spectacles. Les camps. Et la terreur qui dévore les siens.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="CHEF · PARTI · HOMME NOUVEAU", branches=[
            dict(t="Le Guide", items=["Duce · Führer · petit père", "Leningrad 1924 · Stalingrad 1925", "Le Porte-drapeau"]),
            dict(t="Les moyens du culte", items=["rassemblements · « Heil Hitler »", "radio · Riefenstahl · Paris 1937", "Iejov effacé (1940)"]),
            dict(t="Le but", items=["nation = parti = chef", "opposition = trahison", "faisceau · croix gammée · faucille et marteau"]),
            dict(t="L'homme nouveau", items=["Balilla · Jeunesses hitlériennes · Komsomol", "sept. 1933 · lois de Nuremberg 1935", "Stakhanov · race, classe, nation"])]),
        "fin": dict(type="mot", t="Ensuite : la terreur de masse", g="Épisode 5 · police, procès spectacles, camps", y=270, taille=74),
    }),
]

QUIZ = [
    dict(q="D'après le cours, que fait la propagande totalitaire du chef ?",
         r=["Un être supérieur, le Guide, l'incarnation de la nation", "Un chef de gouvernement qu'on peut remplacer aux prochaines élections",
            "Un monarque constitutionnel", "Un porte-parole du parlement"], ok=0, voir="def1",
         ex="Il est présenté à la fois comme soldat, travailleur, père et visionnaire."),
    dict(q="Quelle ville est rebaptisée du nom du chef soviétique en 1925 ?",
         r=["Stalingrad", "Leningrad", "Petrograd", "Smolensk"], ok=0, voir="noms",
         ex="Petrograd était devenue Leningrad en 1924, après la mort de Lénine."),
    dict(q="Que signifie la devise fasciste « Il Duce ha sempre ragione » ?",
         r=["Mussolini a toujours raison", "Croire, obéir, combattre", "Tout est dans l'État", "La jeunesse sert le chef"], ok=0, voir="rit",
         ex="« Credere, obbedire, combattere » signifie croire, obéir, combattre."),
    dict(q="Qu'arrive-t-il à Iejov, chef du NKVD, après son exécution en 1940 ?",
         r=["Il est effacé d'une photographie prise à côté de Staline", "Il est remplacé par Molotov", "Il devient un héros du travail soviétique",
            "Son nom est donné à une ville"], ok=0, voir="photo",
         ex="Molotov n'a jamais été exécuté ; Beria ne l'a été qu'en 1953."),
    dict(q="Quel symbole le NSDAP adopte-t-il en 1920 ?",
         r=["La croix gammée", "Le faisceau romain", "La faucille et le marteau", "La chemise noire"], ok=0, voir="sym",
         ex="Le faisceau : Parti fasciste (1921) ; la faucille et le marteau : emblème soviétique (1923)."),
    dict(q="D'après le cours, qu'est-ce qui sépare un régime totalitaire d'une dictature ordinaire ?",
         r=["Il exige qu'on change, pas seulement qu'on se taise", "Il a un parti unique", "Il a une police politique",
            "Il n'organise pas d'élections"], ok=0, voir="cmp",
         ex="Le but est un homme nouveau : la vie privée n'a plus d'espace protégé."),
    dict(q="Quelle organisation de jeunesse est fondée en Italie en 1926 ?",
         r=["L'Opera Nazionale Balilla", "Le Komsomol", "Les Jeunesses hitlériennes", "Le Jungvolk"], ok=0, voir="org",
         ex="Le Komsomol date de 1918 ; la loi sur les Jeunesses hitlériennes, de 1936."),
    dict(q="Que font les lois de Nuremberg du 15 septembre 1935 ?",
         r=["Elles définissent la citoyenneté par l'ascendance et interdisent le mariage entre Juifs et « personnes de sang allemand »",
            "Elles rendent l'enseignement racial obligatoire à l'école", "Elles créent les Jeunesses hitlériennes", "Elles lancent le plan de quatre ans"], ok=0, voir="def5",
         ex="L'enseignement racial devient obligatoire en septembre 1933."),
    dict(q="Qu'aurait fait Stakhanov en 1935, selon le régime ?",
         r=["Extraire quatorze fois sa norme de charbon en une seule équipe", "Construire le canal de la mer Blanche", "Fonder le Komsomol",
            "Peindre le pavillon soviétique de 1937"], ok=0, voir="gs",
         ex="Son nom a donné le stakhanovisme, le culte du travailleur qui bat les records."),
]

CREDITS = [
    "Contenu : le cours d'histoire de Terminale, chapitre 2 « Les régimes totalitaires », parties II.1 et II.2, avec le dossier documentaire sur la jeunesse et les schémas « Trois chefs, trois cultes » et « Fabriquer un homme nouveau », tel qu'il est rédigé sur le site ; corrections d'erreurs fréquentes tirées des vérifications du site ; hors du cours, et dit comme tel : la date du décret de 1938 sur le russe, la préparation du record de Stakhanov, les Jeunesses hitlériennes rendues vraiment obligatoires en 1939 ; questions et modèles de réponse écrits pour cette vidéo ; carte animée du chapitre 2 (site).",
    "Citations en traduction française : Benito Mussolini, cité dans le cours ; publicité pour le Volksempfänger (Allemagne, 1938).",
    "Photographies (via Wikimedia Commons) : Joseph Staline, Moscou, 1937 (photographe inconnu, domaine public) ; le congrès de Nuremberg de septembre 1936 (Bundesarchiv, Bild 183-1982-1130-502, CC BY-SA 3.0 DE) ; l'autodafé de l'Opernplatz, Berlin, mai 1933 (Georg Pahl, Bundesarchiv, Bild 102-14597, CC BY-SA 3.0 DE ; l'événement est hors du cours) ; Alexeï Stakhanov expliquant sa méthode (Eleazar Langman, domaine public).",
    "Narration : voix de synthèse générées localement (Qwen3-TTS) ; musique originale.",
]
