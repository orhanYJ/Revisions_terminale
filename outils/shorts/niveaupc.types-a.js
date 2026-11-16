// Plans propres au short « Physique-chimie : niveau 1 → 10 ». O = outils du modèle (carte, multi, tampon, barreRouge,
// petitTitre, fondImg, al, C = couleurs). Couleurs : uniquement O.C et O.al (l'habillage néon les remplace).
// Les plans « niveau », « photo » et « collage » sont communs (formats-a.js, modele-a.js).
window.SANS_ST_A = ['photo', 'collage', 'echelle', 'triche', 'echelleph', 'dilution', 'beer', 'tangentes', 'zinc', 'lunette', 'commentaire'];
window.PROPRES_A = ['echelle', 'triche', 'echelleph', 'dilution', 'beer', 'tangentes', 'zinc', 'lunette', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  // contournement : le plan commun « niveau » (formats-a.js) appelle carte() sans O. devant ; sans cette ligne,
  // un plan « niveau » avec image lève « carte is not defined ». Sans effet si formats-a.js est corrigé.
  if (!window.carte) window.carte = (...x) => O.carte(...x);
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // titre sur une ou deux lignes (« | »), la seconde en couleur vive
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const ligne = (x0, y0, x1, y1, c, ep = 6, tirets) => { g.save(); g.strokeStyle = c; g.lineWidth = ep; g.lineCap = 'round'; if (tirets) g.setLineDash(tirets);
    g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); g.restore(); };
  const croix = (x, y, r, k) => { if (k <= 0) return; g.save(); g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round'; g.beginPath();
    g.moveTo(x - r, y - r); g.lineTo(x - r + 2 * r * cl(k * 2), y - r + 2 * r * cl(k * 2)); if (k > .5) { const k2 = cl(k * 2 - 1); g.moveTo(x + r, y - r); g.lineTo(x + r - 2 * r * k2, y - r + 2 * r * k2); } g.stroke(); g.restore(); };

  // l'échelle des dix niveaux qui s'allument, un curseur qui grimpe et hésite
  function echelle(p, t) {
    const lt = t - p.a;
    for (let i = 0; i < 10; i++) {
      const y = 1130 - i * 74, k = back(pr(t, p.a + i * .06, .25)), on = lt > .3 + i * .09;
      const c = i < 3 ? CREME : i < 7 ? OR : ROUGE, w = 360 + i * 38;
      g.save(); g.translate(W / 2, y); g.scale(k, 1);
      g.fillStyle = on ? al(c, .9) : al(CREME, .1); g.beginPath(); g.roundRect(-w / 2, -26, w, 52, 14); g.fill(); g.restore();
      if (k > .5) S.texte(String(i + 1), W / 2 - w / 2 - 50, y, { taille: 44, coul: on ? c : GRIS });
    }
    // curseur : monte, puis oscille entre 6 et 8
    const n = lt < 1.1 ? lerp(0, 6, eo(cl(lt / 1.1))) : 7 + Math.sin((lt - 1.1) * 5) * .9;
    const yc = 1130 - n * 74;
    g.save(); g.fillStyle = ROUGE; g.beginPath(); g.moveTo(W / 2 + 330, yc); g.lineTo(W / 2 + 390, yc - 34); g.lineTo(W / 2 + 390, yc + 34); g.closePath(); g.fill(); g.restore();
    S.texte('?', W / 2 + 440, yc, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 8 });
    titrePop('À QUEL NIVEAU|TU T’ARRÊTES ?', 1380, t, p.a, 104);
  }

  // pas de calculatrice, pas d'internet : tampon
  function triche(p, t) {
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 830); g.scale(k, k); g.rotate(-.06);
    g.fillStyle = al(CREME, .08); g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.roundRect(-190, -300, 380, 600, 34); g.fill(); g.stroke();
    g.fillStyle = al(OR, .25); g.fillRect(-140, -250, 280, 120); S.texte('42', 100, -190, { taille: 70, coul: OR, align: 'right', police: 'Spectral', poids: 600 });
    for (let r = 0; r < 4; r++) for (let c = 0; c < 3; c++) { g.fillStyle = al(CREME, .22); g.beginPath(); g.roundRect(-140 + c * 100, -90 + r * 95, 80, 72, 12); g.fill(); }
    g.restore();
    croix(W / 2, 830, 220, pr(t, p.a + .2, .35));
    O.tampon('PAS DE TRICHE', W / 2, 1330, pr(t, p.a + .35, .3), -.08, 110, ROUGE);
  }

  // l'échelle de pH : le citron tombe dans la zone acide
  function echelleph(p, t) {
    const x = v => lerp(110, 970, v / 14), y = 860, k = eo(pr(t, p.a, .5));
    O.petitTitre('— L’ÉCHELLE DE pH —', 470);
    for (let v = 0; v < 14; v++) { const c = v < 7 ? ROUGE : OR, a = v < 7 ? .85 - v * .1 : .2 + (v - 7) * .1;
      g.fillStyle = al(c, a); g.fillRect(x(v), y - 50, (x(1) - x(0)) * cl(k * 14 - v) + 1, 100); }
    g.strokeStyle = CREME; g.lineWidth = 4; g.strokeRect(x(0), y - 50, x(14) - x(0), 100);
    [0, 7, 14].forEach(v => S.texte(String(v), x(v), y + 100, { taille: 54, coul: CREME }));
    ligne(x(7), y - 80, x(7), y + 60, CREME, 6);
    S.texte('NEUTRE', x(7), y - 115, { taille: 40, coul: CREME, poids: 700 });
    S.texte('ACIDE', x(3.5), y + 175, { taille: 60, coul: ROUGE, poids: 700 });
    S.texte('BASIQUE', x(10.5), y + 175, { taille: 60, coul: OR, poids: 700 });
    // le citron (disque jaune stylisé) tombe vers pH 2,5
    const kc = back(pr(t, p.a + .4, .45)), yc = lerp(300, y - 170, kc);
    if (kc > 0) { g.save(); g.translate(x(2.5), yc); g.fillStyle = OR; g.beginPath(); g.ellipse(0, 0, 70, 54, -.3, 0, 7); g.fill();
      g.strokeStyle = NOIR; g.lineWidth = 4; for (let i = 0; i < 6; i++) { const a = i / 6 * 6.283; g.beginPath(); g.moveTo(0, 0); g.lineTo(Math.cos(a) * 48, Math.sin(a) * 36); g.stroke(); }
      g.restore(); ligne(x(2.5), yc + 60, x(2.5), y - 55, OR, 5, [10, 8]);
      S.texte('CITRON : 2,5', x(2.5) + 230, yc, { taille: 44, coul: OR, poids: 700 }); }
    deux('ACIDE|pH < 7', 1420, 120);
  }

  // un bécher d'acide fort dilué dix fois : moins d'ions, pH + 1
  function becher(cx, cy, w, h, n, k, lbl) {
    g.save(); g.translate(cx, cy);
    g.fillStyle = al(OR, .16); g.fillRect(-w / 2, -h * .75, w, h * .75);
    g.strokeStyle = CREME; g.lineWidth = 7; g.beginPath(); g.moveTo(-w / 2 - 14, -h); g.lineTo(-w / 2, -h + 14); g.lineTo(-w / 2, 0); g.lineTo(w / 2, 0); g.lineTo(w / 2, -h); g.stroke();
    for (let i = 0; i < n; i++) { const px = (rnd(i * 3.7 + w) - .5) * (w - 40), py = -h * .72 * rnd(i * 5.1 + h) - 10;
      g.globalAlpha = cl(k * 2 - i / n); g.fillStyle = ROUGE; g.beginPath(); g.arc(px, py, 11, 0, 7); g.fill(); }
    g.globalAlpha = 1; g.restore();
    S.texte(lbl, cx, cy + 70, { taille: 64, coul: OR, poids: 700, police: 'Spectral' });
  }
  function dilution(p, t) {
    const k = eo(pr(t, p.a, .5)), k2 = eo(pr(t, p.a + .5, .5));
    O.petitTitre('— ACIDE FORT —', 430);
    becher(290, 1020, 260, 380, 30, k, 'pH 2');
    if (k2 > 0) { g.save(); g.globalAlpha = k2; S.d.fleche(450, 820, 600, 820, k2, { trait: CREME, ep: 10 });
      S.texte('× 10 d’eau', 525, 750, { taille: 44, coul: CREME, poids: 700 }); g.restore();
      becher(800, 1020, 340, 480, 6, k2, 'pH 3'); }
    deux('+ 1 À CHAQUE|DILUTION × 10', 1420, 110);
  }

  // A en fonction de c : une droite qui passe par l'origine ; c double, A double
  function beer(p, t) {
    const ox = 190, oy = 1180, L = 760, Hh = 640, k = eo(pr(t, p.a, .6));
    ligne(ox, oy, ox + L, oy, CREME, 6); ligne(ox, oy, ox, oy - Hh, CREME, 6);
    S.texte('c', ox + L + 30, oy, { taille: 60, coul: CREME, police: 'Spectral', it: true, poids: 600 });
    S.texte('A', ox, oy - Hh - 50, { taille: 60, coul: CREME, police: 'Spectral', it: true, poids: 600 });
    ligne(ox, oy, ox + L * .9 * k, oy - Hh * .9 * k, OR, 10);
    const pt = (u, a, lbl, lblA) => { const kk = back(pr(t, p.a + a, .3)); if (kk <= 0) return; const x = ox + L * u, y = oy - Hh * u;
      ligne(x, oy, x, y, al(CREME, .6), 4, [12, 10]); ligne(ox, y, x, y, al(CREME, .6), 4, [12, 10]);
      g.save(); g.translate(x, y); g.scale(kk, kk); g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 22, 0, 7); g.fill(); g.restore();
      S.texte(lbl, x, oy + 55, { taille: 48, coul: CREME, poids: 700 }); S.texte(lblA, ox - 70, y, { taille: 48, coul: CREME, poids: 700 }); };
    pt(.35, .5, 'c', 'A'); pt(.7, .9, '2c', '2A');
    S.texte('A = k × c', ox + L * .55, oy - Hh * .95, { taille: 70, coul: OR, police: 'Spectral', poids: 600 });
    O.petitTitre('— LOI DE BEER-LAMBERT —', 430);
    deux('PROPORTIONNELLE|À LA CONCENTRATION', 1430, 96);
  }

  // courbe de titrage, deux tangentes parallèles, la droite du milieu : le volume équivalent
  function tangentes(p, t) {
    const ox = 170, oy = 1180, L = 800, Hh = 620;
    const f = v => 2 + 10 / (1 + Math.exp(-(v - 10) * .9)), df = v => { const e = Math.exp(-(v - 10) * .9); return 10 * .9 * e / ((1 + e) ** 2); };
    const X = v => ox + v / 20 * L, Y = ph => oy - ph / 14 * Hh;
    ligne(ox, oy, ox + L, oy, CREME, 6); ligne(ox, oy, ox, oy - Hh, CREME, 6);
    S.texte('V', ox + L + 30, oy, { taille: 56, coul: CREME, police: 'Spectral', it: true, poids: 600 });
    S.texte('pH', ox, oy - Hh - 50, { taille: 56, coul: CREME, police: 'Spectral', it: true, poids: 600 });
    const k = eo(pr(t, p.a, .7));
    g.save(); g.strokeStyle = OR; g.lineWidth = 9; g.beginPath();
    for (let v = 0; v <= 20 * k; v += .2) { const x = X(v), y = Y(f(v)); v ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); g.restore();
    // tangentes en V = 7,5 et V = 12,5 (même pente par symétrie)
    const tg = (v0, a) => { const kk = eo(pr(t, p.a + a, .35)); if (kk <= 0) return; const s = df(v0), y0 = f(v0), d = 4.5 * kk;
      ligne(X(v0 - d), Y(y0 - s * d), X(v0 + d), Y(y0 + s * d), CREME, 5); };
    tg(7.5, .6); tg(12.5, .85);
    const km = eo(pr(t, p.a + 1.15, .35));
    if (km > 0) { const s = df(7.5), ym = (f(7.5) + f(12.5)) / 2 - s * 0, d = 4.5 * km;
      ligne(X(10 - d), Y(ym - s * d), X(10 + d), Y(ym + s * d), ROUGE, 6, [14, 10]);
      ligne(X(10), Y(ym), X(10), oy, al(ROUGE, .8), 4, [10, 8]);
      g.fillStyle = ROUGE; g.beginPath(); g.arc(X(10), Y(ym), 18, 0, 7); g.fill();
      S.texte('VE', X(10), oy + 55, { taille: 52, coul: ROUGE, poids: 700 }); }
    O.petitTitre('— LA MÉTHODE DES TANGENTES —', 430);
    deux('AU MILIEU|DU SAUT DE pH', 1430, 104);
  }

  // un photon : petite onde qui avance de (x0, y0) vers (x1, y1)
  function photon(x0, y0, x1, y1, u, c) {
    const x = lerp(x0, x1, u), y = lerp(y0, y1, u), a = Math.atan2(y1 - y0, x1 - x0);
    g.save(); g.translate(x, y); g.rotate(a); g.strokeStyle = c; g.lineWidth = 7; g.lineCap = 'round'; g.beginPath();
    for (let s = -110; s <= 0; s += 4) { const yy = Math.sin(s * .16) * 16; s === -110 ? g.moveTo(s, yy) : g.lineTo(s, yy); } g.stroke();
    g.fillStyle = c; g.beginPath(); g.moveTo(14, 0); g.lineTo(-6, -14); g.lineTo(-6, 14); g.closePath(); g.fill(); g.restore();
  }
  // lumière rouge : les photons rebondissent ; ultraviolet : un électron sort
  function zinc(p, t) {
    const lt = t - p.a, tuv = tps(['r8', 'il']), uv = t >= tuv;
    g.fillStyle = al(GRIS, .7); g.fillRect(140, 1040, 800, 110); g.strokeStyle = CREME; g.lineWidth = 5; g.strokeRect(140, 1040, 800, 110);
    S.texte('PLAQUE DE ZINC', W / 2, 1095, { taille: 50, coul: NOIR, poids: 700 });
    // électrons prisonniers
    for (let i = 0; i < 7; i++) { const x = 220 + i * 110; g.fillStyle = CREME; g.beginPath(); g.arc(x, 1015 + Math.sin(lt * 6 + i) * 4, 13, 0, 7); g.fill(); }
    if (!uv) {
      for (let i = 0; i < 5; i++) { const u = ((lt * 1.4 + i / 5) % 1), x0 = 200 + i * 160;
        if (u < .6) photon(x0 - 120, 450, x0, 1000, u / .6, ROUGE);
        else photon(x0, 1000, x0 + 120, 450, (u - .6) / .4 * .5, al(ROUGE, 1 - (u - .6) / .4)); }
      S.texte('ROUGE INTENSE', W / 2, 380, { taille: 64, coul: ROUGE, poids: 700 });
      deux('0 ÉLECTRON', 1380, 130);
    } else {
      const u = cl((t - tuv) / .45); photon(320, 450, 540, 1000, u, OR);
      if (u >= 1) { const ke = eo(cl((t - tuv - .45) / .6)); g.fillStyle = OR; g.beginPath(); g.arc(540 + ke * 260, 1000 - ke * 520, 18, 0, 7); g.fill();
        S.texte('e−', 540 + ke * 260 + 45, 1000 - ke * 520 - 30, { taille: 54, coul: OR, poids: 700 }); }
      S.texte('ULTRAVIOLET', W / 2, 380, { taille: 64, coul: OR, poids: 700 });
      deux('UN ÉLECTRON|SORT', 1400, 120);
    }
  }

  // lunette afocale du TP 7 : objectif 50 cm, oculaire 5 cm, foyers confondus ; G = 50 / 5
  function lentille(x, y, h, c) {
    g.save(); g.strokeStyle = c; g.fillStyle = c; g.lineWidth = 9; g.beginPath(); g.moveTo(x, y - h); g.lineTo(x, y + h); g.stroke();
    [[-1, y - h], [1, y + h]].forEach(([s, yy]) => { g.beginPath(); g.moveTo(x, yy - s * 4); g.lineTo(x - 22, yy + s * 30); g.lineTo(x + 22, yy + s * 30); g.closePath(); g.fill(); });
    g.restore();
  }
  function lunette(p, t) {
    const y = 840, k = eo(pr(t, p.a, .5)), u = 13, xo1 = 140, xf = xo1 + 50 * u, xo2 = xf + 5 * u;
    ligne(80, y, 1000, y, al(CREME, .5), 4);
    lentille(xo1, y, 230 * k, OR); lentille(xo2, y, 120 * k, OR);
    S.texte('OBJECTIF', xo1 + 20, y - 300, { taille: 40, coul: OR, poids: 700, align: 'left' });
    S.texte('OCULAIRE', xo2, y - 190, { taille: 40, coul: OR, poids: 700 });
    // rayons parallèles à l'axe → foyer, puis ressortent parallèles
    const kr = eo(pr(t, p.a + .3, .7));
    [-150, 150].forEach(h0 => { const h2 = h0 * 5 / 50;
      if (kr > 0) ligne(40, y + h0, lerp(40, xo1, cl(kr * 2)), y + h0, CREME, 5);
      if (kr > .5) { const kk = cl(kr * 2 - 1); ligne(xo1, y + h0, lerp(xo1, xo2, kk), lerp(y + h0, y - h2, kk), CREME, 5); }
      if (kr >= 1) ligne(xo2, y - h2, 1040, y - h2, CREME, 5); });
    g.fillStyle = ROUGE; g.beginPath(); g.arc(xf, y, 14, 0, 7); g.fill();
    // cotes 50 cm et 5 cm
    const kc = eo(pr(t, p.a + .7, .4)); g.save(); g.globalAlpha = kc;
    ligne(xo1, y + 300, xf, y + 300, CREME, 4); S.texte('f′1 = 50 cm', (xo1 + xf) / 2, y + 345, { taille: 50, coul: CREME, poids: 700 });
    ligne(xf, y + 210, xo2, y + 210, OR, 4); S.texte('f′2 = 5 cm', xo2 - 60, y + 165, { taille: 44, coul: OR, poids: 700, align: 'right' });
    g.restore();
    const kg = back(pr(t, p.a + 1.1, .35)); if (kg > 0) { g.save(); g.translate(W / 2, 1440); g.scale(kg, kg);
      S.texte('G = 50 / 5 = 10', 0, 0, { taille: 120, coul: OR, contour: NOIR, contourL: 12, police: 'Spectral', poids: 700, max: 980 }); g.restore(); }
    O.petitTitre('— G = f′1 / f′2 —', 430);
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

  return { echelle, triche, echelleph, dilution, beer, tangentes, zinc, lunette, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  if (p.type === 'echelle') { for (let i = 0; i < 10; i++) L.push([p.a + .3 + i * .09, 'tic', .3]); L.push([p.a, 'montee', .4]); }
  if (p.type === 'triche') L.push([p.a + .2, 'buzz', .5], [p.a + .35, 'tampon', .9]);
  if (p.type === 'echelleph') L.push([p.a, 'whoosh', .4], [p.a + .7, 'pop', .5]);
  if (p.type === 'dilution') L.push([p.a + .5, 'souffle', .45]);
  if (p.type === 'beer') L.push([p.a + .5, 'pop', .45], [p.a + .9, 'pop', .5]);
  if (p.type === 'tangentes') L.push([p.a, 'stylo', .5], [p.a + 1.15, 'valide', .5]);
  if (p.type === 'zinc') { L.push([p.a, 'blip', .35]); L.push([S.T('r8', 'il') - .04 + .45, 'drop', .6]); }
  if (p.type === 'lunette') L.push([p.a, 'whoosh', .4], [p.a + 1.1, 'gong', .5]);
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .3 + k * .1, 'tic', .25]); L.push([p.a + 1.2, 'pop', .5]); }
};
