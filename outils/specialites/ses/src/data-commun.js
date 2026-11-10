var CH = {}, CHAINES = {}, GRAPHES = {}, ANIMS = {};

var PROG = [
  { id: "eco", nom: "Science économique", qs: [
    { id: "e1", code: "É1", court: "Croissance", statut: "red", ecrit: true, spark: "e1-pib",
      titre: "Quels sont les sources et les défis de la croissance économique ?",
      objectifs: [
        "Comprendre le processus de croissance économique et les sources de la croissance : accumulation des facteurs et accroissement de la productivité globale des facteurs ; comprendre le lien entre le progrès technique et l’accroissement de la productivité globale des facteurs.",
        "Comprendre que le progrès technique est endogène et qu’il résulte en particulier de l’innovation.",
        "Comprendre comment les institutions (notamment les droits de propriété) influent sur la croissance en affectant l’incitation à investir et innover ; savoir que l’innovation s’accompagne d’un processus de destruction créatrice.",
        "Comprendre comment le progrès technique peut engendrer des inégalités de revenus.",
        "Comprendre qu’une croissance économique soutenable se heurte à des limites écologiques (notamment l’épuisement des ressources, la pollution et le réchauffement climatique) et que l’innovation peut aider à reculer ces limites."],
      notions: [] },
    { id: "e2", code: "É2", court: "Commerce international", statut: "red", ecrit: true,
      titre: "Quels sont les fondements du commerce international et de l’internationalisation de la production ?",
      objectifs: [
        "Comprendre le rôle des dotations factorielles et technologiques (avantages comparatifs) dans les échanges commerciaux et la spécialisation internationale.",
        "Comprendre le commerce entre pays comparables (différenciation des produits, qualité des produits, et fragmentation de la chaîne de valeur).",
        "Comprendre que la productivité des firmes sous-tend la compétitivité d’un pays, c’est-à-dire son aptitude à exporter.",
        "Comprendre l’internationalisation de la chaîne de valeur et savoir l’illustrer.",
        "Comprendre les effets induits par le commerce international : gains moyens en termes de baisse de prix, réduction des inégalités entre pays, accroissement des inégalités de revenus au sein de chaque pays ; comprendre les termes du débat entre libre-échange et protectionnisme."],
      notions: [] },
    { id: "e3", code: "É3", court: "Chômage", statut: "bt", ecrit: true,
      titre: "Comment lutter contre le chômage ?",
      objectifs: [
        "Savoir définir le chômage et le sous-emploi et connaître les indicateurs de taux de chômage et de taux d’emploi.",
        "Comprendre que les problèmes d’appariements (frictions, inadéquations spatiales et de qualifications) et les asymétries d’information (salaire d’efficience) sont des sources de chômage structurel.",
        "Comprendre les effets (positifs ou négatifs) des institutions sur le chômage structurel (notamment salaire minimum et règles de protection de l’emploi).",
        "Comprendre les effets des fluctuations de l’activité économique sur le chômage conjoncturel.",
        "Connaître les principales politiques mises en œuvre pour lutter contre le chômage : politiques macroéconomiques de soutien de la demande globale, politiques d’allégement du coût du travail, politiques de formation et politiques de flexibilisation pour lutter contre les rigidités du marché du travail."],
      notions: ["chômage (au sens du BIT)", "sous-emploi", "taux de chômage", "taux d’emploi", "appariement", "frictions", "inadéquations spatiales et de qualifications", "asymétries d’information", "salaire d’efficience", "chômage structurel", "salaire minimum", "règles de protection de l’emploi", "chômage conjoncturel", "fluctuations de l’activité", "demande globale", "coût du travail", "politiques de formation", "flexibilisation", "rigidités du marché du travail"],
      liens: "La destruction créatrice et le progrès technique biaisé (<a href=\"#e1\">É1 Croissance</a>) expliquent une partie du chômage des moins qualifiés ; la concurrence internationale aussi (<a href=\"#e2\">É2 Commerce</a>)." },
    { id: "e4", code: "É4", court: "Crises financières", statut: "bt", ecrit: false,
      titre: "Comment expliquer les crises financières et réguler le système financier ?",
      objectifs: [
        "Connaître les principales caractéristiques de la crise financière des années 1930 et de celle de 2008 (effondrement boursier, faillites en chaîne, chute du PIB et accroissement du chômage).",
        "Comprendre et savoir illustrer la formation et l’éclatement d’une bulle spéculative (comportements mimétiques et prophéties autoréalisatrices).",
        "Comprendre les phénomènes de panique bancaire et de faillites bancaires en chaîne.",
        "Connaître les principaux canaux de transmission d’une crise financière à l’économie réelle : effets de richesse négatif, baisse du prix du collatéral et ventes forcées, contraction du crédit.",
        "Connaître les principaux instruments de régulation du système bancaire et financier qui permettent de réduire l’aléa moral des banques : supervision des banques par la banque centrale, ratio de solvabilité."],
      notions: ["crise financière", "krach boursier", "bulle spéculative", "comportements mimétiques", "prophétie autoréalisatrice", "panique bancaire", "faillites bancaires en chaîne", "effet de richesse négatif", "collatéral", "ventes forcées", "contraction du crédit", "aléa moral", "supervision bancaire", "ratio de solvabilité"],
      liens: "La chute du PIB de 2009 (−2,8 % en volume) est visible sur le graphique de la croissance française du chapitre <a href=\"#e1:e1-1\">É1</a>." },
    { id: "e5", code: "É5", court: "Politiques européennes", statut: "bt", ecrit: true,
      titre: "Quelles politiques économiques dans le cadre européen ?",
      objectifs: [
        "Connaître les grandes caractéristiques de l’intégration européenne (marché unique et zone euro) ; comprendre les effets du marché unique sur la croissance.",
        "Comprendre les objectifs, les modalités et les limites de la politique européenne de la concurrence.",
        "Comprendre comment la politique monétaire et la politique budgétaire agissent sur la conjoncture.",
        "Savoir que la politique monétaire dans la zone euro, conduite de façon indépendante par la Banque centrale européenne, est unique alors que la politique budgétaire est du ressort de chaque pays membre mais contrainte par les traités européens ; comprendre les difficultés soulevées par cette situation (défaut de coordination, chocs asymétriques)."],
      notions: ["intégration européenne", "marché unique", "zone euro", "politique de la concurrence", "politique monétaire", "politique budgétaire", "conjoncture", "Banque centrale européenne", "indépendance de la banque centrale", "traités européens", "coordination des politiques", "chocs asymétriques"],
      liens: "Les gains du marché unique prolongent ceux du commerce entre pays comparables (<a href=\"#e2:e2-3\">É2</a>). Sujets 2026 : la dissertation du jour 2 portait sur la politique européenne de la concurrence, la partie 1 du jour 1 sur les chocs asymétriques." }
  ] },
  { id: "socio", nom: "Sociologie et science politique", qs: [
    { id: "s1", code: "S1", court: "Structure sociale", statut: "red", ecrit: true, spark: "s1-pcs",
      titre: "Comment est structurée la société française actuelle ?",
      objectifs: [
        "Savoir identifier les multiples facteurs de structuration et de hiérarchisation de l’espace social (catégorie socioprofessionnelle, revenu, diplôme, composition du ménage, position dans le cycle de vie, sexe, lieu de résidence).",
        "Comprendre les principales évolutions de la structure socioprofessionnelle en France depuis la seconde moitié du XXe siècle (salarisation, tertiarisation, élévation du niveau de qualification, féminisation des emplois).",
        "Connaître les théories des classes et de la stratification sociale dans la tradition sociologique (Marx, Weber) ; comprendre que la pertinence d’une approche en termes de classes sociales pour rendre compte de la société française fait l’objet de débats théoriques et statistiques : évolution des distances inter- et intra-classes, articulation avec les rapports sociaux de genre, identifications subjectives à un groupe social, multiplication des facteurs d’individualisation."],
      notions: [] },
    { id: "s2", code: "S2", court: "École", statut: "red", ecrit: false, spark: "s2-bac",
      titre: "Quelle est l’action de l’École sur les destins individuels et sur l’évolution de la société ?",
      objectifs: [
        "Comprendre que, dans les sociétés démocratiques, l’École transmet des savoirs et vise à favoriser l’égalité des chances ; comprendre l’évolution, depuis les années 1950, des principaux indicateurs mesurant l’accès à l’école et à l’enseignement supérieur (taux de scolarisation, taux d’accès à un diplôme ou à un type de formation) en distinguant les processus de massification et de démocratisation.",
        "Comprendre la multiplicité des facteurs d’inégalités de réussite scolaire (notamment, rôle de l’École, rôle du capital culturel et des investissements familiaux, socialisation selon le genre, effets des stratégies des ménages) dans la construction des trajectoires individuelles de formation."],
      notions: [] },
    { id: "s3", code: "S3", court: "Mobilité sociale", statut: "bt", ecrit: true,
      titre: "Quels sont les caractéristiques contemporaines et les facteurs de la mobilité sociale ?",
      objectifs: [
        "Savoir distinguer la mobilité sociale intergénérationnelle des autres formes de mobilité (géographique, professionnelle).",
        "Comprendre les principes de construction, les intérêts et les limites des tables de mobilité comme instrument de mesure de la mobilité sociale.",
        "Comprendre que la mobilité observée comporte une composante structurelle (mobilité structurelle) ; comprendre que la mobilité peut aussi se mesurer de manière relative indépendamment des différences de structure entre origine et position sociales (fluidité sociale) et qu’une société plus mobile n’est pas nécessairement une société plus fluide.",
        "À partir de la lecture des tables de mobilité, être capable de mettre en évidence des situations de mobilité ascendante, de reproduction sociale et de déclassement, et de retrouver les spécificités de la mobilité sociale des hommes et de celles des femmes.",
        "Comprendre comment l’évolution de la structure socioprofessionnelle, les niveaux de formation et les ressources et configurations familiales contribuent à expliquer la mobilité sociale."],
      notions: ["mobilité intergénérationnelle", "mobilité intragénérationnelle (professionnelle)", "mobilité géographique", "table de mobilité", "table de destinée", "table de recrutement", "mobilité observée", "mobilité structurelle", "fluidité sociale", "mobilité ascendante", "mobilité descendante", "reproduction sociale", "déclassement", "ressources et configurations familiales"],
      liens: "L’évolution de la structure socioprofessionnelle (<a href=\"#s1:s1-3\">S1</a>) explique la mobilité structurelle ; l’École et le capital culturel (<a href=\"#s2\">S2</a>) expliquent une partie de la reproduction. Sujet 2026 (jour 2, partie 1) : présenter les intérêts des tables de mobilité." },
    { id: "s4", code: "S4", court: "Travail et emploi", statut: "bt", ecrit: true,
      titre: "Quelles mutations du travail et de l’emploi ?",
      objectifs: [
        "Savoir distinguer les notions de travail, activité, statut d’emploi (salarié, non-salarié), chômage ; comprendre que les évolutions des formes d’emploi rendent plus incertaines les frontières entre emploi, chômage et inactivité.",
        "Connaître les principaux descripteurs de la qualité des emplois (conditions de travail, niveau de salaire, sécurité économique, horizon de carrière, potentiel de formation, variété des tâches).",
        "Comprendre les principales caractéristiques des modèles d’organisation taylorien (division du travail horizontale et verticale, relation hiérarchique stricte) et post-taylorien (flexibilité, recomposition des tâches, management participatif) ; comprendre les effets positifs et négatifs de l’évolution des formes de l’organisation du travail sur les conditions de travail.",
        "Comprendre comment le numérique brouille les frontières du travail (télétravail, travail / hors travail), transforme les relations d’emploi et accroît les risques de polarisation des emplois.",
        "Comprendre que le travail est source d’intégration sociale et que certaines évolutions de l’emploi (précarisation, taux persistant de chômage élevé, polarisation de la qualité des emplois) peuvent affaiblir ce pouvoir intégrateur."],
      notions: ["travail", "emploi", "activité", "statut d’emploi (salarié, non-salarié)", "inactivité", "qualité de l’emploi", "taylorisme", "division horizontale et verticale du travail", "post-taylorisme", "flexibilité", "management participatif", "télétravail", "polarisation des emplois", "intégration sociale", "précarisation"],
      liens: "La salarisation (86,7 % des emplois en 2024) est étudiée en <a href=\"#s1:s1-3\">S1</a> ; la polarisation des emplois par le progrès technique en <a href=\"#e1:e1-5\">É1</a>." },
    { id: "s5", code: "S5", court: "Engagement politique", statut: "bt", ecrit: true,
      titre: "Comment expliquer l’engagement politique dans les sociétés démocratiques ?",
      objectifs: [
        "Comprendre que l’engagement politique prend des formes variées (vote, militantisme, engagement associatif, consommation engagée).",
        "Comprendre pourquoi, malgré le paradoxe de l’action collective, les individus s’engagent (incitations sélectives, rétributions symboliques, structure des opportunités politiques).",
        "Comprendre que l’engagement politique dépend notamment de variables sociodémographiques (catégorie socioprofessionnelle, diplôme, âge et génération, sexe).",
        "Comprendre la diversité et les transformations des objets de l’action collective (conflits du travail, nouveaux enjeux de mobilisation, luttes minoritaires), des acteurs (partis politiques, syndicats, associations, groupements) et de leurs répertoires."],
      notions: ["engagement politique", "vote", "militantisme", "engagement associatif", "consommation engagée", "paradoxe de l’action collective", "incitations sélectives", "rétributions symboliques", "structure des opportunités politiques", "variables sociodémographiques", "action collective", "conflits du travail", "nouveaux enjeux de mobilisation", "luttes minoritaires", "partis politiques", "syndicats", "associations", "répertoires d’action collective"],
      liens: "Le diplôme et la PCS structurent l’espace social (<a href=\"#s1\">S1</a>) et aussi la participation politique. Sujet 2026 (jour 1, partie 2) : un tableau sur le vote systématique selon l’âge et le diplôme." }
  ] },
  { id: "rc", nom: "Regards croisés", qs: [
    { id: "r1", code: "R1", court: "Justice sociale", statut: "bt", ecrit: false,
      titre: "Quelles inégalités sont compatibles avec les différentes conceptions de la justice sociale ?",
      objectifs: [
        "Connaître les grandes tendances d’évolution des inégalités économiques depuis le début du XXe siècle et comprendre que les inégalités économiques et sociales présentent un caractère multiforme et cumulatif.",
        "Savoir interpréter les principaux outils de mesure des inégalités, statique (rapport inter-quantiles, courbe de Lorenz et coefficient de Gini, top 1 %) et dynamique (corrélation de revenu parents-enfants).",
        "Comprendre que les différentes formes d’égalité (égalité des droits, des chances ou des situations) permettent de définir ce qui est considéré comme juste selon différentes conceptions de la justice sociale (notamment l’utilitarisme, le libertarisme, l’égalitarisme libéral, l’égalitarisme strict).",
        "Comprendre que l’action des pouvoirs publics en matière de justice sociale (fiscalité, protection sociale, services collectifs, mesures de lutte contre les discriminations) s’exerce sous contrainte de financement et fait l’objet de débats en termes d’efficacité (réduction des inégalités), de légitimité (notamment consentement à l’impôt) et de risque d’effets pervers (désincitations)."],
      notions: ["inégalités économiques et sociales", "caractère multiforme et cumulatif des inégalités", "rapport inter-quantiles", "courbe de Lorenz", "coefficient de Gini", "top 1 %", "corrélation des revenus parents-enfants", "égalité des droits", "égalité des chances", "égalité des situations", "utilitarisme", "libertarisme", "égalitarisme libéral", "égalitarisme strict", "fiscalité", "protection sociale", "services collectifs", "discriminations", "consentement à l’impôt", "désincitations"],
      liens: "Les outils de mesure (déciles, D9/D1, Gini) sont déjà dans la page <a href=\"#outils\">Savoir-faire</a> ; le niveau de vie et ses écarts dans <a href=\"#s1:s1-1\">S1</a>." },
    { id: "r2", code: "R2", court: "Environnement", statut: "bt", ecrit: true,
      titre: "Quelle action publique pour l’environnement ?",
      objectifs: [
        "Savoir identifier les différents acteurs (pouvoirs publics, ONG, entreprises, experts, partis, mouvements citoyens) qui participent à la construction des questions environnementales comme problème public et à leur mise à l’agenda politique ; comprendre que ces acteurs entretiennent des relations de coopération et de conflit.",
        "Comprendre que l’action publique pour l’environnement articule différentes échelles (locale, nationale, européenne, mondiale).",
        "En prenant l’exemple du changement climatique : connaître les principaux instruments dont disposent les pouvoirs publics pour faire face aux externalités négatives sur l’environnement : réglementation, marchés de quotas d’émission, taxation, subvention à l’innovation verte ; comprendre que ces différents instruments présentent des avantages et des limites, et que leur mise en œuvre peut se heurter à des dysfonctionnements de l’action publique.",
        "En prenant l’exemple du changement climatique : comprendre qu’en présence de bien commun les négociations et accords internationaux liés à la préservation de l’environnement sont contraints par des stratégies de passager clandestin et les inégalités de développement entre pays."],
      notions: ["problème public", "mise à l’agenda politique", "acteurs de l’action publique (pouvoirs publics, ONG, entreprises, experts, partis, mouvements citoyens)", "échelles de l’action publique", "externalités négatives", "réglementation", "marché de quotas d’émission", "taxation", "subvention à l’innovation verte", "dysfonctionnements de l’action publique", "bien commun", "passager clandestin", "inégalités de développement"],
      liens: "Les limites écologiques de la croissance et le découplage (<a href=\"#e1:e1-6\">É1</a>) sont le point de départ. Sujet 2026 (jour 1, dissertation) : « Comment les questions environnementales peuvent-elles devenir un problème public ? »" }
  ] }
];

var ACCUEIL = { chiffres: [
  { n: "× 8,6", l: "Le PIB de la France en volume entre 1950 et 2025.", s: "Insee, comptes nationaux annuels, base 2020 (mai 2026)" },
  { n: "80,1 %", l: "La part d’une génération qui obtient le baccalauréat en 2025, contre 20,1 % en 1970.", s: "DEPP, Note d’information n° 26-05" },
  { n: "23,0 %", l: "La part des cadres dans l’emploi en 2024, contre 8,0 % en 1982.", s: "Insee, enquête Emploi 2024" }
] };

var AUTEURS = [
  { ch: "e1", n: "Robert Solow", d: "1924-2023 · Nobel 1987", th: "Modèle de croissance : le « résidu » attribué au progrès technique", l: "Modèle de croissance (1956) où le progrès technique est <b>exogène</b>. En 1957, il montre que l’essentiel de la hausse de la production par heure de travail aux États-Unis (1909-1949) ne s’explique pas par le capital : c’est le <b>résidu</b>, attribué au progrès technique." },
  { ch: "e1", n: "Paul Romer", d: "né en 1955 · Nobel 2018", th: "Croissance endogène : les connaissances, non rivales, se diffusent", l: "Fondateur des théories de la <b>croissance endogène</b> (1986, 1990) : les connaissances produites par la R&D sont <b>non rivales</b> et créent des externalités positives, donc des rendements croissants." },
  { ch: "e1", n: "Robert Lucas", d: "1937-2023 · Nobel 1995", th: "Croissance endogène par l’accumulation de capital humain", l: "Croissance endogène par le <b>capital humain</b> (1988) : l’éducation et la formation rendent chacun plus productif et rendent les autres plus productifs." },
  { ch: "e1", n: "Robert Barro", d: "né en 1944", th: "Croissance endogène par les infrastructures publiques", l: "Croissance endogène par les <b>dépenses publiques productives</b> (1990) : routes, réseaux, recherche publique augmentent la productivité des entreprises privées." },
  { ch: "e1", n: "Joseph Schumpeter", d: "1883-1950", th: "Innovations en grappes et destruction créatrice", l: "L’entrepreneur innovateur est le moteur du capitalisme ; les innovations arrivent <b>en grappes</b> et provoquent une <b>destruction créatrice</b> (<i>Capitalisme, socialisme et démocratie</i>, 1942)." },
  { ch: "e1", n: "Douglass North", d: "1920-2015 · Nobel 1993", th: "Les institutions sont les « règles du jeu » qui orientent les incitations", l: "Les <b>institutions</b> sont les « règles du jeu » d’une société, formelles (droit, droits de propriété) et informelles (normes, coutumes) ; elles expliquent les écarts durables de croissance." },
  { ch: "e1", n: "Daron Acemoglu et James Robinson", d: "Nobel 2024 avec Simon Johnson", th: "Institutions inclusives contre institutions extractives", l: "Les pays prospèrent avec des institutions <b>inclusives</b> (droits de propriété pour tous, concurrence, État de droit) et stagnent avec des institutions <b>extractives</b> qui captent la richesse au profit d’une élite (<i>Why Nations Fail</i>, 2012)." },
  { ch: "e1", n: "Philippe Aghion et Peter Howitt", d: "Nobel 2025 avec Joel Mokyr", th: "Modèle de croissance fondé sur la destruction créatrice", l: "Modèle mathématique de croissance par la <b>destruction créatrice</b> (1992) : chaque innovation rend la précédente obsolète ; la croissance dépend de la concurrence, des rentes d’innovation et de leur durée." },
  { ch: "e1", n: "Alfred Sauvy", d: "1898-1990", th: "Théorie du déversement des emplois entre secteurs", l: "Théorie du <b>déversement</b> : les gains de productivité détruisent des emplois dans un secteur mais en créent ailleurs, grâce aux nouveaux besoins que la hausse des revenus fait naître (<i>La Machine et le chômage</i>, 1980)." },
  { ch: "e1", n: "Claudia Goldin et Lawrence Katz", d: "<i>The Race between Education and Technology</i>, 2008", th: "La « course » entre l’éducation et la technologie", l: "Les inégalités de salaires dépendent d’une <b>course entre éducation et technologie</b> : quand l’offre de diplômés progresse moins vite que la demande de travail qualifié créée par le progrès technique, l’écart de salaire se creuse." },
  { ch: "e1", n: "Donella Meadows (dir.)", d: "rapport au Club de Rome, 1972", th: "<i>Les Limites à la croissance</i> (Club de Rome, 1972)", l: "Rapport <i>The Limits to Growth</i> : une croissance exponentielle de la production et de la population dans un monde fini mène à l’épuisement des ressources et à la pollution." },
  { ch: "e1", n: "William Stanley Jevons", d: "1835-1882", th: "Paradoxe : un usage plus efficace d’une ressource peut en accroître la consommation", l: "<i>The Coal Question</i> (1865) : les machines à vapeur plus économes en charbon ont fait <b>augmenter</b> la consommation totale de charbon. C’est l’ancêtre de l’<b>effet rebond</b>." },
  { ch: "e2", n: "Adam Smith", d: "1723-1790", th: "Avantage absolu : se spécialiser là où l’on produit avec moins de travail", l: "<i>La Richesse des nations</i> (1776) : chaque pays gagne à se spécialiser dans les biens pour lesquels il a un <b>avantage absolu</b> (il les produit avec moins de travail que les autres)." },
  { ch: "e2", n: "David Ricardo", d: "1772-1823", th: "Avantage comparatif : l’Angleterre, le Portugal, le drap et le vin", l: "<i>Des principes de l’économie politique et de l’impôt</i> (1817) : même un pays moins productif partout gagne à l’échange en se spécialisant là où son désavantage est le moins grand : l’<b>avantage comparatif</b>." },
  { ch: "e2", n: "Heckscher, Ohlin et Samuelson (HOS)", d: "1919, 1933, années 1940", th: "Un pays exporte les biens qui utilisent intensément son facteur abondant", l: "Modèle <b>HOS</b> : les avantages comparatifs viennent des <b>dotations factorielles</b>. Un pays exporte les biens intensifs dans le facteur dont il est relativement bien doté (Ohlin : Nobel 1977 ; Samuelson : Nobel 1970)." },
  { ch: "e2", n: "Wassily Leontief", d: "1905-1999 · Nobel 1973", th: "Paradoxe : les États-Unis exportaient des biens plutôt intensifs en travail", l: "En 1953, il trouve que les exportations des États-Unis, pays riche en capital, sont <b>plus intensives en travail</b> que leurs importations : un <b>paradoxe</b> pour HOS, qui s’explique par la qualification du travail américain." },
  { ch: "e2", n: "Paul Krugman", d: "né en 1953 · Nobel 2008", th: "Nouvelle théorie du commerce : rendements croissants et goût pour la variété", l: "<b>Nouvelle théorie du commerce international</b> (1979-1980) : les économies d’échelle et le goût des consommateurs pour la <b>variété</b> expliquent le commerce <b>intra-branche</b> entre pays semblables." },
  { ch: "e2", n: "Marc Melitz", d: "né en 1968", th: "Seules les firmes les plus productives exportent", l: "Modèle des <b>firmes hétérogènes</b> (2003) : exporter a un coût fixe ; seules les entreprises les plus productives peuvent le payer. L’ouverture réalloue la production vers elles." },
  { ch: "e2", n: "Friedrich List", d: "1789-1846", th: "Protectionnisme éducateur pour les industries naissantes", l: "<i>Système national d’économie politique</i> (1841) : un pays en retard doit protéger temporairement ses <b>industries naissantes</b> le temps qu’elles deviennent compétitives : c’est le <b>protectionnisme éducateur</b>." },
  { ch: "e2", n: "Branko Milanovic", d: "né en 1953", th: "La « courbe de l’éléphant » des gains de la mondialisation", l: "Avec Christoph Lakner, il montre que de 1988 à 2008 les classes moyennes des pays émergents et les plus riches du monde ont vu leurs revenus bondir, tandis que les classes populaires et moyennes des pays riches stagnaient : la <b>courbe de l’éléphant</b>." },
  { ch: "e2", n: "Autor, Dorn et Hanson", d: "« The China Syndrome », 2013", th: "Le « choc chinois » sur l’emploi industriel américain", l: "Les zones des États-Unis les plus exposées aux importations chinoises ont perdu durablement des emplois industriels et vu baisser les salaires : le <b>choc chinois</b>." },
  { ch: "s1", n: "Karl Marx", d: "1818-1883", th: "Classes définies par la place dans les rapports de production ; classe en soi et pour soi", l: "Les <b>classes sociales</b> se définissent par leur place dans les <b>rapports de production</b> : bourgeoisie propriétaire des moyens de production, prolétariat qui vend sa force de travail. Une classe « en soi » devient classe « pour soi » quand elle prend <b>conscience</b> de ses intérêts et lutte." },
  { ch: "s1", n: "Max Weber", d: "1864-1920", th: "Trois ordres : économique (classes), social (statut), politique (partis)", l: "Approche <b>multidimensionnelle</b> : ordre économique (<b>classes</b>, selon les chances d’accès aux biens), ordre social (<b>groupes de statut</b>, selon le prestige), ordre politique (<b>partis</b>, selon le pouvoir). <i>Économie et société</i> (1922, posthume)." },
  { ch: "s1", n: "Pierre Bourdieu", d: "1930-2002", th: "Espace social structuré par le volume et la structure des capitaux", l: "L’<b>espace social</b> se lit selon le <b>volume</b> et la <b>structure</b> du capital (économique, culturel, social, symbolique). Les goûts et les styles de vie marquent les positions : <i>La Distinction</i> (1979)." },
  { ch: "s1", n: "Henri Mendras", d: "1927-2003", th: "Moyennisation : la société en forme de « toupie »", l: "<i>La Seconde Révolution française 1965-1984</i> (1988) : la société s’organise autour d’une vaste <b>constellation centrale</b> ; la structure ressemble à une <b>toupie</b> : c’est la <b>moyennisation</b>." },
  { ch: "s1", n: "Louis Chauvel", d: "né en 1967", th: "« Le retour des classes sociales ? » (2001)", l: "Article « Le retour des classes sociales ? » (2001) : les inégalités ont cessé de se réduire ; il distingue l’identité <b>temporelle</b> (permanence), <b>culturelle</b> et <b>collective</b> d’une classe, et parle de « classes sans conscience »." },
  { ch: "s1", n: "Michel Pinçon et Monique Pinçon-Charlot", d: "1942-2022 ; née en 1946", th: "La grande bourgeoisie, une classe mobilisée « en soi et pour soi »", l: "Enquêtes sur la <b>grande bourgeoisie</b> : patrimoine, réseaux, entre-soi résidentiel (beaux quartiers, cercles). Pour eux, c’est la dernière classe à la fois « en soi » et « pour soi »." },
  { ch: "s1", n: "Kimberlé Crenshaw", d: "née en 1959", th: "Intersectionnalité : les dominations se croisent", l: "Juriste américaine qui propose en 1989 la notion d’<b>intersectionnalité</b> : les rapports de classe, de genre et de race se croisent et produisent des situations spécifiques." },
  { ch: "s1", n: "Ulrich Beck", d: "1944-2015", th: "Individualisation : chacun doit construire sa trajectoire", l: "<i>La Société du risque</i> (1986) : la hausse des revenus et de l’éducation et l’affaiblissement des appartenances collectives conduisent à une <b>individualisation</b> des trajectoires et des risques." },
  { ch: "s2", n: "Émile Durkheim", d: "1858-1917", th: "L’éducation, socialisation méthodique de la jeune génération", l: "L’éducation est une « <b>socialisation méthodique</b> de la jeune génération » : l’École transmet les valeurs communes qui font tenir la société (<i>Éducation et sociologie</i>, 1922, posthume)." },
  { ch: "s2", n: "Pierre Bourdieu et Jean-Claude Passeron", d: "1964 et 1970", th: "Capital culturel, héritiers et reproduction scolaire", l: "<i>Les Héritiers</i> (1964) et <i>La Reproduction</i> (1970) : l’École valorise une culture proche de celle des classes favorisées ; le <b>capital culturel</b> hérité se transforme en réussite scolaire, qui paraît due au seul mérite." },
  { ch: "s2", n: "Raymond Boudon", d: "1934-2013", th: "Stratégies : calcul coûts / avantages / risques selon la position sociale", l: "<i>L’Inégalité des chances</i> (1973) : à chaque palier d’orientation, les familles comparent <b>coûts, avantages et risques</b> d’une poursuite d’études ; ce calcul dépend de leur position sociale. Les choix individuels s’agrègent en inégalités (<b>effet d’agrégation</b>)." },
  { ch: "s2", n: "Bernard Lahire", d: "né en 1963", th: "Réussites « paradoxales » en milieu populaire selon les configurations familiales", l: "<i>Tableaux de familles</i> (1995) : la transmission du capital culturel n’est pas automatique ; des <b>configurations familiales</b> (ordre, régularité, autorité, rapport à l’écrit) expliquent des réussites en milieu populaire." },
  { ch: "s2", n: "Christian Baudelot et Roger Establet", d: "<i>Allez les filles !</i>, 1992", th: "Les filles réussissent mieux à l’école mais s’orientent moins vers les filières sélectives scientifiques", l: "<i>Allez les filles !</i> (1992) : les filles ont dépassé les garçons dans la réussite scolaire, mais leurs <b>orientations</b> restent moins tournées vers les filières scientifiques et les plus rentables." },
  { ch: "s2", n: "Marie Duru-Bellat", d: "née en 1950", th: "L’École des filles : socialisation de genre et orientation", l: "<i>L’École des filles</i> (1990) : les choix d’orientation des filles s’expliquent par une <b>socialisation différenciée</b> et par l’anticipation de leurs rôles futurs." },
  { ch: "s2", n: "Pierre Merle", d: "sociologue, <i>La Démocratisation de l’enseignement</i>, 2002", th: "Démocratisation ségrégative", l: "Distingue démocratisation <b>uniforme</b>, <b>égalisatrice</b> et <b>ségrégative</b> : l’accès au bac s’est ouvert, mais les enfants des classes populaires sont surreprésentés dans les filières les moins valorisées." },
  { ch: "s2", n: "Agnès van Zanten", d: "<i>Choisir son école</i>, 2009", th: "Stratégies scolaires des classes moyennes et contournement de la carte scolaire", l: "Étudie les <b>stratégies des familles</b> de classes moyennes et supérieures : choix de l’établissement, options, contournement de la carte scolaire, qui renforcent la ségrégation." }
];

var RESSOURCES = [
  { t: "Les textes officiels", l: [
    { n: "Programme de SES de terminale (arrêté du 19 juillet 2019)", u: "https://eduscol.education.fr/document/23155/download", b: "PDF officiel", d: "Les douze questions et leurs objectifs d’apprentissage, plus la liste des savoir-faire quantitatifs exigibles. C’est la liste de contrôle de tes révisions." },
    { n: "Note de service du 11 septembre 2026 : l’épreuve de SES à partir de la session 2027", u: "https://www.education.gouv.fr/bo/2026/Special4/MENE2622656N", b: "BO spécial n° 4", d: "Format de l’épreuve (dissertation ou épreuve composée), barème 3,5 / 5,5 / 9 + 2 points de langue, liste des neuf questions évaluables." },
    { n: "Bulletin officiel spécial n° 4 du 17 septembre 2026 (PDF complet)", u: "https://www.education.gouv.fr/sites/default/files/document/20260917boenjsspe4pdf-520753.pdf", b: "PDF", d: "Contient aussi la note sur le Grand oral à partir de 2027 (20 minutes, coefficient 8)." },
    { n: "Eduscol : programmes et ressources en SES (voie générale et technologique)", u: "https://eduscol.education.gouv.fr/5838/programmes-et-ressources-en-sciences-economiques-et-sociales-voie-gt", d: "La page du ministère qui rassemble programmes, ressources d’accompagnement et liens vers les partenaires." }
  ] },
  { t: "Sites de cours de référence", l: [
    { n: "SES-ENS (ENS de Lyon)", u: "https://ses.ens-lyon.fr/", d: "Site de ressources scientifiques pour les SES, issu d’une convention entre les ENS et le ministère : dossiers d’universitaires, actualité de la recherche." },
    { n: "Melchior", u: "https://www.melchior.fr/", b: "gratuit", d: "Plus de 10 000 ressources pédagogiques gratuites en SES et en économie, en partenariat avec l’Éducation nationale : notions, études de cas, exercices." },
    { n: "Collège de France : Campus de l’innovation pour les lycées", u: "https://www.college-de-france.fr/fr/le-college/campus-de-innovation-pour-les-lycees", d: "Partenariat avec le ministère : ressources et rencontres avec des chercheurs, notamment en SES." },
    { n: "Citéco, la Cité de l’économie", u: "https://www.citeco.fr/", d: "Musée et site de la Banque de France : fiches et animations sur la monnaie, la croissance, le commerce." },
    { n: "APSES (Association des professeurs de SES)", u: "https://www.apses.org/", d: "Actualité de la discipline, sujets et réactions aux épreuves." }
  ] },
  { t: "Sites des académies", l: [
    { n: "SES · académie d’Aix-Marseille", u: "https://www.pedagogie.ac-aix-marseille.fr/jcms/c_10418932/fr/accueil-ses", d: "Site disciplinaire académique." },
    { n: "SES · académie de Toulouse", u: "https://pedagogie.ac-toulouse.fr/ses/", d: "Rubrique « Enseigner » avec des ressources par niveau, dont la spécialité de terminale, la méthodologie et l’oral." },
    { n: "SES · académie de Nancy-Metz", u: "https://sites.ac-nancy-metz.fr/ses/wordpress/", d: "Sélection de ressources numériques pour les SES." },
    { n: "SES · académie de Besançon", u: "https://ses.ac-besancon.fr/", d: "Ressources pour la classe, présentation des épreuves." }
  ] },
  { t: "Les données utilisées sur ce site", l: [
    { n: "Insee : évolution du PIB et de ses composantes, 1950-2025", u: "https://www.insee.fr/fr/statistiques/2830613", b: "données", d: "Taux de croissance annuels et niveaux du PIB en volume (base 2020), mai 2026." },
    { n: "Insee : professions et secteurs d’activité (enquête Emploi 2024)", u: "https://www.insee.fr/fr/statistiques/8376826", b: "données", d: "Répartition de l’emploi par catégorie socioprofessionnelle de 1982 à 2024, par sexe, et par secteur." },
    { n: "Insee Première n° 2117 : niveau de vie et pauvreté en 2024", u: "https://www.insee.fr/fr/statistiques/9019316", b: "données", d: "Médiane, déciles, rapport interdécile, indice de Gini, taux de pauvreté." },
    { n: "data.gouv.fr : la proportion de bacheliers dans une génération", u: "https://www.data.gouv.fr/datasets/la-proportion-de-bacheliers-dans-une-generation", b: "données", d: "Série de la DEPP de 1970 à 2025, par type de bac et par sexe." },
    { n: "DEPP : résultats définitifs du baccalauréat 2025", u: "https://www.education.gouv.fr/depp/resultats-definitifs-du-baccalaureat-2025-moins-de-bacheliers-dans-les-voies-generale-et-469403", d: "Note d’information n° 26-05 : 80,1 % d’une génération bachelière en 2025." },
    { n: "Observatoire des inégalités : composition sociale des filières du supérieur", u: "https://www.inegalites.fr/Enseignement-superieur-comment-evolue-la-composition-sociale-des-filieres", d: "Part des enfants de cadres et d’ouvriers à l’université, en BTS, en CPGE et en ENS, de 2009 à 2024." },
    { n: "OMC : statistiques du commerce", u: "https://www.wto.org/french/res_f/statis_f/statis_f.htm", b: "données", d: "Valeur du commerce mondial de marchandises et de services commerciaux, principaux exportateurs." },
    { n: "Douane : résultats du commerce extérieur de la France en 2025", u: "https://www.douane.gouv.fr/actualites/resultats-du-commerce-exterieur-de-la-france-pour-le-mois-de-decembre-et-pour-lannee", d: "Solde commercial des biens, exportations, importations." },
    { n: "Citepa : inventaire des émissions de gaz à effet de serre", u: "https://www.citepa.org/", d: "Émissions françaises de 1990 à 2025 (rapport Secten 2026)." },
    { n: "CEPII", u: "https://www.cepii.fr/", d: "Centre français de recherche en économie internationale : analyses et bases de données sur le commerce mondial." }
  ] },
  { t: "Manuels", l: [
    { n: "Lelivrescolaire.fr · SES Première (2019)", u: "https://www.lelivrescolaire.fr/manuels/sciences-economiques-et-sociales-1re-2019", b: "consultable en ligne", d: "Manuel complet consultable en ligne, utile pour les rappels de Première (marché, monnaie, socialisation). Nous n’avons pas trouvé de manuel de Terminale chez cet éditeur." },
    { n: "Bordas · Passard & Perl, SES Terminale (édition 2025)", u: "https://www.editions-bordas.fr/ouvrage/passard-perl-ses-tle-manuel-de-leleve-ed-2025-9782047407134.html", b: "payant", d: "Manuel de Terminale conforme au programme. Les autres grands éditeurs (Nathan, Hatier, Magnard, Belin) publient aussi un manuel de Terminale : demande lequel ton lycée utilise." }
  ] },
  { t: "Annales", l: [
    { n: "L’Étudiant : sujets et corrigés du bac SES 2026", u: "https://www.letudiant.fr/bac/corriges-du-bac/article/sujets-et-corriges-bac-ses-2026.html", d: "Les deux jours de la session 2026, avec des corrigés proposés par des professeurs." },
    { n: "digiSchool : annales du bac SES", u: "https://www.digischool.fr/lycee/annales/terminale-generale/ses", d: "Sujets officiels des sessions précédentes et corrigés." }
  ] },
  { t: "Vidéos", l: [
    { n: "Dessine-moi l’éco", u: "https://www.youtube.com/user/dessinemoileco", b: "YouTube", d: "Courtes vidéos dessinées sur les notions d’économie (dette, chômage, monopoles, confiance)." },
    { n: "Les Bons Profs", u: "https://www.youtube.com/@LesBonsProfs", b: "YouTube", d: "Cours vidéo par des enseignants, dont des chapitres de SES et des conseils de méthode." }
  ] }
];
