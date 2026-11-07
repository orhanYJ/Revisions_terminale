// Modèle C « Typo choc » : le texte lu EST l'image. Chaque mot claque à l'instant où il est dit, les mots clés
// sont géants ; couleurs de fond qui s'inversent à chaque plan, secousses, tranches qui glissent, gros sons.
(function () {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const NOIR = '#0b0b0b', BLANC = '#f6f3ec', JAUNE = '#ffe14a', ROUGE = '#ec2b2b';
  const SCHEMAS = [
    { bg: NOIR, fg: BLANC, acc: JAUNE }, { bg: JAUNE, fg: NOIR, acc: ROUGE }, { bg: BLANC, fg: NOIR, acc: ROUGE },
    { bg: NOIR, fg: BLANC, acc: ROUGE }, { bg: ROUGE, fg: BLANC, acc: JAUNE },
  ];
  const CLES = new Set(['cerveau', 'marche', '1983', 'libet', 'experience', 'poignet', 'veux', 'horloge', 'instant', 'electrodes',
    'resultat', 'demiseconde', 'geste', 'deux', 'dixiemes', 'trois', 'sans', 'toi', 'spinoza', 'pierre', 'penser', 'vole', 'veut',
    'pareils', 'libre', 'ignore', 'causes', 'illusion', 'vite', 'pouvoir', 'non', 'veto', 'bruit', 'fond', 'bac', 'revisions', 'animees',
    'decides', 'sur', 'avant', 'signal']);
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
  const cv = document.getElementById('c');

  function schema(p) {
    if (p.choc) return SCHEMAS[4];
    if (p.sombre || p.bruit) return SCHEMAS[3];
    return SCHEMAS[[0, 1, 0, 2, 0, 1, 3, 2][p.i % 8]];
  }

  // mots dits pendant le plan, disposés en lignes (mise en page calculée une fois par plan)
  const MISE = new Map();
  function mise(p) {
    if (MISE.has(p.i)) return MISE.get(p.i);
    const mots = S.MOTS.filter(m => m.t >= p.a - .02 && m.t < p.b - .02);
    const lignes = []; let cur = [], larg = 0;
    mots.forEach(m => {
      const cle = CLES.has(norm(m.w)), taille = cle ? 200 : 104, s = m.w.toUpperCase();
      const w = S.largeur(s, { taille }) * (cle ? 1 : 1);
      if (cle || larg + w > 900 || cur.some(x => x.cle)) { if (cur.length) lignes.push(cur); cur = []; larg = 0; }
      cur.push({ m, s, taille, w, cle }); larg += w + 30;
    });
    if (cur.length) lignes.push(cur);
    lignes.forEach(L => { const tot = L.reduce((a, x) => a + x.w, 0) + 30 * (L.length - 1), k = Math.min(1, 960 / tot); L.forEach(x => { x.taille *= k; x.w *= k; }); L.k = k; L.h = Math.max(...L.map(x => x.taille)) * 1.02; });
    MISE.set(p.i, lignes); return lignes;
  }

  // petite icône au-dessus du texte
  const ICONES = {
    cerveau: (p, t, c) => S.d.cerveau(540, 600, 220, { trait: c.fg, fond: c.acc, ep: 12 }),
    tampon: (p, t, c) => S.d.cerveau(540, 600, 200, { trait: c.fg, ep: 12 }),
    poignet: (p, t, c) => S.d.main(620, 600, Math.max(0, Math.sin((t - p.a) * 3.2)) * .75, { trait: c.fg, fond: c.acc, ep: 10 }, 1),
    horloge: (p, t, c) => { const b = S.T('s3', 'horloge') - .06, a = ((p.fige ? p.a - b + Math.min(t - p.a, .25) : t - b) / 2.56) * 6.283;
      S.d.horloge(540, 600, 260, a, { trait: c.fg, ep: 10, point: c.acc, marque: c.acc }, p.fige ? a : undefined); },
    eeg: (p, t, c) => S.d.eeg(80, 1000, 600, t, 120, { trait: c.acc === JAUNE ? c.fg : c.acc, ep: 9 }, { bruit: p.bruit }),
    pierre: (p, t, c) => { if (p.etape === 1) { const k = cl((t - p.a) / 1.4); S.d.pierre(lerp(160, 920, k), 720 - Math.sin(k * Math.PI) * 330, 70, k * 9, { trait: c.fg, fond: c.acc, ep: 10 }); }
      else S.d.pierre(540, 600, 130, .3, { trait: c.fg, fond: c.acc, ep: 12 }); },
    causes: (p, t, c) => { S.d.tete(640, 600, 200, { trait: c.fg, ep: 10 }); [520, 600, 680].forEach((y, i) => S.d.fleche(140, y, 420, y, eo(pr(t, p.a + i * .12, .3)), { trait: c.acc, ep: 14 })); },
    poignet2: null,
    perso: (p, t, c) => { S.d.tete(540, 600, 210, { trait: c.fg, ep: 10 }); S.texte('?', 560, 560, { taille: 150, coul: c.acc }); },
    chaine: (p, t, c) => { const k = back(pr(t, p.a, .3)); g.save(); g.translate(540, 600); g.scale(k, k); S.d.lecture(0, 0, 130, BLANC, ROUGE); g.restore(); },
    bac: (p, t, c) => { g.save(); g.translate(540, 600); g.rotate(-.05); g.fillStyle = c.fg; g.fillRect(-200, -260, 400, 520); g.fillStyle = c.bg;
      S.texte('BAC', 0, -170, { taille: 90, coul: c.bg }); for (let i = 0; i < 6; i++) g.fillRect(-150, -60 + i * 50, 300 - (i === 5 ? 120 : 0), 14); g.restore(); },
    portrait: (p, t, c) => { const im = S.img(p.img); if (!im) return; const k = back(pr(t, p.a, .3));
      g.save(); g.translate(540, 620); g.scale(k, k); g.filter = 'grayscale(1) contrast(2.6) brightness(1.05)';
      g.beginPath(); g.arc(0, 0, 280, 0, 7); g.clip(); S.cover(im, -280, -280, 560, 560, 1.2, .5, .3); g.filter = 'none';
      g.globalCompositeOperation = 'multiply'; g.fillStyle = c.acc; g.fillRect(-280, -280, 560, 560); g.restore();
      g.save(); g.strokeStyle = c.fg; g.lineWidth = 12; g.beginPath(); g.arc(540, 620, 280 * k, 0, 7); g.stroke(); g.restore(); },
  };

  // chiffres géants de la frise
  function frise(p, t, c) {
    const k = eo(pr(t, p.a, .4)), e = p.etape;
    const gros = e === 1 ? '−0,5 s' : e === 2 ? '−0,2 s' : e === 3 ? (lerp(0, .3, k)).toFixed(1).replace('.', ',') + ' s' : e === 4 ? '−0,2 → 0' : 'VETO';
    const kk = back(pr(t, p.a, .25));
    g.save(); g.translate(540, 620); g.scale(lerp(1.8, 1, kk), lerp(1.8, 1, kk));
    S.texte(gros, 0, 0, { taille: e === 4 ? 170 : 250, coul: e === 5 ? c.acc : c.fg, max: 980 }); g.restore();
    // jauge
    const x = s => lerp(120, 960, (s + .6) / .7);
    g.save(); g.fillStyle = c.fg; g.fillRect(100, 820, 880, 10);
    [[0, c.fg], [-.5, c.acc], ...(e >= 2 ? [[-.2, c.fg]] : [])].forEach(([s, col]) => { g.fillStyle = col; g.fillRect(x(s) - 8, 790, 16, 70); });
    if (e === 3) { g.fillStyle = c.acc; g.fillRect(x(-.5), 800, (x(-.2) - x(-.5)) * k, 50); }
    if (e >= 4) { g.fillStyle = c.acc; g.fillRect(x(-.2), 800, (x(0) - x(-.2)) * (e === 4 ? k : 1), 50); }
    g.restore();
  }

  function rendu(t) {
    const p = S.planA(t), c = schema(p), l = t - p.a;
    g.fillStyle = c.bg; g.fillRect(0, 0, W, H);
    // dernier mot apparu → petit coup de zoom
    const dern = S.MOTS.filter(m => m.t <= t).pop(), dz = dern ? 1 - pr(t, dern.t, .14) : 0;
    const z = 1 + dz * .035 + l * .008;
    let sx = 0, sy = 0; const choc = p.choc ? 1 : dern && CLES.has(norm(dern.w)) ? .5 : 0;
    if (choc && dz > 0) { const a = dz * 26 * choc; sx = (rnd(t * 97) - .5) * a; sy = (rnd(t * 61) - .5) * a; }
    g.save(); g.translate(W / 2 + sx, H / 2 + sy); g.scale(z, z); g.translate(-W / 2, -H / 2);
    // motif de fond : grosses bandes obliques qui défilent
    g.save(); g.globalAlpha = .07; g.fillStyle = c.fg; g.translate(W / 2, H / 2); g.rotate(-.35);
    for (let i = -12; i < 12; i++) g.fillRect(-1600, i * 160 + ((t * 120) % 160), 3200, 50); g.restore();
    // icône
    if (p.type === 'frise') frise(p, t, c);
    else if (ICONES[p.type]) ICONES[p.type](p, t, c);
    // texte
    const L = mise(p), tot = L.reduce((a, x) => a + x.h, 0);
    let y = (p.type === 'mot' || p.type === 'stop' || p.type === 'tampon' || p.type === 'date') ? 960 - tot / 2 : 1000;
    // si le texte déborde (plan long), on fait glisser vers le haut
    const bas = y + tot, lim = 1560; if (bas > lim) { const vis = L.filter(Lg => Lg[0].m.t <= t); const hv = vis.reduce((a, x) => a + x.h, 0); y -= Math.max(0, y + hv - lim); }
    L.forEach(Lg => {
      const tot2 = Lg.reduce((a, x) => a + x.w, 0) + 30 * (Lg.length - 1); let x = W / 2 - tot2 / 2;
      Lg.forEach(o => {
        const k = pr(t, o.m.t - .03, .16);
        if (k > 0) {
          const s = o.cle ? lerp(1.9, 1, back(k)) : lerp(1.35, 1, eo(k)), cx = x + o.w / 2, cy = y + Lg.h / 2;
          g.save(); g.translate(cx, cy); g.scale(s, s); g.rotate(o.cle ? (rnd(o.m.t) - .5) * .08 : 0);
          if (o.cle && c.acc !== c.bg) { g.fillStyle = c.acc; const pad = 14; g.fillRect(-o.w / 2 - pad, -o.taille * .47, o.w + 2 * pad, o.taille * .9); }
          S.texte(o.s, 0, 0, { taille: o.taille, coul: o.cle ? (c.acc === JAUNE || c.acc === BLANC ? NOIR : c.bg === ROUGE ? NOIR : BLANC) : c.fg });
          g.restore();
        }
        x += o.w + 30;
      });
      y += Lg.h;
    });
    g.restore();
    // à l'entrée du plan : tranches qui glissent + éclair inversé
    if (l < .12) {
      const k = 1 - l / .12;
      for (let i = 0; i < 7; i++) { const yy = rnd(i + p.i * 13) * H, hh = 40 + rnd(i * 5 + p.i) * 160, dx = (rnd(i * 3 + p.i * 7) - .5) * 260 * k;
        g.drawImage(cv, 0, yy, W, hh, dx, yy, W, hh); }
      if (l < .045) { g.fillStyle = c.fg; g.globalAlpha = .85; g.fillRect(0, 0, W, H); g.globalAlpha = 1; }
    }
    if (p.bruit) for (let i = 0; i < 30; i++) { g.fillStyle = i % 2 ? c.fg : c.acc; g.globalAlpha = .4; g.fillRect(0, rnd(i + Math.floor(t * 25) * 7) * H, W, 3 + rnd(i) * 8); g.globalAlpha = 1; }
    S.texte('@RÉVISIONS ANIMÉES', W / 2, 150, { taille: 30, coul: c.fg, esp: 8, poids: 600 });
    if (t > S.D.dur - .2) { g.fillStyle = `rgba(0,0,0,${pr(t, S.D.dur - .2, .2)})`; g.fillRect(0, 0, W, H); }
  }

  function sons() {
    const L = [];
    S.PLANS.forEach(p => {
      L.push([p.a, p.choc ? 'drop' : 'coupe', p.choc ? 1 : .7]);
      if (p.choc) L.push([p.a - .5, 'aspire', .7]);
      if (p.type === 'stop') L.push([p.a, 'disque', 1]);
      if (p.type === 'horloge' && !p.fige) for (let k = 0; k < Math.floor((p.b - p.a) / .25); k++) L.push([p.a + k * .25, 'tic', .4]);
      if (p.bruit) L.push([p.a, 'statique', .6]);
      if (p.type === 'chaine') L.push([p.a, 'valide', .9]);
    });
    // un petit coup sur chaque mot clé
    S.MOTS.forEach(m => { if (CLES.has(norm(m.w))) L.push([m.t - .01, 'frappe', .55]); });
    return { sons: L, musique: 'beat', bpm: 128 };
  }

  window.MODELE = { images: window.IMAGES, rendu, sons };
})();
