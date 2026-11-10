// Généré par outils/serie-ses/site_ses.py depuis outils/specialites/ses/src/ : ne pas modifier à la main.
// Animations du site (anim-moteur.js, data-anim-e1.js, data-anim-e2.js, data-anim-s1s2.js, data-anim-s3s4s5r1.js) rejouées dans les vidéos (type sanim).
var CH = {}, CHAINES = {}, ANIMS = {};
var GRAPHES = {"e1-pib":{"type":"barres","t":"Taux de croissance du PIB de la France en volume, 1950-2025","s":"En % par rapport à l’année précédente. Touche une barre pour lire la valeur.","src":"Source : Insee, comptes nationaux annuels, base 2020 (mai 2026). Données 2024 semi-définitives, 2025 provisoires.","unite":" %","x":[1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],"y":[8.6,5.7,3.1,3.4,5.7,5.4,5,5.6,2.8,2.8,8,4.9,6.9,6.1,6.6,4.8,5.2,4.8,4.5,7.1,6.2,5.3,4.5,6.2,4.4,-0.9,4.3,3.6,3.9,3.7,1.7,1.2,2.4,1.3,1.6,1.6,2.4,2.6,4.8,4.4,2.8,1.2,1.5,-0.4,2.4,2.3,1.4,2.5,3.5,3.4,4.1,1.9,1.1,1,2.9,1.9,2.7,2.5,0.4,-2.8,2,2.4,0.2,0.8,1,1.1,0.9,2.1,1.6,2,-7.4,6.9,2.7,1.6,1.5,0.8],"bandes":[{"de":1950,"a":1973,"l":"1950-1973 : 5,2 %/an"}],"notes":[{"x":1975,"y":-0.9,"t":"1975"},{"x":2009,"y":-2.8,"t":"2009"},{"x":2020,"y":-7.4,"t":"2020 Covid"}],"pasX":10,"h":300,"min":-8,"max":10},"e1-periodes":{"type":"hbarres","t":"Croissance annuelle moyenne du PIB en volume, par période","s":"En % par an, calculé à partir des niveaux du PIB en volume (euros 2020).","src":"Source : Insee, comptes nationaux annuels, base 2020 ; calculs du site (taux annuel moyen).","unite":" %","cats":["1950-1973","1973-2007","2007-2019","2019-2025"],"series":[{"n":"Croissance moyenne","v":[5.2,2.4,1,0.9],"c":1}],"lab":110},"e1-decouplage":{"type":"hbarres","t":"France, 1990-2025 : la production augmente, les émissions baissent","s":"Variation entre 1990 et 2025, en %.","src":"Sources : Insee, PIB en volume, base 2020 (1 566,2 puis 2 646,7 milliards d’euros 2020) ; Citepa, rapport Secten 2026, émissions territoriales de gaz à effet de serre hors puits de carbone (−34,3 %, 359,4 Mt CO₂e en 2025, estimation provisoire).","unite":" %","cats":["PIB en volume","Émissions de gaz à effet de serre"],"series":[{"n":"Variation 1990-2025","v":[69,-34.3],"c":1}],"lab":150},"e2-monde":{"type":"hbarres","t":"Le commerce mondial en 2024","s":"Exportations mondiales, en milliers de milliards de dollars.","src":"Source : OMC, Perspectives et statistiques du commerce mondial (avril 2025). Marchandises : y compris le commerce entre pays de l’Union européenne.","unite":"","dec":2,"cats":["Marchandises","Services commerciaux","dont Chine (marchandises)"],"series":[{"n":"2024","v":[24.43,8.69,3.58],"c":1}],"lab":170},"e2-france":{"type":"hbarres","t":"Le commerce extérieur de biens de la France en 2025","s":"En milliards d’euros. Exportations FAB, importations CAF ; le solde officiel est calculé FAB/FAB.","src":"Source : Douane, résultats du commerce extérieur pour l’année 2025 (9 février 2026).","unite":"","cats":["Exportations de biens","Importations de biens","Solde commercial (FAB/FAB)"],"series":[{"n":"2025","v":[614.7,703.6,-69.2],"c":1}],"lab":170},"e2-iphone":{"type":"hbarres","t":"Qui produit la valeur d’un iPhone 3G ? (2009)","s":"Coût de fabrication estimé d’un iPhone 3G, en dollars (total : 178,96 $).","src":"Source : Y. Xing et N. Detert, « How the iPhone Widens the United States Trade Deficit with the People’s Republic of China », ADBI Working Paper n° 257, décembre 2010, d’après des estimations du cabinet iSuppli (2009).","unite":" $","dec":2,"cats":["Composants achetés aux fournisseurs (Japon, Allemagne, Corée du Sud, États-Unis…)","Assemblage en Chine"],"series":[{"n":"Coût","v":[172.46,6.5],"c":1}],"lab":200},"e3-chomage":{"type":"lignes","t":"Le taux de chômage en France, 1975-2025","spark":0,"s":"Taux de chômage au sens du BIT, en % de la population active. Touche le graphique pour lire une année.","src":"Source : Insee, enquête Emploi 2025, séries longues sur le marché du travail (juillet 2026). Champ : France, personnes vivant dans un logement ordinaire, actives.","unite":" %","pasX":10,"h":300,"min":0,"max":12,"x":[1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],"series":[{"n":"Ensemble","c":2,"v":[3.6,4,4.5,4.7,5.3,5.6,6.6,7.1,7.4,8.7,9.1,9.1,9.2,8.9,8.2,8,8.2,9,10,10.6,10,10.5,10.6,10.2,9.9,8.5,7.8,7.9,8.5,8.9,8.9,8.9,8,7.4,9.1,9.3,9.2,9.8,10.3,10.3,10.4,10.1,9.4,9.1,8.5,8.1,7.9,7.3,7.4,7.4,7.7]},{"n":"Femmes","c":3,"v":[5,5.8,6.4,6.6,7.4,8.2,9.1,9.5,9.7,10.8,11.1,11,11.4,11.1,10.6,10.1,10.2,11,11.5,12,11.5,11.8,11.8,11.5,11.1,9.8,9,8.7,9.3,9.7,9.6,9.5,8.4,7.8,9.2,9.5,9.5,9.7,10.2,10,9.9,9.9,9.4,9.1,8.4,8,7.8,7.2,7.3,7.3,7.6]},{"n":"Hommes","c":1,"v":[2.7,2.8,3.2,3.4,3.8,3.8,4.8,5.4,5.8,7,7.7,7.7,7.5,7.1,6.4,6.3,6.5,7.5,8.8,9.4,8.7,9.3,9.6,9.1,8.9,7.4,6.7,7.2,7.8,8.2,8.2,8.3,7.6,7.1,9,9.1,8.9,9.8,10.4,10.6,10.8,10.3,9.5,9,8.5,8.1,8,7.5,7.5,7.6,7.8]}]},"e3-diplome":{"type":"hbarres","t":"Qui est le plus exposé au chômage ? (2025)","s":"Taux de chômage au sens du BIT selon le diplôme et la catégorie socioprofessionnelle du dernier emploi, en %.","src":"Source : Insee, enquête Emploi 2025 (Emploi, chômage, revenus du travail, juillet 2026).","unite":" %","lab":170,"cats":["Aucun diplôme ou brevet","CAP, BEP ou équivalent","Baccalauréat","Bac + 2 ou plus","Ouvriers peu qualifiés","Employés peu qualifiés","Cadres"],"series":[{"n":"Taux de chômage","v":[14.7,7.6,9.1,5.3,17.1,11.4,4],"c":2}]},"e4-pib":{"type":"barres","t":"La France dans la crise de 2008-2009","s":"Taux de croissance du PIB en volume, en %.","src":"Source : Insee, comptes nationaux annuels, base 2020 (mai 2026).","unite":" %","x":[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013],"y":[2.9,1.9,2.7,2.5,0.4,-2.8,2,2.4,0.2,0.8],"pasX":1,"h":240,"min":-4,"max":4,"notes":[{"x":2009,"y":-2.8,"t":"−2,8 %"}]},"e5-bce":{"type":"lignes","t":"Le taux de la facilité de dépôt de la BCE, 2021-2026","s":"Taux en vigueur à la fin de chaque trimestre (dernier point : novembre 2026, trimestre en cours), en % (repères : premier trimestre de chaque année). Touche le graphique pour lire un trimestre.","src":"Source : Banque centrale européenne, taux directeurs (dates d’effet des décisions). Dernière valeur : 2,50 % depuis le 16 septembre 2026 (taux inchangé le 29 octobre 2026).","unite":" %","pasX":4,"h":260,"min":-1,"max":5,"dec":2,"sansDernier":true,"x":["2021","2021 T2","2021 T3","2021 T4","2022","2022 T2","2022 T3","2022 T4","2023","2023 T2","2023 T3","2023 T4","2024","2024 T2","2024 T3","2024 T4","2025","2025 T2","2025 T3","2025 T4","2026","2026 T2","2026 T3","nov. 2026"],"series":[{"n":"Facilité de dépôt","c":1,"v":[-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,0.75,2,3,3.5,4,4,4,3.75,3.5,3,2.5,2,2,2,2,2.25,2.5,2.5]}]},"e5-budget":{"type":"hbarres","t":"Les finances publiques françaises face aux règles européennes","s":"En % du PIB, 2025, comparé aux valeurs de référence des traités.","src":"Sources : Insee, comptes des administrations publiques (première estimation, mars 2026) : déficit 5,1 %, dette 115,6 % du PIB ; valeurs de référence du traité de Maastricht (1992) : 3 % et 60 %.","unite":" %","lab":120,"cats":["Déficit public","Dette publique"],"series":[{"n":"France 2025","v":[5.1,115.6],"c":2},{"n":"Référence européenne","v":[3,60],"c":1}]},"r1-ineg":{"type":"lignes","t":"Les inégalités de niveau de vie en France, 1996-2024","spark":1,"s":"Deux rapports, après impôts et prestations sociales. Touche le graphique pour lire une année ; touche la légende pour masquer une courbe.","src":"Source : Insee-DGFiP-Cnaf-Cnav-CCMSA, enquêtes Revenus fiscaux et sociaux (Insee Première n° 2117, juillet 2026). Champ : France métropolitaine, personnes vivant dans un logement ordinaire. Séries rétropolées par l’Insee de 1996 à 2020 pour corriger les ruptures de 2010, 2012 et 2020 ; point 2020 fragile.","unite":"","dec":2,"pasX":7,"h":280,"min":2,"max":6,"x":[1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],"series":[{"n":"Rapport interdécile D9/D1","c":1,"v":[3.51,3.49,3.42,3.44,3.5,3.43,3.39,3.35,3.3,3.35,3.41,3.38,3.38,3.44,3.48,3.58,3.55,3.44,3.43,3.47,3.42,3.43,3.5,3.44,3.29,3.41,3.38,3.49,3.48]},{"n":"Rapport des masses (100 − S80)/S20","c":2,"v":[4.08,4.03,3.99,4.07,4.14,4.09,3.98,4.01,3.97,4.14,4.19,4.16,4.19,4.21,4.4,4.47,4.44,4.17,4.17,4.2,4.17,4.17,4.34,4.2,4.07,4.45,4.4,4.53,4.62]}]},"r1-redis":{"type":"hbarres","t":"Ce que change la redistribution, 2024","s":"Rapports d’inégalité de niveau de vie avant et après impôts directs et prestations sociales.","src":"Source : Insee Première n° 2117 (juillet 2026). « Avant redistribution » : revenus d’activité, du patrimoine et de remplacement (pensions, allocations chômage) avant impôts directs et prestations sociales.","unite":"","dec":2,"lab":150,"cats":["Rapport interdécile D9/D1","Rapport des masses (100 − S80)/S20"],"series":[{"n":"Avant redistribution","v":[5.89,8.37],"c":2},{"n":"Après redistribution","v":[3.48,4.62],"c":1}]},"r1-patri":{"type":"hbarres","t":"L’échelle des patrimoines, début 2021","s":"Patrimoine brut des ménages (logement, placements, biens professionnels…), en euros. La première barre est presque invisible : c’est le message.","src":"Source : Insee, enquête Histoire de vie et Patrimoine 2020-2021 (Les revenus et le patrimoine des ménages, Insee Références, édition 2024). Champ : France hors Mayotte, ménages en logement ordinaire.","unite":" €","dec":0,"lab":150,"cats":["Plafond des 10 % les moins dotés (D1)","Médiane (D5)","Plancher des 10 % les mieux dotés (D9)","Plancher des 5 % les mieux dotés","Plancher des 1 % les mieux dotés"],"series":[{"n":"2021","v":[4400,177200,716300,1035000,2200000],"c":1}]},"r2-ges":{"type":"hbarres","t":"Qui émet le CO₂ fossile dans le monde ? (2024)","s":"Part des émissions mondiales de CO₂ d’origine fossile, en %.","src":"Source : Global Carbon Project, Global Carbon Budget 2025 (émissions de 2024).","unite":" %","lab":120,"cats":["Chine","États-Unis","Inde","Union européenne"],"series":[{"n":"Part des émissions mondiales","v":[32,13,8,6],"c":2}]},"s1-pcs":{"type":"lignes","t":"La structure socioprofessionnelle de l’emploi en France, 1982-2024","spark":2,"s":"Part de chaque catégorie dans l’emploi, en %. Touche le graphique pour lire une année ; touche la légende pour masquer une courbe.","src":"Source : Insee, enquête Emploi 2024, séries longues sur le marché du travail. Champ : France, personnes vivant dans un logement ordinaire, en emploi. L’enquête a connu des changements de méthode (ruptures de série).","unite":" %","pasX":7,"h":320,"min":0,"max":32,"x":[1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],"series":[{"n":"Agriculteurs","c":4,"v":[7.5,7.5,7.8,7.4,6.9,6.8,6.4,6.1,5.6,5.4,5,4.5,4.2,3.9,3.7,3.6,3.3,3.2,3,2.9,3,3.3,3,2.8,2.9,2.5,2.2,2.4,2.4,2.4,2.3,2.4,2.3,2.1,2.2,2,1.9,1.8,1.7,1.5,1.6,1.5,1.3]},{"n":"Artisans, commerçants, chefs d’entreprise","c":6,"v":[7.7,7.6,7.7,7.4,7.6,7.4,7.5,7.2,7.7,7.5,7.4,7.1,7.2,7,6.8,6.8,6.6,6.4,6,5.7,5.5,5.7,5.5,5.6,5.8,5.8,5.7,5.8,6.1,6,5.9,5.7,5.8,5.7,5.9,5.8,5.8,6,6.1,6.5,6.8,6.7,6.8]},{"n":"Cadres","c":2,"v":[8,8.5,8.8,8.7,9.3,9.5,10.2,10,10.8,11.4,12,12.2,12.7,12.8,12.9,13.1,13.2,13.5,13.7,14.2,14.7,15.1,15.4,15.9,16.1,16.2,16.5,16.8,17.1,17.9,18.3,17.8,17.5,18.1,18.4,18.6,19,20,21.1,21.5,21.6,22.4,23]},{"n":"Professions intermédiaires","c":3,"v":[18.8,19.4,19.9,20.2,20.2,20.4,20.3,20.4,19.9,20.6,20.6,21.5,21.3,21.4,21.3,21.5,21.5,21.6,21.5,21.7,21.9,21.8,22.1,22,22,22,22.7,23.1,23.3,23.3,23.6,24.3,24.7,24.5,24.9,24.8,24.9,24.8,25.1,24.7,24.7,25.1,25.2]},{"n":"Employés","c":5,"v":[26.4,26.3,26.4,26.7,27.1,27.4,27.7,28.2,27.9,27.2,27.4,28.5,28.7,29,29.3,29.4,29.5,29.7,29.7,29.8,30.1,30.3,30.1,30.2,30,30.3,30.3,30.1,29.7,29.2,29,29.1,29.2,29,28.1,27.9,27.9,27.5,26.5,26.2,25.9,25.2,24.8]},{"n":"Ouvriers","c":1,"v":[29.9,28.9,27.8,28,27.2,26.9,26.2,26.5,26.6,26.5,26,24.7,24.4,24.5,24.6,24.4,24.7,24.7,25.3,25.2,24.4,23.4,23.6,23,22.8,22.8,22.3,21.5,21,20.8,20.6,20.3,20.2,20.1,20.1,20.5,20.1,19.4,19.1,19.1,18.9,18.6,18]}]},"s1-sexe":{"type":"hbarres","t":"Femmes et hommes en emploi selon la catégorie socioprofessionnelle, 2024","s":"Répartition de chaque sexe, en % (chaque série totalise 100 % avec 0,9 % de non-renseignés).","src":"Source : Insee, enquête Emploi 2024 (Emploi, chômage, revenus du travail, édition 2025).","unite":" %","lab":150,"cats":["Agriculteurs","Artisans, commerçants, chefs d’entreprise","Cadres","Professions intermédiaires","Employés","Ouvriers"],"series":[{"n":"Femmes","v":[0.7,4.8,20.4,27.3,38.8,7.2],"c":2},{"n":"Hommes","v":[1.9,8.8,25.4,23.2,11.6,28.2],"c":1}]},"s1-niveau":{"type":"hbarres","t":"L’échelle des niveaux de vie en 2024","s":"Niveau de vie annuel par unité de consommation, en euros.","src":"Source : Insee Première n° 2117, juillet 2026. Champ : France métropolitaine, personnes vivant dans un logement ordinaire.","unite":" €","dec":0,"lab":160,"cats":["Plafond des 10 % les plus modestes (D1)","Médiane (D5)","Plancher des 10 % les plus aisés (D9)"],"series":[{"n":"2024","v":[13970,26740,48580],"c":1}]},"s2-bac":{"type":"lignes","t":"Proportion de bacheliers dans une génération, 1970-2025","s":"En %, tous baccalauréats. Touche le graphique pour lire une année.","src":"Source : ministère de l’Éducation nationale, DEPP (série publiée sur data.gouv.fr ; Note d’information n° 26-05). Champ : France hors DROM jusqu’en 2000, puis France hors Mayotte. 2020 et 2021 : épreuves remplacées en partie par le contrôle continu (crise sanitaire). 2024-2025 : données provisoires.","unite":" %","pasX":8,"h":300,"min":0,"max":100,"x":[1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],"series":[{"n":"Bacheliers dans une génération","c":2,"v":[20.1,21.4,22.2,23,23.7,24.2,23.9,24.6,25.3,25.2,25.9,26,27.2,28.1,28.6,29.4,31.2,32.6,36.3,39.8,43.5,47.5,51.1,54.7,58.9,62.7,61.3,61.8,62.6,61.6,62.9,61.9,61.6,62.3,60.8,61.1,62.6,62.7,62.3,65.2,65,71.2,78.3,74.9,78.6,77.7,78.7,79.6,80.6,79,86.7,83.6,80.2,80.7,80.5,80.1]}]},"s2-filieres":{"type":"hbarres","t":"Qui étudie où ? Origine sociale des étudiants selon la filière","s":"Part des enfants de cadres et d’ouvriers parmi les étudiants, en %, année 2023-2024.","src":"Source : Observatoire des inégalités (février 2025), d’après le ministère de l’Éducation nationale et de l’Enseignement supérieur, données 2023-2024. À comparer avec la part des cadres (23,0 %) et des ouvriers (18,0 %) dans l’emploi en 2024 (Insee).","unite":" %","lab":150,"cats":["Écoles normales supérieures","Classes préparatoires (CPGE)","Université","Sections de technicien supérieur (BTS)"],"series":[{"n":"Enfants de cadres","v":[64.9,53.7,34.9,15.9],"c":1},{"n":"Enfants d’ouvriers","v":[2,6.4,8.7,21.6],"c":2}]},"s2-sexe":{"type":"hbarres","t":"Filles et garçons bacheliers en 2025","s":"Proportion de bacheliers dans une génération, en %.","src":"Source : DEPP, données provisoires 2025 (data.gouv.fr). Champ : France hors Mayotte.","unite":" %","lab":130,"cats":["Tous baccalauréats","Bac général","Bac technologique","Bac professionnel"],"series":[{"n":"Filles","v":[85.4,49.9,16.8,18.7],"c":2},{"n":"Garçons","v":[75.1,37,15,23.1],"c":1}]},"s3-mob":{"type":"lignes","t":"La mobilité sociale observée en France, 1977-2015","spark":0,"s":"En % des personnes de 35 à 59 ans en emploi ou anciennement en emploi. Touche le graphique pour lire une année ; touche la légende pour masquer une courbe.","src":"Source : Insee, enquêtes Formation et qualification professionnelle (FQP) 1977 à 2014-2015 ; Insee Première n° 1739, février 2019. Champ : France métropolitaine, Français de 35 à 59 ans actifs occupés ou anciens actifs occupés. La FQP 2014-2015 est la dernière enquête publiée.","unite":" %","pasX":1,"h":300,"min":0,"max":70,"x":[1977,1985,1993,2003,2015],"series":[{"n":"Mobilité observée des hommes (par rapport au père)","c":1,"v":[63.8,66.2,67.4,66.4,65.2]},{"n":"Mobilité ascendante des hommes","c":2,"v":[23.5,26.6,30.3,30.8,27.6]},{"n":"Mobilité descendante des hommes","c":3,"v":[7.2,7.7,9.7,10.9,15]},{"n":"Mobilité ascendante des femmes (par rapport à la mère)","c":4,"v":[16.8,24.6,30.8,35.2,39.8]}]},"s3-dest":{"type":"hbarres","t":"Que deviennent les fils ? Deux origines comparées, 2015","s":"Position des fils de 35 à 59 ans selon la catégorie de leur père, en %. Chaque série totalise 100 %.","src":"Source : Insee, enquête FQP 2014-2015 (Insee Première n° 1739, figure 2). Catégories regroupées par l’Insee : les employés et les ouvriers sont classés ensemble selon leur qualification.","unite":" %","lab":150,"cats":["Agriculteurs exploitants","Artisans, commerçants, chefs d’entreprise","Cadres","Professions intermédiaires","Employés et ouvriers qualifiés","Employés et ouvriers non qualifiés"],"series":[{"n":"Fils de cadres","v":[0.2,7.9,49,25.4,13.7,3.8],"c":1},{"n":"Fils d’employés ou d’ouvriers non qualifiés","v":[0.6,6.5,8.3,18.7,43.9,22.1],"c":2}]},"s3-or":{"type":"barres","t":"La fluidité sociale progresse : le rapport des chances relatives, 1977-2015","s":"Rapport des chances relatives (odds ratio) d’être cadre plutôt qu’employé ou ouvrier non qualifié, entre fils de cadres et fils d’employés ou d’ouvriers non qualifiés. 1 = parfaite fluidité.","src":"Source : Marc Collet et Émilie Pénicaud, « La mobilité sociale des femmes et des hommes : évolutions entre 1977 et 2015 », Insee, France, portrait social, édition 2019, coll. Insee Références (figure 7c). Champ : hommes de 35 à 59 ans comparés à leur père.","unite":"","dec":1,"h":260,"pasX":1,"x":[1977,1985,1993,2003,2015],"y":[165,92.3,65.3,29.3,34.7],"etiquette":"fois"},"s4-statut":{"type":"hbarres","t":"Les formes d’emploi en 2025 : l’ensemble et les 15-24 ans","s":"Répartition des personnes en emploi selon le statut et le contrat, en %. Chaque série totalise 100 % (aux arrondis près).","src":"Source : Insee, enquête Emploi 2025 (Insee Première n° 2096, mars 2026, figure 3). Champ : France, personnes vivant dans un logement ordinaire, en emploi. CDD : toutes durées réunies.","unite":" %","lab":140,"cats":["CDI ou fonctionnaire","CDD","Intérim","Alternance, stage","Indépendants (dont micro-entrepreneurs)","Sans contrat ou contrat inconnu"],"series":[{"n":"Ensemble des personnes en emploi","v":[72.8,7.5,1.8,3.5,13.5,0.9],"c":1},{"n":"15-24 ans en emploi","v":[39.8,19.1,4.6,30.5,3.7,2.4],"c":2}]},"s4-cond":{"type":"hbarres","t":"Conditions de travail des salariés selon la catégorie, 2019","s":"Part des salariés concernés, en %.","src":"Source : Dares-Drees-DGAFP-Insee, enquête Conditions de travail 2019 (Insee Références, Emploi, chômage, revenus du travail, édition 2023, fiche 4.4). Contraintes de rythme : cadence d’une machine, déplacement automatique d’un produit, normes de production, demande extérieure, surveillance de la hiérarchie… Contraintes physiques : station debout prolongée, postures pénibles, charges lourdes…","unite":" %","dec":0,"lab":150,"cats":["Au moins trois contraintes de rythme","Travail répétitif","Ne pas pouvoir régler soi-même les incidents","Au moins trois contraintes physiques"],"series":[{"n":"Cadres","v":[22,11,17,7],"c":1},{"n":"Employés","v":[29,56,37,40],"c":3},{"n":"Ouvriers","v":[54,69,42,64],"c":2}]},"s4-halo":{"type":"hbarres","t":"Sans emploi et souhaitant travailler : chômeurs et halo, 2025","s":"Part de la population de chaque âge, en % (et non taux de chômage, qui se rapporte aux seuls actifs).","src":"Source : Insee, enquête Emploi 2025 (Insee Première n° 2096, figure 6). Champ : France, personnes de 15 à 64 ans vivant dans un logement ordinaire.","unite":" %","lab":130,"cats":["15-24 ans","25-49 ans","50-64 ans","Ensemble des 15-64 ans"],"series":[{"n":"Au chômage (BIT)","v":[8.5,6.2,3.7,5.8],"c":2},{"n":"Dans le halo autour du chômage","v":[7.4,4.4,2.8,4.5],"c":3}]},"s5-tend":{"type":"lignes","t":"Voter à chaque tour, parfois, ou jamais : 2002-2022","spark":1,"s":"Comportements des inscrits sur l’ensemble des tours de la présidentielle et des législatives de chaque année, en %.","src":"Source : Insee, enquêtes sur la participation électorale 2002 à 2022 (Insee Première n° 1929, novembre 2022). Champ : inscrits sur les listes électorales résidant en France métropolitaine.","unite":" %","pasX":1,"h":280,"min":0,"max":60,"x":[2002,2007,2012,2017,2022],"series":[{"n":"Vote systématique (tous les tours)","c":1,"v":[47.6,50.9,47.8,35.9,37]},{"n":"Vote intermittent","c":3,"v":[40.1,40.5,41.3,50.8,47.2]},{"n":"Abstention systématique (aucun tour)","c":2,"v":[12.2,8.6,10.9,13.4,15.8]}]},"s5-age":{"type":"lignes","t":"Le vote systématique selon l’âge, 2002 et 2022","s":"Part des inscrits de chaque âge qui ont voté à tous les tours de la présidentielle et des législatives, en %.","src":"Source : Insee, enquêtes sur la participation électorale 2002 et 2022 (Insee Première n° 1929, figure 3). Champ : inscrits résidant en France métropolitaine.","unite":" %","pasX":2,"h":280,"min":0,"max":70,"x":["18-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90+"],"series":[{"n":"2002","c":3,"v":[32.5,30.1,35.3,42.9,46.5,52,54.5,57.2,59.4,60.3,60,56.8,55.8,40,23.5]},{"n":"2022","c":1,"v":[16.7,18.1,19.9,26.7,32.7,40.5,42.5,45.6,47.6,48.2,53.7,54.1,48.8,37.1,21.4]}]},"s5-dipl":{"type":"hbarres","t":"Diplôme et participation électorale, 2022","s":"Inscrits non étudiants selon leur diplôme, en %.","src":"Source : Insee, enquête sur la participation électorale 2022 (Insee Première n° 1929, figure 5). Champ : inscrits hors étudiants, France métropolitaine.","unite":" %","lab":130,"cats":["Aucun diplôme","Diplôme inférieur au bac","Baccalauréat","Diplôme du supérieur"],"series":[{"n":"Vote systématique","v":[28.8,38.1,33.3,43.7],"c":1},{"n":"Abstention systématique","v":[30.4,18,15.2,9.5],"c":2}]},"s5-pcs":{"type":"hbarres","t":"Abstention systématique selon la catégorie sociale, 2022","s":"Part des inscrits de 25 ans ou plus qui n’ont voté à aucun tour, en %.","src":"Source : Insee, enquête sur la participation électorale 2022 (Insee Première n° 1929, tableau complémentaire 4). Champ : inscrits de 25 ans ou plus, France métropolitaine.","unite":" %","lab":150,"cats":["Agriculteurs exploitants","Artisans, commerçants, chefs d’entreprise","Cadres","Professions intermédiaires","Employés","Ouvriers","Retraités"],"series":[{"n":"2022","v":[8.5,10.6,6.8,11.1,15.7,19.7,16.4],"c":2}]}};
/* Moteur des animations explicatives.
   Une animation se déclare dans un fichier de données :
     ANIMS["id"] = {
       t: "Titre",                       // affiché au-dessus de la scène
       h: 300,                           // hauteur de la scène (largeur fixe : 360)
       src: "Source : …",                // facultatif, sous la scène
       etapes: [{ l: "légende de l'étape", d: 4 }, …],   // d = durée en secondes (3,5 par défaut)
       rendu: function (A, i, p) { return "<svg…>" }      // i = étape (0…n−1), p = avancement 0…1 de l'étape
     };
   et se place dans le cours par <div data-anim="id"></div>.
   rendu est une fonction pure : elle dessine tout l'état à l'instant (i, p). Les étapes antérieures sont
   considérées comme terminées (p = 1). Outils A : voir plus bas (A.s, A.t, A.boite, A.fl, A.pl, A.axes…).
   Sans mouvement (prefers-reduced-motion), chaque étape s'affiche directement terminée. */
var ANIM_MOTEUR = (function () {
  "use strict";
  var W = 360;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fr(n, d) {
    if (!isFinite(n)) return "—";
    var s = Math.abs(n).toFixed(d === undefined ? 1 : d), p = s.split(".");
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return (n < 0 && +s !== 0 ? "−" : "") + p.join(",");
  }
  var ctx = null, famille = "";
  function larg(t, taille, gras) {
    if (!ctx) { ctx = document.createElement("canvas").getContext("2d"); famille = getComputedStyle(document.body).fontFamily; }
    ctx.font = (gras ? "700 " : "") + taille + "px " + famille; return ctx.measureText(t).width;
  }
  function couper(t, w, taille, gras) {
    var out = [], cur = "";
    String(t).split(" ").forEach(function (m) {
      var e = cur ? cur + " " + m : m;
      if (larg(e, taille, gras) > w && cur) { out.push(cur); cur = m; } else cur = e;
    });
    if (cur) out.push(cur);
    return out;
  }
  function borne(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function ease(p) { p = borne(p); return p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2; }
  var COUL = { canard: "var(--canard)", corail: "var(--corail)", moutarde: "var(--moutarde)", encre: "var(--encre)", gris: "var(--encre2)", vert: "var(--vert)", ligne: "var(--ligne)", carte: "var(--carte)", papier: "var(--papier)", canardc: "var(--canard-c)", corailc: "var(--corail-c)", moutardec: "var(--moutarde-c)", carte2: "var(--carte2)" };
  function c(n) { return COUL[n] || n; }
  /* couleurs de texte : corail et moutarde foncés en thème clair (contraste AA sur le papier) */
  var COUL_T = { corail: "var(--corail-t)", moutarde: "var(--moutarde-t)" };
  function ct(n) { return COUL_T[n] || c(n); }

  var A = {
    W: W, fr: fr, esc: esc,
    /* avancement d'un sous-intervalle [a, b] de p, adouci */
    s: function (p, a, b) { return ease((p - a) / ((b === undefined ? 1 : b) - a)); },
    l: function (a, b, t) { return a + (b - a) * t; },
    /* texte : o = { t: taille, g: gras, c: couleur, a: "start|middle|end", op: opacité, it: italique, w: largeur max (retour à la ligne) } */
    t: function (x, y, txt, o) {
      o = o || {}; var t = o.t || 13, lignes = o.w ? couper(txt, o.w, t, o.g) : [String(txt)];
      var dy = o.v ? -(lignes.length - 1) * t * 0.6 : 0;
      return '<text x="' + x + '" y="' + (y + dy) + '" text-anchor="' + (o.a || "start") + '" style="font-size:' + t + "px;" + (o.g ? "font-weight:700;" : "") + (o.it ? "font-style:italic;" : "") + "fill:" + ct(o.c || "encre") + ";opacity:" + (o.op === undefined ? 1 : o.op) + (o.f ? ";font-family:var(--titre);font-stretch:condensed" : "") + (o.h ? ";paint-order:stroke;stroke:var(--carte);stroke-width:4px;stroke-linejoin:round" : "") + '">' +
        lignes.map(function (l, k) { return '<tspan x="' + x + '" dy="' + (k ? t * 1.2 : 0) + '">' + esc(l) + "</tspan>"; }).join("") + "</text>";
    },
    /* rectangle : o = { f: remplissage, s: trait, r: arrondi, op, sw } */
    r: function (x, y, w, h, o) {
      o = o || {};
      return '<rect x="' + x + '" y="' + y + '" width="' + Math.max(0, w) + '" height="' + Math.max(0, h) + '" rx="' + (o.r === undefined ? 4 : o.r) + '" style="fill:' + c(o.f || "carte") + ";stroke:" + (o.s ? c(o.s) : "none") + ";stroke-width:" + (o.sw || 1.5) + ";opacity:" + (o.op === undefined ? 1 : o.op) + '"/>';
    },
    cercle: function (x, y, r, o) {
      o = o || {};
      return '<circle cx="' + x + '" cy="' + y + '" r="' + Math.max(0, r) + '" style="fill:' + c(o.f || "canard") + ";stroke:" + (o.s ? c(o.s) : "none") + ";stroke-width:" + (o.sw || 1.5) + ";opacity:" + (o.op === undefined ? 1 : o.op) + '"/>';
    },
    /* boîte avec texte centré : o = { k: "cause|meca|effet|frein|neutre", t: taille, op } */
    boite: function (x, y, w, h, txt, o) {
      o = o || {};
      var k = o.k || "meca", t = o.t || 12.5;
      var st = { cause: ["canard", "canard", "carte"], meca: ["carte", "canard", "encre"], effet: ["corailc", "corail", "encre"], frein: ["moutardec", "moutarde", "encre"], neutre: ["carte2", "ligne", "encre"] }[k];
      var lignes = couper(txt, w - 12, t, o.g), lh = t * 1.22, y0 = y + h / 2 - (lignes.length - 1) * lh / 2 + t * 0.36;
      return '<g style="opacity:' + (o.op === undefined ? 1 : o.op) + '">' + A.r(x, y, w, h, { f: st[0], s: st[1], r: 8 }) +
        lignes.map(function (l, j) { return '<text x="' + (x + w / 2) + '" y="' + (y0 + j * lh) + '" text-anchor="middle" style="font-size:' + t + "px;fill:" + c(st[2]) + (o.g ? ";font-weight:700" : "") + '">' + esc(l) + "</text>"; }).join("") + "</g>";
    },
    /* flèche de (x1, y1) à (x2, y2), tracée jusqu'à la fraction o.p ; o = { c, sw, p, op, tete } */
    fl: function (x1, y1, x2, y2, o) {
      o = o || {}; var p = o.p === undefined ? 1 : borne(o.p);
      if (p <= 0) return "";
      var x = x1 + (x2 - x1) * p, y = y1 + (y2 - y1) * p, a = Math.atan2(y2 - y1, x2 - x1), L = 7;
      var col = c(o.c || "gris");
      var s = '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x + '" y2="' + y + '" style="stroke:' + col + ";stroke-width:" + (o.sw || 1.8) + ";opacity:" + (o.op === undefined ? 1 : o.op) + (o.tir ? ";stroke-dasharray:4 3" : "") + '"/>';
      if (o.tete !== false) s += '<path d="M' + x + " " + y + "L" + (x - L * Math.cos(a - 0.45)) + " " + (y - L * Math.sin(a - 0.45)) + "L" + (x - L * Math.cos(a + 0.45)) + " " + (y - L * Math.sin(a + 0.45)) + 'z" style="fill:' + col + ";opacity:" + (o.op === undefined ? 1 : o.op) + '"/>';
      return s;
    },
    /* ligne brisée tracée jusqu'à la fraction p de sa longueur ; o = { c, sw, op, aire: y du bas pour remplir } */
    pl: function (pts, p, o) {
      o = o || {}; p = p === undefined ? 1 : borne(p);
      if (pts.length < 2 || p <= 0) return "";
      var long = 0, seg = [];
      for (var i = 1; i < pts.length; i++) { var d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(d); long += d; }
      var reste = long * p, out = [pts[0]];
      for (var j = 1; j < pts.length && reste > 0; j++) {
        if (seg[j - 1] <= reste) { out.push(pts[j]); reste -= seg[j - 1]; }
        else { var f = reste / seg[j - 1]; out.push([pts[j - 1][0] + (pts[j][0] - pts[j - 1][0]) * f, pts[j - 1][1] + (pts[j][1] - pts[j - 1][1]) * f]); reste = 0; }
      }
      var d2 = out.map(function (q, k) { return (k ? "L" : "M") + q[0].toFixed(1) + " " + q[1].toFixed(1); }).join("");
      var s = "";
      if (o.aire !== undefined) s += '<path d="' + d2 + "L" + out[out.length - 1][0].toFixed(1) + " " + o.aire + "L" + out[0][0].toFixed(1) + " " + o.aire + 'z" style="fill:' + c(o.c || "canard") + ';opacity:.13"/>';
      s += '<path d="' + d2 + '" style="fill:none;stroke:' + c(o.c || "canard") + ";stroke-width:" + (o.sw || 2.6) + ";stroke-linejoin:round;stroke-linecap:round;opacity:" + (o.op === undefined ? 1 : o.op) + (o.tir ? ";stroke-dasharray:5 4" : "") + '"/>';
      return s;
    },
    /* axes : origine (x0, y0), largeur w, hauteur h ; o = { lx, ly : libellés } */
    axes: function (x0, y0, w, h, o) {
      o = o || {};
      var s = A.fl(x0, y0, x0 + w, y0, { c: "gris", sw: 1.3 }) + A.fl(x0, y0, x0, y0 - h, { c: "gris", sw: 1.3 });
      if (o.lx) s += A.t(x0 + w, y0 + 16, o.lx, { t: 11, a: "end", c: "gris" });
      if (o.ly) s += A.t(x0 + 6, y0 - h + 4, o.ly, { t: 11, c: "gris" });
      return s;
    },
    g: function (op, contenu, tr) { return '<g style="opacity:' + borne(op) + '"' + (tr ? ' transform="' + tr + '"' : "") + ">" + contenu + "</g>"; },
    /* pastille numérotée */
    puce: function (x, y, n, o) { o = o || {}; return A.cercle(x, y, 10, { f: o.f || "corail", op: o.op }) + A.t(x, y + 4, n, { t: 11, g: true, a: "middle", c: "carte", op: o.op }); },
    /* jauge horizontale de valeur v entre 0 et max */
    jauge: function (x, y, w, v, max, o) {
      o = o || {};
      return A.r(x, y, w, 10, { f: "carte2", r: 5 }) + A.r(x, y, w * borne(v / max), 10, { f: o.c || "corail", r: 5 }) +
        (o.l ? A.t(x, y - 5, o.l, { t: 11, c: "gris" }) : "") + (o.val ? A.t(x + w, y - 5, o.val, { t: 11, g: true, a: "end" }) : "");
    }
  };

  function mouvement() {
    return document.documentElement.classList.contains("mo") && !(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  }
  var IC_LECT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>';
  var IC_PAUSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM13 5h4v14h-4z" fill="currentColor"/></svg>';
  var IC_PREC = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM20 5v14L9 12z" fill="currentColor"/></svg>';
  var IC_SUIV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM4 5v14l11-7z" fill="currentColor"/></svg>';
  var IC_ZERO = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 12a8 8 0 1 0 2.4-5.7"/><path d="M4 4v4h4"/></svg>';

  var actives = [];
  function monterUne(d) {
    var id = d.getAttribute("data-anim"), an = ANIMS[id];
    if (!an) return;
    var n = an.etapes.length, H = an.h || 300;
    d.className = "anim";
    d.innerHTML = '<div class="an-tete"><span class="an-k">Animation</span><span class="an-t">' + esc(an.t) + "</span></div>" +
      '<div class="an-scene"><svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(an.t) + '"></svg></div>' +
      '<div class="an-leg" aria-live="polite"><span class="an-n"></span><span class="an-l"></span></div>' +
      '<div class="an-barre" role="group" aria-label="Étapes">' + an.etapes.map(function (e, k) { return '<button type="button" data-k="' + k + '" aria-label="Étape ' + (k + 1) + '"><i></i></button>'; }).join("") + "</div>" +
      '<div class="an-cmd"><button type="button" class="an-b" data-a="prec" aria-label="Étape précédente">' + IC_PREC + '</button><button type="button" class="an-b an-jouer" data-a="jouer" aria-label="Lecture">' + IC_LECT + '</button><button type="button" class="an-b" data-a="suiv" aria-label="Étape suivante">' + IC_SUIV + '</button><button type="button" class="an-b" data-a="zero" aria-label="Recommencer">' + IC_ZERO + "</button></div>" +
      '<details class="an-txt"><summary>Le déroulé en texte</summary><ol>' + an.etapes.map(function (e) { return "<li>" + esc(e.l) + "</li>"; }).join("") + "</ol></details>" +
      (an.src ? '<p class="src-l">' + an.src + "</p>" : "");
    var svg = d.querySelector("svg"), leg = d.querySelector(".an-l"), num = d.querySelector(".an-n"), bJ = d.querySelector(".an-jouer");
    var segs = Array.prototype.slice.call(d.querySelectorAll(".an-barre button"));
    var etat = { i: 0, p: mouvement() ? 0 : 1, joue: false, attente: 0, dernier: 0, vu: false };
    function duree(k) { return (an.etapes[k].d || 3.5) * 1000; }
    function dessiner() {
      var s;
      try { s = an.rendu(A, etat.i, etat.p); } catch (e) { s = ""; }
      svg.innerHTML = s;
      segs.forEach(function (b, k) { b.querySelector("i").style.width = (k < etat.i ? 100 : k === etat.i ? etat.p * 100 : 0) + "%"; b.classList.toggle("act", k === etat.i); });
    }
    function legende(anim) {
      num.textContent = "Étape " + (etat.i + 1) + " / " + n;
      leg.textContent = an.etapes[etat.i].l;
      if (anim && mouvement()) { leg.classList.remove("vient"); void leg.offsetWidth; leg.classList.add("vient"); }
    }
    function majBouton() { bJ.innerHTML = etat.joue ? IC_PAUSE : IC_LECT; bJ.setAttribute("aria-label", etat.joue ? "Pause" : "Lecture"); d.classList.toggle("joue", etat.joue); }
    function aller(k, depart) {
      etat.i = Math.max(0, Math.min(n - 1, k));
      etat.p = depart && mouvement() ? 0 : 1; etat.attente = 0;
      legende(true); dessiner();
    }
    function boucle(t) {
      if (!etat.joue) return;
      var dt = Math.min(100, Math.max(0, t - (etat.dernier || t))); etat.dernier = t;
      if (etat.p < 1) { etat.p = Math.min(1, etat.p + dt / duree(etat.i)); dessiner(); }
      else {
        etat.attente += dt;
        if (etat.attente > 1500) {
          if (etat.i < n - 1) { aller(etat.i + 1, true); }
          else { etat.joue = false; majBouton(); return; }
        }
      }
      requestAnimationFrame(boucle);
    }
    function jouer() {
      if (!mouvement()) { if (etat.i < n - 1) aller(etat.i + 1, false); return; }
      if (etat.i === n - 1 && etat.p >= 1) aller(0, true);
      etat.joue = true; etat.dernier = 0; majBouton(); requestAnimationFrame(boucle);
    }
    function pause() { etat.joue = false; majBouton(); }
    d.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      var a = b.getAttribute("data-a");
      if (b.hasAttribute("data-k")) { pause(); aller(+b.getAttribute("data-k"), false); return; }
      if (a === "jouer") { if (etat.joue) pause(); else jouer(); }
      else if (a === "suiv") { aller(etat.i + 1, etat.joue); }
      else if (a === "prec") { pause(); aller(etat.i - 1, false); }
      else if (a === "zero") { pause(); aller(0, true); if (mouvement()) jouer(); }
    });
    legende(false); dessiner(); majBouton();
    var obj = { d: d, demarrer: function () { if (!etat.vu && mouvement()) { etat.vu = true; jouer(); } }, pause: pause, joue: function () { return etat.joue; } };
    actives.push(obj);
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (en) {
        en.forEach(function (x) {
          if (x.isIntersecting && x.intersectionRatio > 0.45) obj.demarrer();
          else if (!x.isIntersecting && etat.joue) pause();
        });
      }, { threshold: [0, 0.45, 0.8] });
      io.observe(d);
    }
  }
  return {
    A: A,
    monter: function (racine) {
      actives.forEach(function (o) { o.pause(); });
      actives = [];
      Array.prototype.slice.call((racine || document).querySelectorAll("[data-anim]")).forEach(monterUne);
    }
  };
})();

ANIMS["e1-solow"] = {
  t: "Pourquoi le progrès technique est indispensable",
  h: 300,
  src: "Schéma de principe (fonction de production à rendements décroissants, valeurs illustratives). Résidu : R. Solow, 1957, données des États-Unis 1909-1949.",
  etapes: [
    { l: "Avec plus de capital par travailleur (machines, outils, logiciels), chacun produit davantage : c’est la fonction de production.", d: 3.5 },
    { l: "Mais les rendements sont décroissants : chaque nouvelle machine rapporte moins que la précédente.", d: 4.5 },
    { l: "Accumuler du capital seul mène à un plafond : la production par travailleur augmente de moins en moins (modèle de Solow, 1956).", d: 4 },
    { l: "Le progrès technique déplace toute la courbe vers le haut : avec le même capital, on produit plus. C’est la hausse de la productivité globale des facteurs.", d: 4 },
    { l: "Ce supplément qui ne vient pas des facteurs, Solow l’appelle le « résidu » : environ 87,5 % de la hausse de la production par heure aux États-Unis de 1909 à 1949.", d: 3.5 }
  ],
  rendu: function (A, i, p) {
    var x0 = 46, y0 = 262, X = function (k) { return x0 + k * 29; }, Y = function (v) { return y0 - v * 60; };
    function f(k, a) { return a * Math.pow(k, 0.4); }
    function courbe(a) { var pts = []; for (var k = 0; k <= 10.001; k += 0.25) pts.push([X(k), Y(f(k, a))]); return pts; }
    var s = A.axes(x0, y0, 300, 236, { lx: "capital par travailleur", ly: "production par travailleur" });
    var pa = i === 0 ? p : 1;
    s += A.pl(courbe(1), pa, { c: i >= 3 ? "gris" : "canard", tir: i >= 3, sw: i >= 3 ? 1.8 : 2.8 });
    if (i === 0) s += A.t(X(9.4), Y(f(9.4, 1)) - 10, "fonction de production", { t: 11.5, a: "end", c: "canard", op: A.s(p, 0.6, 1) });
    if (i >= 1) {
      var marches = [[1, 3], [3, 5], [5, 7], [7, 9]];
      marches.forEach(function (m, j) {
        var q = i === 1 ? A.s(p, j * 0.22, j * 0.22 + 0.3) : 1;
        if (q <= 0) return;
        var ya = Y(f(m[0], 1)), yb = Y(f(m[1], 1)), op = i >= 3 ? 0.35 : 1;
        s += A.g(op, A.fl(X(m[0]), ya, X(m[0]) + (X(m[1]) - X(m[0])) * q, ya, { c: "gris", sw: 1.2, tete: false }) +
          (q > 0.5 ? A.r(X(m[1]) - 3, yb, 6, (ya - yb) * A.s(q, 0.5, 1), { f: "corail", r: 2 }) : "") +
          A.t(X(m[1]) + 6, (ya + yb) / 2 + 4, "+" + A.fr(f(m[1], 1) - f(m[0], 1), 2), { t: 10.5, g: true, c: "corail", op: A.s(q, 0.7, 1) }));
      });
      if (i === 1) s += A.t(X(3.2), Y(0.75), "même ajout de capital, gain de production qui diminue", { t: 11, c: "corail", op: A.s(p, 0.85, 1), w: 190, h: true });
    }
    if (i === 2) {
      var k = A.l(2, 9, A.s(p, 0, 0.9));
      s += A.cercle(X(k), Y(f(k, 1)), 7, { f: "corail", s: "carte", sw: 2 });
      s += A.t(X(5.5), Y(0.45), "la croissance s’essouffle", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.6, 1) });
    }
    if (i >= 3) {
      var a = i === 3 ? A.l(1, 1.35, A.s(p, 0, 0.8)) : 1.35;
      s += A.pl(courbe(a), 1, { c: "canard", sw: 2.8 });
      var yh = Y(f(9, a));
      s += A.cercle(X(9), yh, 7, { f: "corail", s: "carte", sw: 2 });
      s += A.t(X(0.6), Y(2.75), "après progrès technique", { t: 11.5, c: "canard", g: true, op: i === 3 ? A.s(p, 0.6, 1) : 1, h: true });
      s += A.fl(X(4), Y(f(4, 1)) - 4, X(4), Y(f(4, a)) + 6, { c: "canard", sw: 2, op: i === 3 ? A.s(p, 0.3, 0.7) : 1 });
    }
    if (i === 4) {
      var ya1 = Y(f(9, 1)), ya2 = Y(f(9, 1.35)), q = A.s(p, 0, 0.6);
      s += A.r(X(9) - 22, ya2, 44, (ya1 - ya2) * q, { f: "moutarde", op: 0.35, r: 3 });
      s += A.t(X(5.6), Y(0.9), "PGF : le « résidu »", { t: 13, g: true, a: "middle", c: "encre", op: A.s(p, 0.4, 1), h: true });
      s += A.fl(X(6.6), Y(0.98), X(9) - 22, (ya1 + ya2) / 2 + 6, { c: "moutarde", sw: 2, p: A.s(p, 0.5, 1) });
    }
    return s;
  }
};

ANIMS["e1-pib"] = {
  t: "75 ans de croissance française, année par année",
  h: 290,
  src: "Source : Insee, comptes nationaux annuels, base 2020 (mai 2026). Taux de croissance du PIB en volume ; moyennes calculées à partir des niveaux.",
  etapes: [
    { l: "1950-1973, les « Trente Glorieuses » : la France rattrape son retard, la croissance dépasse souvent 5 % (5,2 % par an en moyenne).", d: 5, de: 1950, a: 1973 },
    { l: "Les chocs pétroliers : en 1975, le PIB recule (−0,9 %). La croissance ne retrouvera plus ce rythme.", d: 2.5, de: 1974, a: 1975 },
    { l: "1976-2007 : une croissance ralentie et heurtée (2,4 % par an en moyenne de 1973 à 2007), avec une récession en 1993 (−0,4 %).", d: 5, de: 1976, a: 2007 },
    { l: "La crise financière : −2,8 % en 2009, la plus forte récession depuis 1950 jusque-là.", d: 2.5, de: 2008, a: 2009 },
    { l: "Les années 2010 : une croissance faible, 1,4 % par an en moyenne de 2010 à 2019.", d: 4, de: 2010, a: 2019 },
    { l: "Covid : −7,4 % en 2020, rebond de +6,9 % en 2021, puis +1,6 %, +1,5 % et +0,8 % de 2023 à 2025.", d: 4, de: 2020, a: 2025 }
  ],
  rendu: function (A, i, p) {
    var g = GRAPHES["e1-pib"], xs = g.x, ys = g.y, n = xs.length;
    var x0 = 34, w = 316, yz = 158, sc = 12, bw = w / n;
    var Y = function (v) { return yz - v * sc; };
    var s = "";
    [-8, -4, 0, 4, 8].forEach(function (t) { s += '<line x1="' + x0 + '" x2="' + (x0 + w) + '" y1="' + Y(t) + '" y2="' + Y(t) + '" style="stroke:var(--' + (t === 0 ? "encre2" : "ligne") + ');stroke-width:1"/>' + A.t(x0 - 5, Y(t) + 4, (t > 0 ? "+" : "") + t + " %", { t: 10.5, a: "end", c: "gris" }); });
    [1950, 1970, 1990, 2010, 2025].forEach(function (yr) { s += A.t(x0 + (yr - 1950 + 0.5) * bw, 282, String(yr), { t: 10.5, a: "middle", c: "gris" }); });
    var etapes = this.etapes;
    var et = etapes[i], fin = et.a, debut = et.de, nb = fin - debut + 1;
    var courant = debut + (nb) * p;
    if (i >= 0) {
      var bande = etapes[i];
      s += A.r(x0 + (bande.de - 1950) * bw, 10, (bande.a - bande.de + 1) * bw, 255, { f: "moutardec", op: 0.6, r: 0 });
    }
    for (var k = 0; k < n; k++) {
      var yr = xs[k], q;
      if (yr < debut) q = 1; else if (yr > fin) q = 0; else q = Math.max(0, Math.min(1, courant - yr));
      if (q <= 0) continue;
      var v = ys[k] * A.s(q, 0, 1), y1 = Y(Math.max(0, v)), y2 = Y(Math.min(0, v));
      s += A.r(x0 + k * bw + 0.5, y1, bw - 1, Math.max(0.6, y2 - y1), { f: ys[k] < 0 ? "corail" : "canard", r: 1 });
    }
    var dernier = Math.min(fin, Math.floor(courant));
    if (dernier >= debut) {
      var kk = dernier - 1950, val = ys[kk];
      s += A.t(x0 + (kk + 0.5) * bw, val >= 0 ? Y(val) - 6 : Y(val) + 14, String(dernier) + " : " + (val > 0 ? "+" : "") + A.fr(val, 1) + " %", { t: 11, g: true, a: kk > 60 ? "end" : kk < 6 ? "start" : "middle", c: val < 0 ? "corail" : "encre", h: true });
    }
    return s;
  }
};

ANIMS["e1-gains"] = {
  t: "Où vont les gains de productivité ?",
  h: 320,
  src: "Schéma de principe (chiffres illustratifs).",
  etapes: [
    { l: "Une usine produit 100 objets par jour avec 10 salariés : 10 objets par salarié et par jour.", d: 3 },
    { l: "Une nouvelle machine (progrès technique) : les mêmes 10 salariés produisent 125 objets. La productivité du travail augmente de 25 %.", d: 3.5 },
    { l: "Chaque objet coûte moins cher à produire : l’entreprise dispose d’un surplus à partager.", d: 3 },
    { l: "Ce surplus peut aller aux consommateurs (prix plus bas), aux salariés (salaires plus élevés) et à l’entreprise (profits pour investir).", d: 4 },
    { l: "Chacun dépense ou investit davantage : la demande augmente, il faut produire plus et embaucher. Les gains de productivité nourrissent la croissance.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "";
    function salarie(x, y, op, c) { return A.cercle(x, y - 9, 5, { f: c || "canard", op: op }) + A.r(x - 6, y - 3, 12, 13, { f: c || "canard", r: 4, op: op }); }
    s += A.t(20, 24, "Salariés", { t: 12, g: true, c: "gris" });
    var nb = 10 + (i === 4 ? Math.round(3 * A.s(p, 0.4, 1)) : 0);
    for (var k = 0; k < nb; k++) s += salarie(30 + k * 24, 54, 1, k >= 10 ? "vert" : "canard");
    s += A.t(20, 96, "Production par jour", { t: 12, g: true, c: "gris" });
    var prod = i === 0 ? 100 : i === 1 ? A.l(100, 125, A.s(p, 0.1, 0.8)) : (i === 4 ? A.l(125, 160, A.s(p, 0.3, 1)) : 125);
    s += A.r(20, 104, prod * 1.65, 26, { f: "canard", r: 4 }) + A.t(26 + prod * 1.65, 122, A.fr(prod, 0) + " objets", { t: 12.5, g: true });
    if (i >= 1) s += A.t(20, 148, "productivité : " + A.fr(prod / nb, 1) + " objets par salarié", { t: 12, c: "canard", g: true, op: i === 1 ? A.s(p, 0.5, 1) : 1 });
    if (i >= 2) {
      var q = i === 2 ? A.s(p, 0, 0.6) : 1;
      s += A.boite(120, 164, 120, 38, "surplus à partager", { k: "frein", t: 12.5, g: true, op: q });
    }
    if (i >= 3) {
      var parts = [["Consommateurs : prix ↓", 20], ["Salariés : salaires ↑", 130], ["Entreprise : profits ↑", 240]];
      parts.forEach(function (pt, k) {
        var q2 = i === 3 ? A.s(p, k * 0.2, 0.5 + k * 0.2) : 1;
        s += A.fl(180, 204, pt[1] + 50, 236, { c: "corail", sw: 2, p: q2 });
        s += A.boite(pt[1], 240, 100, 40, pt[0], { k: "effet", t: 11.5, op: q2 });
      });
    }
    if (i === 4) s += A.t(180, 304, "plus de demande → plus de production → embauches", { t: 12.5, g: true, a: "middle", c: "vert", op: A.s(p, 0.2, 0.7) });
    return s;
  }
};

ANIMS["e2-ricardo"] = {
  t: "L’avantage comparatif se construit",
  h: 345,
  src: "Exemple de David Ricardo, <i>Des principes de l’économie politique et de l’impôt</i>, 1817 (heures de travail pour une unité de chaque bien).",
  etapes: [
    { l: "Heures de travail pour produire une unité : en Angleterre, 100 h pour le drap et 120 h pour le vin ; au Portugal, 90 h et 80 h.", d: 3.5 },
    { l: "Le Portugal est plus productif dans les deux biens : il a un avantage absolu partout. L’échange serait-il inutile ?", d: 3 },
    { l: "Comparons les coûts relatifs. En Angleterre, un drap coûte 100/120 = 0,83 vin ; au Portugal, 90/80 = 1,125 vin. L’Angleterre a un avantage comparatif en drap, le Portugal en vin.", d: 4.5 },
    { l: "Sans échange, chaque pays produit une unité de chaque bien : le monde dispose de 2 draps et de 2 vins.", d: 3 },
    { l: "Chacun se spécialise : l’Angleterre met ses 220 h dans le drap (2,2 draps), le Portugal ses 170 h dans le vin (2,125 vins).", d: 4 },
    { l: "Avec le même travail, le monde produit 0,2 drap et 0,125 vin de plus. L’échange partage ce gain : les deux pays y gagnent.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", pays = [{ n: "Angleterre", x: 12, h: [100, 120], aut: [1, 1], spe: [2.2, 0] }, { n: "Portugal", x: 186, h: [90, 80], aut: [1, 1], spe: [0, 2.125] }];
    var biens = [{ n: "drap", c: "canard" }, { n: "vin", c: "corail" }];
    pays.forEach(function (P, j) {
      s += A.t(P.x + 81, 20, P.n, { t: 15, g: true, a: "middle", f: true });
      s += '<line x1="' + P.x + '" x2="' + (P.x + 162) + '" y1="28" y2="28" style="stroke:var(--encre);stroke-width:2"/>';
      biens.forEach(function (b, k) {
        var y = 44 + k * 30, q = i === 0 ? A.s(p, k * 0.3 + j * 0.15, k * 0.3 + j * 0.15 + 0.5) : 1;
        var hl = (i === 1 && j === 1) ? 1 : 0;
        s += A.t(P.x, y + 13, b.n, { t: 11.5, c: "gris" });
        s += A.r(P.x + 34, y, P.h[k] * 0.8 * q, 18, { f: b.c, op: i === 1 && j === 0 ? 0.45 : 1, s: hl ? "moutarde" : null, sw: 3 });
        s += A.t(P.x + 40 + P.h[k] * 0.8 * q, y + 13, A.fr(P.h[k] * q, 0) + " h", { t: 11.5, g: true, op: q });
      });
      if (i === 1 && j === 1) s += A.t(P.x + 81, 120, "avantage absolu dans les deux biens", { t: 11.5, g: true, a: "middle", c: "moutarde", op: A.s(p, 0.3, 0.8), w: 150 });
      if (i >= 2) {
        var ratio = P.h[0] / P.h[1], q2 = i === 2 ? A.s(p, j * 0.3, j * 0.3 + 0.5) : 1;
        s += A.t(P.x + 81, 120, "1 drap = " + A.fr(ratio, ratio === 1.125 ? 3 : 2) + " vin", { t: 13, g: true, a: "middle", op: q2 });
        s += A.t(P.x + 81, 138, j === 0 ? "avantage comparatif : drap" : "avantage comparatif : vin", { t: 11.5, a: "middle", c: j === 0 ? "canard" : "corail", g: true, op: i === 2 ? A.s(p, 0.6 + j * 0.15, 0.95) : 1 });
      }
      if (i >= 3) {
        var q3 = i === 3 ? A.s(p, 0, 0.6) : 1, t4 = i === 4 ? A.s(p, 0.1, 0.8) : (i > 4 ? 1 : 0);
        s += A.g(q3, A.t(P.x, 172, "Production", { t: 11, c: "gris", g: true }));
        biens.forEach(function (b, k) {
          var qte = A.l(P.aut[k], P.spe[k], t4), y = 180 + k * 28;
          s += A.g(q3, A.t(P.x, y + 13, b.n, { t: 11.5, c: "gris" }) + A.r(P.x + 34, y, qte * 46, 18, { f: b.c }) + (qte > 0.02 ? A.t(P.x + 40 + qte * 46, y + 13, A.fr(qte, Math.abs(qte - 2.125) < 1e-9 ? 3 : (Math.abs(qte * 10 - Math.round(qte * 10)) < 1e-9 ? (qte % 1 ? 1 : 0) : 2)), { t: 11.5, g: true }) : ""));
        });
      }
    });
    if (i >= 3) {
      var t4b = i === 4 ? A.s(p, 0.1, 0.8) : (i > 4 ? 1 : 0), q3b = i === 3 ? A.s(p, 0.4, 1) : 1;
      var dr = A.l(2, 2.2, t4b), vi = A.l(2, 2.125, t4b);
      s += A.g(q3b, A.r(12, 244, 336, 34, { f: "carte2", r: 8 }) + A.t(180, 266, "Monde : " + A.fr(dr, dr === 2 ? 0 : (dr > 2.19 ? 1 : 2)) + " draps et " + A.fr(vi, vi === 2 ? 0 : 3) + " vins", { t: 14, g: true, a: "middle" }));
    }
    if (i === 5) {
      s += A.fl(70, 296, 290, 296, { c: "canard", sw: 2.4, p: A.s(p, 0, 0.4) }) + A.t(180, 291, "drap anglais", { t: 11, a: "middle", c: "canard", g: true, op: A.s(p, 0.2, 0.4), h: true });
      s += A.fl(290, 312, 70, 312, { c: "corail", sw: 2.4, p: A.s(p, 0.2, 0.6) }) + A.t(180, 325, "vin portugais", { t: 11, a: "middle", c: "corail", g: true, op: A.s(p, 0.4, 0.6), h: true });
      s += A.t(180, 342, "gain : +0,2 drap et +0,125 vin, à partager par l’échange", { t: 12.5, g: true, a: "middle", c: "encre", op: A.s(p, 0.6, 1) });
    }
    return s;
  }
};

ANIMS["e2-iphone"] = {
  t: "Le voyage d’un iPhone 3G (2009)",
  h: 300,
  src: "Source : Y. Xing et N. Detert, ADBI Working Paper n° 257, décembre 2010, d’après des estimations d’iSuppli (2009). Coût de fabrication : 178,96 $, dont 6,50 $ d’assemblage en Chine.",
  etapes: [
    { l: "Apple conçoit l’iPhone aux États-Unis. Ses composants viennent de fournisseurs de plusieurs pays : Japon, Allemagne, Corée du Sud, États-Unis…", d: 3 },
    { l: "Les composants, 172,46 $ par appareil, sont expédiés vers l’usine d’assemblage en Chine.", d: 3.5 },
    { l: "En Chine, l’usine assemble le téléphone : 6,50 $ de valeur ajoutée, soit 3,6 % du coût de fabrication.", d: 3.5 },
    { l: "L’iPhone part vers les États-Unis : la statistique douanière enregistre une importation de 178,96 $ en provenance de Chine.", d: 3.5 },
    { l: "En valeur ajoutée, la Chine n’a produit que 6,50 $ sur 178,96 $. Le commerce mesuré en valeur brute exagère son rôle : d’où le commerce en valeur ajoutée.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", four = ["Japon", "Allemagne", "Corée du Sud", "États-Unis"];
    four.forEach(function (n, k) {
      var q = i === 0 ? A.s(p, k * 0.18, k * 0.18 + 0.4) : 1;
      s += A.boite(6, 18 + k * 46, 96, 36, n, { k: "neutre", op: q, t: 12 });
    });
    s += A.t(54, 205, "fournisseurs", { t: 10.5, a: "middle", c: "gris", op: i === 0 ? A.s(p, 0.7, 1) : 1 });
    var chine = i >= 1 ? (i === 1 ? A.s(p, 0, 0.3) : 1) : 0;
    s += A.boite(146, 80, 84, 52, "Chine : assemblage", { k: i >= 2 ? "effet" : "meca", op: chine, t: 12.5, g: true });
    var us = i >= 3 ? (i === 3 ? A.s(p, 0, 0.3) : 1) : 0;
    s += A.boite(270, 80, 84, 52, "États-Unis : vente", { k: "cause", op: us, t: 12.5, g: true });
    if (i >= 1) {
      four.forEach(function (n, k) {
        var y = 36 + k * 46, q = i === 1 ? A.s(p, 0.15 + k * 0.1, 0.65 + k * 0.1) : 1;
        s += A.fl(104, y, 144, 106, { c: "gris", p: q, sw: 1.4 });
        if (i === 1 && q > 0 && q < 1) s += A.r(104 + 40 * q - 5, y + (106 - y) * q - 5, 10, 10, { f: "canard", r: 2 });
      });
    }
    if (i >= 3) {
      var q3 = i === 3 ? A.s(p, 0.2, 0.8) : 1;
      s += A.fl(232, 106, 268, 106, { c: "corail", sw: 2.4, p: q3 });
      if (i === 3) s += A.t(352, 160, "importation : 178,96 $", { t: 12, g: true, a: "end", c: "corail", op: A.s(p, 0.6, 1), h: true });
    }
    var x0 = 20, L = 320, sc = L / 178.96, yb = 238;
    if (i >= 1) {
      var qc = i === 1 ? A.s(p, 0.4, 1) : 1;
      s += A.t(x0, yb - 8, "Coût de fabrication d’un appareil", { t: 11, c: "gris", g: true });
      s += A.r(x0, yb, 172.46 * sc * qc, 26, { f: "canard", r: 3 });
      if (qc > 0.6) s += A.t(x0 + 8, yb + 17, "composants 172,46 $", { t: 12, g: true, c: "carte" });
    }
    if (i >= 2) {
      var qa = i === 2 ? A.s(p, 0.3, 0.8) : 1;
      s += A.r(x0 + 172.46 * sc, yb, 6.5 * sc * qa, 26, { f: "corail", r: 2 });
      s += A.t(x0 + L, yb + 44, "assemblage chinois : 6,50 $ (3,6 %)", { t: 12, g: true, a: "end", c: "corail", op: i === 2 ? A.s(p, 0.6, 1) : 1 });
    }
    if (i === 4) {
      s += A.r(x0 - 3, yb - 3, L + 6, 32, { f: "none", s: "moutarde", sw: 2.5, op: A.s(p, 0, 0.4) });
      s += A.t(352, 160, "valeur ajoutée chinoise : 3,6 %", { t: 13.5, g: true, a: "end", c: "corail", op: A.s(p, 0.2, 0.7), h: true });
      s += A.t(352, 178, "valeur brute comptée : 100 %", { t: 12, a: "end", c: "gris", op: A.s(p, 0.4, 0.9), h: true });
    }
    return s;
  }
};

/* Courbes qui se tracent année par année (utilitaire commun aux animations de séries) */
function ANIM_SERIES(A, x0, y0, w, h, xs, series, ymax, jusqua, opts) {
  opts = opts || {};
  var n = xs.length, X = function (k) { return x0 + w * k / (n - 1); }, Y = function (v) { return y0 - h * v / ymax; };
  var s = "";
  (opts.ticks || []).forEach(function (t) { s += '<line x1="' + x0 + '" x2="' + (x0 + w) + '" y1="' + Y(t) + '" y2="' + Y(t) + '" style="stroke:var(--ligne);stroke-width:1"/>' + A.t(x0 - 4, Y(t) + 4, t + (opts.u || ""), { t: 10.5, a: "end", c: "gris" }); });
  (opts.annees || []).forEach(function (yr) { var k = xs.indexOf(yr); if (k >= 0) s += A.t(X(k), y0 + 16, String(yr), { t: 10.5, a: "middle", c: "gris" }); });
  var kmax = Math.floor(jusqua), fr = jusqua - kmax, labs = [];
  series.forEach(function (sr) {
    var pts = [];
    for (var k = 0; k <= Math.min(kmax, n - 1); k++) pts.push([X(k), Y(sr.v[k])]);
    if (kmax < n - 1 && fr > 0) pts.push([X(kmax) + (X(kmax + 1) - X(kmax)) * fr, Y(sr.v[kmax] + (sr.v[kmax + 1] - sr.v[kmax]) * fr)]);
    if (pts.length < 2) pts.push(pts[0]);
    s += A.pl(pts, 1, { c: sr.c, sw: sr.sw || 2.4, op: sr.op });
    var der = pts[pts.length - 1], kv = Math.min(kmax, n - 1), val = kmax < n - 1 ? sr.v[kmax] + (sr.v[kmax + 1] - sr.v[kmax]) * fr : sr.v[n - 1];
    s += A.cercle(der[0], der[1], 3.6, { f: sr.c });
    if (sr.lab !== false) labs.push({ x: der[0] + 6, y: der[1] + 4 + (sr.dy || 0), t: (sr.court ? sr.court + " " : "") + A.fr(val, 1) + (opts.u || ""), c: sr.c });
  });
  /* étiquettes de fin de courbe : écartées d’au moins 12 px pour ne jamais se chevaucher */
  labs.sort(function (a, b) { return a.y - b.y; });
  for (var m = 1; m < labs.length; m++) if (labs[m].y - labs[m - 1].y < 12) labs[m].y = labs[m - 1].y + 12;
  labs.forEach(function (l) { s += A.t(l.x, l.y, l.t, { t: 10.5, g: true, c: l.c }); });
  return s;
}

ANIMS["s1-pcs"] = {
  t: "Quarante ans de transformations de l’emploi",
  h: 300,
  src: "Source : Insee, enquête Emploi 2024, séries longues (part de chaque catégorie dans l’emploi, en %). Ruptures de série liées aux changements de l’enquête.",
  etapes: [
    { l: "1982 : les ouvriers sont le premier groupe (29,9 % des personnes en emploi) ; les cadres ne sont que 8,0 %, les agriculteurs encore 7,5 %.", d: 3.5, a: 1990 },
    { l: "Années 1990 : la tertiarisation fait grimper les employés (près de 30 % de l’emploi) pendant que les ouvriers et les agriculteurs reculent.", d: 4, a: 2002 },
    { l: "Années 2000 : la montée des qualifications s’accélère. Les cadres passent de 14,7 % à 18,3 % de 2002 à 2012, les ouvriers tombent à 20,6 %.", d: 4, a: 2012 },
    { l: "2024 : 23,0 % de cadres et 18,0 % d’ouvriers. Pour la première fois depuis 1982, les professions intermédiaires (25,2 %) dépassent les employés (24,8 %).", d: 4.5, a: 2024 }
  ],
  rendu: function (A, i, p) {
    var g = GRAPHES["s1-pcs"], xs = g.x, debut = i === 0 ? 1982 : this.etapes[i - 1].a, fin = this.etapes[i].a;
    var jusqua = (debut - 1982) + (fin - debut) * (i === 0 ? A.s(p, 0, 1) : p);
    var noms = ["Agri.", "Artisans", "Cadres", "Prof. int.", "Employés", "Ouvriers"], dys = [6, -2, 0, -6, -6, 4];
    var ser = g.series.map(function (sr, k) { return { v: sr.v, c: ["vert", "gris", "corail", "moutarde", "#7B5EA7", "canard"][k], court: noms[k], dy: dys[k], sw: k === 2 || k === 5 ? 3 : 2 }; });
    var s = ANIM_SERIES(A, 34, 270, 232, 250, xs, ser, 32, jusqua, { ticks: [0, 10, 20, 30], u: " %", annees: [1982, 1990, 2000, 2010, 2024] });
    var an = Math.round(1982 + jusqua);
    s += A.t(300, 26, String(an), { t: 26, g: true, a: "middle", c: "encre", f: true, op: 0.85 });
    return s;
  }
};

ANIMS["s2-mass"] = {
  t: "Massification… et démocratisation ?",
  h: 300,
  src: "Sources : DEPP, proportion de bacheliers dans une génération (France hors DROM jusqu’en 2000, puis hors Mayotte) ; Observatoire des inégalités d’après le ministère, origine sociale des élèves de CPGE en 2023-2024.",
  etapes: [
    { l: "1970 : 20,1 % d’une génération obtient le bac. Le collège unique (1975) ouvre le secondaire à tous, la hausse reste lente.", d: 4, a: 1985 },
    { l: "1985 : objectif de 80 % d’une génération au niveau du bac et création du bac professionnel. En dix ans, la proportion passe de 29,4 % à 62,7 %.", d: 3.5, a: 1995 },
    { l: "1995-2008 : un palier autour de 62 %.", d: 3, a: 2008 },
    { l: "Réforme du bac professionnel en trois ans (2009) : nouvelle hausse, jusqu’à 80,1 % en 2025. C’est la massification.", d: 4, a: 2025 },
    { l: "Mais qui va où ? En classes préparatoires, 53,7 % des élèves sont enfants de cadres et 6,4 % enfants d’ouvriers : la démocratisation reste ségrégative.", d: 4.5 }
  ],
  rendu: function (A, i, p) {
    var g = GRAPHES["s2-bac"], xs = g.x, s = "";
    var fin = i < 4 ? this.etapes[i].a : 2025, debut = i === 0 ? 1970 : (i < 4 ? this.etapes[i - 1].a : 2025);
    var jusqua = (debut - 1970) + (fin - debut) * (i < 4 ? p : 1);
    var opC = i === 4 ? 1 - 0.75 * A.s(p, 0, 0.4) : 1;
    s += A.g(opC, ANIM_SERIES(A, 38, 270, 276, 240, xs, [{ v: g.series[0].v, c: "corail", sw: 3 }], 100, jusqua, { ticks: [0, 20, 40, 60, 80, 100], u: " %", annees: [1970, 1985, 1995, 2009, 2025] }));
    var jalons = [[1975, "collège unique"], [1985, "objectif 80 %, bac pro"], [2009, "bac pro en 3 ans"]];
    jalons.forEach(function (j) {
      var k = j[0] - 1970; if (k > jusqua) return;
      var x = 34 + 280 * k / (xs.length - 1);
      s += A.g(opC, '<line x1="' + x + '" x2="' + x + '" y1="40" y2="270" style="stroke:var(--moutarde);stroke-width:1.5;stroke-dasharray:3 3"/>' + A.t(x + 4, 48 + (j[0] === 1985 ? 16 : 0), j[1], { t: 10.5, g: true, c: "moutarde" }));
    });
    if (i === 4) {
      var q = A.s(p, 0.25, 0.75);
      s += A.r(20, 60, 320, 182, { f: "carte", s: "ligne", r: 12, op: A.s(p, 0.15, 0.4) });
      s += A.t(180, 86, "Élèves de classes préparatoires (2023-2024)", { t: 13, g: true, a: "middle", op: A.s(p, 0.2, 0.45) });
      s += A.t(36, 124, "enfants de cadres", { t: 12, c: "gris", op: q }) + A.r(36, 130, 260 * 0.537 * q, 22, { f: "canard" }) + A.t(42 + 260 * 0.537 * q, 146, A.fr(53.7 * q, 1) + " %", { t: 13, g: true, op: q });
      s += A.t(36, 178, "enfants d’ouvriers", { t: 12, c: "gris", op: q }) + A.r(36, 184, 260 * 0.064 * q, 22, { f: "corail" }) + A.t(42 + 260 * 0.064 * q, 200, A.fr(6.4 * q, 1) + " %", { t: 13, g: true, op: q });
      s += A.t(180, 222, "pour 23,0 % de cadres et 18,0 % d’ouvriers dans l’emploi (2024)", { t: 10.5, a: "middle", c: "gris", op: A.s(p, 0.7, 1), w: 270, v: true });
    }
    return s;
  }
};

ANIMS["s2-boudon"] = {
  t: "À notes égales, des choix différents",
  h: 320,
  src: "Source du chiffre : ministère de l’Éducation nationale, DEPP, note sur l’orientation en fin de troisième (élèves ayant entre 10 et 12 de moyenne). Mécanisme : R. Boudon, <i>L’Inégalité des chances</i>, 1973.",
  etapes: [
    { l: "Deux élèves ont la même moyenne en fin de troisième, entre 10 et 12.", d: 3 },
    { l: "L’un est enfant de cadre, l’autre enfant d’ouvrier non qualifié. Pour la première famille, une seconde générale coûte peu et ouvre beaucoup ; pour l’autre, le coût et le risque d’échec pèsent plus lourd.", d: 4.5 },
    { l: "Résultat observé : 91 % des enfants de cadres demandent une seconde générale et technologique, contre 59 % des enfants d’ouvriers non qualifiés.", d: 4 },
    { l: "Le même calcul se répète à chaque palier (seconde, bac, études supérieures) : les écarts s’additionnent.", d: 3.5 },
    { l: "C’est l’effet d’agrégation décrit par Raymond Boudon : des choix individuels raisonnables produisent des inégalités collectives que personne n’a voulues.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "", E = [{ n: "Enfant de cadre", x: 20, c: "canard", v: 91 }, { n: "Enfant d’ouvrier non qualifié", x: 190, c: "corail", v: 59 }];
    E.forEach(function (e, k) {
      s += A.cercle(e.x + 75, 34, 13, { f: e.c }) + A.r(e.x + 62, 50, 26, 30, { f: e.c, r: 8 });
      s += A.t(e.x + 75, 98, e.n, { t: 12, g: true, a: "middle", w: 150 });
      s += A.jauge(e.x + 10, 132, 130, 11, 20, { c: "moutarde", l: "moyenne en 3e", val: "10 à 12" });
      if (i >= 1) {
        var q = i === 1 ? A.s(p, 0.1 + k * 0.2, 0.6 + k * 0.2) : 1, pente = k === 0 ? -8 : 8;
        s += A.g(q, '<line x1="' + (e.x + 25) + '" x2="' + (e.x + 125) + '" y1="' + (176 - pente) + '" y2="' + (176 + pente) + '" style="stroke:var(--encre);stroke-width:2.5"/>' +
          A.t(e.x + 25, 162 - pente, "gains", { t: 11, a: "middle", c: "vert", g: true }) + A.t(e.x + 125, 162 + pente, "coûts", { t: 11, a: "middle", c: "corail", g: true }) +
          '<path d="M' + (e.x + 70) + ' 196L' + (e.x + 80) + ' 196L' + (e.x + 75) + ' 178z" style="fill:var(--encre2)"/>');
      }
      if (i >= 2) {
        var q2 = i === 2 ? A.s(p, 0.1, 0.8) : 1;
        s += A.t(e.x + 10, 222, "2de générale demandée", { t: 11, c: "gris" });
        s += A.r(e.x + 10, 228, 110, 14, { f: "carte2", r: 6 }) + A.r(e.x + 10, 228, 110 * e.v / 100 * q2, 14, { f: e.c, r: 6 });
        s += A.t(e.x + 125, 240, A.fr(e.v * q2, 0) + " %", { t: 12.5, g: true });
      }
    });
    if (i >= 3) {
      var q3 = i === 3 ? A.s(p, 0, 0.8) : 1;
      ["3e → 2de", "2de → bac", "bac → supérieur"].forEach(function (pal, k) {
        var x = 30 + k * 108;
        s += A.boite(x, 262, 96, 28, pal, { k: "neutre", t: 11, op: A.s(q3, k * 0.25, k * 0.25 + 0.4) });
        if (k < 2) s += A.fl(x + 98, 276, x + 106, 276, { c: "gris", p: A.s(q3, k * 0.25 + 0.2, k * 0.25 + 0.5) });
      });
    }
    if (i === 4) s += A.t(180, 310, "des choix individuels → une inégalité collective", { t: 12.5, g: true, a: "middle", c: "corail", op: A.s(p, 0.3, 0.8) });
    return s;
  }
};

ANIMS["s1-marx-weber"] = {
  t: "Deux façons de découper la société : Marx et Weber",
  h: 320,
  src: "Schéma de principe. Positions illustratives sur les échelles de Weber.",
  etapes: [
    { l: "Marx : une seule ligne de partage, la propriété des moyens de production. D’un côté la bourgeoisie, peu nombreuse ; de l’autre le prolétariat.", d: 3.5 },
    { l: "Le prolétaire vend sa force de travail ; le bourgeois s’approprie la plus-value. Leurs intérêts sont opposés.", d: 3.5 },
    { l: "Classe en soi, puis classe pour soi : quand les ouvriers prennent conscience de leurs intérêts communs, ils se mobilisent. C’est la lutte des classes.", d: 3.5 },
    { l: "Weber : non pas une mais trois échelles, indépendantes. Ordre économique (classes), ordre social (prestige des groupes de statut), ordre politique (partis).", d: 4 },
    { l: "Une même personne peut être haut sur une échelle et bas sur une autre : un professeur a plus de prestige que de revenu, un commerçant aisé l’inverse.", d: 4 }
  ],
  rendu: function (A, i, p) {
    var s = "";
    function pers(x, y, c, op) { return A.cercle(x, y - 8, 4.5, { f: c, op: op }) + A.r(x - 5, y - 3, 10, 11, { f: c, r: 3, op: op }); }
    var opM = i <= 2 ? 1 : 1 - A.s(p, 0, 0.5);
    if (opM > 0.02) {
      var m = A.boite(110, 20, 140, 40, "Bourgeoisie : propriétaires", { k: "cause", t: 12, g: true }) ;
      for (var k = 0; k < 3; k++) m += pers(150 + k * 30, 84, "canard");
      m += '<line x1="20" x2="340" y1="112" y2="112" style="stroke:var(--encre);stroke-width:3"/>' + A.t(20, 101, "propriété des moyens de production", { t: 10.5, c: "gris", w: 118, v: true });
      var conscience = i >= 2 ? (i === 2 ? A.s(p, 0.2, 0.8) : 1) : 0;
      for (var j = 0; j < 12; j++) {
        var x0 = 30 + j * 26, y0 = 160 + (j % 2) * 26, xf = 120 + (j % 6) * 24, yf = 158 + Math.floor(j / 6) * 26;
        m += pers(A.l(x0, xf, conscience), A.l(y0, yf, conscience), "corail");
      }
      m += A.boite(110, 214, 140, 38, "Prolétariat : vend sa force de travail", { k: "effet", t: 11.5, g: true });
      if (i >= 1) m += A.fl(180, 150, 180, 96, { c: "moutarde", sw: 3, p: i === 1 ? A.s(p, 0.1, 0.7) : 1 }) + A.t(188, 130, "plus-value", { t: 11.5, g: true, c: "moutarde", op: i === 1 ? A.s(p, 0.4, 0.9) : 1, h: true });
      if (i >= 2) m += A.t(180, 278, "classe pour soi : conscience et lutte", { t: 12.5, g: true, a: "middle", c: "corail", op: conscience });
      s += A.g(opM, m);
    }
    if (i >= 3) {
      var opW = i === 3 ? A.s(p, 0.3, 0.9) : 1, axes = [["Économique : revenus, patrimoine", 70], ["Social : prestige", 150], ["Politique : pouvoir", 230]];
      var w = "";
      axes.forEach(function (ax, k) {
        w += A.t(20, ax[1] - 14, ax[0], { t: 12, g: true }) + A.fl(20, ax[1], 340, ax[1], { c: "gris", sw: 2 }) + A.t(20, ax[1] + 16, "bas", { t: 10, c: "gris" }) + A.t(340, ax[1] + 16, "haut", { t: 10, c: "gris", a: "end" });
      });
      if (i === 4) {
        var q = A.s(p, 0.1, 0.8), prof = [150, 280, 170], comm = [270, 140, 150];
        axes.forEach(function (ax, k) {
          w += A.cercle(A.l(180, prof[k], q), ax[1], 8, { f: "canard", s: "carte", sw: 2 }) + A.cercle(A.l(180, comm[k], q), ax[1], 8, { f: "moutarde", s: "carte", sw: 2 });
        });
        w += A.cercle(40, 296, 7, { f: "canard" }) + A.t(52, 300, "professeur", { t: 11.5, g: true }) + A.cercle(170, 296, 7, { f: "moutarde" }) + A.t(182, 300, "commerçant aisé", { t: 11.5, g: true });
      }
      s += A.g(opW, w);
    }
    return s;
  }
};

/* Animations explicatives supplémentaires : S3 (mobilité structurelle), S4 (critères du BIT),
   S5 (répertoires d'action collective), R1 (conceptions de la justice sociale).
   Chiffres S3 et S4 recalculés par outils/specialites/ses/verif/renfort_s3s4s5r1.py. */

/* Point situé à la fraction q (0…1) de la longueur d'une ligne brisée */
function ANIM_LE_LONG(pts, q) {
  var L = 0, seg = [];
  for (var i = 1; i < pts.length; i++) { var d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(d); L += d; }
  var r = L * Math.max(0, Math.min(1, q));
  for (var j = 1; j < pts.length; j++) {
    if (seg[j - 1] >= r) { var f = seg[j - 1] ? r / seg[j - 1] : 0; return [pts[j - 1][0] + (pts[j][0] - pts[j - 1][0]) * f, pts[j - 1][1] + (pts[j][1] - pts[j - 1][1]) * f]; }
    r -= seg[j - 1];
  }
  return pts[pts.length - 1];
}

ANIMS["s3-structure"] = {
  t: "La mobilité structurelle mesurée : les hommes en 2015",
  h: 340,
  src: "Source : Insee, enquête Formation et qualification professionnelle 2014-2015 (Insee Première n° 1739, février 2019). Hommes de 35 à 59 ans, comparés à leur père. Mobilité structurelle = moitié de la somme des écarts entre les deux structures (calcul vérifié).",
  etapes: [
    { l: "Les pères d’abord : en 2015, on compare la catégorie sociale des hommes de 35 à 59 ans à celle de leur père. Parmi les pères, 8,3 % d’agriculteurs et 13,9 % de cadres.", d: 4 },
    { l: "Puis les fils : 2,8 % d’agriculteurs seulement, mais 20,4 % de cadres et 25,3 % de professions intermédiaires. En une génération, la structure des emplois s’est déplacée vers le haut.", d: 4.5 },
    { l: "Des places ont disparu (agriculteurs −5,5 points, artisans et commerçants −3,9, employés et ouvriers −6,2) ; d’autres sont apparues (cadres +6,5, professions intermédiaires +9,4).", d: 4.5 },
    { l: "Même si chacun voulait rester dans le groupe de son père, ce serait impossible : au moins 15,8 fils sur 100 doivent changer de groupe. C’est la mobilité structurelle, la moitié de la somme des écarts (31,5 ÷ 2).", d: 5 },
    { l: "Or 65,2 % des hommes ont changé de groupe (mobilité observée). La structure n’en explique qu’environ un quart (15,8 ÷ 65,2 ≈ 24 %) : le reste est la mobilité nette, ou de circulation.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var noms = ["Agriculteurs", "Artisans, commerçants", "Cadres", "Professions intermédiaires", "Employés et ouvriers qualifiés", "Employés et ouvriers non qualifiés"];
    var P = [8.3, 13.0, 13.9, 15.9, 35.6, 13.1], F = [2.8, 9.1, 20.4, 25.3, 32.4, 10.1];
    var x0 = 112, sc = 4.9, y0 = 34, rh = 37, s = "";
    s += A.r(x0 - 2, 8, 12, 9, { f: "gris", r: 2, op: 0.55 }) + A.t(x0 + 15, 16, "pères (origine)", { t: 11, c: "gris" });
    s += A.r(x0 + 112, 8, 12, 9, { f: "canard", r: 2, op: i >= 1 ? 1 : 0.3 }) + A.t(x0 + 129, 16, "fils (position)", { t: 11, c: "canard", g: true, op: i >= 1 ? 1 : 0.4 });
    var somme = 0;
    noms.forEach(function (n, k) {
      var y = y0 + k * rh, qP = i === 0 ? A.s(p, k * 0.08, 0.45 + k * 0.08) : 1, qF = i === 0 ? 0 : i === 1 ? A.s(p, k * 0.08, 0.45 + k * 0.08) : 1;
      s += A.t(x0 - 8, y + 13, n, { t: 10.5, a: "end", w: 100, v: true, c: "encre" });
      s += A.r(x0, y, P[k] * sc * qP, 11, { f: "gris", r: 2, op: 0.55 });
      s += A.t(x0 + P[k] * sc * qP + 4, y + 10, A.fr(P[k] * qP, 1), { t: 10, c: "gris", op: qP });
      if (qF > 0) {
        s += A.r(x0, y + 13, F[k] * sc * qF, 11, { f: "canard", r: 2 });
        s += A.t(x0 + F[k] * sc * qF + 4, y + 23, A.fr(F[k] * qF, 1), { t: 10.5, g: true, c: "canard", op: qF });
      }
      var d = F[k] - P[k];
      if (i >= 2) {
        var qd = i === 2 ? A.s(p, 0.1 + k * 0.1, 0.4 + k * 0.1) : 1;
        s += A.t(356, y + 18, (d > 0 ? "+" : "−") + A.fr(Math.abs(d), 1), { t: 12, g: true, a: "end", c: d > 0 ? "vert" : "corail", op: qd });
        if (i === 3) somme += Math.abs(d) * A.s(p, k * 0.1, 0.1 + k * 0.1);
      }
    });
    var yb = y0 + 6 * rh + 8;
    if (i === 2) s += A.t(180, yb + 22, "places créées : +15,9 points · places disparues : −15,6 points", { t: 11.5, g: true, a: "middle", op: A.s(p, 0.7, 1), w: 320 });
    if (i === 3) {
      s += A.t(180, yb + 14, "somme des écarts : " + A.fr(somme, 1) + " points", { t: 12, a: "middle", c: "gris" });
      s += A.t(180, yb + 40, "mobilité structurelle = " + A.fr(somme, 1) + " ÷ 2 = " + A.fr(somme / 2, 1) + " %", { t: 14.5, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.65, 1) });
    }
    if (i === 4) {
      var q = A.s(p, 0, 0.6), q2 = A.s(p, 0.45, 1);
      s += A.t(20, yb + 10, "Mobilité observée des hommes : " + A.fr(65.2 * q, 1) + " %", { t: 11.5, g: true });
      s += A.r(20, yb + 18, 320, 16, { f: "carte2", r: 5 }) + A.r(20, yb + 18, 320 * 0.652 * q, 16, { f: "canard", r: 5, op: 0.35 });
      s += A.r(20, yb + 18, 320 * 0.158 * q2, 16, { f: "corail", r: 5 });
      s += A.t(24, yb + 50, "dont structurelle : 15,8 points, soit 24 %", { t: 11.5, g: true, c: "corail", op: q2 });
      s += A.t(24, yb + 66, "le reste, mobilité nette : 49,4 points", { t: 11.5, g: true, c: "canard", op: q2 });
    }
    return s;
  }
};

ANIMS["s4-bit"] = {
  t: "Chômeur, halo ou inactif ? Les trois critères du BIT",
  h: 340,
  src: "Cas fictifs construits pour le site. Définitions : Insee (chômage au sens du BIT, halo autour du chômage). Chiffres : Insee, enquête Emploi 2025 (Insee Première n° 2096), part de la population des 15-64 ans.",
  etapes: [
    { l: "Le Bureau international du travail classe chacun avec trois critères, dans l’ordre. D’abord : avoir travaillé, ne serait-ce qu’une heure, pendant la semaine de référence.", d: 3.5 },
    { l: "Un étudiant a fait 3 heures de livraison cette semaine-là : il est en emploi. Une heure suffit. S’il souhaite travailler davantage et qu’il est disponible, il est en sous-emploi.", d: 4.5 },
    { l: "Une ancienne vendeuse n’a pas travaillé, peut commencer tout de suite et envoie des candidatures : les trois critères sont remplis, elle est chômeuse au sens du BIT.", d: 5 },
    { l: "Une mère cherche un emploi mais ne peut pas commencer avant un mois, faute de garde d’enfant : pas disponible, donc pas chômeuse. Elle souhaite travailler : elle est dans le halo autour du chômage.", d: 5 },
    { l: "Un ouvrier de 58 ans, disponible, a cessé de chercher, découragé : sans recherche active, il n’est pas chômeur au sens du BIT. Il souhaite travailler : il est lui aussi dans le halo.", d: 5 },
    { l: "Un retraité qui ne souhaite pas travailler est inactif. En 2025, 5,8 % des 15-64 ans sont au chômage et 4,5 % dans le halo : 10,3 % sont sans emploi et souhaitent travailler.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var s = "", bx = 36, bw = 190, bh = 34;
    var Q = [{ y: 30, t: "A travaillé au moins 1 heure dans la semaine ?" }, { y: 92, t: "Disponible dans les 2 semaines ?" }, { y: 154, t: "A cherché activement dans le mois ?" }, { y: 230, t: "Souhaite travailler ?" }];
    var R = { emploi: { y: 30, t: "En emploi", k: "canard" }, chomeur: { y: 154, t: "Chômeur (BIT)", k: "corail" }, halo: { y: 230, t: "Halo du chômage", k: "moutarde" }, inactif: { y: 292, t: "Inactif", k: "gris" } };
    var rx = 250, rw = 104;
    var qa = i === 0 ? p : 1;
    /* rails : « non » descend à gauche vers la question 4, « oui » descend au centre */
    var rail = '<line x1="12" x2="12" y1="' + (92 + bh / 2) + '" y2="' + (230 + bh / 2) + '" style="stroke:var(--ligne);stroke-width:2"/>';
    s += A.g(A.s(qa, 0.3, 0.7), rail +
      A.fl(bx, 92 + bh / 2, 12, 92 + bh / 2, { c: "ligne", sw: 2, tete: false }) + A.fl(bx, 154 + bh / 2, 12, 154 + bh / 2, { c: "ligne", sw: 2, tete: false }) +
      A.fl(12, 230 + bh / 2, bx - 2, 230 + bh / 2, { c: "ligne", sw: 2 }) +
      A.t(15, 92 + bh / 2 - 5, "non", { t: 10.5, c: "gris", it: true }) + A.t(15, 154 + bh / 2 - 5, "non", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw / 2, 30 + bh, bx + bw / 2, 92 - 2, { c: "ligne", sw: 2 }) + A.fl(bx + bw / 2, 92 + bh, bx + bw / 2, 154 - 2, { c: "ligne", sw: 2 }) +
      A.t(bx + bw / 2 + 6, 82, "non", { t: 10.5, c: "gris", it: true }) + A.t(bx + bw / 2 + 6, 144, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw, 30 + bh / 2, rx - 2, 30 + bh / 2, { c: "ligne", sw: 2 }) + A.t(bx + bw + 6, 30 + bh / 2 - 5, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw, 154 + bh / 2, rx - 2, 154 + bh / 2, { c: "ligne", sw: 2 }) + A.t(bx + bw + 6, 154 + bh / 2 - 5, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw, 230 + bh / 2, rx - 2, 230 + bh / 2, { c: "ligne", sw: 2 }) + A.t(bx + bw + 6, 230 + bh / 2 - 5, "oui", { t: 10.5, c: "gris", it: true }) +
      A.fl(bx + bw / 2, 230 + bh, bx + bw / 2, 292 + bh / 2, { c: "ligne", sw: 2, tete: false }) + A.fl(bx + bw / 2, 292 + bh / 2, rx - 2, 292 + bh / 2, { c: "ligne", sw: 2 }) +
      A.t(bx + bw / 2 + 6, 280, "non", { t: 10.5, c: "gris", it: true }));
    /* trajets : de l'entrée jusqu'au bord de la case d'arrivée ; le tracé passe sous les cases */
    var cx = bx + bw / 2, M = function (y) { return y + bh / 2; }, fin = rx - 3;
    var T = {
      1: { pts: [[cx, 8], [cx, M(30)], [fin, M(30)]], c: "canard", lab: "3 h de livraison" },
      2: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [cx, M(154)], [fin, M(154)]], c: "corail", lab: "disponible, cherche" },
      3: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [12, M(92)], [12, M(230)], [cx, M(230)], [fin, M(230)]], c: "moutarde", lab: "pas disponible" },
      4: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [cx, M(154)], [12, M(154)], [12, M(230)], [cx, M(230)], [fin, M(230)]], c: "moutarde", lab: "ne cherche plus" },
      5: { pts: [[cx, 8], [cx, M(30)], [cx, M(92)], [12, M(92)], [12, M(230)], [cx, M(230)], [cx, M(292)], [fin, M(292)]], c: "gris", lab: "ne veut pas travailler" }
    };
    var tr = T[i], qt = A.s(p, 0, 0.85);
    if (tr) s += A.pl(tr.pts, qt, { c: tr.c, sw: 3.2, op: 0.8 });
    Q.forEach(function (q, k) { s += A.boite(bx, q.y, bw, bh, q.t, { k: "meca", t: 11.5, op: i === 0 ? A.s(p, k * 0.15, 0.3 + k * 0.15) : 1 }); });
    var bilan = i === 5 && p > 0.75;
    Object.keys(R).forEach(function (k, j) {
      var r = R[k], q = i === 0 ? A.s(p, 0.5 + j * 0.1, 0.8 + j * 0.1) : 1;
      var txt = bilan && k === "chomeur" ? "Chômage : 5,8 %" : bilan && k === "halo" ? "Halo : 4,5 %" : r.t;
      s += A.boite(rx, r.y, rw, bh, txt, { k: k === "chomeur" ? "effet" : k === "halo" ? "frein" : k === "emploi" ? "cause" : "neutre", t: 11.5, g: true, op: q });
    });
    if (tr) {
      var pos = ANIM_LE_LONG(tr.pts, qt);
      s += A.cercle(pos[0], pos[1], 8, { f: tr.c, s: "carte", sw: 2.5 });
      s += A.t(rx + rw, pos[1] - 21, tr.lab, { t: 11, g: true, c: tr.c === "gris" ? "encre" : tr.c, h: true, a: "end", op: A.s(p, 0.8, 1) });
    }
    return s;
  }
};

ANIMS["s5-tilly"] = {
  t: "Comment le répertoire d’action collective change",
  h: 330,
  src: "D’après Charles Tilly, <i>La France conteste, de 1600 à nos jours</i>, 1986. Dates : abolition du délit de coalition (loi du 25 mai 1864), liberté syndicale (loi du 21 mars 1884) ; tribunal administratif de Paris, 3 février 2021 (L’Affaire du siècle).",
  etapes: [
    { l: "Charles Tilly appelle répertoire d’action collective l’ensemble limité des moyens d’action qu’un groupe connaît et juge légitimes à une époque. Il ne change que lentement.", d: 3.5 },
    { l: "Du XVIIe au milieu du XIXe siècle : un répertoire local et patronné. On agit dans sa communauté, souvent par l’intermédiaire d’un notable, directement contre l’adversaire : charivaris, émeutes de subsistance, révoltes contre l’impôt.", d: 5 },
    { l: "Au XIXe siècle, l’État national et l’industrie s’imposent : les décisions se prennent dans la capitale et les grandes entreprises. Les luttes changent d’échelle et s’adressent à l’État.", d: 4.5 },
    { l: "Vers le milieu du XIXe siècle naît un répertoire national et autonome : grève (le délit de coalition est aboli en 1864), syndicats (autorisés en 1884), manifestation, pétition, réunion publique. Des organisations permanentes agissent en leur nom propre.", d: 5.5 },
    { l: "Depuis la fin du XXe siècle, le répertoire s’enrichit : actions médiatiques, contre-expertise, pétitions en ligne, recours en justice (L’Affaire du siècle, jugée le 3 février 2021), désobéissance civile, marches pour le climat dans de nombreux pays (2019).", d: 5.5 },
    { l: "Les anciens moyens ne disparaissent pas : la grève et la manifestation restent au cœur des mobilisations de 2023 contre la réforme des retraites. Le répertoire s’élargit : les militants combinent les formes.", d: 4.5 }
  ],
  rendu: function (A, i, p) {
    var s = "", X = function (an) { return 22 + (an - 1600) * 316 / 430; }, ya = 300;
    var qa = i === 0 ? A.s(p, 0, 0.7) : 1;
    s += A.fl(X(1600), ya, X(1600) + (X(2030) - X(1600)) * qa, ya, { c: "encre", sw: 1.6 });
    [1600, 1700, 1800, 1900, 2000].forEach(function (an, k) {
      var q = i === 0 ? A.s(p, 0.1 + k * 0.12, 0.3 + k * 0.12) : 1;
      s += '<line x1="' + X(an) + '" x2="' + X(an) + '" y1="' + (ya - 4) + '" y2="' + (ya + 4) + '" style="stroke:var(--encre);stroke-width:1.5;opacity:' + q + '"/>' + A.t(X(an), ya + 18, String(an), { t: 11, a: "middle", c: "gris", op: q });
    });
    if (i === 0) s += A.boite(60, 70, 240, 74, "Répertoire : les moyens d’action connus et jugés légitimes à une époque", { k: "cause", t: 13, g: true, op: A.s(p, 0.5, 0.9) });
    /* bande 1 : local et patronné (1600-1850) */
    if (i >= 1) {
      var q1 = i === 1 ? A.s(p, 0, 0.4) : 1, op1 = i >= 3 ? 0.55 : 1;
      s += A.r(X(1600), 252, (X(1850) - X(1600)) * q1, 34, { f: "moutardec", s: "moutarde", r: 6, op: op1 });
      s += A.t(X(1600) + 8, 266, "local et patronné", { t: 12, g: true, c: "moutarde", op: q1 * op1 });
      s += A.t(X(1600) + 8, 280, "village, notable", { t: 10.5, c: "gris", op: q1 * op1 });
      if (i <= 2) ["charivari", "émeute de subsistance", "révolte contre l’impôt"].forEach(function (f, k) {
        var q = i === 1 ? A.s(p, 0.35 + k * 0.15, 0.6 + k * 0.15) : 1;
        s += A.boite(18 + k * 112, 140 + (k % 2) * 40, 104, 32, f, { k: "frein", t: 11.5, op: q * (i === 2 ? 0.5 : 1) });
      });
    }
    /* changement d'échelle : les villages convergent vers l'État */
    if (i === 2) {
      var vil = [[40, 70], [90, 34], [140, 72], [270, 50], [320, 84], [220, 28]], cE = [180, 100];
      vil.forEach(function (v, k) {
        var q = A.s(p, 0.1 + k * 0.06, 0.55 + k * 0.06);
        s += A.cercle(v[0], v[1], 7, { f: "moutarde", op: 0.8 }) + A.fl(v[0], v[1], v[0] + (cE[0] - v[0]) * 0.8 * q, v[1] + (cE[1] - v[1]) * 0.8 * q, { c: "canard", sw: 1.8, p: q > 0 ? 1 : 0 });
      });
      s += A.boite(cE[0] - 70, cE[1] - 2, 140, 30, "État national, industrie", { k: "cause", t: 12, g: true, op: A.s(p, 0.45, 0.8) });
    }
    /* bande 2 : national et autonome (1850-) */
    if (i >= 3) {
      var q2 = i === 3 ? A.s(p, 0, 0.45) : 1;
      s += A.r(X(1850), 252, (X(2026) - X(1850)) * q2, 34, { f: "canardc", s: "canard", r: 6 });
      s += A.t(X(1850) + 5, 266, "national, autonome", { t: 11.5, g: true, c: "canard", op: q2 });
      s += A.t(X(1850) + 6, 280, "syndicats, partis", { t: 10.5, c: "gris", op: q2 });
      [[1864, "1864"], [1884, "1884"]].forEach(function (d, k) {
        var q = i === 3 ? A.s(p, 0.35 + k * 0.1, 0.55 + k * 0.1) : 1;
        s += A.cercle(X(d[0]), ya, 4.5, { f: "canard", op: q });
      });
      if (i === 3) ["grève (1864)", "syndicats (1884)", "manifestation", "pétition, réunion"].forEach(function (f, k) {
        var q = A.s(p, 0.4 + k * 0.12, 0.65 + k * 0.12);
        s += A.boite(14 + (k % 2) * 170, 60 + Math.floor(k / 2) * 46, 160, 36, f, { k: "cause", t: 12.5, g: true, op: q });
      });
    }
    /* bande 3 : élargissement (fin du XXe siècle -) */
    if (i >= 4) {
      var q3 = i === 4 ? A.s(p, 0, 0.4) : 1;
      s += A.r(X(1975), 210, (X(2026) - X(1975)) * q3, 36, { f: "corailc", s: "corail", r: 6 });
      s += A.t(X(1975) - 6, 224, "élargi", { t: 12, g: true, a: "end", c: "corail", op: q3 });
      s += A.t(X(1975) - 6, 238, "médias, justice, en ligne", { t: 10.5, a: "end", c: "gris", op: q3 });
      if (i === 4) ["action médiatique", "contre-expertise", "pétition en ligne", "recours en justice (2021)", "désobéissance civile", "marches pour le climat (2019)"].forEach(function (f, k) {
        var q = A.s(p, 0.3 + k * 0.09, 0.55 + k * 0.09);
        s += A.boite(14 + (k % 2) * 170, 22 + Math.floor(k / 2) * 44, 160, 34, f, { k: "effet", t: 12, op: q });
      });
    }
    if (i === 5) {
      var q5 = A.s(p, 0.1, 0.6);
      s += A.boite(30, 40, 300, 46, "2023, retraites : grèves et manifestations, mais aussi pétitions et réseaux sociaux", { k: "cause", t: 12.5, g: true, op: q5 });
      s += A.fl(316, 92, 316, 204, { c: "canard", sw: 2, p: A.s(p, 0.4, 0.8) });
      s += A.t(306, 150, "les couches s’empilent", { t: 12, g: true, a: "end", c: "canard", op: A.s(p, 0.6, 1), h: true });
    }
    return s;
  }
};

ANIMS["r1-voile"] = {
  t: "Trois sociétés, quatre conceptions de la justice",
  h: 330,
  src: "Exemple fictif construit pour le site (revenus en milliers d’euros par an, sommes vérifiées). Ici, pour simplifier, le bien-être total est mesuré par la somme des revenus. Auteurs : J. Bentham et J. S. Mill ; J. Rawls, <i>Théorie de la justice</i>, 1971 ; R. Nozick, <i>Anarchie, État et utopie</i>, 1974.",
  etapes: [
    { l: "Trois sociétés de cinq personnes (revenus fictifs, en milliers d’euros par an). A est parfaitement égale ; B produit le plus, mais avec de fortes inégalités ; C est inégale, mais moins que B.", d: 4 },
    { l: "Utilitarisme : est juste la société où le bien-être total est le plus grand. En le mesurant par la somme des revenus, B l’emporte : 310, contre 150 pour A et 260 pour C.", d: 4.5 },
    { l: "Égalitarisme strict : est juste la société où les situations sont égales. Seule A convient, même si chacun y est moins riche qu’une partie des habitants de B et C.", d: 4 },
    { l: "Rawls : choisis sans savoir quelle place tu occuperas, derrière un « voile d’ignorance ». Prudent, tu regardes la pire place : 30 en A, 10 en B, 38 en C.", d: 5 },
    { l: "Principe de différence : les inégalités de C sont acceptables, car le plus défavorisé y vit mieux que dans la société égale (38 contre 30). Rawls choisit C, à condition que les libertés de base et l’égalité des chances soient garanties.", d: 5.5 },
    { l: "Libertarisme (Nozick) : on ne compare pas les résultats. Une répartition est juste si chacun a acquis ses revenus par le travail, l’échange libre ou le don ; prendre aux uns pour donner aux autres porte atteinte à leurs droits.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var S = [{ n: "Société A", v: [30, 30, 30, 30, 30] }, { n: "Société B", v: [10, 25, 50, 90, 135] }, { n: "Société C", v: [38, 42, 48, 58, 74] }];
    var base = 222, k = 1.18, s = "";
    var choix = i === 1 ? 1 : i === 2 ? 0 : i === 4 ? 2 : -1, qc = A.s(p, 0.35, 0.8);
    S.forEach(function (so, j) {
      var x0 = 14 + j * 116, tot = so.v.reduce(function (a, b) { return a + b; }, 0), mn = Math.min.apply(null, so.v);
      var choisi = choix === j, eteint = choix >= 0 && !choisi;
      if (choisi) s += A.r(x0 - 6, 30, 110, base - 30 + 34, { f: "moutardec", s: "moutarde", r: 10, op: qc });
      s += A.t(x0 + 49, 48, so.n, { t: 14, g: true, a: "middle", f: true, op: eteint ? 0.45 : 1 });
      so.v.forEach(function (v, m) {
        var q = i === 0 ? A.s(p, j * 0.2 + m * 0.04, j * 0.2 + m * 0.04 + 0.35) : 1;
        var pire = (i === 3 || i === 4) && v === mn && m === 0;
        var h = v * k * q;
        s += A.r(x0 + m * 20, base - h, 16, h, { f: pire ? "corail" : j === 0 ? "gris" : j === 1 ? "canard" : "vert", r: 2, op: eteint ? 0.3 : (i === 3 && !pire ? 0.35 : 1) });
        if (i === 0 || pire) s += A.t(x0 + m * 20 + 8, base - h - 4, String(Math.round(v * q)), { t: 10, a: "middle", g: pire, c: pire ? "corail" : "gris", op: i === 0 ? q : (i === 3 ? A.s(p, 0.5, 0.9) : 1) });
      });
      s += '<line x1="' + (x0 - 3) + '" x2="' + (x0 + 101) + '" y1="' + base + '" y2="' + base + '" style="stroke:var(--encre2);stroke-width:1"/>';
      if (i === 1) s += A.t(x0 + 49, base + 22, "total : " + Math.round(tot * A.s(p, 0, 0.5)), { t: 12.5, g: true, a: "middle", c: choisi ? "encre" : "gris" });
      if (i === 2) s += A.t(x0 + 49, base + 22, j === 0 ? "aucun écart" : "écart : " + (Math.max.apply(null, so.v) - mn), { t: 12.5, g: true, a: "middle", c: choisi ? "encre" : "gris", op: A.s(p, 0.1, 0.5) });
      if (i === 3 || i === 4) s += A.t(x0 + 49, base + 22, "pire place : " + mn, { t: 12.5, g: true, a: "middle", c: j === 2 && i === 4 ? "corail" : "gris" });
    });
    if (i === 3) {
      /* le voile : un rideau translucide passe sur les trois sociétés */
      var v = A.s(p, 0, 0.45) * (1 - A.s(p, 0.55, 0.85));
      s += A.r(4, 56, 352, base - 52, { f: "encre", r: 10, op: 0.55 * v });
      s += A.t(180, 140, "Quelle place auras-tu ?", { t: 16, g: true, a: "middle", c: "papier", op: v, f: true });
    }
    if (i === 4) s += A.fl(14 + 8, base - 30 * k - 10, 14 + 232 + 8, base - 38 * k - 18, { c: "corail", sw: 2, p: A.s(p, 0.1, 0.6), tir: true });
    var verdict = ["", "Utilitarisme → B", "Égalitarisme strict → A", "", "Rawls → C", ""][i];
    if (verdict) s += A.t(180, base + 56, verdict, { t: 16, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.5, 0.9) });
    if (i === 5) {
      var q5 = A.s(p, 0.2, 0.7);
      s += A.r(20, 56, 320, 112, { f: "carte", s: "canard", r: 12, op: q5 });
      s += A.t(180, 92, "Nozick ne choisit pas un tableau :", { t: 13.5, g: true, a: "middle", c: "canard", op: q5 });
      s += A.t(180, 118, "les trois peuvent être justes", { t: 13, a: "middle", op: q5 });
      s += A.t(180, 142, "si les revenus ont été acquis légitimement.", { t: 13, a: "middle", op: q5 });
      s += A.t(180, base + 56, "Libertarisme → la procédure, pas le résultat", { t: 14, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.6, 1), w: 330 });
    }
    return s;
  }
};

