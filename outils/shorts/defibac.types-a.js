// Plans propres au short « Défi bac : 5 épreuves ». O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre,
// fondImg, al, C = couleurs). Couleurs : uniquement O.C et O.al (l'habillage « jeu » les remplace).
// Les plans vraifaux, ordre, intrus, plusmoins, niveau, photo et portrait sont communs (formats-a.js, modele-a.js).
window.SANS_ST_A = ['photo', 'collage', 'epreuves', 'score', 'endo', 'piege41', 'contrat', 'flotte', 'atome', 'commentaire'];
window.PROPRES_A = ['epreuves', 'score', 'endo', 'piege41', 'contrat', 'flotte', 'atome', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  // contournement : le plan commun « niveau » (formats-a.js) appelle carte() sans O. devant (sans effet ici, ce short
  // n'y met pas d'image, mais évite l'erreur si on en ajoute une).
  if (!window.carte) window.carte = (...x) => O.carte(...x);
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const ligne = (x0, y0, x1, y1, c, ep = 6, tirets) => { g.save(); g.strokeStyle = c; g.lineWidth = ep; g.lineCap = 'round'; if (tirets) g.setLineDash(tirets);
    g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); g.restore(); };
  const MAT = ['SVT', 'HISTOIRE', 'PHILO', 'GÉO', 'PHYSIQUE'];

  // les cinq épreuves : cinq pastilles qui tombent, une par matière
  function epreuves(p, t) {
    MAT.forEach((m, i) => {
      const k = back(pr(t, p.a + .1 + i * .13, .35)); if (k <= 0) return;
      const x = W / 2, y = 470 + i * 150;
      g.save(); g.translate(lerp(i % 2 ? W + 300 : -300, x, cl(k)), y); g.scale(k, k);
      g.fillStyle = i % 2 ? al(OR, .9) : al(ROUGE, .9); g.beginPath(); g.roundRect(-330, -58, 660, 116, 58); g.fill();
      g.fillStyle = NOIR; g.beginPath(); g.arc(-270, 0, 44, 0, 7); g.fill();
      S.texte(String(i + 1), -270, 3, { taille: 60, coul: i % 2 ? OR : ROUGE });
      S.texte(m, 30, 3, { taille: 64, coul: NOIR }); g.restore();
    });
    titrePop('5 ÉPREUVES|5 MATIÈRES', 1380, t, p.a + .7, 120);
  }

  // tableau des points : 0 / 5 au départ, + 1 après la première épreuve
  function score(p, t) {
    const v = p.v || 0, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 820); g.scale(k, k);
    g.fillStyle = al(NOIR, .85); g.strokeStyle = OR; g.lineWidth = 12; g.beginPath(); g.roundRect(-400, -260, 800, 520, 40); g.fill(); g.stroke();
    // ampoules du cadre
    for (let i = 0; i < 16; i++) { const a = i / 16 * 6.283, on = Math.floor(t * 8 + i) % 2;
      g.fillStyle = on ? OR : al(OR, .3); g.beginPath(); g.arc(Math.cos(a) * 430, Math.sin(a) * 290, 14, 0, 7); g.fill(); }
    S.texte('SCORE', 0, -170, { taille: 56, coul: CREME, esp: 10 });
    const kv = v ? back(pr(t, p.a + .25, .3)) : 1;
    g.save(); g.scale(lerp(1.8, 1, kv), lerp(1.8, 1, kv));
    S.texte(`${v} / 5`, 0, 40, { taille: 210, coul: OR, police: 'Spectral', poids: 700, contour: NOIR, contourL: 12 }); g.restore();
    g.restore();
    for (let i = 0; i < 5; i++) { g.fillStyle = i < v ? OR : al(CREME, .15); g.beginPath(); g.arc(W / 2 - 240 + i * 120, 1160, 34, 0, 7); g.fill(); }
    if (v) titrePop('+ 1|POINT', 1420, t, p.a + .2, 130);
    else deux('COMPTE|TES POINTS', 1420, 130);
  }

  // l'endosymbiose : une grande cellule entoure une bactérie, qui reste vivante dedans et devient la mitochondrie
  function endo(p, t) {
    const lt = t - p.a, cx = W / 2, cy = 860, k = eo(cl(lt / 1.2));
    // la cellule hôte
    g.save(); g.fillStyle = al(CREME, .08); g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath();
    for (let i = 0; i <= 60; i++) { const a = i / 60 * 6.283, r = 330 + Math.sin(a * 5 + lt * 2) * 14 - (Math.abs(a - 0) < .7 || a > 5.6 ? 70 * (1 - k) : 0);
      i ? g.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r) : g.moveTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r); }
    g.closePath(); g.fill(); g.stroke(); g.restore();
    // noyau
    g.fillStyle = al(GRIS, .7); g.beginPath(); g.arc(cx - 120, cy - 60, 90, 0, 7); g.fill();
    // la bactérie entre puis devient mitochondrie (crêtes)
    const bx = lerp(cx + 560, cx + 130, k), by = cy + 90;
    g.save(); g.translate(bx, by); g.rotate(-.2); g.fillStyle = al(OR, .9); g.strokeStyle = NOIR; g.lineWidth = 6;
    g.beginPath(); g.ellipse(0, 0, 120, 62, 0, 0, 7); g.fill(); g.stroke();
    if (k > .7) { g.globalAlpha = cl((k - .7) / .3); g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath();
      for (let i = 0; i < 6; i++) { const x = -85 + i * 34; g.moveTo(x, i % 2 ? -50 : 50); g.lineTo(x, i % 2 ? 10 : -10); } g.stroke(); }
    g.restore();
    S.texte(k < .7 ? 'BACTÉRIE' : 'MITOCHONDRIE', bx, by + 110, { taille: 46, coul: OR, poids: 700, contour: NOIR, contourL: 8 });
    // pas digérée : croix sur le « miam »
    if (k > .8) { const kk = back(pr(t, p.a + 1.0, .3)); g.save(); g.translate(cx - 170, cy + 210); g.scale(kk, kk);
      S.texte('JAMAIS DIGÉRÉE', 0, 0, { taille: 44, coul: ROUGE, poids: 700, contour: NOIR, contourL: 8 }); g.restore(); }
    deux('L’ENDO-|SYMBIOSE', 1420, 120);
  }

  // 1941 : juin (Barbarossa) avant décembre (Pearl Harbor)
  function piege41(p, t) {
    const x0 = 120, x1 = 960, y = 900, k = eo(pr(t, p.a, .5)), X = m => lerp(x0, x1, (m - .5) / 12);
    S.texte('1941', W / 2, 560, { taille: 200, coul: OR, police: 'Spectral', poids: 700, contour: NOIR, contourL: 12 });
    ligne(x0, y, lerp(x0, x1, k), y, CREME, 10);
    'JFMAMJJASOND'.split('').forEach((m, i) => { if (k < (i + .5) / 12) return; ligne(X(i + 1), y - 18, X(i + 1), y + 18, CREME, 5);
      S.texte(m, X(i + 1), y + 55, { taille: 36, coul: GRIS, poids: 700 }); });
    const ev = (mois, a, nom, date, haut, c) => { const kk = back(pr(t, a, .35)); if (kk <= 0) return; const x = X(mois), yy = haut ? y - 170 : y + 210;
      ligne(x, y, x, haut ? yy + 50 : yy - 50, c, 6);
      g.save(); g.translate(Math.max(240, Math.min(W - 240, x)), yy); g.scale(kk, kk); g.fillStyle = c; g.beginPath(); g.roundRect(-190, -48, 380, 96, 20); g.fill();
      S.texte(nom, 0, -8, { taille: 42, coul: NOIR, max: 350 }); S.texte(date, 0, 30, { taille: 28, coul: NOIR, poids: 600 }); g.restore(); };
    ev(6.7, tps(['o2', 'barbarossa']), 'BARBAROSSA', '22 JUIN', true, OR);
    ev(12.2, tps(['o2', 'pearl']), 'PEARL HARBOR', '7 DÉCEMBRE', false, ROUGE);
    O.tampon('LE PIÈGE', W / 2, 1420, pr(t, p.a + .15, .3), -.08, 120, ROUGE);
  }

  // le contrat : un parchemin, trois signatures qui s'écrivent
  function contrat(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1300, 860, k)); g.rotate(-.03);
    g.fillStyle = CREME; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillRect(-380, -440, 760, 880); g.shadowColor = 'transparent';
    S.texte('CONTRAT', 0, -350, { taille: 92, coul: NOIR, police: 'Spectral', poids: 700, esp: 8 });
    for (let i = 0; i < 5; i++) { g.fillStyle = al(NOIR, .15); g.fillRect(-300, -240 + i * 44, 600 - (i === 4 ? 220 : 0), 8); }
    ['Hobbes', 'Locke', 'Rousseau'].forEach((n, i) => { const ks = cl((t - p.a - .3 - i * .3) / .35); if (ks <= 0) return;
      const y = 60 + i * 120, txt = n.slice(0, Math.ceil(n.length * ks));
      g.fillStyle = al(NOIR, .3); g.fillRect(-280, y + 30, 560, 4);
      S.texte(txt, -250, y, { taille: 72, coul: ROUGE, police: 'Spectral', it: true, poids: 500, align: 'left' }); });
    g.restore();
    deux('L’ÉTAT NAÎT|D’UN CONTRAT', 1450, 104);
  }

  // la flotte mondiale : barres 1980 et 2024, pétroliers et vrac sec (parts de capacité)
  function flotte(p, t) {
    const k = eo(pr(t, p.a + .1, .8)), y0 = 1120, hmax = 560;
    O.petitTitre('— PART DE LA FLOTTE MONDIALE —', 430);
    const barre = (x, v, c, lbl) => { const h = hmax * v / 50 * k; g.fillStyle = c; g.fillRect(x - 70, y0 - h, 140, h);
      S.texte(Math.round(v * k) + ' %', x, y0 - h - 45, { taille: 54, coul: c, poids: 700 }); S.texte(lbl, x, y0 + 45, { taille: 38, coul: CREME, poids: 700 }); };
    barre(200, 50, ROUGE, '1980'); barre(370, 28, ROUGE, '2024');
    barre(710, 27, OR, '1980'); barre(880, 43, OR, '2024');
    ligne(100, y0, 980, y0, CREME, 5);
    S.texte('PÉTROLIERS', 285, y0 + 115, { taille: 46, coul: ROUGE, poids: 700 });
    S.texte('VRAC SEC', 795, y0 + 115, { taille: 46, coul: OR, poids: 700 });
    S.texte('capacité, CNUCED', W / 2, y0 + 190, { taille: 34, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    deux('LE VRAC SEC|PASSE DEVANT', 1500, 104);
  }

  // l'atome d'hydrogène : niveaux 1, 2, 3 ; le photon de 11 eV ne tombe sur aucun écart et traverse
  function atome(p, t) {
    // échelle coupée entre 0 et 9 eV (zigzag) pour que les niveaux 2 et 3 restent lisibles
    const lt = t - p.a, x0 = 230, x1 = 850, Y = e => e < 1 ? 1150 : lerp(900, 480, (e - 9) / 4);
    O.petitTitre('— L’ATOME D’HYDROGÈNE —', 430);
    [[0, 'n = 1'], [10.2, 'n = 2'], [12.1, 'n = 3']].forEach(([e, n]) => { ligne(x0, Y(e), x1, Y(e), CREME, 8);
      S.texte(n, x0 - 30, Y(e), { taille: 40, coul: CREME, poids: 700, align: 'right' }); });
    const fl = (e, a, c) => { const kk = eo(pr(t, p.a + a, .4)); if (kk <= 0) return; const x = e > 11 ? 760 : 620;
      ligne(x, Y(0), x, lerp(Y(0), Y(e), kk), c, 9);
      S.texte(String(e).replace('.', ',') + ' eV', x + (e > 11 ? 20 : -20), (Y(0) + Y(e)) / 2 - (e > 11 ? 60 : 0), { taille: 44, coul: c, poids: 700, align: e > 11 ? 'left' : 'right' }); };
    fl(10.2, .2, OR); fl(12.1, .5, OR);
    [620, 760].forEach(x => { g.save(); g.fillStyle = NOIR; g.fillRect(x - 20, 1010, 40, 40); g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath();
      g.moveTo(x - 24, 1012); g.lineTo(x + 24, 1002); g.moveTo(x - 24, 1052); g.lineTo(x + 24, 1042); g.stroke(); g.restore(); });
    // le photon de 11 eV : arrive, ne trouve aucun niveau, repart
    const u = cl((lt - .8) / 1.4);
    if (u > 0) { const x = lerp(-60, W + 60, u), y = Y(11);
      g.save(); g.strokeStyle = ROUGE; g.lineWidth = 7; g.beginPath(); for (let s = -120; s <= 0; s += 4) { const yy = y + Math.sin(s * .16) * 16; s === -120 ? g.moveTo(x + s, yy) : g.lineTo(x + s, yy); } g.stroke(); g.restore();
      S.texte('11 eV', x - 60, y - 50, { taille: 44, coul: ROUGE, poids: 700 }); }
    ligne(x0, Y(11), x1, Y(11), al(ROUGE, .5), 4, [14, 12]);
    deux('L’ÉNERGIE|EXACTE', 1450, 120);
  }

  // une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .3)), txt = 'Mon score : … / 5', n = Math.floor(cl((t - p.a - .3) / .8) * txt.length);
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-300, 165); g.lineTo(-340, 260); g.lineTo(-220, 165); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-330, -60, 50, 0, 7); g.fill();
    S.texte('toi', -230, -60, { taille: 44, coul: GRIS, align: 'left', poids: 600 });
    S.texte(txt.slice(0, n), -360, 60, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, align: 'left', max: 760 });
    const kc = pr(t, p.a + 1.2, .3); if (kc > 0) { g.save(); g.translate(350, -80); g.scale(back(kc), back(kc)); g.fillStyle = ROUGE;
      g.beginPath(); g.moveTo(0, 30); g.bezierCurveTo(-60, -10, -30, -60, 0, -30); g.bezierCurveTo(30, -60, 60, -10, 0, 30); g.fill(); g.restore(); }
    g.restore();
    deux('TON SCORE SUR 5|EN COMMENTAIRE', 1350, 104);
  }

  return { epreuves, score, endo, piege41, contrat, flotte, atome, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  if (p.type === 'epreuves') for (let i = 0; i < 5; i++) L.push([p.a + .1 + i * .13, 'pop', .4]);
  if (p.type === 'score') L.push([p.a, 'blip', .5], ...(p.v ? [[p.a + .25, 'valide', .8]] : []));
  if (p.type === 'endo') L.push([p.a, 'aspire', .45], [p.a + 1.0, 'pop', .4]);
  if (p.type === 'piege41') { L.push([p.a + .15, 'tampon', .8]); L.push([S.T('o2', 'barbarossa') - .04, 'pop', .5], [S.T('o2', 'pearl') - .04, 'pop', .5]); }
  if (p.type === 'contrat') L.push([p.a, 'papier', .5], [p.a + .3, 'stylo', .5], [p.a + .6, 'stylo', .5], [p.a + .9, 'stylo', .5]);
  if (p.type === 'flotte') L.push([p.a + .1, 'montee', .4]);
  if (p.type === 'atome') L.push([p.a + .2, 'blip', .4], [p.a + .5, 'blip', .4], [p.a + .8, 'whoosh', .5]);
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .3 + k * .1, 'tic', .25]); L.push([p.a + 1.2, 'pop', .5]); }
};
