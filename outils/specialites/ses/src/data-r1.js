GRAPHES["r1-ineg"] = {
  type: "lignes", t: "Les inégalités de niveau de vie en France, 1996-2024", spark: 1,
  s: "Deux rapports, après impôts et prestations sociales. Touche le graphique pour lire une année ; touche la légende pour masquer une courbe.",
  src: "Source : Insee-DGFiP-Cnaf-Cnav-CCMSA, enquêtes Revenus fiscaux et sociaux (Insee Première n° 2117, juillet 2026). Champ : France métropolitaine, personnes vivant dans un logement ordinaire. Ruptures de série en 2010, 2012 et 2020 ; données de 2020 fragiles.",
  unite: "", dec: 2, pasX: 7, h: 280, min: 2, max: 6,
  x: [1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
  series: [
    { n: "Rapport interdécile D9/D1", c: 1, v: [3.51,3.49,3.42,3.44,3.5,3.43,3.39,3.35,3.3,3.35,3.41,3.38,3.38,3.44,3.48,3.58,3.55,3.44,3.43,3.47,3.42,3.43,3.5,3.44,3.29,3.41,3.38,3.49,3.48] },
    { n: "Rapport des masses (100 − S80)/S20", c: 2, v: [4.08,4.03,3.99,4.07,4.14,4.09,3.98,4.01,3.97,4.14,4.19,4.16,4.19,4.21,4.4,4.47,4.44,4.17,4.17,4.2,4.17,4.17,4.34,4.2,4.07,4.45,4.4,4.53,4.62] }
  ]
};
GRAPHES["r1-redis"] = {
  type: "hbarres", t: "Ce que change la redistribution, 2024",
  s: "Rapports d’inégalité de niveau de vie avant et après impôts directs et prestations sociales.",
  src: "Source : Insee Première n° 2117 (juillet 2026). « Avant redistribution » : revenus d’activité, du patrimoine et de remplacement (pensions, allocations chômage) avant impôts directs et prestations sociales.",
  unite: "", dec: 2, lab: 150,
  cats: ["Rapport interdécile D9/D1", "Rapport des masses (100 − S80)/S20"],
  series: [{ n: "Avant redistribution", v: [5.89, 8.37], c: 2 }, { n: "Après redistribution", v: [3.48, 4.62], c: 1 }]
};
GRAPHES["r1-patri"] = {
  type: "hbarres", t: "L’échelle des patrimoines, début 2021",
  s: "Patrimoine brut des ménages (logement, placements, biens professionnels…), en euros. La première barre est presque invisible : c’est le message.",
  src: "Source : Insee, enquête Histoire de vie et Patrimoine 2020-2021 (Les revenus et le patrimoine des ménages, Insee Références, édition 2024). Champ : France hors Mayotte, ménages en logement ordinaire.",
  unite: " €", dec: 0, lab: 150,
  cats: ["Plafond des 10 % les moins dotés (D1)", "Médiane (D5)", "Plancher des 10 % les mieux dotés (D9)", "Plancher des 5 % les mieux dotés", "Plancher des 1 % les mieux dotés"],
  series: [{ n: "2021", v: [4400, 177200, 716300, 1035000, 2200000], c: 1 }]
};

CHAINES["r1-cumul"] = { t: "Pourquoi les inégalités sont cumulatives", e: [
  { t: "Revenus élevés et patrimoine hérité", k: "cause" },
  { f: [{ t: "Logement dans un quartier favorisé, établissements scolaires réputés" }, { t: "Accès aux soins, alimentation, conditions de travail moins pénibles" }], a: "donc" },
  { t: "Diplômes plus élevés, meilleure santé (13 ans d’espérance de vie en plus pour les hommes les plus aisés)", a: "donc" },
  { t: "Emplois mieux payés, épargne, patrimoine transmis aux enfants", a: "donc" },
  { t: "Les avantages s’additionnent et se reproduisent d’une génération à l’autre", k: "effet", a: "donc" }
] };
CHAINES["r1-u"] = { t: "La courbe en U des hauts revenus au XXe siècle", e: [
  { t: "Avant 1914 : patrimoines très concentrés, faible impôt ; le 1 % le plus aisé reçoit environ un cinquième des revenus", k: "cause" },
  { t: "Guerres, crise de 1929, inflation : destruction et dévalorisation des gros patrimoines", a: "puis" },
  { t: "Impôt progressif sur le revenu (1914) et sur les successions, Sécurité sociale (1945), salaire minimum", a: "et" },
  { t: "1945-1983 : inégalités au plus bas (moins de 8 % pour le 1 % le plus aisé en 1983)", k: "effet", a: "donc" },
  { t: "Depuis 1983 : hausse des très hauts salaires et des revenus du capital, fiscalité moins progressive en haut", k: "frein", a: "puis" }
] };
CHAINES["r1-rawls"] = { t: "Le raisonnement de Rawls : le voile d’ignorance", e: [
  { t: "Imaginons que l’on choisisse les règles de la société sans savoir quelle place on y occupera (position originelle)", k: "cause" },
  { t: "Personne ne veut risquer d’être sacrifié : on choisit d’abord des libertés égales pour tous", a: "donc" },
  { t: "Puis l’égalité équitable des chances face aux positions", a: "et" },
  { t: "Principe de différence : des inégalités ne sont justes que si elles profitent aux plus défavorisés", k: "effet", a: "et" }
] };
CHAINES["r1-redis"] = { t: "Comment la redistribution réduit les inégalités", e: [
  { f: [{ t: "Prélèvements progressifs : impôt sur le revenu, droits de succession", k: "cause" }, { t: "Prestations sous conditions de ressources : RSA, prime d’activité, aides au logement", k: "cause" }, { t: "Services collectifs gratuits : école, santé", k: "cause" }] },
  { t: "On prélève proportionnellement plus en haut et on reverse proportionnellement plus en bas", a: "donc" },
  { t: "Rapport D9/D1 : 5,89 avant redistribution, 3,48 après (2024)", k: "effet", a: "donc" }
] };
CHAINES["r1-pervers"] = { t: "Le risque d’effets pervers (désincitations)", e: [
  { t: "Prélèvements élevés sur les revenus supplémentaires ou prestations qui baissent quand le revenu augmente", k: "cause" },
  { t: "Le gain à travailler plus ou à reprendre un emploi devient faible", a: "donc" },
  { t: "Désincitation au travail, à l’investissement, voire exil fiscal (« trappe à inactivité »)", k: "frein", a: "donc" },
  { t: "Réponse : rendre le travail payant (prime d’activité, 2016), mieux cibler, lutter contre la fraude et l’optimisation", k: "effet", a: "d’où" }
] };

CH.r1 = {
  horsEcrit: "elle fournit les outils de mesure des inégalités (Gini, rapport interdécile, top 1 %) utiles dans toutes les copies sur la structure sociale, la mobilité ou la croissance, et elle nourrit très bien un Grand oral",
  chapo: "Faut-il que tout le monde ait le même revenu ? Ou seulement les mêmes chances au départ ? Ou simplement les mêmes droits ? Ce chapitre retrace un siècle d’inégalités, apprend à les mesurer (rapports inter-quantiles, courbe de Lorenz, coefficient de Gini, top 1 %, corrélation parents-enfants), présente quatre grandes conceptions de la justice sociale et examine ce que font les pouvoirs publics, sous contrainte de financement.",
  essentiel: [
    "Depuis le début du XX<sup>e</sup> siècle, les inégalités économiques dessinent un <b>U</b> : très fortes avant 1914, elles baissent jusqu’au début des années 1980, puis remontent par le haut de la distribution. Elles sont <b>multiformes</b> (revenu, patrimoine, santé, école, logement) et <b>cumulatives</b>.",
    "On les mesure par des outils <b>statiques</b> (rapport D9/D1 : 3,48 en 2024 ; courbe de Lorenz et coefficient de Gini : 0,302 ; part du top 1 %) et <b>dynamiques</b> (corrélation des revenus parents-enfants : 0,30 en France).",
    "Trois formes d’égalité : <b>des droits</b>, <b>des chances</b>, <b>des situations</b>. Elles fondent quatre conceptions de la justice : <b>utilitarisme</b> (maximiser le bien-être total), <b>libertarisme</b> (respecter les droits de propriété, Nozick), <b>égalitarisme libéral</b> (Rawls : inégalités justes si elles profitent aux plus défavorisés), <b>égalitarisme strict</b> (égalité des situations).",
    "Les pouvoirs publics agissent par la <b>fiscalité</b>, la <b>protection sociale</b>, les <b>services collectifs</b> et la <b>lutte contre les discriminations</b> : la redistribution ramène le rapport D9/D1 de 5,89 à 3,48 en 2024.",
    "Cette action s’exerce sous <b>contrainte de financement</b> (prélèvements obligatoires : 43,6 % du PIB en 2025) et fait débat : <b>efficacité</b>, <b>légitimité</b> (consentement à l’impôt), <b>effets pervers</b> (désincitations)."
  ],
  chiffres: [
    { n: "0,302", l: "l’indice de Gini des niveaux de vie en 2024, son plus haut niveau depuis le début de la série (1996).", s: "Insee Première n° 2117" },
    { n: "8 %", l: "du patrimoine brut est détenu par la moitié la moins dotée des ménages début 2021 ; l’autre moitié en détient 92 %.", s: "Insee, enquête Histoire de vie et Patrimoine 2020-2021" },
    { n: "9,7 %", l: "seulement des enfants nés dans les 20 % des familles les plus modestes atteignent les 20 % les plus aisés à l’âge adulte.", s: "Kenedi et Sirugue, note IPP n° 95, 2023" }
  ],
  objectifs: [
    { bo: "Connaître les grandes tendances d’évolution des inégalités économiques depuis le début du XXe siècle et comprendre que les inégalités économiques et sociales présentent un caractère multiforme et cumulatif.", clair: "Raconter le U des inégalités depuis 1900 et montrer, exemples à l’appui, que les inégalités se combinent et se renforcent.", voir: "r1-1" },
    { bo: "Savoir interpréter les principaux outils de mesure des inégalités, statique (rapport inter-quantiles, courbe de Lorenz et coefficient de Gini, top 1%) et dynamique (corrélation de revenu parents-enfants).", clair: "Lire et interpréter D9/D1, S80/S20, courbe de Lorenz, Gini, part du top 1 % et corrélation parents-enfants.", voir: "r1-2" },
    { bo: "Comprendre que les différentes formes d’égalité (égalité des droits, des chances ou des situations) permettent de définir ce qui est considéré comme juste selon différentes conceptions de la justice sociale (notamment l’utilitarisme, le libertarisme, l’égalitarisme libéral, l’égalitarisme strict).", clair: "Distinguer les trois formes d’égalité et les quatre conceptions de la justice sociale, et dire quelles inégalités chacune accepte.", voir: "r1-3" },
    { bo: "Comprendre que l’action des pouvoirs publics en matière de justice sociale (fiscalité, protection sociale, services collectifs, mesures de lutte contre les discriminations) s’exerce sous contrainte de financement et fait l’objet de débats en termes d’efficacité (réduction des inégalités), de légitimité (notamment consentement à l’impôt) et de risque d’effets pervers (désincitations).", clair: "Présenter les quatre instruments, la contrainte de financement et les trois débats.", voir: "r1-5" }
  ],
  notions: ["inégalités économiques", "inégalités sociales", "caractère multiforme et cumulatif", "revenu, patrimoine", "rapport inter-quantiles (D9/D1, S80/S20)", "courbe de Lorenz", "coefficient de Gini", "top 1 %", "corrélation des revenus parents-enfants", "égalité des droits", "égalité des chances", "égalité des situations", "justice sociale", "utilitarisme", "libertarisme", "égalitarisme libéral", "égalitarisme strict", "redistribution", "fiscalité (progressive, proportionnelle)", "protection sociale (assurance, assistance)", "services collectifs", "discriminations", "contrainte de financement", "consentement à l’impôt", "désincitations"],
  sections: [
    { id: "r1-1", t: "Un siècle d’inégalités : une courbe en U, des inégalités cumulatives", h:
      '<div class="def"><b>Inégalité</b> — différence d’accès à des ressources rares et valorisées (revenu, patrimoine, diplôme, santé, pouvoir) qui se traduit par une hiérarchie entre individus ou groupes. Les inégalités <b>économiques</b> portent sur le revenu et le patrimoine ; les inégalités <b>sociales</b> sur l’accès à l’école, à la santé, au logement, à la culture, au pouvoir.</div>' +
      '<h3>La grande tendance : un U</h3>' +
      '<div data-chain="r1-u"></div>' +
      '<p>Les travaux de Thomas Piketty et de ses coauteurs (World Inequality Database) montrent qu’en France, au début du XX<sup>e</sup> siècle, les 10 % les plus aisés perçoivent environ la moitié des revenus avant impôts, et le 1 % le plus aisé environ un cinquième. Leur part s’effondre avec les deux guerres et la crise des années 1930, puis reste basse : les 10 % les plus aisés reçoivent environ 30 % des revenus au début des années 1980, le 1 % le plus aisé moins de 8 % en 1983. Elle remonte ensuite : plus de 12 % pour le 1 % le plus aisé à la veille de la crise de 2008 (Garbinti, Goupille-Lebret et Piketty, 2018), 9,8 % en 2017, et 32 % pour les 10 % les plus aisés (Observatoire des inégalités, d’après la WID).</p>' +
      '<div class="aut"><span class="mono">TP</span><span class="an">Thomas Piketty<small><i>Le Capital au XXI<sup>e</sup> siècle</i>, 2013</small></span><span class="ad">Quand le rendement du capital (r) dépasse durablement la croissance (g), les patrimoines hérités croissent plus vite que les revenus du travail : les inégalités se creusent. La baisse du XX<sup>e</sup> siècle tient aux chocs (guerres, crises) et à des politiques (impôt progressif, État social), pas à une loi automatique.</span></div>' +
      '<div class="plus"><p>L’économiste Simon Kuznets (1955) pensait que les inégalités augmentent puis diminuent naturellement avec le développement (courbe en U inversé). La remontée depuis les années 1980 dans les pays riches a fragilisé cette idée.</p></div>' +
      '<p>Sur la période récente, l’Insee mesure une hausse modérée : l’indice de Gini des niveaux de vie passe de 0,274 en 1996 à 0,302 en 2024, son plus haut niveau depuis le début de la série.</p>' +
      '<div data-graph="r1-ineg"></div>' +
      '<h3>Le patrimoine, beaucoup plus inégal que le revenu</h3><div data-graph="r1-patri"></div>' +
      '<p>Début 2021, la moitié la moins dotée des ménages détient 8 % du patrimoine brut ; les 10 % les mieux dotés possèdent au moins 716 300 euros, les 10 % les moins dotés moins de 4 400 euros, soit un rapport D9/D1 d’environ 160 (calcul du site). L’indice de Gini du patrimoine brut (hors biens durables) atteint 0,662, contre 0,294 pour le niveau de vie en 2021 ; il était de 0,639 en 1998 (Insee). La hausse des prix de l’immobilier depuis le début des années 2000 a creusé l’écart entre propriétaires et non-propriétaires.</p>' +
      '<h3>Des inégalités multiformes et cumulatives</h3>' +
      '<div data-chain="r1-cumul"></div>' +
      '<div class="ex"><p>Santé : selon l’Insee (Insee Première n° 1687, 2018), l’espérance de vie à la naissance des hommes parmi les 5 % les plus aisés dépasse de 13 ans celle des 5 % les plus modestes (8 ans pour les femmes). École : 53,7 % des élèves de classes préparatoires sont enfants de cadres (voir <a href="#s2">S2</a>). Logement, emploi, patrimoine, réseau : les avantages s’additionnent.</p></div>' },

    { id: "r1-2", t: "Mesurer les inégalités : outils statiques et dynamiques", h:
      '<h3>1. Les rapports inter-quantiles</h3><p>On range la population par revenu croissant et on la découpe en dix (déciles) ou en cinq (quintiles). En 2024 (niveau de vie annuel par unité de consommation, Insee) : D1 = 13 970 €, médiane = 26 740 €, D9 = 48 580 €.</p><ul><li><b>D9/D1 = 3,48</b> : le seuil des 10 % les plus aisés est 3,48 fois plus élevé que le plafond des 10 % les plus modestes. C’est un rapport de <b>seuils</b>.</li><li><b>(100 − S80)/S20 = 4,62</b> : les 20 % les plus aisés perçoivent une masse de niveaux de vie 4,62 fois plus élevée que les 20 % les plus modestes. C’est un rapport de <b>masses</b> (parts du total).</li></ul>' +
      '<div class="attn"><p>Ces rapports ignorent ce qui se passe à l’intérieur des déciles extrêmes : D9/D1 ne bouge pas si les revenus des 1 % les plus riches doublent. D’où l’intérêt du top 1 %.</p></div>' +
      '<h3>2. La courbe de Lorenz et le coefficient de Gini</h3><div data-anim="r1-lorenz"></div>' +
      '<div class="def"><b>Courbe de Lorenz</b> — courbe qui associe à chaque part cumulée de la population, rangée du plus modeste au plus aisé (en abscisse), la part cumulée des revenus qu’elle reçoit (en ordonnée). L’égalité parfaite est la diagonale.</div>' +
      '<div class="def"><b>Coefficient (indice) de Gini</b> — rapport entre la surface comprise entre la diagonale et la courbe de Lorenz, et la surface totale sous la diagonale. Il vaut 0 en cas d’égalité parfaite et 1 si une seule personne reçoit tout.</div>' +
      '<p>En 2024, les 20 % les plus modestes perçoivent 8,4 % de la masse des niveaux de vie, les 50 % les plus modestes 30,1 %, et les 10 % les plus aisés 24,9 % (Insee). Gini : 0,302. Le Gini résume toute la distribution, mais deux courbes qui se croisent peuvent avoir le même Gini.</p>' +
      '<h3>3. Le top 1 %</h3><p>La <b>part du revenu (ou du patrimoine) détenue par le 1 % le plus aisé</b> mesure la concentration tout en haut. Elle s’appuie sur les données fiscales, plus fiables que les enquêtes pour les très hauts revenus. C’est elle qui révèle la courbe en U du siècle (section 1).</p>' +
      '<h3>4. Un outil dynamique : la corrélation des revenus parents-enfants</h3><p>Les outils précédents sont des photographies. Pour savoir si les inégalités se <b>transmettent</b>, on mesure le lien entre le revenu des parents et celui des enfants devenus adultes : coefficient de <b>corrélation</b> (ou élasticité) entre les rangs ou les revenus. 0 : le revenu des enfants ne dépend pas de celui des parents ; 1 : il en dépend entièrement.</p>' +
      '<div class="ex"><p>Pour les enfants nés entre 1972 et 1981, la corrélation entre le rang de revenu des parents et celui des enfants est de 0,30 en France, contre 0,34 aux États-Unis ; 9,7 % des enfants des 20 % de familles les plus modestes atteignent les 20 % les plus aisés, environ quatre fois moins que les enfants des familles les plus aisées (Gustave Kenedi et Louis Sirugue, note IPP n° 95, 2023). L’OCDE (<i>Un ascenseur social en panne ?</i>, 2018) estimait qu’il faudrait six générations à une famille modeste française pour atteindre le revenu moyen, contre quatre et demie en moyenne dans l’OCDE.</p></div>' +
      '<div class="attn"><p>Une corrélation n’est pas une causalité : elle mesure un lien statistique, sans dire s’il passe par l’héritage, l’école, le réseau ou le lieu de vie (voir la mobilité sociale en <a href="#s3">S3</a>).</p></div>' },

    { id: "r1-3", t: "Égalité des droits, des chances, des situations", h:
      '<div class="def"><b>Égalité des droits</b> — tous les individus sont soumis aux mêmes règles et disposent des mêmes droits civils et politiques. « Les hommes naissent et demeurent libres et égaux en droits » (Déclaration des droits de l’homme et du citoyen, 1789, article 1<sup>er</sup>).</div>' +
      '<div class="ex"><p>Le suffrage universel étendu aux femmes (1944), l’égalité de tous devant l’impôt et la justice, l’interdiction des discriminations à l’embauche.</p></div>' +
      '<div class="def"><b>Égalité des chances</b> — chacun doit avoir les mêmes possibilités d’accéder aux positions sociales, quelle que soit son origine : les inégalités de résultat sont acceptées si elles reflètent le mérite (talent, effort).</div>' +
      '<div class="ex"><p>Bourses sur critères sociaux, éducation prioritaire, conventions d’éducation prioritaire de Sciences Po (2001) : on corrige les handicaps de départ sans égaliser les arrivées.</p></div>' +
      '<div class="def"><b>Égalité des situations (ou des positions, des résultats)</b> — réduction des écarts de conditions de vie réelles entre les individus : revenus, logement, santé.</div>' +
      '<div class="ex"><p>Le salaire minimum, les minima sociaux, la gratuité des soins essentiels réduisent directement les écarts de situation.</p></div>' +
      '<div class="aut"><span class="mono">FD</span><span class="an">François Dubet<small><i>Les Places et les chances</i>, 2010</small></span><span class="ad">Deux conceptions de la justice sociale s’opposent : l’<b>égalité des places</b> (réduire les écarts entre les positions) et l’<b>égalité des chances</b> (permettre à chacun d’accéder à toutes les positions). Dubet défend la priorité de la première : plus les places sont proches, plus les chances sont égales.</span></div>' +
      '<div class="cle"><p>Les trois formes ne s’excluent pas, mais elles entrent en tension : l’égalité des situations peut limiter certaines libertés (impôt) ; l’égalité des chances peut légitimer de fortes inégalités de résultat (« méritocratie »).</p></div>' },

    { id: "r1-4", t: "Quatre conceptions de la justice sociale", h:
      '<p class="lede">La <b>justice sociale</b> désigne la répartition jugée juste des ressources et des positions dans une société. Chaque conception dit quelles inégalités sont acceptables.</p>' +
      '<h3>1. L’utilitarisme</h3><div class="aut"><span class="mono">JB</span><span class="an">Jeremy Bentham et John Stuart Mill<small>1789 ; <i>L’Utilitarisme</i>, 1861</small></span><span class="ad">Est juste ce qui maximise la <b>somme des utilités</b> (le bien-être total) : « le plus grand bonheur du plus grand nombre ».</span></div><p>Les inégalités sont acceptables si elles augmentent le bien-être total. Comme un euro de plus compte davantage pour un pauvre que pour un riche (utilité marginale décroissante), l’utilitarisme peut justifier une redistribution ; mais il peut aussi accepter le sacrifice d’une minorité si la somme augmente.</p>' +
      '<h3>2. Le libertarisme</h3><div class="aut"><span class="mono">RN</span><span class="an">Robert Nozick<small><i>Anarchie, État et utopie</i>, 1974</small></span><span class="ad">Une répartition est juste si les biens ont été <b>acquis</b> et <b>transmis</b> de façon juste (travail, échange libre, don), quel que soit le résultat. L’impôt redistributif est une atteinte aux droits de propriété ; seul un <b>État minimal</b> (police, justice, défense) est légitime.</span></div><p>Friedrich Hayek parle du « mirage de la justice sociale » (1976) : le marché n’est l’œuvre de personne, ses résultats ne peuvent être dits justes ou injustes. Seule compte l’<b>égalité des droits</b> ; toutes les inégalités de situation issues d’échanges libres sont acceptables.</p>' +
      '<h3>3. L’égalitarisme libéral</h3><div class="aut"><span class="mono">JR</span><span class="an">John Rawls<small><i>Théorie de la justice</i>, 1971</small></span><span class="ad">Placés sous un <b>voile d’ignorance</b>, des individus rationnels choisiraient deux principes : 1) des <b>libertés de base égales</b> pour tous ; 2) des inégalités économiques et sociales acceptables seulement si a) elles sont attachées à des positions ouvertes à tous selon une <b>juste égalité des chances</b> et b) elles profitent aux plus défavorisés (<b>principe de différence</b>).</span></div><div data-chain="r1-rawls"></div><div class="ex"><p>Un salaire élevé pour un chirurgien est juste, selon Rawls, s’il est nécessaire pour que des personnes se forment à ce métier long et difficile, et si les plus modestes en bénéficient (soins de qualité accessibles à tous).</p></div>' +
      '<div class="plus"><p>Amartya Sen (prix Nobel 1998, <i>Repenser l’inégalité</i>, 1992) propose d’égaliser les <b>capabilités</b> : les libertés réelles de faire et d’être (se soigner, s’instruire, participer). Deux personnes avec le même revenu n’ont pas les mêmes capabilités si l’une est handicapée.</p></div>' +
      '<h3>4. L’égalitarisme strict</h3><p>La justice exige l’<b>égalité des situations</b> : toute inégalité de revenu ou de condition est suspecte. Gracchus Babeuf et la Conjuration des Égaux (1796) réclamaient l’égalité réelle des biens ; Karl Marx formule le principe « de chacun selon ses capacités, à chacun selon ses besoins » (<i>Critique du programme de Gotha</i>, 1875).</p>' +
      '<div class="tbl"><table><thead><tr><th>Conception</th><th>Égalité visée</th><th>Inégalités acceptées</th><th>Rôle de l’État</th></tr></thead><tbody>' +
      '<tr><td><b>Utilitarisme</b></td><td>Aucune en soi : maximiser le bien-être total</td><td>Celles qui augmentent la somme des utilités</td><td>Variable, selon ce qui maximise le bien-être</td></tr>' +
      '<tr><td><b>Libertarisme</b> (Nozick, Hayek)</td><td>Droits</td><td>Toutes celles issues d’acquisitions et d’échanges libres</td><td>Minimal</td></tr>' +
      '<tr><td><b>Égalitarisme libéral</b> (Rawls)</td><td>Droits et chances</td><td>Celles qui profitent aux plus défavorisés</td><td>Garantir les libertés, l’égalité des chances, redistribuer</td></tr>' +
      '<tr><td><b>Égalitarisme strict</b></td><td>Situations</td><td>Aucune, ou très peu</td><td>Très étendu</td></tr></tbody></table></div>' },

    { id: "r1-5", t: "L’action des pouvoirs publics : instruments, financement, débats", h:
      '<h3>Quatre instruments</h3><ul>' +
      '<li><b>La fiscalité</b>. Un impôt <b>progressif</b> prélève une part plus élevée des revenus élevés (impôt sur le revenu, créé par la loi du 15 juillet 1914 ; droits de succession). Un impôt <b>proportionnel</b> prélève le même taux (CSG, 1991). Un impôt est dit <b>régressif</b> quand il pèse proportionnellement plus sur les modestes : la TVA, car ils consomment une plus grande part de leur revenu.</li>' +
      '<li><b>La protection sociale</b>, créée sous sa forme actuelle en 1945. Logique d’<b>assurance</b> (cotisations, prestations liées aux cotisations : retraites, chômage) et d’<b>assistance</b> (prestations sous conditions de ressources, financées par l’impôt : RSA, prime d’activité, minimum vieillesse). Les prestations sociales représentent 31,9 % du PIB en 2024 (Drees).</li>' +
      '<li><b>Les services collectifs</b> : école, hôpital, transports, culture, gratuits ou peu chers. Ils agissent comme un revenu en nature, qui profite relativement plus aux ménages modestes.</li>' +
      '<li><b>La lutte contre les discriminations</b> : interdiction légale (le Défenseur des droits, institué en 2011, peut être saisi), testings, mesures de discrimination positive (parité en politique, loi du 6 juin 2000 ; éducation prioritaire).</li></ul>' +
      '<div data-graph="r1-redis"></div><div data-chain="r1-redis"></div>' +
      '<div class="ex"><p>Une vaste campagne de testing auprès de grandes entreprises, publiée par la Dares, a montré qu’à profil identique, les candidats dont le nom suggère une origine maghrébine avaient en moyenne environ 31,5 % de chances de moins d’être recontactés (Dares Analyses, novembre 2021).</p></div>' +
      '<h3>La contrainte de financement</h3><p>Ces politiques coûtent cher : les prélèvements obligatoires (impôts et cotisations sociales) atteignent 43,6 % du PIB en 2025 et le déficit public 5,1 % du PIB (Insee). Toute dépense nouvelle exige des recettes nouvelles, des économies ailleurs ou de la dette.</p>' +
      '<h3>Trois débats</h3>' +
      '<p><b>L’efficacité</b> : réduit-on vraiment les inégalités ? La redistribution divise le rapport D9/D1 par 1,7 en 2024. Mais une partie des personnes éligibles ne demandent pas les aides : selon la Drees, environ un tiers des foyers éligibles au RSA ne le perçoivent pas (<b>non-recours</b>). Et les prestations universelles profitent aussi aux aisés.</p>' +
      '<p><b>La légitimité</b> : le <b>consentement à l’impôt</b> est au cœur de la démocratie (article 14 de la Déclaration de 1789 : les citoyens ont le droit de constater la nécessité de la contribution publique et de la « consentir librement »). Il s’affaiblit quand l’impôt paraît injuste ou inutile : le mouvement des gilets jaunes est né en novembre 2018 du refus d’une hausse de la fiscalité sur les carburants.</p>' +
      '<p><b>Les effets pervers</b> : des prélèvements trop élevés ou des aides mal conçues peuvent décourager le travail ou l’investissement.</p><div data-chain="r1-pervers"></div>' +
      '<div class="plus"><p>La « courbe de Laffer » (économiste américain Arthur Laffer, années 1970) illustre l’idée que « trop d’impôt tue l’impôt » : au-delà d’un certain taux, les recettes baissent. Le niveau de ce taux fait débat parmi les économistes.</p></div>' +
      '<div class="cle"><p>Ces débats renvoient aux conceptions de la justice : un libertarien juge la redistribution illégitime ; un rawlsien l’accepte tant qu’elle améliore le sort des plus défavorisés, y compris en tenant compte des effets incitatifs ; un égalitariste strict la juge insuffisante.</p></div>' }
  ],
  pieges: [
    { f: "« D9/D1 = 3,48 : les 10 % les plus riches gagnent 3,48 fois plus que les 10 % les plus pauvres. »", v: "C’est un rapport de <b>seuils</b> : le plancher des 10 % les plus aisés est 3,48 fois le plafond des 10 % les plus modestes. Le rapport des <b>masses</b> serait bien plus élevé." },
    { f: "« Un Gini de 0,302 signifie que 30,2 % de la population est pauvre. »", v: "Le Gini mesure la <b>concentration</b> de toute la distribution (0 = égalité, 1 = un seul reçoit tout). Le taux de pauvreté est un autre indicateur (15,4 % en 2024)." },
    { f: "« Plus la courbe de Lorenz est proche de la diagonale, plus la société est inégalitaire. »", v: "C’est l’inverse : la diagonale est l’égalité parfaite ; plus la courbe s’en <b>éloigne</b>, plus la répartition est inégale." },
    { f: "« L’égalité des chances, c’est que tout le monde ait le même revenu. »", v: "L’égalité des chances porte sur les <b>possibilités au départ</b> ; l’égalité de revenu est une égalité des <b>situations</b>." },
    { f: "« Rawls veut l’égalité stricte. »", v: "Il accepte les inégalités <b>si elles profitent aux plus défavorisés</b> (principe de différence) et si les positions sont ouvertes à tous." },
    { f: "« La TVA est un impôt progressif. »", v: "Son taux est le même pour tous, mais elle pèse proportionnellement plus sur les ménages modestes, qui consomment une plus grande part de leur revenu : elle est <b>régressive</b> par rapport au revenu." },
    { f: "Confondre corrélation parents-enfants et causalité.", v: "Une corrélation de 0,30 mesure un lien statistique ; elle ne dit pas par quel canal (héritage, école, réseau, lieu) passe la transmission." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Inégalités</b> : économiques (revenu, patrimoine) et sociales (école, santé, logement…), <b>multiformes</b> et <b>cumulatives</b>.</li>' +
    '<li><b>Tendance</b> : U au XX<sup>e</sup> siècle (top 1 % ≈ un cinquième des revenus avant 1914, &lt; 8 % en 1983, &gt; 12 % en 2007 ; Piketty, r &gt; g).</li>' +
    '<li><b>Outils</b> : D9/D1 (seuils), (100 − S80)/S20 (masses), courbe de Lorenz, Gini (0 à 1), top 1 %, corrélation des revenus parents-enfants (France : 0,30).</li>' +
    '<li><b>Égalités</b> : des droits (DDHC, art. 1), des chances (mérite), des situations (conditions réelles). Dubet : places contre chances.</li>' +
    '<li><b>Conceptions</b> : utilitarisme (Bentham, Mill : maximiser le bien-être total) ; libertarisme (Nozick 1974, Hayek : droits de propriété, État minimal) ; égalitarisme libéral (Rawls 1971 : voile d’ignorance, libertés égales, égalité équitable des chances, principe de différence ; Sen : capabilités) ; égalitarisme strict (égalité des situations).</li>' +
    '<li><b>Instruments</b> : fiscalité (progressive, proportionnelle, régressive), protection sociale (assurance / assistance), services collectifs, lutte contre les discriminations.</li>' +
    '<li><b>Débats</b> : efficacité (non-recours), légitimité (consentement à l’impôt, art. 14 DDHC, gilets jaunes), effets pervers (désincitations, Laffer), sous contrainte de financement.</li></ul>' +
    '<h3>Chiffres à citer</h3><ul><li>Niveau de vie 2024 : D9/D1 = 3,48 ; S80/S20 = 4,62 ; Gini 0,302 ; avant redistribution D9/D1 = 5,89, Gini 0,378 (Insee).</li><li>Patrimoine 2021 : la moitié la moins dotée détient 8 % ; D1 4 400 €, D9 716 300 € ; Gini 0,662.</li><li>Prélèvements obligatoires 43,6 % du PIB (2025) ; prestations sociales 31,9 % du PIB (2024).</li></ul>',
  chainesFiche: ["r1-u", "r1-cumul", "r1-rawls", "r1-redis", "r1-pervers"],
  quiz: [
    { q: "Au XXe siècle, en France, la part des revenus reçue par le 1 % le plus aisé…", c: ["baisse fortement jusqu’au début des années 1980, puis remonte", "augmente sans interruption", "reste stable autour de 10 %", "baisse sans interruption"], r: 0, e: "Courbe en U : environ un cinquième avant 1914, moins de 8 % en 1983, plus de 12 % en 2007 (Garbinti, Goupille-Lebret, Piketty).", s: "r1-1" },
    { q: "Dire que les inégalités sont cumulatives signifie que…", c: ["les avantages (ou handicaps) dans un domaine favorisent ceux d’autres domaines", "elles augmentent chaque année", "on peut les additionner en euros", "elles ne concernent que le patrimoine"], r: 0, e: "Revenu, logement, école, santé, patrimoine se renforcent : 13 ans d’écart d’espérance de vie entre les hommes les plus aisés et les plus modestes.", s: "r1-1" },
    { q: "Début 2021, la moitié la moins dotée des ménages détient environ…", c: ["8 % du patrimoine brut", "50 % du patrimoine brut", "30 % du patrimoine brut", "1 % du patrimoine brut"], r: 0, e: "L’autre moitié en détient 92 % (Insee). Le patrimoine est beaucoup plus concentré que le revenu.", s: "r1-1" },
    { q: "En 2024, le rapport D9/D1 des niveaux de vie vaut 3,48. Cela signifie que…", c: ["le seuil des 10 % les plus aisés est 3,48 fois plus élevé que le plafond des 10 % les plus modestes", "les 10 % les plus aisés reçoivent 3,48 fois plus de revenus au total", "le revenu moyen a été multiplié par 3,48", "3,48 % de la population est pauvre"], r: 0, e: "C’est un rapport de seuils (48 580 € ÷ 13 970 €).", s: "r1-2" },
    { q: "Sur une courbe de Lorenz, si les 20 % les plus modestes reçoivent 8,4 % des revenus…", c: ["le point (20 % ; 8,4 %) est sous la diagonale", "le point est sur la diagonale", "le point est au-dessus de la diagonale", "la courbe est horizontale"], r: 0, e: "La diagonale correspondrait à (20 % ; 20 %). Plus la courbe est basse, plus la répartition est inégale.", s: "r1-2" },
    { q: "Un coefficient de Gini égal à 0 correspond…", c: ["à l’égalité parfaite", "à l’inégalité maximale", "à une société sans revenu", "à un taux de pauvreté nul"], r: 0, e: "0 : tout le monde reçoit la même part ; 1 : une seule personne reçoit tout.", s: "r1-2" },
    { q: "Pourquoi mesurer la part du top 1 % en plus du rapport D9/D1 ?", c: ["Parce que D9/D1 ne voit pas ce qui se passe tout en haut de la distribution", "Parce que D9/D1 est toujours faux", "Parce que le top 1 % mesure la pauvreté", "Parce que le top 1 % est un outil dynamique"], r: 0, e: "Les revenus des 1 % les plus aisés peuvent exploser sans changer le seuil D9.", s: "r1-2" },
    { q: "Une corrélation des rangs de revenu parents-enfants de 0,30 en France signifie que…", c: ["le revenu des enfants reste en partie lié à celui des parents", "30 % des enfants ont le même revenu que leurs parents", "les enfants gagnent 30 % de plus que leurs parents", "la transmission est parfaite"], r: 0, e: "0 = aucun lien, 1 = lien total. C’est un outil dynamique (Kenedi et Sirugue, 2023 ; 0,34 aux États-Unis).", s: "r1-2" },
    { q: "Les bourses sur critères sociaux visent surtout…", c: ["l’égalité des chances", "l’égalité des droits", "l’égalité stricte des situations", "la maximisation du bien-être total"], r: 0, e: "On corrige les handicaps de départ pour que chacun puisse accéder aux positions selon son mérite.", s: "r1-3" },
    { q: "Pour l’utilitarisme, une situation est juste si…", c: ["elle maximise la somme des utilités", "elle respecte les droits de propriété", "elle profite aux plus défavorisés", "tout le monde a la même situation"], r: 0, e: "Bentham, Mill : « le plus grand bonheur du plus grand nombre ».", s: "r1-4" },
    { q: "Pour Robert Nozick, l’impôt redistributif…", c: ["porte atteinte aux droits de propriété légitimement acquis", "est indispensable à la justice", "doit financer l’égalité des situations", "doit maximiser le bien-être total"], r: 0, e: "Libertarisme : une répartition issue d’acquisitions et d’échanges justes est juste ; l’État doit être minimal.", s: "r1-4" },
    { q: "Le principe de différence de Rawls affirme que les inégalités sont justes si…", c: ["elles profitent aux plus défavorisés", "elles résultent d’échanges libres", "elles augmentent le PIB", "elles sont temporaires"], r: 0, e: "Et à condition que les libertés de base soient égales et que les positions soient ouvertes selon une juste égalité des chances.", s: "r1-4" },
    { q: "La TVA est dite régressive par rapport au revenu parce que…", c: ["les ménages modestes consomment une plus grande part de leur revenu", "son taux baisse quand le revenu augmente", "elle n’est payée que par les pauvres", "elle finance la protection sociale"], r: 0, e: "Même taux pour tous, mais une part plus lourde du revenu des modestes.", s: "r1-5" },
    { q: "Le non-recours désigne…", c: ["le fait que des personnes éligibles à une aide ne la demandent pas", "le refus de payer l’impôt", "l’exil fiscal", "l’absence de recours en justice"], r: 0, e: "Environ un tiers des foyers éligibles au RSA ne le perçoivent pas (Drees) : c’est un problème d’efficacité.", s: "r1-5" },
    { q: "Le consentement à l’impôt relève du débat sur…", c: ["la légitimité de l’action publique", "l’efficacité de la redistribution", "les désincitations", "la mesure du Gini"], r: 0, e: "Article 14 de la Déclaration de 1789 ; les gilets jaunes (2018) ont exprimé un refus de la fiscalité jugée injuste.", s: "r1-5" }
  ],
  cartes: [
    { r: "Inégalités multiformes et cumulatives", v: "Elles touchent revenu, patrimoine, école, santé, logement… et se renforcent mutuellement." },
    { r: "Courbe en U des inégalités (France, XXe siècle)", v: "Top 1 % ≈ un cinquième des revenus avant 1914, moins de 8 % en 1983, plus de 12 % en 2007 (Garbinti, Goupille-Lebret, Piketty)." },
    { r: "Rapport interdécile D9/D1", v: "Seuil des 10 % les plus aisés ÷ plafond des 10 % les plus modestes. Niveau de vie 2024 : 3,48 (5,89 avant redistribution)." },
    { r: "Rapport (100 − S80)/S20", v: "Masse reçue par les 20 % les plus aisés ÷ masse reçue par les 20 % les plus modestes : 4,62 en 2024." },
    { r: "Courbe de Lorenz", v: "Part cumulée des revenus (ordonnée) reçue par chaque part cumulée de la population rangée du plus modeste au plus aisé (abscisse). Diagonale = égalité." },
    { r: "Coefficient de Gini", v: "Surface entre la diagonale et la courbe de Lorenz ÷ surface sous la diagonale. 0 = égalité, 1 = inégalité maximale. Niveau de vie 2024 : 0,302." },
    { r: "Top 1 %", v: "Part du revenu ou du patrimoine détenue par le 1 % le plus aisé ; révèle la concentration au sommet." },
    { r: "Corrélation des revenus parents-enfants", v: "Mesure dynamique de la transmission des inégalités : 0,30 en France (rangs), 0,34 aux États-Unis (Kenedi et Sirugue, 2023)." },
    { r: "Égalité des droits / des chances / des situations", v: "Droits : mêmes règles pour tous. Chances : mêmes possibilités d’accès aux positions. Situations : conditions de vie réelles rapprochées." },
    { r: "Utilitarisme", v: "Est juste ce qui maximise la somme des utilités (Bentham, Mill)." },
    { r: "Libertarisme", v: "Est juste ce qui résulte d’acquisitions et d’échanges libres ; État minimal (Nozick, 1974 ; Hayek)." },
    { r: "Égalitarisme libéral (Rawls, 1971)", v: "Voile d’ignorance ; libertés égales ; juste égalité des chances ; inégalités justes si elles profitent aux plus défavorisés (principe de différence)." },
    { r: "Égalitarisme strict", v: "La justice exige l’égalité des situations (Babeuf ; Marx : « à chacun selon ses besoins »)." },
    { r: "Capabilités (Sen)", v: "Libertés réelles de faire et d’être ; l’égalité doit porter sur elles plutôt que sur les seuls revenus." },
    { r: "Impôt progressif / proportionnel / régressif", v: "Progressif : taux qui augmente avec le revenu (IR). Proportionnel : même taux (CSG). Régressif : pèse plus sur les modestes (TVA, rapportée au revenu)." },
    { r: "Assurance / assistance", v: "Assurance : prestations financées par des cotisations (retraite, chômage). Assistance : sous conditions de ressources, financées par l’impôt (RSA)." },
    { r: "Consentement à l’impôt", v: "Acceptation par les citoyens de payer l’impôt, condition de sa légitimité (art. 14 DDHC)." },
    { r: "Désincitations (effets pervers)", v: "Prélèvements ou aides qui découragent le travail ou l’investissement (trappe à inactivité, courbe de Laffer)." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice inventé pour le site, données Insee", t: "Lire une courbe de Lorenz et des rapports inter-quantiles", enonce:
      '<p>En 2024 (Insee), les 20 % de personnes les plus modestes perçoivent 8,4 % de la masse des niveaux de vie, les 50 % les plus modestes 30,1 %, les 80 % les plus modestes 61,2 % et les 90 % les plus modestes 75,1 %.</p><ol><li>Quelle part de la masse perçoivent les 20 % les plus aisés ? les 10 % les plus aisés ?</li><li>Calcule le rapport (100 − S80)/S20 et rédige une phrase.</li><li>Place ces points sur une courbe de Lorenz : où se situent-ils par rapport à la diagonale ?</li></ol>',
      corrige: '<ol><li>Les 20 % les plus aisés : 100 − 61,2 = 38,8 % ; les 10 % les plus aisés : 100 − 75,1 = 24,9 %.</li><li>38,8 ÷ 8,4 ≈ 4,62. « En 2024, selon l’Insee, les 20 % de personnes les plus aisées perçoivent une masse de niveaux de vie 4,62 fois plus élevée que les 20 % les plus modestes. »</li><li>Points (20 ; 8,4), (50 ; 30,1), (80 ; 61,2), (90 ; 75,1) : tous sous la diagonale (qui passerait par (20 ; 20), (50 ; 50)…), ce qui traduit une répartition inégale. L’écart à la diagonale est le plus grand vers le milieu de la distribution (50 − 30,1 ≈ 20 points).</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Distinguez égalité des chances et égalité des situations.", enonce: "<p>Sans document. Rappel : cette question n’est pas évaluée à l’écrit en 2027 ; l’exercice entraîne la méthode.</p>",
      corrige: '<div class="copie"><p>L’égalité est un idéal des sociétés démocratiques, mais elle peut porter sur des objets différents.</p><p>L’égalité des chances vise à donner à chacun les mêmes possibilités d’accéder aux différentes positions sociales, quelle que soit son origine. Elle accepte les inégalités de résultat si elles reflètent le mérite, c’est-à-dire le talent et l’effort. Les bourses sur critères sociaux ou l’éducation prioritaire en sont des exemples : on corrige les handicaps de départ, sans égaliser les arrivées. Elle se mesure par exemple par la corrélation des revenus parents-enfants, de 0,30 en France.</p><p>L’égalité des situations vise au contraire à réduire directement les écarts de conditions de vie réelles : revenus, logement, santé. Le salaire minimum, les minima sociaux ou la gratuité des soins y contribuent. La redistribution réduit ainsi le rapport D9/D1 des niveaux de vie de 5,89 à 3,48 en 2024 selon l’Insee.</p><p>Les deux se complètent mais peuvent s’opposer : François Dubet montre que plus les places sont inégales, plus la compétition pour y accéder est rude, ce qui rend l’égalité des chances plus difficile à atteindre.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice inventé pour le site, document Insee", t: "Ce que change la redistribution", enonce:
      '<p>Document : le graphique « Ce que change la redistribution, 2024 » du <a href="#r1:r1-5">cours</a> (Insee).</p><ol><li>Présentez l’effet de la redistribution sur le rapport D9/D1. (2 points)</li><li>À l’aide du document et de vos connaissances, montrez que l’action des pouvoirs publics réduit les inégalités mais fait l’objet de débats. (4 points)</li></ol>',
      corrige: '<ol><li>Selon l’Insee, en 2024, avant redistribution, le niveau de vie plancher des 10 % les plus aisés est 5,89 fois plus élevé que le plafond des 10 % les plus modestes ; après impôts directs et prestations sociales, ce rapport n’est plus que de 3,48 : il est divisé par 1,7 environ.</li><li>La redistribution réduit les inégalités par des prélèvements progressifs (impôt sur le revenu), des prestations sous conditions de ressources (RSA, prime d’activité, aides au logement) et des services collectifs gratuits. Le rapport des masses (100 − S80)/S20 passe ainsi de 8,37 à 4,62. Mais elle fait débat. Son <b>efficacité</b> est limitée par le non-recours (environ un tiers des foyers éligibles au RSA ne le perçoivent pas) et par des impôts régressifs comme la TVA. Sa <b>légitimité</b> dépend du consentement à l’impôt, mis à l’épreuve par les gilets jaunes en 2018, dans un pays où les prélèvements obligatoires atteignent 43,6 % du PIB (2025). Enfin, elle peut avoir des <b>effets pervers</b> : des taux marginaux élevés ou des aides qui diminuent quand on reprend un emploi peuvent décourager le travail, d’où la création de la prime d’activité en 2016.</li></ol>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Toutes les inégalités sont-elles injustes ?", enonce: "<p>Construis la problématique et le plan, puis compare. Rappel : question non évaluée à l’écrit en 2027 ; sujet utile pour le Grand oral.</p>",
      corrige: '<p><b>Problématique.</b> Les inégalités de revenu et de patrimoine ont augmenté depuis les années 1980 (Gini 0,302 en 2024). Mais juger qu’une inégalité est injuste suppose un critère de justice : selon la conception retenue, certaines inégalités sont acceptables, d’autres non.</p><p><b>I. Certaines inégalités peuvent être jugées justes</b><br>A. Libertarisme : inégalités issues d’échanges libres et d’acquisitions justes (Nozick, Hayek).<br>B. Utilitarisme : inégalités qui augmentent le bien-être total (incitations à innover, à se former).<br>C. Égalitarisme libéral : inégalités qui profitent aux plus défavorisés et sont ouvertes à tous (Rawls).</p><p><b>II. Mais beaucoup d’inégalités sont injustes</b><br>A. Elles ne reflètent pas le mérite : corrélation parents-enfants de 0,30, 9,7 % seulement des enfants modestes atteignent le haut (Kenedi et Sirugue) ; discriminations (testing).<br>B. Elles sont cumulatives : patrimoine (8 % pour la moitié la moins dotée), santé (13 ans d’espérance de vie).<br>C. Elles menacent la cohésion et les capabilités (Sen) ; égalitarisme strict.</p><p><b>III. D’où une action publique, elle-même débattue</b><br>A. Fiscalité, protection sociale, services collectifs, lutte contre les discriminations (D9/D1 de 5,89 à 3,48).<br>B. Sous contrainte de financement et de légitimité (43,6 % du PIB de prélèvements, consentement à l’impôt).<br>C. Avec un risque d’effets pervers (désincitations) qu’il faut limiter.</p>' }
  ]
};

AUTEURS.push(
  { ch: "r1", n: "Thomas Piketty", d: "né en 1971", th: "Courbe en U des inégalités ; r > g", l: "<i>Le Capital au XXIe siècle</i> (2013) : quand le rendement du capital dépasse la croissance, les patrimoines hérités prennent le dessus ; la baisse des inégalités au XXe siècle tient aux chocs et aux politiques fiscales et sociales." },
  { ch: "r1", n: "Simon Kuznets", d: "1901-1985 · Nobel 1971", th: "Les inégalités augmentent puis diminuent avec le développement", l: "Hypothèse de 1955 : une courbe en U inversé reliant développement et inégalités ; remise en cause par la remontée des inégalités depuis 1980." },
  { ch: "r1", n: "Jeremy Bentham et John Stuart Mill", d: "1748-1832 ; 1806-1873", th: "Utilitarisme : maximiser la somme des utilités", l: "Est juste ce qui produit « le plus grand bonheur du plus grand nombre » (Bentham, 1789 ; Mill, <i>L’Utilitarisme</i>, 1861)." },
  { ch: "r1", n: "Robert Nozick", d: "1938-2002", th: "Libertarisme : droits de propriété, État minimal", l: "<i>Anarchie, État et utopie</i> (1974) : une répartition est juste si les biens ont été acquis et transmis de façon juste ; l’impôt redistributif viole les droits." },
  { ch: "r1", n: "Friedrich Hayek", d: "1899-1992 · Nobel 1974", th: "« Le mirage de la justice sociale »", l: "Les résultats du marché ne sont voulus par personne : on ne peut les dire justes ou injustes (1976). Seule compte l’égalité devant la loi." },
  { ch: "r1", n: "John Rawls", d: "1921-2002", th: "Égalitarisme libéral : voile d’ignorance, principe de différence", l: "<i>Théorie de la justice</i> (1971) : libertés de base égales ; inégalités acceptables si positions ouvertes à tous (juste égalité des chances) et si elles profitent aux plus défavorisés." },
  { ch: "r1", n: "Amartya Sen", d: "né en 1933 · Nobel 1998", th: "Égalité des capabilités", l: "<i>Repenser l’inégalité</i> (1992) : il faut égaliser les libertés réelles de faire et d’être (capabilités), pas seulement les revenus." },
  { ch: "r1", n: "François Dubet", d: "<i>Les Places et les chances</i>, 2010", th: "Égalité des places ou égalité des chances", l: "Défend la priorité de l’égalité des places (réduire les écarts entre positions), condition d’une réelle égalité des chances." }
);

ANIMS["r1-lorenz"] = {
  t: "Quand les inégalités montent, la courbe de Lorenz se creuse",
  h: 330,
  src: "Étapes 1 à 4 : société fictive de cinq personnes (calculs du Gini vérifiés). Étape 5 : Insee Première n° 2117 (niveaux de vie 2024). Étape 6 : Insee, enquête Histoire de vie et Patrimoine 2020-2021 ; seul le point médian de la courbe du patrimoine est publié, il est seul représenté.",
  etapes: [
    { l: "Cinq personnes se partagent 100 € de revenus. On les range de la plus modeste à la plus aisée. À égalité parfaite (20 € chacune), les 20 % les plus modestes ont 20 % du total : la courbe de Lorenz se confond avec la diagonale. Gini = 0.", d: 4.5, r: [20, 20, 20, 20, 20] },
    { l: "Les revenus s’écartent : 10, 15, 20, 25, 30 €. Les 20 % les plus modestes n’ont plus que 10 % du total ; la courbe se creuse sous la diagonale. Gini = 0,20.", d: 4.5, r: [10, 15, 20, 25, 30] },
    { l: "Les inégalités montent : 5, 10, 15, 20 et 50 €. La personne la plus aisée reçoit la moitié du total. Gini = 0,40.", d: 4.5, r: [5, 10, 15, 20, 50] },
    { l: "Encore plus concentré : 2, 4, 8, 16 et 70 €. La surface entre la diagonale et la courbe grandit : le coefficient de Gini est cette surface rapportée à toute l’aire sous la diagonale. Gini ≈ 0,59.", d: 5, r: [2, 4, 8, 16, 70] },
    { l: "La France en 2024 (niveaux de vie) : les 20 % les plus modestes perçoivent 8,4 % du total, les 50 % les plus modestes 30,1 %, les 10 % les plus aisés 24,9 %. Gini publié par l’Insee : 0,302.", d: 5 },
    { l: "Le patrimoine est bien plus concentré : début 2021, la moitié la moins dotée des ménages ne détient que 8 % du patrimoine brut. Gini du patrimoine : 0,662, plus du double de celui du niveau de vie.", d: 5 }
  ],
  rendu: function (A, i, p) {
    var X0 = 34, Y0 = 268, S = 200, s = "";
    var X = function (v) { return X0 + S * v / 100; }, Y = function (v) { return Y0 - S * v / 100; };
    function courbeRev(r) { var tot = r.reduce(function (a, b) { return a + b; }, 0), c = 0, pts = [[0, 0]]; r.forEach(function (v, k) { c += v; pts.push([20 * (k + 1), 100 * c / tot]); }); return pts; }
    var FR = [[0, 0], [20, 8.4], [40, 21.9], [50, 30.1], [80, 61.2], [90, 75.1], [100, 100]];
    function val(pts, x) { for (var k = 1; k < pts.length; k++) if (x <= pts[k][0]) { var a = pts[k - 1], b = pts[k]; return a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0]); } return 100; }
    var ets = this.etapes;
    function courbeEtape(k) { return k <= 3 ? courbeRev(ets[k].r) : FR; }
    var grille = []; for (var g = 0; g <= 100; g += 10) grille.push(g);
    var cible = i <= 4 ? courbeEtape(i) : FR, avant = i === 0 ? courbeEtape(0) : courbeEtape(Math.min(i - 1, 4));
    var m = i === 5 ? 1 : A.s(p, 0.05, 0.6);
    var cur = grille.map(function (x) { return [x, A.l(val(avant, x), val(cible, x), m)]; });
    s += A.r(X0, Y0 - S, S, S, { f: "carte", s: "ligne", r: 0 });
    [20, 40, 60, 80].forEach(function (v) { s += '<line x1="' + X(v) + '" x2="' + X(v) + '" y1="' + Y(0) + '" y2="' + Y(100) + '" style="stroke:var(--ligne);stroke-width:1"/><line x1="' + X(0) + '" x2="' + X(100) + '" y1="' + Y(v) + '" y2="' + Y(v) + '" style="stroke:var(--ligne);stroke-width:1"/>'; });
    var aire = cur.map(function (q) { return X(q[0]).toFixed(1) + "," + Y(q[1]).toFixed(1); }).join(" ");
    s += '<polygon points="' + aire + " " + X(0) + "," + Y(0) + '" style="fill:var(--corail);opacity:.18"/>';
    s += A.pl([[X(0), Y(0)], [X(100), Y(100)]], 1, { c: "gris", sw: 1.5, tir: true });
    s += A.pl(cur.map(function (q) { return [X(q[0]), Y(q[1])]; }), 1, { c: "corail", sw: 3 });
    for (var t = 0; t <= 100; t += 50) { s += A.t(X(t), Y0 + 14, t + " %", { t: 9.5, a: "middle", c: "gris" }) + A.t(X0 - 4, Y(t) + 3, t + " %", { t: 9.5, a: "end", c: "gris" }); }
    s += A.t(X0 + S / 2, Y0 + 30, "part cumulée de la population →", { t: 10.5, a: "middle", c: "gris" });
    s += A.t(X0 + 4, Y0 - S - 8, "↑ part cumulée des revenus", { t: 10.5, c: "gris" });
    s += A.t(X(3), Y(30), "égalité parfaite", { t: 10, c: "gris", it: true, h: true });
    var aireT = 0; for (var k = 1; k < cur.length; k++) aireT += (cur[k][0] - cur[k - 1][0]) * (cur[k][1] + cur[k - 1][1]) / 2;
    var gini = 1 - 2 * aireT / 10000;
    var px = 254;
    if (i <= 3) {
      var rv = ets[i].r, rav = ets[i === 0 ? 0 : i - 1].r;
      s += A.t(px + 46, 26, "Revenus (€)", { t: 11, g: true, a: "middle" });
      rv.forEach(function (v, k2) {
        var vv = A.l(rav[k2], v, m), h = 1.6 * vv, x = px + k2 * 19;
        s += A.r(x, 200 - h, 15, h, { f: k2 === 4 ? "corail" : "canard", r: 3 }) + A.t(x + 7.5, 196 - h, String(Math.round(vv)), { t: 9.5, a: "middle", g: true });
      });
      s += '<line x1="' + px + '" x2="' + (px + 94) + '" y1="200" y2="200" style="stroke:var(--gris);stroke-width:1"/>';
      s += A.t(px + 46, 230, "Gini", { t: 12, a: "middle", c: "gris" }) + A.t(px + 46, 256, A.fr(Math.max(0, gini), 2), { t: 24, g: true, a: "middle", c: "corail", f: true });
    } else {
      s += A.t(px + 46, 60, i === 4 ? "France, 2024" : "Gini", { t: 12, g: true, a: "middle" });
      if (i === 4) {
        s += A.t(px + 46, 84, "niveau de vie", { t: 10.5, a: "middle", c: "gris" }) + A.t(px + 46, 124, "Gini (Insee)", { t: 11, a: "middle", c: "gris", op: A.s(p, 0.5, 0.8) }) + A.t(px + 46, 152, "0,302", { t: 26, g: true, a: "middle", c: "corail", f: true, op: A.s(p, 0.5, 0.8) });
        [[20, 8.4], [50, 30.1], [90, 75.1]].forEach(function (q, k3) { var op = A.s(p, 0.55 + 0.1 * k3, 0.75 + 0.1 * k3); s += A.cercle(X(q[0]), Y(q[1]), 4, { f: "encre", op: op }) + A.t(X(q[0]) + 6, Y(q[1]) + 12, A.fr(q[1], 1) + " %", { t: 10, g: true, op: op, h: true }); });
      } else {
        var q5 = A.s(p, 0.15, 0.6);
        s += A.jauge(px - 6, 92, 104, 0.302, 1, { c: "corail", l: "Revenu", val: "0,302" });
        s += A.jauge(px - 6, 136, 104, 0.662 * q5, 1, { c: "canard", l: "Patrimoine", val: A.fr(0.662 * q5, 3) });
        s += A.cercle(X(50), Y(8), 5, { f: "canard", op: q5 }) + A.t(X(50) + 8, Y(8) - 6, "50 % → 8 %", { t: 11, g: true, c: "canard", op: q5, h: true });
        s += '<line x1="' + X(50) + '" x2="' + X(50) + '" y1="' + Y(8) + '" y2="' + Y(50) + '" style="stroke:var(--canard);stroke-width:1.5;stroke-dasharray:3 3;opacity:' + q5 + '"/>';
        s += A.t(px + 46, 186, "Patrimoine brut,", { t: 10, a: "middle", c: "gris", op: q5 }) + A.t(px + 46, 200, "début 2021", { t: 10, a: "middle", c: "gris", op: q5 });
      }
    }
    return s;
  }
};
