// Découpage du short « quidit » (format 5, « Qui a dit ça ? » : quatre citations, trois auteurs), modèle A.
// a: [passage, mot] ; av : avance sur le mot. Pour chaque citation : numéro, citation dite (en deux temps si elle est
// longue), plan `quiz3` (chrono dans le silence qui suit la question, verdict sur « Réponse »), l'auteur, une image du sens.
const Q = { type: 'quiz3', sur: 'QUI A DIT ÇA ?' };
const quiz = o => Object.assign({}, Q, o);
const C1 = '« L’homme est condamné|à être libre. »';
const C2 = '« Le bonheur est un idéal,|non de la raison,|mais de l’imagination. »';
const C3 = '« L’homme n’est qu’un roseau,|le plus faible de la nature ;|mais c’est un roseau pensant. »';
const C4 = '« L’homme est né libre,|et partout|il est dans les fers. »';
window.PLAN = S => S.plans([
  // h1 « 4 citations. Combien tu en reconnais ? »
  { a: ['h1', 0], av: .2, type: 'cases', ch: 0, q: ['h1', 'combien'] },
  // h2 « Pour chacune, trois auteurs. Un seul l'a écrite. »
  { a: ['h2', 0], type: 'trois', un: ['h2', 'un'] },
  // q1 « Citation 1 : « L'homme est condamné à être libre. » Descartes, Spinoza… ou Sartre ? »
  { a: ['q1', 0], type: 'num', n: 1, ch: 1 },
  { a: ['q1', "l'homme"], type: 'citation', n: 1, q: C1 },
  quiz({ a: ['q1', 'descartes'], n: '1 / 4', q: C1, chrono: ['q1', 'descartes'], rep: ['r1a', 'réponse'], bonne: 2, expl: 'L’existentialisme est un humanisme, 1946',
    options: [{ t: 'Descartes', img: 'descartes', sous: '1596 – 1650' }, { t: 'Spinoza', img: 'spinoza', sous: '1632 – 1677' }, { t: 'Sartre', img: 'sartre', sous: '1905 – 1980' }] }),
  // r1a « Réponse : Sartre ! » r1b « L'existentialisme est un humanisme, 1946. Même ne pas choisir, c'est encore choisir. »
  { a: ['r1b', 0], type: 'auteur', img: 'sartre', t: 'SARTRE', oeuvre: 'L’existentialisme est un humanisme', date: '1946' },
  { a: ['r1b', 'même'], type: 'choix', encore: ['r1b', 'encore'] },
  // q2 « Citation 2 : « Le bonheur est un idéal, non de la raison, mais de l'imagination. » Épicure, Kant… ou Aristote ? »
  { a: ['q2', 0], type: 'num', n: 2, ch: 2 },
  { a: ['q2', 'le'], type: 'citation', n: 2, q: C2, jusqua: 2 },
  { a: ['q2', 'mais'], type: 'citation', n: 2, q: C2, deja: 2 },
  quiz({ a: ['q2', 'épicure'], n: '2 / 4', q: C2, chrono: ['q2', 'épicure'], rep: ['r2a', 'réponse'], bonne: 1, expl: 'Fondements de la métaphysique des mœurs, 1785',
    options: [{ t: 'Épicure', img: 'epicure', sous: '341 – 270 av. J.-C.' }, { t: 'Kant', img: 'kant', sous: '1724 – 1804' }, { t: 'Aristote', img: 'aristote', sous: '384 – 322 av. J.-C.' }] }),
  // r2b « Fondements de la métaphysique des mœurs, 1785. Tout le monde veut être heureux… mais personne ne sait dire ce qu'il veut. »
  { a: ['r2b', 0], type: 'auteur', img: 'kant', t: 'KANT', oeuvre: 'Fondements de la métaphysique des mœurs', date: '1785' },
  { a: ['r2b', 'tout'], type: 'nuage', etape: 1 },
  { a: ['r2b', 'personne'], type: 'nuage', etape: 2 },
  // q3 « Citation 3 : « L'homme n'est qu'un roseau, le plus faible de la nature ; mais c'est un roseau pensant. » Pascal, Descartes… ou Montaigne ? »
  { a: ['q3', 0], type: 'num', n: 3, ch: 3 },
  { a: ['q3', "l'homme"], type: 'citation', n: 3, q: C3, jusqua: 2 },
  { a: ['q3', 'mais'], type: 'citation', n: 3, q: C3, deja: 2 },
  quiz({ a: ['q3', 'pascal'], n: '3 / 4', q: C3, chrono: ['q3', 'pascal'], rep: ['r3a', 'réponse'], bonne: 0, expl: 'Pensées, publiées en 1670',
    options: [{ t: 'Pascal', img: 'pascal', sous: '1623 – 1662' }, { t: 'Descartes', img: 'descartes', sous: '1596 – 1650' }, { t: 'Montaigne', img: 'montaigne', sous: '1533 – 1592' }] }),
  // r3b « Les Pensées, publiées en 1670. L'univers peut l'écraser, mais l'homme, lui, sait qu'il meurt. »
  { a: ['r3b', 0], type: 'auteur', img: 'pascal', t: 'PASCAL', oeuvre: 'Pensées (publiées après sa mort)', date: '1670' },
  { a: ['r3b', "l'univers"], type: 'roseau', sait: ['r3b', 'sait'] },
  // q4 « Dernière citation : « L'homme est né libre, et partout il est dans les fers. » Hobbes, Rousseau… ou Locke ? »
  { a: ['q4', 0], type: 'num', n: 4, t: 'DERNIÈRE', ch: 4, choc: true },
  { a: ['q4', "l'homme"], type: 'citation', n: 4, q: C4, jusqua: 1 },
  { a: ['q4', 'partout'], type: 'citation', n: 4, q: C4, deja: 1 },
  quiz({ a: ['q4', 'hobbes'], n: '4 / 4', q: C4, chrono: ['q4', 'hobbes'], rep: ['r4a', 'réponse'], bonne: 1, expl: 'Du contrat social, I, 1, 1762',
    options: [{ t: 'Hobbes', img: 'hobbes', sous: '1588 – 1679' }, { t: 'Rousseau', img: 'rousseau', sous: '1712 – 1778' }, { t: 'Locke', img: 'locke', sous: '1632 – 1704' }] }),
  // r4b « Du contrat social, 1762. Sa question : quelle société ne serait pas une prison ? »
  { a: ['r4b', 0], type: 'auteur', img: 'rousseau', t: 'ROUSSEAU', oeuvre: 'Du contrat social', date: '1762' },
  { a: ['r4b', 'sa'], type: 'prison', barreaux: ['r4b', 'prison'] },
  // o1 « Alors, ton score ? Dis-le en commentaire. »
  { a: ['o1', 0], type: 'mot', t: 'ALORS,|TON SCORE ?', choc: true },
  { a: ['o1', 'dis-le'], type: 'score' },
  // o2 « Les 4 auteurs sont expliqués en détail dans les séries de Révisions Animées. »
  { a: ['o2', 0], type: 'quatre' },
  { a: ['o2', 'séries'], type: 'chaine', serie: 'Philosophie', fond: 'nuit' },
  // o3 « Et toi… tu en as reconnu combien ? » (relance la question du début)
  { a: ['o3', 0], type: 'cases', fin: true, q: ['o3', 0] },
]);
window.CHAPITRES = ['ACCROCHE', 'CITATION 1', 'CITATION 2', 'CITATION 3', 'CITATION 4'];
window.IMAGES = {
  sartre: '../../philo/serie/img/sartre.jpg',          // photographie de 1965, Nationaal Archief / Anefo, CC BY-SA 3.0 NL (attribution obligatoire)
  descartes: '../../philo/serie/img/descartes.jpg',    // d'après Frans Hals, domaine public
  spinoza: '../../philo/serie/img/spinoza.jpg',        // portrait anonyme, vers 1665, domaine public
  epicure: '../../philo/serie/img/epicure.jpg',        // buste antique, domaine public
  kant: '../../philo/serie/img/kant.jpg',              // portrait anonyme, XVIIIe s., domaine public
  aristote: '../../philo/serie/img/aristote.jpg',      // buste, Rome, Palazzo Altemps, photographie Jastrow, domaine public
  pascal: '../../philo/serie/img/pascal.jpg',          // copie d'après François II Quesnel, domaine public
  montaigne: '../../philo/serie/img/montaigne.jpg',    // portrait anonyme, musée Condé, domaine public
  hobbes: '../../philo/serie/img/hobbes.jpg',          // John Michael Wright, vers 1669-1670, domaine public
  rousseau: '../../philo/serie/img/rousseau.jpg',      // Maurice Quentin de La Tour, 1753, domaine public
  locke: '../../philo/serie/img/locke.jpg',            // Godfrey Kneller, 1697, domaine public
  chemins: '../../philo/serie/img/t2-chemins.jpg',     // un chemin qui se divise, photo Alec MacKinnon, CC BY-SA 2.0
  jeunesse: '../../philo/serie/img/bh1-jeunesse.jpg',  // Thomas Cole, Le Voyage de la vie : la jeunesse, 1840-1842, domaine public
  roseaux: '../../philo/serie/img/cs5-roseaux.jpg',    // roseaux au bord d'un lac, photo Joshua Mayer, CC BY-SA 2.0
  nuit: '../../philo/serie/img/t4-nuit-etoilee.jpg',   // Vincent van Gogh, La Nuit étoilée, 1889, domaine public
  carceri: '../../philo/serie/img/t-carceri.jpg',      // Piranèse, Prisons imaginaires, planche XVI, 1761, domaine public
};
window.MUSIQUE = 'chiptune';   // musique imposée pour ce short (format 5, quiz)
