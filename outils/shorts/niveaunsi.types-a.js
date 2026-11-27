// Plans propres au short « NSI : niveau 1 → 10 ». O = outils du modèle (carte, multi, tampon, barreRouge,
// petitTitre, fondImg, al, C = couleurs). Couleurs : uniquement O.C et O.al (l'habillage terminal les remplace).
// Les plans « niveau », « photo », « collage », « portrait » et « mot » sont communs (formats-a.js, modele-a.js).
// Code et requêtes en police à chasse fixe (JetBrains Mono, chargée par core.js).
window.SANS_ST_A = ['photo', 'collage', 'echelle', 'triche', 'bits', 'pile', 'sql', 'niveaucode', 'appels', 'dicho', 'commentaire'];
window.PROPRES_A = ['echelle', 'triche', 'bits', 'pile', 'sql', 'niveaucode', 'appels', 'dicho', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al, MONO = 'JetBrains Mono';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // texte à chasse fixe, aligné à gauche, dessiné caractère par caractère : pas de ligature (« == », « >>> » restent lisibles)
  const mono = (s, x, y, o = {}) => {
    const q = Object.assign({ taille: 48, police: MONO, poids: 500, coul: CREME }, o, { align: 'left', max: undefined });
    let adv = S.largeur('M', q);
    if (o.max && adv * s.length > o.max) { q.taille *= o.max / (adv * s.length); adv = S.largeur('M', q); }
    [...s].forEach((c, i) => { if (c !== ' ') S.texte(c, x + i * adv, y, q); });
  };
  // titre sur une ou deux lignes (« | »), la seconde en couleur vive
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const croix = (x, y, r, k) => { if (k <= 0) return; g.save(); g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round'; g.beginPath();
    g.moveTo(x - r, y - r); g.lineTo(x - r + 2 * r * cl(k * 2), y - r + 2 * r * cl(k * 2)); if (k > .5) { const k2 = cl(k * 2 - 1); g.moveTo(x + r, y - r); g.lineTo(x + r - 2 * r * k2, y - r + 2 * r * k2); } g.stroke(); g.restore(); };
  // fenêtre de terminal : cadre, barre de titre et trois pastilles
  function fenetre(x, y, w, h, titre) {
    g.save(); g.fillStyle = al(NOIR, .92); g.strokeStyle = OR; g.lineWidth = 5;
    g.beginPath(); g.roundRect(x, y, w, h, 22); g.fill(); g.stroke();
    g.fillStyle = al(OR, .16); g.beginPath(); g.roundRect(x, y, w, 70, [22, 22, 0, 0]); g.fill();
    [ROUGE, OR, CREME].forEach((c, i) => { g.fillStyle = c; g.beginPath(); g.arc(x + 45 + i * 44, y + 35, 13, 0, 7); g.fill(); });
    if (titre) S.texte(titre, x + w / 2, y + 36, { taille: 30, police: MONO, poids: 500, coul: GRIS });
    g.restore();
  }
  const espaces = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  // chrono rond (comme les formats communs), en couleurs de l'habillage
  function chrono(t, tc, tr, x, y, r = 95) {
    if (t < tc || t >= tr) return;
    const u = cl((t - tc) / Math.max(.6, tr - tc)), reste = Math.ceil(tr - t);
    g.save(); g.translate(x, y); g.strokeStyle = al(CREME, .2); g.lineWidth = r * .16; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
    g.strokeStyle = u > .7 ? ROUGE : OR; g.beginPath(); g.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
    S.texte(String(Math.max(0, reste)), 0, 4, { taille: r, coul: CREME }); g.restore();
  }

  // l'échelle des dix niveaux qui s'allument, un curseur qui grimpe et hésite
  function echelle(p, t) {
    const lt = t - p.a;
    for (let i = 0; i < 10; i++) {
      const y = 1130 - i * 74, k = back(pr(t, p.a + i * .06, .25)), on = lt > .3 + i * .09;
      const c = i < 3 ? CREME : i < 7 ? OR : ROUGE, w = 360 + i * 38;
      g.save(); g.translate(W / 2, y); g.scale(k, 1);
      g.fillStyle = on ? al(c, .9) : al(CREME, .1); g.beginPath(); g.roundRect(-w / 2, -26, w, 52, 14); g.fill(); g.restore();
      if (k > .5) S.texte(String(i + 1), W / 2 - w / 2 - 50, y, { taille: 44, coul: on ? c : GRIS, police: MONO, poids: 500 });
    }
    const n = lt < 1.1 ? lerp(0, 6, eo(cl(lt / 1.1))) : 7 + Math.sin((lt - 1.1) * 5) * .9, yc = 1130 - n * 74;
    g.save(); g.fillStyle = ROUGE; g.beginPath(); g.moveTo(W / 2 + 330, yc); g.lineTo(W / 2 + 390, yc - 34); g.lineTo(W / 2 + 390, yc + 34); g.closePath(); g.fill(); g.restore();
    S.texte('?', W / 2 + 440, yc, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 8 });
    titrePop('À QUEL NIVEAU|TU T’ARRÊTES ?', 1380, t, p.a, 104);
  }

  // pas de copier-coller : la commande barrée, tampon
  function triche(p, t) {
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 800); g.scale(k, k); g.translate(-W / 2, -800);
    fenetre(140, 560, 800, 480, 'terminal');
    mono('> copier', 200, 720, { taille: 64 });
    mono('> coller', 200, 820, { taille: 64 });
    mono('> demander à l’IA', 200, 920, { taille: 64, max: 700 });
    g.restore();
    croix(W / 2, 800, 230, pr(t, p.a + .2, .35));
    O.tampon('PAS DE TRICHE', W / 2, 1330, pr(t, p.a + .35, .3), -.08, 110, ROUGE);
  }

  // 13 en binaire : quatre cases de poids 8, 4, 2, 1
  function bits(p, t) {
    const B = [1, 1, 0, 1], P = [8, 4, 2, 1];
    O.petitTitre('— LE BINAIRE —', 420);
    B.forEach((b, i) => {
      const x = 225 + i * 210, y = 820, k = back(pr(t, p.a + i * .15, .3));
      S.texte(String(P[i]), x, 640, { taille: 60, coul: GRIS, police: MONO, poids: 500 });
      g.save(); g.translate(x, y); g.scale(k, k);
      g.fillStyle = b ? OR : al(CREME, .08); g.strokeStyle = b ? OR : al(CREME, .4); g.lineWidth = 6;
      g.beginPath(); g.roundRect(-85, -95, 170, 190, 20); g.fill(); g.stroke();
      S.texte(String(b), 0, 4, { taille: 130, coul: b ? NOIR : CREME, police: MONO, poids: 500 });
      g.restore();
    });
    const ks = eo(pr(t, p.a + .7, .4)); g.save(); g.globalAlpha = ks;
    S.texte('8 + 4 + 0 + 1 = 13', W / 2, 1060, { taille: 76, coul: CREME, police: MONO, poids: 500 }); g.restore();
    titrePop('13 EN BINAIRE|1101', 1380, t, p.a + .9, 120);
  }

  // pile (on dépile par le haut) puis file (on sort par l'avant)
  function pile(p, t) {
    const tf = tps(p.file), estFile = t >= tf, L = ['A', 'B', 'C'];
    const boite = (s, x, y, c, a = 1) => { g.save(); g.globalAlpha = a; g.fillStyle = al(c, .2); g.strokeStyle = c; g.lineWidth = 6;
      g.beginPath(); g.roundRect(x - 120, y - 70, 240, 140, 18); g.fill(); g.stroke(); S.texte(s, x, y + 4, { taille: 90, coul: c, police: MONO, poids: 500 }); g.restore(); };
    if (!estFile) {
      O.petitTitre('— LA PILE —', 420);
      g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 8; g.beginPath(); g.moveTo(370, 560); g.lineTo(370, 1180); g.lineTo(710, 1180); g.lineTo(710, 560); g.stroke(); g.restore();
      const ks = eo(pr(t, p.a + .3, .5));
      L.forEach((s, i) => { const y = 1095 - i * 165;
        if (i < 2) boite(s, 540, y, CREME);
        else boite(s, lerp(540, 850, ks), lerp(y, 760, ks), OR); });
      if (ks > .6) S.texte('SORT EN 1er', 850, 640, { taille: 46, coul: OR, poids: 700 });
      deux('DERNIER ENTRÉ|PREMIER SORTI', 1400, 104);
    } else {
      O.petitTitre('— LA FILE —', 420);
      const kf = eo(pr(t, tf + .15, .5));
      g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 8; g.beginPath(); g.moveTo(140, 700); g.lineTo(940, 700); g.moveTo(140, 960); g.lineTo(940, 960); g.stroke(); g.restore();
      L.forEach((s, i) => { const x = 300 + i * 260;
        if (i) boite(s, x, 830, CREME);
        else boite(s, lerp(x, -60, kf), 830, OR, 1 - kf * .3); });
      S.texte('◀ SORTIE', 230, 610, { taille: 44, coul: OR, poids: 700 });
      S.texte('ENTRÉE ◀', 860, 610, { taille: 44, coul: GRIS, poids: 700 });
      deux('PREMIER ENTRÉ|PREMIER SORTI', 1400, 104);
    }
  }

  // une table et une requête : WHERE garde seulement les lignes qui vérifient la condition
  function sql(p, t) {
    const k = eo(pr(t, p.a, .3)), kw = eo(pr(t, p.a + .5, .35));
    fenetre(90, 330, 900, 300, 'requête');
    mono('SELECT nom FROM eleves', 140, 470, { taille: 52 });
    const n = Math.floor(cl((t - p.a - .2) / .4) * 15);
    mono('WHERE note > 14'.slice(0, n), 140, 560, { taille: 52, coul: OR });
    const R = [['Alice', 17], ['Bob', 12], ['Chloé', 15], ['David', 9]];
    g.save(); g.globalAlpha = k;
    const x0 = 190, y0 = 740, cw = [420, 280], rh = 120;
    g.fillStyle = al(OR, .18); g.fillRect(x0, y0, 700, rh);
    mono('nom', x0 + 40, y0 + rh / 2, { taille: 50, coul: OR }); mono('note', x0 + cw[0] + 40, y0 + rh / 2, { taille: 50, coul: OR });
    R.forEach(([nom, note], i) => {
      const y = y0 + rh * (i + 1), ok = note > 14;
      g.globalAlpha = k * (kw > 0 && !ok ? lerp(1, .25, kw) : 1);
      if (ok && kw > 0) { g.fillStyle = al(OR, .25 * kw); g.fillRect(x0, y, 700, rh); }
      mono(nom, x0 + 40, y + rh / 2, { taille: 50 }); mono(String(note), x0 + cw[0] + 40, y + rh / 2, { taille: 50 });
      if (!ok && kw > 0) { g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath(); g.moveTo(x0 + 20, y + rh / 2); g.lineTo(x0 + 20 + 660 * kw, y + rh / 2); g.stroke(); }
    });
    g.globalAlpha = k; g.strokeStyle = al(CREME, .45); g.lineWidth = 3;
    for (let i = 0; i <= 5; i++) { g.beginPath(); g.moveTo(x0, y0 + i * rh); g.lineTo(x0 + 700, y0 + i * rh); g.stroke(); }
    g.beginPath(); g.moveTo(x0 + cw[0], y0); g.lineTo(x0 + cw[0], y0 + 5 * rh); g.stroke();
    g.restore();
    titrePop('WHERE|FILTRE LES LIGNES', 1530, t, p.a + .6, 100);
  }

  // niveau 6 : le code reste affiché pendant le chrono, puis la console répond
  function niveaucode(p, t) {
    const tr = tps(p.rep), tc = tps(p.chrono), avant = t < tr, k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 330); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k));
    S.texte('NIVEAU ' + p.n, 0, 0, { taille: 120, coul: OR, contour: NOIR, contourL: 12 }); g.restore();
    S.texte('DIFFICILE', W / 2, 430, { taille: 40, coul: OR, esp: 12, poids: 700 });
    for (let i = 0; i < 10; i++) {
      const x = W / 2 - 420 + i * 84 + 42, on = i < p.n, c = i < 3 ? CREME : i < 7 ? OR : ROUGE;
      const ki = i === p.n - 1 ? 1 + .25 * Math.abs(Math.sin(t * 8)) : 1;
      g.save(); g.translate(x, 500); g.scale(ki, ki); g.fillStyle = on ? c : al(CREME, .12); g.beginPath(); g.roundRect(-34, -14, 68, 28, 10); g.fill(); g.restore();
    }
    fenetre(80, 570, 920, 560, 'recursif.py');
    const C = [['def f(n):', 0], ['if n == 0:', 1], ['return 0', 2], ['return n + f(n - 1)', 1]];
    C.forEach(([s, ind], i) => {
      const ta = p.a + .25 + i * .3, n = Math.floor(cl((t - ta) / .35) * s.length);
      mono(s.slice(0, n), 130 + ind * 62, 700 + i * 82, { taille: 50, coul: i === 3 ? OR : CREME });
    });
    const kq = eo(pr(t, p.a + 1.6, .3)); g.save(); g.globalAlpha = kq;
    mono('>>> f(4)', 130, 1050, { taille: 54, coul: CREME });
    if (!avant) mono('10', 420, 1050, { taille: 54, coul: OR });
    else if (Math.floor(t * 3) % 2) { g.fillStyle = OR; g.fillRect(400, 1025, 26, 52); }
    g.restore();
    if (avant) {
      const kt = eo(pr(t, p.a + .3, .3)); g.save(); g.globalAlpha = kt;
      S.texte('Que renvoie f(4) ?', W / 2, 1230, { taille: 74, coul: CREME, contour: NOIR, contourL: 8 }); g.restore();
      chrono(t, tc, tr, W / 2, 1420, 100);
    } else {
      const kv = back(pr(t, tr, .3)); g.save(); g.translate(W / 2, 1260); g.scale(kv, kv);
      g.fillStyle = OR; g.beginPath(); g.roundRect(-430, -75, 860, 150, 22); g.fill();
      S.texte(p.r, 0, 4, { taille: 82, coul: NOIR, police: MONO, poids: 500 }); g.restore();
      const ke = eo(pr(t, tr + .3, .3)); g.save(); g.globalAlpha = ke;
      S.texte(p.expl, W / 2, 1420, { taille: 60, coul: CREME, police: MONO, poids: 500, max: 960 }); g.restore();
    }
  }

  // les appels qui s'empilent au rythme de la voix (« 4 plus 3 plus 2 plus 1 plus 0 »)
  function appels(p, t) {
    const L = ['f(4) = 4 + f(3)', 'f(3) = 3 + f(2)', 'f(2) = 2 + f(1)', 'f(1) = 1 + f(0)', 'f(0) = 0'];
    const quand = [p.a, S.T('r6', 3) - .1, S.T('r6', 5) - .1, S.T('r6', 7) - .1, S.T('r6', 9) - .1];
    O.petitTitre('— LES APPELS RÉCURSIFS —', 400);
    L.forEach((s, i) => {
      const ki = back(pr(t, quand[i], .25)); if (ki <= 0) return;
      const x = 150 + i * 40, y = 540 + i * 130, der = i === L.length - 1 || t < quand[i + 1];
      g.save(); g.globalAlpha = cl(ki); g.translate(lerp(-300, 0, ki), 0);
      g.fillStyle = der ? al(OR, .2) : al(CREME, .06); g.beginPath(); g.roundRect(x - 20, y - 52, 760, 104, 16); g.fill();
      mono(s, x + 10, y, { taille: 56, coul: der ? OR : CREME });
      g.restore();
    });
    const tl = S.T('r6', 10) - .1;
    if (t >= tl) titrePop('ELLE S’APPELLE|ELLE-MÊME', 1400, t, tl, 110);
    else { const ks = eo(pr(t, quand[1], .3)); g.save(); g.globalAlpha = ks;
      S.texte('4 + 3 + 2 + 1 + 0 = 10', W / 2, 1400, { taille: 80, coul: CREME, police: MONO, poids: 500, max: 960 }); g.restore(); }
  }

  // dichotomie : à chaque étape, il reste la moitié ; 20 étapes pour 1 million
  function dicho(p, t) {
    const ta = p.a + .3, n = Math.min(20, Math.max(0, Math.floor((t - ta) / .16) + 1)), reste = Math.ceil(1e6 / 2 ** n);
    O.petitTitre('— RECHERCHE DICHOTOMIQUE —', 400);
    // la barre de la liste et la partie restante (côté gauche ou droit au hasard)
    const x0 = 90, w = 900, y = 640;
    g.fillStyle = al(CREME, .1); g.fillRect(x0, y - 50, w, 100);
    let a = 0, b = 1;
    for (let i = 0; i < n; i++) { const m = (a + b) / 2; if (rnd(i * 7.3) < .5) b = m; else a = m; }
    const lw = Math.max(8, (b - a) * w);
    g.fillStyle = OR; g.fillRect(x0 + a * w - (lw - (b - a) * w) / 2, y - 50, lw, 100);
    g.strokeStyle = CREME; g.lineWidth = 4; g.strokeRect(x0, y - 50, w, 100);
    S.texte('ÉTAPE', W / 2, 840, { taille: 50, coul: GRIS, esp: 10, poids: 700 });
    S.texte(String(n), W / 2, 980, { taille: 200, coul: n >= 20 ? OR : CREME, police: MONO, poids: 500, contour: NOIR, contourL: 10 });
    S.texte('reste : ' + espaces(reste) + (reste > 1 ? ' éléments' : ' élément'), W / 2, 1140, { taille: 58, coul: CREME, police: MONO, poids: 500, max: 960 });
    const te = S.T('r8', 'et') - .1;
    if (t >= te) titrePop('2 PUISSANCE 20|= 1 048 576', 1400, t, te, 104);
    else titrePop('COUPER EN 2|À CHAQUE ÉTAPE', 1400, t, p.a, 104);
  }

  // une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .3)), txt = 'Mon niveau : … / 10', n = Math.floor(cl((t - p.a - .3) / .8) * txt.length);
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-300, 165); g.lineTo(-340, 260); g.lineTo(-220, 165); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-330, -60, 50, 0, 7); g.fill();
    S.texte('toi', -230, -60, { taille: 44, coul: GRIS, align: 'left', poids: 600 });
    S.texte(txt.slice(0, n), -360, 60, { taille: 66, police: MONO, poids: 500, coul: NOIR, align: 'left', max: 760 });
    const kc = pr(t, p.a + 1.2, .3); if (kc > 0) { g.save(); g.translate(350, -80); g.scale(back(kc), back(kc)); g.fillStyle = ROUGE;
      g.beginPath(); g.moveTo(0, 30); g.bezierCurveTo(-60, -10, -30, -60, 0, -30); g.bezierCurveTo(30, -60, 60, -10, 0, 30); g.fill(); g.restore(); }
    g.restore();
    deux('DIS TON NIVEAU|EN COMMENTAIRE', 1350, 110);
  }

  return { echelle, triche, bits, pile, sql, niveaucode, appels, dicho, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'echelle') { for (let i = 0; i < 10; i++) L.push([p.a + .3 + i * .09, 'tic', .3]); L.push([p.a, 'montee', .4]); }
  if (p.type === 'triche') L.push([p.a + .2, 'buzz', .5], [p.a + .35, 'tampon', .9]);
  if (p.type === 'bits') { for (let i = 0; i < 4; i++) L.push([p.a + i * .15, 'blip', .35]); L.push([p.a + .9, 'valide', .5]); }
  if (p.type === 'pile') L.push([p.a + .3, 'whoosh', .45], [tps(p.file) + .15, 'whoosh', .45]);
  if (p.type === 'sql') { for (let k = 0; k < 6; k++) L.push([p.a + .2 + k * .07, 'clic', .2]); L.push([p.a + .5, 'lame', .4]); }
  if (p.type === 'niveaucode') {
    const tr = tps(p.rep), tc = tps(p.chrono);
    L.push([p.a, 'montee', .5]); for (let k = 0; k < 10; k++) L.push([p.a + .25 + k * .12, 'clic', .18]);
    for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]);
    L.push([tr, 'valide', .9]);
  }
  if (p.type === 'appels') [p.a, S.T('r6', 3) - .1, S.T('r6', 5) - .1, S.T('r6', 7) - .1, S.T('r6', 9) - .1].forEach(x => L.push([x, 'pop', .4]));
  if (p.type === 'dicho') { for (let k = 0; k < 20; k += 2) L.push([p.a + .3 + k * .16, 'tic', .25]); L.push([p.a + .3 + 19 * .16, 'valide', .5]); }
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .3 + k * .1, 'tic', .25]); L.push([p.a + 1.2, 'pop', .5]); }
};
