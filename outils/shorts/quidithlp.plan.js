// Découpage du short « quidithlp » (format 5, « HLP : qui a dit ça ? » : quatre citations, trois auteurs), modèle A,
// habillage « jeu » (plateau de jeu télé). a: [passage, mot] ; av : avance sur le mot.
// Pour chaque citation : numéro, citation écrite au fil de la voix, plan `quiz3` (chrono dans le silence qui suit la
// question, verdict sur « Réponse »), l'auteur, puis une ou deux images du sens.
const Q = { type: 'quiz3', sur: 'HLP · QUI A DIT ÇA ?' };
const quiz = o => Object.assign({}, Q, o);
const C1 = '« Je suis moi-même|la matière de mon livre. »';
const C2 = '« Le moi|est haïssable. »';
const C3 = '« Je est|un autre. »';
const C4 = '« La banalité|du mal. »';
window.PLAN = S => S.plans([
  // h1 « HLP : 4 citations. Combien tu en reconnais ? »
  { a: ['h1', 0], av: .2, type: 'cases', ch: 0, q: ['h1', 'combien'] },
  // h2 « Pour chacune, trois auteurs. Un seul l'a écrite. Attention aux pièges ! »
  { a: ['h2', 0], type: 'trois', un: ['h2', 'un'] },
  { a: ['h2', 'attention'], type: 'mot', t: 'ATTENTION|AUX PIÈGES', choc: true },
  // q1 « Citation 1 : « Je suis moi-même la matière de mon livre. » Rousseau, Montaigne… ou Proust ? »
  { a: ['q1', 0], type: 'num', n: 1, ch: 1 },
  { a: ['q1', 'je'], type: 'citation', n: 1, q: C1 },
  quiz({ a: ['q1', 'rousseau'], n: '1 / 4', q: C1, chrono: ['q1', 'rousseau'], rep: ['r1a', 'réponse'], bonne: 1, expl: 'Les Essais, « Au lecteur », 1580',
    options: [{ t: 'Rousseau', img: 'rousseau', sous: '1712 – 1778' }, { t: 'Montaigne', img: 'montaigne', sous: '1533 – 1592' }, { t: 'Proust', img: 'proust', sous: '1871 – 1922' }] }),
  // r1b « Les Essais, 1580. Son projet : se peindre lui-même, tel qu'il est. Deux siècles avant les Confessions de Rousseau ! »
  { a: ['r1b', 0], type: 'auteur', img: 'montaigne', t: 'MONTAIGNE', oeuvre: 'Les Essais', date: '1580' },
  { a: ['r1b', 'son'], type: 'photo', img: 'tour', t: 'SE PEINDRE|TEL QU’IL EST', de: [1.0, .5, .4], vers: [1.15, .5, .35], legende: 'La tour de Montaigne, où il écrit les Essais (photo Henry Salomé, CC BY-SA 4.0)' },
  { a: ['r1b', 'deux'], type: 'siecles' },
  // q2 « Citation 2 : « Le moi est haïssable. » Montaigne, Pascal… ou Descartes ? »
  { a: ['q2', 0], type: 'num', n: 2, ch: 2 },
  { a: ['q2', 'le'], type: 'citation', n: 2, q: C2 },
  quiz({ a: ['q2', 'montaigne'], n: '2 / 4', q: C2, chrono: ['q2', 'montaigne'], rep: ['r2a', 'réponse'], bonne: 1, expl: 'Pensées, publiées en 1670',
    options: [{ t: 'Montaigne', img: 'montaigne', sous: '1533 – 1592' }, { t: 'Pascal', img: 'pascal', sous: '1623 – 1662' }, { t: 'Descartes', img: 'descartes', sous: '1596 – 1650' }] }),
  // r2b « Les Pensées, 1670. Et il se moque de Montaigne : quel sot projet, de se peindre ! »
  { a: ['r2b', 0], type: 'auteur', img: 'pascal', t: 'PASCAL', oeuvre: 'Pensées (publiées après sa mort)', date: '1670' },
  { a: ['r2b', 'et'], type: 'sot', sot: ['r2b', 'sot'] },
  // q3 « Citation 3 : « Je est un autre. » Baudelaire, Rimbaud… ou Verlaine ? »
  { a: ['q3', 0], type: 'num', n: 3, ch: 3 },
  { a: ['q3', 'je'], type: 'citation', n: 3, q: C3 },
  quiz({ a: ['q3', 'baudelaire'], n: '3 / 4', q: C3, chrono: ['q3', 'baudelaire'], rep: ['r3a', 'réponse'], bonne: 1, expl: 'Lettres « du voyant », mai 1871',
    options: [{ t: 'Baudelaire', img: 'baudelaire', sous: '1821 – 1867' }, { t: 'Rimbaud', img: 'rimbaud', sous: '1854 – 1891' }, { t: 'Verlaine', img: 'verlaine', sous: '1844 – 1896' }] }),
  // r3b « Une lettre de mai 1871. Il a 16 ans, et pour lui, le poète doit se faire voyant. »
  { a: ['r3b', 0], type: 'auteur', img: 'rimbaud', t: 'RIMBAUD', oeuvre: 'Lettre « du voyant »', date: '1871' },
  { a: ['r3b', 'il'], type: 'photo', img: 'coindetable', t: 'IL A|16 ANS', sous: 'Verlaine et Rimbaud, assis à gauche, en 1872', de: [1.6, .15, .7], vers: [1.85, .17, .68], legende: 'Henri Fantin-Latour, Un coin de table, 1872 (musée d’Orsay)' },
  { a: ['r3b', 'poète'], type: 'voyant' },
  // q4 « Dernière citation : « La banalité du mal. » Kant, Arendt… ou Sartre ? »
  { a: ['q4', 0], type: 'num', n: 4, t: 'DERNIÈRE', ch: 4, choc: true },
  { a: ['q4', 'la'], type: 'citation', n: 4, q: C4 },
  quiz({ a: ['q4', 'kant'], n: '4 / 4', q: C4, chrono: ['q4', 'kant'], rep: ['r4a', 'réponse'], bonne: 1, expl: 'Eichmann à Jérusalem, 1963',
    options: [{ t: 'Kant', img: 'kant', sous: '1724 – 1804' }, { t: 'Arendt', img: 'arendt', sous: '1906 – 1975' }, { t: 'Sartre', img: 'sartre', sous: '1905 – 1980' }] }),
  // r4a « … Le piège, c'était Kant et son mal radical. »
  { a: ['r4a', 'le'], type: 'piege', img: 'kant', t: 'KANT', sous: '« le mal radical », 1793' },
  // r4b « Eichmann à Jérusalem, 1963. Au procès d'un organisateur de la Shoah, elle ne voit pas un monstre… mais un homme qui ne pense pas. »
  { a: ['r4b', 0], type: 'auteur', img: 'arendt', t: 'ARENDT', oeuvre: 'Eichmann à Jérusalem', date: '1963' },
  { a: ['r4b', 'au'], type: 'photo', img: 'eichmann', t: 'JÉRUSALEM|1961', sous: 'le procès d’Adolf Eichmann', nb: true, de: [1.05, .5, .4], vers: [1.2, .5, .35], legende: 'Adolf Eichmann à son procès, 1961 (Israel Government Press Office, domaine public)' },
  { a: ['r4b', 'mais'], type: 'penser' },
  // o1 « Alors, ton score ? Dis-le en commentaire. »
  { a: ['o1', 0], type: 'mot', t: 'ALORS,|TON SCORE ?', choc: true },
  { a: ['o1', 'dis-le'], type: 'score' },
  // o2 « Pascal et Arendt sont expliqués dans les séries philo de Révisions Animées. »
  { a: ['o2', 0], type: 'collage', imgs: ['pascal', 'arendt', 'pensees'], t: 'EXPLIQUÉS|EN VIDÉO' },
  { a: ['o2', 'séries'], type: 'chaine', serie: 'Philosophie', fond: 'nuit' },
  // o3 « Et toi… tu en as reconnu combien ? » (relance la question du début)
  { a: ['o3', 0], type: 'cases', fin: true, q: ['o3', 0] },
]);
window.CHAPITRES = ['ACCROCHE', 'CITATION 1', 'CITATION 2', 'CITATION 3', 'CITATION 4'];
window.IMAGES = {
  montaigne: '../../philo/serie/img/montaigne.jpg',    // portrait anonyme, musée Condé, domaine public
  rousseau: '../../philo/serie/img/rousseau.jpg',      // Maurice Quentin de La Tour, 1753, domaine public
  pascal: '../../philo/serie/img/pascal.jpg',          // copie d'après François II Quesnel, domaine public
  descartes: '../../philo/serie/img/descartes.jpg',    // d'après Frans Hals, domaine public
  kant: '../../philo/serie/img/kant.jpg',              // portrait anonyme, XVIIIe s., domaine public
  arendt: '../../philo/serie/img/arendt.jpg',          // photographie anonyme, 1933, domaine public
  sartre: '../../philo/serie/img/sartre.jpg',          // photographie de 1965, Nationaal Archief / Anefo, CC BY-SA 3.0 NL (attribution obligatoire)
  pensees: '../../philo/serie/img/bh1-pensees.jpg',    // Pascal, Pensées, manuscrit (BnF, Gallica), domaine public
  eichmann: '../../philo/serie/img/dv5-eichmann.jpg',  // Adolf Eichmann à son procès, Jérusalem, 1961, Israel Government Press Office, domaine public
  nuit: '../../philo/serie/img/t4-nuit-etoilee.jpg',   // Vincent van Gogh, La Nuit étoilée, 1889, domaine public
  // Wikimedia Commons, enregistrées dans outils/shorts/img/ le 27/11/2026 :
  proust: 'img/hlp-proust.jpg',             // Otto Wegener, Marcel Proust vers 1895, domaine public (File:Marcel_Proust_vers_1895.jpg)
  rimbaud: 'img/hlp-rimbaud.jpg',           // Étienne Carjat, Arthur Rimbaud, 1872, domaine public (File:Arthur_Rimbaud_by_Carjat_-_Musée_Arthur_Rimbaud_2.jpg)
  baudelaire: 'img/hlp-baudelaire.jpg',     // Étienne Carjat, Charles Baudelaire, vers 1862, domaine public (File:Charles_Baudelaire,_Étienne_Carjat,_P.P.1931.peg.jpg)
  verlaine: 'img/hlp-verlaine.jpg',         // Otto Wegener, Paul Verlaine de profil, domaine public (File:Profile_portrait_of_Paul_Verlaine_by_Otto_Wegener.jpg)
  coindetable: 'img/hlp-coindetable.jpg',   // Henri Fantin-Latour, Un coin de table, 1872, musée d'Orsay, domaine public (File:Henri_Fantin-Latour_-_By_the_Table_-_Google_Art_Project.jpg)
  tour: 'img/hlp-tour-montaigne.jpg',       // la tour de Montaigne, Saint-Michel-de-Montaigne, photo Henry Salomé, CC BY-SA 4.0 (File:St_Michel_de_Montaigne_Tour01.jpg)
};
window.MUSIQUE = 'funk_agressif';   // funk brésilien agressif (musique imposée)
window.THEME = 'jeu';               // plateau de jeu télé
