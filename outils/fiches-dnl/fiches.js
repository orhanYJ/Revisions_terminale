/* Contenu propre aux fiches imprimables (le contenu des chapitres est lu dans dnl/index.html).
   Pour chaque chapitre : la frise (une dizaine de dates), la légende de la carte récapitulative
   et un schéma de synthèse. Tout est tiré des chapitres du site. */
module.exports = {
  H1: {
    frise: [
      ["1924", "Dawes Plan: American loans to Germany", "Plan Dawes : prêts américains à l'Allemagne"],
      ["24 Oct. 1929", "Black Thursday: the Crash begins", "Jeudi noir : le krach commence"],
      ["June 1930", "Smoot–Hawley Tariff; Canada retaliates", "Tarif Smoot-Hawley ; riposte du Canada"],
      ["May–Sept. 1931", "Creditanstalt fails; Britain leaves gold", "Faillite de la Creditanstalt ; Londres quitte l'or"],
      ["Sept. 1931", "Mukden incident: Japan invades Manchuria", "Incident de Moukden : le Japon envahit la Mandchourie"],
      ["1933", "Hitler chancellor; Roosevelt's New Deal", "Hitler chancelier ; New Deal de Roosevelt"],
      ["1935", "Italy invades Ethiopia; first Neutrality Act", "L'Italie envahit l'Éthiopie ; premier Neutrality Act"],
      ["1936", "Rhineland remilitarised; Front populaire", "Remilitarisation de la Rhénanie ; Front populaire"],
      ["Sept. 1938", "Munich Agreement", "Accords de Munich"],
      ["1 Sept. 1939", "Germany invades Poland", "L'Allemagne envahit la Pologne"]
    ],
    carte: {
      titre: ["The crisis goes global, and the aggressions it opened (1929–1939)", "La crise devient mondiale, et les agressions qu'elle ouvre (1929-1939)"],
      monde: true,
      serie: [
        [["Oct. 1929", "oct. 1929"], "The Crash in New York; American loans start to be recalled.", "Le krach de New York ; les prêts américains commencent à être rappelés."],
        [["1931", "1931"], "Banks fail in Austria and Germany, Britain leaves gold, commodity prices collapse; Japan invades Manchuria.", "Faillites bancaires en Autriche et en Allemagne, Londres quitte l'or, effondrement des prix agricoles ; le Japon envahit la Mandchourie."],
        [["1933", "1933"], "The trough: France hit in turn; Hitler in power, so three militarist regimes; Roosevelt's New Deal.", "Le creux : la France touchée à son tour ; Hitler au pouvoir, d'où trois régimes militaristes ; New Deal de Roosevelt."],
        [["1935–37", "1935-37"], "The aggressions: Italy in Ethiopia (1935–36), Japan attacks China (1937); the democracies retreat.", "Les agressions : l'Italie en Éthiopie (1935-36), le Japon attaque la Chine (1937) ; les démocraties se replient."]
      ],
      cles: [
        ["#8E2F2A", "Origin of the crisis: the United States", "Origine de la crise : les États-Unis"],
        ["#E8C9C4", "European economies hit by the recall of American loans", "Économies européennes frappées par le rappel des prêts américains"],
        ["#EBDDB5", "Exporters of one commodity, ruined by falling prices", "Exportateurs d'un seul produit, ruinés par la chute des prix"],
        ["#CFDDD8", "USSR, outside world trade: barely touched", "URSS, hors du commerce mondial : à peine touchée"],
        ["#A9BED3", "Militarist regimes (Japan, Italy; Germany from 1933)", "Régimes militaristes (Japon, Italie ; Allemagne dès 1933)"],
        ["hatch", "Territories conquered by force", "Territoires conquis par la force"]
      ],
      reperes: [
        ["New York, 24–29 Oct. 1929: the Crash; the Dow Jones loses 89% by July 1932.", "New York, 24-29 oct. 1929 : le krach ; le Dow Jones perd 89 % jusqu'en juillet 1932."],
        ["Canada retaliates within days against Smoot–Hawley (1930); Ottawa Conference and imperial preference (1932).", "Le Canada riposte en quelques jours au tarif Smoot-Hawley (1930) ; conférence d'Ottawa et préférence impériale (1932)."],
        ["Vienna, May 1931: the Creditanstalt fails; German banks follow in July.", "Vienne, mai 1931 : faillite de la Creditanstalt ; les banques allemandes suivent en juillet."],
        ["London, Sept. 1931: Britain leaves the Gold Standard; Import Duties Act, 10% tariff (1932).", "Londres, sept. 1931 : le Royaume-Uni quitte l'étalon-or ; Import Duties Act, droit de 10 % (1932)."],
        ["Berlin: 43.8% of insured workers unemployed (1932); Hitler chancellor (Jan. 1933).", "Berlin : 43,8 % des assurés au chômage (1932) ; Hitler chancelier (janv. 1933)."],
        ["Paris: France hit late (1932); riots of 6 Feb. 1934; Front populaire (1936).", "Paris : la France touchée tard (1932) ; émeutes du 6 février 1934 ; Front populaire (1936)."],
        ["Brazil: about 78 million bags of coffee burned (1931–44) to hold up the price.", "Brésil : environ 78 millions de sacs de café brûlés (1931-44) pour soutenir les cours."],
        ["Chile: nitrate export earnings down by more than 80% (1929–32).", "Chili : recettes d'exportation du nitrate en baisse de plus de 80 % (1929-32)."],
        ["USSR: in its first Five-Year Plan, outside the capitalist trading system.", "URSS : en plein premier plan quinquennal, hors du système commercial capitaliste."],
        ["Mukden, 18 Sept. 1931: false-flag attack; Japan invades Manchuria (Manchukuo).", "Moukden, 18 sept. 1931 : attentat sous fausse bannière ; le Japon envahit la Mandchourie (Mandchoukouo)."],
        ["Ethiopia, Oct. 1935: invaded by Italy; the League debates sanctions until May 1936.", "Éthiopie, oct. 1935 : envahie par l'Italie ; la SDN débat des sanctions jusqu'en mai 1936."]
      ],
      note: ["Borders of 1930. Arrows: Japanese and Italian aggressions; dashed: the recall of American loans.", "Frontières de 1930. Flèches : agressions japonaise et italienne ; tirets : rappel des prêts américains."]
    },
    schema: {
      type: "chaine",
      titre: ["How the crash became a world depression — and pushed the world towards war", "Comment le krach devient une dépression mondiale, et pousse le monde vers la guerre"],
      etapes: [
        ["Speculation", "Buying on margin; the market triples (1924–29)", "Spéculation", "Achat à crédit ; la Bourse triple (1924-29)"],
        ["Crash", "24–29 Oct. 1929: panic selling", "Krach", "24-29 oct. 1929 : ventes de panique"],
        ["Bank failures", "5,000 US banks by 1932: the Depression begins", "Faillites bancaires", "5 000 banques américaines en 1932 : la Dépression commence"],
        ["Loans recalled, gold", "Dawes circuit broken; rates raised everywhere", "Prêts rappelés, or", "Circuit Dawes rompu ; taux relevés partout"],
        ["Economic nationalism", "Tariffs, quotas, imperial blocs; trade −66%", "Nationalisme économique", "Droits de douane, quotas, blocs impériaux ; commerce −66 %"],
        ["Two roads", "Democracies retreat; three regimes choose militarism", "Deux voies", "Les démocraties se replient ; trois régimes choisissent le militarisme"]
      ]
    }
  },
  H2: {
    frise: [
      ["Oct. 1917", "Bolshevik coup in Russia", "Coup d'État bolchevique en Russie"],
      ["1919", "Versailles “Diktat”; D'Annunzio seizes Fiume", "« Diktat » de Versailles ; D'Annunzio prend Fiume"],
      ["Oct. 1922", "March on Rome: Mussolini Prime Minister", "Marche sur Rome : Mussolini président du Conseil"],
      ["1925", "“Fascistissime” laws: a totalitarian State", "Lois « fascistissimes » : un État totalitaire"],
      ["1928", "First Five-Year Plan; forced collectivisation", "Premier plan quinquennal ; collectivisation forcée"],
      ["30 Jan. 1933", "Hindenburg appoints Hitler chancellor", "Hindenburg nomme Hitler chancelier"],
      ["1935", "Nuremberg laws; Italy invades Ethiopia", "Lois de Nuremberg ; l'Italie envahit l'Éthiopie"],
      ["1936–38", "Great Purge: 680,000 executions", "Grandes purges : 680 000 exécutions"],
      ["1938", "Anschluss (March); Munich (Sept.)", "Anschluss (mars) ; Munich (sept.)"],
      ["23 Aug. 1939", "Nazi-Soviet pact; war on 1–3 Sept.", "Pacte germano-soviétique ; guerre les 1er-3 sept."]
    ],
    carte: {
      titre: ["Europe from 1933 to 1939: regimes and the stages of expansion", "L'Europe de 1933 à 1939 : les régimes et les étapes de l'expansion"],
      serie: [
        [["1933", "1933"], "Hitler in power: two fascist regimes, the USSR, democracies in the west and north.", "Hitler au pouvoir : deux régimes fascistes, l'URSS, des démocraties à l'ouest et au nord."],
        [["1936", "1936"], "The Saar returns (1935), the Rhineland is remilitarised; civil war in Spain.", "La Sarre revient (1935), la Rhénanie est remilitarisée ; guerre civile en Espagne."],
        [["End of 1938", "Fin 1938"], "Austria annexed (March), the Sudetenland ceded at Munich (September).", "L'Autriche annexée (mars), les Sudètes cédés à Munich (septembre)."],
        [["Sept. 1939", "Sept. 1939"], "Bohemia-Moravia occupied (March); Poland partitioned between Germany and the USSR.", "La Bohême-Moravie occupée (mars) ; la Pologne partagée entre l'Allemagne et l'URSS."]
      ],
      cles: [
        ["#5E1C19", "Nazi Germany, borders of 1933", "L'Allemagne nazie, frontières de 1933"],
        ["#8E2F2A", "1935: the Saar returns to Germany", "1935 : la Sarre revient à l'Allemagne"],
        ["hatch-rh", "1936: the Rhineland remilitarised (simplified area)", "1936 : la Rhénanie remilitarisée (zone simplifiée)"],
        ["#B8564C", "1938: Austria (Anschluss) and the Sudetenland (Munich)", "1938 : l'Autriche (Anschluss) et les Sudètes (Munich)"],
        ["#D88A80", "1939: Bohemia-Moravia (March), Danzig and western Poland (September)", "1939 : la Bohême-Moravie (mars), Dantzig et l'ouest de la Pologne (septembre)"],
        ["hatch-su", "Sept. 1939: eastern Poland occupied by the USSR", "Sept. 1939 : l'est de la Pologne occupé par l'URSS"],
        ["#6F7E99", "USSR", "URSS"],
        ["#8E6F37", "Fascist Italy", "Italie fasciste"],
        ["#CDAE6F", "1939: Albania occupied by Italy", "1939 : l'Albanie occupée par l'Italie"],
        ["#C3D3E2", "Democracies", "Démocraties"],
        ["#EFE3C4", "Other authoritarian regimes", "Autres régimes autoritaires"],
        ["hatch-es", "Spain: civil war, 1936–39", "Espagne : guerre civile, 1936-39"]
      ],
      reperes: [
        ["Saar, Jan. 1935: a plebiscite returns the territory to Germany.", "Sarre, janv. 1935 : un plébiscite rend le territoire à l'Allemagne."],
        ["Rhineland, 7 Mar. 1936: reoccupied; France and Britain do not react.", "Rhénanie, 7 mars 1936 : réoccupée ; la France et le Royaume-Uni ne réagissent pas."],
        ["Vienna, 12 Mar. 1938: Anschluss; a plebiscite gives 99% “yes”, opponents and Jews excluded.", "Vienne, 12 mars 1938 : Anschluss ; plébiscite à 99 % de « oui », opposants et Juifs exclus."],
        ["Sudetenland, Oct. 1938: about 3 million German speakers, ceded to Germany.", "Sudètes, oct. 1938 : environ 3 millions de germanophones, cédés à l'Allemagne."],
        ["Prague, 15 Mar. 1939: the rest of the Czech lands occupied; appeasement ends; Slovakia becomes a satellite.", "Prague, 15 mars 1939 : le reste des pays tchèques occupé ; fin de l'apaisement ; la Slovaquie devient un satellite."],
        ["Danzig, 1 Sept. 1939: the free city of 1919 annexed (see the Première recap H11).", "Dantzig, 1er sept. 1939 : la ville libre de 1919 annexée (voir la fiche de Première H11)."],
        ["Poland, 1 Sept. 1939: invaded; France and Britain declare war on 3 Sept.", "Pologne, 1er sept. 1939 : envahie ; la France et le Royaume-Uni déclarent la guerre le 3."],
        ["Eastern Poland, Sept. 1939: occupied by the Red Army under the secret protocol of the pact.", "Est de la Pologne, sept. 1939 : occupé par l'Armée rouge en vertu du protocole secret du pacte."],
        ["Moscow, 23 Aug. 1939: Nazi-Soviet pact.", "Moscou, 23 août 1939 : pacte germano-soviétique."],
        ["Albania, Apr. 1939: occupied by Italy.", "Albanie, avr. 1939 : occupée par l'Italie."],
        ["Spain, 1936–39: Germany and Italy back Franco (dashed arrows); France and Britain stay out.", "Espagne, 1936-39 : l'Allemagne et l'Italie soutiennent Franco (tirets) ; la France et le Royaume-Uni restent à l'écart."],
        ["Munich, 29–30 Sept. 1938: Hitler, Chamberlain, Daladier and Mussolini; the Czechs are not invited.", "Munich, 29-30 sept. 1938 : Hitler, Chamberlain, Daladier et Mussolini ; les Tchèques ne sont pas invités."]
      ],
      note: ["Base: borders of 1930. Sudetenland from the CShapes dataset; Saar, Bohemia-Moravia and the partition of Poland drawn from today's borders (approximate). Off the map: Ethiopia (1935–36), Manchuria (1931), China (1937).", "Fond : frontières de 1930. Sudètes d'après les données CShapes ; Sarre, Bohême-Moravie et partage de la Pologne tracés d'après les frontières actuelles (approximation). Hors carte : Éthiopie (1935-36), Mandchourie (1931), Chine (1937)."]
    },
    schema: {
      type: "tableau",
      titre: ["Three regimes compared: one totalitarian method, three supreme goals", "Trois régimes comparés : une même méthode totalitaire, trois buts suprêmes"],
      colonnes: [["Fascist Italy (1922–43)", "Italie fasciste (1922-43)"], ["Nazi Germany (1933–45)", "Allemagne nazie (1933-45)"], ["Stalin's USSR (1924–53)", "URSS de Staline (1924-53)"]],
      lignes: [
        [["Supreme goal", "But suprême"], ["The nation and the State; the glory of Rome", "La nation et l'État ; la grandeur de Rome"], ["The race: purity and domination", "La race : pureté et domination"], ["A classless society", "Une société sans classes"]],
        [["Road to power", "Accès au pouvoir"], ["March on Rome (Oct. 1922): appointed by the king", "Marche sur Rome (oct. 1922) : nommé par le roi"], ["Appointed by Hindenburg, 30 Jan. 1933", "Nommé par Hindenburg, 30 janv. 1933"], ["Bolshevik coup (1917), civil war", "Coup d'État bolchevique (1917), guerre civile"]],
        [["Leader", "Chef"], ["Il Duce", "Il Duce"], ["Der Führer", "Der Führer"], ["“Little father of the peoples”", "« Petit père des peuples »"]],
        [["Political police", "Police politique"], ["OVRA (1927), Special Court (1926)", "OVRA (1927), Tribunal spécial (1926)"], ["Gestapo and SS, both under Himmler", "Gestapo et SS, toutes deux sous Himmler"], ["OGPU, then NKVD (1934)", "OGPU, puis NKVD (1934)"]],
        [["Enemy of the nation", "Ennemi de la nation"], ["“Enemies of the State”", "« Ennemis de l'État »"], ["Jews, Roma, disabled people…", "Juifs, Roms, personnes handicapées…"], ["Kulaks, “class enemies”", "Koulaks, « ennemis de classe »"]],
        [["Youth", "Jeunesse"], ["Opera Nazionale Balilla (1926)", "Opera Nazionale Balilla (1926)"], ["Hitler Youth, compulsory in 1936", "Jeunesses hitlériennes, obligatoires en 1936"], ["Komsomol (1918)", "Komsomol (1918)"]],
        [["Terror", "Terreur"], ["Confino on islands; “less oppressive?”", "Relégation (confino) ; « moins oppressive ? »"], ["Dachau (1933), sterilisation, T4 (1939)", "Dachau (1933), stérilisation, T4 (1939)"], ["Gulag, Great Purge (680,000 executed)", "Goulag, grandes purges (680 000 exécutions)"]],
        [["Expansion", "Expansion"], ["Libya, Ethiopia (1935): a new Roman empire", "Libye, Éthiopie (1935) : un nouvel empire romain"], ["Lebensraum in the East (Mein Kampf)", "Lebensraum à l'Est (Mein Kampf)"], ["Pact with Hitler: share of Poland (1939)", "Pacte avec Hitler : part de la Pologne (1939)"]]
      ]
    }
  },
  H3: {
    frise: [
      ["1937", "Japan attacks southern China: war begins in Asia", "Le Japon attaque la Chine du Sud : la guerre commence en Asie"],
      ["1 Sept. 1939", "Germany invades Poland", "L'Allemagne envahit la Pologne"],
      ["18 June 1940", "De Gaulle's appeal from London", "Appel du général de Gaulle depuis Londres"],
      ["22 June 1940", "Armistice at Rethondes", "Armistice de Rethondes"],
      ["22 June 1941", "Operation Barbarossa", "Opération Barbarossa"],
      ["Dec. 1941", "Pearl Harbor; first killing centre (Chelmno)", "Pearl Harbor ; premier centre de mise à mort (Chelmno)"],
      ["July 1942", "Treblinka built; mass arrests of Jews in France", "Construction de Treblinka ; rafles de Juifs en France"],
      ["11 Nov. 1942", "Germany invades the “free zone”", "L'Allemagne envahit la « zone libre »"],
      ["2 Feb. 1943", "Paulus capitulates at Stalingrad", "Paulus capitule à Stalingrad"],
      ["19 Apr. 1943", "Warsaw ghetto uprising", "Soulèvement du ghetto de Varsovie"]
    ],
    carte: {
      titre: ["Europe dominated by the Axis, and the war in the East (1939–1943)", "L'Europe dominée par l'Axe, et la guerre à l'Est (1939-1943)"],
      serie: [
        [["Oct. 1939", "Oct. 1939"], "Poland conquered and partitioned with the USSR; the phoney war in the west.", "La Pologne conquise et partagée avec l'URSS ; la drôle de guerre à l'ouest."],
        [["July 1940", "Juill. 1940"], "Denmark, Norway, the Benelux and France defeated; the USSR takes the Baltic states and Bessarabia; Britain alone.", "Le Danemark, la Norvège, le Benelux et la France vaincus ; l'URSS prend les pays baltes et la Bessarabie ; le Royaume-Uni seul."],
        [["May 1941", "Mai 1941"], "The Balkans occupied; Hungary, Romania and Bulgaria in the Axis — on the eve of Barbarossa.", "Les Balkans occupés ; la Hongrie, la Roumanie et la Bulgarie dans l'Axe, à la veille de Barbarossa."],
        [["Nov. 1942", "Nov. 1942"], "The furthest German advance: from besieged Leningrad to Stalingrad and the Caucasus.", "L'avancée allemande maximale : de Leningrad assiégée à Stalingrad et au Caucase."]
      ],
      cles: [
        ["#5E1C19", "The Reich: Germany, Austria, Sudetenland, Bohemia-Moravia, Alsace-Moselle (1940)", "Le Reich : Allemagne, Autriche, Sudètes, Bohême-Moravie, Alsace-Moselle (1940)"],
        ["#B8564C", "Occupied by Germany and its allies (dates on the map)", "Occupé par l'Allemagne et ses alliés (dates sur la carte)"],
        ["hatch-vi", "Vichy France, the “free zone” until 11 Nov. 1942", "La France de Vichy, « zone libre » jusqu'au 11 nov. 1942"],
        ["#8E6F37", "Italy and Albania", "Italie et Albanie"],
        ["#E2C88E", "Allies of the Axis", "Alliés de l'Axe"],
        ["#6F7E99", "USSR (unoccupied)", "URSS (non occupée)"],
        ["hatch-su", "Soviet gains of 1939–40 still held in 1942", "Gains soviétiques de 1939-40 encore tenus en 1942"],
        ["#5F86AD", "United Kingdom: alone against Germany from June 1940 to June 1941", "Royaume-Uni : seul face à l'Allemagne de juin 1940 à juin 1941"],
        ["#E3DED2", "Neutral states", "États neutres"],
        ["line-f41", "Front line, 5 Dec. 1941 (simplified)", "Ligne de front, 5 déc. 1941 (tracé simplifié)"],
        ["line-f42", "Front line, Nov. 1942: the furthest advance (simplified)", "Ligne de front, nov. 1942 : l'avancée maximale (tracé simplifié)"]
      ],
      reperes: [
        ["Poland, Sept. 1939: invaded, then partitioned with the USSR.", "Pologne, sept. 1939 : envahie, puis partagée avec l'URSS."],
        ["Denmark, Apr. 1940: occupied.", "Danemark, avr. 1940 : occupé."],
        ["Norway, Apr.–June 1940: invaded; Britain fails to prevent it, and Chamberlain falls.", "Norvège, avr.-juin 1940 : envahie ; le Royaume-Uni n'empêche pas l'occupation, et Chamberlain tombe."],
        ["Netherlands, Belgium, Luxembourg, from 10 May 1940: overrun in a few days.", "Pays-Bas, Belgique, Luxembourg, à partir du 10 mai 1940 : submergés en quelques jours."],
        ["France, May–June 1940: defeated in six weeks; armistice of 22 June.", "France, mai-juin 1940 : vaincue en six semaines ; armistice du 22 juin."],
        ["United Kingdom: Churchill prime minister on 10 May 1940; the Blitz (1940–41) fails to win control of the air.", "Royaume-Uni : Churchill Premier ministre le 10 mai 1940 ; le Blitz (1940-41) n'obtient pas la maîtrise du ciel."],
        ["Baltic states, 1940: annexed by the USSR, then overrun by Germany in 1941.", "Pays baltes, 1940 : annexés par l'URSS, puis envahis par l'Allemagne en 1941."],
        ["Bessarabia and Northern Bukovina, 1940: taken from Romania by the USSR.", "Bessarabie et Bucovine du Nord, 1940 : prises à la Roumanie par l'URSS."],
        ["Yugoslavia, Apr. 1941: invaded and partitioned.", "Yougoslavie, avr. 1941 : envahie et dépecée."],
        ["Greece, Apr.–May 1941: occupied.", "Grèce, avr.-mai 1941 : occupée."],
        ["Finland, Romania, Hungary, Slovakia: German allies against the USSR in 1941; Bulgaria joins the Axis in 1941.", "Finlande, Roumanie, Hongrie, Slovaquie : alliées de l'Allemagne contre l'URSS en 1941 ; la Bulgarie rejoint l'Axe en 1941."],
        ["Vichy: Pétain's regime, which chose collaboration.", "Vichy : le régime de Pétain, qui choisit la collaboration."],
        ["Leningrad: besieged, never taken.", "Leningrad : assiégée, jamais prise."],
        ["Moscow, Dec. 1941: the German advance stopped by the Red Army.", "Moscou, déc. 1941 : l'avance allemande arrêtée par l'Armée rouge."],
        ["Stalingrad, Aug. 1942 – 2 Feb. 1943: the Germans stalled, encircled in November, Paulus capitulates: the turning point.", "Stalingrad, août 1942 - 2 févr. 1943 : les Allemands s'enlisent, sont encerclés en novembre, Paulus capitule : le tournant."],
        ["Occupied Soviet territory: scorched earth, war of annihilation, Soviet prisoners starved to death.", "Territoire soviétique occupé : terre brûlée, guerre d'anéantissement, prisonniers soviétiques morts de faim."]
      ],
      note: ["Dark arrows in the East: Operation Barbarossa (22 June 1941) and the summer offensive of 1942 towards Stalingrad and the Caucasus. Front lines and the Soviet border of 1941 simplified. Base: borders of 1930, with the changes of 1939–40 from the CShapes dataset.", "Flèches sombres à l'Est : l'opération Barbarossa (22 juin 1941) et l'offensive de l'été 1942 vers Stalingrad et le Caucase. Lignes de front et frontière soviétique de 1941 simplifiées. Fond : frontières de 1930, avec les changements de 1939-40 d'après CShapes."]
    },
    zoom: {
      titre: ["France defeated and cut up (1940–1942)", "La France vaincue et découpée (1940-1942)"],
      carre: true,
      petit: true,
      cles: [
        ["#E8C9C4", "Occupied zone: three-fifths of the country, German Military Command (MBF)", "Zone occupée : les trois cinquièmes du pays, commandement militaire allemand (MBF)"],
        ["#CFDDD8", "“Free zone”, governed from Vichy until 11 Nov. 1942", "« Zone libre », gouvernée depuis Vichy jusqu'au 11 nov. 1942"],
        ["#8E2F2A", "Alsace-Moselle, annexed: back to the borders of 1871", "Alsace-Moselle, annexée : retour aux frontières de 1871"],
        ["#EBDDB5", "Nord and Pas-de-Calais, attached to the German command in Brussels", "Nord et Pas-de-Calais, rattachés au commandement allemand de Bruxelles"],
        ["line", "Demarcation line", "Ligne de démarcation"],
        ["dots", "Maginot Line (schematic): it did not cover the Belgian border", "Ligne Maginot (schématique) : elle ne couvre pas la frontière belge"]
      ],
      reperes: [
        ["Dunkirk, 26 May–4 June 1940: Operation Dynamo, 338,000 soldiers evacuated.", "Dunkerque, 26 mai-4 juin 1940 : opération Dynamo, 338 000 soldats évacués."],
        ["Sedan, 13–20 May 1940: the armoured breakthrough after the Ardennes; Rommel's 7th Panzer Division races to the Somme.", "Sedan, 13-20 mai 1940 : la percée blindée après les Ardennes ; la 7e Panzer de Rommel fonce vers la Somme."],
        ["Paris, 14 June 1940: German troops enter; some 8 million people on the roads of the exodus.", "Paris, 14 juin 1940 : les troupes allemandes entrent ; quelque 8 millions de personnes sur les routes de l'exode."],
        ["Rethondes, 22 June 1940: the armistice; 1,850,000 French prisoners.", "Rethondes, 22 juin 1940 : l'armistice ; 1 850 000 prisonniers français."],
        ["Vichy: seat of Marshal Pétain's authoritarian regime, which chose collaboration.", "Vichy : siège du régime autoritaire du maréchal Pétain, qui choisit la collaboration."],
        ["Italian zone: about 15 communes in 1940, mainly in the Alpes-Maritimes; much larger from Nov. 1942 to Sept. 1943.", "Zone italienne : une quinzaine de communes en 1940, surtout dans les Alpes-Maritimes ; bien plus large de nov. 1942 à sept. 1943."],
        ["Alsace-Moselle: annexed and merged into German regions.", "Alsace-Moselle : annexée et fondue dans des régions allemandes."],
        ["Nord and Pas-de-Calais: under the German Military Command in Brussels (MBB).", "Nord et Pas-de-Calais : sous le commandement militaire allemand de Bruxelles (MBB)."]
      ],
      note: ["Red arrows: the German attack of May 1940; green dashes: the Allied advance into Belgium. Demarcation line: Département de l'Ain dataset (data.gouv.fr), drawn from the armistice documents.", "Flèches rouges : l'attaque allemande de mai 1940 ; tirets verts : l'avance alliée en Belgique. Ligne de démarcation : données du Département de l'Ain (data.gouv.fr), établies d'après les documents de l'armistice."]
    },
    schema: {
      type: "liste",
      titre: ["The New European Order: the five driving forces announced in the introduction", "Le Nouvel Ordre européen : les cinq forces motrices annoncées en introduction"],
      items: [
        ["Europe as a “racial entity”: racial purification through genocide", "L'Europe comme « entité raciale » : purification raciale par le génocide"],
        ["The quest for Lebensraum in the East", "La quête du Lebensraum à l'Est"],
        ["A crusade against communism", "Une croisade contre le communisme"],
        ["The Grossraum: Europe as a single economic unit serving Germany", "Le Grossraum : l'Europe comme unité économique unique au service de l'Allemagne"],
        ["Supplying Germany with the people, materials and money required for total war", "Fournir à l'Allemagne les hommes, les matières et l'argent qu'exige la guerre totale"]
      ]
    }
  },
  /* ---------- Géographie, thème 1 « Maritime Areas and Geopolitics » : les cartes sont celles du site (cartes-geo.js),
     légende comprise ; la fiche ne fait qu'ajouter des repères. ---------- */
  G1: {
    /* Géographie : un chapitre par thème. G1 = tout le thème 1 « Maritime Areas and Geopolitics », parties I à V ;
       les cartes sont celles du site (cartes-geo.js), légende comprise ; la fiche ne fait qu'ajouter des repères. */
    frise: [
      ["1869", "The Suez Canal opens", "Ouverture du canal de Suez"],
      ["1956", "Nasser nationalises Suez: the Suez Crisis", "Nasser nationalise Suez : crise de Suez"],
      ["1982", "UNCLOS (Montego Bay) creates the EEZs", "Convention de Montego Bay : création des ZEE"],
      ["2010", "Shanghai becomes the first container port", "Shanghai devient le premier port à conteneurs"],
      ["12 July 2016", "Arbitral ruling rejects the nine-dash line", "La sentence arbitrale rejette la ligne en neuf traits"],
      ["Mar. 2021", "The Ever Given blocks the Suez Canal", "L'Ever Given bloque le canal de Suez"],
      ["2022", "Israel–Lebanon maritime border agreement", "Accord frontalier maritime Israël–Liban"],
      ["Late 2023", "Houthi attacks: ships turn to the Cape", "Attaques houthies : les navires passent par le Cap"],
      ["June 2025", "UN Ocean Conference in Nice", "Conférence des Nations unies sur l'océan à Nice"],
      ["2026", "CMA CGM Notre Dame: 24,000 TEUs", "CMA CGM Notre Dame : 24 000 EVP"]
    ],
    carte: {
      titre: ["The maritimisation of the global economy: centres, routes, ports, choke points", "La maritimisation de l'économie mondiale : centres, routes, ports, choke points"],
      cles: [],
      reperes: [
        ["Shanghai: first container port since 2010, 50 million TEUs in 2024; Yangshan, offshore and automated.", "Shanghai : premier port à conteneurs depuis 2010, 50 millions d'EVP en 2024 ; Yangshan, au large et automatisé."],
        ["Singapore: second container port, 39 million TEUs (2023), connected to more than 600 ports.", "Singapour : deuxième port à conteneurs, 39 millions d'EVP (2023), relié à plus de 600 ports."],
        ["Rotterdam and the Northern Range: the first container region until the mid-1990s.", "Rotterdam et la Northern Range : première région à conteneurs jusqu'au milieu des années 1990."],
        ["FAL 1 (CMA CGM): 105 days, 15 ships, 11 ports of call; to Europe via Suez, back round the Cape.", "FAL 1 (CMA CGM) : 105 jours, 15 navires, 11 escales ; vers l'Europe par Suez, retour par le Cap."],
        ["Suez (1869) and Panama (1914): Rotterdam–Singapore 8,440 nautical miles via Suez, 11,940 round the Cape.", "Suez (1869) et Panama (1914) : Rotterdam–Singapour 8 440 milles par Suez, 11 940 par le Cap."],
        ["Chancay (Peru, 2024): a port 60% owned by COSCO, on China's Belt and Road.", "Chancay (Pérou, 2024) : un port détenu à 60 % par COSCO, sur les « routes de la soie »."]
      ],
      note: ["Natural Earth base map; routes simplified. The second map shows oil at the choke points and piracy.", "Fond Natural Earth ; tracés simplifiés. La seconde carte montre le pétrole aux choke points et la piraterie."]
    },
    zooms: [{
      fichier: "choke", label: ["Map", "Carte"],
      titre: ["Oil and the choke points (2023), attacks and piracy", "Le pétrole et les choke points (2023), attaques et piraterie"],
      cles: [],
      reperes: [
        ["Malacca 23.7 and Hormuz 20.9 million barrels a day (2023); in 2025, Suez fell to 4.9 and the Cape rose to 9.1: the Houthi detour.", "Malacca 23,7 et Ormuz 20,9 millions de barils par jour (2023) ; en 2025, Suez tombe à 4,9 et le Cap monte à 9,1 : le détour imposé par les Houthis."],
        ["Malacca: more than 200 ships a day, 29% of seaborne oil, 25% of traded goods; 60% of China's oil.", "Malacca : plus de 200 navires par jour, 29 % du pétrole transporté par mer, 25 % des marchandises ; 60 % du pétrole chinois."],
        ["Piracy: 668 incidents in 2011, 375 in 2020; Nigeria, Indonesia, Singapore first; in 2025 South-East Asia leads.", "Piraterie : 668 incidents en 2011, 375 en 2020 ; Nigeria, Indonésie, Singapour en tête ; en 2025, l'Asie du Sud-Est domine."]
      ],
      note: ["Volumes: U.S. Energy Information Administration; piracy: French Ministry of the Armed Forces and IMB.", "Volumes : U.S. Energy Information Administration ; piraterie : ministère des Armées et BMI."]
    }, {
      fichier: "arctic", label: ["Map", "Carte"],
      titre: ["The Arctic shipping routes opened by the melting ice", "Les routes arctiques ouvertes par la fonte des glaces"],
      cote: true,
      cles: [],
      reperes: [
        ["Three routes: the Northern Sea Route (along Russia), the Northwest Passage (Canadian archipelago), the Transpolar Sea Route (future).", "Trois routes : la route maritime du Nord (le long de la Russie), le passage du Nord-Ouest (archipel canadien), la route transpolaire (à venir)."],
        ["Open only a short time in late summer; expensive icebreakers: Russia at least 50, China 4, Denmark none since 2010.", "Ouvertes peu de temps à la fin de l'été ; des brise-glace coûteux : la Russie au moins 50, la Chine 4, le Danemark aucun depuis 2010."],
        ["Canada claims the Northwest Passage as Canadian waters; Greenland lies on its route.", "Le Canada revendique le passage du Nord-Ouest comme eaux canadiennes ; le Groenland est sur sa route."]
      ],
      note: ["Azimuthal polar projection, Natural Earth; routes simplified.", "Projection polaire azimutale, Natural Earth ; tracés simplifiés."]
    }, {
      fichier: "scs", label: ["Map", "Carte"], cote: true,
      titre: ["Territorial claims in the South China Sea", "Les revendications en mer de Chine méridionale"],
      cles: [],
      reperes: [
        ["China's nine-dash line (approximate) against the claims of Vietnam, the Philippines, Malaysia, Brunei and Taiwan.", "La ligne en neuf traits chinoise (approchée) face aux revendications du Vietnam, des Philippines, de la Malaisie, de Brunei et de Taïwan."],
        ["Paracels, Spratlys (Fiery Cross, artificial and militarised), Scarborough Shoal; the 2016 ruling in favour of the Philippines.", "Paracels, Spratleys (Fiery Cross, artificielle et militarisée), récif de Scarborough ; la sentence de 2016 en faveur des Philippines."],
        ["About 3 million km², more than US$5 trillion of trade a year; five maritime entries lead into it.", "Environ 3 millions de km², plus de 5 000 milliards de dollars d'échanges par an ; cinq entrées maritimes y mènent."]
      ],
      note: ["Mercator projection, Natural Earth; the nine-dash line is approximate.", "Projection de Mercator, Natural Earth ; la ligne en neuf traits est approchée."]
    }, {
      fichier: "bases", label: ["Map", "Carte"],
      titre: ["American sea power: the US Navy's forward deployed bases", "La puissance navale américaine : les bases avancées de l'US Navy"],
      cles: [],
      reperes: [
        ["US Navy: 11 aircraft carriers, 66 submarines, 73 destroyers, 340,000 active personnel.", "US Navy : 11 porte-avions, 66 sous-marins, 73 destroyers, 340 000 militaires d'active."],
        ["Navies by tonnage: USA 3.4 million t, far ahead of Russia, China, Japan, the UK and France.", "Marines par tonnage : États-Unis 3,4 millions de t, loin devant la Russie, la Chine, le Japon, le Royaume-Uni et la France."]
      ],
      note: ["Main naval bases; Natural Earth base map.", "Principales bases navales ; fond Natural Earth."]
    }, {
      fichier: "monde", label: ["Map", "Carte"],
      titre: ["France, a great maritime power", "La France, une grande puissance maritime"],
      cles: [],
      reperes: [
        ["EEZ of 10.7 million km², the 2nd in the world: 62% in the Pacific, 40% for French Polynesia alone; 97% of the maritime space is overseas.", "ZEE de 10,7 millions de km², la 2e du monde : 62 % dans le Pacifique, 40 % pour la seule Polynésie ; 97 % de l'espace maritime est outre-mer."],
        ["Bases on every ocean and abroad (Djibouti, Abu Dhabi); a nuclear aircraft carrier, 4 SSBNs, 5 SSNs.", "Des bases sur tous les océans et à l'étranger (Djibouti, Abou Dhabi) ; un porte-avions nucléaire, 4 SNLE, 5 SNA."],
        ["EXTRAPLAC: requests to extend the continental shelf; Atalanta against piracy; Total's gas off Mozambique.", "EXTRAPLAC : demandes d'extension du plateau continental ; Atalanta contre la piraterie ; le gaz de Total au large du Mozambique."]
      ],
      note: ["After a map by the French Navy and the Ministry for the Overseas (2019); EEZ approximated by 200-nautical-mile circles.", "D'après une carte de la Marine nationale et du ministère des Outre-mer (2019) ; ZEE approchée par des cercles de 200 milles."]
    }, {
      fichier: "metro", label: ["Zoom", "Zoom"], cote: true,
      titre: ["Ports, naval bases and shipyards of mainland France", "Ports, arsenaux et chantiers de la France métropolitaine"],
      cles: [],
      reperes: [
        ["66 ports; Marseille-Fos (Fos 4XL) and Le Havre are only 53rd and 68th in the world; far from the Northern Range.", "66 ports ; Marseille-Fos (Fos 4XL) et Le Havre ne sont que 53e et 68e mondiaux ; loin de la Northern Range."],
        ["Toulon, the most active arsenal (carrier, SSNs); Brest, Cherbourg; Chantiers de l'Atlantique at Saint-Nazaire.", "Toulon, l'arsenal le plus actif (porte-avions, SNA) ; Brest, Cherbourg ; Chantiers de l'Atlantique à Saint-Nazaire."]
      ],
      note: ["Natural Earth base map; main fishing ports.", "Fond Natural Earth ; principaux ports de pêche."]
    }, {
      fichier: "synth", label: ["Summary of the theme", "Synthèse du thème"],
      titre: ["Maritime areas in globalisation", "Les espaces maritimes dans la mondialisation"],
      cles: [],
      reperes: [
        ["A ready-made essay plan: 1) a space of circulation, 2) economic stakes, 3) strategic stakes.", "Un plan de dissertation tout fait : 1) un espace de circulation, 2) des enjeux économiques, 3) des enjeux stratégiques."],
        ["On the summary map, the top three maritime domains: the United States, the United Kingdom, France.", "Sur la carte de synthèse, les trois premiers domaines maritimes : États-Unis, Royaume-Uni, France."]
      ],
      note: ["Summary map of the theme; Arctic routes cut by the edge of the map.", "Carte de synthèse du thème ; routes arctiques coupées par le bord de la carte."]
    }],
    schemas: [{
      type: "chaine",
      titre: ["How maritimisation organises the global economy — and makes it vulnerable", "Comment la maritimisation organise l'économie mondiale, et la rend vulnérable"],
      etapes: [
        ["Containerisation", "One standard box for ship, truck and train", "Conteneurisation", "Une boîte standard pour le navire, le camion et le train"],
        ["Gigantism", "24,000-TEU ships; a few lines (MSC, Maersk, CMA CGM)", "Gigantisme", "Navires de 24 000 EVP ; quelques armateurs (MSC, Maersk, CMA CGM)"],
        ["Hubs and ports", "East Asia leads; ports move offshore", "Hubs et ports", "L'Asie orientale domine ; les ports gagnent le large"],
        ["Value chains", "TNCs produce near Asian ports: the NIDL", "Chaînes de valeur", "Les FTN produisent près des ports d'Asie : la NDIT"],
        ["Choke points", "Suez, Malacca, Hormuz: blockage, attacks, piracy", "Choke points", "Suez, Malacca, Ormuz : blocage, attaques, piraterie"],
        ["Rules", "EEZs (1982), protected areas, high seas treaty", "Règles", "ZEE (1982), aires protégées, traité sur la haute mer"]
      ]
    }, {
      type: "tableau",
      titre: ["Maritime areas: a source of conflict or of cooperation?", "Les espaces maritimes : source de conflit ou de coopération ?"],
      colonnes: [["Stakes", "Enjeux"], ["Sources of tension", "Sources de tension"], ["Cooperation or settlement", "Coopération ou règlement"]],
      lignes: [
        [["The Arctic", "L'Arctique"], ["Shorter routes, ores and fuels, development of remote regions", "Routes plus courtes, minerais et hydrocarbures, essor de régions isolées"], ["Sovereignty, crime, militarisation; icebreakers; Greenland", "Souveraineté, criminalité, militarisation ; brise-glace ; Groenland"], ["Long a region of cooperation and low tensions", "Longtemps une région de coopération et de faibles tensions"]],
        [["Northwest Passage", "Passage du Nord-Ouest"], ["A short cut instead of the Panama Canal", "Un raccourci au lieu du canal de Panama"], ["Canada claims it as Canadian waters", "Le Canada le revendique comme eaux canadiennes"], ["Benefits on paper, constraints in reality (DBQ)", "Atouts sur le papier, contraintes dans les faits (DBQ)"]],
        [["South China Sea", "Mer de Chine méridionale"], ["Trade, fish, oil and gas, approaches to China", "Commerce, pêche, hydrocarbures, approches de la Chine"], ["Nine-dash line, artificial islands, militia (2021)", "Ligne en neuf traits, îles artificielles, milice (2021)"], ["2016 ruling ignored; the Quad and a “Free and Open Indo-Pacific”", "Sentence de 2016 ignorée ; le Quad et un « Indo-Pacifique libre et ouvert »"]],
        [["Eastern Mediterranean", "Méditerranée orientale"], ["Gas fields (Karish, Qana)", "Gisements de gaz (Karish, Qana)"], ["Israel and Lebanon, technically at war", "Israël et le Liban, techniquement en guerre"], ["2022 agreement on the maritime border", "Accord de 2022 sur la frontière maritime"]]
      ]
    }, {
      type: "tableau",
      titre: ["A great maritime power, between power and fear of decline", "Une grande puissance maritime, entre puissance et peur du déclin"],
      colonnes: [["Strengths", "Atouts"], ["Limits", "Limites"]],
      lignes: [
        [["Territory and EEZ", "Territoire et ZEE"], ["2nd EEZ (10.7 M km²), on every ocean; EXTRAPLAC", "2e ZEE (10,7 M km²), sur tous les océans ; EXTRAPLAC"], ["Mostly distant territories (97% overseas)", "Surtout des territoires lointains (97 % outre-mer)"]],
        [["Navy", "Marine"], ["Nuclear carrier (with the USA only), 4 SSBNs, 5 SSNs, bases abroad", "Porte-avions nucléaire (avec les seuls États-Unis), 4 SNLE, 5 SNA, bases à l'étranger"], ["Equipment costly to renew", "Équipements coûteux à renouveler"]],
        [["Merchant navy, shipyards", "Marine marchande, chantiers"], ["CMA CGM, 3rd in the world; Saint-Nazaire's cruise ships", "CMA CGM, 3e mondial ; paquebots de Saint-Nazaire"], ["Ships under other flags; shipbuilding lost to Asia", "Navires sous d'autres pavillons ; construction navale perdue au profit de l'Asie"]],
        [["Ports", "Ports"], ["66 ports; Fos 4XL", "66 ports ; Fos 4XL"], ["Marseille 53rd, Le Havre 68th; far from the Northern Range", "Marseille 53e, Le Havre 68e ; loin de la Northern Range"]],
        [["Economy and resources", "Économie et ressources"], ["2.5% of GDP, 300,000 jobs; 3rd in Europe for fishing", "2,5 % du PIB, 300 000 emplois ; 3e en Europe pour la pêche"], ["Little offshore oil; marine renewables only 800 jobs", "Peu de pétrole en mer ; EMR : 800 emplois seulement"]],
        [["Protection", "Protection"], ["546 MPAs, 23.5% of waters (2019); Scandola", "546 AMP, 23,5 % des eaux (2019) ; Scandola"], ["The 2018 constitutional reform never completed", "La révision constitutionnelle de 2018 jamais aboutie"]]
      ]
    }]
  }
};
