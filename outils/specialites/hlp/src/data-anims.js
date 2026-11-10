/* Animations explicatives (moteur : animations.js). Types :
   - texte  : { atelier: n } ou { segs: [...] } (même format que l'atelier) ; chaque segment annoté est une étape ;
   - graphe : { w, h, noeuds: [{ id, x, y, w, h, t: "ligne|ligne", s: these|arg|obj|ex|concl }], liens: [{ de, a, t, s: "contre", courbe }],
              etapes: [{ montre: [ids], legende }] } ;
   - frise  : { debut, fin, pas, periodes: [{ id, de, a, nom, rang }], evts: [{ id, an, t, h, g }], etapes: [{ an, montre, legende }] }.
   Une entrée les appelle par son champ anims: ["id", …] ; une page par <div data-anim="id"></div>. */
HLP.ANIMS = HLP.ANIMS || {};
Object.assign(HLP.ANIMS, {
  "e1-paradoxe": { type: "graphe", titre: "Le paradoxe de l’Émile : éduquer sans dénaturer", w: 640, h: 420,
    intro: "Rousseau ouvre son traité par une accusation contre l’homme… puis la retourne. Suis l’argument étape par étape.",
    noeuds: [
      { id: "a", x: 20, y: 16, w: 280, h: 58, s: "these", t: "« Tout est bien sortant des mains|de l’Auteur des choses »" },
      { id: "b", x: 340, y: 16, w: 280, h: 58, s: "obj", t: "« tout dégénère|entre les mains de l’homme »" },
      { id: "c", x: 340, y: 110, w: 280, h: 58, s: "ex", t: "il mutile, défigure, veut « dresser »|l’homme « comme un cheval de manège »" },
      { id: "d", x: 20, y: 110, w: 280, h: 58, s: "arg", t: "Retournement : « Sans cela,|tout irait plus mal encore »" },
      { id: "e", x: 20, y: 204, w: 280, h: 58, s: "ex", t: "préjugés, autorité, exemple|« étoufferaient en lui la nature »" },
      { id: "f", x: 340, y: 204, w: 280, h: 58, s: "ex", t: "l’arbrisseau né au milieu du chemin,|que « les passants font bientôt périr »" },
      { id: "g", x: 120, y: 300, w: 400, h: 54, s: "concl", t: "Conclusion : éduquer, c’est cultiver,|pas dresser (« On façonne les plantes par la culture »)" },
      { id: "h", x: 170, y: 372, w: 300, h: 40, s: "arg", t: "Livre II : l’éducation « négative »" }
    ],
    liens: [{ de: "a", a: "b", t: "mais" }, { de: "b", a: "c", t: "exemples" }, { de: "c", a: "d", t: "pourtant", s: "contre" }, { de: "d", a: "e", t: "car" }, { de: "e", a: "f", t: "image" }, { de: "f", a: "g", t: "donc" }, { de: "g", a: "h" }],
    etapes: [
      { montre: ["a"], legende: "<b>La thèse de départ.</b> Ce qui vient de la nature est bon : c’est le présupposé de tout le livre." },
      { montre: ["b"], legende: "<b>L’accusation.</b> L’homme gâte ce qu’il touche. L’éducation ordinaire en fait partie." },
      { montre: ["c"], legende: "<b>Les exemples</b> vont de la terre à l’animal, puis à l’esclave et à l’enfant : on « dresse » l’homme pour soi." },
      { montre: ["d"], legende: "<b>Le retournement.</b> Refuser d’éduquer serait pire : dans la société telle qu’elle est, l’enfant serait livré à tout." },
      { montre: ["e"], legende: "<b>La raison :</b> sans éducation, ce sont les préjugés et l’exemple qui forment l’enfant, au hasard." },
      { montre: ["f"], legende: "<b>L’image</b> condense l’argument : sans enceinte, la jeune plante est piétinée. L’éducation protège." },
      { montre: ["g"], legende: "<b>La conclusion :</b> il ne s’agit pas de choisir entre nature et éducation, mais de trouver une éducation qui cultive la nature." },
      { montre: ["h"], legende: "<b>Ce que Rousseau en tire :</b> une première éducation « négative », qui protège du vice et de l’erreur au lieu d’imposer des leçons." }
    ] },
  "e1-minorite": { type: "graphe", titre: "Sortir de la minorité : le raisonnement de Kant (1784)", w: 640, h: 400,
    intro: "Pourquoi tant d’hommes restent-ils « mineurs » toute leur vie, et comment en sortir ?",
    noeuds: [
      { id: "m", x: 200, y: 14, w: 240, h: 54, s: "these", t: "Minorité :|penser sous la direction d’autrui" },
      { id: "p", x: 14, y: 110, w: 172, h: 54, s: "arg", t: "Paresse|« Il est si commode… »" },
      { id: "l", x: 234, y: 110, w: 172, h: 54, s: "arg", t: "Lâcheté|peur de penser seul" },
      { id: "t", x: 454, y: 110, w: 172, h: 54, s: "obj", t: "Les tuteurs|en profitent" },
      { id: "s", x: 120, y: 214, w: 400, h: 54, s: "ex", t: "« Sapere aude, aie le courage de te servir|de ta propre intelligence ! »" },
      { id: "u", x: 120, y: 304, w: 180, h: 66, s: "arg", t: "Liberté de l’usage|public de la raison|(écrire, publier)" },
      { id: "c", x: 340, y: 304, w: 180, h: 66, s: "concl", t: "Un public qui|s’éclaire lui-même :|les Lumières" }
    ],
    liens: [{ de: "p", a: "m", t: "cause" }, { de: "l", a: "m", t: "cause" }, { de: "t", a: "m", t: "entretiennent", via: [[540, 60], [470, 41]], lx: 506, ly: 52, la: "start" }, { de: "m", a: "s", t: "remède", via: [[430, 96], [440, 200]], lx: 448, ly: 198, la: "start" }, { de: "s", a: "u", t: "condition" }, { de: "u", a: "c" }],
    etapes: [
      { montre: ["m"], legende: "<b>Définition.</b> La minorité n’est pas un âge : c’est l’incapacité de penser sans être dirigé." },
      { montre: ["p"], legende: "<b>Première cause : la paresse.</b> Un livre, un directeur, un médecin pensent à ma place." },
      { montre: ["l"], legende: "<b>Deuxième cause : la lâcheté.</b> Penser seul expose à se tromper et à déplaire." },
      { montre: ["t"], legende: "<b>Les tuteurs</b> tirent leur pouvoir de cette minorité et l’entretiennent." },
      { montre: ["s"], legende: "<b>Le remède est moral :</b> du courage. D’où la devise, à l’impératif." },
      { montre: ["u"], legende: "<b>Il a une condition politique :</b> la liberté de faire un usage public de sa raison." },
      { montre: ["c"], legende: "<b>Conclusion :</b> un individu seul en sort difficilement, mais un public libre s’éclaire peu à peu." }
    ] },
  "e1-kant-lecture": { type: "texte", atelier: 2, titre: "Lecture animée : Kant, « Qu’est-ce que les Lumières ? »", intro: "Les mouvements du texte (définition, devise, causes) s’allument au fil de la lecture." },
  "e2-madeleine": { type: "graphe", titre: "La mémoire involontaire : comment revient le souvenir (Proust, 1913)", w: 640, h: 450,
    intro: "Le phénomène, pas à pas : une sensation présente fait revivre un passé que l’effort de mémoire ne retrouvait pas.",
    noeuds: [
      { id: "a", x: 20, y: 14, w: 260, h: 54, s: "arg", t: "Un jour d’hiver,|du thé et une madeleine" },
      { id: "b", x: 360, y: 14, w: 260, h: 54, s: "ex", t: "« Un plaisir délicieux m’avait envahi,|isolé, sans la notion de sa cause »" },
      { id: "c", x: 360, y: 108, w: 260, h: 54, s: "ex", t: "« cette essence n’était pas en moi,|elle était moi »" },
      { id: "d", x: 20, y: 108, w: 260, h: 54, s: "obj", t: "Deuxième, troisième gorgée :|l’effet diminue" },
      { id: "e", x: 20, y: 202, w: 260, h: 54, s: "these", t: "« la vérité que je cherche|n’est pas en lui, mais en moi »" },
      { id: "f", x: 360, y: 202, w: 260, h: 54, s: "arg", t: "Le narrateur se tourne vers son esprit :|le souvenir résiste, remonte" },
      { id: "g", x: 190, y: 296, w: 260, h: 54, s: "concl", t: "« Et tout d’un coup|le souvenir m’est apparu »" },
      { id: "h", x: 120, y: 380, w: 400, h: 54, s: "ex", t: "Combray, le dimanche matin : la madeleine|trempée dans le thé ou le tilleul de la tante Léonie" }
    ],
    liens: [{ de: "a", a: "b", t: "sensation" }, { de: "b", a: "c", t: "joie" }, { de: "c", a: "d", t: "répéter ?" }, { de: "d", a: "e", t: "donc" }, { de: "e", a: "f", t: "chercher" }, { de: "f", a: "g" }, { de: "g", a: "h", t: "tout revient" }],
    etapes: [
      { montre: ["a"], legende: "<b>Le déclencheur</b> est banal : le goût d’une boisson et d’un gâteau, un jour ordinaire." },
      { montre: ["b"], legende: "<b>Une joie sans cause apparente.</b> La sensation précède la compréhension." },
      { montre: ["c"], legende: "<b>Le moi se sent autre :</b> « J’avais cessé de me sentir médiocre, contingent, mortel »." },
      { montre: ["d"], legende: "<b>L’échec de la répétition.</b> Boire encore ne sert à rien : la vertu du breuvage diminue." },
      { montre: ["e"], legende: "<b>Le déplacement décisif :</b> la vérité n’est pas dans l’objet mais dans la mémoire du sujet." },
      { montre: ["f"], legende: "<b>Un travail intérieur.</b> Le souvenir remonte lentement, sans qu’on sache encore lequel." },
      { montre: ["g"], legende: "<b>La révélation</b> est soudaine : c’est le propre de la mémoire involontaire." },
      { montre: ["h"], legende: "<b>Tout un monde renaît :</b> c’est le point de départ de Combray, et de toute la Recherche." }
    ] },
  "e2-lac-lecture": { type: "texte", atelier: 0, titre: "Lecture animée : Lamartine, « Le Lac »", intro: "Les trois mouvements du poème et ses procédés s’allument vers après vers." },
  "e2-dire": { type: "graphe", titre: "Peut-on dire ce qu’on ressent ? Un schéma d’argumentation", w: 640, h: 430,
    intro: "Comment construire une réponse à la question du programme sur le langage commun et l’expérience singulière.",
    noeuds: [
      { id: "q", x: 150, y: 12, w: 340, h: 50, s: "these", t: "Problème : l’expérience est singulière,|les mots sont communs" },
      { id: "a", x: 20, y: 100, w: 270, h: 58, s: "obj", t: "Bergson : « le mot brutal »|écrase les impressions fugitives" },
      { id: "b", x: 360, y: 100, w: 260, h: 58, s: "ex", t: "Le mets « réputé exquis » : le nom|s’interpose entre sensation et conscience" },
      { id: "c", x: 20, y: 196, w: 280, h: 58, s: "arg", t: "Wittgenstein : un langage privé|est impossible ; les mots s’apprennent" },
      { id: "d", x: 340, y: 196, w: 280, h: 58, s: "arg", t: "Proust : le style, « question|non de technique, mais de vision »" },
      { id: "e", x: 340, y: 286, w: 280, h: 52, s: "ex", t: "Baudelaire : les synesthésies|inventent des manières de sentir" },
      { id: "f", x: 90, y: 362, w: 460, h: 56, s: "concl", t: "On ne dit pas l’intime malgré les mots communs,|mais en les travaillant : c’est le rôle de l’art" }
    ],
    liens: [{ de: "q", a: "a", t: "objection" }, { de: "a", a: "b", t: "exemple", lx: 331, ly: 122 }, { de: "q", a: "c", t: "réponse", via: [[298, 120], [305, 190]], lx: 286, ly: 186, la: "end" }, { de: "c", a: "d", t: "et" }, { de: "d", a: "e", t: "exemple" }, { de: "c", a: "f" }, { de: "e", a: "f" }],
    etapes: [
      { montre: ["q"], legende: "<b>Poser le problème.</b> Ce que je ressens n’appartient qu’à moi ; les mots appartiennent à tous." },
      { montre: ["a"], legende: "<b>L’objection forte :</b> le langage fixe et généralise ce qui est mouvant et singulier." },
      { montre: ["b"], legende: "<b>L’exemple de Bergson</b> : on croit aimer une saveur parce que son nom est flatteur." },
      { montre: ["c"], legende: "<b>Premier dépassement :</b> nos sentiments ne sont pas enfermés ; nous apprenons à les nommer avec les autres." },
      { montre: ["d"], legende: "<b>Deuxième dépassement :</b> l’écrivain travaille les mots communs pour faire voir sa vision." },
      { montre: ["e"], legende: "<b>Un exemple littéraire</b> : « Les parfums, les couleurs et les sons se répondent »." },
      { montre: ["f"], legende: "<b>La réponse :</b> dire l’intime est difficile mais possible ; c’est même ce que fait la littérature." }
    ] },
  "e3-soupcon": { type: "graphe", titre: "Le moi, de la certitude au soupçon", w: 640, h: 470,
    intro: "Quatre siècles de réponses à la question « qui suis-je ? », chacune répondant à la précédente.",
    noeuds: [
      { id: "m", x: 20, y: 12, w: 280, h: 58, s: "arg", t: "Montaigne (1588) :|« Je peins le passage »" },
      { id: "d", x: 340, y: 12, w: 280, h: 58, s: "these", t: "Descartes (1637-1641) :|« une chose qui pense »" },
      { id: "h", x: 340, y: 106, w: 280, h: 58, s: "obj", t: "Hume (1739) : je ne trouve|que des perceptions, pas un « moi »" },
      { id: "r", x: 20, y: 106, w: 280, h: 58, s: "ex", t: "Rousseau (1782) : « Si je ne vaux pas|mieux, au moins je suis autre »" },
      { id: "j", x: 20, y: 200, w: 280, h: 58, s: "obj", t: "Rimbaud (1871) :|« Je est un autre »" },
      { id: "n", x: 340, y: 200, w: 280, h: 58, s: "obj", t: "Nietzsche (1886) : le « je »|est une habitude de la grammaire" },
      { id: "f", x: 340, y: 294, w: 280, h: 58, s: "obj", t: "Freud (1917) : le moi n’est pas|maître dans sa propre maison" },
      { id: "b", x: 20, y: 294, w: 280, h: 58, s: "arg", t: "Bergson (1889) : moi profond,|moi superficiel" },
      { id: "c", x: 100, y: 394, w: 440, h: 60, s: "concl", t: "Se connaître n’est pas un constat|mais une tâche : interpréter, écrire, devenir" }
    ],
    liens: [{ de: "m", a: "d", t: "contre l’instable" }, { de: "d", a: "h", t: "objection", s: "contre" }, { de: "h", a: "r" }, { de: "r", a: "j", t: "critique du Moi" }, { de: "j", a: "n" }, { de: "n", a: "f", t: "soupçon" }, { de: "f", a: "b" }, { de: "b", a: "c" }],
    etapes: [
      { montre: ["m"], legende: "<b>Montaigne</b> observe un moi qui change « de jour en jour, de minute en minute »." },
      { montre: ["d"], legende: "<b>Descartes</b> cherche un point fixe : je suis certain d’exister tant que je pense." },
      { montre: ["h"], legende: "<b>Hume objecte :</b> en regardant en moi, je ne vois que des perceptions qui se succèdent." },
      { montre: ["r"], legende: "<b>Rousseau</b> fonde l’autobiographie sur la singularité et la sincérité." },
      { montre: ["j"], legende: "<b>Rimbaud</b> renverse le lyrisme : le moi n’est pas l’auteur de ses pensées (« On me pense »)." },
      { montre: ["n"], legende: "<b>Nietzsche</b> : une pensée vient quand elle veut, pas quand « je » veux." },
      { montre: ["f"], legende: "<b>Freud</b> : l’inconscient agit sans que le moi le sache (rêves, lapsus, symptômes)." },
      { montre: ["b"], legende: "<b>Bergson</b> distingue le moi social, découpé par le langage, et le moi profond, durée vivante." },
      { montre: ["c"], legende: "<b>Bilan pour la copie :</b> le moi n’est pas donné ; on y accède par des récits, des interprétations, une œuvre." }
    ] },
  "e3-cogito": { type: "graphe", titre: "Du doute au « je pense » : le chemin de Descartes (1637-1641)", w: 640, h: 476,
    intro: "Comment Descartes trouve, au bout du doute, une certitude que rien ne peut ébranler : celle du moi qui pense. Citations des <i>Méditations</i> dans la traduction du duc de Luynes (1647), orthographe modernisée.",
    noeuds: [
      { id: "p", x: 130, y: 12, w: 380, h: 54, s: "these", t: "Projet : établir « quelque chose|de ferme et de constant dans les sciences »" },
      { id: "s", x: 10, y: 104, w: 196, h: 66, s: "obj", t: "1. Les sens|ils se sont « quelquefois »|montrés trompeurs" },
      { id: "r", x: 222, y: 104, w: 196, h: 66, s: "obj", t: "2. Le rêve|veille ou sommeil ? point|d’« indices certains »" },
      { id: "g", x: 434, y: 104, w: 196, h: 66, s: "obj", t: "3. Le « mauvais génie »|« rusé et trompeur » :|même 2 + 3 = 5 ?" },
      { id: "c", x: 100, y: 206, w: 440, h: 66, s: "arg", t: "Mais pour être trompé, il faut être :|« Il n’y a donc point de doute|que je suis, s’il me trompe »" },
      { id: "q", x: 24, y: 310, w: 284, h: 58, s: "these", t: "« Je pense, donc je suis »|Discours de la méthode, 1637" },
      { id: "e", x: 332, y: 310, w: 284, h: 58, s: "ex", t: "« je suis, j’existe » : vrai « toutes|les fois que je la prononce »" },
      { id: "f", x: 70, y: 404, w: 500, h: 58, s: "concl", t: "Ce que je suis : « une chose qui pense, c’est-à-dire|un esprit, un entendement ou une raison »" }
    ],
    liens: [{ de: "p", a: "s", t: "douter" }, { de: "p", a: "r" }, { de: "p", a: "g" }, { de: "s", a: "c" }, { de: "r", a: "c" }, { de: "g", a: "c", t: "même alors" }, { de: "c", a: "q", t: "donc" }, { de: "c", a: "e" }, { de: "q", a: "f" }, { de: "e", a: "f" }],
    etapes: [
      { montre: ["p"], legende: "<b>Le projet.</b> Pour fonder le savoir sur un point indubitable, Descartes rejette tout ce qui laisse le moindre doute. C’est une méthode, pas un scepticisme : on doute pour trouver le certain." },
      { montre: ["s"], legende: "<b>Premier niveau : les sens.</b> Ils nous ont parfois trompés ; par prudence, on ne se fie plus à ce qui nous a trompés une fois." },
      { montre: ["r"], legende: "<b>Deuxième niveau : le rêve.</b> Je crois souvent être éveillé quand je dors : rien ne garantit que ce que je perçois existe." },
      { montre: ["g"], legende: "<b>Troisième niveau, « hyperbolique » :</b> un trompeur tout-puissant pourrait m’abuser même quand je calcule que deux et trois font cinq. Plus rien ne semble résister." },
      { montre: ["c"], legende: "<b>Le retournement.</b> Le doute bute sur une limite : si l’on me trompe, c’est que j’existe pour être trompé. Le trompeur « ne saura jamais faire que je ne sois rien, tant que je penserai être quelque chose »." },
      { montre: ["q"], legende: "<b>La formule du <i>Discours de la méthode</i></b> (IV<sup>e</sup> partie) : la première vérité certaine, que Descartes reçoit comme « le premier principe de la philosophie »." },
      { montre: ["e"], legende: "<b>Dans les <i>Méditations</i> (1641),</b> la certitude tient à l’acte de penser : elle vaut chaque fois que je pense ou que je dis « je suis », pas une fois pour toutes." },
      { montre: ["f"], legende: "<b>Ce qu’est ce moi :</b> une chose « qui doute, qui entend, qui conçoit, qui affirme, qui nie, qui veut, qui ne veut pas, qui imagine aussi, et qui sent ». Un moi stable, substance pensante : c’est ce que Hume, Nietzsche et Freud contesteront." }
    ] },
  "e3-rimbaud-lecture": { type: "texte", atelier: 3, titre: "Lecture animée : Rimbaud, lettre du voyant", intro: "La grammaire, les images et la ponctuation qui disent un moi dédoublé, une à une." },
  "frise-mouvements": { type: "frise", titre: "La frise qui se déroule : des Lumières au surréalisme", debut: 1750, fin: 1960, pas: 25, h: 330, min: 820,
    intro: "Les grands mouvements apparaissent dans l’ordre, avec une œuvre repère pour chacun. Dates indicatives : un mouvement n’a ni naissance ni mort précises.",
    periodes: [
      { id: "lum", de: 1750, a: 1789, nom: "Lumières", rang: 0, c: 0 },
      { id: "rom", de: 1820, a: 1850, nom: "Romantisme", rang: 0, c: 1 },
      { id: "rea", de: 1850, a: 1890, nom: "Réalisme et naturalisme", rang: 1, c: 2 },
      { id: "par", de: 1866, a: 1886, nom: "Parnasse", rang: 0, c: 3 },
      { id: "sym", de: 1886, a: 1905, nom: "Symbolisme", rang: 0, c: 0 },
      { id: "avg", de: 1909, a: 1924, nom: "Avant-gardes", rang: 1, c: 1 },
      { id: "sur", de: 1924, a: 1945, nom: "Surréalisme", rang: 0, c: 2 },
      { id: "exi", de: 1943, a: 1960, nom: "Existentialisme", rang: 2, c: 3 }
    ],
    evts: [
      { id: "a", an: 1762, t: "Émile", h: 30 }, { id: "b", an: 1782, t: "Confessions", h: 58 },
      { id: "c", an: 1820, t: "Méditations poétiques", h: 30 }, { id: "d", an: 1830, t: "Hernani", h: 58 },
      { id: "e", an: 1857, t: "Fleurs du mal, Bovary", h: 30 }, { id: "f", an: 1871, t: "Lettres du voyant", h: 58 },
      { id: "g", an: 1886, t: "Manifeste du symbolisme", h: 30 }, { id: "h", an: 1909, t: "Manifeste du futurisme", h: 58 },
      { id: "i", an: 1913, t: "Swann, Alcools", h: 30 }, { id: "j", an: 1924, t: "Manifeste du surréalisme", h: 58, g: false },
      { id: "k", an: 1943, t: "L’Être et le Néant", h: 30 }
    ],
    etapes: [
      { an: 1762, montre: ["lum", "a"], legende: "<b>Les Lumières</b> : raison critique, mais aussi « droits de la sensibilité ». Rousseau publie l’<i>Émile</i> (1762)." },
      { an: 1782, montre: ["b"], legende: "<b>1782</b> : les <i>Confessions</i> paraissent après la mort de Rousseau. Le moi devient un sujet littéraire." },
      { an: 1820, montre: ["rom", "c"], legende: "<b>Le romantisme</b> : lyrisme, nature-miroir, mal du siècle. Lamartine, <i>Méditations poétiques</i> (1820)." },
      { an: 1830, montre: ["d"], legende: "<b>1830</b> : la bataille d’<i>Hernani</i> ; le drame romantique s’impose au théâtre." },
      { an: 1857, montre: ["rea", "e"], legende: "<b>Réalisme</b> : regarder le réel. 1857 : <i>Madame Bovary</i> et <i>Les Fleurs du mal</i>, deux procès." },
      { an: 1866, montre: ["par"], legende: "<b>Le Parnasse</b> (recueils du <i>Parnasse contemporain</i> à partir de 1866) : la forme parfaite, contre l’épanchement." },
      { an: 1871, montre: ["f"], legende: "<b>1871</b> : Rimbaud, « Je est un autre ». La poésie se veut voyance." },
      { an: 1886, montre: ["sym", "g"], legende: "<b>Le symbolisme</b> : suggérer plutôt que décrire. Manifeste de Moréas dans <i>Le Figaro</i> (1886)." },
      { an: 1909, montre: ["avg", "h"], legende: "<b>Les avant-gardes</b> : futurisme (1909), Dada (1916). On veut rompre avec tout le passé." },
      { an: 1913, montre: ["i"], legende: "<b>1913</b> : Proust, <i>Du côté de chez Swann</i> ; Apollinaire, <i>Alcools</i>. Modernité et mémoire." },
      { an: 1924, montre: ["sur", "j"], legende: "<b>Le surréalisme</b> : le rêve et l’inconscient en littérature. Breton, <i>Manifeste</i> (1924)." },
      { an: 1943, montre: ["exi", "k"], legende: "<b>L’existentialisme</b> : l’homme se fait par ses actes. Sartre, <i>L’Être et le Néant</i> (1943)." }
    ] },
  "ep-essai": { type: "graphe", titre: "Construire un essai : du sujet au plan", w: 640, h: 450,
    intro: "Sur l’exemple « Peut-on être heureux sans penser ? » (corrigé de l’entrée II).",
    noeuds: [
      { id: "s", x: 170, y: 10, w: 300, h: 44, s: "these", t: "Sujet : « Peut-on être heureux sans penser ? »" },
      { id: "t", x: 20, y: 86, w: 290, h: 62, s: "arg", t: "Analyser les termes : bonheur ≠ plaisir ;|penser = réfléchir, comparer, prévoir" },
      { id: "x", x: 330, y: 86, w: 290, h: 62, s: "ex", t: "Partir du texte : Rousseau sent|son existence « sans […] penser »" },
      { id: "p", x: 120, y: 180, w: 400, h: 58, s: "these", t: "Problème : la pensée est-elle l’obstacle|ou la condition du bonheur ?" },
      { id: "i", x: 20, y: 274, w: 190, h: 70, s: "arg", t: "I. La pensée|trouble le bonheur|(Pascal, Musset)" },
      { id: "ii", x: 225, y: 274, w: 190, h: 70, s: "obj", t: "II. Un bonheur|sans conscience n’est|pas humain (Kant)" },
      { id: "iii", x: 430, y: 274, w: 190, h: 70, s: "arg", t: "III. Penser autrement :|Épicure, Bergson,|l’écriture" },
      { id: "c", x: 120, y: 378, w: 400, h: 56, s: "concl", t: "Conclusion : réponse nette, qui reprend|les termes du sujet" }
    ],
    liens: [{ de: "s", a: "t" }, { de: "s", a: "x" }, { de: "t", a: "p" }, { de: "x", a: "p" }, { de: "p", a: "i" }, { de: "i", a: "ii", t: "mais" }, { de: "ii", a: "iii", t: "donc" }, { de: "iii", a: "c" }],
    etapes: [
      { montre: ["s"], legende: "<b>Lire le sujet</b> en entier, mot à mot. C’est une question soulevée par le texte." },
      { montre: ["t"], legende: "<b>Définir les termes</b> : chaque mot important a plusieurs sens, à distinguer." },
      { montre: ["x"], legende: "<b>Repartir du texte</b> : l’essai doit répondre « au regard du texte étudié » (barème officiel)." },
      { montre: ["p"], legende: "<b>Formuler le problème</b> : une tension entre deux réponses défendables." },
      { montre: ["i"], legende: "<b>Partie I</b> : la réponse la plus évidente, appuyée sur des références précises." },
      { montre: ["ii"], legende: "<b>Partie II</b> : ses limites, avec d’autres références." },
      { montre: ["iii"], legende: "<b>Partie III</b> : une réponse plus juste, qui tient compte des deux premières." },
      { montre: ["c"], legende: "<b>Conclure</b> : répondre clairement à la question posée, sans formule creuse." }
    ] }
});
Object.assign(HLP.ANIMS, {
  "e4-frise": { type: "frise", titre: "Les ruptures se suivent : de la modernité aux avant-gardes", debut: 1860, fin: 1965, pas: 15, h: 300, min: 860,
    intro: "Chaque rupture répond à la précédente. Dates indicatives pour les mouvements, exactes pour les œuvres.",
    periodes: [
      { id: "imp", de: 1874, a: 1886, nom: "Impressionnisme", rang: 0, c: 0 },
      { id: "sym", de: 1886, a: 1905, nom: "Symbolisme", rang: 1, c: 1 },
      { id: "cub", de: 1907, a: 1920, nom: "Cubisme", rang: 0, c: 2 },
      { id: "fut", de: 1909, a: 1920, nom: "Futurisme", rang: 1, c: 3 },
      { id: "dad", de: 1916, a: 1924, nom: "Dada", rang: 2, c: 1 },
      { id: "sur", de: 1924, a: 1945, nom: "Surréalisme", rang: 0, c: 0 },
      { id: "abs", de: 1950, a: 1965, nom: "Absurde, Nouveau Roman, Oulipo", rang: 1, c: 2 }
    ],
    evts: [
      { id: "a", an: 1863, t: "La modernité", h: 30 }, { id: "b", an: 1873, t: "« absolument moderne »", h: 62 },
      { id: "c", an: 1895, t: "Cinématographe", h: 30 }, { id: "d", an: 1909, t: "Manifeste futuriste", h: 62 },
      { id: "e", an: 1913, t: "« Zone »", h: 30 }, { id: "f", an: 1917, t: "Fontaine", h: 62 },
      { id: "g", an: 1924, t: "Manifeste surréaliste", h: 30 }, { id: "h", an: 1950, t: "Cantatrice chauve", h: 62 },
      { id: "i", an: 1961, t: "Cent mille milliards", h: 30, g: true }
    ],
    etapes: [
      { an: 1863, montre: ["a"], legende: "<b>1863 :</b> Baudelaire définit la modernité, « le transitoire, le fugitif, le contingent »." },
      { an: 1873, montre: ["b"], legende: "<b>1873 :</b> Rimbaud, « Il faut être absolument moderne »." },
      { an: 1874, montre: ["imp"], legende: "<b>1874 :</b> les impressionnistes exposent hors du Salon officiel ; l’injure devient un nom." },
      { an: 1886, montre: ["sym"], legende: "<b>1886 :</b> le symbolisme veut suggérer plutôt que décrire." },
      { an: 1895, montre: ["c"], legende: "<b>1895 :</b> le cinématographe Lumière ; un art nouveau naît d’une technique." },
      { an: 1907, montre: ["cub"], legende: "<b>1907 :</b> Picasso, <i>Les Demoiselles d’Avignon</i> : la perspective héritée de la Renaissance éclate." },
      { an: 1909, montre: ["fut", "d"], legende: "<b>1909 :</b> le futurisme veut « démolir les musées » et chante la vitesse." },
      { an: 1913, montre: ["e"], legende: "<b>1913 :</b> « Zone » : « À la fin tu es las de ce monde ancien ». Mais le poème garde l’image du berger." },
      { an: 1916, montre: ["dad", "f"], legende: "<b>1916-1917 :</b> Dada à Zurich ; Duchamp expose un urinoir. L’art lui-même est contesté." },
      { an: 1924, montre: ["sur", "g"], legende: "<b>1924 :</b> le surréalisme cherche dans le rêve et l’inconscient une autre logique." },
      { an: 1950, montre: ["abs", "h"], legende: "<b>Après 1945 :</b> le théâtre de l’absurde défait le dialogue, le Nouveau Roman le personnage." },
      { an: 1961, montre: ["i"], legende: "<b>1961 :</b> Queneau fait de la contrainte une machine à créer. Rompre est devenu une tradition." }
    ] },
  "e4-zone-lecture": { type: "texte", vers: true, titre: "Lecture animée : Apollinaire, « Zone » (v. 1-8)", intro: "Comment le poème dit la rupture avec le « monde ancien » en gardant les mots de la tradition.",
    segs: [
      { t: "À la fin tu es las de ce monde ancien", m: 1, titre: "Un tutoiement de soi", n: "Le poète se parle à lui-même : le « tu » dédouble le sujet. « À la fin » donne l’impression d’une décision longtemps mûrie : rompre." },
      "\n",
      { t: "Bergère ô tour Eiffel le troupeau des ponts bêle ce matin", m: 1, titre: "Une métaphore pastorale", n: "La tour Eiffel devient une bergère, les ponts un troupeau qui bêle : la ville moderne est dite avec l’image la plus ancienne de la poésie, celle des bergers antiques." },
      "\n",
      { t: "Tu en as assez de vivre dans l’antiquité grecque et romaine", m: 1, titre: "Le rejet explicite", n: "Registre familier (« en as assez ») pour congédier l’héritage gréco-romain : le ton lui-même rompt avec la solennité." },
      "\n",
      { t: "Ici même les automobiles ont l’air d’être anciennes", m: 2, titre: "Un paradoxe", n: "Même la machine, symbole futuriste, paraît déjà vieille : le nouveau s’use vite. La rupture n’a pas de fin." },
      "\n",
      { t: "La religion seule est restée toute neuve la religion", m: 2, titre: "Un renversement", n: "Le plus ancien (la religion) est déclaré le plus neuf. La répétition du mot, sans ponctuation, crée un effet d’insistance orale." },
      "\n",
      { t: "Est restée simple comme les hangars de Port-Aviation", m: 2, titre: "Une comparaison moderne", n: "Le religieux est comparé aux hangars d’un aérodrome : l’ancien et le moderne s’échangent leurs images." },
      "\n",
      { t: "Seul en Europe tu n’es pas antique ô Christianisme", m: 3, titre: "Apostrophe", n: "L’apostrophe solennelle (« ô ») revient, mais adressée au christianisme présenté comme moderne." },
      "\n",
      { t: "L’Européen le plus moderne c’est vous Pape Pie X", m: 3, titre: "Une pointe", n: "Le pape régnant (Pie X) devient « l’Européen le plus moderne » : un trait d’humour qui achève de brouiller l’opposition entre ancien et nouveau." }
    ] },
  "e4-rupture": { type: "graphe", titre: "Y a-t-il des ruptures radicales ? Un schéma d’argumentation", w: 640, h: 440,
    intro: "Trois réponses possibles à la question du programme, chacune appuyée sur des exemples.",
    noeuds: [
      { id: "q", x: 140, y: 12, w: 360, h: 50, s: "these", t: "Question : y a-t-il des ruptures radicales|en art, en littérature, en pensée ?" },
      { id: "a", x: 20, y: 100, w: 280, h: 58, s: "arg", t: "Oui : table rase des avant-gardes|(futurisme 1909, Dada 1916)" },
      { id: "ae", x: 340, y: 100, w: 280, h: 58, s: "ex", t: "« démolir les musées » ;|un urinoir exposé (Duchamp, 1917)" },
      { id: "b", x: 20, y: 194, w: 280, h: 58, s: "obj", t: "Mais : une rupture dépend|de ce qu’elle rejette" },
      { id: "be", x: 340, y: 194, w: 280, h: 58, s: "ex", t: "la Victoire de Samothrace nommée ;|la querelle de 1687, déjà" },
      { id: "c", x: 20, y: 288, w: 280, h: 58, s: "arg", t: "Créer, c’est transformer l’héritage|(Apollinaire, Eliot)" },
      { id: "ce", x: 340, y: 288, w: 280, h: 58, s: "ex", t: "Picasso et Les Ménines (1957) ;|Anouilh, Antigone (1944)" },
      { id: "z", x: 110, y: 374, w: 420, h: 56, s: "concl", t: "Les ruptures sont réelles mais jamais absolues :|la rupture est devenue une « tradition du nouveau »" }
    ],
    liens: [{ de: "q", a: "a" }, { de: "a", a: "ae", t: "exemples" }, { de: "a", a: "b", t: "objection", s: "contre" }, { de: "b", a: "be", t: "exemples" }, { de: "b", a: "c", t: "donc" }, { de: "c", a: "ce", t: "exemples" }, { de: "c", a: "z" }],
    etapes: [
      { montre: ["q"], legende: "<b>La question</b> vient du programme : elle appelle une réponse nuancée, pas un oui ou un non." },
      { montre: ["a"], legende: "<b>Première réponse :</b> les avant-gardes ont voulu tout recommencer." },
      { montre: ["ae"], legende: "<b>Exemples</b> : le manifeste futuriste, le ready-made." },
      { montre: ["b"], legende: "<b>Objection :</b> rompre, c’est encore se définir par rapport à ce qu’on rejette." },
      { montre: ["be"], legende: "<b>Exemples</b> : le futurisme cite la statue qu’il veut détrôner ; la querelle des Anciens et des Modernes date de 1687." },
      { montre: ["c"], legende: "<b>Dépassement :</b> la création réorganise l’héritage au lieu de l’abolir." },
      { montre: ["ce"], legende: "<b>Exemples</b> : les variations de Picasso, les mythes réécrits au théâtre." },
      { montre: ["z"], legende: "<b>Conclusion :</b> la rupture est un geste réel, mais elle appartient elle-même à une histoire." }
    ] }
});
