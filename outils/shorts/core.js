// Moteur des shorts (TikTok / YouTube Shorts) : image 1080 × 1920 rendue en fonction pure du temps.
// short.html?c=<code>&m=<modèle> charge sortie/<code>.data.js (voix et temps des mots, voix.py),
// le découpage commun <code>.plan.js (plans calés sur les mots) et le style modele-<m>.js.
// Export : window.PRET (promesse), window.RENDU(t), window.DUR, window.SONS ([t, type, gain] pour mix.py).
(function () {
  const W = 1080, H = 1920;
  const cv = document.getElementById('c'), g = cv.getContext('2d');
  cv.width = W; cv.height = H;
  const D = window.SHORT;

  // ---------- temps des mots
  const seg = id => D.segs.find(s => s.id === id) || (() => { throw new Error('passage ' + id); })();
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
  // T('s3') début du passage ; T('s3', 4) mot n° 4 ; T('s3', 'horloge') premier mot qui commence ainsi ; T('s3', -1) dernier mot
  function T(id, k) {
    const s = seg(id);
    if (k === undefined) return s.t0;
    if (typeof k === 'number') return s.mots[(k + s.mots.length) % s.mots.length][0];
    const n = norm(k), m = s.mots.find(w => norm(w[2]).startsWith(n));
    if (!m) throw new Error(`mot « ${k} » absent de ${id}`);
    return m[0];
  }
  const Tfin = id => { const s = seg(id), m = s.mots[s.mots.length - 1]; return m[0] + m[1]; };
  const MOTS = D.segs.flatMap(s => s.mots.map(m => ({ t: m[0], d: m[1], w: m[2], s: s.id })));

  // ---------- outils
  const cl = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lerp = (a, b, k) => a + (b - a) * k;
  const pr = (t, a, d) => cl((t - a) / d);
  const eo = k => 1 - Math.pow(1 - k, 3);
  const eio = k => k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
  const back = k => { const c = 1.9; return 1 + (c + 1) * Math.pow(k - 1, 3) + c * Math.pow(k - 1, 2); };
  const elas = k => k === 0 || k === 1 ? k : Math.pow(2, -10 * k) * Math.sin((k * 10 - .75) * 2 * Math.PI / 3) + 1;
  function rnd(seed) { let x = Math.sin(seed * 12.9898) * 43758.5453; return x - Math.floor(x); }

  const IMGS = {};
  function img(nom) { return IMGS[nom]; }
  function chargerImg(nom, src) {
    return new Promise(r => { const i = new Image(); i.onload = () => { IMGS[nom] = i; r(); }; i.onerror = () => { console.error('image', src); r(); }; i.src = src; });
  }
  // image en « cover » dans un cadre, zoom z autour du point (fx, fy) de l'image (0..1)
  function cover(im, x, y, w, h, z = 1, fx = .5, fy = .5) {
    if (!im) return;
    const s = Math.max(w / im.width, h / im.height) * z;
    const iw = im.width * s, ih = im.height * s;
    const dx = x + w / 2 - fx * iw + (fx - .5) * 0, dy = y + h / 2 - fy * ih;
    g.save(); g.beginPath(); g.rect(x, y, w, h); g.clip();
    g.drawImage(im, cl(dx, x + w - iw, x), cl(dy, y + h - ih, y), iw, ih);
    g.restore();
  }
  function texte(s, x, y, o = {}) {
    g.save();
    g.font = `${o.it ? 'italic ' : ''}${o.poids || 700} ${o.taille || 80}px ${o.police || 'Archivo'}`;
    g.textAlign = o.align || 'center'; g.textBaseline = o.base || 'middle';
    if (o.esp) g.letterSpacing = o.esp + 'px';
    let sz = o.taille || 80;
    if (o.max) { const m = g.measureText(s).width; if (m > o.max) { sz *= o.max / m; g.font = `${o.it ? 'italic ' : ''}${o.poids || 700} ${sz}px ${o.police || 'Archivo'}`; } }
    if (o.ombre) { g.shadowColor = o.ombre; g.shadowBlur = o.flou || 30; }
    if (o.contour) { g.lineJoin = 'round'; g.lineWidth = o.contourL || sz * .12; g.strokeStyle = o.contour; g.strokeText(s, x, y); }
    g.fillStyle = o.coul || '#fff'; g.fillText(s, x, y);
    if (o.ombre2) { g.shadowColor = o.ombre2; g.shadowBlur = (o.flou || 30) * 2; g.fillText(s, x, y); }
    const w = g.measureText(s).width;
    g.restore();
    return { w, taille: sz };
  }
  function largeur(s, o = {}) {
    g.save(); g.font = `${o.it ? 'italic ' : ''}${o.poids || 700} ${o.taille || 80}px ${o.police || 'Archivo'}`;
    if (o.esp) g.letterSpacing = o.esp + 'px';
    const w = g.measureText(s).width; g.restore(); return w;
  }

  // ---------- sous-titres : groupes de 1 à 3 mots, coupés à la ponctuation (à la TikTok)
  const GROUPES = [];
  D.segs.forEach(s => {
    let cur = [];
    s.mots.forEach((m, i) => {
      cur.push(m);
      const ponct = /[.,:;?!…]$/.test(m[2]) || /[.,:;?!…]/.test((s.texte.split(m[2])[1] || '').trim()[0] || '');
      const lettres = cur.reduce((a, x) => a + x[2].length + 1, 0);
      if (ponct || cur.length >= 3 || lettres > 16 || i === s.mots.length - 1) { GROUPES.push({ s: s.id, mots: cur, t0: cur[0][0] }); cur = []; }
    });
  });
  GROUPES.forEach((gr, i) => { const n = GROUPES[i + 1]; const m = gr.mots[gr.mots.length - 1]; gr.t1 = Math.min(n ? n.t0 : 1e9, m[0] + m[1] + .35); });
  // ponctuation d'origine collée au mot (les mots de voix.py n'en ont pas)
  function avecPonct(sid, w, k) {
    const s = seg(sid); const re = new RegExp(w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '([.,:;?!…]*)', 'g');
    let m, n = 0; while ((m = re.exec(s.texte))) { if (n === k) return w + (m[1] || ''); n++; }
    return w;
  }
  const groupeA = t => GROUPES.find(gr => t >= gr.t0 && t < gr.t1);

  // ---------- plans (découpage commun) : [{a, type, ...}] trié ; le plan k dure jusqu'au suivant
  let PLANS = [];
  function plans(liste) { PLANS = liste.map(p => Object.assign({}, p, { a: Array.isArray(p.a) ? T(...p.a) - (p.av ?? .06) : p.a })).sort((x, y) => x.a - y.a); PLANS.forEach((p, i) => { p.i = i; p.b = i + 1 < PLANS.length ? PLANS[i + 1].a : D.dur; }); return PLANS; }
  const planA = t => { let r = PLANS[0]; for (const p of PLANS) if (p.a <= t) r = p; return r; };

  const CLES = new Set(['cerveau', 'marche', '1983', 'libet', 'experience', 'poignet', 'veux', 'horloge', 'linstant', 'electrodes',
    'resultat', 'demiseconde', 'geste', 'deux', 'dixiemes', 'trois', 'sans', 'toi', 'spinoza', 'pierre', 'penser', 'vole', 'veut',
    'pareils', 'libre', 'ignore', 'causes', 'illusion', 'vite', 'pouvoir', 'non', 'veto', 'bruit', 'fond', 'bac', 'revisions', 'animees',
    'decides', 'sur', 'avant', 'signal']);
  const cle = w => CLES.has(norm(w));
  // coup de zoom sur le dernier mot clé dit : 0 → 1 → 0 en d secondes
  const coup = (t, d = .2) => { let r = 0; for (const m of MOTS) { if (m.t > t) break; if (cle(m.w)) r = 1 - pr(t, m.t, d); } return r; };
  // structure pour la musique : début de chaque chapitre, instants des chocs
  const structure = () => ({ sections: PLANS.filter(p => p.ch !== undefined).map(p => [p.a, p.ch]), chocs: PLANS.filter(p => p.choc).map(p => p.a) });
  const S = { structure, cle, coup, W, H, g, D, T, Tfin, MOTS, GROUPES, groupeA, avecPonct, seg, cl, lerp, pr, eo, eio, back, elas, rnd, img, cover, texte, largeur, plans, planA, get PLANS() { return PLANS; } };
  window.S = S;

  window.SHORT_LANCER = function (modele) {
    const sources = Object.assign({}, modele.images || {});
    window.DUR = D.dur;
    window.PRET = Promise.all([document.fonts.ready, ...Object.entries(sources).map(([n, s]) => chargerImg(n, s)),
      ...['700 80px Archivo', '600 80px Archivo', 'italic 400 80px Spectral', '600 80px Spectral', '500 40px "JetBrains Mono"'].map(f => document.fonts.load(f))])
      .then(() => { modele.init && modele.init(S); window.SONS = modele.sons(S); return true; });
    window.RENDU = t => { g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1; g.filter = 'none'; modele.rendu(t, S); };
    // aperçu dans un navigateur : lecture avec la piste mixée si elle existe
    const q = new URLSearchParams(location.search);
    if (!q.has('export')) window.PRET.then(() => {
      const au = new Audio(`sortie/${D.code}-${q.get('m')}.mix.wav`);
      let t0 = null;
      const tick = () => { const t = au.paused ? (t0 ?? 0) : au.currentTime; window.RENDU(Math.min(t, D.dur - .001)); requestAnimationFrame(tick); };
      cv.onclick = () => au.paused ? au.play() : au.pause();
      if (q.has('t')) t0 = +q.get('t'), au.currentTime = t0;
      tick();
    });
  };
})();
