// Plans propres au short « niveauphilo » (« Philo, niveau 1 → 10 »), modèle A, habillage « jeu ».
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
window.SANS_ST_A = ['echelle', 'minuteur', 'ascenseur', 'verbes', 'commentaires'];
window.PROPRES_A = ['echelle', 'minuteur', 'ascenseur', 'tiraille', 'verbes', 'monopole', 'commentaires'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const claque = (s, y, ta, t, o) => { const k = back(pr(t, ta, .3)); if (k <= 0) return; g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
    S.texte(s, 0, 0, Object.assign({ taille: 100, coul: CREME, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };
  const deuxClaque = (txt, y, ta, t, taille = 110) => { const k = back(pr(t, ta, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  // couleur d'un palier (1 à 10) et son étiquette, dans les cinq couleurs de l'habillage
  // (mêmes seuils que le plan `niveau` de formats-a.js, sur 10 niveaux)
  const uN = n => (n - 1) / 9;
  const coulN = n => uN(n) < .34 ? CREME : uN(n) < .67 ? OR : ROUGE;
  const etiq = n => uN(n) < .25 ? 'FACILE' : uN(n) < .5 ? 'MOYEN' : uN(n) < .8 ? 'DIFFICILE' : 'IMPOSSIBLE';

  // l'échelle des dix niveaux ; un pion « TOI » grimpe et hésite (p.fin : il vise le niveau 10)
  function echelle(p, t) {
    const lt = t - p.a;
    if (p.fin) deuxClaque('ET TOI…|JUSQU’AU 10 ?', 400, p.a + .05, t, 120);
    else deuxClaque('À QUEL NIVEAU|TU T’ARRÊTES ?', 400, p.a + .05, t, 110);
    const x0 = 330, larg = 560, y0 = 1500, pas = 88;
    for (let i = 0; i < 10; i++) {
      const k = back(pr(t, p.a + .1 + i * .06, .25)); if (k <= 0) continue;
      const y = y0 - i * pas, c = coulN(i + 1);
      g.save(); g.translate(x0 + larg / 2, y); g.scale(k, 1);
      g.fillStyle = al(c, .22); g.strokeStyle = c; g.lineWidth = 5;
      g.beginPath(); g.roundRect(-larg / 2, -32, larg, 64, 18); g.fill(); g.stroke(); g.restore();
      S.texte(String(i + 1), x0 - 70, y + 3, { taille: 56, coul: c });
    }
    // montants de l'échelle
    g.save(); g.strokeStyle = al(CREME, .35); g.lineWidth = 10;
    [x0 - 10, x0 + larg + 10].forEach(x => { g.beginPath(); g.moveTo(x, y0 + 50); g.lineTo(x, y0 - 9 * pas - 50); g.stroke(); }); g.restore();
    // le pion
    const cible = p.fin ? 9 : 6.2, monte = eo(pr(t, p.a + .3, 1.1));
    let niv = cible * monte; if (!p.fin && monte > .95) niv += Math.sin(lt * 5) * .8;
    if (p.fin && monte > .95) niv = 9 + Math.sin(lt * 9) * .05;
    const yp = y0 - niv * pas, xp = x0 + larg + 90;
    g.save(); g.translate(xp, yp);
    g.fillStyle = OR; g.shadowColor = OR; g.shadowBlur = 30; g.beginPath(); g.arc(0, 0, 52, 0, 7); g.fill(); g.shadowBlur = 0;
    g.fillStyle = NOIR; g.beginPath(); g.moveTo(-82, 0); g.lineTo(-58, -18); g.lineTo(-58, 18); g.fill();
    S.texte('TOI', 0, 3, { taille: 34, coul: NOIR }); g.restore();
    if (p.fin && monte > .95) { const kk = back(pr(t, p.a + 1.4, .3)); if (kk > 0) { g.save(); g.translate(x0 + larg / 2, y0 - 9 * pas - 100); g.scale(kk, kk); S.texte('10 ?', 0, 0, { taille: 80, coul: ROUGE, contour: NOIR, contourL: 8 }); g.restore(); } }
  }

  // le chrono géant : trois, deux, un
  function minuteur(p, t) {
    const lt = t - p.a, n = Math.max(1, 3 - Math.floor(lt / .7)), u = (lt % .7) / .7;
    const sec = n === 1 ? (rnd(Math.floor(t * 30)) - .5) * 16 : 0;
    g.save(); g.translate(W / 2 + sec, 820);
    const k = back(pr(t, p.a, .3)); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-50, -400, 100, 70, 14); g.fill();
    g.strokeStyle = CREME; g.lineWidth = 22; g.beginPath(); g.arc(0, 0, 300, 0, 7); g.stroke();
    g.strokeStyle = n === 1 ? ROUGE : OR; g.lineWidth = 36;
    g.beginPath(); g.arc(0, 0, 255, -Math.PI / 2, -Math.PI / 2 + (1 - (3 - n + u) / 3) * 6.283); g.stroke();
    S.texte(String(n), 0, 10, { taille: 300, police: 'Spectral', poids: 600, coul: n === 1 ? ROUGE : CREME });
    g.restore();
    deuxClaque('RÉPONDS AVANT|LA FIN DU CHRONO', 1390, p.a + .1, t, 100);
  }

  // l'ascenseur des niveaux : le compteur monte de p.de à p.n, les portes s'ouvrent ; p.boss : « BOSS FINAL »
  function ascenseur(p, t) {
    const kc = eo(pr(t, p.a + .02, .3)), v = Math.round(lerp(p.de || 0, p.n, kc)), arrive = kc >= 1;
    const c = coulN(p.n);
    g.save(); g.fillStyle = al(CREME, .06); g.strokeStyle = OR; g.lineWidth = 8;
    g.beginPath(); g.roundRect(220, 470, 640, 800, 30); g.fill(); g.stroke(); g.restore();
    S.texte('NIVEAU', W / 2, 560, { taille: 64, coul: CREME, esp: 12 });
    // écran
    g.save(); g.fillStyle = al(NOIR, .85); g.beginPath(); g.roundRect(300, 620, 480, 380, 24); g.fill();
    S.texte(String(v), W / 2, 820, { taille: 300, coul: c, ombre: al(c, .7), flou: 40 });
    g.restore();
    g.save(); g.strokeStyle = OR; g.lineWidth = 8; g.strokeRect(300, 620, 480, 380);
    // « ding » à l'arrivée : un cadre lumineux qui s'élargit et s'efface
    const kd = pr(t, p.a + .32, .4); if (kd > 0 && kd < 1) { g.globalAlpha = 1 - kd; g.strokeStyle = c; g.lineWidth = 12;
      g.strokeRect(300 - kd * 80, 620 - kd * 80, 480 + kd * 160, 380 + kd * 160); }
    g.restore();
    // flèche qui clignote pendant la montée
    if (!arrive && Math.floor(t * 8) % 2 === 0) S.texte('▲', W / 2, 1110, { taille: 110, coul: OR });
    if (arrive) { const ke = back(pr(t, p.a + .32, .3)); g.save(); g.translate(W / 2, 1150); g.scale(ke, ke);
      S.texte(etiq(p.n), 0, 0, { taille: 90, coul: c, contour: NOIR, contourL: 10, esp: 8, max: 600 }); g.restore(); }
    if (p.boss && t >= tps(p.boss)) {
      const tb = tps(p.boss), sx = (rnd(Math.floor(t * 40)) - .5) * 18 * (1 - pr(t, tb, .6));
      g.save(); g.translate(sx, 0); claque('BOSS FINAL', 1450, tb, t, { taille: 140, coul: ROUGE, contourL: 14 }); g.restore();
    }
  }

  // Freud : le moi tiraillé entre le ça (pulsions) et le surmoi (interdits)
  function tiraille(p, t) {
    const lt = t - p.a, ts = tps(p.surmoi), ks = back(pr(t, ts, .3));
    O.carte('freud', W / 2, 560, 340, 430, -.03, 1.05 + lt * .02, .5, .35);
    S.texte('FREUD · 1923', W / 2, 830, { taille: 40, coul: OR, esp: 8 });
    const y = 1150, tir = Math.sin(lt * 6) * (t >= ts ? 70 : 30) - (t >= ts ? 0 : 40), xm = W / 2 + tir;
    // cordes
    g.save(); g.strokeStyle = CREME; g.lineWidth = 8; g.lineCap = 'round';
    g.beginPath(); g.moveTo(275, y); g.quadraticCurveTo((275 + xm) / 2, y + 20, xm - 95, y); g.stroke();
    g.globalAlpha = t >= ts ? 1 : .3; g.beginPath(); g.moveTo(xm + 95, y); g.quadraticCurveTo((805 + xm) / 2, y + 20, 805, y); g.stroke(); g.restore();
    // le ça
    const kc = back(pr(t, p.a + .05, .3));
    g.save(); g.translate(165, y); g.scale(kc, kc); g.fillStyle = al(ROUGE, .25); g.strokeStyle = ROUGE; g.lineWidth = 6;
    g.beginPath(); g.roundRect(-110, -80, 220, 160, 22); g.fill(); g.stroke(); S.texte('ÇA', 0, 4, { taille: 80, coul: ROUGE }); g.restore();
    if (kc > 0) S.texte('les pulsions', 165, y + 130, { taille: 40, police: 'Spectral', it: true, poids: 500, coul: CREME });
    // le surmoi
    g.save(); g.translate(915, y); g.globalAlpha = t >= ts ? 1 : .3; const k2 = t >= ts ? ks : 1; g.scale(k2, k2);
    g.fillStyle = al(OR, .2); g.strokeStyle = OR; g.lineWidth = 6;
    g.beginPath(); g.roundRect(-125, -80, 250, 160, 22); g.fill(); g.stroke(); S.texte('SURMOI', 0, 4, { taille: 50, coul: OR, max: 220 }); g.restore();
    if (t >= ts) S.texte('les interdits', 915, y + 130, { taille: 40, police: 'Spectral', it: true, poids: 500, coul: CREME });
    deuxClaque('LE MOI,|COINCÉ AU MILIEU', 1440, p.a + .2, t, 96);
    // le moi
    g.save(); g.translate(xm, y); g.fillStyle = al(CREME, .14); g.strokeStyle = CREME; g.lineWidth = 8;
    g.beginPath(); g.arc(0, 0, 95, 0, 7); g.fill(); g.stroke(); S.texte('MOI', 0, 4, { taille: 64, coul: CREME }); g.restore();
  }

  // arrêter, enfermer, contraindre : chaque mot claque à son repère, des barreaux tombent
  function verbes(p, t) {
    const M = p.mots || [];
    for (let i = 0; i < 9; i++) { const k = eo(pr(t, p.a + i * .05, .3)); g.save(); g.fillStyle = al(GRIS, .3);
      g.fillRect(70 + i * 120, lerp(-H, 0, k), 22, H); g.restore(); }
    M.forEach((a, i) => {
      const ta = tps(a); if (t < ta) return;
      const actif = !M[i + 1] || t < tps(M[i + 1]);
      claque(['ARRÊTER', 'ENFERMER', 'CONTRAINDRE'][i], 680 + i * 250, ta, t, { taille: 140, coul: actif ? OR : CREME, contourL: 14 });
    });
  }

  // le monopole : un disque qui se remplit à 100 %, l'État seul ; le duel de Gérôme en fond
  function monopole(p, t) {
    O.fondImg('duel', 1.15 + (t - p.a) * .02, .3, .5, .4);
    claque('L’ÉTAT', 430, p.a + .05, t, { taille: 130, coul: CREME, contourL: 12 });
    const k = eo(pr(t, p.a + .15, .6));
    g.save(); g.translate(W / 2, 820);
    g.fillStyle = al(CREME, .12); g.beginPath(); g.arc(0, 0, 280, 0, 7); g.fill();
    g.fillStyle = OR; g.beginPath(); g.moveTo(0, 0); g.arc(0, 0, 280, -Math.PI / 2, -Math.PI / 2 + k * 6.283); g.closePath(); g.fill();
    S.texte(Math.round(k * 100) + ' %', 0, 6, { taille: 150, coul: k > .5 ? NOIR : CREME });
    g.restore();
    if (t > p.a + .8) O.tampon('MONOPOLE', W / 2, 1190, pr(t, p.a + .8, .3), -.1, 90, ROUGE);
    if (t > p.a + .9) deuxClaque('NE PARTAGE PAS|CE DROIT', 1420, p.a + .9, t, 96);
  }

  // des commentaires qui tombent : « niveau 3 », « niveau 10 »…
  function commentaires(p, t) {
    deuxClaque('DIS TON NIVEAU|EN COMMENTAIRE', 420, p.a + .05, t, 100);
    const C = [['NIVEAU 3', 'Aristote m’a eu'], ['NIVEAU 7', 'le surmoi, je connais'], ['NIVEAU 10', 'trop facile'], ['NIVEAU 5', 'Sartre ??']];
    C.forEach(([n, txt], i) => {
      const k = back(pr(t, p.a + .3 + i * .3, .3)); if (k <= 0) return;
      const y = 720 + i * 220;
      g.save(); g.translate(lerp(600, 0, k), y);
      g.fillStyle = al(CREME, .1); g.strokeStyle = al(CREME, .35); g.lineWidth = 3;
      g.beginPath(); g.roundRect(240, -90, 780, 180, 30); g.fill(); g.stroke();
      g.fillStyle = [GRIS, OR, ROUGE, CREME][i]; g.beginPath(); g.arc(160, 0, 58, 0, 7); g.fill();
      S.texte('?', 160, 4, { taille: 64, coul: NOIR });
      S.texte(n, 280, -36, { taille: 54, coul: coulN(+n.split(' ')[1]), align: 'left' });
      S.texte(txt, 280, 36, { taille: 52, police: 'Spectral', it: true, poids: 500, coul: CREME, align: 'left', max: 600 });
      S.texte('♥', 960, 0, { taille: 50, coul: ROUGE });
      g.restore();
    });
  }

  return { echelle, minuteur, ascenseur, tiraille, verbes, monopole, commentaires };
};
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'echelle') L.push([p.a + .1, 'montee', .5], [p.a + 1.4, 'pop', .5]);
  if (p.type === 'minuteur') [0, .7, 1.4].forEach(d => L.push([p.a + d, 'tic', .7]));
  if (p.type === 'ascenseur') {
    const n = Math.max(1, p.n - (p.de || 0)); for (let k = 0; k < n; k++) L.push([p.a + .05 + k * .45 / n, 'tic', .4]);
    L.push([p.a + .32, 'blip', .7]);
    if (p.boss) L.push([tps(p.boss), 'lame', .8]);
  }
  if (p.type === 'tiraille') L.push([p.a, 'frotte', .5], [tps(p.surmoi), 'pop', .6]);
  if (p.type === 'verbes') (p.mots || []).forEach(a => L.push([tps(a), 'frappe', .7]));
  if (p.type === 'monopole') L.push([p.a + .15, 'montee', .4], [p.a + .8, 'tampon', .8]);
  if (p.type === 'commentaires') [0, 1, 2, 3].forEach(i => L.push([p.a + .3 + i * .3, 'pop', .5]));
};
