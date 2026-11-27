// Plans propres au short « SES : trouve l'intrus » (habillage alerte). O = outils du modèle (carte, multi, tampon,
// barreRouge, petitTitre, fondImg, photo, al, C = couleurs de l'habillage). Couleurs : O.C et O.al seulement.
// Convention des dessins : OR = premier rôle, ROUGE = alerte, ce qui baisse ou ce qui est faux.
window.SANS_ST_A = ['titre', 'score', 'manche', 'pcs'];
window.PROPRES_A = ['titre', 'score', 'manche', 'ricardo', 'pcs', 'baril', 'conjoncture', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  // titre sur deux lignes : la première en crème, la seconde en couleur vive
  const deux = (txt, y, taille = 110, c2 = OR) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? c2 : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const lueur = (c, f = 26) => { g.shadowColor = c; g.shadowBlur = f; };
  const ligne = (x0, y0, x1, y1, c, ep) => { g.strokeStyle = c; g.lineWidth = ep; g.lineCap = 'round'; g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); };
  function fleche(x0, y0, x1, y1, k, c, ep = 10) {
    if (k <= 0) return; const x = lerp(x0, x1, k), y = lerp(y0, y1, k), a = Math.atan2(y1 - y0, x1 - x0);
    g.save(); ligne(x0, y0, x, y, c, ep);
    g.fillStyle = c; g.beginPath(); g.moveTo(x + Math.cos(a) * ep * 2.4, y + Math.sin(a) * ep * 2.4);
    g.lineTo(x + Math.cos(a + 2.4) * ep * 2.6, y + Math.sin(a + 2.4) * ep * 2.6); g.lineTo(x + Math.cos(a - 2.4) * ep * 2.6, y + Math.sin(a - 2.4) * ep * 2.6); g.fill(); g.restore();
  }
  // gyrophare d'alerte (deux demi-cercles qui clignotent)
  function gyro(x, y, r, t) {
    const on = Math.floor(t * 6) % 2;
    g.save(); g.translate(x, y);
    g.fillStyle = on ? ROUGE : al(ROUGE, .35); if (on) lueur(ROUGE, 50);
    g.beginPath(); g.arc(0, 0, r, Math.PI, 0); g.closePath(); g.fill();
    g.shadowBlur = 0; g.fillStyle = al(CREME, .2); g.fillRect(-r * 1.2, 0, r * 2.4, r * .35);
    g.restore();
  }

  // ---------- titre : quatre cases, l'une devient l'intrus ; « TROUVE L'INTRUS » ; bandeau « SPÉCIALITÉ SES »
  function titre(p, t) {
    const lt = t - p.a;
    gyro(W / 2, 330, 70, t);
    for (let i = 0; i < 4; i++) {
      const x = i % 2 ? 730 : 350, y = i < 2 ? 590 : 950, k = back(pr(lt, i * .08, .3)), bad = i === 1 && lt > .55;
      pop(k, x, y, () => {
        if (bad) g.translate(Math.sin(t * 70) * 8, 0);
        g.save(); g.strokeStyle = bad ? ROUGE : OR; g.lineWidth = 8;
        g.fillStyle = bad ? al(ROUGE, .25) : al(OR, .08); g.beginPath(); g.roundRect(-160, -160, 320, 320, 30); g.fill(); g.stroke(); g.restore();
        S.texte(bad ? '!' : '?', 0, 8, { taille: 200, coul: bad ? ROUGE : CREME });
      });
    }
    S.texte('TROUVE', W / 2, 1270, { taille: 120, coul: CREME });
    S.texte('L’INTRUS', W / 2, 1410, { taille: 170, coul: ROUGE, contour: NOIR, contourL: 12 });
    const kb = eo(pr(lt, .3, .3)); g.save(); g.globalAlpha = kb; g.translate(lerp(-300, 0, kb), 0);
    g.fillStyle = OR; g.beginPath(); g.roundRect(W / 2 - 300, 1520, 600, 100, 16); g.fill();
    S.texte('SPÉCIALITÉ SES', W / 2, 1572, { taille: 60, coul: NOIR, esp: 4 }); g.restore();
  }

  // ---------- score : etape 0 = « ? / 4 » et quatre cases vides ; etape 1 = les quatre intrus rappelés, puis « TON SCORE ? »
  const INTRUS = ['DURKHEIM', 'CLASSES MOYENNES', 'CHOC PÉTROLIER', 'CHUTE DE LA DEMANDE'];
  function score(p, t) {
    const lt = t - p.a;
    if (!p.etape) {
      pop(back(pr(lt, 0, .35)), W / 2, 640, () => S.texte('? / 4', 0, 0, { taille: 260, coul: OR, contour: NOIR, contourL: 14 }));
      for (let i = 0; i < 4; i++) pop(pr(lt, .25 + i * .12, .3), 210 + i * 220, 1000, () => {
        g.save(); g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.roundRect(-85, -85, 170, 170, 24); g.stroke(); g.restore();
        S.texte(String(i + 1), 0, 6, { taille: 90, coul: al(CREME, .5) });
      });
      deux('COMBIEN TU|EN TROUVES ?', 1330, 110);
      return;
    }
    S.texte('LES 4 INTRUS', W / 2, 420, { taille: 60, coul: OR, esp: 8 });
    INTRUS.forEach((s, i) => {
      const k = pr(lt, i * .22, .3), y = 560 + i * 170;
      if (k <= 0) return;
      g.save(); g.globalAlpha = cl(k * 2); g.translate(lerp(-400, 0, eo(k)), 0);
      g.fillStyle = al(OR, .12); g.beginPath(); g.roundRect(110, y - 65, 860, 130, 24); g.fill();
      S.texte(String(i + 1), 180, y + 4, { taille: 70, coul: OR });
      S.texte(s, 530, y + 4, { taille: 64, coul: CREME, max: 560 });
      g.restore();
      pop(pr(lt, i * .22 + .2, .3), 900, y, () => { g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 44, 0, 7); g.fill(); S.texte('✓', 0, 4, { taille: 60, coul: CREME }); });
    });
    const kf = back(pr(lt, 1.1, .35)); g.save(); g.translate(W / 2, 1360); g.scale(kf, kf);
    S.texte('TON SCORE : … / 4', 0, 0, { taille: 100, coul: OR, contour: NOIR, contourL: 10, max: 960 }); g.restore();
  }

  // ---------- manche : « MANCHE n », quatre voyants, une image ou l'icône « feu », le thème
  function manche(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    S.texte(p.n === 4 ? 'MANCHE FINALE' : 'MANCHE', W / 2, 330, { taille: 54, coul: GRIS, esp: 14 });
    g.save(); g.translate(W / 2, 520); g.scale(lerp(2.2, 1, k), lerp(2.2, 1, k)); g.globalAlpha = cl(k * 2);
    g.save(); g.strokeStyle = OR; g.lineWidth = 12; g.beginPath(); g.arc(0, 0, 140, 0, 7); g.stroke();
    g.setLineDash([22, 18]); g.lineDashOffset = -t * 60; g.lineWidth = 5; g.beginPath(); g.arc(0, 0, 172, 0, 7); g.stroke(); g.restore();
    S.texte(String(p.n), 0, 10, { taille: 190, coul: CREME }); g.restore();
    for (let i = 0; i < 4; i++) {
      const on = i < p.n, ki = pr(lt, .2 + i * .08, .25), c = i === p.n - 1 ? ROUGE : OR;
      g.save(); g.globalAlpha = .25 + .75 * ki; g.fillStyle = on ? c : al(CREME, .15);
      g.beginPath(); g.roundRect(W / 2 - 250 + i * 130, 735, 110, 26, 13); g.fill(); g.restore();
    }
    const kv = eo(pr(lt, .15, .4));
    if (p.img) { g.save(); g.globalAlpha = kv; O.carte(p.img, W / 2, 1060, 440, 480, -.03, 1.08 + lt * .03, .5, .35); g.restore(); }
    else if (p.icone === 'feu') {   // ondes d'alerte et « 4 / 4 »
      g.save(); g.translate(W / 2, 1060); g.globalAlpha = kv;
      for (let i = 0; i < 3; i++) { const u = (t * 2 + i / 3) % 1; g.save(); g.globalAlpha = kv * (1 - u);
        g.strokeStyle = ROUGE; g.lineWidth = 10; g.beginPath(); g.arc(0, 0, 150 + u * 140, 0, 7); g.stroke(); g.restore(); }
      S.texte('4 / 4', 0, 0, { taille: 150, coul: CREME }); g.restore();
    }
    const kt = eo(pr(lt, .25, .3)); g.save(); g.globalAlpha = kt; g.translate(0, lerp(60, 0, kt)); deux(p.t, 1470, 120, p.n === 4 ? ROUGE : OR); g.restore();
  }

  // ---------- ricardo : l'exemple de 1817, chaque pays se spécialise et échange (drap anglais, vin portugais)
  function drap(x, y, s) {   // rouleau de drap
    g.save(); g.translate(x, y); g.fillStyle = CREME; g.beginPath(); g.roundRect(-s, -s * .45, 2 * s, s * .9, s * .2); g.fill();
    g.strokeStyle = al(NOIR, .35); g.lineWidth = s * .06; for (let i = -2; i <= 2; i++) { g.beginPath(); g.moveTo(i * s * .35, -s * .45); g.lineTo(i * s * .35, s * .45); g.stroke(); }
    g.fillStyle = OR; g.beginPath(); g.ellipse(s, 0, s * .2, s * .45, 0, 0, 7); g.fill(); g.restore();
  }
  function bouteille(x, y, s) {
    g.save(); g.translate(x, y); g.fillStyle = ROUGE;
    g.beginPath(); g.roundRect(-s * .35, -s * .2, s * .7, s * 1.1, s * .15); g.fill();
    g.fillRect(-s * .12, -s * .75, s * .24, s * .6); g.fillStyle = CREME; g.fillRect(-s * .25, s * .2, s * .5, s * .35); g.restore();
  }
  function ricardo(p, t) {
    const lt = t - p.a, k1 = back(pr(lt, 0, .35)), k2 = back(pr(lt, .2, .35)), kf = eo(pr(lt, .7, .6));
    S.texte('RICARDO, 1817', W / 2, 340, { taille: 50, coul: GRIS, esp: 8 });
    pop(k1, 290, 600, () => { g.fillStyle = al(OR, .12); g.beginPath(); g.roundRect(-210, -150, 420, 300, 30); g.fill();
      drap(0, -10, 110); S.texte('ANGLETERRE', 0, 190, { taille: 54, coul: OR, max: 420 }); });
    pop(k2, 790, 600, () => { g.fillStyle = al(ROUGE, .14); g.beginPath(); g.roundRect(-210, -150, 420, 300, 30); g.fill();
      bouteille(0, -10, 150); S.texte('PORTUGAL', 0, 190, { taille: 54, coul: ROUGE, max: 420 }); });
    // les échanges : le drap part au Portugal, le vin en Angleterre
    fleche(330, 880, 760, 880, kf, OR, 12);
    fleche(750, 1010, 320, 1010, eo(pr(lt, 1, .6)), ROUGE, 12);
    if (kf > .3) drap(lerp(350, 720, kf), 880 - 50, 40);
    const kv = eo(pr(lt, 1, .6)); if (kv > .3) bouteille(lerp(730, 360, kv), 1010 - 70, 50);
    S.texte('chacun se spécialise, puis échange', W / 2, 1140, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 });
    deux('AVANTAGES|COMPARATIFS', 1420, 110);
  }

  // ---------- pcs : les 6 groupes socioprofessionnels de l'INSEE (PCS 2020), « classes moyennes » barré
  const GROUPES = ['Agriculteurs exploitants', 'Artisans, commerçants, chefs d’entreprise', 'Cadres, professions intellectuelles sup.',
    'Professions intermédiaires', 'Employés', 'Ouvriers'];
  function pcs(p, t) {
    const lt = t - p.a;
    S.texte('LES 6 GROUPES DE L’INSEE', W / 2, 330, { taille: 62, coul: OR, max: 960 });
    GROUPES.forEach((s, i) => {
      const k = eo(pr(lt, .1 + i * .14, .3)), y = 470 + i * 140; if (k <= 0) return;
      g.save(); g.globalAlpha = k; g.translate(lerp(300, 0, k), 0);
      g.fillStyle = al(CREME, .08); g.beginPath(); g.roundRect(90, y - 55, 900, 110, 20); g.fill();
      g.fillStyle = OR; g.beginPath(); g.arc(160, y, 40, 0, 7); g.fill();
      S.texte(String(i + 1), 160, y + 3, { taille: 54, coul: NOIR });
      S.texte(s, 230, y + 2, { taille: 44, coul: CREME, align: 'left', max: 730 });
      g.restore();
    });
    const kx = eo(pr(lt, 1.1, .3)), y = 1330;
    if (kx > 0) {
      g.save(); g.globalAlpha = kx; g.strokeStyle = al(ROUGE, .8); g.lineWidth = 5; g.setLineDash([16, 12]);
      g.beginPath(); g.roundRect(90, y - 55, 900, 110, 20); g.stroke(); g.restore();
      g.save(); g.globalAlpha = kx; S.texte('?', 160, y + 3, { taille: 60, coul: ROUGE }); S.texte('Classes moyennes', 230, y + 2, { taille: 44, coul: GRIS, align: 'left', max: 730 }); g.restore();
      const kb = pr(lt, 1.35, .25); g.save(); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.moveTo(220, y); g.lineTo(lerp(220, 640, kb), y - 6); g.stroke(); g.restore();
      O.tampon('PAS UNE CASE', 760, y + 150, pr(lt, 1.5, .3), -.08, 70, ROUGE);
    }
  }

  // ---------- baril : le prix du baril multiplié par 4 (octobre 1973 → janvier 1974)
  function baril(x, y, s, c) {
    g.save(); g.translate(x, y); g.fillStyle = c; g.beginPath(); g.roundRect(-s * .55, -s * .75, s * 1.1, s * 1.5, s * .12); g.fill();
    g.strokeStyle = al(NOIR, .45); g.lineWidth = s * .07; [-.4, 0, .4].forEach(v => { g.beginPath(); g.moveTo(-s * .55, v * s); g.lineTo(s * .55, v * s); g.stroke(); });
    g.restore();
  }
  function barilP(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .2, 1.2)), n = Math.min(4, 1 + Math.floor(k * 3.999));
    S.texte('PRIX DU BARIL DE PÉTROLE', W / 2, 340, { taille: 56, coul: OR, max: 960 });
    // avant : un baril ; après : la hauteur de la colonne de prix est multipliée par 4
    const base = 1180, u = 140;
    g.save(); g.fillStyle = al(CREME, .5); g.fillRect(140, base, 800, 6); g.restore();
    g.save(); g.fillStyle = al(CREME, .25); g.beginPath(); g.roundRect(230, base - u, 200, u, 12); g.fill(); g.restore();
    baril(330, base - u - 90, 110, GRIS);
    const h = u * lerp(1, 4, k);
    g.save(); g.fillStyle = ROUGE; g.beginPath(); g.roundRect(650, base - h, 200, h, 12); g.fill(); g.restore();
    baril(750, base - h - 90, 110, ROUGE);
    S.texte('oct. 1973', 330, base + 60, { taille: 44, coul: CREME });
    S.texte('janv. 1974', 750, base + 60, { taille: 44, coul: CREME });
    pop(back(pr(lt, .3, .3)), 540, base - 330, () => S.texte('× ' + n, 0, 0, { taille: 150, coul: OR, contour: NOIR, contourL: 12 }));
    const kt = eo(pr(lt, 1.4, .3)); g.save(); g.globalAlpha = kt; deux('UN CHOC|PÉTROLIER', 1460, 110, ROUGE); g.restore();
  }

  // ---------- conjoncture : schéma, l'activité ralentit et le chômage monte
  function conjoncture(p, t) {
    const lt = t - p.a, gx = 140, gy = 430, gw = 820, gh = 700, k = eo(pr(lt, 0, 1.4));
    g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 5; g.beginPath(); g.moveTo(gx, gy); g.lineTo(gx, gy + gh); g.lineTo(gx + gw, gy + gh); g.stroke(); g.restore();
    S.texte('temps →', gx + gw - 80, gy + gh + 45, { taille: 38, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    const courbe = (f, c) => { g.save(); g.strokeStyle = c; g.lineWidth = 14; g.lineJoin = 'round'; g.lineCap = 'round'; g.beginPath();
      for (let i = 0; i <= 50 * k; i++) { const u = i / 50, x = gx + 30 + u * (gw - 60), y = gy + gh * f(u); i ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); g.restore(); };
    const act = u => .3 + (u < .35 ? 0 : (u - .35) * .75) + Math.sin(u * 20) * .015;
    const cho = u => .75 - (u < .45 ? 0 : (u - .45) * .8);
    courbe(act, OR); courbe(cho, ROUGE);
    if (k > .95) {
      pop(pr(lt, 1.4, .3), gx + gw - 170, gy + gh * act(1) + 70, () => S.texte('ACTIVITÉ ▼', 0, 0, { taille: 50, coul: OR }));
      pop(pr(lt, 1.55, .3), gx + gw - 170, gy + gh * cho(1) - 60, () => S.texte('CHÔMAGE ▲', 0, 0, { taille: 50, coul: ROUGE }));
    }
    S.texte('schéma', gx + 80, gy + gh + 45, { taille: 32, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    deux('CHÔMAGE|CONJONCTUREL', 1420, 110, ROUGE);
  }

  // ---------- commentaire : une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    g.save(); g.translate(W / 2, 800); g.scale(k, k);
    g.save(); g.fillStyle = al(CREME, .1); g.strokeStyle = OR; g.lineWidth = 8;
    g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(-250, 170); g.lineTo(-320, 280); g.lineTo(-160, 170); g.fill(); g.stroke(); g.restore();
    const msg = 'J’en ai trouvé … / 4', n = Math.floor(cl((lt - .25) / .7) * msg.length);
    S.texte(msg.slice(0, n), 0, 0, { taille: 76, coul: CREME, max: 780 });
    if (n < msg.length && Math.floor(t * 4) % 2) S.texte('|', S.largeur(msg.slice(0, n), { taille: 76 }) / 2 + 14, 0, { taille: 76, coul: OR });
    g.restore();
    deux('DIS-LE EN|COMMENTAIRE', 1300, 110, ROUGE);
  }

  return { titre, score, manche, ricardo, pcs, baril: barilP, conjoncture, commentaire };
};
window.SONS_A = (p, L) => {
  if (p.type === 'titre') L.push([p.a, 'bip', .4], [p.a + .55, 'buzz', .5]);
  if (p.type === 'score') for (let i = 0; i < 4; i++) L.push([p.a + .25 + i * (p.etape ? .22 : .12), 'pop', .4]);
  if (p.type === 'manche') L.push([p.a, 'gong', .55], [p.a + .2, 'montee', .35]);
  if (p.type === 'ricardo') L.push([p.a + .7, 'whoosh', .4], [p.a + 1, 'whoosh', .4]);
  if (p.type === 'pcs') { for (let i = 0; i < 6; i++) L.push([p.a + .1 + i * .14, 'pop', .3]); L.push([p.a + 1.35, 'stylo', .6], [p.a + 1.5, 'tampon', .7]); }
  if (p.type === 'baril') L.push([p.a + .2, 'montee', .5], [p.a + 1.4, 'boum', .6]);
  if (p.type === 'conjoncture') L.push([p.a, 'souffle', .5]);
  if (p.type === 'commentaire') L.push([p.a + .25, 'clic', .4]);
};
