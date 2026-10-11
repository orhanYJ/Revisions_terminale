/* Contenu propre aux fiches imprimables (le cours lui-même est lu dans dnl/index.html).
   Pour chaque chapitre : la frise (une dizaine de dates), la légende de la carte récapitulative
   et un schéma de synthèse. Tout est tiré du cours ; rien ne dépasse le point atteint en classe. */
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
        ["Saar, Jan. 1935: a plebiscite returns the territory to Germany (outside the course).", "Sarre, janv. 1935 : un plébiscite rend le territoire à l'Allemagne (hors cours)."],
        ["Rhineland, 7 Mar. 1936: reoccupied; France and Britain do not react.", "Rhénanie, 7 mars 1936 : réoccupée ; la France et le Royaume-Uni ne réagissent pas."],
        ["Vienna, 12 Mar. 1938: Anschluss; a plebiscite gives 99% “yes”, opponents and Jews excluded.", "Vienne, 12 mars 1938 : Anschluss ; plébiscite à 99 % de « oui », opposants et Juifs exclus."],
        ["Sudetenland, Oct. 1938: about 3 million German speakers, ceded to Germany.", "Sudètes, oct. 1938 : environ 3 millions de germanophones, cédés à l'Allemagne."],
        ["Prague, 15 Mar. 1939: the rest of the Czech lands occupied; appeasement ends; Slovakia becomes a satellite.", "Prague, 15 mars 1939 : le reste des pays tchèques occupé ; fin de l'apaisement ; la Slovaquie devient un satellite."],
        ["Danzig, 1 Sept. 1939: the free city of 1919 annexed (see the Première recap H11).", "Dantzig, 1er sept. 1939 : la ville libre de 1919 annexée (voir la fiche de Première H11)."],
        ["Poland, 1 Sept. 1939: invaded; France and Britain declare war on 3 Sept.", "Pologne, 1er sept. 1939 : envahie ; la France et le Royaume-Uni déclarent la guerre le 3."],
        ["Eastern Poland, Sept. 1939: occupied by the Red Army under the secret protocol of the pact.", "Est de la Pologne, sept. 1939 : occupé par l'Armée rouge en vertu du protocole secret du pacte."],
        ["Moscow, 23 Aug. 1939: Nazi-Soviet pact.", "Moscou, 23 août 1939 : pacte germano-soviétique."],
        ["Albania, Apr. 1939: occupied by Italy (outside the course).", "Albanie, avr. 1939 : occupée par l'Italie (hors cours)."],
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
      ["Sept. 1939–May 1940", "The phoney war", "La drôle de guerre"],
      ["10 May 1940", "German attack in the west; Churchill PM", "Attaque allemande à l'ouest ; Churchill Premier ministre"],
      ["26 May–4 June 1940", "Dunkirk: 338,000 evacuated", "Dunkerque : 338 000 évacués"],
      ["14 June 1940", "German troops enter Paris", "Les troupes allemandes entrent dans Paris"],
      ["22 June 1940", "Armistice at Rethondes", "Armistice de Rethondes"],
      ["Oct. 1940", "Vichy decree defining who is a Jew", "Décret de Vichy définissant qui est juif"],
      ["11 Dec. 1941", "Hitler defines the New Order", "Hitler définit l'Ordre nouveau"],
      ["July 1942", "Mass arrests of Jews for deportation", "Arrestations massives de Juifs pour la déportation"],
      ["11 Nov. 1942", "Germany invades the “free zone”", "L'Allemagne envahit la « zone libre »"]
    ],
    carte: {
      titre: ["Europe dominated by the Axis (1939 – May 1941)", "L'Europe dominée par l'Axe (1939 - mai 1941)"],
      carre: true,
      serie: [
        [["Oct. 1939", "Oct. 1939"], "Poland conquered and partitioned with the USSR; the phoney war in the west.", "La Pologne conquise et partagée avec l'URSS ; la drôle de guerre à l'ouest."],
        [["July 1940", "Juill. 1940"], "Denmark, Norway, the Benelux and France defeated; the USSR takes the Baltic states and Bessarabia; Britain alone.", "Le Danemark, la Norvège, le Benelux et la France vaincus ; l'URSS prend les pays baltes et la Bessarabie ; le Royaume-Uni seul."],
        [["May 1941", "Mai 1941"], "The Balkans occupied; Hungary, Romania and Bulgaria in the Axis — on the eve of the attack on the USSR.", "Les Balkans occupés ; la Hongrie, la Roumanie et la Bulgarie dans l'Axe, à la veille de l'attaque contre l'URSS."]
      ],
      cles: [
        ["#5E1C19", "The Reich: Germany, Austria, Sudetenland, Bohemia-Moravia, Alsace-Moselle (1940)", "Le Reich : Allemagne, Autriche, Sudètes, Bohême-Moravie, Alsace-Moselle (1940)"],
        ["#B8564C", "Occupied by Germany (dates on the map)", "Occupé par l'Allemagne (dates sur la carte)"],
        ["hatch-vi", "Vichy France, the “free zone” until 11 Nov. 1942", "La France de Vichy, « zone libre » jusqu'au 11 nov. 1942"],
        ["#8E6F37", "Italy and Albania", "Italie et Albanie"],
        ["#E2C88E", "Allies of the Axis", "Alliés de l'Axe"],
        ["#6F7E99", "USSR", "URSS"],
        ["hatch-su", "Soviet gains, 1939–40: eastern Poland, Baltic states, Bessarabia, Karelia", "Gains soviétiques, 1939-40 : est de la Pologne, pays baltes, Bessarabie, Carélie"],
        ["#5F86AD", "United Kingdom: alone against Germany from June 1940", "Royaume-Uni : seul face à l'Allemagne à partir de juin 1940"],
        ["#E3DED2", "Neutral states", "États neutres"]
      ],
      reperes: [
        ["Poland, Sept. 1939: invaded, then partitioned with the USSR.", "Pologne, sept. 1939 : envahie, puis partagée avec l'URSS."],
        ["Denmark, Apr. 1940: occupied (outside the course).", "Danemark, avr. 1940 : occupé (hors cours)."],
        ["Norway, Apr.–June 1940: invaded (outside the course).", "Norvège, avr.-juin 1940 : envahie (hors cours)."],
        ["Netherlands, Belgium, Luxembourg, from 10 May 1940: overrun in a few days.", "Pays-Bas, Belgique, Luxembourg, à partir du 10 mai 1940 : submergés en quelques jours."],
        ["France, May–June 1940: defeated in six weeks; armistice of 22 June.", "France, mai-juin 1940 : vaincue en six semaines ; armistice du 22 juin."],
        ["United Kingdom: Churchill prime minister on 10 May 1940; the only nation still resisting in 1941.", "Royaume-Uni : Churchill Premier ministre le 10 mai 1940 ; seule nation qui résiste encore en 1941."],
        ["Baltic states, June 1940: occupied, then annexed by the USSR (outside the course).", "Pays baltes, juin 1940 : occupés, puis annexés par l'URSS (hors cours)."],
        ["Bessarabia, June 1940: taken from Romania by the USSR (outside the course).", "Bessarabie, juin 1940 : prise à la Roumanie par l'URSS (hors cours)."],
        ["Yugoslavia, Apr. 1941: invaded and partitioned (outside the course).", "Yougoslavie, avr. 1941 : envahie et dépecée (hors cours)."],
        ["Greece, Apr.–May 1941: occupied (outside the course).", "Grèce, avr.-mai 1941 : occupée (hors cours)."],
        ["Hungary, Romania, Bulgaria: join the Axis in 1940–41 (outside the course).", "Hongrie, Roumanie, Bulgarie : rejoignent l'Axe en 1940-41 (hors cours)."],
        ["Vichy: Pétain's regime, which chose collaboration.", "Vichy : le régime de Pétain, qui choisit la collaboration."]
      ],
      note: ["Situation in May 1941, before the German attack on the USSR (22 June 1941), which Part II will study. The course says: by 1941 continental Europe was overcome and only Britain still resisted; items marked “outside the course” complete the picture. Base: borders of 1930, with the CShapes changes of 1939–40.", "Situation en mai 1941, avant l'attaque allemande contre l'URSS (22 juin 1941), que la partie II étudiera. Le cours dit : en 1941, l'Europe continentale est vaincue et seul le Royaume-Uni résiste encore ; les éléments « hors cours » complètent le tableau. Fond : frontières de 1930, avec les changements de 1939-40 d'après CShapes."]
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
        ["Italian zone: about 15 communes, mainly in the Alpes-Maritimes.", "Zone italienne : une quinzaine de communes, surtout dans les Alpes-Maritimes."],
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
  }
};
