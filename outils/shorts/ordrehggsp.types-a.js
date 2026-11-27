// Plans propres au short « ordrehggsp » (HGGSP : remets dans l'ordre), modèle A, habillage archives.
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, al, C = couleurs).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al, pour que l'habillage s'applique.
// melange, score, manche, pioche et commentaire reprennent ceux d'ordre1929.types-a.js (dessins propres à ce short) ;
// thermometre est propre à ce short. Le plan ordre est commun (formats-a.js).
window.SANS_ST_A = ['melange', 'score', 'manche', 'pioche', 'commentaire', 'thermometre', 'collage', 'photo'];
window.PROPRES_A = ['melange', 'score', 'manche', 'pioche', 'commentaire', 'thermometre'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, eio, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.1, i ? taille : taille * .85)); };
  const lignes = (txt, y, o) => { const L = txt.split('|'); L.forEach((s, i) => S.texte(s, W / 2, y + (i - (L.length - 1) / 2) * o.taille * 1.12, o)); };

  // douze cartes retournées qui se mélangent
  function melange(p, t) {
    const lt = t - p.a, cyc = Math.floor(lt / .55), u = eio(cl((lt % .55) / .4));
    const pos = (i, c) => { const j = Math.floor(rnd(i * 7.3 + c * 3.1) * 12); return [200 + (j % 3) * 340, 470 + Math.floor(j / 3) * 190]; };
    for (let i = 0; i < 12; i++) {
      const [x0, y0] = pos(i, cyc), [x1, y1] = pos(i, cyc + 1), kin = back(pr(t, p.a + i * .03, .3));
      const x = lerp(x0, x1, u), y = lerp(y0, y1, u) + lerp(-900, 0, kin);
      g.save(); g.translate(x, y); g.rotate((rnd(i + cyc) - .5) * .25);
      g.shadowColor = al(NOIR, .7); g.shadowBlur = 20; g.fillStyle = CREME; g.beginPath(); g.roundRect(-140, -70, 280, 140, 16); g.fill(); g.shadowColor = 'transparent';
      g.strokeStyle = OR; g.lineWidth = 5; g.beginPath(); g.roundRect(-126, -56, 252, 112, 10); g.stroke();
      S.texte('?', 0, 4, { taille: 80, coul: ROUGE, police: 'Spectral', poids: 600 }); g.restore();
    }
    deux(p.t, 1380, 120);
  }

  // tableau des trois manches (fin: true → « … / 3 »)
  function score(p, t) {
    const lt = t - p.a;
    [0, 1, 2].forEach(i => {
      const k = back(pr(t, p.a + i * .12, .3)), x = W / 2 + (i - 1) * 320, y = 760;
      g.save(); g.translate(x, y); g.scale(k, k);
      g.fillStyle = al(CREME, .07); g.strokeStyle = OR; g.lineWidth = 7; g.beginPath(); g.roundRect(-140, -150, 280, 300, 24); g.fill(); g.stroke();
      S.texte('MANCHE', 0, -95, { taille: 34, coul: GRIS, esp: 6, poids: 700 });
      S.texte(String(i + 1), 0, -20, { taille: 120, coul: CREME, police: 'Spectral', poids: 600 });
      g.strokeStyle = al(CREME, .35); g.lineWidth = 5; g.beginPath(); g.arc(0, 85, 38, 0, 7); g.stroke();
      if (p.fin) S.texte('?', 0, 88, { taille: 54, coul: OR });
      g.restore();
    });
    if (p.fin) { const kk = back(pr(t, p.a + .4, .3)); g.save(); g.translate(W / 2, 1070); g.scale(kk, kk);
      S.texte('… / 3', 0, 0, { taille: 150, coul: OR, police: 'Spectral', poids: 600, contour: NOIR, contourL: 10 }); g.restore(); }
    else { const s = 1 + .04 * Math.sin(lt * 8); g.save(); g.translate(W / 2, 1060); g.scale(s, s);
      S.texte('3 × 4 ÉVÉNEMENTS', 0, 0, { taille: 64, coul: CREME, esp: 4 }); g.restore(); }
    deux(p.t, 1330, 115);
  }

  // annonce d'une manche : grand numéro, trois points de progression
  function manche(p, t) {
    if (p.fond) O.fondImg(p.fond, 1.15 + (t - p.a) * .03, .5, .5, .3);
    const k = back(pr(t, p.a, .3));
    S.texte('MANCHE', W / 2, 520, { taille: 70, coul: CREME, esp: 18 });
    g.save(); g.translate(W / 2, 820); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(String(p.n), 0, 0, { taille: 420, coul: OR, police: 'Spectral', poids: 600, contour: NOIR, contourL: 16 }); g.restore();
    [1, 2, 3].forEach(i => { g.fillStyle = i <= p.n ? OR : al(CREME, .2); g.beginPath(); g.arc(W / 2 + (i - 2) * 90, 1080, 22, 0, 7); g.fill(); });
    const kt = eo(pr(t, p.a + .2, .3)); g.save(); g.globalAlpha = kt; deux(p.t, 1290, 120); g.restore();
  }

  // dessins quand l'événement n'a pas de photo libre : la charte de l'ONU, le sommet de la Terre
  function globe(r, lt, coul) {
    g.fillStyle = al(coul, .12); g.beginPath(); g.arc(0, 0, r, 0, 7); g.fill();
    g.strokeStyle = coul; g.lineWidth = 5; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
    g.lineWidth = 3; g.strokeStyle = al(coul, .7);
    for (let i = -2; i <= 2; i++) { g.beginPath(); g.ellipse(0, 0, Math.abs(Math.cos(i * .6 + lt * .5)) * r, r, 0, 0, 7); g.stroke(); }
    for (let j = -2; j <= 2; j++) { const y = j * r / 3; g.beginPath(); g.moveTo(-Math.sqrt(r * r - y * y), y); g.lineTo(Math.sqrt(r * r - y * y), y); g.stroke(); }
  }
  function dessin(nom, x, y, w, h, lt) {
    g.save(); g.translate(x, y);
    g.shadowColor = al(NOIR, .7); g.shadowBlur = 50; g.shadowOffsetY = 20; g.fillStyle = CREME; g.fillRect(-w / 2 - 14, -h / 2 - 14, w + 28, h + 28); g.shadowColor = 'transparent';
    g.fillStyle = NOIR; g.fillRect(-w / 2, -h / 2, w, h);
    if (nom === 'onu') {   // une charte signée : feuille, plume, globe entouré de rameaux
      g.save(); g.translate(-120, 10); g.rotate(-.06);
      g.fillStyle = CREME; g.fillRect(-170, -230, 340, 460);
      S.texte('CHARTE', 0, -180, { taille: 40, coul: NOIR, esp: 6 });
      g.fillStyle = al(NOIR, .35); for (let i = 0; i < 8; i++) g.fillRect(-130, -120 + i * 36, i === 7 ? 140 : 260, 10);
      const k = cl(lt / 1.2); g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath();
      for (let i = 0; i <= 30 * k; i++) { const u = i / 30; g.lineTo(-110 + u * 200, 190 + Math.sin(u * 18) * 14); } g.stroke();
      g.restore();
      g.save(); g.translate(190, -40); globe(110, lt, OR);
      g.strokeStyle = OR; g.lineWidth = 8;
      [-1, 1].forEach(s => { g.beginPath(); g.arc(0, 10, 150, Math.PI / 2 + s * .25, Math.PI / 2 + s * 2.2, s < 0); g.stroke();
        for (let i = 0; i < 6; i++) { const a = Math.PI / 2 + s * (.5 + i * .3), lx = Math.cos(a) * 150, ly = 10 + Math.sin(a) * 150;
          g.fillStyle = OR; g.beginPath(); g.ellipse(lx, ly, 22, 9, a + s * .9, 0, 7); g.fill(); } });
      g.restore();
      S.texte('SAN FRANCISCO', 190, 200, { taille: 34, coul: CREME, esp: 4 });
      S.texte('DESSIN', w / 2 - 20, -h / 2 + 30, { taille: 24, coul: GRIS, align: 'right', esp: 6 });
    } else if (nom === 'terre') {   // la Terre et une jeune pousse : le sommet de la Terre
      g.save(); g.translate(0, -10); globe(190, lt, OR); g.restore();
      const k = eo(cl(lt / 1.2));
      g.save(); g.translate(0, -200); g.strokeStyle = CREME; g.lineWidth = 10; g.beginPath(); g.moveTo(0, 0); g.lineTo(0, -60 * k); g.stroke();
      g.fillStyle = CREME; [-1, 1].forEach(s => { g.save(); g.translate(0, -50 * k); g.rotate(s * .7); g.beginPath(); g.ellipse(s * 34 * k, 0, 36 * k, 15 * k, 0, 0, 7); g.fill(); g.restore(); });
      g.restore();
      S.texte('RIO', -w / 2 + 40, h / 2 - 50, { taille: 54, coul: OR, align: 'left', esp: 6 });
      S.texte('DESSIN', w / 2 - 20, -h / 2 + 30, { taille: 24, coul: GRIS, align: 'right', esp: 6 });
    }
    g.restore();
  }

  // pioche : les quatre événements apparaissent un par un (lettre, image, intitulé), au mot de la voix
  function pioche(p, t) {
    const E = p.etapes || [], T0 = E.map(([a]) => tps(a)), k = T0.filter(x => t >= x).length - 1;
    O.petitTitre(p.sur, 300);
    const carteE = (i, dx, rot, kk) => {
      const [, txt, img, des, fy] = E[i], lt = t - T0[i];
      g.save(); g.translate(dx, 0); g.globalAlpha = cl(kk * 2);
      if (img) O.carte(img, W / 2, 790, 760, 580, rot, 1.06 + lt * .03, .5, fy ?? .35, { lum: .95 }); else { g.save(); g.translate(W / 2, 790); g.rotate(rot); dessin(des, 0, 0, 760, 580, lt); g.restore(); }
      g.save(); g.translate(W / 2 - 360, 530); g.scale(back(kk), back(kk)); g.fillStyle = OR; g.beginPath(); g.arc(0, 0, 70, 0, 7); g.fill();
      S.texte('ABCD'[i], 0, 6, { taille: 92, coul: NOIR }); g.restore();
      lignes(txt, 1240, { taille: 82, coul: CREME, contour: NOIR, contourL: 10, max: 980 });
      g.restore();
    };
    if (k >= 1 && t - T0[k] < .25) carteE(k - 1, lerp(0, -1100, eo((t - T0[k]) / .25)), -.03, 1);
    if (k >= 0) { const kin = back(pr(t, T0[k], .3)); carteE(k, lerp(900, 0, kin), lerp(.2, -.03, kin), pr(t, T0[k], .3)); }
    else S.texte('4 ÉVÉNEMENTS', W / 2, 800, { taille: 100, coul: CREME });
    E.forEach((_, i) => { const x = W / 2 + (i - 1.5) * 150, on = i <= k;
      g.fillStyle = on ? OR : al(CREME, .12); g.beginPath(); g.arc(x, 1470, i === k ? 50 : 40, 0, 7); g.fill();
      S.texte('ABCD'[i], x, 1474, { taille: i === k ? 56 : 44, coul: on ? NOIR : GRIS }); });
  }

  // bulle de commentaire : le score défile, puis « ? »
  function commentaire(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .35));
    deux(p.t, 520, 100);
    g.save(); g.translate(W / 2, 980); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-260, 160); g.lineTo(-330, 270); g.lineTo(-170, 165); g.closePath(); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-320, -60, 56, 0, 7); g.fill();
    S.texte('toi', -320, -58, { taille: 36, coul: NOIR });
    const n = lt < 1.4 ? String(Math.floor(lt * 7) % 4) : '?';
    S.texte('Moi :', -230, -60, { taille: 64, police: 'Spectral', poids: 600, coul: NOIR, align: 'left' });
    S.texte(n + ' / 3', 140, -62, { taille: 100, coul: lt < 1.4 ? ROUGE : OR, contour: NOIR, contourL: 6 });
    g.fillStyle = al(NOIR, .15); g.fillRect(-370, 40, 600, 22); g.fillRect(-370, 90, 420, 22);
    g.restore();
    const kf = .5 + .5 * Math.sin(lt * 7); S.texte('↓', W / 2, 1380 + kf * 20, { taille: 120, coul: OR });
  }

  // thermomètre : le niveau monte et s'arrête sous la barre des + 2 degrés
  function thermometre(p, t) {
    const lt = t - p.a, k = eo(pr(t, p.a, 1.4)), x = W / 2 - 120, yb = 1080, yh = 420, h = yb - yh;
    const yv = v => yb - 80 - v / 3 * (h - 120);   // échelle de 0 à + 3 degrés
    g.fillStyle = al(CREME, .1); g.strokeStyle = CREME; g.lineWidth = 8;
    g.beginPath(); g.roundRect(x - 50, yh, 100, h, 50); g.fill(); g.stroke();
    g.beginPath(); g.arc(x, yb + 40, 95, 0, 7); g.fillStyle = ROUGE; g.fill(); g.stroke();
    const niv = lerp(0, 1.6, k) + Math.sin(lt * 5) * .03;
    g.fillStyle = ROUGE; g.fillRect(x - 28, yv(niv), 56, yb + 40 - yv(niv));
    const kb = eo(pr(t, p.a + .3, .4)); g.save(); g.setLineDash([26, 16]); g.strokeStyle = OR; g.lineWidth = 10;
    g.beginPath(); g.moveTo(x - 140, yv(2)); g.lineTo(lerp(x - 140, W - 60, kb), yv(2)); g.stroke(); g.restore();
    [0, 1, 2, 3].forEach(v => { g.fillStyle = CREME; g.fillRect(x + 60, yv(v) - 3, 40, 6); if (v === 2) S.texte('+2', x - 70, yv(2) - 42, { taille: 50, coul: CREME, align: 'right', contour: NOIR, contourL: 8 }); else S.texte('+' + v, x + 120, yv(v), { taille: 50, coul: CREME, align: 'left', contour: NOIR, contourL: 8 }); });
    if (kb > .6) S.texte('LIMITE', W - 70, yv(2) - 50, { taille: 50, coul: OR, align: 'right', esp: 6 });
    S.texte('DEGRÉS', x + 120, yh - 40, { taille: 40, coul: GRIS, align: 'left', esp: 6 });
    const kt = back(pr(t, p.a + .4, .3)); g.save(); g.globalAlpha = cl(kt * 2); deux(p.t, 1380, 115); g.restore();
    if (p.sous) S.texte(p.sous, W / 2, 1580, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  return { melange, score, manche, pioche, commentaire, thermometre };
};

// sons propres à ces plans (discrets)
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'melange') L.push([p.a, 'frotte', .45], [p.a + .6, 'frotte', .35]);
  if (p.type === 'score') [0, 1, 2].forEach(i => L.push([p.a + i * .12, 'pop', .35]));
  if (p.type === 'manche') L.push([p.a, 'chapitre', .6]);
  if (p.type === 'pioche') (p.etapes || []).forEach(([a]) => L.push([tps(a), 'papier', .45]));
  if (p.type === 'commentaire') L.push([p.a, 'pop', .5]);
  if (p.type === 'thermometre') L.push([p.a, 'montee', .5], [p.a + .4, 'tampon', .6]);
};
