// Plans propres au short « devinehggsp » (HGGSP : devine qui c'est), modèle A, habillage terminal.
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
// devine2, silhouettes, regles, manche, citation et score reprennent ceux de devinehistoire.types-a.js ;
// avion, orbite, livre, element et nobel sont propres à ce short.
window.SANS_ST_A = ['devine2', 'silhouettes', 'regles', 'manche', 'citation', 'score', 'avion', 'orbite', 'livre', 'element', 'nobel', 'collage', 'photo'];
window.PROPRES_A = ['devine2', 'silhouettes', 'regles', 'manche', 'citation', 'score', 'avion', 'orbite', 'livre', 'element', 'nobel'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 110) => { const k = back(pr(t, a, .3)); g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const F = window.FORMATS_A ? window.FORMATS_A(O) : null;   // plan commun `devine`, réutilisé avec un chrono en plus

  // devine + chrono (anneau) entre p.chrono et p.rep
  function devine2(p, t) {
    F.devine(p, t);
    const tc = tps(p.chrono), tr = tps(p.rep);
    if (t >= tc && t < tr) {
      const u = cl((t - tc) / Math.max(.6, tr - tc)), reste = Math.ceil(tr - t), k = back(pr(t, tc, .3));
      g.save(); g.translate(W / 2, 1640); g.scale(k, k);
      g.fillStyle = al(NOIR, .8); g.beginPath(); g.arc(0, 0, 92, 0, 7); g.fill();
      g.strokeStyle = al(CREME, .2); g.lineWidth = 14; g.beginPath(); g.arc(0, 0, 78, 0, 7); g.stroke();
      g.strokeStyle = u > .6 ? ROUGE : OR; g.beginPath(); g.arc(0, 0, 78, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
      S.texte(String(Math.max(0, reste)), 0, 4, { taille: 80, coul: CREME }); g.restore();
    }
  }

  // trois têtes anonymes avec un « ? »
  function silhouettes(p, t) {
    [220, 540, 860].forEach((x, i) => {
      const k = back(pr(t, p.a + i * .15, .35)); if (k <= 0) return;
      g.save(); g.translate(x, 800); g.scale(k, k);
      S.d.tete(-30, 0, 170, { trait: CREME, fond: al(CREME, .06), ep: 7 });
      S.texte('?', 0, -40, { taille: 150, coul: i === 1 ? ROUGE : OR, contour: NOIR, contourL: 10 });
      S.texte(String(i + 1), 0, 200, { taille: 60, coul: GRIS });
      g.restore();
    });
    titrePop(p.t, 1330, t, p.a + .4, 120);
  }

  // les règles : trois bandeaux d'indices (difficile → facile) et une mosaïque qui se précise
  function regles(p, t) {
    O.petitTitre('LES RÈGLES', 360);
    const E = p.etapes || [], vus = E.filter(([a]) => t >= tps(a)).length;
    const n = [4, 6, 10, 18][Math.min(3, vus)], c = 420, x0 = W / 2 - c / 2, y0 = 440;
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
      const dx = (i + .5) / n - .5, dy = (j + .5) / n - .42, v = Math.exp(-(dx * dx * 6 + dy * dy * 4)) * .9 + rnd(i * 7 + j * 13 + n) * .1;
      g.fillStyle = al(CREME, .08 + v * .7); g.fillRect(x0 + i * c / n, y0 + j * c / n, c / n + .5, c / n + .5);
    }
    g.strokeStyle = OR; g.lineWidth = 6; g.strokeRect(x0, y0, c, c);
    E.forEach(([a, s, niv], i) => {
      const ta = tps(a); if (t < ta) return;
      const k = back(pr(t, ta, .3)), y = 1020 + i * 170, coul = [ROUGE, OR, CREME][i];
      g.save(); g.translate(lerp(-W, 0, cl(k)), 0);
      g.fillStyle = al(coul, .16); g.beginPath(); g.roundRect(110, y - 65, 860, 130, 65); g.fill();
      g.strokeStyle = coul; g.lineWidth = 4; g.stroke();
      S.texte(s, 160, y, { taille: 56, coul: CREME, align: 'left' });
      S.texte(niv, 930, y, { taille: 52, coul, align: 'right', poids: 700 });
      g.restore();
    });
  }

  // carte « MANCHE n / 3 » avec le thème du programme
  function manche(p, t) {
    const k = back(pr(t, p.a, .35));
    S.texte('MANCHE', W / 2, 420, { taille: 70, coul: CREME, esp: 18 });
    g.save(); g.translate(W / 2, 640); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(p.n + ' / 3', 0, 0, { taille: 250, police: 'Spectral', poids: 600, coul: OR, ombre: al(OR, .45), flou: 40 }); g.restore();
    const kd = eo(pr(t, p.a + .2, .4)); g.save(); g.translate(W / 2, 1080); g.scale(kd, kd);
    g.fillStyle = al(CREME, .06); g.beginPath(); g.arc(0, 0, 220, 0, 7); g.fill();
    g.strokeStyle = OR; g.lineWidth = 8; g.setLineDash([24, 16]); g.lineDashOffset = -t * 60; g.stroke(); g.setLineDash([]);
    S.d.tete(-25, 10, 120, { trait: CREME, fond: al(NOIR, .5), ep: 6 });
    S.texte('?', 0, -10, { taille: 150, coul: ROUGE, contour: NOIR, contourL: 10 }); g.restore();
    const kb = eo(pr(t, p.a + .1, .3)); g.save(); g.translate(lerp(-W, 0, kb), 0);
    g.fillStyle = ROUGE; g.fillRect(0, 1400, W, 130); S.texte(p.matiere, W / 2, 1467, { taille: 70, coul: CREME, esp: 4, max: 1000 }); g.restore();
  }

  // citation sur un papier, guillemets et légende
  function citation(p, t) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 860); g.rotate(lerp(.2, -.03, cl(k))); g.scale(k, k);
    g.shadowColor = al(NOIR, .8); g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-440, -300, 880, 600); g.shadowColor = 'transparent';
    S.texte('“', -330, -170, { taille: 260, police: 'Spectral', poids: 600, coul: ROUGE });
    const L = p.t.split('|'); L.forEach((s, i) => S.texte(s, 0, -30 + i * 120, { taille: 110, coul: NOIR, max: 800 }));
    g.restore();
    const kd = eo(pr(t, p.a + .3, .3)); g.save(); g.globalAlpha = kd;
    S.texte('— ' + p.an + ' —', W / 2, 1300, { taille: 80, police: 'Spectral', poids: 600, coul: OR, max: 980 }); g.restore();
  }

  // ton score : les trois visages révélés
  function score(p, t) {
    O.petitTitre('TON SCORE', 360);
    (p.imgs || []).forEach(([nom, lab], i) => {
      const k = back(pr(t, p.a + i * .15, .35)); if (k <= 0) return;
      const x = W / 2 + (i - 1) * 330, y = 760;
      g.save(); g.translate(x, lerp(-400, y, cl(k))); g.rotate((i - 1) * .05);
      O.carte(nom, 0, 0, 280, 360, 0, 1.15, .5, .3);
      S.texte(lab, 0, 240, { taille: 44, coul: OR, max: 300 });
      g.restore();
    });
    const kt = back(pr(t, p.a + .5, .3)); g.save(); g.globalAlpha = cl(kt * 2); g.translate(W / 2, 1250); g.scale(lerp(1.5, 1, kt), lerp(1.5, 1, kt));
    S.texte('? / 3', 0, 0, { taille: 200, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 12 }); g.restore();
    S.texte('COMBIEN TU EN AS TROUVÉS ?', W / 2, 1480, { taille: 62, coul: OR, max: 980 });
  }

  // un avion de chasse qui traverse l'écran, traînées de vitesse
  function avion(p, t) {
    const lt = t - p.a, k = eo(pr(t, p.a, .6)), x = lerp(-250, W / 2 + 40, k) + lt * 30, y = 820 + Math.sin(lt * 2.2) * 14;
    for (let i = 0; i < 14; i++) {   // traînées
      const yy = 640 + rnd(i * 3.7) * 380, l = 160 + rnd(i * 1.3) * 300, xx = ((rnd(i * 9.1) * W * 1.6) - lt * 1400 * (.6 + rnd(i))) % (W * 1.6);
      g.fillStyle = al(CREME, .08 + rnd(i * 5) * .12); g.fillRect(xx < 0 ? xx + W * 1.6 : xx, yy, l, 4);
    }
    g.save(); g.translate(x, y); g.rotate(-.06 + Math.sin(lt * 1.7) * .03); g.scale(1.5, 1.5);
    g.fillStyle = al(OR, .25); g.beginPath(); g.moveTo(-150, -8); g.lineTo(-330, 0); g.lineTo(-150, 8); g.closePath(); g.fill();   // flamme
    g.fillStyle = CREME; g.strokeStyle = NOIR; g.lineWidth = 4;
    g.beginPath(); g.moveTo(190, 0); g.quadraticCurveTo(120, -26, 40, -24); g.lineTo(-150, -18); g.lineTo(-150, 18); g.lineTo(40, 24); g.quadraticCurveTo(120, 26, 190, 0); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(40, -18); g.lineTo(-70, -150); g.lineTo(-110, -150); g.lineTo(-60, -18); g.closePath(); g.fill(); g.stroke();   // aile haute
    g.beginPath(); g.moveTo(40, 18); g.lineTo(-70, 150); g.lineTo(-110, 150); g.lineTo(-60, 18); g.closePath(); g.fill(); g.stroke();      // aile basse
    g.beginPath(); g.moveTo(-110, -16); g.lineTo(-160, -90); g.lineTo(-180, -90); g.lineTo(-150, -16); g.closePath(); g.fill(); g.stroke();   // dérive
    g.fillStyle = OR; g.beginPath(); g.ellipse(90, -14, 34, 12, -.1, 0, 7); g.fill();   // cockpit
    g.fillStyle = ROUGE; g.beginPath(); g.arc(-30, 80, 14, 0, 7); g.fill(); g.beginPath(); g.arc(-30, -80, 14, 0, 7); g.fill();
    g.restore();
    titrePop(p.t, 1320, t, p.a + .3, 120);
    if (p.sous) S.texte(p.sous, W / 2, 1480, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  // la Terre, une orbite et un compteur de minutes
  function orbite(p, t) {
    const lt = t - p.a, cx = W / 2, cy = 800, R = 230, k = eo(pr(t, p.a, 1.8));
    g.save(); g.translate(cx, cy);
    g.fillStyle = al(OR, .12); g.beginPath(); g.arc(0, 0, R, 0, 7); g.fill();
    g.strokeStyle = al(OR, .5); g.lineWidth = 3;
    for (let i = -2; i <= 2; i++) { g.beginPath(); g.ellipse(0, 0, Math.abs(Math.cos(i * .55 + lt * .4)) * R, R, 0, 0, 7); g.stroke(); }
    for (let j = -2; j <= 2; j++) { const yy = j * R / 3; g.beginPath(); g.ellipse(0, yy, Math.sqrt(R * R - yy * yy), 14, 0, 0, 7); g.stroke(); }
    g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.arc(0, 0, R, 0, 7); g.stroke();
    // orbite inclinée et trace de la capsule
    g.rotate(-.35);
    g.strokeStyle = al(CREME, .25); g.lineWidth = 4; g.setLineDash([14, 12]); g.beginPath(); g.ellipse(0, 0, 400, 150, 0, 0, 7); g.stroke(); g.setLineDash([]);
    const a0 = -Math.PI / 2, a1 = a0 + k * 6.283;
    g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.ellipse(0, 0, 400, 150, 0, a0, a1); g.stroke();
    const px = Math.cos(a1) * 400, py = Math.sin(a1) * 150;
    g.fillStyle = CREME; g.beginPath(); g.arc(px, py, 20, 0, 7); g.fill(); g.strokeStyle = ROUGE; g.lineWidth = 5; g.stroke();
    g.restore();
    const n = Math.round(108 * k);
    S.texte(String(n), W / 2, 1270, { taille: 230, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 });
    S.texte(p.t || 'MINUTES', W / 2, 1420, { taille: 70, coul: CREME, esp: 8 });
    if (p.sous) S.texte(p.sous, W / 2, 1520, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  // un livre fermé au titre caché, une date, une mention
  function livre(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, 780); g.rotate(lerp(.25, -.05, cl(k)) + Math.sin(lt * 1.5) * .01); g.scale(k, k);
    g.shadowColor = al(NOIR, .8); g.shadowBlur = 50; g.shadowOffsetY = 20;
    g.fillStyle = al(CREME, .9); g.fillRect(-250, -330, 500, 660); g.shadowColor = 'transparent';
    g.fillStyle = al(OR, .55); g.fillRect(-250, -330, 46, 660);
    g.strokeStyle = NOIR; g.lineWidth = 4; g.strokeRect(-180, -260, 380, 520);
    g.fillStyle = al(NOIR, .75); [-150, -100].forEach((y, i) => g.fillRect(-140, y, i ? 220 : 300, 26));
    S.texte('? ? ?', 10, 20, { taille: 110, coul: ROUGE, police: 'Spectral', poids: 600 });
    S.texte(p.an || '', 10, 190, { taille: 70, coul: NOIR, police: 'Spectral', poids: 600 });
    g.restore();
    const ks = pr(t, p.a + .5, .3); if (ks > 0) O.tampon(p.tampon || 'POSTHUME', W / 2 + 190, 1080, ks, -.12, 70);
    titrePop(p.t, 1360, t, p.a + .3, 110);
  }

  // une case du tableau périodique, des particules qui s'échappent (radioactivité)
  function element(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .35)), cx = W / 2, cy = 760;
    for (let i = 0; i < 26; i++) {
      const ang = rnd(i * 2.3) * 6.283, v = (lt * (180 + rnd(i) * 220) + rnd(i * 7) * 400) % 520;
      g.fillStyle = al(i % 3 ? OR : ROUGE, cl(1 - v / 520) * .8);
      g.beginPath(); g.arc(cx + Math.cos(ang) * (240 + v), cy + Math.sin(ang) * (240 + v), 8 + rnd(i * 3) * 6, 0, 7); g.fill();
    }
    g.save(); g.translate(cx, cy); g.scale(k, k); g.rotate(-.03);
    const pulse = 1 + .03 * Math.sin(lt * 6);
    g.shadowColor = OR; g.shadowBlur = 50 * pulse; g.fillStyle = al(NOIR, .9); g.fillRect(-230, -230, 460, 460); g.shadowBlur = 0;
    g.strokeStyle = OR; g.lineWidth = 10; g.strokeRect(-230, -230, 460, 460);
    S.texte(String(p.num || '?'), -200, -180, { taille: 64, coul: CREME, align: 'left' });
    S.texte(p.sym || '?', 0, 10, { taille: 230, police: 'Spectral', poids: 600, coul: OR });
    S.texte(p.nom || '???', 0, 170, { taille: 50, coul: CREME, esp: 6, max: 420 });
    g.restore();
    titrePop(p.t, 1330, t, p.a + .3, 110);
    if (p.sous) S.texte(p.sous, W / 2, 1490, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  // deux médailles qui tombent, avec leur année et leur science
  function nobel(p, t) {
    (p.medailles || []).forEach(([an, sc], i) => {
      const k = back(pr(t, p.a + i * .25, .4)); if (k <= 0) return;
      const x = W / 2 + (i - .5) * 420, y = lerp(-300, 780, cl(k)), r = 170;
      g.save(); g.translate(x, y); g.rotate((i ? .08 : -.08) + Math.sin((t - p.a) * 2 + i) * .03);
      g.strokeStyle = ROUGE; g.lineWidth = 26; g.beginPath(); g.moveTo(-60, -r - 260); g.lineTo(0, -r); g.lineTo(60, -r - 260); g.stroke();
      g.shadowColor = al(OR, .6); g.shadowBlur = 40; g.fillStyle = OR; g.beginPath(); g.arc(0, 0, r, 0, 7); g.fill(); g.shadowBlur = 0;
      g.strokeStyle = al(NOIR, .5); g.lineWidth = 6; g.beginPath(); g.arc(0, 0, r - 22, 0, 7); g.stroke();
      S.texte('NOBEL', 0, -40, { taille: 54, coul: NOIR, esp: 4 });
      S.texte(an, 0, 40, { taille: 76, police: 'Spectral', poids: 600, coul: NOIR });
      g.restore();
      const ks = eo(pr(t, p.a + i * .25 + .3, .3)); g.save(); g.globalAlpha = ks;
      S.texte(sc, x, 1040, { taille: 60, coul: CREME, esp: 4, max: 400 }); g.restore();
    });
    titrePop(p.t, 1330, t, p.a + .6, 110);
  }

  return { devine2, silhouettes, regles, manche, citation, score, avion, orbite, livre, element, nobel };
};
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'devine2' && p.sons) {
    (p.indices || []).forEach(([a]) => L.push([tps(a), 'pop', .5]));
    const tc = tps(p.chrono), tr = tps(p.rep);
    for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]);
    L.push([tr, 'gong', .8]);
  }
  if (p.type === 'silhouettes') [0, 1, 2].forEach(i => L.push([p.a + i * .15, 'pop', .4]));
  if (p.type === 'regles') (p.etapes || []).forEach(([a]) => L.push([tps(a), 'blip', .5]));
  if (p.type === 'manche') L.push([p.a, 'chapitre', .8]);
  if (p.type === 'citation') L.push([p.a, 'papier', .5]);
  if (p.type === 'score') [0, 1, 2].forEach(i => L.push([p.a + i * .15, 'pop', .45]));
  if (p.type === 'avion') L.push([p.a, 'whoosh', .7]);
  if (p.type === 'orbite') L.push([p.a, 'montee', .5]);
  if (p.type === 'livre') L.push([p.a, 'papier', .5], [p.a + .5, 'tampon', .7]);
  if (p.type === 'element') L.push([p.a, 'bip', .4]);
  if (p.type === 'nobel') L.push([p.a, 'pop', .45], [p.a + .25, 'pop', .45]);
};
