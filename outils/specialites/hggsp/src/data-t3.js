/* ======================= THÈME 3 — HISTOIRE ET MÉMOIRES (renfort thèmes 3 et 4) ======================= */
rediger("t3", { pb: "Comment les sociétés et les États se reconstruisent-ils après des conflits majeurs, entre travail des historiens, revendications mémorielles et action de la justice ?", ecrit: "Pas à l'écrit en 2027 (années impaires) : évaluable à l'écrit en 2028. Excellent terrain pour le Grand oral, et utile pour comprendre le patrimoine (thème 4).", chs: ["t3-intro", "t3-a1", "t3-a2", "t3-otc"] });

/* ======================= THÈME 3 — INTRODUCTION ======================= */
CHAPS["t3-intro"] = { th: "t3", code: "T3 · INTRODUCTION", t: "Histoire et mémoire, histoire et justice",
  ess: [
    "La mémoire est un rapport vécu, affectif et sélectif au passé, propre à un individu ou à un groupe ; l'histoire est une connaissance critique, fondée sur des sources et une méthode.",
    "Les mémoires sont plurielles et parfois concurrentes ; elles ont leurs temps (oubli, refoulement, retour) et deviennent un enjeu politique quand l'État commémore ou légifère.",
    "En France, les « lois mémorielles » (loi Gayssot 1990, lois de 2001, loi de 2005) ont déclenché un débat entre historiens et législateurs sur la liberté de l'histoire.",
    "Les notions de crime contre l'humanité (statut de Nuremberg, 8 août 1945) et de génocide (mot forgé par Raphael Lemkin en 1944, convention de l'ONU du 9 décembre 1948) naissent des crimes de masse du XXe siècle.",
    "Justice et histoire ne font pas le même métier : le juge tranche sur la responsabilité d'individus, l'historien explique ; mais les procès produisent des archives et façonnent les mémoires."
  ],
  att: [
    "Distinguer histoire et mémoire, et montrer comment elles s'articulent (sources, témoins, commémorations).",
    "Comprendre les usages politiques de la mémoire : commémorations, lois mémorielles, reconnaissances officielles.",
    "Définir précisément crime de guerre, crime contre l'humanité et génocide, et les replacer dans le contexte de leur élaboration (1915, 1944, 1945, 1948).",
    "Poser la question directrice du thème : quel rôle jouent la connaissance historique et la justice dans la reconstruction des sociétés après les conflits ?"
  ],
  secs: [
    { t: "Histoire et mémoire : deux rapports au passé", idees: [
      { t: "La mémoire, un rapport vécu et sélectif", h: "La mémoire est la présence du passé dans le présent d'un individu ou d'un groupe : souvenirs, récits, émotions, rites. Elle sélectionne, oublie, embellit ; elle sert l'identité du groupe. Le sociologue Maurice Halbwachs a montré que même les souvenirs individuels s'appuient sur des <b>cadres sociaux</b> (famille, religion, classe, nation) : on parle de <b>mémoire collective</b>.", ex: "Maurice Halbwachs publie <em>Les Cadres sociaux de la mémoire</em> en 1925 puis travaille à <em>La Mémoire collective</em>, ouvrage posthume (1950) : déporté, il meurt à Buchenwald en mars 1945." },
      { t: "L'histoire, une connaissance critique", h: "L'histoire cherche à établir et à expliquer les faits passés à partir de <b>sources</b> (archives, témoignages, objets) critiquées et recoupées. Elle vise la vérité, admet la complexité et se corrige sans cesse ; elle ne juge pas, elle rend intelligible. L'historien Pierre Nora résume l'opposition : « La mémoire est un absolu et l'histoire ne connaît que le relatif. »", ex: "Pierre Nora dirige <em>Les Lieux de mémoire</em> (7 volumes, 1984-1992) : il y étudie la façon dont la nation française a construit sa mémoire (le Panthéon, le 14 Juillet, <em>La Marseillaise</em>, le Tour de France…)." },
      { t: "Des mémoires plurielles, parfois concurrentes", h: "Un même événement laisse plusieurs mémoires : celles des combattants, des victimes, des familles, des États. Elles peuvent s'ignorer, se contredire ou rivaliser pour la reconnaissance : on parle de <b>concurrence des mémoires</b>. L'historien doit les étudier comme des objets, sans en épouser aucune.", ex: "Pour la guerre d'Algérie, l'historien Benjamin Stora distingue dès <em>La Gangrène et l'Oubli</em> (1991) des mémoires cloisonnées : appelés du contingent, pieds-noirs, harkis, immigrés algériens, État algérien (voir l'axe 1)." },
      { t: "Le temps du témoin", h: "Depuis les années 1960, la parole des témoins prend une place considérable dans l'espace public. Le témoin apporte une expérience irremplaçable ; mais son récit est une source comme une autre, que l'historien confronte aux archives. L'historienne Annette Wieviorka parle d'« ère du témoin » (1998).", ex: "Au procès d'Adolf Eichmann à Jérusalem (avril-décembre 1961), l'accusation fait entendre plus d'une centaine de témoins rescapés : pour la première fois, le génocide des Juifs est raconté au monde par ses victimes." },
      { t: "Les mémoires ont leurs temps", h: "Une mémoire collective n'est pas fixe : après un conflit, viennent souvent l'oubli ou le silence, puis le retour du passé refoulé, porté par une nouvelle génération, des historiens, des procès ou des œuvres. L'historien Henry Rousso a décrit ces phases pour la mémoire de Vichy (<em>Le Syndrome de Vichy</em>, 1987).", ex: "Le documentaire <em>Le Chagrin et la Pitié</em> de Marcel Ophuls (1969, en salles en France en 1971) et le livre de l'historien américain Robert Paxton, <em>La France de Vichy</em> (traduit en 1973), brisent le mythe d'une France unanimement résistante." }
    ] },
    { t: "Quand l'État se saisit de la mémoire", idees: [
      { t: "Des politiques de la mémoire", h: "L'État commémore (journées nationales, monuments, panthéonisations), enseigne et reconnaît officiellement des responsabilités. Le <b>devoir de mémoire</b>, expression devenue courante dans les années 1990, désigne l'obligation morale de se souvenir des crimes et de leurs victimes.", ex: "Le 16 juillet 1995, Jacques Chirac reconnaît la responsabilité de l'État français dans la rafle du Vél d'Hiv (16-17 juillet 1942, plus de 13 000 Juifs arrêtés à Paris par la police française) : « La France, ce jour-là, accomplissait l'irréparable. »" },
      { t: "Les lois mémorielles", h: "On appelle <b>lois mémorielles</b> les lois qui disent l'histoire ou qualifient un fait historique. Certaines sanctionnent la négation d'un crime, d'autres se contentent de reconnaître. Elles répondent aux demandes de groupes porteurs de mémoire.", ex: "Loi Gayssot du 13 juillet 1990 (punit la contestation des crimes contre l'humanité jugés à Nuremberg) ; loi du 29 janvier 2001 (« La France reconnaît publiquement le génocide arménien de 1915 ») ; loi Taubira du 21 mai 2001 (la traite et l'esclavage sont des crimes contre l'humanité) ; loi du 23 février 2005 sur les rapatriés." },
      { t: "La riposte des historiens", h: "L'article 4 de la loi du 23 février 2005 demandait aux programmes scolaires de reconnaître « le rôle positif de la présence française outre-mer ». Des historiens protestent : ce n'est pas à la loi d'écrire l'histoire. Le 12 décembre 2005, dix-neuf historiens lancent l'appel « Liberté pour l'histoire ».", ex: "L'alinéa contesté est abrogé par décret le 15 février 2006. En 2008, un rapport parlementaire (mission présidée par Bernard Accoyer) recommande de ne plus voter de lois mémorielles. Le 28 février 2012, le Conseil constitutionnel censure une loi qui punissait la négation du génocide arménien." },
      { t: "Du devoir de mémoire au travail de mémoire", h: "Le philosophe Paul Ricœur (<em>La Mémoire, l'histoire, l'oubli</em>, 2000) s'inquiète des abus de mémoire, par excès comme par défaut, et plaide pour une « juste mémoire », éclairée par l'histoire. On parle désormais plus volontiers de <b>travail de mémoire</b> : comprendre plutôt que seulement commémorer.", ex: "Le rapport remis par Benjamin Stora au président de la République le 20 janvier 2021 sur la colonisation et la guerre d'Algérie ne propose ni « repentance » ni loi, mais 22 recommandations : archives, commission de vérité, lieux de mémoire, enseignement." }
    ], viz: "anim:t3lois" },
    { t: "Crime contre l'humanité et génocide : des notions nées de l'histoire", idees: [
      { t: "Avant 1945 : les crimes de guerre", h: "Le droit de la guerre encadre d'abord les combats entre armées : conventions de La Haye (1899 et 1907) sur les lois et coutumes de la guerre. Un <b>crime de guerre</b> est une violation grave de ces règles (tuer des prisonniers, viser des civils, piller). Ce droit ne protège pas une population contre son propre État.", ex: "Le 24 mai 1915, la France, le Royaume-Uni et la Russie dénoncent les massacres des Arméniens de l'Empire ottoman comme des « crimes contre l'humanité et la civilisation » : première apparition diplomatique de l'expression. Le génocide des Arméniens fait environ 1,2 à 1,5 million de morts (1915-1916)." },
      { t: "Raphael Lemkin invente le mot « génocide »", h: "Juriste juif polonais réfugié aux États-Unis, Raphael Lemkin forge en 1944 le mot <b>génocide</b>, à partir du grec <em>genos</em> (race, peuple) et du latin <em>-cide</em> (tuer), pour nommer un « crime sans nom » : la destruction planifiée d'un groupe en tant que tel.", ex: "Le mot apparaît dans son livre <em>Axis Rule in Occupied Europe</em> (1944), consacré aux politiques d'occupation nazies. Lemkin pense aussi aux massacres des Arméniens. Une grande partie de sa famille est assassinée pendant la Shoah." },
      { t: "1945 : le crime contre l'humanité entre dans le droit", h: "L'accord de Londres du 8 août 1945 crée le Tribunal militaire international de Nuremberg. Son statut (article 6) définit trois crimes : crimes contre la paix, crimes de guerre et <b>crimes contre l'humanité</b> : assassinat, extermination, réduction en esclavage, déportation et autres actes inhumains commis contre des populations civiles, ou persécutions pour des motifs politiques, raciaux ou religieux.", ex: "À Nuremberg (20 novembre 1945-1er octobre 1946), le mot « génocide » figure dans l'acte d'accusation, mais aucun accusé n'est condamné pour ce crime, qui n'existe pas encore en droit." },
      { t: "1948 : la convention sur le génocide", h: "Adoptée par l'Assemblée générale de l'ONU le 9 décembre 1948, la convention pour la prévention et la répression du crime de génocide le définit comme des actes « commis dans l'intention de détruire, en tout ou en partie, un groupe national, ethnique, racial ou religieux, comme tel ». Ce qui le distingue est l'<b>intention</b> de détruire un groupe.", ex: "Les cinq actes énumérés : meurtre de membres du groupe ; atteinte grave à leur intégrité ; conditions d'existence devant entraîner sa destruction ; mesures visant à entraver les naissances ; transfert forcé d'enfants. Les groupes politiques et sociaux ne sont pas protégés, à la demande notamment de l'URSS." },
      { t: "Des crimes imprescriptibles", h: "Un crime <b>imprescriptible</b> peut être jugé quel que soit le temps écoulé. C'est ce qui permet de juger des décennies plus tard des criminels nazis ou leurs complices.", ex: "La France rend imprescriptibles les crimes contre l'humanité par la loi du 26 décembre 1964 ; l'ONU adopte une convention sur l'imprescriptibilité le 26 novembre 1968. Sans elles, ni Klaus Barbie (1987) ni Maurice Papon (1998) n'auraient pu être jugés." },
      { t: "Trois crimes à bien distinguer", h: "Le statut de Rome de la Cour pénale internationale (1998) reprend la hiérarchie : <b>crime de guerre</b> (violation grave du droit des conflits armés) ; <b>crime contre l'humanité</b> (actes commis dans le cadre d'une attaque généralisée ou systématique contre une population civile, en guerre comme en paix) ; <b>génocide</b> (intention de détruire un groupe). S'y ajoute le crime d'agression.", ex: "Le 2 septembre 1998, le Tribunal pénal international pour le Rwanda condamne Jean-Paul Akayesu, ancien bourgmestre de Taba : c'est la première condamnation pour génocide prononcée par une juridiction internationale, cinquante ans après la convention." }
    ], viz: "anim:t3droit", plis: [{ t: "Pour aller plus loin : Lemkin et Lauterpacht, deux juristes de Lviv", h: "<p>Deux juristes passés par l'université de Lwów (aujourd'hui Lviv, en Ukraine) ont inventé les deux grandes notions du droit pénal international. Hersch Lauterpacht défend le <b>crime contre l'humanité</b>, qui protège les individus ; Raphael Lemkin défend le <b>génocide</b>, qui protège les groupes. Lauterpacht craint qu'en insistant sur les groupes on n'attise les identités qui ont nourri les massacres ; Lemkin pense qu'on ne comprend pas le crime nazi sans voir qu'il visait des peuples. L'avocat Philippe Sands raconte cette double histoire dans <em>Retour à Lemberg</em> (2016). <em>(Hors programme, mais très utile en introduction de dissertation.)</em></p>" }] }
  ],
  pieges: [
    "Opposer histoire « vraie » et mémoire « fausse » : la mémoire est un objet d'histoire, et l'histoire nourrit la mémoire.",
    "Employer « génocide » pour tout massacre : il faut l'intention de détruire un groupe national, ethnique, racial ou religieux comme tel.",
    "Dire qu'on a jugé le « génocide » à Nuremberg : le tribunal a condamné pour crimes contre l'humanité ; la convention sur le génocide date de 1948.",
    "Confondre devoir de mémoire (obligation morale) et histoire (connaissance critique).",
    "Oublier que les lois mémorielles n'ont pas toutes la même portée : certaines punissent (loi Gayssot), d'autres reconnaissent seulement (2001)."
  ],
  retenir: [
    ["Mémoire / histoire", "Mémoire : rapport vécu, affectif, sélectif, d'un groupe au passé (Halbwachs, 1925). Histoire : connaissance critique fondée sur des sources (Nora, <em>Les Lieux de mémoire</em>, 1984-1992)."],
    ["Temps de la mémoire", "Oubli, refoulement puis retour (Rousso, <em>Le Syndrome de Vichy</em>, 1987) ; « ère du témoin » (Wieviorka) depuis le procès Eichmann (1961)."],
    ["Lois mémorielles", "Gayssot (13 juill. 1990) ; génocide arménien (29 janv. 2001) ; Taubira (21 mai 2001) ; 23 févr. 2005 (art. 4 abrogé en 2006) ; « Liberté pour l'histoire » (12 déc. 2005) ; censure du Conseil constitutionnel (28 févr. 2012)."],
    ["Crime contre l'humanité", "Déclaration du 24 mai 1915 ; statut de Nuremberg, art. 6 c (8 août 1945) ; imprescriptible en France (26 déc. 1964)."],
    ["Génocide", "Mot forgé par Lemkin (1944) ; convention de l'ONU (9 déc. 1948) : intention de détruire tout ou partie d'un groupe national, ethnique, racial ou religieux ; 1re condamnation internationale : Akayesu (2 sept. 1998)."],
    ["Question du thème", "Quel rôle jouent l'histoire et la justice dans la reconstruction des sociétés après les conflits ?"]
  ],
  qcm: [
    { q: "Qui a forgé la notion de « mémoire collective » ?", o: ["Pierre Nora", "Maurice Halbwachs", "Paul Ricœur", "Henry Rousso"], r: 1, e: "Maurice Halbwachs, dans <em>Les Cadres sociaux de la mémoire</em> (1925).", ref: "1-1" },
    { q: "Qu'est-ce qui caractérise d'abord l'histoire par rapport à la mémoire ?", o: ["Elle est plus émouvante", "Elle repose sur la critique des sources", "Elle est fixée par la loi", "Elle ne concerne que les vainqueurs"], r: 1, e: "L'histoire est une connaissance critique, qui confronte et recoupe des sources.", ref: "1-2" },
    { q: "Qui a dirigé <em>Les Lieux de mémoire</em> (1984-1992) ?", o: ["Benjamin Stora", "Annette Wieviorka", "Pierre Nora", "Robert Paxton"], r: 2, e: "Pierre Nora, qui oppose la mémoire, « un absolu », à l'histoire, qui « ne connaît que le relatif ».", ref: "1-2" },
    { q: "Quel procès ouvre, selon Annette Wieviorka, « l'ère du témoin » ?", o: ["Nuremberg (1945)", "Eichmann (1961)", "Barbie (1987)", "Papon (1997)"], r: 1, e: "Au procès Eichmann, à Jérusalem en 1961, plus d'une centaine de rescapés témoignent.", ref: "1-4" },
    { q: "Que reconnaît Jacques Chirac le 16 juillet 1995 ?", o: ["Le génocide arménien", "La responsabilité de l'État français dans la rafle du Vél d'Hiv", "La torture en Algérie", "L'esclavage comme crime contre l'humanité"], r: 1, e: "« La France, ce jour-là, accomplissait l'irréparable. »", ref: "2-1" },
    { q: "Que fait la loi Gayssot du 13 juillet 1990 ?", o: ["Elle reconnaît le génocide arménien", "Elle punit la contestation des crimes contre l'humanité jugés à Nuremberg", "Elle crée le 8 mai férié", "Elle reconnaît l'esclavage comme crime"], r: 1, e: "Elle crée un délit de contestation des crimes contre l'humanité tels que définis par le statut de Nuremberg.", ref: "2-2" },
    { q: "Pourquoi des historiens lancent-ils l'appel « Liberté pour l'histoire » en décembre 2005 ?", o: ["Pour obtenir plus d'archives", "Parce qu'ils refusent que la loi écrive l'histoire", "Pour défendre la loi Gayssot", "Pour créer un musée"], r: 1, e: "L'article 4 de la loi du 23 février 2005 (« rôle positif » de la colonisation) a déclenché la protestation.", ref: "2-3" },
    { q: "Que décide le Conseil constitutionnel le 28 février 2012 ?", o: ["Il valide toutes les lois mémorielles", "Il censure une loi punissant la négation du génocide arménien", "Il abroge la loi Gayssot", "Il crée la journée du 19 mars"], r: 1, e: "Il juge que cette loi porte une atteinte inconstitutionnelle à la liberté d'expression.", ref: "2-3" },
    { q: "Qui a forgé le mot « génocide » ?", o: ["Hersch Lauterpacht", "Raphael Lemkin", "Robert Jackson", "René Cassin"], r: 1, e: "Raphael Lemkin, en 1944, dans <em>Axis Rule in Occupied Europe</em>.", ref: "3-2" },
    { q: "Quand l'expression « crimes contre l'humanité » apparaît-elle dans une déclaration diplomatique ?", o: ["1899", "1915", "1945", "1948"], r: 1, e: "Le 24 mai 1915, à propos des massacres des Arméniens.", ref: "3-1" },
    { q: "Quel texte définit pour la première fois juridiquement le crime contre l'humanité ?", o: ["La convention de La Haye (1907)", "Le statut du tribunal de Nuremberg (8 août 1945)", "La Charte de l'ONU (1945)", "La convention de 1948"], r: 1, e: "Article 6 c du statut annexé à l'accord de Londres.", ref: "3-3" },
    { q: "Qu'est-ce qui définit le génocide selon la convention de 1948 ?", o: ["Le nombre de victimes", "L'intention de détruire, en tout ou en partie, un groupe comme tel", "L'usage d'armes chimiques", "Le fait d'être commis en temps de guerre"], r: 1, e: "C'est l'intention qui compte, pas le nombre de morts.", ref: "3-4" },
    { q: "Depuis quand les crimes contre l'humanité sont-ils imprescriptibles en France ?", o: ["1945", "1964", "1990", "2002"], r: 1, e: "Loi du 26 décembre 1964 : elle rend possibles les procès Barbie, Touvier et Papon.", ref: "3-5" },
    { q: "Qui est le premier condamné pour génocide par une juridiction internationale ?", o: ["Hermann Göring", "Jean-Paul Akayesu", "Slobodan Milošević", "Radovan Karadžić"], r: 1, e: "Akayesu, par le TPIR, le 2 septembre 1998.", ref: "3-6" }
  ],
  fc: [
    ["Mémoire collective", "Souvenirs partagés par un groupe, construits dans des cadres sociaux (Halbwachs, 1925)."],
    ["Histoire", "Connaissance critique du passé, fondée sur des sources confrontées et recoupées."],
    ["Lieu de mémoire", "Lieu, objet, rite ou symbole où se cristallise la mémoire d'un groupe (Nora, 1984-1992)."],
    ["Devoir de mémoire", "Obligation morale de se souvenir des crimes et de leurs victimes."],
    ["Loi mémorielle", "Loi qui qualifie un fait historique (Gayssot 1990, 2001, 2005)."],
    ["Liberté pour l'histoire", "Appel de 19 historiens (12 décembre 2005) contre l'écriture de l'histoire par la loi."],
    ["Crime de guerre", "Violation grave des lois et coutumes de la guerre (La Haye 1899-1907, Genève 1949)."],
    ["Crime contre l'humanité", "Actes inhumains contre des civils dans le cadre d'une attaque généralisée ou systématique (statut de Nuremberg, 1945)."],
    ["Génocide", "Actes commis dans l'intention de détruire, en tout ou en partie, un groupe national, ethnique, racial ou religieux (convention du 9 décembre 1948)."],
    ["Raphael Lemkin", "Juriste polonais qui forge le mot « génocide » en 1944."],
    ["Imprescriptible", "Qui peut être jugé sans limite de temps (France, 26 décembre 1964)."],
    ["Akayesu", "Premier condamné pour génocide par un tribunal international (TPIR, 2 septembre 1998)."]
  ],
  bac: { s: "Histoire et mémoire : deux rapports au passé opposés ?", type: "Sujet de dissertation inventé pour le site (thème 3, introduction)", h: "<p><b>Problématique possible :</b> l'histoire et la mémoire s'opposent-elles, ou s'enrichissent-elles mutuellement dans la façon dont les sociétés se rapportent aux conflits passés ?</p><p><b>I. Deux rapports au passé différents.</b> Mémoire vécue, sélective, identitaire (Halbwachs, 1925) ; histoire critique, fondée sur les sources (Nora, 1984). Mémoires plurielles de la guerre d'Algérie (Stora, 1991).</p><p><b>II. Des tensions quand la mémoire devient politique.</b> Lois mémorielles (Gayssot 1990, 2001, 2005) ; « Liberté pour l'histoire » (2005) ; censure de 2012 ; reconnaissances officielles (Vél d'Hiv, 1995).</p><p><b>III. Une articulation nécessaire.</b> Les historiens brisent les mythes (Paxton, 1973 ; Rousso, 1987) ; les témoins nourrissent l'histoire (Eichmann, 1961) ; la « juste mémoire » (Ricœur, 2000) et le travail de mémoire (rapport Stora, 2021).</p>" }
};

/* Animation : les lois mémorielles en France (frise verticale) */
ANIMS.t3lois = {
  titre: "Les lois mémorielles en France : de l'élan au reflux (1990-2012)",
  scene: { w: 640, h: 380, svg:
    "<line x1='92' y1='26' x2='92' y2='360' stroke='var(--kraft-f)' stroke-width='3'/>" +
    "<text x='92' y='16' text-anchor='middle' class='lbl'>Lois et débats</text>" +
    "<g data-k='l90'><circle cx='92' cy='44' r='9' class='pt-b'/><text x='20' y='48' class='lbl-f'>1990</text><text x='110' y='42' class='lbl'>Loi Gayssot (13 juillet)</text><text x='110' y='57' class='lbl' style='font-weight:500'>punit la contestation des crimes contre l'humanité</text></g>" +
    "<g data-k='l99'><circle cx='92' cy='86' r='9' class='pt-b'/><text x='20' y='90' class='lbl-f'>1999</text><text x='110' y='84' class='lbl'>Loi du 18 octobre</text><text x='110' y='99' class='lbl' style='font-weight:500'>on dit enfin « guerre d'Algérie »</text></g>" +
    "<g data-k='l01a'><circle cx='92' cy='128' r='9' class='pt-b'/><text x='20' y='132' class='lbl-f'>2001</text><text x='110' y='126' class='lbl'>Loi du 29 janvier</text><text x='110' y='141' class='lbl' style='font-weight:500'>« La France reconnaît publiquement le génocide arménien de 1915 »</text></g>" +
    "<g data-k='l01b'><circle cx='92' cy='170' r='9' class='pt-b'/><text x='20' y='174' class='lbl-f'>2001</text><text x='110' y='168' class='lbl'>Loi Taubira (21 mai)</text><text x='110' y='183' class='lbl' style='font-weight:500'>traite et esclavage : crimes contre l'humanité</text></g>" +
    "<g data-k='l05'><circle cx='92' cy='212' r='9' class='pt-a'/><text x='20' y='216' class='lbl-f'>2005</text><text x='110' y='210' class='lbl'>Loi du 23 février, article 4</text><text x='110' y='225' class='lbl' style='font-weight:500'>« rôle positif de la présence française outre-mer »</text></g>" +
    "<g data-k='lph'><rect x='104' y='236' width='300' height='30' rx='4' fill='var(--rouge)' opacity='.14'/><text x='20' y='256' class='lbl-f'>2005</text><text x='110' y='255' class='lbl'>« Liberté pour l'histoire » (12 déc.) : 19 historiens</text></g>" +
    "<g data-k='l06'><line x1='110' y1='219' x2='400' y2='219' stroke='var(--rouge)' stroke-width='2.5'/><text x='410' y='223' class='lbl-f'>abrogé (15 févr. 2006)</text></g>" +
    "<g data-k='l08'><circle cx='92' cy='296' r='9' class='pt-b'/><text x='20' y='300' class='lbl-f'>2008</text><text x='110' y='294' class='lbl'>Rapport Accoyer (18 nov.)</text><text x='110' y='309' class='lbl' style='font-weight:500'>plus de nouvelles lois mémorielles : des résolutions</text></g>" +
    "<g data-k='l12'><circle cx='92' cy='340' r='9' class='pt-a'/><text x='20' y='344' class='lbl-f'>2012</text><text x='110' y='338' class='lbl'>Conseil constitutionnel (28 févr.)</text><text x='110' y='353' class='lbl' style='font-weight:500'>censure la loi punissant la négation du génocide arménien</text></g>"
  },
  etapes: [
    { date: "1990", titre: "Punir le négationnisme", texte: "La loi Gayssot crée un délit de contestation des crimes contre l'humanité définis à Nuremberg : elle vise les négationnistes qui nient l'existence des chambres à gaz.", montre: ["l90"], accent: ["l90"] },
    { date: "1999", titre: "Nommer une guerre", texte: "Pendant 37 ans, la loi parlait d'« opérations de maintien de l'ordre en Afrique du Nord ». La loi du 18 octobre 1999 reconnaît qu'il s'agissait d'une guerre.", montre: ["l99"], accent: ["l99"] },
    { date: "2001", titre: "Reconnaître un génocide", texte: "Une loi d'un seul article reconnaît le génocide arménien. Elle ne punit rien : c'est une reconnaissance symbolique, demandée par les descendants des victimes.", montre: ["l01a"], accent: ["l01a"] },
    { date: "2001", titre: "Qualifier l'esclavage", texte: "La loi Taubira fait de la traite négrière et de l'esclavage un crime contre l'humanité et demande qu'ils aient leur place dans les programmes scolaires.", montre: ["l01b"], accent: ["l01b"] },
    { date: "2005", titre: "Une loi qui écrit l'histoire scolaire", texte: "La loi sur les rapatriés demande que les programmes reconnaissent « le rôle positif » de la colonisation : c'est la loi de trop pour beaucoup d'historiens et d'enseignants.", montre: ["l05"], accent: ["l05"] },
    { date: "2005-2006", titre: "La riposte des historiens", texte: "L'appel « Liberté pour l'histoire » demande l'abrogation des lois mémorielles. L'alinéa contesté de la loi de 2005 est abrogé par décret en février 2006.", montre: ["lph", "l06"], accent: ["lph"] },
    { date: "2008", titre: "Le Parlement fait une pause", texte: "Une mission parlementaire conclut que le Parlement ne doit plus qualifier l'histoire par la loi, mais peut voter des résolutions, sans portée normative.", montre: ["l08"], accent: ["l08"] },
    { date: "2012", titre: "Le juge constitutionnel fixe une limite", texte: "Une loi punissant la négation des génocides reconnus par la loi est censurée au nom de la liberté d'expression. L'élan législatif des années 1990-2000 est retombé.", montre: ["l12"], accent: ["l12"] }
  ],
  source: "Sources : Légifrance (textes des lois), décision n° 2012-647 DC du Conseil constitutionnel, rapport de la mission d'information de l'Assemblée nationale sur les questions mémorielles (18 novembre 2008)."
};

/* Animation : naissance du droit des crimes de masse (trois couloirs) */
(function () {
  var X = function (a) { return Math.round(40 + (a - 1895) * 4.87); };
  var couloir = function (y, t) { return "<line x1='40' y1='" + y + "' x2='600' y2='" + y + "' stroke='var(--kraft-f)' stroke-width='2' stroke-dasharray='5 4'/><text x='40' y='" + (y - 30) + "' class='lbl' style='letter-spacing:.08em'>" + t + "</text>"; };
  var m = function (k, a, y, cl, l, dy, anc) { return "<g data-k='" + k + "'><circle cx='" + X(a) + "' cy='" + y + "' r='7' class='" + cl + "'/><text x='" + (X(a) + (anc === "end" ? -10 : 10)) + "' y='" + (y + dy) + "' class='lbl'" + (anc === "end" ? " text-anchor='end'" : "") + ">" + l + "</text></g>"; };
  var axe = "<line x1='40' y1='300' x2='600' y2='300' stroke='var(--encre2)' stroke-width='1.5'/>";
  [1900, 1925, 1950, 1975, 2000].forEach(function (a) { axe += "<line x1='" + X(a) + "' y1='296' x2='" + X(a) + "' y2='304' stroke='var(--encre2)'/><text x='" + X(a) + "' y='320' text-anchor='middle' class='lbl'>" + a + "</text>"; });
  ANIMS.t3droit = {
    titre: "Nommer et juger les crimes de masse : un droit né des guerres du XXe siècle",
    scene: { w: 640, h: 330, svg: axe + couloir(90, "CRIMES DE GUERRE") + couloir(170, "CRIMES CONTRE L'HUMANITÉ") + couloir(250, "GÉNOCIDE") +
      m("g1899", 1899, 90, "pt-b", "La Haye 1899-1907", 4, "start") +
      m("h1915", 1915, 170, "pt-b", "Déclaration du 24 mai 1915", -12, "start") +
      m("l1944", 1944, 250, "pt-b", "Lemkin : « génocide »", -12, "end") +
      m("h1945", 1945, 170, "pt-a", "Statut de Nuremberg, art. 6 c", 22, "start") +
      m("g1948", 1948, 250, "pt-a", "Convention de l'ONU", 22, "start") +
      m("g1949", 1949, 90, "pt-b", "Conventions de Genève", -12, "start") +
      m("i1964", 1964, 170, "pt-b", "imprescriptible (1964)", -12, "start") +
      "<g data-k='tpi'><rect x='" + (X(1993) - 4) + "' y='56' width='" + (X(1994) - X(1993) + 8) + "' height='210' rx='4' fill='var(--rouge)' opacity='.18'/><text x='" + (X(1993) - 8) + "' y='48' text-anchor='end' class='lbl-f'>TPIY 1993 · TPIR 1994</text></g>" +
      m("a1998", 1998, 250, "pt-a", "Akayesu", 22, "end") +
      "<g data-k='cpi'><rect x='" + (X(2002) - 4) + "' y='56' width='8' height='210' rx='4' fill='var(--acier)' opacity='.35'/><text x='" + (X(2002) + 8) + "' y='48' class='lbl-f' style='fill:var(--acier)'>CPI</text></g>"
    },
    etapes: [
      { date: "1899-1907", titre: "Encadrer la guerre entre armées", texte: "Les conventions de La Haye fixent les lois et coutumes de la guerre : un crime de guerre est une violation de ces règles. Rien ne protège encore un peuple contre son propre État.", montre: ["g1899"], accent: ["g1899"] },
      { date: "24 mai 1915", titre: "Une expression nouvelle", texte: "Face aux massacres des Arméniens par l'Empire ottoman, les Alliés parlent de « crimes contre l'humanité et la civilisation » : l'expression n'a pas encore de valeur juridique.", montre: ["h1915"], accent: ["h1915"] },
      { date: "1944", titre: "Nommer le crime sans nom", texte: "Raphael Lemkin forge le mot « génocide » pour désigner la destruction d'un groupe en tant que tel.", montre: ["l1944"], accent: ["l1944"] },
      { date: "8 août 1945", titre: "Le crime contre l'humanité devient du droit", texte: "Le statut du tribunal de Nuremberg définit le crime contre l'humanité. Les dirigeants nazis sont jugés pour ce crime, pour crimes de guerre et crimes contre la paix.", montre: ["h1945"], accent: ["h1945"] },
      { date: "1948-1949", titre: "Le génocide et les civils protégés", texte: "La convention du 9 décembre 1948 définit le génocide ; les conventions de Genève du 12 août 1949 protègent blessés, prisonniers et civils en temps de guerre.", montre: ["g1948", "g1949"], accent: ["g1948"] },
      { date: "1964", titre: "Juger sans limite de temps", texte: "La France rend les crimes contre l'humanité imprescriptibles : les procès Barbie, Touvier et Papon deviennent possibles des décennies plus tard.", montre: ["i1964"], accent: ["i1964"] },
      { date: "1993-1994", titre: "Le retour des tribunaux internationaux", texte: "Après la guerre froide, le Conseil de sécurité crée le TPIY (ex-Yougoslavie) puis le TPIR (Rwanda) : les trois crimes sont enfin jugés par des juges internationaux.", montre: ["tpi"], accent: ["tpi"] },
      { date: "2 sept. 1998", titre: "Première condamnation pour génocide", texte: "Cinquante ans après la convention, le TPIR condamne Jean-Paul Akayesu pour génocide ; il reconnaît aussi le viol comme acte constitutif de génocide.", montre: ["a1998"], accent: ["a1998"] },
      { date: "1998-2002", titre: "Une cour permanente", texte: "Le statut de Rome (17 juillet 1998) crée la Cour pénale internationale, en fonction depuis le 1er juillet 2002 : elle juge les trois crimes et le crime d'agression.", montre: ["cpi"], accent: ["cpi"] }
    ],
    source: "Repères : conventions de La Haye (1899, 1907), statut du TMI (1945), convention de l'ONU (1948), conventions de Genève (1949), loi n° 64-1326, statut de Rome (1998)."
  };
})();

/* ======================= THÈME 3 — AXE 1 ======================= */
CHAPS["t3-a1"] = { th: "t3", code: "T3 · AXE 1", t: "Histoire et mémoires des conflits",
  ess: [
    "Les causes de la Première Guerre mondiale font l'objet d'un débat historique depuis 1919 : l'article 231 du traité de Versailles impute la responsabilité à l'Allemagne, qui la rejette.",
    "Ce débat a des implications politiques : responsabilité partagée dans l'entre-deux-guerres, thèse de Fritz Fischer (1961) qui ébranle l'Allemagne fédérale, « somnambules » de Christopher Clark (2012) au moment du centenaire.",
    "La guerre d'Algérie (1954-1962) a longtemps été une guerre sans nom en France (reconnue comme « guerre » par la loi du 18 octobre 1999).",
    "Ses mémoires sont plurielles et cloisonnées (appelés, pieds-noirs, harkis, immigrés algériens, État algérien) ; les historiens et l'ouverture des archives ont permis un travail de mémoire, encore inachevé.",
    "Les deux jalons montrent que l'histoire savante intervient dans le débat public et que la mémoire d'un conflit pèse sur les relations entre États (réconciliation franco-allemande, tensions franco-algériennes)."
  ],
  att: [
    "Montrer comment un débat historique (les responsabilités du déclenchement de la guerre en 1914) a des implications politiques, de 1919 à nos jours.",
    "Étudier les mémoires de la guerre d'Algérie, leur pluralité et leur évolution, en France et en Algérie.",
    "Comprendre le rôle des historiens, des archives, des témoins et des États dans l'articulation entre histoire et mémoires."
  ],
  secs: [
    { t: "Un débat historique et ses implications politiques : les causes de la Première Guerre mondiale", idees: [
      { t: "L'engrenage de l'été 1914", h: "L'attentat de Sarajevo déclenche une crise que le jeu des alliances transforme en guerre européenne en cinq semaines : Triple-Entente (France, Russie, Royaume-Uni) contre Triple-Alliance (Allemagne, Autriche-Hongrie ; l'Italie reste neutre en 1914).", ex: "28 juin 1914 : assassinat de l'archiduc François-Ferdinand par Gavrilo Princip ; 5-6 juillet : l'Allemagne assure l'Autriche-Hongrie de son soutien (« chèque en blanc ») ; 23 juillet : ultimatum à la Serbie ; 28 juillet : déclaration de guerre à la Serbie ; 30 juillet : mobilisation générale russe ; 1er août : l'Allemagne déclare la guerre à la Russie ; 3 août : à la France ; 4 août : invasion de la Belgique, le Royaume-Uni entre en guerre." },
      { t: "1919 : la « responsabilité » allemande inscrite dans un traité", h: "L'article 231 du traité de Versailles (28 juin 1919) fait reconnaître à l'Allemagne et à ses alliés leur responsabilité dans les pertes et dommages de la guerre, pour fonder les réparations. En Allemagne, toute la classe politique dénonce le « mensonge de la culpabilité » (<em>Kriegsschuldlüge</em>).", ex: "Pour prouver son innocence, le ministère allemand des Affaires étrangères publie de 1922 à 1927 quarante volumes de documents diplomatiques (<em>Die Grosse Politik der europäischen Kabinette</em>) ; la France répond par ses propres <em>Documents diplomatiques français</em> à partir de 1929. L'histoire devient une arme." },
      { t: "L'entre-deux-guerres : la responsabilité partagée", h: "Les historiens des années 1920-1930 lisent ces archives et concluent à une responsabilité partagée, avec des nuances : Pierre Renouvin insiste sur le rôle de l'Allemagne et de l'Autriche-Hongrie, d'autres sur la course aux armements et la mobilisation russe. Cette lecture apaisée sert la réconciliation… et nourrit la remise en cause du traité de Versailles par les nationalistes allemands.", ex: "Pierre Renouvin, ancien combattant mutilé, publie <em>Les Origines immédiates de la guerre</em> en 1925. Dans ses <em>Mémoires de guerre</em> (1933-1936), l'ancien Premier ministre britannique David Lloyd George écrit que les nations ont « glissé » dans la guerre." },
      { t: "1961 : la thèse de Fritz Fischer", h: "L'historien allemand Fritz Fischer, à partir des archives allemandes, montre que les dirigeants du Reich ont sciemment pris le risque d'une guerre européenne et poursuivi des buts de guerre expansionnistes. Il suggère une continuité entre l'Empire de Guillaume II et le nazisme : c'est un séisme politique en Allemagne fédérale.", ex: "<em>Griff nach der Weltmacht</em> (« Les buts de guerre de l'Allemagne impériale », 1961) s'appuie notamment sur le programme de septembre 1914 du chancelier Bethmann Hollweg (annexions, domination de l'Europe centrale). La controverse culmine au congrès des historiens allemands de Berlin en 1964." },
      { t: "2012 : les « somnambules » de Christopher Clark", h: "Au moment du centenaire, l'historien australien Christopher Clark, professeur à Cambridge, déplace le regard vers les Balkans, la Russie et la France : aucune puissance n'a voulu une guerre générale, toutes ont pris des risques en croyant pouvoir contrôler la crise. Le livre connaît un immense succès, surtout en Allemagne, où certains y voient une forme de soulagement.", ex: "<em>The Sleepwalkers</em> (2012), traduit en français en 2013 (<em>Les Somnambules</em>). L'historien allemand Gerd Krumeich lui répond dans <em>Le Feu aux poudres</em> (2014), en rappelant le rôle décisif de Berlin et de Vienne : le débat continue." },
      { t: "Un débat qui a toujours des implications politiques", h: "Désigner un responsable de 1914, c'est encore aujourd'hui prendre position sur la place de l'Allemagne en Europe, sur la Serbie, ou sur la paix par l'équilibre des puissances. Mais les historiens français et allemands travaillent désormais ensemble, et la mémoire commune de la guerre sert la réconciliation.", ex: "Le 3 août 2014, cent ans jour pour jour après la déclaration de guerre de l'Allemagne à la France, François Hollande et Joachim Gauck commémorent ensemble la guerre au Hartmannswillerkopf, en Alsace. Un manuel d'histoire franco-allemand commun a été publié de 2006 à 2011 (trois volumes)." }
    ], viz: "anim:t3juillet" },
    { t: "Mémoires et histoire d'un conflit : la guerre d'Algérie", idees: [
      { t: "Une guerre longtemps sans nom", h: "La guerre d'Algérie commence avec les attentats de la « Toussaint rouge » (1er novembre 1954) et s'achève par les accords d'Évian (18 mars 1962), le cessez-le-feu du 19 mars et l'indépendance (5 juillet 1962). Officiellement, la France y menait des « opérations de maintien de l'ordre » : l'Algérie était alors constituée de départements français.", ex: "Plus d'un million de jeunes appelés du contingent servent en Algérie ; environ 25 000 militaires français meurent. Côté algérien, les historiens estiment les morts entre 250 000 et 400 000 ; le chiffre officiel algérien est d'un million et demi de « martyrs ». Le mot « guerre » n'entre dans la loi française que le 18 octobre 1999." },
      { t: "L'oubli organisé, puis des mémoires cloisonnées", h: "Les amnisties de 1962 à 1968 empêchent de juger les crimes commis pendant la guerre. Chaque groupe garde sa mémoire, souvent douloureuse, et la transmet peu : appelés qui se taisent, pieds-noirs rapatriés, harkis relégués dans des camps, immigrés algériens victimes de la répression, FLN au pouvoir en Algérie.", ex: "En 1962, environ 800 000 Européens d'Algérie (« pieds-noirs ») gagnent la métropole. Des harkis (supplétifs algériens de l'armée française) sont massacrés en Algérie après l'indépendance (plusieurs dizaines de milliers selon les estimations, très débattues) ; ceux qui arrivent en France sont souvent placés dans des camps, comme Rivesaltes ou Bias." },
      { t: "Des dates qui divisent", h: "La concurrence des mémoires se lit dans le calendrier. Les associations d'anciens appelés commémorent le cessez-le-feu du 19 mars 1962 ; les associations de rapatriés le refusent, car les violences ont continué après (massacre d'Oran, 5 juillet 1962 ; enlèvements, harkis). L'État multiplie les journées.", ex: "Journée nationale d'hommage aux harkis le 25 septembre (2001, officialisée en 2003) ; journée du 5 décembre pour les morts de la guerre d'Algérie (décret du 26 septembre 2003, date sans signification historique, choisie pour ne froisser personne) ; journée du 19 mars créée par la loi du 6 décembre 2012." },
      { t: "La mémoire officielle algérienne", h: "En Algérie, la guerre de libération est le récit fondateur de l'État et la source de légitimité du FLN, parti unique jusqu'en 1989. Ce récit héroïque et unanime laisse peu de place aux divisions internes (FLN contre MNA, purges) ou aux harkis, présentés comme des traîtres.", ex: "Le Maqam Echahid (mémorial du Martyr) d'Alger est inauguré le 5 juillet 1982, pour le vingtième anniversaire de l'indépendance. Le 3 juillet 2020, la France restitue à l'Algérie les crânes de 24 combattants de la résistance à la conquête du XIXe siècle, conservés au Muséum national d'histoire naturelle." },
      { t: "Le retour du refoulé : la torture et le travail des historiens", h: "À partir des années 1990, une nouvelle génération d'historiens travaille sur les archives et les témoignages. En 2000-2001, le débat sur la torture éclate : des victimes témoignent, des officiers avouent. L'histoire savante éclaire et apaise en partie un débat passionnel.", ex: "Le 20 juin 2000, <em>Le Monde</em> publie le témoignage de Louisette Ighilahriz, militante du FLN torturée en 1957 ; en 2001, le général Paul Aussaresses reconnaît dans un livre avoir pratiqué la torture et des exécutions, et il est condamné en 2002 pour complicité d'apologie de crimes de guerre. La même année, Raphaëlle Branche publie sa thèse, <em>La Torture et l'armée pendant la guerre d'Algérie</em> (2001)." },
      { t: "Des gestes de reconnaissance, une mémoire encore conflictuelle", h: "Depuis 2012, les présidents français multiplient les reconnaissances, sans « excuses » officielles. La mémoire de la guerre reste au cœur des relations entre Paris et Alger, qui alternent rapprochements et crises.", ex: "17 octobre 2012 : François Hollande reconnaît la « sanglante répression » du 17 octobre 1961 ; 13 septembre 2018 : Emmanuel Macron reconnaît que Maurice Audin est mort sous la torture de militaires français ; 20 janvier 2021 : rapport Stora ; 23 février 2022 : loi de reconnaissance envers les harkis ; août 2022 : création d'une commission mixte d'historiens français et algériens. Le 24 décembre 2025, l'Assemblée populaire nationale algérienne adopte une loi criminalisant la colonisation française ; révisé en mars 2026 (sans les demandes d'excuses et de réparations), le texte est définitivement adopté par le Parlement en avril 2026." }
    ], viz: "anim:t3algerie" },
    { t: "Ce que montrent les deux jalons", idees: [
      { t: "L'historien dans la cité", h: "Les historiens ne sont pas en dehors des débats : leurs travaux sont lus, utilisés, contestés par les politiques et l'opinion. Leur force est la méthode : archives, recoupement, refus de juger à la place des tribunaux.", ex: "En 1961, Fischer est accusé de trahir son pays ; en 2021, Benjamin Stora est critiqué à la fois en France et en Algérie pour son rapport : signe que l'histoire touche des identités." },
      { t: "La mémoire, ressource politique et diplomatique", h: "La mémoire d'un conflit peut servir à rassembler une nation, à légitimer un pouvoir ou à peser dans une négociation entre États.", ex: "La mémoire partagée de 1914-1918 a servi la réconciliation franco-allemande (Verdun, 22 septembre 1984 : Mitterrand et Kohl main dans la main) ; la mémoire de la guerre d'Algérie reste un instrument de pression dans les crises franco-algériennes (rappel de l'ambassadeur algérien en juillet 2024)." },
      { t: "Réconcilier par l'histoire ?", h: "Réconcilier ne signifie pas oublier : cela passe par l'accès aux archives, la reconnaissance des faits et le travail commun des historiens des deux pays. Le cas franco-allemand montre que c'est possible ; le cas franco-algérien montre que c'est long.", ex: "La France ouvre en décembre 2021, avec quinze ans d'avance, l'accès aux archives des enquêtes judiciaires de police et de gendarmerie de la guerre d'Algérie. La commission mixte d'historiens créée en 2022 a vu ses travaux ralentis par la crise diplomatique ouverte en 2024." }
    ] }
  ],
  pieges: [
    "Présenter la responsabilité de 1914 comme une question tranchée : c'est un débat historique, dont les réponses ont varié avec les sources et le contexte politique.",
    "Confondre l'article 231 (responsabilité des dommages, base des réparations) et une « culpabilité » morale formulée en ces termes dans le traité.",
    "Parler « de la » mémoire de la guerre d'Algérie : il y a des mémoires, portées par des groupes différents.",
    "Oublier l'Algérie : le jalon porte aussi sur la mémoire officielle algérienne et les relations entre les deux États.",
    "Mélanger les dates : 1er novembre 1954 (début), 18 mars 1962 (accords d'Évian), 19 mars (cessez-le-feu), 5 juillet 1962 (indépendance)."
  ],
  retenir: [
    ["Été 1914", "28 juin Sarajevo ; 5-6 juill. « chèque en blanc » ; 23 juill. ultimatum ; 28 juill. guerre à la Serbie ; 30 juill. mobilisation russe ; 1er-4 août guerre générale."],
    ["Le débat", "Article 231 (1919) ; « mensonge de la culpabilité » ; responsabilité partagée (Renouvin, 1925) ; Fischer (1961) ; Clark (2012) contre Krumeich (2014)."],
    ["Guerre d'Algérie", "1er nov. 1954-5 juill. 1962 ; plus d'un million d'appelés ; environ 25 000 militaires français et 250 000 à 400 000 Algériens morts ; « guerre » reconnue par la loi du 18 oct. 1999."],
    ["Mémoires", "Appelés (19 mars), pieds-noirs (800 000 rapatriés), harkis (25 sept.), immigrés (17 oct. 1961), État algérien (« un million et demi de martyrs »)."],
    ["Histoire", "Stora (1991, rapport 2021) ; Branche (2001) ; torture : Ighilahriz (2000), Aussaresses (2001) ; archives judiciaires ouvertes en 2021."],
    ["Reconnaissances", "Hollande 17 oct. 2012 ; Audin 2018 ; harkis 2022 ; commission mixte 2022 ; loi algérienne de déc. 2025."]
  ],
  qcm: [
    { q: "Quel jour l'archiduc François-Ferdinand est-il assassiné ?", o: ["28 juin 1914", "28 juillet 1914", "1er août 1914", "4 août 1914"], r: 0, e: "À Sarajevo, par Gavrilo Princip, le 28 juin 1914.", ref: "1-1" },
    { q: "Qu'appelle-t-on le « chèque en blanc » ?", o: ["Les réparations de 1919", "Le soutien inconditionnel de l'Allemagne à l'Autriche-Hongrie (5-6 juillet 1914)", "Un prêt américain", "L'ultimatum à la Serbie"], r: 1, e: "Berlin assure Vienne de son appui, quelles que soient les conséquences.", ref: "1-1" },
    { q: "Que fonde l'article 231 du traité de Versailles ?", o: ["La SDN", "La responsabilité de l'Allemagne et de ses alliés dans les dommages, base des réparations", "Le désarmement naval", "L'indépendance de la Pologne"], r: 1, e: "Les Allemands le dénoncent comme le « mensonge de la culpabilité ».", ref: "1-2" },
    { q: "Quelle thèse Fritz Fischer défend-il en 1961 ?", o: ["La responsabilité de la Russie", "Les dirigeants allemands ont sciemment pris le risque de la guerre et avaient des buts expansionnistes", "Une guerre voulue par la France", "Une guerre accidentelle"], r: 1, e: "<em>Griff nach der Weltmacht</em> : un séisme en Allemagne fédérale.", ref: "1-4" },
    { q: "Quel historien a publié <em>Les Somnambules</em> (2012) ?", o: ["Gerd Krumeich", "Christopher Clark", "Pierre Renouvin", "Fritz Fischer"], r: 1, e: "Clark insiste sur la responsabilité diffuse de toutes les puissances.", ref: "1-5" },
    { q: "Quand le mot « guerre d'Algérie » entre-t-il dans la loi française ?", o: ["1962", "1981", "18 octobre 1999", "2012"], r: 2, e: "Loi du 18 octobre 1999 : on parlait auparavant d'« opérations de maintien de l'ordre ».", ref: "2-1" },
    { q: "Quel événement marque le début de la guerre d'Algérie ?", o: ["Les émeutes de Sétif (8 mai 1945)", "La « Toussaint rouge » (1er novembre 1954)", "La bataille d'Alger (1957)", "Le 13 mai 1958"], r: 1, e: "Une série d'attentats du FLN, le 1er novembre 1954.", ref: "2-1" },
    { q: "Pourquoi la date du 19 mars divise-t-elle les mémoires ?", o: ["Elle ne correspond à rien", "Les violences ont continué après le cessez-le-feu (Oran, harkis)", "C'est la date de la Toussaint rouge", "C'est une fête algérienne"], r: 1, e: "Les associations de rapatriés et de harkis refusent de commémorer une date suivie de massacres.", ref: "2-3" },
    { q: "Qui sont les harkis ?", o: ["Des colons européens", "Des Algériens supplétifs de l'armée française", "Des appelés du contingent", "Des militants du FLN"], r: 1, e: "Une loi du 23 février 2022 reconnaît la responsabilité de la France envers eux.", ref: "2-2" },
    { q: "Que symbolise le Maqam Echahid d'Alger (1982) ?", o: ["La réconciliation franco-algérienne", "La mémoire officielle algérienne des « martyrs » de la guerre de libération", "La mémoire des pieds-noirs", "Le souvenir de la Première Guerre mondiale"], r: 1, e: "Inauguré le 5 juillet 1982 pour les vingt ans de l'indépendance.", ref: "2-4" },
    { q: "Quel témoignage relance en 2000 le débat sur la torture ?", o: ["Celui de Louisette Ighilahriz dans <em>Le Monde</em>", "Le rapport Stora", "Le film <em>La Bataille d'Alger</em>", "Un discours de Jacques Chirac"], r: 0, e: "Publié le 20 juin 2000, suivi des aveux du général Aussaresses en 2001.", ref: "2-5" },
    { q: "Que reconnaît Emmanuel Macron le 13 septembre 2018 ?", o: ["Le massacre de Sétif", "La mort de Maurice Audin sous la torture de militaires français", "Le génocide arménien", "La responsabilité dans le 17 octobre 1961"], r: 1, e: "Il reconnaît aussi l'existence d'un « système » permettant la torture.", ref: "2-6" },
    { q: "Que propose le rapport Stora (20 janvier 2021) ?", o: ["Des excuses officielles", "22 recommandations pour un travail de mémoire, sans repentance", "Une loi mémorielle", "La fermeture des archives"], r: 1, e: "Archives, commission « Mémoires et vérité », lieux de mémoire, enseignement.", ref: "2-6" },
    { q: "Quel geste symbolise à Verdun la réconciliation franco-allemande le 22 septembre 1984 ?", o: ["Un traité signé", "Mitterrand et Kohl se tenant la main", "Un manuel commun", "Un défilé commun"], r: 1, e: "Une mémoire partagée de 1914-1918 au service de la réconciliation.", ref: "3-2" }
  ],
  fc: [
    ["28 juin 1914", "Attentat de Sarajevo : François-Ferdinand assassiné par Gavrilo Princip."],
    ["Chèque en blanc", "Soutien inconditionnel de l'Allemagne à l'Autriche-Hongrie (5-6 juillet 1914)."],
    ["Article 231", "Article du traité de Versailles (1919) sur la responsabilité allemande, base des réparations."],
    ["Kriegsschuldlüge", "« Mensonge de la culpabilité » : rejet allemand de l'article 231."],
    ["Fritz Fischer", "Historien allemand : les buts de guerre expansionnistes du Reich (1961)."],
    ["Christopher Clark", "<em>Les Somnambules</em> (2012) : une responsabilité partagée par toutes les puissances."],
    ["1er novembre 1954", "« Toussaint rouge » : début de la guerre d'Algérie."],
    ["18-19 mars 1962", "Accords d'Évian et cessez-le-feu en Algérie."],
    ["Loi du 18 octobre 1999", "La France reconnaît officiellement la « guerre d'Algérie »."],
    ["Harkis", "Algériens supplétifs de l'armée française ; loi de reconnaissance du 23 février 2022."],
    ["17 octobre 1961", "Répression sanglante d'une manifestation d'Algériens à Paris ; reconnue par Hollande en 2012."],
    ["Rapport Stora", "Remis le 20 janvier 2021 : 22 recommandations pour un travail de mémoire sur la guerre d'Algérie."]
  ],
  bac: { s: "Les mémoires de la guerre d'Algérie en France et en Algérie depuis 1962", type: "Sujet de dissertation inventé pour le site (thème 3, axe 1)", h: "<p><b>Problématique possible :</b> comment les mémoires de la guerre d'Algérie sont-elles passées de l'oubli organisé à une reconnaissance progressive, et pourquoi restent-elles conflictuelles ?</p><p><b>I. 1962-années 1980 : silence en France, mémoire officielle en Algérie.</b> Amnisties (1962-1968), « opérations de maintien de l'ordre » ; mémoires cloisonnées (pieds-noirs, harkis dans les camps, appelés) ; récit héroïque du FLN (Maqam Echahid, 1982).</p><p><b>II. Années 1990-2000 : le réveil des mémoires et le travail des historiens.</b> Stora (1991) ; loi du 18 octobre 1999 ; torture (Ighilahriz 2000, Aussaresses 2001, Branche 2001) ; guerre des dates (19 mars, 5 décembre, 25 septembre) ; loi de 2005 contestée.</p><p><b>III. Depuis 2012 : reconnaissances et tensions entre États.</b> Hollande (2012), Audin (2018), rapport Stora (2021), harkis (2022), commission mixte (2022) ; crises diplomatiques et loi algérienne de décembre 2025.</p>" }
};

/* Animation : mémoires de la guerre d'Algérie (deux couloirs) */
(function () {
  var X = function (a) { return Math.round(60 + (a - 1960) * 8.3); };
  var g = function (k, a, y, cl, l1, l2, anc) {
    var dx = anc === "end" ? -10 : 10, ta = anc === "end" ? " text-anchor='end'" : "";
    return "<g data-k='" + k + "'><circle cx='" + X(a) + "' cy='" + y + "' r='7' class='" + cl + "'/><text x='" + (X(a) + dx) + "' y='" + (y - 4) + "' class='lbl'" + ta + ">" + l1 + "</text>" + (l2 ? "<text x='" + (X(a) + dx) + "' y='" + (y + 11) + "' class='lbl' style='font-weight:500'" + ta + ">" + l2 + "</text>" : "") + "</g>";
  };
  var axe = "<line x1='40' y1='190' x2='620' y2='190' stroke='var(--encre2)' stroke-width='1.5'/>";
  [1960, 1970, 1980, 1990, 2000, 2010, 2020].forEach(function (a) { axe += "<text x='" + X(a) + "' y='206' text-anchor='middle' class='lbl'>" + a + "</text>"; });
  axe += "<text x='40' y='22' class='lbl-f' style='fill:var(--acier)'>EN FRANCE</text><text x='40' y='370' class='lbl-f'>EN ALGÉRIE</text>";
  ANIMS.t3algerie = {
    titre: "De l'oubli à la reconnaissance : les mémoires de la guerre d'Algérie",
    scene: { w: 640, h: 380, svg: axe +
      g("f62", 1962, 60, "pt-b", "Amnisties (1962-1968)", "l'oubli organisé", "start") +
      g("a62", 1962, 300, "pt-a", "Indépendance (5 juillet 1962)", "« un million et demi de martyrs »", "start") +
      g("a82", 1982, 250, "pt-a", "Maqam Echahid (1982)", "mémoire officielle du FLN", "start") +
      g("f91", 1991, 110, "pt-b", "Stora, La Gangrène et l'Oubli", "", "end") +
      g("f99", 1999, 60, "pt-b", "Loi du 18 octobre 1999 :", "« guerre d'Algérie »", "end") +
      g("f00", 2000, 150, "pt-b", "Débat sur la torture", "(2000-2001)", "start") +
      g("f12", 2012, 60, "pt-b", "Hollande : 17 octobre 1961", "« sanglante répression »", "end") +
      g("f18", 2018, 110, "pt-b", "Audin (2018), Stora (2021)", "harkis (loi de 2022)", "end") +
      g("a20", 2020, 250, "pt-a", "Restitution de 24 crânes", "(3 juillet 2020)", "end") +
      g("a22", 2022, 300, "pt-a", "Commission mixte d'historiens", "(août 2022)", "end") +
      "<g data-k='a25'><circle cx='" + X(2025) + "' cy='340' r='8' class='pt-a'/><text x='" + (X(2025) - 12) + "' y='344' text-anchor='end' class='lbl-f'>Loi criminalisant la colonisation (déc. 2025)</text></g>"
    },
    etapes: [
      { date: "1962-1968", titre: "Oublier pour tourner la page", texte: "En France, des décrets (1962) puis une loi d'amnistie (1968) empêchent de juger les crimes de la guerre, y compris ceux de l'OAS : la guerre devient un silence.", montre: ["f62"], accent: ["f62"] },
      { date: "1962", titre: "Une mémoire fondatrice en Algérie", texte: "L'Algérie indépendante fait de la guerre de libération son récit fondateur : un peuple uni derrière le FLN, « un million et demi de martyrs ».", montre: ["a62"], accent: ["a62"] },
      { date: "1982", titre: "Monumentaliser le récit national", texte: "Le Maqam Echahid domine Alger : la mémoire officielle légitime le pouvoir du FLN et laisse peu de place aux divisions ou aux harkis.", montre: ["a82"], accent: ["a82"] },
      { date: "1991-1999", titre: "Les historiens et la loi nomment la guerre", texte: "Benjamin Stora analyse des mémoires cloisonnées ; en 1999, la loi reconnaît enfin qu'il s'agissait d'une guerre.", montre: ["f91", "f99"], accent: ["f99"] },
      { date: "2000-2001", titre: "Le retour du refoulé", texte: "Témoignages de victimes, aveux d'officiers, thèse de Raphaëlle Branche : la torture, longtemps niée, entre dans le débat public et dans l'histoire savante.", montre: ["f00"], accent: ["f00"] },
      { date: "2012-2022", titre: "Le temps des reconnaissances", texte: "Les présidents français reconnaissent des faits précis (17 octobre 1961, Audin, harkis) sans présenter d'excuses ; le rapport Stora propose un travail de mémoire.", montre: ["f12", "f18"], accent: ["f12", "f18"] },
      { date: "2020-2022", titre: "Une mémoire partagée ?", texte: "Restitution de restes humains à l'Algérie, puis création d'une commission mixte d'historiens : la mémoire devient un sujet de coopération entre États.", montre: ["a20", "a22"], accent: ["a22"] },
      { date: "Déc. 2025", titre: "La mémoire, arme diplomatique", texte: "En pleine crise entre Paris et Alger, l'Assemblée populaire nationale algérienne vote une loi qui criminalise la colonisation (adoption définitive en avril 2026) : la mémoire du conflit reste un enjeu politique entre les deux États.", montre: ["a25"], accent: ["a25"] }
    ],
    source: "Repères : Légifrance (lois de 1968, 1999, 2022), rapport Stora (2021), presse algérienne et française (loi votée le 24 décembre 2025, adoptée définitivement en avril 2026)."
  };
})();

/* ======================= THÈME 3 — AXE 2 ======================= */
CHAPS["t3-a2"] = { th: "t3", code: "T3 · AXE 2", t: "Histoire, mémoire et justice",
  ess: [
    "Après un crime de masse, juger les coupables est une condition de la reconstruction : la justice établit des faits, désigne des responsables, reconnaît les victimes et produit des archives.",
    "Au Rwanda, après le génocide des Tutsis (avril-juillet 1994, environ 800 000 morts selon l'ONU), les tribunaux gacaca, juridictions populaires installées dans les collines, ont jugé près de deux millions d'affaires entre 2002 et 2012.",
    "La justice s'exerce à plusieurs échelles : locale (gacaca), nationale (procès en France au nom de la compétence universelle), internationale (TPIR d'Arusha).",
    "Le TPIY (La Haye, 1993-2017), créé par le Conseil de sécurité pendant la guerre de Bosnie, a mis en accusation 161 personnes et qualifié de génocide le massacre de Srebrenica (juillet 1995).",
    "Cette justice reste limitée : lenteur, coût, accusations de « justice des vainqueurs », mémoires toujours divisées ; la Cour pénale internationale (2002) se heurte à la souveraineté des puissances."
  ],
  att: [
    "Montrer comment la justice se saisit des génocides et des crimes de masse aux échelles locale, nationale et internationale.",
    "Étudier les tribunaux gacaca : origine, fonctionnement, bilan, limites, rôle dans la réconciliation.",
    "Étudier la construction d'une justice pénale internationale avec le TPIY : création, jugements, apports au droit, limites.",
    "Réfléchir aux rapports entre justice, histoire (établissement des faits) et mémoire (reconnaissance des victimes)."
  ],
  secs: [
    { t: "La justice à l'échelle locale : les tribunaux gacaca face au génocide des Tutsis", idees: [
      { t: "Le génocide des Tutsis (avril-juillet 1994)", h: "Le 6 avril 1994, l'avion du président Habyarimana est abattu au-dessus de Kigali. Dès le 7 avril, les extrémistes hutu du « Hutu Power », l'armée et les milices Interahamwe, appuyés par la Radio-télévision libre des Mille Collines (RTLM), exterminent les Tutsis et assassinent les Hutu opposés au massacre. Le génocide prend fin avec la victoire du Front patriotique rwandais (FPR) en juillet.", ex: "En une centaine de jours, environ 800 000 personnes sont tuées selon l'ONU ; le dénombrement des autorités rwandaises compte plus d'un million de victimes. La plupart sont tuées par des voisins, à la machette, dans les collines, les églises et les écoles." },
      { t: "Une justice ordinaire impossible", h: "Après le génocide, le pays est dévasté, la plupart des magistrats sont morts ou en fuite, et des dizaines de milliers de suspects sont arrêtés. Les procès ordinaires commencent en décembre 1996, mais ils sont beaucoup trop lents.", ex: "À la fin des années 1990, environ 120 000 détenus s'entassent dans des prisons prévues pour quelques milliers. Au rythme des tribunaux ordinaires, il aurait fallu plus d'un siècle pour les juger tous." },
      { t: "Les gacaca : une tradition réinventée", h: "Le mot <em>gacaca</em> désigne en kinyarwanda l'herbe sur laquelle les anciens réglaient autrefois les litiges du village. La loi organique du 26 janvier 2001 transforme cette pratique en juridictions pénales : dans chaque cellule et chaque secteur, des juges non professionnels élus par la population, les <b>inyangamugayo</b> (« personnes intègres »), jugent en public, en présence des rescapés et des accusés.", ex: "Les juges sont élus en octobre 2001 ; une phase pilote est lancée le 18 juin 2002, puis les gacaca sont généralisées à tout le pays en 2005. Les accusés sont classés en catégories : les planificateurs restent jugés par les tribunaux ordinaires." },
      { t: "Avouer pour réduire sa peine", h: "Le cœur du système est l'<b>aveu</b> : l'accusé qui avoue, demande pardon et dit la vérité (où sont les corps, qui a tué) obtient une réduction de peine, dont une partie peut être purgée en travaux d'intérêt général. La vérité sert à la fois la justice, l'histoire (on sait ce qui s'est passé sur chaque colline) et la mémoire des familles.", ex: "Beaucoup de rescapés ont appris lors des audiences où avaient été jetés les corps de leurs proches, ce qui a permis de les inhumer dans les mémoriaux." },
      { t: "Un bilan massif", h: "Les gacaca ont jugé en dix ans un nombre d'affaires sans équivalent dans l'histoire judiciaire, en impliquant toute la population. Elles ont vidé les prisons et donné une place publique à la parole des rescapés.", ex: "Selon le bilan officiel présenté à leur clôture, le 18 juin 2012, plus de 12 000 juridictions gacaca ont traité 1 958 634 affaires." },
      { t: "Des limites et des critiques", h: "Les droits de la défense étaient faibles (pas d'avocat), des juges ont été corrompus ou intimidés, des témoins menacés ou tués, de fausses accusations ont été portées. Surtout, les crimes commis par des soldats du FPR, au pouvoir depuis 1994, ont été exclus des gacaca : certains y voient une justice des vainqueurs.", ex: "Le rapport de Human Rights Watch « Justice compromise » (31 mai 2011) reconnaît l'apport des gacaca mais dénonce ces failles. La réconciliation passe aussi par d'autres politiques : commémorations Kwibuka chaque 7 avril, programme <em>Ndi Umunyarwanda</em> (« Je suis rwandais », 2013), mémoriaux inscrits au patrimoine mondial en 2023 (Nyamata, Murambi, Gisozi, Bisesero)." }
    ], viz: "anim:t3gacaca" },
    { t: "Juger le génocide des Tutsis à d'autres échelles", idees: [
      { t: "L'échelle internationale : le TPIR d'Arusha", h: "Le Conseil de sécurité crée le Tribunal pénal international pour le Rwanda par la résolution 955 du 8 novembre 1994. Installé à Arusha (Tanzanie), il juge les principaux responsables : militaires, ministres, propagandistes.", ex: "Le 4 septembre 1998, l'ancien Premier ministre Jean Kambanda est condamné à la perpétuité pour génocide : premier chef de gouvernement condamné pour ce crime. Le 3 décembre 2003, le « procès des médias » condamne les responsables de la RTLM et du journal <em>Kangura</em>. Le TPIR ferme le 31 décembre 2015 après avoir condamné 62 personnes." },
      { t: "L'échelle nationale : la compétence universelle", h: "Des États tiers jugent aussi des génocidaires réfugiés sur leur sol, au nom de la <b>compétence universelle</b> : certains crimes sont si graves que tout État peut les juger, quel que soit le lieu où ils ont été commis.", ex: "En France, Pascal Simbikangwa, ancien capitaine de la garde présidentielle, est condamné le 14 mars 2014 à 25 ans de réclusion : premier procès en France lié au génocide des Tutsis. En 2001 déjà, la Belgique avait jugé « les quatre de Butare »." },
      { t: "Justice, histoire et responsabilité des États", h: "La justice juge des individus ; la responsabilité des États relève de l'histoire et de la politique. La France, alliée du régime Habyarimana, a longtemps refusé d'examiner son rôle.", ex: "La commission d'historiens présidée par Vincent Duclert conclut le 26 mars 2021 à des « responsabilités lourdes et accablantes » de la France, sans complicité de génocide. Le 27 mai 2021, à Kigali, Emmanuel Macron reconnaît ces responsabilités devant le mémorial de Gisozi." }
    ] },
    { t: "La construction d'une justice pénale internationale : le TPIY", idees: [
      { t: "Les guerres de Yougoslavie et la « purification ethnique »", h: "La Yougoslavie éclate à partir de 1991. En Bosnie-Herzégovine (1992-1995), les forces serbes de Bosnie, mais aussi croates et bosniaques à une moindre échelle, pratiquent la <b>purification ethnique</b> : expulsions, massacres, camps, viols systématiques, pour créer des territoires ethniquement homogènes.", ex: "La guerre de Bosnie fait environ 100 000 morts. Le siège de Sarajevo dure du 5 avril 1992 au 29 février 1996, le plus long d'une capitale dans l'histoire contemporaine. Les accords de Dayton, signés à Paris le 14 décembre 1995, mettent fin à la guerre." },
      { t: "Une création inédite du Conseil de sécurité", h: "Pour la première fois depuis Nuremberg et Tokyo, un tribunal pénal international est créé, cette fois par le Conseil de sécurité de l'ONU agissant en vertu du chapitre VII de la Charte, pendant la guerre elle-même. Il siège à La Haye et juge les crimes de guerre, crimes contre l'humanité et génocides commis sur le territoire de l'ex-Yougoslavie depuis 1991.", ex: "Résolution 808 du 22 février 1993 (principe), puis résolution 827 du 25 mai 1993 (statut). Le premier jugement, contre Duško Tadić, responsable local serbe de Bosnie accusé de crimes dans les camps de la région de Prijedor, est rendu le 7 mai 1997." },
      { t: "Des jugements qui font avancer le droit", h: "La jurisprudence du TPIY précise les crimes internationaux : responsabilité du supérieur hiérarchique, viol et esclavage sexuel comme crimes contre l'humanité, génocide « en partie » d'un groupe dans une zone limitée.", ex: "Le 22 février 2001 (affaire Kunarac, Foča), le viol et la réduction en esclavage sexuel sont jugés comme crimes contre l'humanité. Le 2 août 2001, le général Krstić est condamné pour génocide à Srebrenica, où environ 8 000 hommes et garçons bosniaques musulmans ont été tués en juillet 1995 ; en appel (19 avril 2004), il est condamné pour complicité de génocide." },
      { t: "Juger les chefs", h: "Le TPIY poursuit les plus hauts responsables, y compris un chef d'État en exercice, ce qui était sans précédent. Les arrestations dépendent de la coopération des États, obtenue notamment par la pression de l'Union européenne (conditionnalité de l'adhésion).", ex: "Slobodan Milošević, inculpé le 24 mai 1999 alors qu'il préside la Yougoslavie, est livré le 28 juin 2001 ; il meurt en détention le 11 mars 2006, avant le verdict. Radovan Karadžić (arrêté en 2008) est condamné à la perpétuité en appel le 20 mars 2019 ; Ratko Mladić (arrêté en 2011) est condamné le 22 novembre 2017, peine confirmée le 8 juin 2021." },
      { t: "Le bilan du TPIY", h: "Le tribunal ferme le 31 décembre 2017 ; un Mécanisme international (MTPI) achève ses dernières affaires. Il a jugé des responsables de tous les camps et constitué des millions de pages d'archives, un matériau immense pour les historiens.", ex: "161 personnes mises en accusation : 93 condamnées, 18 acquittées (bilan du tribunal mis à jour en 2023), les autres ayant été renvoyées devant des juridictions nationales, étant décédées ou ayant vu leur acte d'accusation retiré." },
      { t: "Une justice contestée, des mémoires toujours divisées", h: "Beaucoup de Serbes ont vu dans le TPIY une justice anti-serbe ; beaucoup de Bosniaques ont jugé les peines trop faibles et les acquittements scandaleux. Les condamnés sont parfois accueillis en héros. La justice établit les faits, mais ne suffit pas à réconcilier.", ex: "Le 29 novembre 2017, le général croate de Bosnie Slobodan Praljak se suicide en pleine audience en avalant du poison. Le 23 mai 2024, l'Assemblée générale de l'ONU fait du 11 juillet la Journée internationale de réflexion et de commémoration du génocide de Srebrenica (84 voix pour, 19 contre, 68 abstentions), contre l'avis de la Serbie." }
    ], viz: "anim:t3tribunaux" },
    { t: "Vers une justice pénale universelle ?", idees: [
      { t: "Une cour permanente : la CPI", h: "Le statut de Rome (17 juillet 1998) crée la Cour pénale internationale, en fonction depuis le 1er juillet 2002 à La Haye. Elle est <b>complémentaire</b> des justices nationales : elle n'intervient que si les États ne veulent pas ou ne peuvent pas juger.", ex: "Le 27 septembre 2016, la CPI condamne Ahmad Al Faqi Al Mahdi à neuf ans de prison pour la destruction de mausolées de Tombouctou : premier procès centré sur la destruction du patrimoine culturel comme crime de guerre (voir le thème 4)." },
      { t: "Les limites : la souveraineté des puissances", h: "Les États-Unis, la Chine, la Russie et l'Inde ne sont pas parties au statut. La CPI dépend des États pour arrêter les suspects et ses mandats ne sont pas toujours exécutés.", ex: "Mandats d'arrêt contre Vladimir Poutine (17 mars 2023, déportation d'enfants ukrainiens) et contre Benyamin Netanyahou (21 novembre 2024) : ni l'un ni l'autre n'a été arrêté. En revanche, l'ancien président philippin Rodrigo Duterte est remis à la Cour le 12 mars 2025." },
      { t: "Une justice fragilisée", h: "La CPI est accusée de viser surtout des Africains ; des États la quittent ; des puissances la sanctionnent. Les tribunaux mixtes ou régionaux offrent une autre voie, plus proche des victimes.", ex: "La Hongrie quitte la Cour (retrait effectif en juin 2026) ; le Burkina Faso, le Mali et le Niger annoncent leur retrait le 22 septembre 2025. À Dakar, les Chambres africaines extraordinaires ont condamné l'ancien président tchadien Hissène Habré le 30 mai 2016." }
    ], viz: "carte:justice" }
  ],
  pieges: [
    "Présenter les gacaca comme une justice « traditionnelle » inchangée : c'est une institution nouvelle, créée par une loi de 2001, inspirée d'une pratique ancienne.",
    "Confondre le TPIR (Arusha, international, chefs) et les gacaca (collines, local, exécutants).",
    "Confondre la CIJ (différends entre États ; Bosnie contre Serbie, 2007) et le TPIY ou la CPI (individus).",
    "Oublier que le TPIY a jugé des responsables de tous les camps, même si les Serbes de Bosnie sont les plus nombreux.",
    "Croire qu'un jugement suffit à réconcilier : la négation de Srebrenica reste forte en Republika Srpska et en Serbie."
  ],
  retenir: [
    ["Génocide des Tutsis", "7 avril-juillet 1994 ; environ 800 000 morts (ONU), plus d'un million selon les autorités rwandaises ; Interahamwe, RTLM."],
    ["Gacaca", "Loi du 26 janv. 2001 ; juges élus (inyangamugayo) ; pilote 18 juin 2002, généralisation 2005 ; aveux et peines réduites ; 1 958 634 affaires selon le bilan officiel ; clôture le 18 juin 2012 ; critiques (HRW, 2011)."],
    ["Autres échelles", "TPIR (résolution 955, 8 nov. 1994 ; Akayesu 1998, Kambanda 1998 ; fermé en 2015) ; compétence universelle (Simbikangwa, 2014) ; rapport Duclert (2021)."],
    ["TPIY", "Résolutions 808 et 827 (1993) ; La Haye ; Tadić (1997), Kunarac (2001), Krstić (2001-2004) ; Milošević (mort en 2006), Karadžić (2019), Mladić (2017-2021) ; 161 accusés, 93 condamnés ; fermé le 31 déc. 2017."],
    ["Srebrenica", "Juillet 1995, environ 8 000 morts ; génocide (TPIY 2001-2004, CIJ 26 févr. 2007) ; journée du 11 juillet (ONU, 23 mai 2024)."],
    ["CPI", "Statut de Rome (17 juill. 1998), en fonction le 1er juill. 2002 ; complémentarité ; limites (mandats Poutine 2023, Netanyahou 2024 ; retraits)."]
  ],
  qcm: [
    { q: "Quel événement déclenche le génocide des Tutsis le 6 avril 1994 ?", o: ["L'invasion ougandaise", "L'attentat contre l'avion du président Habyarimana", "Les accords d'Arusha", "L'arrivée des casques bleus"], r: 1, e: "Dès le 7 avril, les massacres planifiés commencent.", ref: "1-1" },
    { q: "Combien de victimes le génocide des Tutsis fait-il selon l'ONU ?", o: ["Environ 80 000", "Environ 800 000", "Environ 8 millions", "Environ 200 000"], r: 1, e: "Environ 800 000 selon l'ONU, plus d'un million selon les autorités rwandaises.", ref: "1-1" },
    { q: "Pourquoi crée-t-on les gacaca ?", o: ["Pour remplacer le TPIR", "Parce que la justice ordinaire ne pouvait pas juger quelque 120 000 détenus", "Pour juger les crimes du FPR", "À la demande de l'ONU"], r: 1, e: "Il aurait fallu plus d'un siècle aux tribunaux ordinaires.", ref: "1-2" },
    { q: "Qui sont les inyangamugayo ?", o: ["Les miliciens", "Les juges élus des gacaca", "Les procureurs du TPIR", "Les rescapés"], r: 1, e: "« Personnes intègres » élues par la population.", ref: "1-3" },
    { q: "Quel est le cœur du fonctionnement des gacaca ?", o: ["La peine de mort", "L'aveu en échange d'une réduction de peine", "Le jury populaire tiré au sort", "L'avocat obligatoire"], r: 1, e: "L'aveu sert la justice, l'histoire et la mémoire des familles.", ref: "1-4" },
    { q: "Quand les gacaca ferment-elles officiellement ?", o: ["1998", "2005", "18 juin 2012", "31 décembre 2015"], r: 2, e: "Après avoir traité 1 958 634 affaires selon le bilan officiel.", ref: "1-5" },
    { q: "Quelle critique majeure est faite aux gacaca ?", o: ["Elles étaient trop lentes", "Elles ont exclu les crimes commis par des soldats du FPR", "Elles étaient dirigées par l'ONU", "Elles ont acquitté tout le monde"], r: 1, e: "D'où l'accusation de justice des vainqueurs, avec la faiblesse des droits de la défense.", ref: "1-6" },
    { q: "Où siège le TPIR ?", o: ["Kigali", "Arusha", "La Haye", "Genève"], r: 1, e: "Arusha, en Tanzanie, de 1994 à 2015.", ref: "2-1" },
    { q: "Qu'est-ce que la compétence universelle ?", o: ["La compétence de l'ONU sur tous les États", "La possibilité pour un État de juger certains crimes graves quel que soit le lieu où ils ont été commis", "Le droit de veto", "Le pouvoir de la CIJ"], r: 1, e: "Exemple : le procès Simbikangwa à Paris en 2014.", ref: "2-2" },
    { q: "Quelle résolution du Conseil de sécurité adopte le statut du TPIY ?", o: ["242", "678", "827", "955"], r: 2, e: "Résolution 827 du 25 mai 1993 ; la 955 crée le TPIR.", ref: "3-2" },
    { q: "Quel crime le TPIY reconnaît-il à Srebrenica ?", o: ["Un crime de guerre seulement", "Un génocide", "Un crime d'agression", "Aucun crime"], r: 1, e: "Affaire Krstić (2001, 2004), confirmée par la CIJ en 2007.", ref: "3-3" },
    { q: "Que devient Slobodan Milošević ?", o: ["Condamné à perpétuité", "Acquitté", "Mort en détention en 2006, avant le verdict", "Jamais arrêté"], r: 2, e: "Livré au TPIY en 2001, il meurt le 11 mars 2006.", ref: "3-4" },
    { q: "Combien de personnes le TPIY a-t-il mises en accusation ?", o: ["22", "62", "161", "1 958 634"], r: 2, e: "161 accusés ; 93 condamnés et 18 acquittés.", ref: "3-5" },
    { q: "Quelle est la différence entre la CPI et les TPI ?", o: ["La CPI est permanente et fondée sur un traité", "La CPI ne juge que les États", "Les TPI sont permanents", "Aucune"], r: 0, e: "Les TPI sont temporaires, créés par le Conseil de sécurité ; la CPI repose sur le statut de Rome.", ref: "4-1" }
  ],
  fc: [
    ["7 avril 1994", "Début du génocide des Tutsis au Rwanda."],
    ["Gacaca", "Juridictions populaires rwandaises (loi du 26 janvier 2001, clôture le 18 juin 2012)."],
    ["Inyangamugayo", "« Personnes intègres » : juges élus des gacaca."],
    ["1 958 634", "Nombre d'affaires traitées par les gacaca selon le bilan officiel de 2012."],
    ["TPIR", "Tribunal pénal international pour le Rwanda, Arusha (résolution 955, 8 novembre 1994 ; fermé en 2015)."],
    ["Compétence universelle", "Possibilité pour un État de juger certains crimes internationaux commis ailleurs (Simbikangwa, Paris, 2014)."],
    ["Purification ethnique", "Expulsion ou extermination d'une population pour rendre un territoire ethniquement homogène."],
    ["TPIY", "Tribunal pénal international pour l'ex-Yougoslavie, La Haye (1993-2017), 161 accusés."],
    ["Srebrenica", "Massacre d'environ 8 000 Bosniaques musulmans en juillet 1995, qualifié de génocide."],
    ["Mladić", "Chef militaire des Serbes de Bosnie, condamné à la perpétuité (2017, confirmé en 2021)."],
    ["Statut de Rome", "Traité du 17 juillet 1998 créant la Cour pénale internationale (en fonction en 2002)."],
    ["Complémentarité", "Principe selon lequel la CPI n'agit que si les justices nationales ne veulent ou ne peuvent pas juger."]
  ],
  bac: { s: "Juger les crimes de masse à différentes échelles depuis les années 1990", type: "Sujet de dissertation inventé pour le site (thème 3, axe 2)", h: "<p><b>Problématique possible :</b> en quoi la justice, aux échelles locale, nationale et internationale, contribue-t-elle à la reconstruction des sociétés après les crimes de masse, et quelles en sont les limites ?</p><p><b>I. Juger pour établir les faits et reconnaître les victimes.</b> TPIY (1993) et TPIR (1994) ; jurisprudences (Akayesu 1998, Kunarac 2001, Krstić) ; archives pour l'histoire.</p><p><b>II. Une justice adaptée aux échelles et aux sociétés.</b> Gacaca (2002-2012, 1 958 634 affaires selon le bilan officiel, aveux) ; compétence universelle (Simbikangwa 2014) ; tribunaux mixtes (Sierra Leone, Cambodge, Dakar).</p><p><b>III. Des limites qui pèsent sur la réconciliation.</b> Justice des vainqueurs (crimes du FPR exclus) ; mémoires divisées (Praljak 2017, négation de Srebrenica, résolution de 2024) ; CPI contestée (mandats non exécutés, retraits 2025-2026).</p>" }
};

/* Animation : des prisons aux collines, la justice gacaca */
(function () {
  var colline = function (x, y, s) { return "<path d='M" + (x - 40 * s) + "," + y + " Q" + x + "," + (y - 46 * s) + " " + (x + 40 * s) + "," + y + "Z' fill='var(--ok)' opacity='.55'/><circle cx='" + x + "' cy='" + (y - 22 * s) + "' r='" + (5 * s) + "' fill='var(--papier)' stroke='var(--encre)' stroke-width='1.5'/>"; };
  var collines = "";
  [[300, 168, 1], [370, 176, .8], [430, 166, 1.1], [500, 176, .9], [560, 168, 1], [330, 228, .9], [400, 238, 1.1], [470, 228, .8], [540, 240, 1]].forEach(function (c) { collines += colline(c[0], c[1], c[2]); });
  ANIMS.t3gacaca = {
    titre: "Des prisons pleines aux collines : comment les gacaca ont jugé le génocide",
    scene: { w: 640, h: 360, svg:
      "<text x='620' y='26' text-anchor='end' class='lbl-f'>RWANDA, 1994-2012</text>" +
      "<g data-k='geno'><rect x='20' y='50' width='220' height='70' rx='6' fill='var(--rouge)' opacity='.16'/><text x='32' y='78' class='lbl-f'>≈ 800 000 morts</text><text x='32' y='98' class='lbl'>(ONU) en une centaine de jours</text><text x='32' y='113' class='lbl' style='font-weight:500'>avril-juillet 1994</text></g>" +
      "<g data-k='prison'><rect x='20' y='136' width='220' height='120' rx='6' fill='none' stroke='var(--encre)' stroke-width='2'/>" +
        "<rect x='30' y='186' width='200' height='60' fill='var(--encre2)' opacity='.45'/><path d='M40,136 V256 M80,136 V256 M120,136 V256 M160,136 V256 M200,136 V256' stroke='var(--encre)' stroke-width='2' opacity='.6'/>" +
        "<text x='130' y='160' text-anchor='middle' class='lbl'>Prisons du pays</text><text x='130' y='222' text-anchor='middle' class='lbl-f'>≈ 120 000 détenus</text></g>" +
      "<g data-k='lent'><text x='130' y='280' text-anchor='middle' class='lbl'>tribunaux ordinaires :</text><text x='130' y='296' text-anchor='middle' class='lbl-f'>plus d'un siècle de procès ?</text></g>" +
      "<g data-k='loi'><text x='300' y='52' class='lbl-f' style='fill:var(--acier)'>Loi du 26 janvier 2001</text><text x='300' y='68' class='lbl'>juges élus dans chaque cellule et secteur</text></g>" +
      "<g data-k='coll'>" + collines + "<text x='430' y='272' text-anchor='middle' class='lbl'>plus de 12 000 juridictions gacaca</text></g>" +
      "<g data-k='flux'><path class='fleche trace' pathLength='1' d='M240,190 Q270,170 292,166'/><path class='fleche trace' pathLength='1' d='M240,226 Q275,250 300,232'/></g>" +
      "<g data-k='aveu'><rect x='282' y='80' width='330' height='34' rx='17' fill='var(--papier)' stroke='var(--acier)' stroke-width='2'/><text x='446' y='102' text-anchor='middle' class='lbl'>aveu + pardon → peine réduite, travaux d'intérêt général</text></g>" +
      "<g data-k='bilan'><rect x='300' y='290' width='300' height='56' rx='6' fill='var(--ok)' opacity='.18'/><text x='450' y='314' text-anchor='middle' class='lbl-f' style='fill:var(--ok)'>1 958 634 affaires (bilan officiel)</text><text x='450' y='334' text-anchor='middle' class='lbl'>clôture : 18 juin 2012</text></g>" +
      "<g data-k='crit'><text x='20' y='330' class='lbl-f'>Limites :</text><text x='20' y='346' class='lbl' style='font-weight:500'>pas d'avocat, pressions, crimes du FPR exclus</text></g>"
    },
    etapes: [
      { date: "Avril-juillet 1994", titre: "Le génocide", texte: "Les Tutsis et les Hutu opposés aux massacres sont exterminés, souvent par leurs voisins : des centaines de milliers de tueurs, des centaines de milliers de victimes.", montre: ["geno"], accent: ["geno"] },
      { date: "1995-2000", titre: "Des prisons saturées", texte: "Environ 120 000 suspects s'entassent dans les prisons. Les procès ordinaires commencent fin 1996, mais le système judiciaire, décimé, avance très lentement.", montre: ["prison", "lent"], accent: ["prison"] },
      { date: "26 janv. 2001", titre: "Une loi pour juger dans les collines", texte: "Le Rwanda transforme une pratique villageoise de règlement des conflits en juridictions pénales locales, avec des juges élus par la population.", montre: ["loi"], accent: ["loi"] },
      { date: "2002-2005", titre: "Les collines jugent", texte: "Après une phase pilote lancée le 18 juin 2002, les gacaca sont généralisées en 2005 : les audiences ont lieu en plein air, devant les rescapés, les familles et les accusés.", montre: ["coll", "flux"], accent: ["coll"] },
      { date: "2005-2012", titre: "Dire la vérité contre une peine réduite", texte: "Les accusés qui avouent et révèlent où sont les corps voient leur peine réduite, en partie remplacée par des travaux d'intérêt général : la vérité sert la justice et la mémoire.", montre: ["aveu"], accent: ["aveu"] },
      { date: "18 juin 2012", titre: "Un bilan sans équivalent", texte: "À leur clôture, les gacaca ont traité près de deux millions d'affaires et vidé les prisons.", montre: ["bilan"], cache: ["lent"], accent: ["bilan"] },
      { date: "Depuis 2011", titre: "Une justice discutée", texte: "Les organisations de défense des droits humains saluent l'ampleur du travail mais critiquent l'absence d'avocats, les pressions sur les témoins et l'exclusion des crimes du FPR.", montre: ["crit"], accent: ["crit"] }
    ],
    source: "Sources : loi organique rwandaise du 26 janvier 2001 ; bilan officiel présenté à la clôture des gacaca (juin 2012) ; Human Rights Watch, « Justice compromise » (2011). Schéma, effectifs non à l'échelle."
  };
})();

/* Animation sur carte : la justice pénale internationale s'installe (scène générée par cartes-t3.js) */
ANIMS.t3tribunaux = {
  titre: "De Nuremberg à Dakar : les tribunaux des crimes de masse",
  scene: "carte:t3tribunaux",
  etapes: [
    { date: "1945-1946", titre: "Nuremberg", texte: "Les vainqueurs jugent les dirigeants nazis : 22 accusés, 12 condamnations à mort. Le crime contre l'humanité entre dans l'histoire judiciaire.", montre: ["nur"], accent: ["nur"] },
    { date: "1946-1948", titre: "Tokyo", texte: "Un tribunal militaire international juge 28 dirigeants japonais. Puis la guerre froide bloque toute nouvelle juridiction internationale pendant plus de quarante ans.", montre: ["tok"], accent: ["tok"] },
    { date: "1993", titre: "Le TPIY", texte: "Pendant la guerre de Bosnie, le Conseil de sécurité crée à La Haye le premier tribunal pénal international depuis 1945.", montre: ["tpiy"], accent: ["tpiy"] },
    { date: "Juillet 1995", titre: "Srebrenica", texte: "Environ 8 000 hommes et garçons bosniaques musulmans sont tués : le TPIY qualifiera ce crime de génocide.", montre: ["srebre"], accent: ["srebre"] },
    { date: "1994-2012", titre: "Rwanda : deux échelles", texte: "Le TPIR, à Arusha (1994-2015), juge les chefs ; les gacaca jugent près de deux millions d'affaires dans les collines (2002-2012).", montre: ["tpir", "gacaca"], accent: ["tpir", "gacaca"] },
    { date: "2002", titre: "Tribunaux mixtes et cour permanente", texte: "Le Tribunal spécial pour la Sierra Leone associe juges nationaux et internationaux ; la Cour pénale internationale entre en fonction à La Haye le 1er juillet.", montre: ["tssl", "cpi"], accent: ["cpi"] },
    { date: "2006-2016", titre: "Juger au plus près des victimes", texte: "Au Cambodge, les crimes des Khmers rouges sont jugés à Phnom Penh ; à Dakar, l'Afrique juge un ancien chef d'État africain, Hissène Habré (2016).", montre: ["cetc", "cae"], accent: ["cetc", "cae"] }
  ],
  source: "Fond Natural Earth (pays actuels). Dates : actes fondateurs et jugements des juridictions citées."
};

/* Animation sur carte : l'engrenage de l'été 1914 et ses lectures (scène générée par cartes-t3.js) */
ANIMS.t3juillet = {
  titre: "Été 1914 : l'engrenage, et la question de la responsabilité",
  scene: "carte:t3juillet",
  etapes: [
    { date: "28 juin 1914", titre: "L'attentat de Sarajevo", texte: "Gavrilo Princip, jeune nationaliste bosno-serbe, assassine l'héritier du trône d'Autriche-Hongrie. Vienne accuse la Serbie.", montre: ["sar"], accent: ["sar"] },
    { date: "5-6 juillet", titre: "Le « chèque en blanc »", texte: "Berlin assure Vienne de son soutien, quelles que soient les suites : c'est l'un des points clés du débat sur la responsabilité allemande.", montre: ["cheque"], accent: ["cheque"] },
    { date: "23-28 juillet", titre: "L'ultimatum puis la guerre", texte: "L'Autriche-Hongrie adresse à la Serbie un ultimatum conçu pour être refusé, puis lui déclare la guerre le 28 juillet.", montre: ["ultim", "g-serbie"], accent: ["g-serbie"] },
    { date: "30 juillet", titre: "La Russie mobilise", texte: "Protectrice de la Serbie, la Russie décrète la mobilisation générale : pour l'état-major allemand, la guerre devient inévitable.", montre: ["mob-ru"], accent: ["mob-ru"] },
    { date: "1er-3 août", titre: "L'Allemagne déclare la guerre", texte: "Le plan allemand prévoit d'écraser la France avant de se tourner vers la Russie : déclarations de guerre à la Russie (1er août) puis à la France (3 août).", montre: ["g-russie", "g-france"], accent: ["g-france"] },
    { date: "4 août", titre: "La guerre devient européenne", texte: "Les troupes allemandes envahissent la Belgique neutre ; le Royaume-Uni, garant de sa neutralité, entre en guerre.", montre: ["belgique", "g-ru"], accent: ["g-ru"] },
    { date: "1961", titre: "Lecture 1 : Fischer", texte: "Pour Fritz Fischer, les dirigeants allemands ont voulu la guerre ou accepté sciemment son risque pour dominer l'Europe : la responsabilité principale est à Berlin.", montre: ["fischer"], accent: ["fischer"] },
    { date: "2012", titre: "Lecture 2 : Clark", texte: "Pour Christopher Clark, aucune capitale n'a voulu une guerre générale ; toutes ont pris des risques en croyant contrôler la crise. Le débat reste ouvert.", montre: ["clark"], cache: ["fischer"], accent: ["clark"] }
  ],
  source: "Fond Natural Earth (frontières actuelles, pas celles de 1914). Dates : chronologie diplomatique de juillet-août 1914."
};

/* ======================= THÈME 3 — OBJET DE TRAVAIL CONCLUSIF ======================= */
CHAPS["t3-otc"] = { th: "t3", code: "T3 · OBJET CONCLUSIF", t: "L'histoire et les mémoires du génocide des Juifs et des Tsiganes",
  ess: [
    "Le régime nazi et ses complices ont assassiné près de six millions de Juifs et, selon les estimations, entre 200 000 et 500 000 Tsiganes (Roms et Sinti) : deux génocides, de mémoire très inégale.",
    "Des lieux de mémoire se construisent par étapes : musée d'Auschwitz (1947), Yad Vashem (1953), Mémorial de la Shoah (Paris, 2005), mémoriaux de Berlin (2005 pour les Juifs, 2012 pour les Sinti et les Roms), reconnaissance de l'internement des Tsiganes en France (2016).",
    "Après Nuremberg, la justice continue : procès Eichmann (1961), Francfort (1963-1965), Barbie (1987), Touvier (1994), Papon (1998), jusqu'aux derniers gardiens jugés en Allemagne dans les années 2010-2020.",
    "Littérature et cinéma transmettent et interrogent : Levi, Antelme, Wiesel, Delbo, Spiegelman ; <em>Nuit et brouillard</em> (1956), <em>Shoah</em> (1985), <em>La Liste de Schindler</em> (1993), <em>Le Fils de Saul</em> (2015).",
    "Ce cas illustre tout le thème : histoire et mémoire s'éclairent, la justice produit faits et reconnaissance, et la mémoire des Tsiganes montre la concurrence et le retard de certaines mémoires."
  ],
  att: [
    "Connaître les grands lieux de mémoire du génocide des Juifs et des Tsiganes et la chronologie de leur création.",
    "Montrer comment on a jugé les crimes nazis après Nuremberg, en Israël, en Allemagne et en France.",
    "Analyser comment la littérature et le cinéma ont représenté le génocide, et les débats qu'ils ont suscités.",
    "Comprendre pourquoi la mémoire du génocide des Tsiganes a été plus tardive."
  ],
  secs: [
    { t: "Un double génocide, une mémoire inégale", idees: [
      { t: "Le génocide des Juifs", h: "Après les persécutions (lois de Nuremberg, 1935), les massacres par balles des <em>Einsatzgruppen</em> commencent en URSS en 1941 ; la conférence de Wannsee (20 janvier 1942) organise la déportation de tous les Juifs d'Europe vers les centres de mise à mort (Chelmno, Belzec, Sobibor, Treblinka, Auschwitz-Birkenau, Majdanek). On parle de <b>Shoah</b> (« catastrophe » en hébreu) ou d'Holocauste.", ex: "Près de six millions de Juifs sont assassinés. À Babi Yar, près de Kiev, 33 771 Juifs sont tués par balles les 29 et 30 septembre 1941. De France, environ 76 000 Juifs sont déportés ; environ 3 % reviennent." },
      { t: "Le génocide des Tsiganes", h: "Les nazis persécutent les Roms et les Sinti comme une « race » : fichage, stérilisations, internement, puis massacres et déportation. Les Roms parlent de <b>Samudaripen</b> (« meurtre total ») ou de Porajmos.", ex: "Le décret de Himmler du 16 décembre 1942 ordonne leur déportation à Auschwitz ; dans la nuit du 2 au 3 août 1944, les derniers internés du « camp des familles tsiganes » de Birkenau sont assassinés. Les estimations du nombre total de victimes vont de 200 000 à 500 000." },
      { t: "Une mémoire longtemps occultée", h: "Après 1945, les Tsiganes, peu organisés, souvent encore discriminés, peinent à faire reconnaître leur persécution. En Allemagne fédérale, la justice estime d'abord qu'ils ont été visés pour leur « asocialité », pas pour des motifs raciaux. En France, des « nomades » restent internés jusqu'en 1946.", ex: "Le chancelier Helmut Schmidt reconnaît le génocide des Sinti et des Roms le 17 mars 1982. Le Parlement européen fait du 2 août la journée européenne de commémoration de ce génocide (résolution du 15 avril 2015)." }
    ] },
    { t: "Lieux de mémoire du génocide des Juifs et des Tsiganes", idees: [
      { t: "Les camps, devenus musées et sites patrimoniaux", h: "Les lieux du crime deviennent des lieux de mémoire, de recueillement et d'enseignement. Leur conservation pose des questions : que garder, comment montrer sans mettre en scène, comment accueillir des millions de visiteurs ?", ex: "Le Musée d'État d'Auschwitz-Birkenau est créé par une loi polonaise du 2 juillet 1947 ; le site est inscrit au patrimoine mondial en 1979 et renommé en 2007 « Auschwitz Birkenau, camp allemand nazi de concentration et d'extermination (1940-1945) », à la demande de la Pologne. Environ 1,1 million de personnes y ont été assassinées, dont environ un million de Juifs." },
      { t: "Yad Vashem, mémorial d'Israël", h: "En Israël, la mémoire de la Shoah fonde en partie l'identité nationale. Yad Vashem documente les victimes, recueille témoignages et archives et honore les <b>Justes parmi les nations</b>, non-Juifs qui ont sauvé des Juifs au péril de leur vie.", ex: "Créé par une loi du 19 août 1953. Plus de 4 000 Justes ont été reconnus en France." },
      { t: "En France, la reconnaissance tardive de Vichy", h: "Après 1945, la mémoire de la déportation est dominée par celle des résistants déportés. La spécificité du génocide et la responsabilité de l'État français sont reconnues tardivement.", ex: "Le Centre de documentation juive contemporaine, fondé clandestinement à Grenoble le 28 avril 1943, est à l'origine du Mémorial du martyr juif inconnu (1956) devenu Mémorial de la Shoah le 27 janvier 2005, avec le mur des Noms des 76 000 déportés. Journée nationale du 16 juillet (décret de 1993, loi de 2000) ; Maison d'Izieu (1994) ; mémorial de Drancy (2012)." },
      { t: "En Allemagne, des mémoriaux au cœur de la capitale", h: "L'Allemagne fait de la mémoire de ses crimes un élément de son identité démocratique : mémoriaux nationaux à Berlin, enseignement, poursuites judiciaires. Des initiatives citoyennes inscrivent la mémoire dans les rues.", ex: "Mémorial aux Juifs assassinés d'Europe (2 711 stèles, inauguré le 10 mai 2005) ; mémorial aux Sinti et Roms d'Europe assassinés (24 octobre 2012). Les « pierres d'achoppement » (<em>Stolpersteine</em>) de l'artiste Gunter Demnig, posées devant le dernier domicile des victimes, dépassent les 100 000 en 2023." },
      { t: "Les lieux de la mémoire tsigane en France", h: "La mémoire de l'internement des « nomades » (1940-1946) émerge grâce aux associations et aux historiens. Plusieurs milliers de personnes ont été internées dans une trentaine de camps.", ex: "Le 29 octobre 2016, au camp de Montreuil-Bellay (Maine-et-Loire), François Hollande reconnaît « la souffrance des nomades » internés et « la responsabilité » de la République." },
      { t: "Une mémoire devenue internationale", h: "La mémoire de la Shoah devient une référence universelle de l'horreur et un fondement des droits humains, au risque de la banalisation ou de la concurrence avec d'autres mémoires.", ex: "Le 1er novembre 2005, l'Assemblée générale de l'ONU fait du 27 janvier, date de la libération d'Auschwitz en 1945, la Journée internationale dédiée à la mémoire des victimes de l'Holocauste." }
    ], viz: ["anim:t3lieux", "carte:memoire"] },
    { t: "Juger les crimes nazis après Nuremberg", idees: [
      { t: "Nuremberg et ses suites", h: "Le procès des grands criminels de guerre (1945-1946) est suivi de douze procès américains à Nuremberg (médecins, juristes, <em>Einsatzgruppen</em>, industriels…), de procès dans les zones d'occupation et dans les pays occupés. Mais la guerre froide pousse vite à l'amnistie et à la réintégration.", ex: "Au « procès des médecins » (décembre 1946-août 1947), sept accusés sont condamnés à mort ; le jugement énonce le « code de Nuremberg » sur le consentement aux expériences médicales." },
      { t: "Le procès Eichmann (1961)", h: "Enlevé en Argentine par le Mossad en mai 1960, Adolf Eichmann, organisateur des déportations, est jugé à Jérusalem. Le procès, filmé et diffusé dans le monde, met au centre les rescapés et le génocide des Juifs en tant que tel.", ex: "Ouvert le 11 avril 1961, il s'achève par une condamnation à mort (15 décembre 1961) exécutée en 1962. La philosophe Hannah Arendt y voit la « banalité du mal » (<em>Eichmann à Jérusalem</em>, 1963) : un bureaucrate ordinaire, pas un monstre." },
      { t: "L'Allemagne juge ses criminels", h: "Dans les années 1960, la justice ouest-allemande, poussée par le procureur Fritz Bauer, juge elle-même des responsables d'Auschwitz : la société allemande découvre le fonctionnement concret du camp.", ex: "Procès d'Auschwitz à Francfort (20 décembre 1963-août 1965) : 22 accusés. En 1979, le Bundestag rend le meurtre imprescriptible, ce qui permet des procès tardifs : John Demjanjuk (Munich, 2011, gardien à Sobibor), Oskar Gröning (Lüneburg, 2015), Irmgard Furchner (Itzehoe, 2022), secrétaire du camp du Stutthof." },
      { t: "En France : Barbie, Touvier, Papon", h: "Grâce à l'imprescriptibilité (1964) et au combat de Serge et Beate Klarsfeld, la France juge des criminels nazis et des Français complices, et regarde en face Vichy.", ex: "Klaus Barbie, chef de la Gestapo de Lyon, est condamné à perpétuité le 4 juillet 1987 (rafle d'Izieu, dernier convoi de Lyon) ; Paul Touvier, ancien chef du renseignement de la Milice lyonnaise, le 20 avril 1994 (exécution de sept otages juifs à Rillieux-la-Pape) ; Maurice Papon, haut fonctionnaire de Vichy à Bordeaux, à dix ans de réclusion le 2 avril 1998 pour complicité de crimes contre l'humanité." },
      { t: "Ce que les procès apportent à l'histoire et à la mémoire", h: "Les procès établissent des faits, produisent des archives, donnent la parole aux victimes et réveillent la mémoire. Mais un procès n'est pas un cours d'histoire : il juge un individu, selon des règles de preuve, et ne peut tout dire d'une époque.", ex: "Le procès Papon a été filmé pour l'histoire, comme celui de Barbie (loi Badinter du 11 juillet 1985 sur l'enregistrement des procès historiques). Des historiens cités comme témoins, tel Henry Rousso, ont refusé de témoigner, estimant que leur rôle n'était pas d'aider à juger." }
    ] },
    { t: "Le génocide dans la littérature et le cinéma", idees: [
      { t: "Témoigner : la littérature des rescapés", h: "Les premiers récits naissent du besoin de témoigner, souvent dans l'indifférence. Ils deviennent des classiques à partir des années 1960, avec l'« ère du témoin ».", ex: "Primo Levi, <em>Si c'est un homme</em> (1947, peu lu avant sa réédition de 1958) ; Robert Antelme, <em>L'Espèce humaine</em> (1947) ; Elie Wiesel, <em>La Nuit</em> (1958 ; prix Nobel de la paix en 1986) ; Charlotte Delbo, <em>Aucun de nous ne reviendra</em> (écrit en 1946, publié en 1965) ; le <em>Journal</em> d'Anne Frank (1947)." },
      { t: "Dire l'indicible : les choix de forme", h: "Comment raconter l'extermination ? Les auteurs inventent des formes : roman d'un adolescent qui ne comprend pas, bande dessinée animalière, roman écrit du point de vue d'un bourreau, ce qui suscite débats et polémiques.", ex: "Imre Kertész, <em>Être sans destin</em> (1975 ; prix Nobel de littérature 2002) ; Art Spiegelman, <em>Maus</em> (1980-1991 ; prix Pulitzer spécial en 1992), où les Juifs sont des souris et les nazis des chats ; Jonathan Littell, <em>Les Bienveillantes</em> (prix Goncourt 2006)." },
      { t: "Le cinéma, de l'archive au témoignage", h: "Le cinéma montre d'abord les images de la libération des camps, puis choisit d'autres voies : la parole des témoins, la fiction grand public, ou le hors-champ, pour éviter de reconstituer l'horreur.", ex: "<em>Nuit et brouillard</em> d'Alain Resnais (1956) : la censure fait masquer le képi d'un gendarme français sur une photo du camp de Pithiviers. <em>Shoah</em> de Claude Lanzmann (1985), plus de neuf heures, sans aucune image d'archive, seulement des témoins et des lieux. La série américaine <em>Holocauste</em> (1978) bouleverse l'Allemagne fédérale lors de sa diffusion en janvier 1979." },
      { t: "Peut-on représenter la Shoah ? Un débat", h: "Lanzmann juge qu'aucune reconstitution n'est possible ; d'autres défendent la fiction comme moyen de toucher le grand public. Le débat porte aussi sur les rares images prises dans les camps.", ex: "Lanzmann critique <em>La Liste de Schindler</em> de Steven Spielberg (1993), qui fonde ensuite la Shoah Foundation (plus de 50 000 témoignages filmés). <em>Le Fils de Saul</em> de László Nemes (2015) et <em>La Zone d'intérêt</em> de Jonathan Glazer (2023) montrent le crime par le son et le hors-champ. Georges Didi-Huberman (<em>Images malgré tout</em>, 2003) étudie les quatre photographies prises clandestinement par un membre du Sonderkommando de Birkenau en août 1944." },
      { t: "Et les Tsiganes ?", h: "Le génocide des Tsiganes est beaucoup moins présent dans les œuvres, ce qui reflète et entretient le retard de sa mémoire.", ex: "Le film <em>Liberté</em> de Tony Gatlif (2010) raconte l'internement d'une famille de nomades en France sous l'Occupation." }
    ] }
  ],
  pieges: [
    "Parler de « camps de concentration » pour tous les camps : distingue camps de concentration et centres de mise à mort (Treblinka, Sobibor, Belzec, Chelmno), Auschwitz et Majdanek étant les deux à la fois.",
    "Oublier les Tsiganes : le jalon parle du génocide des Juifs <b>et</b> des Tsiganes.",
    "Croire que la mémoire de la Shoah a été immédiate : elle s'impose surtout à partir des années 1960-1970 (Eichmann, Paxton, <em>Holocauste</em>).",
    "Confondre Barbie (Allemand, nazi), Touvier (milicien français) et Papon (haut fonctionnaire de Vichy).",
    "Présenter les œuvres sans les dater ni dire ce qu'elles apportent (témoignage, forme, débat)."
  ],
  retenir: [
    ["Bilan", "Près de 6 millions de Juifs ; 200 000 à 500 000 Tsiganes (estimations) ; environ 76 000 Juifs déportés de France."],
    ["Lieux", "Auschwitz : musée 1947, patrimoine mondial 1979 ; Yad Vashem 1953 ; CDJC 1943, Mémorial de la Shoah 2005 ; Izieu 1994 ; Berlin 2005 et 2012 ; Montreuil-Bellay 2016."],
    ["Mémoire tsigane", "Reconnaissance allemande 17 mars 1982 ; 2 août (Parlement européen, 2015) ; Hollande, 29 oct. 2016."],
    ["Procès", "Eichmann 1961 (Arendt, « banalité du mal ») ; Francfort 1963-1965 ; Barbie 1987 ; Touvier 1994 ; Papon 1998 ; Demjanjuk 2011, Gröning 2015."],
    ["Œuvres", "Levi 1947 ; Antelme 1947 ; Wiesel 1958 ; Kertész 1975 ; <em>Maus</em> 1980-1991 ; <em>Nuit et brouillard</em> 1956 ; <em>Shoah</em> 1985 ; <em>Schindler</em> 1993 ; <em>Le Fils de Saul</em> 2015 ; <em>La Zone d'intérêt</em> 2023."],
    ["27 janvier", "Libération d'Auschwitz (1945) ; journée internationale (ONU, 2005)."]
  ],
  qcm: [
    { q: "Que signifie « Shoah » ?", o: ["Extermination en allemand", "Catastrophe en hébreu", "Mémoire en yiddish", "Holocauste en grec"], r: 1, e: "Le mot s'impose en France avec le film de Lanzmann (1985).", ref: "1-1" },
    { q: "Quel terme désigne le génocide des Roms ?", o: ["Samudaripen", "Holodomor", "Nakba", "Pogrom"], r: 0, e: "« Meurtre total » en romani ; on dit aussi Porajmos.", ref: "1-2" },
    { q: "Quand l'Allemagne reconnaît-elle le génocide des Sinti et des Roms ?", o: ["1945", "1961", "17 mars 1982", "2012"], r: 2, e: "Par la voix du chancelier Helmut Schmidt.", ref: "1-3" },
    { q: "Quand le site d'Auschwitz-Birkenau est-il inscrit au patrimoine mondial ?", o: ["1947", "1979", "2005", "2007"], r: 1, e: "1979 ; le musée existe depuis 1947 ; le nom est précisé en 2007.", ref: "2-1" },
    { q: "Qui sont les « Justes parmi les nations » ?", o: ["Les juges de Nuremberg", "Des non-Juifs ayant sauvé des Juifs au péril de leur vie", "Les rescapés", "Les historiens de Yad Vashem"], r: 1, e: "Le titre est décerné par Yad Vashem (créé en 1953).", ref: "2-2" },
    { q: "Quand le Mémorial de la Shoah de Paris est-il inauguré sous ce nom ?", o: ["1943", "1956", "27 janvier 2005", "2012"], r: 2, e: "Il prolonge le CDJC (1943) et le Mémorial du martyr juif inconnu (1956).", ref: "2-3" },
    { q: "Que reconnaît François Hollande à Montreuil-Bellay le 29 octobre 2016 ?", o: ["La rafle du Vél d'Hiv", "La responsabilité de la République dans l'internement des nomades", "Le génocide arménien", "La torture en Algérie"], r: 1, e: "Montreuil-Bellay fut le plus grand camp d'internement des nomades en France.", ref: "2-5" },
    { q: "Pourquoi le 27 janvier a-t-il été choisi par l'ONU ?", o: ["Date de Wannsee", "Date de la libération d'Auschwitz en 1945", "Date de Nuremberg", "Date du procès Eichmann"], r: 1, e: "Résolution du 1er novembre 2005.", ref: "2-6" },
    { q: "Quelle expression Hannah Arendt emploie-t-elle à propos d'Eichmann ?", o: ["Le mal radical", "La banalité du mal", "Le crime sans nom", "L'ère du témoin"], r: 1, e: "<em>Eichmann à Jérusalem</em> (1963).", ref: "3-2" },
    { q: "Qui pousse l'Allemagne fédérale à juger elle-même des responsables d'Auschwitz (1963-1965) ?", o: ["Serge Klarsfeld", "Le procureur Fritz Bauer", "Konrad Adenauer", "Simon Wiesenthal"], r: 1, e: "Procès d'Auschwitz à Francfort.", ref: "3-3" },
    { q: "Qui est Paul Touvier ?", o: ["Un chef de la Gestapo", "Un ancien chef du renseignement de la Milice lyonnaise", "Un préfet de Vichy", "Un procureur"], r: 1, e: "Premier Français condamné pour crime contre l'humanité (20 avril 1994).", ref: "3-4" },
    { q: "Pour quel crime Maurice Papon est-il condamné en 1998 ?", o: ["Crime de guerre", "Complicité de crimes contre l'humanité", "Génocide", "Haute trahison"], r: 1, e: "Dix ans de réclusion, pour la déportation de Juifs de la Gironde.", ref: "3-4" },
    { q: "Quel film est fait uniquement de témoignages et de lieux, sans images d'archive ?", o: ["<em>Nuit et brouillard</em>", "<em>Shoah</em>", "<em>La Liste de Schindler</em>", "<em>Le Pianiste</em>"], r: 1, e: "Claude Lanzmann, 1985, plus de neuf heures.", ref: "4-3" },
    { q: "Dans <em>Maus</em>, comment Art Spiegelman représente-t-il les Juifs ?", o: ["En oiseaux", "En souris", "En chiens", "En humains"], r: 1, e: "Les nazis sont des chats : une forme qui a fait débat, couronnée par un prix Pulitzer spécial en 1992.", ref: "4-2" }
  ],
  fc: [
    ["Wannsee", "Conférence du 20 janvier 1942 qui organise la déportation des Juifs d'Europe vers les centres de mise à mort."],
    ["Centre de mise à mort", "Lieu conçu pour tuer dès l'arrivée : Chelmno, Belzec, Sobibor, Treblinka (Auschwitz-Birkenau et Majdanek étaient aussi des camps de concentration)."],
    ["Samudaripen", "« Meurtre total » : nom romani du génocide des Tsiganes."],
    ["2 août", "Journée européenne du génocide des Roms (nuit du 2 au 3 août 1944 à Birkenau)."],
    ["Yad Vashem", "Mémorial israélien de la Shoah (loi du 19 août 1953) ; honore les Justes."],
    ["Mur des Noms", "Mémorial de la Shoah (Paris, 2005) : noms des 76 000 Juifs déportés de France."],
    ["Stolpersteine", "« Pierres d'achoppement » de Gunter Demnig devant les domiciles des victimes."],
    ["Procès Eichmann", "Jérusalem, 1961 : le génocide raconté par les témoins."],
    ["Procès Barbie", "Lyon, 1987 : premier procès pour crime contre l'humanité en France."],
    ["Procès Papon", "Bordeaux, 1997-1998 : un haut fonctionnaire de Vichy condamné pour complicité de crimes contre l'humanité."],
    ["<em>Shoah</em>", "Film de Claude Lanzmann (1985) fondé sur les témoignages, sans images d'archive."],
    ["<em>Si c'est un homme</em>", "Témoignage de Primo Levi sur Auschwitz (1947)."]
  ],
  bac: { s: "Les lieux de mémoire du génocide des Juifs et des Tsiganes depuis 1945", type: "Sujet de dissertation inventé pour le site (thème 3, objet de travail conclusif)", h: "<p><b>Problématique possible :</b> comment les lieux de mémoire du génocide des Juifs et des Tsiganes se sont-ils construits, et que révèlent-ils des inégalités et des usages de la mémoire ?</p><p><b>I. Des lieux du crime aux lieux de mémoire (1945-années 1960).</b> Musée d'Auschwitz (1947) ; Yad Vashem (1953) ; Mémorial du martyr juif inconnu (1956) ; une mémoire dominée par la déportation résistante.</p><p><b>II. L'affirmation d'une mémoire spécifique de la Shoah (années 1970-2000).</b> Patrimoine mondial (1979) ; Vél d'Hiv (1993, 1995) ; Izieu (1994) ; Mémorial de la Shoah et Berlin (2005) ; 27 janvier (ONU, 2005).</p><p><b>III. La reconnaissance tardive des Tsiganes et l'internationalisation de la mémoire.</b> Allemagne (1982) ; mémorial de Berlin (2012) ; 2 août (2015) ; Montreuil-Bellay (2016) ; <em>Stolpersteine</em> ; risques de concurrence et de banalisation.</p>" }
};

/* Animation sur carte : des centres de mise à mort aux lieux de mémoire (scène générée par cartes-t3.js) */
ANIMS.t3lieux = {
  titre: "Du lieu du crime au lieu de mémoire : la carte d'une mémoire qui se construit",
  scene: "carte:t3lieux",
  etapes: [
    { date: "1941-1944", titre: "Les centres de mise à mort", texte: "En Pologne occupée, les nazis installent six centres où les Juifs déportés de toute l'Europe sont assassinés, surtout dans des chambres à gaz.", montre: ["centres"], accent: ["centres"] },
    { date: "1941-1944", titre: "Depuis la France", texte: "Environ 76 000 Juifs sont déportés de France, la plupart via Drancy vers Auschwitz. Des milliers de « nomades » sont internés dans des camps français, dont Montreuil-Bellay.", montre: ["depor"], accent: ["depor"] },
    { date: "1947", titre: "Auschwitz devient un musée", texte: "La Pologne crée un musée d'État sur le site. Le récit officiel communiste insiste alors sur les victimes polonaises plus que sur les Juifs.", montre: ["m1947"], accent: ["m1947"] },
    { date: "1953", titre: "Yad Vashem", texte: "Israël crée son mémorial national : documenter chaque victime, recueillir les témoignages, honorer les Justes.", montre: ["m1953"], accent: ["m1953"] },
    { date: "1956-1994", titre: "La France se souvient", texte: "Mémorial du martyr juif inconnu à Paris (1956), puis Maison d'Izieu (1994), après le procès Barbie et la reconnaissance de la rafle du Vél d'Hiv.", montre: ["m1956", "m1994"], accent: ["m1956", "m1994"] },
    { date: "2005", titre: "Deux grands mémoriaux", texte: "Mémorial de la Shoah à Paris (27 janvier) et mémorial aux Juifs assassinés d'Europe à Berlin (10 mai) : la mémoire s'installe au cœur des capitales.", montre: ["m2005"], accent: ["m2005", "m1956"] },
    { date: "2012", titre: "Les Tsiganes enfin au cœur de Berlin", texte: "Un mémorial aux Sinti et Roms assassinés est inauguré près du Reichstag ; en France, le mémorial de Drancy ouvre ses portes.", montre: ["m2012"], accent: ["m2012"] },
    { date: "2016", titre: "La reconnaissance de l'internement des nomades", texte: "À Montreuil-Bellay, le président de la République reconnaît la responsabilité de la France : la dernière mémoire à émerger est la plus longtemps oubliée.", montre: ["m2016"], accent: ["m2016"] }
  ],
  source: "Fond Natural Earth (pays actuels). Dates de création des musées et mémoriaux cités."
};

/* ======================= THÈME 3 — DOSSIER ======================= */
DOSSIERS.t3 = {
  cats: { conflits: ["Conflits et crimes de masse", "#B3241B"], justice: ["Justice", "#2D5675"], memoire: ["Mémoires, lois, historiens", "#B07A1E"] },
  frise: [
    ["1914", "28 juin 1914", "conflits", "Attentat de Sarajevo", "Début de la crise qui mène à la Première Guerre mondiale (guerre générale le 4 août)."],
    ["1915", "24 mai 1915", "justice", "« Crimes contre l'humanité »", "Déclaration alliée sur les massacres des Arméniens (1,2 à 1,5 million de morts)."],
    ["1919", "28 juin 1919", "memoire", "Traité de Versailles, art. 231", "Responsabilité de l'Allemagne et de ses alliés : début du débat sur les causes de la guerre."],
    ["1925", "1925", "memoire", "Halbwachs et Renouvin", "<em>Les Cadres sociaux de la mémoire</em> ; <em>Les Origines immédiates de la guerre</em>."],
    ["1942", "20 janv. 1942", "conflits", "Conférence de Wannsee", "Organisation de la déportation des Juifs d'Europe vers les centres de mise à mort."],
    ["1944", "1944", "justice", "Lemkin invente « génocide »", "Dans <em>Axis Rule in Occupied Europe</em>."],
    ["1945", "8 août 1945", "justice", "Statut de Nuremberg", "Définit le crime contre l'humanité (art. 6 c)."],
    ["1946", "1er oct. 1946", "justice", "Verdict de Nuremberg", "12 condamnations à mort, 3 acquittements."],
    ["1948", "9 déc. 1948", "justice", "Convention sur le génocide", "Adoptée par l'Assemblée générale de l'ONU."],
    ["1954", "1er nov. 1954", "conflits", "Toussaint rouge", "Début de la guerre d'Algérie (indépendance le 5 juillet 1962)."],
    ["1961", "11 avril 1961", "justice", "Procès Eichmann", "Jérusalem : les rescapés témoignent ; « l'ère du témoin »."],
    ["1961", "Oct. 1961", "memoire", "Thèse de Fritz Fischer", "Les buts de guerre de l'Allemagne impériale : controverse en RFA."],
    ["1964", "26 déc. 1964", "justice", "Imprescriptibilité", "Les crimes contre l'humanité deviennent imprescriptibles en France."],
    ["1982", "17 mars 1982", "memoire", "Génocide des Sinti et Roms reconnu", "Par le chancelier ouest-allemand Helmut Schmidt."],
    ["1987", "4 juill. 1987", "justice", "Procès Barbie", "Premier procès pour crime contre l'humanité en France."],
    ["1990", "13 juill. 1990", "memoire", "Loi Gayssot", "Punit la contestation des crimes contre l'humanité."],
    ["1993", "25 mai 1993", "justice", "Création du TPIY", "Résolution 827 du Conseil de sécurité ; siège à La Haye."],
    ["1994", "7 avril 1994", "conflits", "Génocide des Tutsis", "Environ 800 000 morts en une centaine de jours (ONU)."],
    ["1994", "8 nov. 1994", "justice", "Création du TPIR", "Résolution 955 ; siège à Arusha."],
    ["1995", "Juillet 1995", "conflits", "Srebrenica", "Environ 8 000 Bosniaques musulmans tués : génocide selon le TPIY et la CIJ."],
    ["1995", "16 juill. 1995", "memoire", "Discours du Vél d'Hiv", "Chirac reconnaît la responsabilité de l'État français."],
    ["1998", "2 sept. 1998", "justice", "Jugement Akayesu", "Première condamnation pour génocide par une juridiction internationale."],
    ["1998", "17 juill. 1998", "justice", "Statut de Rome", "Crée la CPI (en fonction le 1er juillet 2002)."],
    ["1999", "18 oct. 1999", "memoire", "« Guerre d'Algérie »", "La loi reconnaît officiellement la guerre."],
    ["2001", "26 janv. 2001", "justice", "Loi sur les gacaca", "Juridictions populaires pour juger le génocide des Tutsis."],
    ["2005", "27 janv. 2005", "memoire", "Mémorial de la Shoah", "Paris ; le 10 mai, mémorial aux Juifs assassinés d'Europe à Berlin."],
    ["2005", "12 déc. 2005", "memoire", "« Liberté pour l'histoire »", "Appel de 19 historiens contre les lois mémorielles."],
    ["2012", "18 juin 2012", "justice", "Clôture des gacaca", "1 958 634 affaires traitées selon le bilan officiel."],
    ["2012", "Sept. 2012", "memoire", "Christopher Clark, <em>The Sleepwalkers</em>", "Les « somnambules » de 1914, au moment du centenaire."],
    ["2016", "29 oct. 2016", "memoire", "Montreuil-Bellay", "La France reconnaît sa responsabilité dans l'internement des nomades."],
    ["2017", "22 nov. 2017", "justice", "Condamnation de Mladić", "Perpétuité ; le TPIY ferme le 31 décembre 2017."],
    ["2021", "20 janv. 2021", "memoire", "Rapport Stora", "22 recommandations sur les mémoires de la colonisation et de la guerre d'Algérie."],
    ["2024", "23 mai 2024", "memoire", "Journée de Srebrenica", "L'ONU fait du 11 juillet une journée de commémoration du génocide."],
    ["2025", "24 déc. 2025", "memoire", "Loi algérienne", "Le Parlement algérien criminalise la colonisation française."]
  ],
  notions: [
    ["Histoire", "Connaissance critique du passé, fondée sur des sources confrontées, qui cherche à expliquer sans juger."],
    ["Mémoire", "Rapport vécu, affectif et sélectif d'un individu ou d'un groupe à son passé ; elle construit une identité."],
    ["Mémoire collective", "Mémoire partagée par un groupe, inscrite dans des cadres sociaux (Halbwachs)."],
    ["Lieu de mémoire", "Lieu, objet, rite, date ou symbole où la mémoire d'un groupe se cristallise (Nora)."],
    ["Devoir de mémoire / travail de mémoire", "Obligation morale de se souvenir ; démarche critique qui cherche à comprendre (« juste mémoire » de Ricœur)."],
    ["Concurrence des mémoires", "Rivalité entre groupes porteurs de mémoire pour la reconnaissance publique de leurs souffrances."],
    ["Loi mémorielle", "Loi qui qualifie un fait historique ou punit sa négation."],
    ["Négationnisme", "Négation d'un crime contre l'humanité ou d'un génocide (chambres à gaz, génocide des Tutsis…)."],
    ["Crime de guerre", "Violation grave des lois et coutumes de la guerre (meurtre de prisonniers, attaques contre des civils, pillage)."],
    ["Crime contre l'humanité", "Actes inhumains (meurtre, extermination, déportation, persécution) commis dans le cadre d'une attaque généralisée ou systématique contre une population civile."],
    ["Génocide", "Actes commis dans l'intention de détruire, en tout ou en partie, un groupe national, ethnique, racial ou religieux, comme tel."],
    ["Imprescriptibilité", "Possibilité de juger un crime sans limite de temps."],
    ["Justice transitionnelle", "Ensemble des moyens (procès, commissions de vérité, réparations, réformes) par lesquels une société sort d'un conflit ou d'une dictature."],
    ["Justice pénale internationale", "Juridictions qui jugent des individus pour les crimes les plus graves : tribunaux ad hoc (TPIY, TPIR), tribunaux mixtes, CPI."],
    ["Compétence universelle", "Possibilité pour un État de juger certains crimes internationaux, quel que soit le lieu où ils ont été commis."]
  ],
  acteurs: [
    ["Historiens", "Renouvin, Fischer, Clark, Krumeich (1914) ; Stora, Branche (Algérie) ; Paxton, Rousso, Wieviorka (Vichy, Shoah) ; commissions d'historiens (Duclert 2021, commission franco-algérienne 2022)."],
    ["Témoins et groupes porteurs de mémoire", "Rescapés (Levi, Wiesel), associations d'anciens combattants, de rapatriés, de harkis, de Roms ; Serge et Beate Klarsfeld."],
    ["États", "Commémorations, lois, reconnaissances (Vél d'Hiv 1995, Audin 2018) ; usage diplomatique de la mémoire (France-Algérie, Serbie)."],
    ["Juges", "Tribunaux nationaux (Barbie, Papon, Simbikangwa) ; gacaca ; tribunaux internationaux (Nuremberg, TPIY, TPIR) ; CPI."],
    ["Organisations internationales", "ONU (Conseil de sécurité, Assemblée générale, journées internationales) ; UNESCO (lieux de mémoire au patrimoine mondial) ; Parlement européen (2 août)."],
    ["Créateurs", "Écrivains (Levi, Delbo, Spiegelman), cinéastes (Resnais, Lanzmann, Spielberg, Nemes, Glazer)."]
  ],
  cartes: ["memoire", "justice"],
  debats: [
    { q: "Faut-il des lois mémorielles ?",
      pour: ["Elles reconnaissent publiquement la souffrance des victimes et de leurs descendants (génocide arménien, esclavage).", "La loi Gayssot permet de poursuivre les négationnistes, dont les discours servent l'antisémitisme.", "Elles poussent l'école à enseigner des pages occultées (loi Taubira)."],
      contre: ["Ce n'est pas au législateur d'écrire l'histoire ; seule la recherche peut établir et réviser les faits (« Liberté pour l'histoire », 2005).", "Elles nourrissent la concurrence des mémoires : chaque groupe réclame sa loi.", "Elles peuvent menacer la liberté d'expression et de recherche (censure du Conseil constitutionnel, 2012)."],
      bilan: "Le Parlement a choisi depuis 2008 de privilégier les résolutions et les commémorations plutôt que de nouvelles lois : reconnaître sans enfermer l'histoire." },
    { q: "La justice peut-elle réconcilier une société après un génocide ?",
      pour: ["Elle établit des faits incontestables et désigne des responsables individuels, ce qui évite la culpabilité collective (Srebrenica, Akayesu).", "Elle donne la parole aux victimes (gacaca, Eichmann) et produit des archives pour l'histoire.", "Au Rwanda, les gacaca ont permis de vider les prisons et de retrouver les corps des victimes."],
      contre: ["Elle peut être perçue comme une justice des vainqueurs (crimes du FPR exclus, TPIY jugé anti-serbe).", "Elle juge des individus, pas des sociétés : la négation de Srebrenica reste forte en Republika Srpska.", "La réconciliation suppose aussi des politiques de mémoire, d'éducation et de réparation."],
      bilan: "La justice est nécessaire mais pas suffisante : elle doit s'articuler avec le travail des historiens et des politiques de mémoire (justice transitionnelle)." },
    { q: "Les historiens doivent-ils intervenir dans les débats de mémoire ?",
      pour: ["Ils apportent des faits vérifiés contre les mythes (Paxton sur Vichy, Fischer sur 1914).", "Les États leur demandent des rapports (Stora 2021, Duclert 2021).", "Les commissions mixtes d'historiens peuvent apaiser les relations entre États (manuel franco-allemand)."],
      contre: ["Ils risquent d'être instrumentalisés par les pouvoirs.", "Témoigner à un procès n'est pas leur rôle (refus de Rousso au procès Papon).", "Le temps de l'histoire n'est pas celui de l'émotion ni de la politique."],
      bilan: "L'historien intervient comme expert de la méthode, pas comme juge ni comme porte-parole d'une mémoire." }
  ],
  dissert: {
    s: "Mémoire et justice face aux génocides et crimes de masse depuis 1945",
    src: "Sujet inventé pour le site (thème 3). Corrigé proposé par le site.",
    analyse: "Sujet à deux termes : il faut étudier le lien entre « mémoire » (comment les sociétés se souviennent) et « justice » (comment elles jugent). « Génocides et crimes de masse » : Shoah et génocide des Tsiganes, génocide des Tutsis, Srebrenica ; on peut évoquer d'autres crimes de masse. « Depuis 1945 » : de Nuremberg à aujourd'hui. Il ne s'agit pas de raconter les génocides mais d'analyser la façon dont on les juge et dont on s'en souvient.",
    pb: "En quoi la justice, en jugeant les génocides et les crimes de masse, contribue-t-elle à construire leur mémoire, et dans quelle mesure se heurte-t-elle aux limites et aux conflits de mémoire ?",
    intro: "Le 22 novembre 2017, à La Haye, Ratko Mladić, ancien chef militaire des Serbes de Bosnie, est condamné à la réclusion à perpétuité pour le génocide de Srebrenica, vingt-deux ans après les faits : quelques semaines plus tard, le tribunal qui l'a jugé ferme ses portes. Depuis 1945, les sociétés frappées par des crimes de masse ont cherché à les juger et à s'en souvenir. Un génocide est la destruction intentionnelle de tout ou partie d'un groupe national, ethnique, racial ou religieux (convention de 1948) ; les crimes de masse englobent aussi les crimes contre l'humanité. La justice désigne des responsables selon le droit ; la mémoire est le rapport vécu d'un groupe à son passé. Depuis Nuremberg, ces deux rapports au passé se croisent sans se confondre. En quoi la justice contribue-t-elle à construire la mémoire des génocides et des crimes de masse, et dans quelle mesure se heurte-t-elle à des limites ? Nous verrons d'abord que la justice nomme et établit les crimes, puis qu'elle s'adapte aux échelles et donne une place aux victimes, enfin qu'elle ne suffit pas à apaiser des mémoires toujours conflictuelles.",
    plan: [
      { t: "I. Juger pour nommer et établir les crimes", sous: [
        ["A. Nuremberg invente le crime contre l'humanité", "Statut du 8 août 1945 ; procès du 20 novembre 1945 au 1er octobre 1946 ; archives nazies utilisées comme preuves ; Lemkin (1944) et la convention du 9 décembre 1948."],
        ["B. Des procès qui fixent les faits pour l'histoire", "Eichmann (1961) : le génocide des Juifs comme tel ; Francfort (1963-1965) ; TPIY : Srebrenica qualifié de génocide (Krstić, 2001-2004 ; CIJ, 2007)."],
        ["C. L'imprescriptibilité, un temps long de la justice", "France, 26 décembre 1964 ; Barbie (1987), Touvier (1994), Papon (1998) ; derniers gardiens jugés en Allemagne (Demjanjuk 2011, Gröning 2015)."]
      ] },
      { t: "II. Une justice à plusieurs échelles, au service des victimes", sous: [
        ["A. L'échelle internationale", "TPIY (1993-2017, 161 accusés) ; TPIR (1994-2015, Akayesu 1998) ; CPI (2002) ; tribunaux mixtes (Sierra Leone, Cambodge, Dakar 2016)."],
        ["B. L'échelle locale : les gacaca", "Loi du 26 janvier 2001 ; aveux et peines réduites ; près de deux millions d'affaires ; la vérité sur chaque colline et les corps retrouvés."],
        ["C. Les procès, moments de mémoire", "« Ère du témoin » (Wieviorka) ; procès filmés (loi de 1985) ; mémoriaux associés (Gisozi, Potočari) ; Vél d'Hiv reconnu en 1995 après les procès."]
      ] },
      { t: "III. Les limites de la justice face aux mémoires", sous: [
        ["A. Justice des vainqueurs ?", "Nuremberg sans juger les crimes alliés ; crimes du FPR exclus des gacaca ; TPIY contesté en Serbie."],
        ["B. Des mémoires toujours divisées", "Praljak (2017) ; négation de Srebrenica ; résolution de l'ONU de 2024 ; mémoire tardive des Tsiganes (1982, 2016)."],
        ["C. Une justice internationale fragile", "Mandats de la CPI non exécutés (Poutine 2023) ; retraits annoncés (2025) ; d'où l'importance des politiques de mémoire et du travail des historiens (rapport Duclert, 2021)."]
      ] }
    ],
    concl: "Depuis 1945, la justice a joué un rôle décisif dans la mémoire des génocides et des crimes de masse : elle a nommé ces crimes, établi les faits, désigné des responsables et donné la parole aux victimes, à l'échelle internationale comme dans les collines rwandaises. Mais elle ne peut pas tout : elle juge des individus, elle est parfois perçue comme partiale, et elle ne fait pas disparaître les conflits de mémoire, comme le montrent la négation persistante de Srebrenica ou la reconnaissance tardive du génocide des Tsiganes. La reconstruction des sociétés suppose d'articuler justice, histoire et politiques de mémoire. Reste à savoir si la Cour pénale internationale, contestée par plusieurs puissances, pourra jouer ce rôle face aux crimes de masse d'aujourd'hui.",
    croquis: "Schéma possible (valorisé, non obligatoire) : trois cercles concentriques pour les échelles de la justice (locale : gacaca ; nationale : procès Barbie, Papon, Simbikangwa ; internationale : Nuremberg, TPIY, TPIR, CPI), reliés par des flèches à trois effets (établir les faits, reconnaître les victimes, construire la mémoire) et à trois limites (justice des vainqueurs, négation, souveraineté des États)."
  },
  etude: {
    titre: "Juger les crimes nazis : le procès de Nuremberg",
    src: "Étude critique inventée pour le site.",
    doc: { ref: "Robert H. Jackson, procureur en chef des États-Unis, déclaration d'ouverture devant le Tribunal militaire international de Nuremberg, 21 novembre 1945 (extraits, traduction du site ; texte officiel du gouvernement américain, dans le domaine public).", txt: [
      "« Le privilège d'ouvrir le premier procès de l'histoire pour crimes contre la paix du monde impose une lourde responsabilité. Les crimes que nous cherchons à condamner et à punir ont été si calculés, si malfaisants et si dévastateurs que la civilisation ne peut tolérer qu'on les ignore, car elle ne survivrait pas à leur répétition. Que quatre grandes nations, grisées par la victoire et meurtries par l'injure, retiennent le bras de la vengeance et soumettent volontairement leurs ennemis captifs au jugement de la loi, c'est l'un des hommages les plus importants que la Puissance ait jamais rendus à la Raison. […]",
      "Nous ne devons jamais oublier que le dossier sur lequel nous jugeons aujourd'hui ces accusés est celui sur lequel l'histoire nous jugera demain. Tendre à ces accusés une coupe empoisonnée, c'est la porter aussi à nos propres lèvres. […]",
      "Nous ne vous demanderons pas de condamner ces hommes sur le témoignage de leurs ennemis. Il n'y a pas un chef de l'acte d'accusation qui ne puisse être prouvé par des livres et des archives. Les Allemands ont toujours tenu leurs archives avec minutie. […]",
      "Les crimes les plus sauvages et les plus nombreux que les nazis ont projetés et commis furent ceux dirigés contre les Juifs. […] L'histoire ne rapporte aucun crime jamais perpétré contre autant de victimes, ni aucun exécuté avec une cruauté aussi calculée. »"
    ] },
    consigne: "En analysant le document de manière critique, montre ce que le procès de Nuremberg apporte à la justice et à l'histoire des crimes nazis, puis discute les limites de cette justice.",
    intro: "Le 21 novembre 1945, au lendemain de l'ouverture du procès, Robert H. Jackson, juge à la Cour suprême des États-Unis et procureur en chef américain, prononce la déclaration d'ouverture de l'accusation devant le Tribunal militaire international de Nuremberg. Il s'adresse aux juges des quatre puissances victorieuses (États-Unis, Royaume-Uni, URSS, France), mais aussi à l'opinion mondiale, puisque le procès est filmé et suivi par des centaines de journalistes. Vingt-deux dirigeants nazis sont jugés pour crimes contre la paix, crimes de guerre et crimes contre l'humanité, définis par l'accord de Londres du 8 août 1945. En quoi ce discours montre-t-il l'ambition d'une justice internationale capable d'établir les crimes nazis pour l'histoire, et quelles en sont les limites ?",
    parts: [
      ["1. Le choix du droit plutôt que de la vengeance", "Jackson oppose « la vengeance » au « jugement de la loi » : les vainqueurs auraient pu exécuter les vaincus sans procès, comme l'avait d'abord envisagé Churchill. Le procès est présenté comme un « hommage » de « la Puissance » à « la Raison ». C'est une rupture : pour la première fois, des dirigeants d'un État sont jugés par une juridiction internationale pour des crimes définis par un statut. L'enjeu est aussi préventif : la civilisation « ne survivrait pas à leur répétition ». Nuremberg fonde ainsi le droit pénal international dont héritent la convention de 1948, les TPI des années 1990 et la CPI (1998-2002)."],
      ["2. Un procès fondé sur les archives, qui écrit l'histoire", "Jackson insiste sur les preuves écrites : « des livres et des archives » allemands, tenus « avec minutie ». L'accusation américaine s'appuie sur des milliers de documents saisis, ce qui fait du procès une source majeure pour les historiens. Jackson souligne aussi la spécificité des crimes « contre les Juifs », les plus « nombreux » et menés avec une « cruauté calculée ». Pourtant, le génocide n'est pas encore un crime en droit : le mot de Lemkin (1944) n'apparaît que dans l'acte d'accusation, et le tribunal condamne pour crimes contre l'humanité, sans placer le génocide des Juifs au centre du procès ; celui des Tsiganes est presque absent."],
      ["3. Une justice des vainqueurs ? Les limites du procès", "Jackson anticipe la critique : l'histoire jugera les juges, et la « coupe empoisonnée » menace aussi les accusateurs. De fait, seuls les crimes de l'Axe sont jugés : ni les bombardements alliés, ni le massacre de Katyn (commis par les Soviétiques en 1940, que l'accusation soviétique tente d'imputer aux Allemands) ne sont condamnés, alors qu'un juge soviétique siège. Le verdict (1er octobre 1946 : 12 condamnations à mort, 3 acquittements) ne touche que quelques dirigeants ; la guerre froide arrête vite les poursuites. Il faudra le procès Eichmann (1961), puis ceux de Francfort, de Barbie et de Papon pour que la justice et la mémoire s'emparent pleinement du génocide."]
    ],
    concl: "La déclaration de Robert Jackson exprime l'ambition fondatrice de Nuremberg : soumettre la puissance au droit, juger des individus pour des crimes inédits et établir les faits par les archives, pour l'histoire. Le procès invente le crime contre l'humanité et prépare toute la justice pénale internationale. Mais c'est un tribunal de vainqueurs, qui ignore les crimes alliés et laisse encore dans l'ombre la singularité des génocides des Juifs et des Tsiganes : la mémoire de ces crimes se construira surtout plus tard.",
    critique: "Regard critique : discours d'un accusateur, donc à charge, prononcé devant les caméras et destiné à l'opinion américaine et mondiale ; il présente comme impartial un tribunal composé uniquement de juges des puissances victorieuses, dont l'URSS, elle-même coupable de crimes de masse ; il ignore le génocide des Tsiganes."
  },
  autres: [
    ["Les causes de la Première Guerre mondiale : un débat historique aux enjeux politiques", "Plan chronologique : I. 1919-1945, la responsabilité, arme diplomatique (art. 231, Kriegsschuldlüge, responsabilité partagée) ; II. 1961-1990, la controverse Fischer et l'identité allemande ; III. depuis 2012, Clark, Krumeich et la réconciliation européenne."],
    ["Juger les crimes nazis de Nuremberg à nos jours", "Plan chronologique : I. Nuremberg et ses suites (1945-1949) ; II. Eichmann et Francfort, la justice et la mémoire (1960-1965) ; III. Imprescriptibilité et derniers procès (Barbie 1987, Papon 1998, Gröning 2015)."],
    ["Les mémoires de la guerre d'Algérie (étude critique possible)", "Document type : discours de François Hollande sur le 17 octobre 1961 ou rapport Stora (extraits courts) : situer le geste, montrer ce qu'il reconnaît et ce qu'il tait, le relier à la concurrence des mémoires et aux relations franco-algériennes."]
  ]
};
