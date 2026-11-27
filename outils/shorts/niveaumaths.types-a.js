// Plans propres au short « Maths : niveau 1 → 10 ». O = outils du modèle (carte, multi, tampon, barreRouge,
// petitTitre, fondImg, al, C = couleurs). Couleurs : uniquement O.C et O.al (l'habillage néon les remplace).
// Les plans « niveau », « photo », « collage », « portrait » et « mot » sont communs (formats-a.js, modele-a.js).
// Formules : seulement des caractères présents dans Archivo et Spectral (², ³, ×, −, ″ ; pas de →, ≈, ∞, ∫).
window.SANS_ST_A = ['photo', 'collage', 'nocalc', 'echelle', 'suite', 'convexe', 'limite', 'puissance', 'aire', 'poignees', 'arbre', 'commentaire'];
window.PROPRES_A = ['nocalc', 'echelle', 'suite', 'convexe', 'limite', 'puissance', 'aire', 'poignees', 'arbre', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  // titre sur une ou deux lignes (« | »), la seconde en couleur vive
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const ligne = (x0, y0, x1, y1, c, ep = 6, tirets) => { g.save(); g.strokeStyle = c; g.lineWidth = ep; g.lineCap = 'round'; if (tirets) g.setLineDash(tirets);
    g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); g.restore(); };
  const croix = (x, y, r, k) => { if (k <= 0) return; g.save(); g.strokeStyle = ROUGE; g.lineWidth = 22; g.lineCap = 'round'; g.beginPath();
    g.moveTo(x - r, y - r); g.lineTo(x - r + 2 * r * cl(k * 2), y - r + 2 * r * cl(k * 2)); if (k > .5) { const k2 = cl(k * 2 - 1); g.moveTo(x + r, y - r); g.lineTo(x + r - 2 * r * k2, y - r + 2 * r * k2); } g.stroke(); g.restore(); };
  const formule = (s, x, y, taille, coul = CREME, o = {}) => S.texte(s, x, y, Object.assign({ taille, coul, police: 'Spectral', poids: 600, max: 980 }, o));
  const pop = (t, a, d = .3) => back(pr(t, a, d));
  // repère d'axes : origine (ox, oy), longueurs L et Hh, noms des axes
  const axes = (ox, oy, L, Hh, nx, ny) => {
    ligne(ox - 20, oy, ox + L, oy, CREME, 6); ligne(ox, oy + 20, ox, oy - Hh, CREME, 6);
    g.save(); g.fillStyle = CREME; g.beginPath(); g.moveTo(ox + L + 26, oy); g.lineTo(ox + L, oy - 14); g.lineTo(ox + L, oy + 14); g.fill();
    g.beginPath(); g.moveTo(ox, oy - Hh - 26); g.lineTo(ox - 14, oy - Hh); g.lineTo(ox + 14, oy - Hh); g.fill(); g.restore();
    if (nx) S.texte(nx, ox + L + 40, oy + 50, { taille: 54, coul: CREME, police: 'Spectral', it: true, poids: 500 });
    if (ny) S.texte(ny, ox - 50, oy - Hh - 20, { taille: 54, coul: CREME, police: 'Spectral', it: true, poids: 500 });
  };

  // la calculatrice barrée, tampon « DE TÊTE »
  function nocalc(p, t) {
    const k = eo(pr(t, p.a, .3));
    O.petitTitre('PAS DE CALCULATRICE', 400);
    O.carte(p.img, W / 2, 840, 520, 640, lerp(.12, -.04, k), 1.1, .5, .45);
    croix(W / 2, 840, 230, pr(t, p.a + .2, .35));
    O.tampon('DE TÊTE', W / 2, 1380, pr(t, p.a + .45, .3), -.08, 140, ROUGE);
  }

  // l'échelle des dix niveaux qui s'allument, un curseur qui grimpe et hésite
  function echelle(p, t) {
    const lt = t - p.a;
    for (let i = 0; i < 10; i++) {
      const y = 1130 - i * 74, k = back(pr(t, p.a + i * .06, .25)), on = lt > .3 + i * .09;
      const c = i < 3 ? CREME : i < 7 ? OR : ROUGE, w = 360 + i * 38;
      g.save(); g.translate(W / 2, y); g.scale(Math.max(0, k), 1);
      g.fillStyle = on ? al(c, .9) : al(CREME, .1); g.beginPath(); g.roundRect(-w / 2, -26, w, 52, 14); g.fill(); g.restore();
      if (k > .5) S.texte(String(i + 1), W / 2 - w / 2 - 50, y, { taille: 44, coul: on ? c : GRIS });
    }
    const n = lt < 1.1 ? lerp(0, 6, eo(cl(lt / 1.1))) : 7 + Math.sin((lt - 1.1) * 5) * .9;
    const yc = 1130 - n * 74;
    g.save(); g.fillStyle = ROUGE; g.beginPath(); g.moveTo(W / 2 + 330, yc); g.lineTo(W / 2 + 390, yc - 34); g.lineTo(W / 2 + 390, yc + 34); g.closePath(); g.fill(); g.restore();
    S.texte('?', W / 2 + 440, yc, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 8 });
    titrePop('À QUEL NIVEAU|TU T’ARRÊTES ?', 1380, t, p.a, 104);
  }

  // u(0) = 3, u(1) = 6, u(2) = 12 : trois barres qui doublent
  function suite(p, t) {
    O.petitTitre('— CHAQUE TERME DOUBLE —', 400);
    const base = 1150, ech = 52, V = [3, 6, 12], X = [270, 540, 810];
    V.forEach((v, i) => {
      const k = eo(pr(t, p.a + i * .3, .4)); if (k <= 0) return;
      const h = v * ech * k;
      g.fillStyle = i === 2 ? ROUGE : OR; g.fillRect(X[i] - 80, base - h, 160, h);
      g.strokeStyle = CREME; g.lineWidth = 4; g.strokeRect(X[i] - 80, base - h, 160, h);
      if (k > .6) formule(String(v), X[i], base - h - 60, 84, i === 2 ? ROUGE : OR, { contour: NOIR, contourL: 8 });
      S.texte('u(' + i + ')', X[i], base + 60, { taille: 52, coul: CREME, police: 'Spectral', it: true, poids: 500 });
      if (i > 0 && k > .3) { const kk = pop(t, p.a + i * .3, .3); g.save(); g.translate((X[i] + X[i - 1]) / 2, base - V[i - 1] * ech - 150); g.scale(kk, kk);
        S.texte('× 2', 0, 0, { taille: 56, coul: CREME, contour: NOIR, contourL: 8 }); g.restore(); }
    });
    ligne(140, base, 940, base, CREME, 6);
    titrePop('SUITE GÉOMÉTRIQUE|DE RAISON 2', 1420, t, p.a + .8, 100);
  }

  // courbe convexe : les tangentes défilent, toutes sous la courbe
  function convexe(p, t) {
    const ox = 540, oy = 1200, s = 62, lt = t - p.a;
    const f = x => .5 * x * x, X = x => ox + x * s, Y = y => oy - y * s;
    O.petitTitre('— f″ > 0 : f CONVEXE —', 400);
    ligne(80, oy, 1000, oy, al(CREME, .4), 4);
    const k = eo(pr(t, p.a, .6));
    g.save(); g.strokeStyle = OR; g.lineWidth = 10; g.lineCap = 'round'; g.beginPath();
    for (let x = -4.4; x <= -4.4 + 8.8 * k; x += .1) { const px = X(x), py = Y(f(x)); x === -4.4 ? g.moveTo(px, py) : g.lineTo(px, py); } g.stroke(); g.restore();
    // point de contact qui glisse, tangente (sous la courbe)
    if (k > .9) {
      const x0 = Math.sin((lt - .55) * 1.6) * 3.2, y0 = f(x0), d = 1.7;
      ligne(X(x0 - d), Y(y0 - x0 * d), X(x0 + d), Y(y0 + x0 * d), ROUGE, 7);
      g.fillStyle = ROUGE; g.beginPath(); g.arc(X(x0), Y(y0), 18, 0, 7); g.fill();
      // traces des tangentes précédentes
      [-3, -1.5, 1.5, 3].forEach(a => ligne(X(a - 1.6), Y(f(a) - a * 1.6), X(a + 1.6), Y(f(a) + a * 1.6), al(ROUGE, .3), 4));
    }
    titrePop('AU-DESSUS DE|SES TANGENTES', 1420, t, p.a + .6, 104);
  }

  // u(n) = (2n + 1) / (n + 3) : les points montent vers la droite y = 2
  function limite(p, t) {
    const ox = 150, oy = 1150, L = 820, Hh = 600, X = n => ox + n / 24 * L, Y = y => oy - y / 2.5 * Hh;
    O.petitTitre('— (2n + 1) / (n + 3) —', 400);
    axes(ox, oy, L, Hh, 'n', 'u');
    ligne(ox, Y(2), ox + L, Y(2), ROUGE, 5, [18, 14]);
    S.texte('2', ox - 45, Y(2), { taille: 60, coul: ROUGE, poids: 700 });
    const N = Math.floor(cl((t - p.a) / 1.4) * 24);
    for (let n = 0; n <= N; n++) { const u = (2 * n + 1) / (n + 3); g.fillStyle = OR; g.beginPath(); g.arc(X(n), Y(u), 13, 0, 7); g.fill(); }
    const kt = pop(t, p.a + 1.2, .35);
    if (kt > 0) { g.save(); g.translate(W / 2, Y(2) - 120); g.scale(kt, kt); formule('2n / n = 2', 0, 0, 84, OR, { contour: NOIR, contourL: 10 }); g.restore(); }
    titrePop('ELLE TEND|VERS 2', 1420, t, p.a + .4, 110);
  }

  // 2 × 2 × 2 = 8, donc ln(8) = 3 ln(2)
  function puissance(p, t) {
    O.petitTitre('— LE LOGARITHME —', 400);
    [0, 1, 2].forEach(i => { const k = pop(t, p.a + i * .15, .3); if (k <= 0) return;
      g.save(); g.translate(300 + i * 200, 680); g.scale(k, k);
      g.fillStyle = al(OR, .16); g.beginPath(); g.arc(0, 0, 80, 0, 7); g.fill(); g.strokeStyle = OR; g.lineWidth = 6; g.stroke();
      formule('2', 0, 4, 110, OR); g.restore();
      if (i < 2 && k > .8) S.texte('×', 400 + i * 200, 680, { taille: 70, coul: CREME }); });
    const k1 = eo(pr(t, p.a + .5, .3)); g.save(); g.globalAlpha = k1; formule('= 8 = 2³', W / 2, 860, 110, CREME); g.restore();
    const k2 = pop(t, p.a + .9, .35);
    if (k2 > 0) { g.save(); g.translate(W / 2, 1080); g.scale(k2, k2);
      g.fillStyle = al(OR, .14); g.beginPath(); g.roundRect(-460, -100, 920, 200, 30); g.fill(); g.strokeStyle = OR; g.lineWidth = 5; g.stroke();
      formule('ln(8) = 3 × ln(2)', 0, 4, 100, OR); g.restore(); }
    titrePop('DONC|k = 3', 1420, t, p.a + 1.1, 120);
  }

  // intégrale de 0 à 1 de 2x : l'aire du triangle sous la droite y = 2x
  function aire(p, t) {
    const ox = 240, oy = 1200, u = 400, X = x => ox + x * u, Y = y => oy - y * u / 1.6;
    O.petitTitre('— L’INTÉGRALE, C’EST UNE AIRE —', 400);
    axes(ox, oy, 720, 720, 'x', 'y');
    const ka = eo(pr(t, p.a + .4, .7));
    g.save(); g.fillStyle = al(OR, .35); g.beginPath(); g.moveTo(X(0), oy); g.lineTo(X(ka), Y(2 * ka)); g.lineTo(X(ka), oy); g.closePath(); g.fill(); g.restore();
    const kd = eo(pr(t, p.a, .4)); ligne(X(0), Y(0), X(1.3 * kd), Y(2.6 * kd), ROUGE, 9);
    S.texte('y = 2x', X(1.3) - 150, Y(2.6) + 10, { taille: 56, coul: ROUGE, police: 'Spectral', it: true, poids: 600 });
    ligne(X(1), oy, X(1), Y(2), al(CREME, .6), 4, [12, 10]); ligne(ox, Y(2), X(1), Y(2), al(CREME, .6), 4, [12, 10]);
    S.texte('1', X(1), oy + 55, { taille: 54, coul: CREME }); S.texte('0', ox - 35, oy + 45, { taille: 54, coul: CREME }); S.texte('2', ox - 45, Y(2), { taille: 54, coul: CREME });
    const kf = pop(t, p.a + 1.1, .35);
    if (kf > 0) { g.save(); g.translate(X(1) + 30, Y(.9)); g.scale(kf, kf); formule('aire = 1 × 2 / 2 = 1', 0, 0, 48, CREME, { contour: NOIR, contourL: 8, align: 'left', max: 380 }); g.restore(); }
    titrePop('[ x² ] DE 0 À 1|= 1', 1450, t, p.a + .9, 104);
  }

  // cinq personnes en pentagone, les dix poignées de main se tracent une à une
  function poignees(p, t) {
    O.petitTitre('— 2 PARMI 5 —', 400);
    const cx = W / 2, cy = 880, r = 330, P = [0, 1, 2, 3, 4].map(i => [cx + r * Math.sin(i * 2 * Math.PI / 5), cy - r * Math.cos(i * 2 * Math.PI / 5)]);
    const A = []; for (let i = 0; i < 5; i++) for (let j = i + 1; j < 5; j++) A.push([i, j]);
    const n = cl((t - p.a - .15) / 1.5) * A.length;
    A.forEach(([i, j], q) => { const k = cl(n - q); if (k <= 0) return;
      ligne(P[i][0], P[i][1], lerp(P[i][0], P[j][0], eo(k)), lerp(P[i][1], P[j][1], eo(k)), q === Math.floor(n) - 1 || (k < 1) ? ROUGE : OR, 7); });
    P.forEach(([x, y], i) => { const k = pop(t, p.a + i * .05, .3); g.save(); g.translate(x, y); g.scale(k, k);
      g.fillStyle = NOIR; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(0, -26, 30, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.arc(0, 40, 46, Math.PI, 0); g.closePath(); g.fill(); g.stroke(); g.restore(); });
    const c = Math.min(10, Math.floor(n + .001));
    formule(String(c), W / 2, cy + 20, 150, c === 10 ? ROUGE : OR, { contour: NOIR, contourL: 12 });
    titrePop('(5 × 4) / 2|= 10', 1440, t, p.a + 1.7, 110);
  }

  // arbre de probabilités : deux dés ; on suit « pas de 6 » deux fois, puis le contraire
  function arbre(p, t) {
    O.petitTitre('— PAR LE CONTRAIRE —', 380);
    const r0 = [110, 860], n1 = [[440, 590, '6', '1/6'], [440, 1130, 'pas 6', '5/6']];
    const k1 = eo(pr(t, p.a, .35)), k2 = eo(pr(t, p.a + .3, .35)), kr = eo(pr(t, p.a + .7, .4));
    n1.forEach(([x, y, lab, pb], i) => {
      ligne(r0[0], r0[1], lerp(r0[0], x - 60, k1), lerp(r0[1], y, k1), i && kr > 0 ? ROUGE : al(CREME, .7), i && kr > 0 ? 9 : 6);
      if (k1 > .8) { S.texte(lab, x, y, { taille: 64, coul: i ? CREME : GRIS, poids: 700 });
        S.texte(pb, (r0[0] + x) / 2 - 40, (r0[1] + y) / 2 + (i ? 50 : -50), { taille: 60, coul: OR, police: 'Spectral', poids: 600 }); }
      [[-110, '6', '1/6'], [110, 'pas 6', '5/6']].forEach(([dy, l2, p2], j) => {
        const x2 = 880, y2 = y + dy * 1.15, rouge = i === 1 && j === 1 && kr > 0;
        ligne(x + 90, y, lerp(x + 90, x2 - 90, k2), lerp(y, y2, k2), rouge ? ROUGE : al(CREME, .45), rouge ? 9 : 4);
        if (k2 > .8) { S.texte(l2, x2, y2, { taille: 56, coul: rouge ? ROUGE : i ? CREME : GRIS, poids: 700 });
          S.texte(p2, (x + x2) / 2, (y + y2) / 2 + (dy < 0 ? -44 : 44), { taille: 50, coul: al(OR, .85), police: 'Spectral', poids: 600 }); }
      });
    });
    g.fillStyle = OR; g.beginPath(); g.arc(r0[0], r0[1], 16, 0, 7); g.fill();
    const ka = eo(pr(t, p.a + .9, .3)); g.save(); g.globalAlpha = ka; formule('aucun 6 : (5/6)² = 25/36', W / 2, 1400, 72, ROUGE); g.restore();
    const kb = pop(t, p.a + 1.4, .35); if (kb > 0) { g.save(); g.translate(W / 2, 1530); g.scale(kb, kb);
      formule('au moins un 6 : 1 − 25/36 = 11/36', 0, 0, 72, OR, { contour: NOIR, contourL: 8, max: 990 }); g.restore(); }
  }

  // une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .3)), txt = 'Mon niveau : … / 10', n = Math.floor(cl((t - p.a - .3) / .8) * txt.length);
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-300, 165); g.lineTo(-340, 260); g.lineTo(-220, 165); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-330, -60, 50, 0, 7); g.fill();
    S.texte('toi', -230, -60, { taille: 44, coul: GRIS, align: 'left', poids: 600 });
    S.texte(txt.slice(0, n), -360, 60, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, align: 'left', max: 760 });
    const kc = pr(t, p.a + 1.2, .3); if (kc > 0) { g.save(); g.translate(350, -80); g.scale(back(kc), back(kc)); g.fillStyle = ROUGE;
      g.beginPath(); g.moveTo(0, 30); g.bezierCurveTo(-60, -10, -30, -60, 0, -30); g.bezierCurveTo(30, -60, 60, -10, 0, 30); g.fill(); g.restore(); }
    g.restore();
    deux('DIS TON NIVEAU|EN COMMENTAIRE', 1350, 110);
  }

  return { nocalc, echelle, suite, convexe, limite, puissance, aire, poignees, arbre, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  if (p.type === 'nocalc') L.push([p.a + .2, 'lame', .6], [p.a + .45, 'tampon', .8]);
  if (p.type === 'echelle') { for (let i = 0; i < 10; i++) L.push([p.a + .3 + i * .09, 'tic', .3]); L.push([p.a, 'montee', .4]); }
  if (p.type === 'suite') [0, 1, 2].forEach(i => L.push([p.a + i * .3, 'pop', .4 + i * .1]));
  if (p.type === 'convexe') L.push([p.a, 'stylo', .5]);
  if (p.type === 'limite') { for (let k = 0; k < 8; k++) L.push([p.a + k * .18, 'tic', .25]); L.push([p.a + 1.2, 'valide', .5]); }
  if (p.type === 'puissance') L.push([p.a, 'pop', .4], [p.a + .15, 'pop', .4], [p.a + .3, 'pop', .4], [p.a + .9, 'valide', .5]);
  if (p.type === 'aire') L.push([p.a, 'stylo', .45], [p.a + .4, 'souffle', .4]);
  if (p.type === 'poignees') { for (let k = 0; k < 10; k++) L.push([p.a + .15 + k * .15, 'blip', .25]); L.push([p.a + 1.7, 'gong', .5]); }
  if (p.type === 'arbre') L.push([p.a, 'whoosh', .4], [p.a + .7, 'lame', .45], [p.a + 1.4, 'valide', .6]);
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .3 + k * .1, 'tic', .25]); L.push([p.a + 1.2, 'pop', .5]); }
};
