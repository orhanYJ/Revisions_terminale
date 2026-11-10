GRAPHES["e2-monde"] = {
  type: "hbarres", t: "Le commerce mondial en 2024", s: "Exportations mondiales, en milliers de milliards de dollars.",
  src: "Source : OMC, Perspectives et statistiques du commerce mondial (avril 2025). Marchandises : y compris le commerce entre pays de l’Union européenne.",
  unite: "", dec: 2, cats: ["Marchandises", "Services commerciaux", "dont Chine (marchandises)"], series: [{ n: "2024", v: [24.43, 8.69, 3.58], c: 1 }], lab: 170
};
GRAPHES["e2-france"] = {
  type: "hbarres", t: "Le commerce extérieur de biens de la France en 2025", s: "En milliards d’euros. Exportations FAB, importations CAF ; le solde officiel est calculé FAB/FAB.",
  src: "Source : Douane, résultats du commerce extérieur pour l’année 2025 (9 février 2026).",
  unite: "", cats: ["Exportations de biens", "Importations de biens", "Solde commercial (FAB/FAB)"], series: [{ n: "2025", v: [614.7, 703.6, -69.2], c: 1 }], lab: 170
};
GRAPHES["e2-iphone"] = {
  type: "hbarres", t: "Qui produit la valeur d’un iPhone 3G ? (2009)", s: "Coût de fabrication estimé d’un iPhone 3G, en dollars (total : 178,96 $).",
  src: "Source : Y. Xing et N. Detert, « How the iPhone Widens the United States Trade Deficit with the People’s Republic of China », ADBI Working Paper n° 257, décembre 2010, d’après des estimations du cabinet iSuppli (2009).",
  unite: " $", dec: 2, cats: ["Composants achetés aux fournisseurs (Japon, Allemagne, Corée du Sud, États-Unis…)", "Assemblage en Chine"], series: [{ n: "Coût", v: [172.46, 6.50], c: 1 }], lab: 200
};

CHAINES["e2-ricardo"] = { t: "Pourquoi l’échange profite aux deux pays (Ricardo)", e: [
  { t: "Chaque pays compare ses coûts relatifs : combien d’un bien il « sacrifie » pour produire l’autre", k: "cause" },
  { t: "Il se spécialise là où son avantage est le plus grand, ou son désavantage le plus faible : l’avantage comparatif", a: "donc" },
  { t: "Avec les mêmes heures de travail, la production mondiale totale augmente", a: "donc" },
  { t: "En échangeant, chaque pays consomme plus qu’en autarcie", k: "effet", a: "donc" }
] };
CHAINES["e2-hos"] = { t: "Les dotations factorielles (HOS)", e: [
  { t: "Un pays est relativement abondant en travail peu qualifié (ex. : le Bangladesh)", k: "cause" },
  { t: "Ce facteur y est relativement bon marché", a: "donc" },
  { t: "Les biens qui en utilisent beaucoup (textile, habillement) y sont produits à bas coût", a: "donc" },
  { t: "Il se spécialise dans ces biens, les exporte et importe des biens intensifs en capital ou en travail qualifié", k: "effet", a: "donc" }
] };
CHAINES["e2-krugman"] = { t: "Le commerce entre pays comparables (Krugman)", e: [
  { t: "Rendements croissants : plus une firme produit, plus son coût unitaire baisse (économies d’échelle)", k: "cause" },
  { t: "Chaque firme se concentre sur quelques variétés produites en grande série", a: "donc" },
  { t: "Les consommateurs aiment la variété : ils veulent choisir entre plusieurs marques et modèles", a: "or" },
  { t: "Des pays semblables échangent des variétés d’un même produit : commerce intra-branche", a: "donc" },
  { t: "Plus de choix et des prix plus bas pour les consommateurs des deux pays", k: "effet", a: "donc" }
] };
CHAINES["e2-compet"] = { t: "De la productivité des firmes à la compétitivité du pays", e: [
  { t: "La productivité des firmes augmente (innovation, équipement, organisation, qualification)", k: "cause" },
  { t: "Le coût unitaire de production baisse", a: "donc" },
  { f: [{ t: "Compétitivité-prix : elles peuvent vendre moins cher à l’étranger" }, { t: "Marges plus élevées : elles investissent en R&D, qualité, marque (compétitivité hors-prix)" }], a: "deux voies" },
  { t: "Elles gagnent des parts de marché à l’étranger", a: "donc" },
  { t: "Les exportations du pays augmentent : il est plus compétitif", k: "effet", a: "donc" }
] };
CHAINES["e2-melitz"] = { t: "Seules les firmes les plus productives exportent (Melitz)", e: [
  { t: "Exporter coûte cher : prospection, normes, logistique, réseau commercial (coûts fixes)", k: "cause" },
  { t: "Seules les firmes les plus productives peuvent payer ces coûts et rester rentables", a: "donc" },
  { t: "Avec l’ouverture, elles grandissent ; les moins productives reculent ou disparaissent", a: "donc" },
  { t: "La productivité moyenne du pays augmente", k: "effet", a: "donc" }
] };
CHAINES["e2-cvm"] = { t: "L’internationalisation de la chaîne de valeur", e: [
  { t: "Une firme multinationale découpe sa production en étapes : conception, composants, assemblage, vente", k: "cause" },
  { t: "Elle place chaque étape là où elle est la plus rentable : coûts, compétences, accès aux marchés, ressources", a: "donc" },
  { f: [{ t: "Par des filiales qu’elle contrôle (investissements directs à l’étranger)" }, { t: "Par des sous-traitants indépendants" }], a: "soit" },
  { t: "Les biens intermédiaires franchissent plusieurs frontières avant le produit final", a: "donc" },
  { t: "Les exportations d’un pays contiennent de la valeur ajoutée venue d’autres pays", k: "effet", a: "donc" }
] };
CHAINES["e2-ineg"] = { t: "Commerce et inégalités dans un pays riche", e: [
  { t: "Un pays riche importe davantage de biens intensifs en travail peu qualifié", k: "cause" },
  { t: "Le prix de ces biens baisse sur le marché intérieur", a: "donc" },
  { t: "Les secteurs nationaux concurrencés réduisent production et emploi ; certaines activités sont délocalisées", a: "donc" },
  { t: "La demande de travail peu qualifié baisse, celle de travail qualifié augmente (secteurs exportateurs)", a: "donc" },
  { t: "Les écarts de salaires et d’emploi entre qualifiés et peu qualifiés se creusent", k: "effet", a: "donc" }
] };
CHAINES["e2-protect"] = { t: "Les effets d’un droit de douane", e: [
  { t: "Un pays relève ses droits de douane", k: "cause" },
  { t: "Le prix des biens importés augmente", a: "donc" },
  { f: [{ t: "Les producteurs nationaux protégés vendent plus : emploi préservé dans ces secteurs", k: "effet" }, { t: "Consommateurs et entreprises qui achètent ces biens paient plus cher", k: "frein" }], a: "donc" },
  { t: "Les partenaires ripostent en taxant à leur tour ses exportations", k: "frein", a: "mais" },
  { t: "Risque de guerre commerciale : les échanges, l’emploi exportateur et la croissance reculent", k: "frein", a: "donc" }
] };

CH.e2 = {
  chapo: "Pourquoi la France achète-t-elle des voitures allemandes tout en en vendant à l’Allemagne ? Pourquoi un smartphone « made in China » est-il surtout fabriqué ailleurs ? Ce chapitre explique sur quoi repose le commerce mondial, qui y gagne, qui y perd, et ce que valent les droits de douane.",
  essentiel: [
    "Les pays se spécialisent selon leurs <b>avantages comparatifs</b> : technologiques (Ricardo, 1817) ou issus de leurs <b>dotations factorielles</b> (modèle HOS). L’échange profite à tous les partenaires, même au moins productif.",
    "Une grande part du commerce se fait <b>entre pays comparables</b> et dans une même branche : différenciation des produits (variété, qualité), économies d’échelle (Krugman) et fragmentation de la chaîne de valeur.",
    "La <b>productivité des firmes</b> sous-tend la compétitivité d’un pays, c’est-à-dire son aptitude à exporter : compétitivité-prix et hors-prix ; seules les firmes les plus productives exportent (Melitz).",
    "La <b>chaîne de valeur s’internationalise</b> : les firmes multinationales répartissent les étapes de production entre pays ; environ 70 % du commerce international passe par des chaînes de valeur mondiales (OCDE).",
    "Le commerce fait <b>baisser les prix</b> et réduit les inégalités <b>entre pays</b>, mais peut accroître les inégalités <b>dans chaque pays</b>. D’où le débat entre libre-échange et protectionnisme."
  ],
  chiffres: [
    { n: "24 430", l: "milliards de dollars d’exportations mondiales de marchandises en 2024, et 8 690 milliards de services commerciaux.", s: "OMC, avril 2025" },
    { n: "3,6 %", l: "seulement du coût de fabrication d’un iPhone 3G revenait à l’assemblage en Chine (6,50 $ sur 178,96 $), alors que l’appareil était compté comme une exportation chinoise.", s: "Xing et Detert, ADBI, 2010" },
    { n: "−69,2", l: "milliards d’euros : le solde des échanges de biens de la France en 2025, en amélioration de 10 milliards sur un an.", s: "Douane, février 2026" }
  ],
  objectifs: [
    { bo: "Comprendre le rôle des dotations factorielles et technologiques (avantages comparatifs) dans les échanges commerciaux et la spécialisation internationale.", clair: "Expliquer pourquoi chaque pays se spécialise et pourquoi l’échange profite à tous (Ricardo, HOS).", voir: "e2-2" },
    { bo: "Comprendre le commerce entre pays comparables (différenciation des produits, qualité des produits, et fragmentation de la chaîne de valeur).", clair: "Expliquer pourquoi des pays semblables échangent des produits semblables.", voir: "e2-3" },
    { bo: "Comprendre que la productivité des firmes sous-tend la compétitivité d’un pays, c’est-à-dire son aptitude à exporter.", clair: "Relier productivité des entreprises, compétitivité-prix et hors-prix, et exportations.", voir: "e2-4" },
    { bo: "Comprendre l’internationalisation de la chaîne de valeur et savoir l’illustrer.", clair: "Décrire comment la production d’un bien se répartit entre plusieurs pays, avec un exemple précis.", voir: "e2-5" },
    { bo: "Comprendre les effets induits par le commerce international : gains moyens en termes de baisse de prix, réduction des inégalités entre pays, accroissement des inégalités de revenus au sein de chaque pays ; comprendre les termes du débat entre libre-échange et protectionnisme.", clair: "Présenter les gagnants et les perdants du commerce, puis les arguments du libre-échange et du protectionnisme.", voir: "e2-6" }
  ],
  notions: ["commerce international", "exportations / importations", "solde commercial", "spécialisation internationale", "avantage absolu", "avantage comparatif", "coût d’opportunité", "dotations factorielles", "dotations technologiques", "commerce intra-branche / inter-branche", "différenciation horizontale / verticale", "économies d’échelle", "compétitivité-prix / hors-prix", "productivité des firmes", "chaîne de valeur", "firme multinationale", "investissement direct à l’étranger", "sous-traitance", "délocalisation", "libre-échange", "protectionnisme", "droits de douane", "barrières non tarifaires"],
  sections: [
    { id: "e2-1", t: "Le commerce mondial en chiffres", h:
      '<p class="lede">Le commerce international est l’échange de biens et de services entre pays. Une <b>exportation</b> est une vente à un non-résident ; une <b>importation</b>, un achat à un non-résident.</p>' +
      '<div data-graph="e2-monde"></div>' +
      '<p>En 2024, selon l’OMC, les exportations mondiales de marchandises atteignent 24 430 milliards de dollars (+2 %) et celles de services commerciaux 8 690 milliards (+9 %). La Chine est le premier exportateur de marchandises (3 580 milliards de dollars, soit environ 15 % du total) ; les États-Unis sont le premier importateur.</p>' +
      '<div class="def"><b>Solde commercial</b> — exportations moins importations de biens. Négatif : déficit ; positif : excédent. Le <b>taux de couverture</b> = exportations ÷ importations × 100.</div>' +
      '<div data-graph="e2-france"></div>' +
      '<p>La France affiche un déficit des échanges de biens : −69,2 milliards d’euros en 2025, contre environ −79 milliards en 2024, d’après la Douane. L’amélioration vient surtout des matériels de transport (aéronautique, automobile), des produits pharmaceutiques (solde record) et d’une facture énergétique plus faible. Un déficit n’est pas en soi une « perte » : il traduit aussi le fait que le pays consomme et investit plus qu’il ne produit, et achète des biens intermédiaires utiles à ses entreprises.</p>' +
      '<div class="plus"><p>Exportations et importations ne se mesurent pas tout à fait de la même façon : FAB (« franco à bord », valeur à la frontière du pays exportateur) ou CAF (« coût, assurance, fret », valeur à l’arrivée). Pour calculer un solde rigoureux, il faut les deux sur la même base, d’où le solde « FAB/FAB » publié par la Douane.</p></div>' },

    { id: "e2-2", t: "Les avantages comparatifs : technologies et dotations", h:
      '<div class="aut"><span class="mono">AS</span><span class="an">Adam Smith<small>1723-1790</small></span><span class="ad"><i>La Richesse des nations</i> (1776) : chaque pays doit se spécialiser dans les biens pour lesquels il a un <b>avantage absolu</b>, c’est-à-dire qu’il produit avec moins de travail que les autres. Limite : un pays qui n’a aucun avantage absolu serait exclu de l’échange.</span></div>' +
      '<div class="aut"><span class="mono">DR</span><span class="an">David Ricardo<small>1772-1823</small></span><span class="ad"><i>Des principes de l’économie politique et de l’impôt</i> (1817) : même un pays moins productif dans tous les biens gagne à l’échange s’il se spécialise là où son désavantage est le plus faible. C’est l’<b>avantage comparatif</b>, qui repose ici sur des différences de <b>technologie</b> (de productivité du travail).</span></div>' +
      '<p>L’exemple de Ricardo : nombre d’heures de travail nécessaires pour produire une unité de drap et une unité de vin.</p>' +
      '<div class="tbl"><table><thead><tr><th></th><th class="n">Drap</th><th class="n">Vin</th><th>Coût d’opportunité du drap</th></tr></thead><tbody>' +
      '<tr><td>Angleterre</td><td class="n">100 h</td><td class="n">120 h</td><td>100 ÷ 120 ≈ 0,83 unité de vin</td></tr>' +
      '<tr><td>Portugal</td><td class="n">90 h</td><td class="n">80 h</td><td>90 ÷ 80 = 1,125 unité de vin</td></tr></tbody></table></div>' +
      '<p>Le Portugal est plus productif dans les deux biens (avantage absolu partout). Mais produire du drap coûte relativement moins cher en Angleterre (0,83 unité de vin « sacrifiée », contre 1,125 au Portugal) : l’Angleterre a un avantage comparatif en drap, le Portugal en vin.</p>' +
      '<details class="pli"><summary>Le calcul du gain à l’échange</summary><div><p>Sans échange, chaque pays produit une unité de chaque bien : 2 draps et 2 unités de vin, avec 220 heures en Angleterre et 170 au Portugal. Si l’Angleterre consacre ses 220 heures au drap, elle en produit 2,2 ; si le Portugal consacre ses 170 heures au vin, il en produit 2,125. Avec les mêmes heures, le monde dispose de 0,2 drap et de 0,125 unité de vin en plus : c’est le gain de la spécialisation, à partager par l’échange.</p></div></details>' +
      '<div data-anim="e2-ricardo"></div>' +
      '<div data-chain="e2-ricardo"></div>' +
      '<div class="def"><b>Dotations factorielles</b> — quantités de facteurs de production (travail plus ou moins qualifié, capital, terres, ressources naturelles) dont dispose un pays.</div>' +
      '<div class="aut"><span class="mono">HOS</span><span class="an">Heckscher, Ohlin et Samuelson<small>1919, 1933, années 1940</small></span><span class="ad">Le modèle <b>HOS</b> explique les avantages comparatifs par les dotations : un pays se spécialise dans les biens qui utilisent intensément le facteur dont il est <b>relativement abondant</b>, donc relativement bon marché.</span></div>' +
      '<div data-chain="e2-hos"></div>' +
      '<div class="ex"><p>Le Bangladesh, où le travail peu qualifié est abondant, est devenu l’un des premiers exportateurs mondiaux de vêtements. L’Australie, abondante en terres et en minerais, exporte surtout des matières premières (minerai de fer, charbon) et des produits agricoles.</p></div>' +
      '<div class="aut"><span class="mono">WL</span><span class="an">Wassily Leontief<small>1905-1999 · Nobel 1973</small></span><span class="ad">En 1953, il constate que les exportations américaines sont plus intensives en travail que leurs importations, alors que les États-Unis sont riches en capital : c’est le <b>paradoxe de Leontief</b>. On l’explique en distinguant le travail <b>qualifié</b>, abondant aux États-Unis : les dotations comprennent aussi le capital humain et la technologie.</span></div>' +
      '<p>Les avantages comparatifs ne sont pas figés : ils se <b>construisent</b> par l’investissement, l’éducation et les politiques industrielles. La Corée du Sud exportait surtout des produits textiles dans les années 1960 ; elle est aujourd’hui un grand exportateur de semi-conducteurs, d’automobiles et de navires.</p>' },

    { id: "e2-3", t: "Le commerce entre pays comparables", h:
      '<p class="lede">Ricardo et HOS expliquent bien les échanges entre pays <b>différents</b> (des vêtements contre des avions). Mais une grande partie du commerce mondial se fait entre pays riches et semblables, qui échangent des produits semblables.</p>' +
      '<div class="def"><b>Commerce intra-branche</b> — échange de produits d’une même branche entre deux pays (la France exporte des voitures en Allemagne et en importe). Le commerce <b>inter-branche</b> échange des produits de branches différentes.</div>' +
      '<p>Trois raisons, citées par le programme, l’expliquent :</p>' +
      '<ul><li><b>La différenciation des produits</b> : les consommateurs aiment la variété. Différenciation <b>horizontale</b> : des produits de même qualité mais de caractéristiques différentes (marques, styles, modèles). </li><li><b>La qualité des produits</b> : différenciation <b>verticale</b>, des gammes de qualité et de prix différents. Un même pays importe des produits d’entrée de gamme et exporte du haut de gamme.</li><li><b>La fragmentation de la chaîne de valeur</b> : les pays échangent des pièces et des composants d’un même produit (voir plus bas).</li></ul>' +
      '<div class="aut"><span class="mono">PK</span><span class="an">Paul Krugman<small>né en 1953 · Nobel 2008</small></span><span class="ad">La <b>nouvelle théorie du commerce international</b> (1979-1980) explique le commerce intra-branche par les <b>économies d’échelle</b> (rendements croissants) et le <b>goût pour la variété</b>. Chaque pays se spécialise dans certaines variétés produites en grande série.</span></div>' +
      '<div data-chain="e2-krugman"></div>' +
      '<div class="ex"><p>L’automobile entre la France et l’Allemagne : Renault et Stellantis vendent des voitures en Allemagne, Volkswagen, BMW et Mercedes en vendent en France. Les modèles diffèrent par le style et l’image (horizontale) et par la gamme (verticale : beaucoup de modèles allemands sont positionnés sur le haut de gamme).</p></div>' +
      '<p>Le marché unique européen, en supprimant les obstacles aux échanges entre pays proches, a fortement développé ce commerce intra-branche (question <a href="#e5">É5</a>).</p>' },

    { id: "e2-4", t: "Productivité des firmes et compétitivité du pays", h:
      '<div class="def"><b>Compétitivité</b> — aptitude d’une entreprise ou d’un pays à vendre ses produits face à la concurrence ; pour un pays, son <b>aptitude à exporter</b> (gagner ou garder des parts de marché).</div>' +
      '<ul><li><b>Compétitivité-prix</b> : vendre moins cher que les concurrents, à qualité égale. Elle dépend du coût unitaire de production (salaires, productivité), des marges et du taux de change.</li><li><b>Compétitivité hors-prix</b> : vendre grâce à autre chose que le prix : qualité, innovation, image de marque, design, service après-vente, délais.</li></ul>' +
      '<div data-chain="e2-compet"></div>' +
      '<p>Le coût salarial ne suffit pas à juger la compétitivité : un salaire plus élevé n’augmente pas le coût unitaire si la productivité augmente autant. C’est le <b>coût salarial unitaire</b> (coût du travail par unité produite) qui compte.</p>' +
      '<div class="aut"><span class="mono">MM</span><span class="an">Marc Melitz<small>né en 1968</small></span><span class="ad">Modèle des <b>firmes hétérogènes</b> (2003) : au sein d’un même pays et d’une même branche, les firmes ont des productivités très différentes. Seules les plus productives exportent.</span></div>' +
      '<div data-chain="e2-melitz"></div>' +
      '<div class="ex"><p>L’aéronautique illustre la compétitivité hors-prix française : un avion se vend sur sa fiabilité, sa consommation de carburant et le service, plus que sur son prix. En 2025, selon la Douane, l’amélioration du solde commercial de la France est portée par les matériels de transport, en particulier l’aéronautique, et par les produits pharmaceutiques.</p></div>' +
      '<div class="ex"><p>Ce mécanisme était le sujet de la partie 3 de l’épreuve composée du bac 2026 (jour 1) : « montrez que la productivité des firmes sous-tend la compétitivité d’un pays, c’est-à-dire son aptitude à exporter ». Voir l’onglet <a href="#e2/bac">Sujets bac</a>.</p></div>' },

    { id: "e2-5", t: "L’internationalisation de la chaîne de valeur", h:
      '<div class="def"><b>Chaîne de valeur</b> — ensemble des étapes qui ajoutent de la valeur à un produit : conception, recherche, fabrication des composants, assemblage, logistique, marketing, vente, services.</div>' +
      '<div class="def"><b>Firme multinationale (FMN)</b> — entreprise qui possède au moins une filiale de production à l’étranger, créée ou rachetée par un <b>investissement direct à l’étranger</b> (IDE), c’est-à-dire une prise de contrôle durable (au moins 10 % du capital par convention).</div>' +
      '<div data-chain="e2-cvm"></div>' +
      '<p>On parle de <b>décomposition internationale des processus productifs</b>. Les firmes y recourent pour réduire leurs coûts (main-d’œuvre, impôts), accéder à des compétences, se rapprocher de leurs marchés ou contourner des barrières douanières. Selon l’OCDE, environ <b>70 % du commerce international</b> fait intervenir des chaînes de valeur mondiales : services, matières premières, pièces et composants franchissent plusieurs frontières.</p>' +
      '<div data-anim="e2-iphone"></div>' +
      '<div data-graph="e2-iphone"></div>' +
      '<div class="ex"><p>En 2009, un iPhone 3G coûte environ 178,96 dollars à fabriquer. L’assemblage en Chine ne représente que 6,50 dollars, soit 3,6 % ; les composants viennent surtout de fournisseurs japonais, allemands, sud-coréens et américains ; la conception et la marque sont américaines. Pourtant, toute la valeur de l’appareil expédié vers les États-Unis est comptée comme une importation en provenance de Chine (Xing et Detert, 2010).</p></div>' +
      '<div class="ex"><p>L’Airbus A320 : des éléments produits en France, en Allemagne, en Espagne et au Royaume-Uni (où sont fabriquées les ailes) ; des lignes d’assemblage final à Toulouse, à Hambourg, à Tianjin en Chine et à Mobile aux États-Unis.</p></div>' +
      '<p>Pour mesurer correctement qui produit quoi, on raisonne donc en <b>commerce en valeur ajoutée</b> plutôt qu’en valeur brute. Les pénuries de 2020-2021 (masques, puis semi-conducteurs) ont montré la fragilité de chaînes très longues : certaines entreprises et certains États cherchent désormais à <b>relocaliser</b> ou à diversifier leurs fournisseurs.</p>' },

    { id: "e2-6", t: "Gagnants et perdants du commerce international", h:
      '<h3>1. Des gains moyens : la baisse des prix</h3>' +
      '<p>L’ouverture fait baisser les prix pour les consommateurs : la spécialisation selon les avantages comparatifs, les économies d’échelle et la concurrence étrangère abaissent les coûts et les marges. Elle élargit aussi la <b>variété</b> des produits disponibles. Ces gains sont dits « moyens » car ils profitent à l’ensemble des consommateurs, même s’ils sont inégalement répartis.</p>' +
      '<h3>2. Une réduction des inégalités entre pays</h3>' +
      '<p>Les pays émergents qui se sont ouverts et intégrés aux chaînes de valeur ont rattrapé une partie de leur retard : la Chine, membre de l’OMC depuis décembre 2001, est devenue le premier exportateur mondial de marchandises. Leur croissance a fait sortir des centaines de millions de personnes de la pauvreté et réduit l’écart de revenu moyen avec les pays riches.</p>' +
      '<div class="aut"><span class="mono">BM</span><span class="an">Branko Milanovic<small>né en 1953</small></span><span class="ad">Avec Christoph Lakner, il montre qu’entre 1988 et 2008 les revenus ont fortement progressé pour les classes moyennes des pays émergents et pour les plus riches du monde, mais peu pour les classes populaires et moyennes des pays riches : la « <b>courbe de l’éléphant</b> ».</span></div>' +
      '<h3>3. Une hausse des inégalités au sein de chaque pays</h3>' +
      '<p>Le théorème de <b>Stolper-Samuelson</b>, issu de HOS, prévoit que l’ouverture profite au facteur abondant et nuit au facteur rare. Dans un pays riche, le facteur rare est le travail peu qualifié.</p>' +
      '<div data-chain="e2-ineg"></div>' +
      '<div class="aut"><span class="mono">ADH</span><span class="an">Autor, Dorn et Hanson<small>« The China Syndrome », 2013</small></span><span class="ad">Les zones des États-Unis les plus exposées à la concurrence des importations chinoises ont perdu durablement des emplois industriels, avec des salaires plus bas et davantage de prestations sociales : c’est le « <b>choc chinois</b> ».</span></div>' +
      '<p>Ces effets se cumulent avec ceux du progrès technique biaisé (<a href="#e1:e1-5">É1</a>) : il est difficile de séparer ce qui vient du commerce et ce qui vient de l’automatisation.</p>' },

    { id: "e2-7", t: "Libre-échange ou protectionnisme ?", h:
      '<div class="def"><b>Libre-échange</b> — politique qui supprime les obstacles aux échanges internationaux. <b>Protectionnisme</b> — politique qui protège la production nationale de la concurrence étrangère.</div>' +
      '<p>Instruments du protectionnisme : <b>droits de douane</b> (taxes sur les importations), <b>quotas</b> (quantités maximales importées), <b>barrières non tarifaires</b> (normes techniques ou sanitaires, procédures), <b>subventions</b> aux producteurs nationaux.</p>' +
      '<div class="tbl"><table><thead><tr><th>Arguments du libre-échange</th><th>Arguments du protectionnisme</th></tr></thead><tbody>' +
      '<tr><td>Gains de la spécialisation (Ricardo, HOS), baisse des prix, variété.</td><td>Protéger les <b>industries naissantes</b> le temps qu’elles deviennent compétitives (List, 1841 : protectionnisme <b>éducateur</b>).</td></tr>' +
      '<tr><td>Concurrence : incite les firmes à innover ; seules les plus productives prospèrent (Melitz).</td><td>Protéger l’emploi et les territoires frappés par la concurrence (choc chinois) ; limiter les inégalités internes.</td></tr>' +
      '<tr><td>Diffusion des technologies et rattrapage des pays pauvres.</td><td>Indépendance stratégique : santé, énergie, défense, semi-conducteurs.</td></tr>' +
      '<tr><td>Le protectionnisme entraîne des représailles et coûte aux consommateurs.</td><td>Répondre à une concurrence jugée déloyale (subventions, dumping social ou environnemental).</td></tr>' +
      '</tbody></table></div>' +
      '<div data-chain="e2-protect"></div>' +
      '<div class="ex"><p>Années 1930 : le tarif Smoot-Hawley adopté par les États-Unis en juin 1930 et les représailles qui ont suivi ont accompagné l’effondrement du commerce mondial pendant la Grande Dépression. Après 1945, le GATT (1947) puis l’OMC (créée le 1er janvier 1995) organisent la baisse négociée des droits de douane.</p><p>2025 : le 2 avril, les États-Unis annoncent des « droits de douane réciproques », avec un taux minimum de 10 % sur la plupart des importations et des taux plus élevés pour de nombreux partenaires. Le protectionnisme est redevenu un instrument politique majeur.</p></div>' +
      '<div class="plus"><p>Entre les deux, il existe des positions intermédiaires : protectionnisme ciblé et temporaire, accords régionaux (Union européenne), clauses sociales et environnementales dans les traités, mécanisme d’ajustement carbone aux frontières de l’Union européenne.</p></div>' }
  ],
  pieges: [
    { f: "« Un pays moins productif dans tous les biens ne peut pas gagner à l’échange. »", v: "Faux : c’est tout l’apport de Ricardo. Il gagne en se spécialisant là où son désavantage est le plus faible (avantage comparatif)." },
    { f: "Confondre avantage absolu et avantage comparatif.", v: "Absolu : produire avec moins de travail que l’autre pays. Comparatif : produire avec un coût d’opportunité plus faible." },
    { f: "« Ricardo explique la spécialisation par les dotations en facteurs. »", v: "Ricardo : différences de technologie (productivité du travail). HOS : différences de dotations factorielles." },
    { f: "« La compétitivité, c’est uniquement vendre moins cher. »", v: "Il y a aussi la compétitivité hors-prix : qualité, innovation, image, services. Et c’est le coût <b>unitaire</b> qui compte, pas le salaire seul." },
    { f: "« Un iPhone importé de Chine, c’est de la valeur ajoutée chinoise. »", v: "Le commerce en valeur brute compte toute la valeur au dernier pays exportateur ; en valeur ajoutée, la Chine n’apporte qu’une petite part (3,6 % pour l’iPhone 3G)." },
    { f: "« Le commerce international augmente les inégalités. »", v: "Il faut préciser : il tend à <b>réduire</b> les inégalités <b>entre</b> pays et peut <b>accroître</b> celles <b>au sein</b> de chaque pays." },
    { f: "« Le protectionnisme protège l’emploi. »", v: "Il protège les emplois des secteurs protégés, mais renchérit les biens importés, pénalise les entreprises utilisatrices et peut entraîner des représailles qui détruisent des emplois exportateurs." }
  ],
  retenir:
    '<h3>Définitions</h3><ul>' +
    '<li><b>Avantage comparatif</b> (Ricardo, 1817) : se spécialiser là où le coût d’opportunité est le plus faible ; l’échange profite aux deux pays.</li>' +
    '<li><b>Dotations factorielles</b> (HOS) : un pays exporte les biens intensifs dans son facteur relativement abondant. Paradoxe de Leontief (1953).</li>' +
    '<li><b>Commerce intra-branche</b> : échange de produits similaires entre pays comparables ; différenciation horizontale (variété) et verticale (qualité) ; économies d’échelle (Krugman, Nobel 2008).</li>' +
    '<li><b>Compétitivité</b> : aptitude à exporter ; prix (coût unitaire, change, marges) et hors-prix (qualité, innovation). Seules les firmes les plus productives exportent (Melitz).</li>' +
    '<li><b>Chaîne de valeur internationalisée</b> : FMN, IDE (≥ 10 % du capital), sous-traitance ; environ 70 % du commerce passe par des chaînes de valeur mondiales (OCDE). iPhone 3G : 6,50 $ d’assemblage chinois sur 178,96 $.</li>' +
    '<li><b>Effets</b> : baisse des prix et variété ; inégalités entre pays en baisse (courbe de l’éléphant, Milanovic) ; inégalités internes en hausse (Stolper-Samuelson, choc chinois).</li>' +
    '<li><b>Protectionnisme</b> : droits de douane, quotas, normes, subventions ; protectionnisme éducateur (List, 1841).</li></ul>' +
    '<h3>Chiffres à citer</h3><ul><li>Commerce mondial 2024 : 24 430 milliards $ de marchandises, 8 690 milliards $ de services ; Chine 3 580 milliards $ (OMC).</li><li>France 2025 : solde des biens −69,2 milliards € (Douane).</li></ul>',
  chainesFiche: ["e2-ricardo", "e2-hos", "e2-krugman", "e2-compet", "e2-melitz", "e2-cvm", "e2-ineg", "e2-protect"],
  quiz: [
    { q: "Dans l’exemple de Ricardo, le Portugal produit drap et vin avec moins de travail que l’Angleterre. Il a donc…", c: ["un avantage absolu dans les deux biens, mais un avantage comparatif seulement dans le vin", "un avantage comparatif dans les deux biens", "intérêt à ne pas échanger", "un avantage comparatif dans le drap"], r: 0, e: "Le coût d’opportunité du vin est plus faible au Portugal (80/90 ≈ 0,89 drap contre 1,2 en Angleterre) : il se spécialise dans le vin.", s: "e2-2" },
    { q: "L’avantage comparatif repose sur…", c: ["le coût d’opportunité relatif d’un bien", "le niveau absolu des salaires", "la taille du pays", "la valeur de la monnaie"], r: 0, e: "On compare ce que coûte un bien en termes de l’autre bien sacrifié, d’un pays à l’autre.", s: "e2-2" },
    { q: "Selon le modèle HOS, un pays abondant en travail peu qualifié exporte…", c: ["des biens intensifs en travail peu qualifié", "des biens intensifs en capital", "des services financiers", "uniquement des matières premières"], r: 0, e: "Le facteur abondant est relativement bon marché : les biens qui l’utilisent beaucoup y sont moins chers.", s: "e2-2" },
    { q: "Le paradoxe de Leontief (1953) porte sur…", c: ["les exportations américaines, plus intensives en travail qu’attendu", "le déficit commercial chinois", "la hausse des droits de douane en 1930", "le commerce intra-branche européen"], r: 0, e: "Les États-Unis, riches en capital, exportaient des biens plutôt intensifs en travail, en fait du travail qualifié.", s: "e2-2" },
    { q: "Le commerce intra-branche désigne…", c: ["l’échange de produits d’une même branche entre deux pays", "l’échange entre filiales d’une même firme seulement", "l’échange de matières premières contre des biens industriels", "le commerce à l’intérieur d’un pays"], r: 0, e: "Exemple : la France exporte et importe des voitures avec l’Allemagne.", s: "e2-3" },
    { q: "Krugman explique le commerce entre pays comparables par…", c: ["les économies d’échelle et le goût pour la variété", "les différences de dotations factorielles", "les différences de climat", "le protectionnisme"], r: 0, e: "Nouvelle théorie du commerce international (1979-1980), Nobel 2008.", s: "e2-3" },
    { q: "La différenciation verticale des produits porte sur…", c: ["la qualité et la gamme", "la couleur et le style", "le pays d’origine", "le mode de transport"], r: 0, e: "Verticale = niveaux de qualité différents ; horizontale = variétés de même qualité.", s: "e2-3" },
    { q: "La compétitivité hors-prix repose notamment sur…", c: ["la qualité, l’innovation et l’image de marque", "le taux de change", "le niveau des salaires", "les subventions à l’exportation"], r: 0, e: "La compétitivité-prix dépend des coûts, des marges et du change ; la hors-prix de tout le reste.", s: "e2-4" },
    { q: "Selon Melitz, pourquoi seules certaines firmes exportent-elles ?", c: ["Exporter a un coût fixe que seules les plus productives peuvent couvrir", "Les petites firmes n’ont pas le droit d’exporter", "Les firmes exportatrices sont subventionnées", "Les droits de douane interdisent l’export"], r: 0, e: "D’où le lien entre productivité des firmes et compétitivité du pays.", s: "e2-4" },
    { q: "Un investissement direct à l’étranger correspond à…", c: ["une prise de contrôle durable d’une entreprise à l’étranger (au moins 10 % du capital)", "un achat d’actions étrangères pour quelques jours", "un prêt à un État étranger", "une exportation de biens d’équipement"], r: 0, e: "L’IDE crée ou rachète une filiale : c’est l’outil de la firme multinationale.", s: "e2-5" },
    { q: "Pour un iPhone 3G de 2009, l’assemblage en Chine représentait environ…", c: ["3,6 % du coût de fabrication", "50 % du coût de fabrication", "90 % du coût de fabrication", "25 % du coût de fabrication"], r: 0, e: "6,50 $ sur 178,96 $ (Xing et Detert, 2010) : la valeur ajoutée chinoise était très faible.", s: "e2-5" },
    { q: "Selon le théorème de Stolper-Samuelson, dans un pays riche, l’ouverture…", c: ["nuit au facteur rare, le travail peu qualifié", "profite à tous les travailleurs de la même façon", "nuit au capital", "n’a pas d’effet sur les salaires"], r: 0, e: "Le facteur abondant gagne, le facteur rare perd : d’où une hausse des inégalités internes.", s: "e2-6" },
    { q: "La « courbe de l’éléphant » de Milanovic montre que, de 1988 à 2008…", c: ["les classes moyennes des pays émergents et les plus riches du monde ont le plus gagné", "tous les revenus ont progressé au même rythme", "les plus pauvres du monde ont perdu", "seuls les pays riches ont gagné"], r: 0, e: "Les classes populaires et moyennes des pays riches ont, elles, peu progressé.", s: "e2-6" },
    { q: "Le protectionnisme éducateur de List (1841) consiste à…", c: ["protéger temporairement les industries naissantes", "fermer définitivement les frontières", "subventionner les importations", "supprimer tous les droits de douane"], r: 0, e: "Une protection provisoire, le temps que l’industrie devienne compétitive.", s: "e2-7" }
  ],
  cartes: [
    { r: "Avantage absolu", v: "Produire un bien avec moins de travail que les autres pays (Smith, 1776)." },
    { r: "Avantage comparatif", v: "Produire un bien avec un coût d’opportunité plus faible que les autres pays (Ricardo, 1817). L’échange profite à tous." },
    { r: "Coût d’opportunité", v: "Ce à quoi on renonce pour produire un bien : la quantité de l’autre bien qu’on aurait pu produire." },
    { r: "Dotations factorielles", v: "Quantités de facteurs (travail plus ou moins qualifié, capital, terres, ressources) dont dispose un pays (modèle HOS)." },
    { r: "Paradoxe de Leontief", v: "1953 : les exportations des États-Unis, riches en capital, sont plus intensives en travail (qualifié) que leurs importations." },
    { r: "Commerce intra-branche", v: "Échange de produits d’une même branche entre pays (voitures France ↔ Allemagne)." },
    { r: "Différenciation horizontale / verticale", v: "Horizontale : variétés de même qualité (marques, styles). Verticale : niveaux de qualité différents (gammes)." },
    { r: "Économies d’échelle", v: "Baisse du coût unitaire quand la quantité produite augmente (rendements croissants) ; base du commerce entre pays comparables (Krugman)." },
    { r: "Compétitivité", v: "Aptitude à vendre face à la concurrence ; pour un pays, aptitude à exporter." },
    { r: "Compétitivité-prix / hors-prix", v: "Prix : coût unitaire, marges, change. Hors-prix : qualité, innovation, marque, services." },
    { r: "Firme multinationale", v: "Entreprise qui contrôle au moins une filiale de production à l’étranger." },
    { r: "Investissement direct à l’étranger", v: "Prise de contrôle durable d’une entreprise à l’étranger (au moins 10 % du capital) : création ou rachat de filiale." },
    { r: "Chaîne de valeur mondiale", v: "Répartition des étapes de production d’un bien entre plusieurs pays ; environ 70 % du commerce international (OCDE)." },
    { r: "Stolper-Samuelson", v: "L’ouverture profite au facteur abondant et nuit au facteur rare (dans un pays riche : le travail peu qualifié)." },
    { r: "Choc chinois", v: "Pertes durables d’emplois industriels dans les zones américaines exposées aux importations chinoises (Autor, Dorn, Hanson, 2013)." },
    { r: "Protectionnisme", v: "Politique qui protège la production nationale : droits de douane, quotas, normes, subventions." },
    { r: "Protectionnisme éducateur", v: "Protection temporaire des industries naissantes (Friedrich List, 1841)." },
    { r: "OMC", v: "Organisation mondiale du commerce, créée le 1er janvier 1995 pour succéder au GATT (1947) ; organise la baisse négociée des obstacles aux échanges." }
  ],
  bac: [
    { type: "Savoir-faire", origine: "Exercice du site (exemple de Ricardo)", t: "Calculer des avantages comparatifs", enonce:
      '<p>Pour produire une unité de drap, il faut 100 heures en Angleterre et 90 au Portugal ; pour une unité de vin, 120 heures en Angleterre et 80 au Portugal.</p><ol><li>Quel pays a un avantage absolu dans chaque bien ?</li><li>Calcule le coût d’opportunité du vin dans chaque pays et déduis-en les avantages comparatifs.</li><li>Montre que la spécialisation augmente la production totale.</li></ol>',
      corrige: '<ol><li>Le Portugal a un avantage absolu dans les deux biens (90 h < 100 h ; 80 h < 120 h).</li><li>Coût d’opportunité du vin = heures pour le vin ÷ heures pour le drap. Angleterre : 120 ÷ 100 = 1,2 unité de drap ; Portugal : 80 ÷ 90 ≈ 0,89. Le vin coûte relativement moins cher au Portugal : avantage comparatif du Portugal en vin, de l’Angleterre en drap.</li><li>Sans échange (une unité de chaque) : 2 draps et 2 vins. Spécialisés : l’Angleterre produit 220 ÷ 100 = 2,2 draps ; le Portugal 170 ÷ 80 = 2,125 vins. La production totale augmente de 0,2 drap et 0,125 vin avec le même travail.</li></ol>' },
    { type: "Partie 1 · Mobilisation des connaissances", origine: "Sujet inventé pour le site", t: "Présentez deux effets du commerce international sur les inégalités.", enonce: "<p>3,5 points, sans document.</p>",
      methode: "<p>« Deux effets » : deux paragraphes nettement séparés. Ici, le plus clair est de distinguer inégalités <b>entre</b> pays (baisse) et <b>au sein</b> des pays (hausse).</p>",
      corrige: '<div class="copie"><p>Le commerce international, échange de biens et de services entre pays, a des effets opposés sur les inégalités selon l’échelle retenue.</p><p>D’une part, il réduit les inégalités entre pays. En s’ouvrant et en s’intégrant aux chaînes de valeur mondiales, des pays émergents ont exploité leurs avantages comparatifs, attiré des investissements étrangers et accéléré leur croissance, ce qui leur a permis de rattraper une partie de leur retard. La Chine, entrée à l’OMC en 2001, est devenue le premier exportateur mondial de marchandises (3 580 milliards de dollars en 2024 selon l’OMC). Milanovic montre que de 1988 à 2008 les classes moyennes des pays émergents ont parmi les plus forts gains de revenu au monde.</p><p>D’autre part, il peut accroître les inégalités au sein des pays riches. Selon le théorème de Stolper-Samuelson, l’ouverture nuit au facteur relativement rare, ici le travail peu qualifié : les importations de biens intensifs en travail peu qualifié et les délocalisations réduisent la demande de ce travail, donc son emploi et son salaire relatif, tandis que les qualifiés des secteurs exportateurs gagnent. Autor, Dorn et Hanson ont ainsi montré que les zones américaines les plus exposées aux importations chinoises ont perdu durablement des emplois industriels.</p></div>' },
    { type: "Partie 2 · Étude d’un document", origine: "Exercice du site, données Xing et Detert (2010)", t: "La chaîne de valeur de l’iPhone", enonce:
      '<p>Document : le graphique « Qui produit la valeur d’un iPhone 3G ? » dans <a href="#e2:e2-5">le cours</a> (coût total 178,96 $ ; composants achetés aux fournisseurs 172,46 $ ; assemblage en Chine 6,50 $).</p><ol><li>Calculez la part de l’assemblage chinois dans le coût de fabrication.</li><li>À l’aide du document et de vos connaissances, montrez que la production de l’iPhone illustre l’internationalisation de la chaîne de valeur.</li></ol>',
      corrige: '<ol><li>6,50 ÷ 178,96 × 100 ≈ 3,6 %. Selon Xing et Detert (2010), d’après iSuppli, l’assemblage en Chine représente environ 3,6 % du coût de fabrication d’un iPhone 3G en 2009 ; les composants, 96,4 %.</li><li>L’internationalisation de la chaîne de valeur consiste à répartir les étapes de production entre plusieurs pays. Pour l’iPhone, la conception est américaine (Apple), les composants (172,46 $ sur 178,96 $) viennent de fournisseurs de plusieurs pays (Japon, Allemagne, Corée du Sud, États-Unis), et l’assemblage final, intensif en main-d’œuvre, est réalisé en Chine, où ce travail est abondant et relativement bon marché. Chaque étape est placée là où elle est la plus rentable : on retrouve la logique des avantages comparatifs, appliquée non plus à des produits mais à des tâches. Les composants franchissent plusieurs frontières avant l’assemblage. Enfin, le commerce mesuré en valeur brute attribue tout l’appareil à la Chine, alors que sa valeur ajoutée y est faible : d’où l’intérêt du commerce en valeur ajoutée.</li></ol>' },
    { type: "Partie 3 · Raisonnement sur dossier", origine: "Sujet officiel : bac 2026, jour 1 (France), partie 3 · corrigé du site", officiel: true, t: "Montrez que la productivité des firmes sous-tend la compétitivité d’un pays, c’est-à-dire son aptitude à exporter.", enonce:
      '<p>Les documents du sujet officiel ne sont pas reproduits ici : entraîne-toi avec ceux du cours (solde commercial 2025, aéronautique, iPhone) et tes connaissances.</p>',
      corrige: '<p><b>Introduction.</b> La productivité mesure l’efficacité de la production (production par unité de facteur). La compétitivité d’un pays est son aptitude à exporter, c’est-à-dire à gagner des parts de marché face à la concurrence étrangère. On montrera que des firmes plus productives rendent le pays plus compétitif par les prix, puis hors prix, et que les exportations d’un pays reposent sur ses firmes les plus productives.</p><p><b>I. La productivité améliore la compétitivité-prix.</b> Hausse de productivité → baisse du coût salarial unitaire → les firmes peuvent baisser leurs prix à l’exportation sans réduire leurs marges → parts de marché. Un salaire élevé n’est pas un handicap si la productivité l’est aussi.</p><p><b>II. La productivité finance la compétitivité hors-prix.</b> Des coûts plus bas dégagent des marges → investissement en R&D, qualité, marque, service → produits différenciés, moins sensibles au prix (différenciation verticale). Exemple : aéronautique et pharmacie portent l’amélioration du solde des biens de la France en 2025 (Douane).</p><p><b>III. Les exportations reposent sur les firmes les plus productives.</b> Melitz : exporter a des coûts fixes ; seules les firmes les plus productives exportent ; l’ouverture les fait grandir et élève la productivité moyenne. La compétitivité d’un pays est donc d’abord celle d’une minorité de grandes firmes très productives.</p><p><b>Conclusion.</b> La productivité des firmes est le socle de la compétitivité du pays, par les prix comme hors prix ; elle dépend elle-même de l’innovation et du capital humain (<a href="#e1:e1-3">É1</a>).</p>' },
    { type: "Dissertation · plan détaillé", origine: "Sujet inventé pour le site", t: "Le protectionnisme peut-il être une réponse efficace aux effets du commerce international ?", enonce: "<p>Construis la problématique et le plan, puis compare.</p>",
      corrige: '<p><b>Problématique.</b> Le commerce international procure des gains moyens mais fait des perdants. Taxer les importations permet-il de corriger ces effets sans détruire les gains de l’échange ?</p><p><b>I. Le protectionnisme peut répondre à certains effets du commerce</b><br>A. Protéger les secteurs et territoires exposés (choc chinois ; Stolper-Samuelson).<br>B. Laisser le temps à des industries naissantes ou stratégiques de devenir compétitives (List ; Corée du Sud).<br>C. Réduire la dépendance de chaînes de valeur trop longues (pénuries de 2020-2021).</p><p><b>II. Mais il est souvent inefficace, voire contre-productif</b><br>A. Il renchérit les biens importés : perte de pouvoir d’achat et hausse des coûts des entreprises utilisatrices de composants importés.<br>B. Il provoque des représailles : années 1930 (Smoot-Hawley) ; tensions commerciales de 2025.<br>C. Il protège des firmes peu productives et freine l’innovation (Melitz).</p><p><b>III. D’autres réponses peuvent être plus efficaces</b><br>A. Accompagner les perdants : formation, reconversion, aides territoriales.<br>B. Redistribuer une partie des gains de l’échange (fiscalité, protection sociale).<br>C. Réguler l’échange plutôt que le fermer : normes sociales et environnementales, ajustement carbone aux frontières, protection ciblée et temporaire.</p>' }
  ]
};
