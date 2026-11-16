// Plans propres au short « Plus ou moins ? » (habillage jeu télé). O = outils du modèle (carte, multi, tampon,
// barreRouge, petitTitre, fondImg, photo, al, C = couleurs de l'habillage). Couleurs : O.C et O.al seulement.
// Convention : OR = PLUS (▲), ROUGE = MOINS (▼).
window.SANS_ST_A = ['titre', 'score', 'duel'];
window.PROPRES_A = ['titre', 'score', 'duel', 'fecondation', 'chute', 'angle', 'volcan', 'detroits', 'podium', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const deux = (txt, y, taille = 110, c2 = OR) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? c2 : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };
  // cadre de plateau télé : ampoules qui clignotent autour d'un rectangle arrondi
  function ampoules(x, y, w, h, t, c = OR) {
    g.save(); g.strokeStyle = c; g.lineWidth = 8; g.beginPath(); g.roundRect(x, y, w, h, 40); g.stroke();
    const n = 34, per = 2 * (w + h);
    for (let i = 0; i < n; i++) {
      let d = i / n * per, px, py;
      if (d < w) { px = x + d; py = y; } else if ((d -= w) < h) { px = x + w; py = y + d; } else if ((d -= h) < w) { px = x + w - d; py = y + h; } else { d -= w; px = x; py = y + h - d; }
      const on = (i + Math.floor(t * 8)) % 3 === 0;
      g.fillStyle = on ? CREME : al(c, .45); if (on) { g.shadowColor = c; g.shadowBlur = 20; } else g.shadowBlur = 0;
      g.beginPath(); g.arc(px, py, 11, 0, 7); g.fill();
    }
    g.restore();
  }
  // un chromosome en X
  function chromoX(x, y, s, c, rot = 0) {
    g.save(); g.translate(x, y); g.rotate(rot); g.fillStyle = c; g.strokeStyle = al(NOIR, .5); g.lineWidth = s * .05;
    [-.35, .35].forEach(a => { g.save(); g.rotate(a); g.beginPath(); g.roundRect(-s * .12, -s * .5, s * .24, s, s * .12); g.fill(); g.stroke(); g.restore(); });
    g.restore();
  }

  // ---------- titre : PLUS ▲ / OU / MOINS ▼
  function titre(p, t) {
    const lt = t - p.a, k1 = back(pr(lt, 0, .3)), k2 = back(pr(lt, .2, .3)), k3 = back(pr(lt, .4, .3));
    const b = Math.sin(t * 7) * 18;
    pop(k1, W / 2, 560 - b, () => { S.texte('▲', 0, -150, { taille: 170, coul: OR }); S.texte('PLUS', 0, 30, { taille: 210, coul: OR, contour: NOIR, contourL: 14 }); });
    pop(k2, W / 2, 900, () => { rond(0, 0, 95, ROUGE, CREME, 8); S.texte('OU', 0, 6, { taille: 90, coul: CREME }); });
    pop(k3, W / 2, 1240 + b, () => { S.texte('MOINS', 0, -30, { taille: 210, coul: ROUGE, contour: NOIR, contourL: 14 }); S.texte('▼', 0, 150, { taille: 170, coul: ROUGE }); });
    S.texte('?', W / 2 + 400, 900, { taille: 200, coul: al(CREME, .25 + .2 * Math.sin(t * 5)) });
    S.texte('?', W / 2 - 400, 900, { taille: 200, coul: al(CREME, .25 + .2 * Math.cos(t * 5)) });
  }

  // ---------- score : etape 0 = quatre cases vides ; etape 1 = les quatre bonnes réponses, puis « TON SCORE ? »
  const REPONSES = [['SVT', 1], ['HISTOIRE', 0], ['PHYSIQUE', 1], ['GÉOGRAPHIE', 0]];
  function score(p, t) {
    const lt = t - p.a;
    if (!p.etape) {
      ampoules(110, 430, 860, 640, t);
      for (let i = 0; i < 4; i++) pop(pr(lt, .1 + i * .12, .3), 260 + i * 187, 750, () => {
        g.fillStyle = al(CREME, .1); g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.roundRect(-75, -110, 150, 220, 22); g.fill(); g.stroke();
        S.texte('?', 0, 6, { taille: 120, coul: OR });
      });
      S.texte('0 / 4', W / 2, 980, { taille: 80, coul: CREME });
      deux('COMPTE TES|POINTS', 1370, 120);
      return;
    }
    S.texte('LES BONNES RÉPONSES', W / 2, 400, { taille: 62, coul: OR, max: 960 });
    REPONSES.forEach(([m, plus], i) => {
      const k = pr(lt, i * .2, .3), y = 560 + i * 190; if (k <= 0) return;
      g.save(); g.globalAlpha = cl(k * 2); g.translate(lerp(500, 0, eo(k)), 0);
      g.fillStyle = al(CREME, .1); g.beginPath(); g.roundRect(110, y - 75, 860, 150, 30); g.fill();
      S.texte(`DUEL ${i + 1} · ${m}`, 150, y, { taille: 48, coul: CREME, align: 'left', max: 470 });
      S.texte(plus ? '▲ PLUS' : '▼ MOINS', 930, y, { taille: 66, coul: plus ? OR : ROUGE, align: 'right' });
      g.restore();
    });
    const kf = back(pr(lt, 1, .35)); g.save(); g.translate(W / 2, 1380); g.scale(kf, kf);
    S.texte('TON SCORE : … / 4', 0, 0, { taille: 100, coul: OR, contour: NOIR, contourL: 10, max: 960 }); g.restore();
  }

  // ---------- duel : « DUEL n » dans un cadre d'ampoules, la matière, une image ou une icône
  function duel(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    ampoules(80, 280, 920, 1300, t, p.n === 4 ? ROUGE : OR);
    g.save(); g.translate(W / 2, 470); g.scale(lerp(2, 1, k), lerp(2, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(p.n === 4 ? 'DERNIER DUEL' : 'DUEL ' + p.n, 0, 0, { taille: p.n === 4 ? 130 : 170, coul: OR, contour: NOIR, contourL: 14, max: 860 }); g.restore();
    const kv = eo(pr(lt, .15, .4));
    if (p.img) { g.save(); g.globalAlpha = kv; O.carte(p.img, W / 2, 920, 620, 520, .03, 1.1 + lt * .04, .5, .45, { couleur: true }); g.restore(); }
    else {
      g.save(); g.translate(W / 2, 920); g.scale(lerp(.5, 1, kv), lerp(.5, 1, kv)); g.globalAlpha = kv;
      if (p.icone === 'chromo') { for (let i = 0; i < 6; i++) chromoX(-250 + (i % 3) * 250, i < 3 ? -110 : 120, 170, i % 2 ? ROUGE : OR, Math.sin(t * 2 + i) * .15); }
      if (p.icone === 'lunette') {   // tube de lunette pointé vers le ciel, une étoile
        g.rotate(-.5); g.fillStyle = CREME; g.beginPath(); g.roundRect(-300, -50, 520, 100, 20); g.fill();
        g.fillStyle = OR; g.fillRect(200, -70, 40, 140); g.fillStyle = ROUGE; g.fillRect(-340, -32, 60, 64); g.rotate(.5);
        const e = 1 + .2 * Math.sin(t * 6); g.save(); g.translate(260, -260); g.scale(e, e); S.texte('★', 0, 0, { taille: 120, coul: OR }); g.restore();
      }
      g.restore();
    }
    const km = back(pr(lt, .3, .3)); g.save(); g.translate(W / 2, 1360); g.scale(km, km);
    g.fillStyle = ROUGE; g.beginPath(); g.roundRect(-330, -80, 660, 160, 80); g.fill();
    S.texte(p.matiere, 0, 6, { taille: 96, coul: CREME, max: 600 }); g.restore();
  }

  // ---------- fecondation : deux gamètes tirés au hasard se rencontrent
  function fecondation(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .2, 1)), kz = pr(lt, 1.2, .4);
    const gam = (x, y, c, r) => { g.save(); rond(x, y, r, al(c, .25), c, 10);
      for (let i = 0; i < 4; i++) chromoX(x - r * .45 + (i % 2) * r * .9, y - r * .35 + Math.floor(i / 2) * r * .7, r * .5, i % 2 ? OR : ROUGE, i); g.restore(); };
    if (kz < 1) { g.save(); g.globalAlpha = 1 - kz; gam(lerp(200, 470, k), 800, OR, 130); gam(lerp(880, 610, k), 800, ROUGE, 130); g.restore(); }
    if (kz > 0) { const s = back(kz); g.save(); g.translate(W / 2, 800); g.scale(s, s); rond(0, 0, 220, al(OR, .2), CREME, 12);
      for (let i = 0; i < 8; i++) chromoX(-120 + (i % 4) * 80, -60 + Math.floor(i / 4) * 130, 100, i % 2 ? OR : ROUGE, i * .7); g.restore();
      pop(pr(lt, 1.5, .3), W / 2, 1110, () => S.texte('UN INDIVIDU UNIQUE', 0, 0, { taille: 62, coul: CREME, max: 900 })); }
    S.texte('?', 200, 560, { taille: 120, coul: al(OR, .5 + .5 * Math.sin(t * 9)) });
    S.texte('?', 880, 560, { taille: 120, coul: al(ROUGE, .5 + .5 * Math.cos(t * 9)) });
    deux('2 GAMÈTES|AU HASARD', 1400, 120);
  }

  // ---------- chute : le Dow Jones de 381 (septembre 1929) à 41 (juillet 1932) ; schéma, sans valeurs intermédiaires
  function chute(p, t) {
    const lt = t - p.a, gx = 150, gy = 420, gw = 800, gh = 760, k = eo(pr(lt, 0, 1));
    g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 5; g.beginPath(); g.moveTo(gx, gy); g.lineTo(gx, gy + gh); g.lineTo(gx + gw, gy + gh); g.stroke(); g.restore();
    const y = v => gy + gh - v / 400 * gh, P = u => [gx + 40 + u * (gw - 80), y(lerp(381, 41, 1 - Math.pow(1 - u, 1.6)))];
    g.save(); g.strokeStyle = ROUGE; g.lineWidth = 14; g.lineJoin = 'round'; g.shadowColor = ROUGE; g.shadowBlur = 20; g.beginPath();
    for (let i = 0; i <= 40 * k; i++) { const [x, yy] = P(i / 40); i ? g.lineTo(x, yy) : g.moveTo(x, yy); } g.stroke(); g.restore();
    const [x0, y0] = P(0), [x1, y1] = P(1);
    rond(x0, y0, 20, OR); S.texte('381', x0 + 40, y0 - 50, { taille: 70, coul: OR, align: 'left' });
    S.texte('sept. 1929', x0, gy + gh + 50, { taille: 40, coul: CREME });
    if (k >= 1) { rond(x1, y1, 20, ROUGE); S.texte('41', x1, y1 - 60, { taille: 70, coul: ROUGE }); }
    S.texte('juil. 1932', x1, gy + gh + 50, { taille: 40, coul: CREME });
    const kt = pr(lt, 1, .3); if (kt > 0) O.tampon('− 89 %', 720, 480, kt, -.1, 110, ROUGE);
    deux('LE KRACH|DE 1929', 1420, 120, ROUGE);
  }

  // ---------- angle : la Lune à l'œil nu, Mars minuscule qu'il faut grossir 105 fois
  function angle(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .8, 2.2)), im = S.img('lune');
    g.save(); g.beginPath(); g.arc(300, 760, 200, 0, 7); g.clip(); if (im) S.cover(im, 100, 560, 400, 400, 1.05); g.restore();
    rond(300, 760, 200, null, CREME, 6);
    S.texte('LA LUNE', 300, 1010, { taille: 56, coul: CREME });
    S.texte('à l’œil nu', 300, 1065, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    const r = lerp(2, 200, k);
    g.save(); g.shadowColor = ROUGE; g.shadowBlur = 30; rond(780, 760, r, ROUGE, CREME, k > .1 ? 6 : 0); g.restore();
    S.texte('MARS', 780, 1010, { taille: 56, coul: ROUGE });
    S.texte('× ' + Math.max(1, Math.round(lerp(1, 105, k))), 780, 1075, { taille: 60, coul: OR, poids: 700 });
    deux('IL FAUT|GROSSIR 105 FOIS', 1400, 110);
  }

  // ---------- volcan : Mars (6 800 km) et Olympus Mons (650 km), dix fois plus petit
  function volcan(p, t) {
    const lt = t - p.a, k = eo(pr(lt, 0, .5)), ko = pr(lt, .5, .4);
    g.save(); g.globalAlpha = k; g.shadowColor = ROUGE; g.shadowBlur = 40; rond(W / 2, 800, 340, al(ROUGE, .55), ROUGE, 8); g.restore();
    g.save(); g.globalAlpha = k; g.strokeStyle = CREME; g.lineWidth = 5; g.setLineDash([16, 12]); g.beginPath(); g.moveTo(W / 2 - 340, 800); g.lineTo(W / 2 + 340, 800); g.stroke(); g.restore();
    S.texte('MARS : 6 800 km', W / 2, 760, { taille: 54, coul: CREME });
    pop(ko, W / 2 + 120, 640, () => { rond(0, 0, 34, OR, NOIR, 4); S.texte('▲', 0, 2, { taille: 40, coul: NOIR }); });
    pop(pr(lt, .7, .3), W / 2 + 120, 560, () => S.texte('OLYMPUS MONS : 650 km', 0, 0, { taille: 48, coul: OR, max: 700 }));
    deux('10 FOIS|PLUS PETIT', 1400, 120);
  }

  // ---------- detroits : un détroit étroit, des pétroliers qui passent, le compteur de barils
  function detroits(p, t) {
    const lt = t - p.a;
    // deux masses de terre et le passage
    g.save(); g.fillStyle = al(GRIS, .45);
    g.beginPath(); g.moveTo(0, 380); g.lineTo(700, 380); g.quadraticCurveTo(520, 700, 600, 760); g.quadraticCurveTo(300, 780, 0, 900); g.fill();
    g.beginPath(); g.moveTo(W, 1300); g.lineTo(380, 1300); g.quadraticCurveTo(560, 1000, 480, 940); g.quadraticCurveTo(780, 900, W, 760); g.fill(); g.restore();
    for (let i = 0; i < 5; i++) {   // pétroliers le long du chenal
      const u = ((lt * .25 + i / 5) % 1), x = lerp(-80, 1160, u), y = lerp(1180, 520, u);
      g.save(); g.translate(x, y); g.rotate(-.49); g.fillStyle = i % 2 ? OR : CREME; g.beginPath(); g.moveTo(-70, -18); g.lineTo(60, -18); g.lineTo(80, 0); g.lineTo(60, 18); g.lineTo(-70, 18); g.closePath(); g.fill();
      g.fillStyle = ROUGE; g.fillRect(-60, -10, 26, 20); g.restore();
    }
    S.texte('MALACCA', 560, 860, { taille: 64, coul: CREME, contour: NOIR, contourL: 8 });
    const n = Math.round(lerp(0, 23700000, eo(pr(lt, .2, 2))));
    S.texte(n.toLocaleString('fr-FR'), W / 2, 1420, { taille: 110, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12, max: 980 });
    S.texte('BARILS DE PÉTROLE PAR JOUR', W / 2, 1530, { taille: 50, coul: CREME, max: 960 });
  }

  // ---------- podium : Malacca devant Ormuz (millions de barils par jour, 2023)
  function podium(p, t) {
    const lt = t - p.a, base = 1200;
    [[330, 23.7, 'MALACCA', OR], [750, 20.9, 'ORMUZ', ROUGE]].forEach(([x, v, nom, c], i) => {
      const k = eo(pr(lt, i * .15, .7)), h = v / 24 * 640 * k;
      g.save(); g.shadowColor = c; g.shadowBlur = 25; g.fillStyle = c; g.beginPath(); g.roundRect(x - 140, base - h, 280, h, 20); g.fill(); g.restore();
      if (k > .3) S.texte(String(v).replace('.', ','), x, base - h - 60, { taille: 90, coul: CREME, police: 'Spectral', poids: 600 });
      S.texte(nom, x, base + 60, { taille: 60, coul: c });
    });
    pop(pr(lt, .9, .3), 330, 400, () => S.texte('♛', 0, 0, { taille: 120, coul: OR }));
    S.texte('millions de barils par jour (2023)', W / 2, 1340, { taille: 44, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 });
  }

  // ---------- commentaire : une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    g.save(); g.translate(W / 2, 800); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-250, 160); g.lineTo(-320, 280); g.lineTo(-160, 160); g.fill();
    const msg = 'J’ai eu … / 4', n = Math.floor(cl((lt - .25) / .6) * msg.length);
    S.texte(msg.slice(0, n), 0, 0, { taille: 90, coul: NOIR, max: 780 });
    g.restore();
    deux('DIS-LE EN|COMMENTAIRE', 1300, 110, ROUGE);
  }

  return { titre, score, duel, fecondation, chute, angle, volcan, detroits, podium, commentaire };
};
window.SONS_A = (p, L) => {
  if (p.type === 'titre') L.push([p.a, 'montee', .5], [p.a + .4, 'pop', .5]);
  if (p.type === 'score') for (let i = 0; i < 4; i++) L.push([p.a + .1 + i * (p.etape ? .2 : .12), 'pop', .4]);
  if (p.type === 'duel') L.push([p.a, 'gong', .6], [p.a + .3, 'pop', .5]);
  if (p.type === 'fecondation') L.push([p.a + 1.2, 'pop', .6]);
  if (p.type === 'chute') L.push([p.a, 'souffle', .6], [p.a + 1, 'tampon', .8]);
  if (p.type === 'angle') L.push([p.a + .8, 'montee', .5]);
  if (p.type === 'volcan') L.push([p.a + .5, 'pop', .5]);
  if (p.type === 'detroits') for (let k = 0; k < 10; k++) L.push([p.a + .2 + k * .2, 'tic', .3]);
  if (p.type === 'podium') L.push([p.a + .9, 'valide', .6]);
  if (p.type === 'commentaire') L.push([p.a + .25, 'clic', .4]);
};
