// Plans propres au short « bacetat » (« L'État est-il l'ennemi de la liberté ? »), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
window.SANS_ST_A = ['chrono', 'loupe', 'oppose', 'oeil', 'pouvoirs', 'deuxlib', 'recite', 'balance'];
window.PROPRES_A = ['chrono', 'loupe', 'oppose', 'oeil', 'montreal', 'gardien', 'pouvoirs', 'watergate', 'bandes', 'deuxlib', 'recite', 'balance'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const PAPIER = '#f3ecdc', PALE = '#b8ad97';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // texte qui claque (grossit puis se pose) à l'instant ta
  const claque = (s, y, ta, t, o) => { const k = back(pr(t, ta, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
    S.texte(s, 0, 0, Object.assign({ taille: 100, coul: CREME, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };

  // compte à rebours de 60 s ; p.run : il tourne
  function chrono(p, t) {
    const u = p.run ? cl((t - p.a) / 60) : 0, reste = p.run ? Math.max(0, 60 - Math.floor(t - p.a)) : 60;
    const k = back(pr(t, p.a, .35)), r = 250;
    g.save(); g.translate(W / 2, 760); g.scale(lerp(.6, 1, k), lerp(.6, 1, k));
    g.strokeStyle = 'rgba(239,230,210,.15)'; g.lineWidth = 26; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
    g.strokeStyle = p.run ? ROUGE : OR; g.lineCap = 'round'; g.beginPath(); g.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
    for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(Math.cos(a) * (r - 50), Math.sin(a) * (r - 50)); g.lineTo(Math.cos(a) * (r - 30), Math.sin(a) * (r - 30)); g.stroke(); }
    S.texte(String(reste), 0, -10, { taille: 230, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 40 });
    S.texte('SECONDES', 0, 120, { taille: 40, coul: CREME, esp: 10, poids: 600 });
    g.restore();
    if (p.t) { const kt = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1290); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt)); g.translate(-W / 2, -1290); deux(p.t, 1290, 110); g.restore(); }
  }

  // le sujet sur une fiche ; cercles = [[repère, mot], …] entourés au stylo rouge
  function loupe(p, t) {
    const k = eo(pr(t, p.a, .35));
    const L1 = 'L’État est-il l’ennemi', L2 = 'de la liberté ?';
    const o = { taille: 76, police: 'Spectral', poids: 600, coul: NOIR };
    g.save(); g.translate(W / 2, lerp(900, 640, k)); g.rotate(-.02);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = PAPIER; g.fillRect(-470, -210, 940, 420); g.shadowColor = 'transparent';
    S.texte('SUJET · PHILOSOPHIE', 0, -140, { taille: 30, coul: GRIS, esp: 6 });
    const x0 = -S.largeur(L1, o) / 2, mots = L1.split(' ');
    const actifs = (p.cercles || []).filter(([r]) => t >= tps(r)).map(([, m]) => m);
    let x = x0; mots.forEach((m, i) => { const s = (i ? ' ' : '') + m, ws = S.largeur(s, o);
      S.texte(s, x + ws / 2, -30, Object.assign({}, o, { coul: actifs.includes(m) ? ROUGE : NOIR })); x += ws; });
    S.texte(L2, 0, 65, o);
    (p.cercles || []).forEach(([r, m]) => {
      const kc = pr(t, tps(r), .4); if (kc <= 0) return;
      const i = mots.indexOf(m), avant = mots.slice(0, i).join(' ') + (i ? ' ' : '');
      const cx = x0 + S.largeur(avant, o) + S.largeur(m, o) / 2, rx = S.largeur(m, o) / 2 + 30;
      g.strokeStyle = ROUGE; g.lineWidth = 7; g.beginPath(); g.ellipse(cx, -30, rx, 56, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    });
    g.restore();
    if (p.t) { const kt = back(pr(t, p.a + .15, .3)); g.save(); g.translate(W / 2, 1150); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt)); g.translate(-W / 2, -1150); deux(p.t, 1150, 120); g.restore(); }
  }

  // obstacle ≠ ennemi : deux cartes qui arrivent à leur repère
  function oppose(p, t) {
    O.petitTitre('« ENNEMI » : LE MOT EST FORT', 420);
    const carteO = (cx, ta, titre, sous, coul, dessin) => {
      if (t < ta) return;
      const k = back(pr(t, ta, .35));
      g.save(); g.translate(cx, 960); g.scale(k, k);
      g.fillStyle = 'rgba(239,230,210,.06)'; g.strokeStyle = coul; g.lineWidth = 6; g.beginPath(); g.roundRect(-230, -380, 460, 760, 30); g.fill(); g.stroke();
      dessin();
      S.texte(titre, 0, 170, { taille: 76, coul, max: 420 });
      S.texte(sous, 0, 270, { taille: 52, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 420 });
      g.restore();
    };
    carteO(285, tps(p.g), 'OBSTACLE', 'il te gêne', CREME, () => {
      // barrière à rayures
      g.save(); g.translate(0, -120); g.fillStyle = CREME; g.fillRect(-150, -40, 300, 80);
      g.fillStyle = ROUGE; for (let i = 0; i < 4; i++) { g.beginPath(); g.moveTo(-150 + i * 80, 40); g.lineTo(-110 + i * 80, -40); g.lineTo(-70 + i * 80, -40); g.lineTo(-110 + i * 80, 40); g.closePath(); g.fill(); }
      g.fillStyle = GRIS; g.fillRect(-140, 40, 22, 120); g.fillRect(118, 40, 22, 120); g.restore();
    });
    carteO(795, tps(p.d), 'ENNEMI', 'il veut ta perte', ROUGE, () => {
      // viseur
      g.save(); g.translate(0, -100); g.strokeStyle = ROUGE; g.lineWidth = 9;
      const pul = 1 + Math.sin(t * 8) * .05; g.scale(pul, pul);
      g.beginPath(); g.arc(0, 0, 120, 0, 7); g.stroke(); g.beginPath(); g.arc(0, 0, 60, 0, 7); g.stroke();
      [[0, -160, 0, -70], [0, 70, 0, 160], [-160, 0, -70, 0], [70, 0, 160, 0]].forEach(([a, b, c, d]) => { g.beginPath(); g.moveTo(a, b); g.lineTo(c, d); g.stroke(); });
      g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 14, 0, 7); g.fill(); g.restore();
    });
    if (t >= tps(p.d)) { const k = back(pr(t, tps(p.d) + .15, .3)); g.save(); g.translate(W / 2, 960); g.scale(k, k); S.texte('≠', 0, 0, { taille: 140, coul: OR, contour: NOIR, contourL: 12 }); g.restore(); }
  }

  // Proudhon : l'œil de l'État, et les mots qui tombent comme des tampons
  function oeil(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte('proudhon', lerp(-200, 250, k), 560, 300, 380, -.05, 1.1 + (t - p.a) * .02, .5, .3, { lum: .95 });
    S.texte('PROUDHON', 720, 470, { taille: 82, coul: OR, contour: NOIR, contourL: 10 });
    S.texte('Idée générale de la Révolution', 720, 560, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 520 });
    S.texte('au XIXᵉ siècle · 1851', 720, 610, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: PALE, max: 520 });
    // l'œil
    const cx = W / 2, cy = 1000, ko = eo(pr(t, p.a + .2, .4));
    g.save(); g.translate(cx, cy); g.scale(1, ko);
    g.fillStyle = PAPIER; g.strokeStyle = CREME; g.lineWidth = 8;
    g.beginPath(); g.moveTo(-300, 0); g.quadraticCurveTo(0, -210, 300, 0); g.quadraticCurveTo(0, 210, -300, 0); g.closePath(); g.fill(); g.stroke();
    g.save(); g.clip();
    const ix = Math.sin((t - p.a) * 1.7) * 110, iy = Math.sin((t - p.a) * 2.3) * 25;
    g.fillStyle = ROUGE; g.beginPath(); g.arc(ix, iy, 95, 0, 7); g.fill();
    g.fillStyle = NOIR; g.beginPath(); g.arc(ix, iy, 45, 0, 7); g.fill();
    g.fillStyle = 'rgba(255,255,255,.8)'; g.beginPath(); g.arc(ix + 25, iy - 28, 14, 0, 7); g.fill();
    g.restore();
    g.restore();
    // rayons qui balaient
    g.save(); g.globalAlpha = .18 * ko; g.fillStyle = OR;
    const a = Math.sin((t - p.a) * 1.7) * .5;
    g.beginPath(); g.moveTo(cx, cy); g.lineTo(cx + Math.sin(a - .25) * 900, cy + Math.cos(a - .25) * 900); g.lineTo(cx + Math.sin(a + .25) * 900, cy + Math.cos(a + .25) * 900); g.closePath(); g.fill(); g.restore();
    // la citation
    if (t >= tps(p.q)) { const kq = eo(pr(t, tps(p.q), .3)); g.save(); g.globalAlpha = kq;
      S.texte('« Être gouverné, c’est être… »', W / 2, 760, { taille: 62, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 960 }); g.restore(); }
    (p.mots || []).forEach(([r, s], j) => { const tr = tps(r); if (t < tr) return;
      const kk = pr(t, tr, .3), y = 1290 + j * 125, sc = lerp(2.2, 1, back(kk));
      g.save(); g.translate(W / 2 + (j - 1) * 40, y); g.rotate((j % 2 ? .04 : -.05)); g.scale(sc, sc); g.globalAlpha = cl(kk * 3);
      S.texte(s, 0, 0, { taille: 96, coul: j === 2 ? ROUGE : CREME, contour: NOIR, contourL: 10, max: 900 }); g.restore(); });
  }

  // Montréal, 7 octobre 1969 : l'insigne en grève, le compteur des heures, la ville qui bascule
  function montreal(p, t) {
    const tb = tps(p.bascule), bas = t >= tb, kb = pr(t, tb, .6);
    O.fondImg('gordon', 1.25 + (t - p.a) * .02, .4, .55, bas ? .45 : .25);
    // insigne de police
    g.save(); g.translate(W / 2, 520); const ki = back(pr(t, p.a, .3)); g.scale(ki, ki);
    g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 7;
    g.beginPath(); g.moveTo(0, -130); g.lineTo(110, -90); g.lineTo(100, 40); g.quadraticCurveTo(60, 110, 0, 140); g.quadraticCurveTo(-60, 110, -100, 40); g.lineTo(-110, -90); g.closePath(); g.fill(); g.stroke();
    S.texte('POLICE', 0, -10, { taille: 44, coul: CREME });
    g.restore();
    O.tampon('GRÈVE', W / 2, 540, pr(t, p.a + .15, .3), -.12, 90);
    // compteur d'heures
    const th = tps(p.h), nh = t < th ? 0 : Math.round(16 * eo(pr(t, th, .8)));
    if (t >= th) S.texte(nh + ' H', W / 2, 800, { taille: 190, police: 'Spectral', poids: 600, coul: bas ? ROUGE : OR, contour: NOIR, contourL: 12 });
    // la ville
    const sec = bas ? (rnd(t * 71) - .5) * 14 * (1 - kb * .5) : 0;
    g.save(); g.translate(sec, 0);
    const imm = [[60, 180, 230], [250, 140, 330], [400, 170, 260], [580, 120, 380], [710, 160, 280], [880, 150, 320]];
    imm.forEach(([x, w, h], i) => {
      g.fillStyle = '#1b1712'; g.strokeStyle = 'rgba(239,230,210,.7)'; g.lineWidth = 4; g.fillRect(x, 1250 - h, w, h); g.strokeRect(x, 1250 - h, w, h);
      for (let r = 0; r < Math.floor(h / 55); r++) for (let c = 0; c < Math.floor(w / 45); c++) {
        const feu = bas && rnd(i * 31 + r * 7 + c) < kb * .6;
        g.fillStyle = feu ? (Math.floor(t * 9 + r + c) % 2 ? ROUGE : '#f0a040') : 'rgba(217,180,90,.55)';
        g.fillRect(x + 14 + c * 45, 1250 - h + 18 + r * 55, 22, 30);
      }
    });
    g.restore();
    if (bas) { g.save(); g.globalAlpha = kb * .35; const gr = g.createLinearGradient(0, 1250, 0, 900); gr.addColorStop(0, ROUGE); gr.addColorStop(1, 'rgba(200,55,45,0)'); g.fillStyle = gr; g.fillRect(0, 900, W, 350); g.restore(); }
    g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(40, 1250); g.lineTo(1040, 1250); g.stroke();
    if (bas) claque('LA VILLE BASCULE', 1400, tb, t, { taille: 110, coul: ROUGE });
    else claque('SANS POLICE', 1400, p.a + .2, t, { taille: 110 });
  }

  // Locke : l'État gardien de la vie, de la liberté, des biens
  function gardien(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte('locke', W / 2, lerp(400, 560, k), 380, 460, -.03, 1.08 + (t - p.a) * .02, .5, .3, { lum: .95 });
    S.texte('LOCKE', W / 2, 860, { taille: 90, coul: OR, contour: NOIR, contourL: 10 });
    // le toit protecteur
    const ka = eo(pr(t, p.a + .3, .5));
    g.save(); g.strokeStyle = OR; g.lineWidth = 12; g.lineCap = 'round';
    g.beginPath(); g.moveTo(W / 2 - 470 * ka, 1110 - 30 * ka); g.lineTo(W / 2, 960); g.lineTo(W / 2 + 470 * ka, 1110 - 30 * ka); g.stroke(); g.restore();
    const ic = [
      (x, y) => { g.fillStyle = ROUGE; g.beginPath(); g.moveTo(x, y + 40); g.bezierCurveTo(x - 80, y - 10, x - 50, y - 70, x, y - 35); g.bezierCurveTo(x + 50, y - 70, x + 80, y - 10, x, y + 40); g.fill(); },
      (x, y) => { const b = Math.sin(t * 9) * 18; g.strokeStyle = CREME; g.lineWidth = 9; g.lineCap = 'round'; g.beginPath(); g.moveTo(x - 70, y - b); g.quadraticCurveTo(x - 30, y - 35, x, y); g.quadraticCurveTo(x + 30, y - 35, x + 70, y - b); g.stroke(); },
      (x, y) => { g.fillStyle = OR; g.beginPath(); g.moveTo(x - 60, y + 40); g.lineTo(x - 60, y - 10); g.lineTo(x, y - 60); g.lineTo(x + 60, y - 10); g.lineTo(x + 60, y + 40); g.closePath(); g.fill(); g.fillStyle = NOIR; g.fillRect(x - 15, y + 5, 30, 35); },
    ];
    (p.items || []).forEach(([r, s], j) => { const tr = tps(r); if (t < tr) return;
      const kk = back(pr(t, tr, .3)), x = 220 + j * 320, y = 1210;
      g.save(); g.translate(x, y); g.scale(kk, kk); g.translate(-x, -y);
      g.fillStyle = 'rgba(239,230,210,.07)'; g.strokeStyle = 'rgba(239,230,210,.4)'; g.lineWidth = 4; g.beginPath(); g.roundRect(x - 140, y - 110, 280, 290, 24); g.fill(); g.stroke();
      ic[j](x, y - 20);
      S.texte(s, x, y + 120, { taille: 54, coul: CREME, max: 260 }); g.restore(); });
    if ((p.items || []).length && t >= tps(p.items[p.items.length - 1][0]) + .3) claque('L’ÉTAT, GARDIEN', 1470, tps(p.items[p.items.length - 1][0]) + .3, t, { taille: 96, coul: OR });
  }

  // Montesquieu : trois pouvoirs séparés, qui s'arrêtent l'un l'autre
  function pouvoirs(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte('montesquieu', W / 2, lerp(380, 520, k), 300, 360, .03, 1.1, .5, .3, { lum: .95 });
    S.texte('MONTESQUIEU', W / 2, 770, { taille: 72, coul: OR, contour: NOIR, contourL: 10 });
    const P = [['FAIRE', 'LA LOI'], ['EXÉCUTER', 'LA LOI'], ['JUGER', '']];
    P.forEach(([a, b], j) => { const kj = back(pr(t, p.a + .25 + j * .2, .3)), x = 220 + j * 320, y = 1030;
      g.save(); g.translate(x, y); g.scale(kj, kj);
      g.fillStyle = CREME; g.fillRect(-110, -150, 220, 24); g.fillRect(-90, -126, 180, 14); g.fillRect(-110, 112, 220, 24);
      g.fillStyle = 'rgba(239,230,210,.85)'; for (let c = 0; c < 4; c++) g.fillRect(-80 + c * 45, -112, 26, 224);
      g.restore();
      S.texte(a, x, 1215, { taille: 44, coul: CREME, max: 290 }); if (b) S.texte(b, x, 1265, { taille: 36, coul: PALE, max: 290 }); });
    // butées entre les colonnes : flèches qui s'avancent puis s'arrêtent net
    const ka = pr(t, p.a + .9, .5);
    [370, 690].forEach(x => { const d = 50 * eo(ka);
      g.save(); g.strokeStyle = ROUGE; g.lineWidth = 10; g.lineCap = 'round';
      g.beginPath(); g.moveTo(x - 60, 1030); g.lineTo(x - 60 + d, 1030); g.stroke(); g.beginPath(); g.moveTo(x + 60, 1030); g.lineTo(x + 60 - d, 1030); g.stroke();
      if (ka >= 1) { g.beginPath(); g.moveTo(x, 990); g.lineTo(x, 1070); g.stroke(); } g.restore(); });
    if (t >= tps(p.q)) {
      const txt = '« … le pouvoir arrête le pouvoir »', n = Math.floor(cl((t - tps(p.q)) / 1.2) * txt.length);
      S.texte(txt.slice(0, n), W / 2, 1400, { taille: 70, police: 'Spectral', it: true, poids: 600, coul: OR, max: 980 });
      const ks = eo(pr(t, tps(p.q) + 1.2, .4)); g.save(); g.globalAlpha = ks;
      S.texte('De l’esprit des lois, XI, 4 · 1748', W / 2, 1490, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: PALE }); g.restore();
    }
  }

  // le Watergate : Nixon, 1974, la Cour suprême ; p.fin : la démission
  function watergate(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte('nixon', W / 2, 700, 860, 640, lerp(.06, -.025, k), 1.15 + (t - p.a) * .03, .5, .4, { lum: .9 });
    if (!p.fin) {
      S.texte('1974', W / 2, 1150, { taille: 170, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 });
      S.texte('L’AFFAIRE DU WATERGATE', W / 2, 1280, { taille: 54, coul: CREME, esp: 4, max: 960 });
      if (p.cour && t >= tps(p.cour)) claque('LA COUR SUPRÊME', 1420, tps(p.cour), t, { taille: 96, coul: ROUGE });
    } else {
      O.tampon('DÉMISSION', W / 2, 1160, pr(t, p.a + .05, .3), -.1, 130);
      const ks = eo(pr(t, p.a + .4, .4)); g.save(); g.globalAlpha = ks;
      S.texte('Washington, 9 août 1974', W / 2, 1360, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore();
    }
  }

  // les enregistrements : deux bobines qui tournent
  function bandes(p, t) {
    O.petitTitre('LA COUR SUPRÊME ORDONNE', 430, ROUGE);
    const ang = (t - p.a) * 5;
    [[330, 820], [750, 820]].forEach(([x, y]) => {
      g.save(); g.translate(x, y); g.rotate(ang);
      g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.arc(0, 0, 170, 0, 7); g.fill(); g.stroke();
      g.fillStyle = '#3a2f25'; g.beginPath(); g.arc(0, 0, 120, 0, 7); g.fill();
      g.fillStyle = NOIR; for (let i = 0; i < 3; i++) { const a = i * 2.094; g.beginPath(); g.arc(Math.cos(a) * 70, Math.sin(a) * 70, 30, 0, 7); g.fill(); }
      g.fillStyle = CREME; g.beginPath(); g.arc(0, 0, 18, 0, 7); g.fill(); g.restore();
    });
    g.strokeStyle = '#6b5640'; g.lineWidth = 8; g.beginPath(); g.moveTo(330, 990); g.lineTo(540, 1060); g.lineTo(750, 990); g.stroke();
    g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.roundRect(440, 1040, 200, 60, 10); g.fill(); g.stroke();
    claque('LIVRER LES', 1250, p.a + .1, t, { taille: 100 });
    claque('ENREGISTREMENTS', 1370, p.a + .25, t, { taille: 110, coul: OR });
    const ku = eo(pr(t, p.a + .6, .4)); g.save(); g.globalAlpha = ku;
    S.texte('à l’unanimité', W / 2, 1480, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore();
  }

  // Rousseau : liberté naturelle / liberté civile ; p.echange : l'État retire la première, donne la seconde
  function deuxlib(p, t) {
    O.carte('rousseau', W / 2, 520, 280, 340, -.03, 1.1, .5, .3, { lum: .95 });
    S.texte('ROUSSEAU · Du contrat social, 1762', W / 2, 740, { taille: 40, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 960 });
    const tg = p.echange ? p.a : tps(p.g), td = p.echange ? p.a : tps(p.d);
    const tr = p.echange ? tps(p.r) : 1e9, ts = p.echange ? tps(p.s) : 1e9;
    const col = (cx, ta, titre, sous, coul, eteint, allume) => {
      if (t < ta) return;
      const k = p.echange ? 1 : back(pr(t, ta, .35));
      g.save(); g.translate(cx, 1040); g.scale(k, k); g.globalAlpha = lerp(1, .35, eteint);
      if (allume > 0) { g.shadowColor = OR; g.shadowBlur = 50 * allume; }
      g.fillStyle = allume > 0 ? 'rgba(217,180,90,.16)' : 'rgba(239,230,210,.06)'; g.strokeStyle = coul; g.lineWidth = 6;
      g.beginPath(); g.roundRect(-225, -200, 450, 400, 28); g.fill(); g.stroke(); g.shadowBlur = 0;
      S.texte('LIBERTÉ', 0, -110, { taille: 60, coul: CREME });
      S.texte(titre, 0, -30, { taille: 76, coul, max: 420 });
      S.texte(sous[0], 0, 70, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 420 });
      S.texte(sous[1], 0, 125, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 420 });
      g.restore();
    };
    const er = pr(t, tr, .4), al = pr(t, ts, .4);
    col(285, tg, 'NATURELLE', ['limitée par', 'tes seules forces'], CREME, er, 0);
    col(795, td, 'CIVILE', ['garantie', 'par la loi'], OR, 0, al);
    if (p.echange) {
      if (er > 0) { g.strokeStyle = ROUGE; g.lineWidth = 12; g.lineCap = 'round'; g.beginPath(); g.moveTo(90, 870); g.lineTo(lerp(90, 480, eo(er)), lerp(870, 1210, eo(er))); g.stroke(); }
      S.d.fleche(510, 1040, 570, 1040, eo(pr(t, tr + .2, .4)), { trait: OR, ep: 12 });
      if (t >= tr) claque('L’ÉTAT RETIRE LA PREMIÈRE…', 1360, tr, t, { taille: 70 });
      if (t >= ts) claque('… POUR DONNER LA SECONDE', 1470, ts, t, { taille: 70, coul: OR });
    } else {
      S.texte('≠', W / 2, 1040, { taille: 120, coul: OR, contour: NOIR, contourL: 10 });
      O.petitTitre('LA DISTINCTION QUI DÉPASSE', 1350);
    }
  }

  // l'erreur : réciter ses auteurs à la suite, sans répondre (barré)
  function recite(p, t) {
    O.petitTitre('L’ERREUR À NE PAS FAIRE', 400, ROUGE);
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1300, 900, k)); g.rotate(-.025);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = PAPIER; g.fillRect(-460, -380, 920, 760); g.shadowColor = 'transparent';
    g.strokeStyle = 'rgba(80,110,160,.25)'; g.lineWidth = 2; for (let y = -300; y < 380; y += 80) { g.beginPath(); g.moveTo(-430, y); g.lineTo(430, y); g.stroke(); }
    g.strokeStyle = 'rgba(200,55,45,.5)'; g.beginPath(); g.moveTo(-360, -380); g.lineTo(-360, 380); g.stroke();
    const L = ['Hobbes dit que…', 'Locke dit que…', 'Proudhon dit que…', 'Rousseau dit que…', 'Montesquieu dit que…'];
    L.forEach((s, i) => { const ta = p.a + .15 + i * .3, n = Math.floor(cl((t - ta) / .3) * s.length);
      if (n > 0) S.texte(s.slice(0, n), -330, -260 + i * 120, { taille: 66, police: 'Spectral', it: true, poids: 400, coul: NOIR, align: 'left' }); });
    const tb = tps(p.barre), kb = pr(t, tb, .25), kb2 = pr(t, tb + .15, .25);
    g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round';
    if (kb > 0) { g.beginPath(); g.moveTo(-380, -300); g.lineTo(lerp(-380, 400, kb), lerp(-300, 300, kb)); g.stroke(); }
    if (kb2 > 0) { g.beginPath(); g.moveTo(400, -300); g.lineTo(lerp(400, -380, kb2), lerp(-300, 300, kb2)); g.stroke(); }
    g.restore();
    if (t >= tb) S.texte('… et la question ?', W / 2, 1420, { taille: 80, police: 'Spectral', it: true, poids: 600, coul: CREME });
    if (t >= tb + .3) O.tampon('À ÉVITER', W / 2, 1560, pr(t, tb + .3, .3), -.1, 100);
  }

  // la balance finale : ennemi ou condition ?
  function balance(p, t) {
    const lt = t - p.a, ang = Math.sin(lt * 2.2) * .16;
    const cx = W / 2, cy = 700;
    g.strokeStyle = CREME; g.lineWidth = 10; g.lineCap = 'round';
    g.beginPath(); g.moveTo(cx, cy); g.lineTo(cx, 1200); g.stroke(); g.beginPath(); g.moveTo(cx - 160, 1200); g.lineTo(cx + 160, 1200); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.arc(cx, cy, 22, 0, 7); g.fill();
    g.save(); g.translate(cx, cy); g.rotate(ang); g.strokeStyle = OR; g.beginPath(); g.moveTo(-380, 0); g.lineTo(380, 0); g.stroke(); g.restore();
    [[-1, 'ENNEMI', ROUGE], [1, 'CONDITION', OR]].forEach(([s, txt, c]) => {
      const x = cx + s * 380 * Math.cos(ang), y = cy + s * 380 * Math.sin(ang);
      g.strokeStyle = 'rgba(239,230,210,.6)'; g.lineWidth = 4; g.beginPath(); g.moveTo(x, y); g.lineTo(x - 130, y + 220); g.moveTo(x, y); g.lineTo(x + 130, y + 220); g.stroke();
      g.fillStyle = '#26221d'; g.strokeStyle = c; g.lineWidth = 6; g.beginPath(); g.ellipse(x, y + 230, 160, 36, 0, 0, 7); g.fill(); g.stroke();
      S.texte(txt, x, y + 165, { taille: 58, coul: c, contour: NOIR, contourL: 8, max: 300 });
    });
    const k = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1420); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -1420); deux(p.t, 1420, 110); g.restore();
  }

  return { chrono, loupe, oppose, oeil, montreal, gardien, pouvoirs, watergate, bandes, deuxlib, recite, balance };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono') { if (p.run) for (let x = p.a; x < p.b - .1; x += 1) L.push([x, 'tic', .5]); else L.push([p.a + .1, 'tic', .4]); }
  if (p.type === 'loupe') (p.cercles || []).forEach(([r]) => L.push([tps(r), 'stylo', .5]));
  if (p.type === 'oppose') L.push([tps(p.g), 'pop', .4], [tps(p.d), 'lame', .5]);
  if (p.type === 'oeil') { L.push([p.a, 'souffle', .35]); (p.mots || []).forEach(([r]) => L.push([tps(r), 'tampon', .55])); }
  if (p.type === 'montreal') { L.push([p.a + .15, 'tampon', .8], [tps(p.h), 'montee', .45], [tps(p.bascule), 'boum', .7]); }
  if (p.type === 'gardien') (p.items || []).forEach(([r]) => L.push([tps(r), 'valide', .45]));
  if (p.type === 'pouvoirs') { L.push([p.a + .9 + .5, 'clic', .6]); L.push([tps(p.q), 'stylo', .4]); }
  if (p.type === 'watergate') { if (p.fin) L.push([p.a + .05, 'tampon', 1]); else { L.push([p.a, 'papier', .35]); if (p.cour) L.push([tps(p.cour), 'gong', .4]); } }
  if (p.type === 'bandes') L.push([p.a, 'rembobine', .5]);
  if (p.type === 'deuxlib') { if (p.echange) L.push([tps(p.r), 'lame', .5], [tps(p.s), 'valide', .6]); else L.push([tps(p.g), 'pop', .4], [tps(p.d), 'pop', .4]); }
  if (p.type === 'recite') { L.push([p.a + .15, 'stylo', .5], [tps(p.barre), 'lame', .6], [tps(p.barre) + .35, 'tampon', 1]); }
  if (p.type === 'balance') L.push([p.a, 'frotte', .35]);
};
