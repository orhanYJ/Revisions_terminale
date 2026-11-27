// Plans propres au short « quidithlp » (« HLP : qui a dit ça ? », quatre citations), modèle A, habillage « jeu ».
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
window.SANS_ST_A = ['cases', 'trois', 'num', 'citation', 'auteur', 'siecles', 'sot', 'voyant', 'piege', 'penser', 'score'];
window.PROPRES_A = ['cases', 'trois', 'num', 'citation', 'auteur', 'siecles', 'sot', 'voyant', 'piege', 'penser', 'score'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const claque = (s, y, ta, t, o) => { const k = back(pr(t, ta, .3)); if (k <= 0) return; g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
    S.texte(s, 0, 0, Object.assign({ taille: 100, coul: CREME, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };
  const deuxClaque = (txt, y, ta, t, taille = 110) => { const k = back(pr(t, ta, .3)); if (k <= 0) return; g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  // un livre fermé, vu de face (couverture, titre, date)
  function livre(x, y, w, h, titre, date, c) {
    g.save(); g.translate(x, y);
    g.fillStyle = al(NOIR, .5); g.fillRect(-w / 2 + 14, -h / 2 + 14, w, h);
    g.fillStyle = c; g.fillRect(-w / 2, -h / 2, w, h);
    g.fillStyle = al(NOIR, .25); g.fillRect(-w / 2, -h / 2, 26, h);
    g.strokeStyle = al(NOIR, .5); g.lineWidth = 4; g.strokeRect(-w / 2 + 44, -h / 2 + 24, w - 68, h - 48);
    S.texte(titre, 13, -h * .12, { taille: 52, police: 'Spectral', poids: 600, coul: NOIR, max: w - 90 });
    S.texte(date, 13, h * .18, { taille: 64, police: 'Spectral', poids: 600, coul: NOIR });
    g.restore();
  }

  // quatre cases « ? » ; p.fin : la question de la fin (boucle)
  function cases(p, t) {
    if (!p.fin) { claque('HLP', 380, p.a + .02, t, { taille: 110, coul: ROUGE }); claque('4 CITATIONS', 530, p.a + .12, t, { taille: 150, coul: OR }); }
    for (let i = 0; i < 4; i++) {
      const k = back(pr(t, p.a + .2 + i * .12, .3)), x = 165 + i * 250, y = 880;
      if (k <= 0) continue;
      g.save(); g.translate(x, y); g.scale(k, k); g.rotate(i % 2 ? .04 : -.04);
      const on = p.fin && Math.floor((t - p.a) * 4 + i) % 4 === 0;
      g.fillStyle = on ? al(OR, .25) : al(CREME, .07); g.strokeStyle = on ? OR : CREME; g.lineWidth = 6;
      g.beginPath(); g.roundRect(-100, -100, 200, 200, 22); g.fill(); g.stroke();
      S.texte('?', 0, 6, { taille: 130, coul: on ? OR : CREME, police: 'Spectral', poids: 600 });
      g.restore();
    }
    if (p.fin) deuxClaque('ET TOI…|COMBIEN SUR 4 ?', 1300, p.a + .1, t, 110);
    else if (t >= tps(p.q)) deuxClaque('COMBIEN TU EN|RECONNAIS ?', 1300, tps(p.q), t, 110);
  }

  // trois auteurs mystère ; à p.un, la roulette : un seul l'a écrite
  function trois(p, t) {
    const tu = tps(p.un), roul = t >= tu ? Math.floor((t - tu) * 9) % 3 : -1;
    ['A', 'B', 'C'].forEach((s, i) => {
      const k = back(pr(t, p.a + i * .15, .3)), x = 200 + i * 340, y = 840;
      if (k <= 0) return;
      const on = roul === i;
      g.save(); g.translate(x, y); g.scale(k, k);
      if (on) { g.shadowColor = OR; g.shadowBlur = 40; }
      g.fillStyle = on ? al(OR, .2) : al(CREME, .06); g.strokeStyle = on ? OR : al(CREME, .5); g.lineWidth = 6;
      g.beginPath(); g.roundRect(-140, -210, 280, 420, 26); g.fill(); g.stroke(); g.shadowBlur = 0;
      S.d.tete(10, -30, 150, { trait: on ? OR : CREME, fond: al(NOIR, .7), ep: 7 });
      S.texte('?', 20, -50, { taille: 110, coul: on ? OR : CREME, police: 'Spectral', poids: 600 });
      S.texte(s, 0, 160, { taille: 70, coul: OR });
      g.restore();
    });
    if (t < tu) claque('TROIS AUTEURS', 1350, p.a + .2, t, { taille: 120 });
    else deuxClaque('UN SEUL|L’A ÉCRITE', 1350, tu, t, 120);
  }

  // le numéro de la citation
  function num(p, t) {
    O.petitTitre(p.t || 'CITATION', 520, p.t ? ROUGE : OR);
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2 - 60, 880); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k));
    S.texte(String(p.n), 0, 0, { taille: 480, police: 'Spectral', poids: 600, coul: OR, ombre: al(OR, .45), flou: 50 });
    g.restore();
    S.texte('/ 4', W / 2 + 190, 980, { taille: 110, police: 'Spectral', poids: 600, coul: CREME });
    for (let i = 0; i < 4; i++) { g.fillStyle = i < p.n ? OR : al(CREME, .2); g.beginPath(); g.arc(W / 2 - 150 + i * 100, 1260, 22, 0, 7); g.fill(); }
  }

  // la citation, écrite au fil de la voix
  function citation(p, t) {
    O.petitTitre('CITATION ' + p.n + ' / 4', 420);
    S.texte('«', 150, 560, { taille: 300, police: 'Spectral', poids: 600, coul: al(OR, .25) });
    const L = p.q.split('|'), tot = L.join('').length, dur = Math.max(.6, (p.b - p.a) * .8), n = Math.floor(cl((t - p.a) / dur) * tot);
    let c = 0;
    L.forEach((s, i) => {
      const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte(vis, W / 2, 860 + (i - (L.length - 1) / 2) * 130, { taille: 92, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 980 });
    });
    const kq = eo(pr(t, p.a + dur * .7, .4)); if (kq > 0) { g.save(); g.globalAlpha = kq * (.75 + .25 * Math.sin(t * 8));
      S.texte('QUI A DIT ÇA ?', W / 2, 1380, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 10 }); g.restore(); }
  }

  // l'auteur révélé : portrait, nom, œuvre, date
  function auteur(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte(p.img, W / 2 + lerp(300, 0, k), 700, 580, 740, lerp(.15, -.03, k), 1.05 + (t - p.a) * .03, .5, .35, { lum: .95 });
    claque(p.t, 1210, p.a + .1, t, { taille: 150, coul: OR, contourL: 12 });
    const ko = eo(pr(t, p.a + .25, .35)); g.save(); g.globalAlpha = ko;
    S.texte(p.oeuvre, W / 2, 1345, { taille: 58, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 960 });
    S.texte(p.date, W / 2, 1450, { taille: 84, police: 'Spectral', poids: 600, coul: CREME });
    g.restore();
  }

  // Montaigne avant Rousseau : deux livres sur une frise, « + 2 siècles »
  function siecles(p, t) {
    O.petitTitre('L’ÉCRITURE DE SOI', 380);
    const k1 = back(pr(t, p.a, .3)), k2 = back(pr(t, p.a + .5, .3)), kf = eo(pr(t, p.a + .2, .5));
    g.save(); g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.moveTo(120, 1150); g.lineTo(120 + 840 * kf, 1150); g.stroke(); g.restore();
    if (k1 > 0) { g.save(); g.translate(300, 820); g.scale(k1, k1); livre(0, 0, 330, 440, 'ESSAIS', '1580', OR); g.restore(); S.texte('MONTAIGNE', 300, 1220, { taille: 52, coul: OR }); }
    if (k2 > 0) { g.save(); g.translate(780, 820); g.scale(k2, k2); livre(0, 0, 330, 440, 'CONFESSIONS', '1782', CREME); g.restore(); S.texte('ROUSSEAU', 780, 1220, { taille: 52, coul: CREME }); }
    if (t > p.a + .7) S.d.fleche(330, 1050, 750, 1050, eo(pr(t, p.a + .7, .4)), { trait: ROUGE, ep: 12 });
    if (t > p.a + .9) deuxClaque('2 SIÈCLES|D’AVANCE', 1440, p.a + .9, t, 110);
  }

  // Pascal se moque de Montaigne : le portrait encadré, puis le tampon « SOT PROJET ! »
  function sot(p, t) {
    O.fondImg('pensees', 1.15 + (t - p.a) * .02, .5, .4, .35);
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 780); g.rotate(lerp(-.2, .03, k)); g.scale(lerp(.7, 1, k), lerp(.7, 1, k));
    g.fillStyle = OR; g.fillRect(-300, -380, 600, 760);
    g.restore();
    O.carte('montaigne', W / 2, 780, 520, 680, .03, 1.05, .5, .35, { lum: .95 });
    claque('PASCAL CONTRE', 1270, p.a + .15, t, { taille: 90, coul: CREME });
    claque('MONTAIGNE', 1380, p.a + .3, t, { taille: 120, coul: OR });
    const ts = tps(p.sot); if (t >= ts) O.tampon('SOT PROJET !', W / 2, 760, pr(t, ts, .3), -.15, 86, ROUGE);
  }

  // Rimbaud : un œil qui s'ouvre ; « JE » devient « UN AUTRE »
  function voyant(p, t) {
    const lt = t - p.a, ko = eo(pr(t, p.a, .6));
    g.save(); g.translate(W / 2, 820);
    for (let i = 0; i < 24; i++) { const a = i * Math.PI / 12 + lt * .3, r1 = 330, r2 = 330 + 90 + 40 * Math.sin(lt * 4 + i);
      g.strokeStyle = al(OR, .5 * ko); g.lineWidth = 8; g.beginPath(); g.moveTo(Math.cos(a) * r1, Math.sin(a) * r1 * .7); g.lineTo(Math.cos(a) * r2, Math.sin(a) * r2 * .7); g.stroke(); }
    g.fillStyle = CREME; g.strokeStyle = OR; g.lineWidth = 12;
    g.beginPath(); g.moveTo(-300, 0); g.quadraticCurveTo(0, -260 * ko, 300, 0); g.quadraticCurveTo(0, 260 * ko, -300, 0); g.closePath(); g.fill(); g.stroke();
    g.save(); g.clip(); g.fillStyle = OR; g.beginPath(); g.arc(Math.sin(lt * 2) * 40, 0, 120, 0, 7); g.fill();
    g.fillStyle = NOIR; g.beginPath(); g.arc(Math.sin(lt * 2) * 40, 0, 55, 0, 7); g.fill(); g.restore();
    g.restore();
    const kj = pr(t, p.a + .5, .5);
    S.texte('JE', lerp(W / 2, 210, eo(kj)), 1260, { taille: 110, coul: al(CREME, 1 - kj * .5), contour: NOIR, contourL: 10 });
    if (kj > 0) { S.texte('=', 365, 1260, { taille: 100, coul: al(CREME, kj) }); S.texte('UN AUTRE', lerp(W / 2, 715, eo(kj)), 1260, { taille: 110, coul: al(OR, kj), contour: NOIR, contourL: 10, max: 560 }); }
    deuxClaque('LE POÈTE|SE FAIT VOYANT', 1460, p.a + .2, t, 100);
  }

  // le piège : Kant, tampon « PIÈGE »
  function piege(p, t) {
    const k = eo(pr(t, p.a, .3));
    O.carte(p.img, W / 2, 760, 560, 720, lerp(-.15, .03, k), 1.05, .5, .35);
    O.tampon('PIÈGE', W / 2, 980, pr(t, p.a + .2, .3), -.12, 120, ROUGE);
    claque(p.t, 1290, p.a + .1, t, { taille: 140, coul: OR, contourL: 12 });
    const ks = eo(pr(t, p.a + .35, .3)); g.save(); g.globalAlpha = ks;
    S.texte(p.sous, W / 2, 1420, { taille: 60, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 960 }); g.restore();
  }

  // Arendt : une rangée d'hommes ordinaires, tous pareils ; celui du milieu s'allume
  function penser(p, t) {
    const lt = t - p.a;
    for (let i = 0; i < 5; i++) {
      const k = back(pr(t, p.a + i * .08, .3)); if (k <= 0) continue;
      const x = 140 + i * 200, on = i === 2;
      g.save(); g.translate(x, 860); g.scale(k * (on ? 1.15 : .9), k * (on ? 1.15 : .9));
      S.d.tete(0, 0, 150, { trait: on ? OR : al(CREME, .45), fond: al(NOIR, .8), ep: 7 });
      g.fillStyle = on ? OR : al(CREME, .35); g.fillRect(-55, 180, 110, 40);   // le dossier sous le bras
      g.restore();
    }
    if (t > p.a + .4) { const kb = eo(pr(t, p.a + .4, .3)); g.save(); g.globalAlpha = kb; g.translate(W / 2 + 70, 600 + Math.sin(lt * 3) * 8);
      g.fillStyle = CREME; g.beginPath(); g.ellipse(0, 0, 130, 85, 0, 0, 7); g.fill();
      g.beginPath(); g.arc(-60, 105, 18, 0, 7); g.fill(); g.beginPath(); g.arc(-80, 140, 10, 0, 7); g.fill();
      S.texte('…', 0, -10, { taille: 110, coul: NOIR }); g.restore(); }
    deuxClaque('UN HOMME|QUI NE PENSE PAS', 1350, p.a + .1, t, 110);
  }

  // « Dis-le en commentaire » : une bulle où l'on tape son score
  function score(p, t) {
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -150, 860, 300, 40); g.fill();
    g.beginPath(); g.moveTo(-300, 150); g.lineTo(-340, 230); g.lineTo(-220, 150); g.fill();
    g.fillStyle = GRIS; g.beginPath(); g.arc(-330, -10, 60, 0, 7); g.fill();
    const s = 'Mon score : ' + (1 + Math.floor((t - p.a) * 4) % 4) + ' / 4', curseur = Math.floor(t * 3) % 2 ? '|' : '';
    S.texte(s + curseur, -240, -10, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, align: 'left', max: 640 });
    g.restore();
    claque('EN COMMENTAIRE', 1300, p.a + .15, t, { taille: 110, coul: OR });
  }

  return { cases, trois, num, citation, auteur, siecles, sot, voyant, piege, penser, score };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'cases') for (let i = 0; i < 4; i++) L.push([p.a + .2 + i * .12, 'blip', .4]);
  if (p.type === 'trois') { L.push([p.a, 'pop', .35]); for (let x = tps(p.un); x < p.b - .1; x += .11) L.push([x, 'tic', .25]); }
  if (p.type === 'num') L.push([p.a, 'chapitre', .6]);
  if (p.type === 'citation') { const n = p.q.length, d = Math.max(.6, (p.b - p.a) * .8); for (let k = 0; k < n; k += 7) L.push([p.a + d * k / n, 'tic', .15]); }
  if (p.type === 'auteur') L.push([p.a, 'whoosh', .4]);
  if (p.type === 'siecles') L.push([p.a, 'pop', .4], [p.a + .5, 'pop', .4], [p.a + .7, 'whoosh', .4]);
  if (p.type === 'sot') { L.push([p.a, 'papier', .4]); L.push([tps(p.sot), 'tampon', .8]); }
  if (p.type === 'voyant') L.push([p.a, 'souffle', .45], [p.a + .5, 'aspire', .4]);
  if (p.type === 'piege') L.push([p.a, 'buzz', .5], [p.a + .2, 'tampon', .8]);
  if (p.type === 'penser') for (let i = 0; i < 5; i++) L.push([p.a + i * .08, 'clic', .3]);
  if (p.type === 'score') L.push([p.a, 'pop', .5]);
};
