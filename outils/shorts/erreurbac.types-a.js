// Plans propres au short « erreurbac » (trouve l'erreur dans trois copies de bac), modèle A.
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
window.SANS_ST_A = ['copies', 'pret', 'manche', 'barre', 'jalons', 'score'];
window.PROPRES_A = ['copies', 'pret', 'manche', 'barre', 'jalons', 'anaphase', 'score'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 110) => { const k = back(pr(t, a, .3)); g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  // feuille de copie : fond crème, lignes, marge rouge, gribouillis d'écriture
  function feuille(w, h, n = 6, rouge = -1) {
    g.shadowColor = al(NOIR, .7); g.shadowBlur = 30; g.fillStyle = CREME; g.fillRect(-w / 2, -h / 2, w, h); g.shadowColor = 'transparent';
    g.strokeStyle = al(ROUGE, .5); g.lineWidth = 3; g.beginPath(); g.moveTo(-w / 2 + w * .16, -h / 2); g.lineTo(-w / 2 + w * .16, h / 2); g.stroke();
    for (let i = 0; i < n; i++) {
      const y = -h / 2 + h * .25 + i * h * .7 / n, l = w * (.55 + rnd(i * 3.7 + w) * .22);
      g.strokeStyle = i === rouge ? ROUGE : al(NOIR, .55); g.lineWidth = 5; g.beginPath(); g.moveTo(-w / 2 + w * .22, y);
      for (let x = 0; x < l; x += 14) g.lineTo(-w / 2 + w * .22 + x, y + Math.sin(x * .35 + i) * 4);
      g.stroke();
    }
  }

  // trois copies qui tombent en éventail ; chacune a une ligne entourée de rouge et un « ? »
  function copies(p, t) {
    const L = [['PHILO', -320, 760, -.14], ['HISTOIRE', 0, 700, .02], ['SVT', 320, 760, .14]];
    L.forEach(([nom, dx, y, r], i) => {
      const k = back(pr(t, p.a + i * .14, .35)); if (k <= 0) return;
      g.save(); g.translate(W / 2 + dx, lerp(-500, y, k)); g.rotate(r * (2 - k));
      feuille(330, 460, 6, 3);
      S.texte(nom, 0, -180, { taille: 40, coul: NOIR, esp: 4, max: 290 });
      const kc = pr(t, p.a + .5 + i * .15, .4);
      g.strokeStyle = ROUGE; g.lineWidth = 7; g.beginPath(); g.ellipse(0, 70, 150, 34, -.05, -1.5, -1.5 + kc * 6.6); g.stroke();
      if (kc > .9) S.texte('?', 120, 150, { taille: 90, coul: ROUGE });
      g.restore();
    });
    titrePop(p.t, 1320, t, p.a + .5, 120);
  }

  // « ON JOUE ! » : cercle de départ qui se remplit, trois points qui s'allument
  function pret(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 820); g.scale(k, k);
    g.strokeStyle = al(CREME, .18); g.lineWidth = 30; g.beginPath(); g.arc(0, 0, 260, 0, 7); g.stroke();
    g.strokeStyle = OR; g.lineCap = 'round'; g.beginPath(); g.arc(0, 0, 260, -Math.PI / 2, -Math.PI / 2 + eo(cl(lt / 1.1)) * 6.283); g.stroke();
    for (let i = 0; i < 3; i++) { const on = lt > .2 + i * .25; g.fillStyle = on ? (i === 2 ? ROUGE : OR) : al(CREME, .2); g.beginPath(); g.arc((i - 1) * 120, 0, 42, 0, 7); g.fill(); }
    g.restore();
    const kt = back(pr(t, p.a + .5, .3)); g.save(); g.translate(W / 2, 1300); g.scale(lerp(2, 1, kt), lerp(2, 1, kt)); g.globalAlpha = cl(kt * 2);
    S.texte(p.t, 0, 0, { taille: 160, coul: OR, contour: NOIR, contourL: 14, max: 960 }); g.restore();
  }

  // petits dessins de matière
  function dessin(nom, t) {
    g.strokeStyle = OR; g.fillStyle = OR; g.lineWidth = 12; g.lineCap = 'round'; g.lineJoin = 'round';
    if (nom === 'plume') {
      g.save(); g.rotate(-.6); g.beginPath(); g.moveTo(0, 150); g.quadraticCurveTo(110, 0, 0, -170); g.quadraticCurveTo(-110, 0, 0, 150); g.stroke();
      g.beginPath(); g.moveTo(0, 190); g.lineTo(0, -120); g.stroke();
      for (let i = 0; i < 5; i++) { g.beginPath(); g.moveTo(0, 80 - i * 45); g.lineTo(i % 2 ? 50 : -50, 40 - i * 45); g.stroke(); }
      g.restore();
    } else if (nom === 'sablier') {
      const r = (t * .8) % 1;
      g.beginPath(); g.moveTo(-110, -170); g.lineTo(110, -170); g.moveTo(-110, 170); g.lineTo(110, 170); g.stroke();
      g.lineWidth = 9; g.beginPath(); g.moveTo(-90, -170); g.quadraticCurveTo(-90, -30, 0, 0); g.quadraticCurveTo(-90, 30, -90, 170);
      g.moveTo(90, -170); g.quadraticCurveTo(90, -30, 0, 0); g.quadraticCurveTo(90, 30, 90, 170); g.stroke();
      g.fillStyle = ROUGE; g.beginPath(); g.moveTo(-70 + r * 40, -150 + r * 80); g.lineTo(70 - r * 40, -150 + r * 80); g.lineTo(0, -20); g.fill();
      g.beginPath(); g.moveTo(-80, 160); g.lineTo(80, 160); g.lineTo(0, 160 - 40 - r * 50); g.fill();
      g.fillRect(-3, -20, 6, 170);
    } else {  // double hélice
      for (let s = 0; s < 2; s++) { g.strokeStyle = s ? ROUGE : OR; g.beginPath();
        for (let y = -180; y <= 180; y += 6) { const x = Math.sin(y / 45 + t * 3 + s * Math.PI) * 80; y === -180 ? g.moveTo(x, y) : g.lineTo(x, y); } g.stroke(); }
      g.strokeStyle = al(CREME, .6); g.lineWidth = 5;
      for (let y = -165; y <= 165; y += 30) { const x = Math.sin(y / 45 + t * 3) * 80; g.beginPath(); g.moveTo(x, y); g.lineTo(-x, y); g.stroke(); }
    }
  }
  // carte « MANCHE n / 3 » avec la matière et un dessin
  function manche(p, t) {
    const k = back(pr(t, p.a, .35));
    S.texte('MANCHE', W / 2, 420, { taille: 70, coul: CREME, esp: 18 });
    g.save(); g.translate(W / 2, 640); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(p.n + ' / 3', 0, 0, { taille: 250, police: 'Spectral', poids: 600, coul: OR, ombre: al(OR, .45), flou: 40 }); g.restore();
    const kd = eo(pr(t, p.a + .2, .4)); g.save(); g.translate(W / 2, 1100); g.scale(kd, kd); g.rotate(lerp(-.5, 0, kd));
    g.fillStyle = al(CREME, .06); g.beginPath(); g.arc(0, 0, 250, 0, 7); g.fill(); g.strokeStyle = al(OR, .5); g.lineWidth = 4; g.stroke();
    dessin(p.dessin, t); g.restore();
    const kb = eo(pr(t, p.a + .1, .3)); g.save(); g.translate(lerp(-W, 0, kb), 0);
    g.fillStyle = ROUGE; g.fillRect(0, 1420, W, 130); S.texte(p.matiere, W / 2, 1487, { taille: 90, coul: CREME, esp: 6, max: 980 }); g.restore();
  }

  // portrait barré d'une grande croix rouge
  function barre(p, t) {
    const k = eo(pr(t, p.a, .3));
    O.carte(p.img, W / 2, 760, 600, 760, lerp(.1, -.03, k), 1.08, .5, .3);
    [[-1, 0], [1, .12]].forEach(([s, d]) => { const kx = eo(pr(t, p.a + .25 + d, .2)); if (kx <= 0) return;
      g.save(); g.strokeStyle = ROUGE; g.lineWidth = 34; g.lineCap = 'round'; g.beginPath();
      g.moveTo(W / 2 - 300 * s, 420); g.lineTo(W / 2 - 300 * s + 600 * s * kx, 420 + 680 * kx); g.stroke(); g.restore(); });
    O.tampon(p.t, W / 2, 1380, pr(t, p.a + .5, .3), -.08, 120, ROUGE);
  }

  // frise : jalons = [[repère, année, libellé], …] qui s'allument au fil de la voix
  function jalons(p, t) {
    const E = p.etapes || [], x0 = 170, x1 = 910, y = 900;
    O.petitTitre('LA CHRONOLOGIE', 420);
    g.save(); g.strokeStyle = al(CREME, .35); g.lineWidth = 10; g.beginPath(); g.moveTo(x0 - 60, y); g.lineTo(x1 + 60, y); g.stroke(); g.restore();
    E.forEach(([a, an, lab], i) => {
      const ta = tps(a), x = lerp(x0, x1, E.length > 1 ? i / (E.length - 1) : .5), on = t >= ta, k = back(pr(t, ta, .3)), dern = i === E.length - 1;
      if (on && i > 0) { const kl = eo(pr(t, ta, .35)), xp = lerp(x0, x1, (i - 1) / (E.length - 1)); g.save(); g.strokeStyle = OR; g.lineWidth = 12; g.beginPath(); g.moveTo(xp, y); g.lineTo(lerp(xp, x, kl), y); g.stroke(); g.restore(); }
      g.save(); g.translate(x, y); g.fillStyle = on ? (dern ? ROUGE : OR) : al(CREME, .25); g.beginPath(); g.arc(0, 0, 34, 0, 7); g.fill(); g.restore();
      if (!on) return;
      g.save(); g.translate(x, y - 130); g.scale(k, k); S.texte(an, 0, 0, { taille: 92, police: 'Spectral', poids: 600, coul: dern ? ROUGE : OR, contour: NOIR, contourL: 8 }); g.restore();
      g.save(); g.globalAlpha = cl(k); S.texte(lab, x, y + 110, { taille: 40, coul: CREME, poids: 700, max: 300 }); g.restore();
    });
    const der = E[E.length - 1];
    if (p.t && der && t >= tps(der[0])) { const kt = back(pr(t, tps(der[0]) + .2, .3)); g.save(); g.globalAlpha = cl(kt * 2); g.translate(W / 2, 1320); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt));
      S.texte(p.t, 0, 0, { taille: 80, coul: OR, contour: NOIR, contourL: 10, max: 960 }); g.restore(); }
  }

  // la méiose : une paire d'homologues (or, rouge), chaque chromosome à deux chromatides.
  // Avant p.e2 : anaphase I (les homologues se séparent) ; après : anaphase II (les chromatides se séparent).
  function baton(x, y, h, w, coul) { g.beginPath(); g.roundRect(x - w / 2, y - h / 2, w, h, w / 2); g.fillStyle = coul; g.fill(); g.strokeStyle = NOIR; g.lineWidth = 3; g.stroke(); }
  function chromo(x, y, h, coul, double, ecart = 0) {
    if (double) { baton(x - 13 - ecart, y, h, 22, coul); baton(x + 13 + ecart, y, h, 22, coul); if (ecart < 4) { g.beginPath(); g.arc(x, y - h * .1, 12, 0, 7); g.fillStyle = coul; g.fill(); g.strokeStyle = NOIR; g.lineWidth = 3; g.stroke(); } }
    else baton(x, y, h, 22, coul);
  }
  function anaphase(p, t) {
    const t2 = tps(p.e2), deuxieme = t >= t2;
    g.save(); g.translate(W / 2, 900); g.scale(1.45, 1.45); g.translate(-W / 2, -900);
    if (!deuxieme) {
      const k = eio(pr(t, p.a + .3, 1.2));
      g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 5; g.beginPath(); g.ellipse(W / 2, 900, lerp(300, 270, k), lerp(260, 330, k), 0, 0, 7); g.stroke(); g.restore();
      fuseau(900, 330);
      chromo(W / 2, lerp(840, 690, k), 170, OR, true); chromo(W / 2, lerp(960, 1110, k), 170, ROUGE, true);
      g.restore(); O.petitTitre('ANAPHASE I', 330, OR);
      S.texte('les homologues se séparent', W / 2, 1450, { taille: 64, coul: CREME, max: 960 });
      S.texte('chaque chromosome garde ses 2 chromatides', W / 2, 1530, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 960 });
    } else {

      const k = eio(pr(t, t2 + .2, 1.2));
      [[W / 2 - 170, OR], [W / 2 + 170, ROUGE]].forEach(([x, c]) => {
        g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 5; g.beginPath(); g.ellipse(x, 900, 150, lerp(200, 270, k), 0, 0, 7); g.stroke(); g.restore();
        chromo(x, lerp(900, 800, k), 130, c, false); chromo(x, lerp(900, 1000, k), 130, c, false);
        if (k < .05) chromo(x, 900, 130, c, true);
      });
      g.restore(); O.petitTitre('ANAPHASE II', 330, ROUGE);
      S.texte('les chromatides se séparent', W / 2, 1450, { taille: 64, coul: CREME, max: 960 });
      S.texte('l’erreur classique : confondre les deux', W / 2, 1530, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 960 });
    }
  }
  const eio = S.eio;
  function fuseau(y, h) { g.save(); g.strokeStyle = al(OR, .25); g.lineWidth = 3; for (let i = -3; i <= 3; i++) { g.beginPath(); g.moveTo(W / 2, y - h); g.quadraticCurveTo(W / 2 + i * 70, y, W / 2, y + h); g.stroke(); } g.restore(); }

  // ton score : trois copies cochées, les chiffres 0, 1, 2, 3 qui s'allument à leur repère (p.n)
  function score(p, t) {
    O.petitTitre('TON SCORE', 380);
    const N = p.n || [];
    N.forEach((a, i) => {
      const ta = tps(a), on = t >= ta, k = back(pr(t, ta, .3)), x = W / 2 + (i - 1.5) * 220, actif = on && (!N[i + 1] || t < tps(N[i + 1]));
      g.save(); g.translate(x, 700); g.scale(on ? lerp(.6, actif ? 1.15 : 1, k) : .8, on ? lerp(.6, actif ? 1.15 : 1, k) : .8);
      g.fillStyle = actif ? OR : al(CREME, on ? .2 : .06); g.beginPath(); g.roundRect(-90, -110, 180, 220, 24); g.fill();
      S.texte(String(i), 0, 6, { taille: 150, police: 'Spectral', poids: 600, coul: actif ? NOIR : CREME }); g.restore();
    });
    S.texte('/ 3', W / 2, 920, { taille: 90, coul: GRIS, poids: 700 });
    ['PHILO', 'HISTOIRE', 'SVT'].forEach((s, i) => { const k = eo(pr(t, p.a + .2 + i * .12, .3)); g.save(); g.globalAlpha = k;
      g.translate(W / 2 + (i - 1) * 320, 1250); g.rotate((i - 1) * .06); feuille(260, 340, 5, 2); S.texte(s, 0, -130, { taille: 34, coul: NOIR, esp: 3, max: 230 }); g.restore(); });
    const kt = back(pr(t, p.a + .4, .3)); g.save(); g.globalAlpha = cl(kt * 2); g.translate(W / 2, 1560); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt));
    S.texte('COMBIEN ?', 0, 0, { taille: 110, coul: OR, contour: NOIR, contourL: 10 }); g.restore();
  }

  return { copies, pret, manche, barre, jalons, anaphase, score };
};
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'copies') [0, 1, 2].forEach(i => L.push([p.a + i * .14, 'papier', .45]));
  if (p.type === 'pret') L.push([p.a, 'montee', .6], [p.a + .5, 'drop', .8]);
  if (p.type === 'manche') L.push([p.a, 'chapitre', .8]);
  if (p.type === 'barre') L.push([p.a + .25, 'lame', .7], [p.a + .5, 'tampon', .8]);
  if (p.type === 'jalons') (p.etapes || []).forEach(([a], i) => L.push([tps(a), i === p.etapes.length - 1 ? 'valide' : 'blip', .6]));
  if (p.type === 'anaphase') L.push([p.a + .3, 'aspire', .5], [tps(p.e2) + .2, 'aspire', .5]);
  if (p.type === 'score') (p.n || []).forEach(a => L.push([tps(a), 'pop', .5]));
};
