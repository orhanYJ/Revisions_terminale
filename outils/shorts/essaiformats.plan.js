window.PLAN = S => S.plans([
  { a: ['s1', 0], av: .2, type: 'copie', matiere: 'PHILOSOPHIE', sujet: 'Peut-on être heureux|sans être libre ?', lignes: [
    [['s1', 'problématique'], 'Problématique :', 'titre'], [['s1', 'bonheur'], 'le bonheur dépend-il de nous ?', ''],
    [['s1', 'première'], 'I. On peut le croire', 'partie'], [['s1', 'deuxième'], 'II. Pourtant non', 'partie']], souligne: [['s1', 'deuxième'], 1] },
  { a: ['s2', 0], type: 'fiche', sur: 'RÉSUMÉ EXPRESS', t: 'LA CONSCIENCE', items: [
    [['s2', 'descartes'], 'Descartes', 'je pense, donc je suis'], [['s2', 'freud'], 'Freud', "l'inconscient"], [['s2', 'nietzsche'], 'Nietzsche', 'une surface']] },
  { a: ['s3', 0], type: 'vraifaux', n: '1 / 5', t: 'Tes mitochondries viennent|d’une bactérie', rep: ['s3', 'réponse'], v: true, expl: "C'est l'endosymbiose" },
  { a: ['s4', 0], type: 'quiz3', sur: 'QUI A DIT ÇA ?', n: '1 / 4', q: '« Le bonheur est un idéal|de l\u2019imagination »', options: [{t: 'Kant', img: 'kant', sous: '1724-1804'}, {t: 'Épicure', img: 'epicure'}, {t: 'Nietzsche', img: 'nietzsche'}], bonne: 0, chrono: ['s4', 'kant'], rep: ['s4', 'réponse'], expl: 'Fondements, 1785' },
]);
window.CHAPITRES = ['A', 'B', 'C'];
window.IMAGES = { kant: '../../philo/serie/img/kant.jpg', epicure: '../../philo/serie/img/epicure.jpg', nietzsche: '../../philo/serie/img/nietzsche.jpg' };
