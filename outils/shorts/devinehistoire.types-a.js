// Plans propres au short « devinehistoire » (devine qui c'est : trois hommes du XXe siècle), modèle A, habillage alerte.
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
window.SANS_ST_A = ['devine2', 'silhouettes', 'regles', 'manche', 'citation', 'affiche', 'usine', 'score'];
window.PROPRES_A = ['devine2', 'silhouettes', 'regles', 'manche', 'citation', 'affiche', 'usine', 'score'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 110) => { const k = back(pr(t, a, .3)); g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const F = window.FORMATS_A ? window.FORMATS_A(O) : null;   // plan commun `devine`, réutilisé avec un chrono en plus

  // devine + chrono (anneau) entre p.chrono et p.rep
  function devine2(p, t) {
    F.devine(p, t);
    const tc = tps(p.chrono), tr = tps(p.rep);
    if (t >= tc && t < tr) {
      const u = cl((t - tc) / Math.max(.6, tr - tc)), reste = Math.ceil(tr - t), k = back(pr(t, tc, .3));
      g.save(); g.translate(W / 2, 1610); g.scale(k, k);
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
    // mosaïque : 4, puis 8, 16, 32 cases de côté
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

  // carte « MANCHE n / 3 » avec le thème du cours
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
    g.fillStyle = ROUGE; g.fillRect(0, 1400, W, 130); S.texte(p.matiere, W / 2, 1467, { taille: 76, coul: CREME, esp: 4, max: 1000 }); g.restore();
  }

  // citation sur un papier, guillemets et date
  function citation(p, t) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 860); g.rotate(lerp(.2, -.03, cl(k))); g.scale(k, k);
    g.shadowColor = al(NOIR, .8); g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-440, -300, 880, 600); g.shadowColor = 'transparent';
    S.texte('“', -330, -170, { taille: 260, police: 'Spectral', poids: 600, coul: ROUGE });
    const L = p.t.split('|'); L.forEach((s, i) => S.texte(s, 0, -30 + i * 120, { taille: 110, coul: NOIR, max: 800 }));
    g.restore();
    const kd = eo(pr(t, p.a + .3, .3)); g.save(); g.globalAlpha = kd;
    S.texte('— ' + p.an + ' —', W / 2, 1300, { taille: 90, police: 'Spectral', poids: 600, coul: OR }); g.restore();
  }

  // affiche de propagande : rayons rouges, étoile, slogan
  function affiche(p, t) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 880); g.scale(k, k);
    g.fillStyle = ROUGE; g.fillRect(-420, -560, 840, 1120);
    g.save(); g.beginPath(); g.rect(-420, -560, 840, 1120); g.clip(); g.rotate(t * .1);
    for (let i = 0; i < 16; i++) { g.fillStyle = al(NOIR, .14); g.beginPath(); g.moveTo(0, -200); g.arc(0, -200, 1400, i * Math.PI / 8, i * Math.PI / 8 + Math.PI / 16); g.closePath(); g.fill(); }
    g.restore();
    g.fillStyle = OR; g.beginPath();
    for (let i = 0; i < 10; i++) { const r = i % 2 ? 70 : 170, a = -Math.PI / 2 + i * Math.PI / 5; g.lineTo(Math.cos(a) * r, -200 + Math.sin(a) * r); }
    g.closePath(); g.fill();
    const L = p.t.split('|'); L.forEach((s, i) => S.texte(s, 0, 120 + i * 120, { taille: 100, coul: CREME, contour: NOIR, contourL: 10, max: 760 }));
    S.texte(p.an, 0, 430, { taille: 80, police: 'Spectral', poids: 600, coul: OR });
    g.lineWidth = 12; g.strokeStyle = OR; g.strokeRect(-400, -540, 800, 1080);
    g.restore();
  }

  // le plan quinquennal : une usine et des barres qui montent (dessin, sans chiffres)
  function usine(p, t) {
    const lt = t - p.a;
    S.texte(p.an, W / 2, 400, { taille: 130, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 10 });
    // usine
    const y = 1020;
    g.fillStyle = al(CREME, .9);
    g.beginPath(); g.moveTo(140, y); g.lineTo(140, y - 160); g.lineTo(290, y - 260); g.lineTo(290, y - 160); g.lineTo(440, y - 260); g.lineTo(440, y - 160); g.lineTo(590, y - 260); g.lineTo(590, y); g.closePath(); g.fill();
    [[200, 300], [500, 360]].forEach(([x, h], i) => {
      g.fillStyle = al(CREME, .9); g.fillRect(x, y - h, 50, h);
      for (let j = 0; j < 5; j++) { const u = ((lt * .6 + j / 5 + i * .3) % 1); g.fillStyle = al(GRIS, .6 * (1 - u)); g.beginPath(); g.arc(x + 25 + u * 120, y - h - 40 - u * 260, 30 + u * 50, 0, 7); g.fill(); }
    });
    // barres qui montent
    for (let i = 0; i < 5; i++) {
      const k = eo(pr(t, p.a + .15 + i * .12, .4)), h = (120 + i * 70) * k;
      g.fillStyle = i === 4 ? ROUGE : OR; g.fillRect(660 + i * 64, y - h, 48, h);
    }
    g.fillStyle = CREME; g.fillRect(120, y, 860, 8);
    titrePop(p.t, 1300, t, p.a + .2, 120);
    S.texte('5 ans pour industrialiser', W / 2, 1480, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
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

  return { devine2, silhouettes, regles, manche, citation, affiche, usine, score };
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
  if (p.type === 'affiche') L.push([p.a, 'drop', .7]);
  if (p.type === 'usine') L.push([p.a, 'montee', .5]);
  if (p.type === 'score') [0, 1, 2].forEach(i => L.push([p.a + i * .15, 'pop', .45]));
};
