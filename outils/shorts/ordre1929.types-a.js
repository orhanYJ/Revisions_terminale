// Plans propres au short « Remets dans l'ordre : de la crise de 1929 à la guerre » (modèle A, habillage « archives »).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, al, C = couleurs).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al, pour que l'habillage s'applique.
// Le plan ordre est commun (formats-a.js).
window.SANS_ST_A = ['melange', 'score', 'manche', 'pioche', 'commentaire', 'collage'];
window.PROPRES_A = ['melange', 'score', 'manche', 'pioche', 'commentaire'];
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

  // tableau des trois manches (fin: true → « ? / 3 »)
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

  // dessins quand l'événement n'a pas de photo
  function dessin(nom, x, y, w, h, lt) {
    g.save(); g.translate(x, y);
    g.shadowColor = al(NOIR, .7); g.shadowBlur = 50; g.shadowOffsetY = 20; g.fillStyle = CREME; g.fillRect(-w / 2 - 14, -h / 2 - 14, w + 28, h + 28); g.shadowColor = 'transparent';
    g.fillStyle = NOIR; g.fillRect(-w / 2, -h / 2, w, h);
    if (nom === 'or') {   // lingots d'or empilés, une livre sterling qui s'en échappe
      const lingot = (cx, cy) => { g.fillStyle = OR; g.strokeStyle = NOIR; g.lineWidth = 4; g.beginPath();
        g.moveTo(cx - 110, cy + 40); g.lineTo(cx + 110, cy + 40); g.lineTo(cx + 80, cy - 40); g.lineTo(cx - 80, cy - 40); g.closePath(); g.fill(); g.stroke(); };
      [[-120, 150], [120, 150], [0, 70]].forEach(([cx, cy]) => lingot(cx, cy));
      const up = (lt * 120) % 200;
      g.save(); g.globalAlpha = 1 - up / 200; S.texte('£', 0, -80 - up * .6, { taille: 170, coul: CREME, police: 'Spectral', poids: 600 }); g.restore();
      S.texte('ÉTALON-OR', 0, -230, { taille: 50, coul: OR, esp: 8 });
    } else if (nom === 'rhin') {   // schéma : le Rhin, la zone démilitarisée, des troupes qui y entrent
      g.fillStyle = al(ROUGE, .25); g.fillRect(-w / 2, -h / 2, w * .55, h);
      g.strokeStyle = OR; g.lineWidth = 16; g.beginPath();
      for (let i = 0; i <= 20; i++) { const yy = -h / 2 + i * h / 20, xx = -w / 2 + w * .55 + Math.sin(i * .9) * 30; i ? g.lineTo(xx, yy) : g.moveTo(xx, yy); } g.stroke();
      S.texte('RHIN', -w / 2 + w * .55 + 90, -h / 2 + 60, { taille: 44, coul: OR });
      S.texte('ZONE', -w / 2 + w * .27, -40, { taille: 50, coul: CREME }); S.texte('DÉMILITARISÉE', -w / 2 + w * .27, 20, { taille: 34, coul: CREME, max: w * .5 });
      const k = cl(lt / 1.2); S.d.fleche(w / 2 - 40, 140, lerp(w / 2 - 60, -w / 2 + 100, eo(k)), 140, 1, { trait: ROUGE, ep: 18 });
      S.texte('TROUPES', w / 2 - 140, 210, { taille: 36, coul: ROUGE });
      S.texte('SCHÉMA', w / 2 - 20, -h / 2 + 30, { taille: 24, coul: GRIS, align: 'right', esp: 6 });
    }
    g.restore();
  }

  // pioche : les quatre événements apparaissent un par un (lettre, image, intitulé), au mot de la voix
  function pioche(p, t) {
    const E = p.etapes || [], T0 = E.map(([a]) => tps(a)), k = T0.filter(x => t >= x).length - 1;
    O.petitTitre(p.sur, 300);
    const carteE = (i, dx, rot, kk) => {
      const [, txt, img, des] = E[i], lt = t - T0[i];
      g.save(); g.translate(dx, 0); g.globalAlpha = cl(kk * 2);
      if (img) O.carte(img, W / 2, 790, 760, 580, rot, 1.06 + lt * .03, .5, .35, { lum: .95 }); else { g.save(); g.translate(W / 2, 790); g.rotate(rot); dessin(des, 0, 0, 760, 580, lt); g.restore(); }
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

  return { melange, score, manche, pioche, commentaire };
};

// sons propres à ces plans (discrets)
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'melange') L.push([p.a, 'frotte', .45], [p.a + .6, 'frotte', .35]);
  if (p.type === 'score') [0, 1, 2].forEach(i => L.push([p.a + i * .12, 'pop', .35]));
  if (p.type === 'manche') L.push([p.a, 'chapitre', .6]);
  if (p.type === 'pioche') (p.etapes || []).forEach(([a]) => L.push([tps(a), 'papier', .45]));
  if (p.type === 'commentaire') L.push([p.a, 'pop', .5]);
};
