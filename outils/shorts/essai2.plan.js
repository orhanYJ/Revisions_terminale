// Essai des nouveaux plans (photo, collage, niveau, ordre, intrus, devine, plusmoins, erreur) ; jamais publié.
window.MUSIQUE = 'funk_agressif';
window.THEME = 'neon';
window.PLAN = S => S.plans([
  { a: ['p1', 0], type: 'photo', img: 'wall', t: '1929|LE KRACH', sous: 'Wall Street, octobre', ch: 0 },
  { a: ['p1', 'regarde'], type: 'collage', imgs: ['wall', 'soupe', 'dust'], t: 'LA GRANDE|DÉPRESSION' },
  { a: ['p2', 0], type: 'niveau', n: 1, total: 10, q: 'Qui a écrit|Du contrat social ?', chrono: ['p2', 'trois'], rep: ['p2', 'réponse'], r: 'ROUSSEAU', expl: '1762', ch: 1 },
  { a: ['p3', 0], type: 'ordre', cartes: [{ t: 'Krach de Wall Street', d: '1929' }, { t: 'Traité de Versailles', d: '1919' }, { t: 'New Deal', d: '1933' }, { t: 'Munich', d: '1938' }],
    ordre: [1, 0, 2, 3], chrono: ['p3', 'trois'], rep: ['p3', 'voilà'], ch: 2 },
  { a: ['p4', 0], type: 'intrus', options: [{ t: 'Kant', img: 'kant', nb: true }, { t: 'Sartre', img: 'sartre', nb: true }, { t: 'Napoléon', img: 'napoleon' }, { t: 'Platon', img: 'platon', nb: true }],
    intrus: 2, chrono: ['p4', 'trois'], rep: ['p4', "l'intrus"], expl: 'Un empereur, pas un philosophe' },
  { a: ['p5', 0], type: 'devine', img: 'kant', indices: [[['p5', 'indice'], 'Il est allemand'], [['p5', 'deux'], 'Trois « Critiques »'], [['p5', 'trois'], 'Réglé comme une horloge']],
    rep: ['p5', "c'est"], nom: 'KANT', sous: '1724 – 1804', ch: 3 },
  { a: ['p6', 0], type: 'plusmoins', q: 'CHÔMEURS AUX ÉTATS-UNIS', A: { t: 'En 1929', img: 'wall', v: 1500000 }, B: { t: 'En 1933', img: 'soupe', v: 12800000 }, chrono: ['p6', 'trois'], rep: ['p6', 'douze'] },
  { a: ['p7', 0], type: 'erreur', matiere: 'PHILOSOPHIE', sujet: 'Sommes-nous libres ?', lignes: ['Pour Descartes, la volonté est infinie.', 'Spinoza : les hommes se croient libres', 'car ils ignorent les causes.', 'Kant : « tu dois, donc tu ne peux pas ».', 'Sartre : l’existence précède l’essence.'],
    faute: 3, correction: '« tu dois, donc tu peux »', chrono: ['p7', 'trois'], rep: ['p7', 'voilà'], ch: 4 },
]);
window.CHAPITRES = ['A', 'B', 'C', 'D', 'E'];
window.IMAGES = {
  wall: '../../dnl/serie/img/h1-wallstreet.jpg', soupe: '../../dnl/serie/img/h1-soupkitchen.jpg', dust: '../../dnl/serie/img/h1-dustbowl.jpg',
  kant: '../../philo/serie/img/kant.jpg', sartre: '../../philo/serie/img/sartre.jpg', platon: '../../philo/serie/img/platon.jpg', napoleon: '../../philo/serie/img/t4-napoleon.jpg',
};
