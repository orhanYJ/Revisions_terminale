window.PLAN = S => S.plans([
  { a: ['s1', 0], av: .2, type: 'copie', matiere: 'PHILOSOPHIE', sujet: 'Peut-on être heureux|sans être libre ?', lignes: [
    [['s1', 'problématique'], 'Problématique :', 'titre'], [['s1', 'bonheur'], 'le bonheur dépend-il de nous ?', ''],
    [['s1', 'première'], 'I. On peut le croire', 'partie'], [['s1', 'deuxième'], 'II. Pourtant non', 'partie']], souligne: [['s1', 'deuxième'], 1] },
  { a: ['s2', 0], type: 'fiche', sur: 'RÉSUMÉ EXPRESS', t: 'LA CONSCIENCE', items: [
    [['s2', 'descartes'], 'Descartes', 'je pense, donc je suis'], [['s2', 'freud'], 'Freud', "l'inconscient"], [['s2', 'nietzsche'], 'Nietzsche', 'une surface']] },
  { a: ['s3', 0], type: 'vraifaux', n: '1 / 5', t: 'Tes mitochondries viennent|d’une bactérie', rep: ['s3', 'réponse'], v: true, expl: "C'est l'endosymbiose" },
]);
window.CHAPITRES = ['A', 'B', 'C'];
window.IMAGES = {};
