// Plans propres au short « devinehlp » (« HLP : devine l'auteur en 3 indices »), modèle A, habillage « alerte ».
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
window.SANS_ST_A = ['devine2', 'mosaique', 'regles', 'manche', 'aveu', 'chambre', 'madeleine', 'maison', 'score'];
window.PROPRES_A = ['devine2', 'mosaique', 'regles', 'manche', 'aveu', 'chambre', 'madeleine', 'maison', 'score'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 110) => { const k = back(pr(t, a, .3)); if (k <= 0) return; g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
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

  // un portrait mystère en mosaïque qui scintille ; p.fin : « le prochain auteur ? »
  function mosaique(p, t) {
    const n = 9, c = 560, x0 = W / 2 - c / 2, y0 = 480, k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, y0 + c / 2); g.scale(k, k); g.translate(-W / 2, -(y0 + c / 2));
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
      const dx = (i + .5) / n - .5, dy = (j + .5) / n - .42, v = Math.exp(-(dx * dx * 7 + dy * dy * 4)) * .85 + rnd(i * 7 + j * 13 + Math.floor(t * 6)) * .15;
      g.fillStyle = al(CREME, .06 + v * .6); g.fillRect(x0 + i * c / n, y0 + j * c / n, c / n + .5, c / n + .5);
    }
    g.strokeStyle = OR; g.lineWidth = 8; g.strokeRect(x0, y0, c, c);
    S.texte('?', W / 2, y0 + c / 2, { taille: 300, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 14 });
    g.restore();
    if (!p.fin) { S.texte('HLP', W / 2, 360, { taille: 90, coul: OR, esp: 20 }); titrePop('DEVINE|L’AUTEUR', 1260, t, p.a + .15, 130);
      const kb = eo(pr(t, p.a + .5, .3)); g.save(); g.globalAlpha = kb; S.texte('EN 3 INDICES', W / 2, 1460, { taille: 80, coul: CREME, esp: 6 }); g.restore(); }
    else { S.texte('AUTEUR SUIVANT', W / 2, 380, { taille: 70, coul: OR, esp: 8 }); titrePop('EN COMBIEN|D’INDICES ?', 1300, t, p.a + .15, 120); }
  }

  // les règles : trois bandeaux d'indices, du difficile au facile
  function regles(p, t) {
    O.petitTitre('LES RÈGLES', 420);
    const E = p.etapes || [];
    S.d.tete(W / 2 - 20, 700, 170, { trait: CREME, fond: al(NOIR, .6), ep: 7 });
    S.texte('?', W / 2, 660, { taille: 160, coul: OR, contour: NOIR, contourL: 10 });
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

  // carte « MANCHE n / 3 » avec la partie du programme
  function manche(p, t) {
    const k = back(pr(t, p.a, .35));
    S.texte('MANCHE', W / 2, 420, { taille: 70, coul: CREME, esp: 18 });
    g.save(); g.translate(W / 2, 640); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(p.n + ' / 3', 0, 0, { taille: 250, police: 'Spectral', poids: 600, coul: OR, ombre: al(OR, .45), flou: 40 }); g.restore();
    const kd = eo(pr(t, p.a + .2, .4)); g.save(); g.translate(W / 2, 1040); g.scale(kd, kd);
    g.fillStyle = al(CREME, .06); g.beginPath(); g.arc(0, 0, 200, 0, 7); g.fill();
    g.strokeStyle = OR; g.lineWidth = 8; g.setLineDash([24, 16]); g.lineDashOffset = -t * 60; g.stroke(); g.setLineDash([]);
    S.d.tete(-25, 10, 110, { trait: CREME, fond: al(NOIR, .5), ep: 6 });
    S.texte('?', 0, -10, { taille: 140, coul: ROUGE, contour: NOIR, contourL: 10 }); g.restore();
    const kb = eo(pr(t, p.a + .1, .3)); g.save(); g.translate(lerp(-W, 0, kb), 0);
    g.fillStyle = ROUGE; g.fillRect(0, 1330, W, 230);
    S.texte('PROGRAMME HLP · LA RECHERCHE DE SOI', W / 2, 1300, { taille: 30, coul: OR, esp: 4, poids: 700, max: 1000 });
    p.matiere.split('|').forEach((s, i) => S.texte(s, W / 2, 1400 + i * 90, { taille: 72, coul: CREME, esp: 3, max: 1000 }));
    g.restore();
  }

  // Rousseau avoue : le livre des Confessions s'ouvre, tampon « IL AVOUE TOUT »
  function aveu(p, t) {
    const k = eo(pr(t, p.a, .4)), ta = tps(p.avoue);
    g.save(); g.translate(W / 2, 820);
    // page gauche et page droite qui s'ouvrent
    g.fillStyle = al(NOIR, .5); g.fillRect(-420, -330, 840, 680);
    g.fillStyle = CREME; g.fillRect(0, -340, 420 * k, 660); g.fillRect(-420 * k, -340, 420 * k, 660);
    g.strokeStyle = al(NOIR, .5); g.lineWidth = 3; g.beginPath(); g.moveTo(0, -340); g.lineTo(0, 320); g.stroke();
    if (k > .8) {
      S.texte('LES', -210, -230, { taille: 48, police: 'Spectral', poids: 600, coul: NOIR });
      S.texte('CONFESSIONS', -210, -170, { taille: 54, police: 'Spectral', poids: 600, coul: NOIR, max: 360 });
      S.texte('Livre premier', -210, -100, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 360 });
      for (let i = 0; i < 9; i++) { g.fillStyle = al(NOIR, .22); g.fillRect(-370, -20 + i * 34, i === 8 ? 180 : 300, 10); g.fillRect(50, -270 + i * 34 + (i > 6 ? 0 : 0), i === 8 ? 160 : 320, 10); }
      for (let i = 0; i < 6; i++) { g.fillStyle = al(NOIR, .22); g.fillRect(50, 40 + i * 34, 320 - (i === 5 ? 140 : 0), 10); }
    }
    g.restore();
    if (t >= ta) O.tampon('IL AVOUE TOUT', W / 2, 900, pr(t, ta, .3), -.1, 92, ROUGE);
    titrePop('LES CONFESSIONS|DE ROUSSEAU', 1370, t, p.a + .2, 100);
  }

  // Proust : une chambre la nuit, murs de liège, lampe, la page qui s'écrit
  function chambre(p, t) {
    const lt = t - p.a, k = eo(pr(t, p.a, .4));
    // murs de liège : petits carreaux bruns dorés
    g.save(); g.globalAlpha = k;
    for (let i = 0; i < 12; i++) for (let j = 0; j < 9; j++) {
      g.fillStyle = al(OR, .1 + rnd(i * 11 + j * 7) * .14); g.fillRect(40 + i * 84, 300 + j * 84, 80, 80);
      for (let d = 0; d < 4; d++) { g.fillStyle = al(NOIR, .35); g.fillRect(40 + i * 84 + rnd(i + j * 3 + d) * 72, 300 + j * 84 + rnd(i * 5 + j + d * 9) * 72, 5, 5); }
    }
    g.restore();
    // la lune à la fenêtre
    g.fillStyle = al(NOIR, .85); g.fillRect(700, 360, 240, 300); g.strokeStyle = CREME; g.lineWidth = 6; g.strokeRect(700, 360, 240, 300);
    g.fillStyle = CREME; g.beginPath(); g.arc(820, 470, 50, 0, 7); g.fill(); g.fillStyle = al(NOIR, .85); g.beginPath(); g.arc(842, 455, 46, 0, 7); g.fill();
    // le lit, la lampe et le halo
    const halo = g.createRadialGradient(360, 820, 20, 360, 820, 420); halo.addColorStop(0, al(OR, .45 + .05 * Math.sin(lt * 6))); halo.addColorStop(1, al(OR, 0));
    g.fillStyle = halo; g.fillRect(0, 380, W, 900);
    g.fillStyle = OR; g.beginPath(); g.moveTo(300, 760); g.lineTo(420, 760); g.lineTo(390, 700); g.lineTo(330, 700); g.closePath(); g.fill();
    g.fillStyle = CREME; g.fillRect(355, 760, 10, 80);
    g.fillStyle = CREME; g.fillRect(120, 880, 840, 150); g.fillStyle = al(NOIR, .3); g.fillRect(120, 1000, 840, 30);
    // la page posée sur le lit, qui s'écrit
    g.save(); g.translate(560, 930); g.rotate(-.05); g.fillStyle = al(CREME, 1); g.strokeStyle = al(NOIR, .4); g.lineWidth = 3; g.fillRect(-170, -60, 340, 120); g.strokeRect(-170, -60, 340, 120);
    const n = Math.floor(cl(lt / 1.6) * 5); for (let i = 0; i < n; i++) { g.fillStyle = al(NOIR, .5); g.fillRect(-150, -42 + i * 20, 300 - (i === 4 ? 120 : 0), 6); }
    g.restore();
    titrePop('LA NUIT,|DANS LE LIÈGE', 1330, t, p.a + .15, 120);
    S.texte('contre le bruit de la ville', W / 2, 1500, { taille: 52, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  // la madeleine : la tasse, la madeleine qui trempe ; à p.revient, les souvenirs remontent
  function madeleine(p, t) {
    const lt = t - p.a, tr = tps(p.revient), rev = t >= tr;
    // tasse
    g.save(); g.translate(W / 2, 1000);
    g.fillStyle = CREME; g.beginPath(); g.ellipse(0, 120, 300, 50, 0, 0, 7); g.fill();
    g.beginPath(); g.moveTo(-200, -60); g.lineTo(200, -60); g.quadraticCurveTo(190, 110, 0, 110); g.quadraticCurveTo(-190, 110, -200, -60); g.fill();
    g.strokeStyle = CREME; g.lineWidth = 22; g.beginPath(); g.arc(215, 10, 55, -1.2, 1.3); g.stroke();
    g.fillStyle = al(OR, .7); g.beginPath(); g.ellipse(0, -60, 200, 32, 0, 0, 7); g.fill();
    // madeleine : coquille dorée qui descend dans le thé
    const dy = lerp(-330, -120, eo(pr(t, p.a, .8)));
    g.save(); g.translate(-30, dy); g.rotate(.5);
    g.fillStyle = OR; g.beginPath(); g.ellipse(0, 0, 120, 75, 0, Math.PI, 0); g.lineTo(120, 10); g.quadraticCurveTo(0, 40, -120, 10); g.closePath(); g.fill();
    g.strokeStyle = al(NOIR, .35); g.lineWidth = 5; for (let i = -4; i <= 4; i++) { g.beginPath(); g.moveTo(i * 4, 20); g.lineTo(i * 26, -62 + Math.abs(i) * 8); g.stroke(); }
    g.restore();
    g.restore();
    // vapeur, puis les souvenirs qui remontent
    for (let i = 0; i < 5; i++) { const u = (lt * .5 + i / 5) % 1; g.strokeStyle = al(CREME, .35 * (1 - u)); g.lineWidth = 8; g.beginPath();
      g.moveTo(W / 2 - 120 + i * 60, 880 - u * 300); g.quadraticCurveTo(W / 2 - 90 + i * 60, 840 - u * 300, W / 2 - 120 + i * 60, 800 - u * 300); g.stroke(); }
    if (rev) ['COMBRAY', 'LA TANTE', 'LE DIMANCHE', 'L’ENFANCE'].forEach((s, i) => {
      const k = eo(pr(t, tr + i * .12, .5)); if (k <= 0) return;
      g.save(); g.globalAlpha = k; S.texte(s, [280, 800, 300, 780][i], lerp(860, [420, 480, 600, 640][i], k), { taille: 52, police: 'Spectral', it: true, poids: 600, coul: OR, max: 420 }); g.restore();
    });
    titrePop(rev ? 'TOUT LE PASSÉ|REVIENT' : 'UN GOÛT,|UN SOUVENIR', 1380, t, rev ? tr : p.a + .1, 120);
  }

  // Freud : la maison du moi ; le moi n'occupe qu'une petite pièce, le reste est dans l'ombre
  function maison(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 880); g.scale(k, k);
    // toit et murs
    g.fillStyle = al(CREME, .1); g.strokeStyle = CREME; g.lineWidth = 10;
    g.beginPath(); g.moveTo(-380, -180); g.lineTo(0, -480); g.lineTo(380, -180); g.closePath(); g.fill(); g.stroke();
    g.strokeRect(-340, -180, 680, 560); g.fillRect(-340, -180, 680, 560);
    // pièces : six fenêtres sombres et une seule éclairée (le moi)
    const P = [[-210, -60], [0, -60], [210, -60], [-210, 160], [0, 160], [210, 160]];
    P.forEach(([x, y], i) => {
      const moi = i === 3;
      g.fillStyle = moi ? OR : al(NOIR, .85); g.fillRect(x - 80, y - 70, 160, 140);
      g.strokeStyle = moi ? OR : al(CREME, .5); g.lineWidth = 5; g.strokeRect(x - 80, y - 70, 160, 140);
      if (moi) S.texte('MOI', x, y, { taille: 52, coul: NOIR });
      else { const v = .25 + .25 * Math.sin(lt * 3 + i * 1.7); S.texte('?', x, y, { taille: 70, coul: al(ROUGE, v + .3), police: 'Spectral', poids: 600 }); }
    });
    g.restore();
    titrePop('LE MOI N’EST PAS MAÎTRE|DANS SA PROPRE MAISON', 1430, t, p.a + .15, 82);
  }

  // ton score : les trois visages révélés, « ? / 3 », « dis-le en commentaire »
  function score(p, t) {
    O.petitTitre('TON SCORE', 360);
    (p.imgs || []).forEach(([nom, lab], i) => {
      const k = back(pr(t, p.a + i * .15, .35)); if (k <= 0) return;
      const x = W / 2 + (i - 1) * 330, y = 760;
      g.save(); g.translate(x, lerp(-400, y, cl(k))); g.rotate((i - 1) * .05);
      O.carte(nom, 0, 0, 280, 360, 0, 1.1, .5, .3);
      S.texte(lab, 0, 240, { taille: 44, coul: OR, max: 300 });
      g.restore();
    });
    const kt = back(pr(t, p.a + .5, .3)); g.save(); g.globalAlpha = cl(kt * 2); g.translate(W / 2, 1250); g.scale(lerp(1.5, 1, kt), lerp(1.5, 1, kt));
    S.texte('? / 3', 0, 0, { taille: 200, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 12 }); g.restore();
    if (t >= tps(p.dis)) { const kd = back(pr(t, tps(p.dis), .3)); g.save(); g.translate(W / 2, 1480); g.scale(kd, kd);
      S.texte('DIS-LE EN COMMENTAIRE', 0, 0, { taille: 70, coul: OR, contour: NOIR, contourL: 8, max: 980 }); g.restore(); }
  }

  return { devine2, mosaique, regles, manche, aveu, chambre, madeleine, maison, score };
};
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'devine2' && p.sons) {
    (p.indices || []).forEach(([a]) => L.push([tps(a), 'pop', .5]));
    const tc = tps(p.chrono), tr = tps(p.rep);
    for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]);
    L.push([tr, 'gong', .8]);
  }
  if (p.type === 'mosaique') L.push([p.a, p.fin ? 'whoosh' : 'statique', .4]);
  if (p.type === 'regles') (p.etapes || []).forEach(([a]) => L.push([tps(a), 'blip', .5]));
  if (p.type === 'manche') L.push([p.a, 'chapitre', .8]);
  if (p.type === 'aveu') L.push([p.a, 'papier', .6], [tps(p.avoue), 'tampon', .8]);
  if (p.type === 'chambre') L.push([p.a, 'souffle', .4], [p.a + .3, 'stylo', .4]);
  if (p.type === 'madeleine') L.push([p.a, 'aspire', .4], [tps(p.revient), 'montee', .5]);
  if (p.type === 'maison') L.push([p.a + .1, 'coeur', .7]);
  if (p.type === 'score') { [0, 1, 2].forEach(i => L.push([p.a + i * .15, 'pop', .45])); L.push([tps(p.dis), 'blip', .6]); }
};
