// Plans propres au short Millikan (« Il voulait prouver qu'Einstein avait tort »), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
window.SANS_ST_A = ['article', 'sujetpc'];
window.PROPRES_A = ['annees', 'tort', 'grains', 'metal', 'onde', 'cible', 'oxyde', 'tube', 'mesure', 'droite', 'article', 'nobel', 'sujetpc'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const VERT = '#7fbf6a', VIOLET = '#9b6bff', VERRE = 'rgba(160,200,220,.18)';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const sous = (s, y, taille = 60) => S.texte(s, W / 2, y, { taille, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 8, max: 960 });
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const etiquette = (s, x, y, coul = CREME, taille = 40) => S.texte(s, x, y, { taille, coul, contour: NOIR, contourL: 8, poids: 700 });

  // 0 → n années qui défilent, cercle de n graduations qui se remplit
  function annees(p, t) {
    const n = p.n || 10, k = eo(pr(t, p.a, .9)), v = Math.round(k * n);
    g.save(); g.translate(W / 2, 860);
    for (let i = 0; i < n; i++) { const a = -Math.PI / 2 + i / n * 2 * Math.PI, on = i < v;
      g.strokeStyle = on ? (i === n - 1 ? ROUGE : OR) : 'rgba(239,230,210,.18)'; g.lineWidth = 34; g.lineCap = 'butt';
      g.beginPath(); g.arc(0, 0, 300, a + .04, a + 2 * Math.PI / n - .04); g.stroke(); }
    S.texte(String(v), 0, -30, { taille: 300, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 40 });
    S.texte('ANS', 0, 150, { taille: 90, coul: CREME, esp: 14 });
    g.restore();
    if (p.t) deux(p.t, 1360, 100);
  }

  // Einstein, rayé au feutre rouge ; p.raison : la croix s'efface, tampon « RAISON » en or
  function tort(p, t, l) {
    O.carte('einstein', W / 2, 800, 600, 780, -.03, 1.05 + l * .03, .5, .35, { lum: .95 });
    const tr = p.raison ? tps(p.raison) : 1e9, kx = eo(pr(t, p.a + .1, .35)) * (1 - pr(t, tr, .2));
    g.save(); g.strokeStyle = ROUGE; g.lineWidth = 26; g.lineCap = 'round'; g.globalAlpha = .92;
    [[[270, 470], [810, 1130]], [[810, 470], [270, 1130]]].forEach(([a, b], i) => { const k = cl(kx * 2 - i);
      if (k > 0) { g.beginPath(); g.moveTo(a[0], a[1]); g.lineTo(lerp(a[0], b[0], k), lerp(a[1], b[1], k)); g.stroke(); } });
    g.restore();
    if (t >= tr) O.tampon('RAISON', W / 2, 1000, pr(t, tr, .3), -.1, 150, OR);
    deux(p.t || 'EINSTEIN|A TORT ?', 1380, 100);
  }

  // un rayon de lumière fait de grains : « E = hν »
  function grains(p, t) {
    const lt = t - p.a;
    g.save(); g.fillStyle = 'rgba(217,180,90,.07)'; g.beginPath(); g.moveTo(-20, 700); g.lineTo(1100, 860); g.lineTo(1100, 1000); g.lineTo(-20, 840); g.fill(); g.restore();
    for (let i = 0; i < 26; i++) { const u = ((lt * .55 + i / 26) % 1), x = lerp(-40, 1120, u), y = lerp(770, 930, u) + (rnd(i) - .5) * 80;
      g.save(); g.fillStyle = OR; g.shadowColor = OR; g.shadowBlur = 24; g.beginPath(); g.arc(x, y, 13, 0, 7); g.fill(); g.restore(); }
    pop(pr(t, p.a + .3, .3), W / 2, 560, () => S.texte('E = h × ν', 0, 0, { taille: 120, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 10 }));
    deux(p.t || 'LA LUMIÈRE|EST FAITE DE GRAINS', 1300, 100);
    sous(p.sous || 'les futurs photons', 1460);
  }

  // plaque de métal éclairée ; p.mode 'rouge' (intense : rien ne sort) ou 'uv' (faible : des électrons sortent aussitôt)
  function metal(p, t) {
    const lt = t - p.a, uv = p.mode === 'uv', coul = uv ? VIOLET : ROUGE, n = uv ? 5 : 22;
    // plaque
    g.save(); g.fillStyle = '#5b5650'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(120, 1020, 840, 150, 12); g.fill(); g.stroke();
    S.texte('MÉTAL', W / 2, 1095, { taille: 54, coul: CREME, esp: 10 }); g.restore();
    for (let i = 0; i < n; i++) {
      const per = uv ? 1.1 : .9, u = ((lt + i * per / n) % per) / per, x0 = 160 + rnd(i * 3) * 760, x = lerp(x0 - 260, x0, u), y = lerp(330, 1015, u);
      g.save(); g.fillStyle = coul; g.shadowColor = coul; g.shadowBlur = 22; g.beginPath(); g.arc(x, y, uv ? 15 : 11, 0, 7); g.fill(); g.restore();
      // ultraviolet : à chaque impact, un électron part aussitôt (u = âge depuis l'impact précédent)
      if (uv && lt + i * per / n >= per) { const ex = x0 + u * 380 * (rnd(i + 7) - .3), ey = 1010 - u * 520;
        g.save(); g.fillStyle = '#7fd6ff'; g.shadowColor = '#7fd6ff'; g.shadowBlur = 20; g.globalAlpha = 1 - u * .6; g.beginPath(); g.arc(ex, ey, 12, 0, 7); g.fill();
        S.texte('e⁻', ex + 30, ey - 26, { taille: 30, coul: '#bfe9ff' }); g.restore(); }
    }
    petitTitre(uv ? 'ULTRAVIOLET TRÈS FAIBLE' : 'ROUGE TRÈS INTENSE', 300, uv ? VIOLET : ROUGE);
    if (!uv) pop(pr(t, p.a + .9, .3), W / 2, 760, () => S.texte('AUCUN ÉLECTRON', 0, 0, { taille: 96, coul: CREME, contour: NOIR, contourL: 12 }));
    else pop(pr(t, p.a + .2, .3), W / 2, 1300, () => S.texte('DES ÉLECTRONS SORTENT', 0, 0, { taille: 72, coul: '#7fd6ff', contour: NOIR, contourL: 10, max: 960 }));
    if (p.t) O.multi([[p.t, OR]], 1430, 110);
    if (p.pas && t >= tps(p.pas)) O.tampon('PAS L’INTENSITÉ', W / 2, 700, pr(t, tps(p.pas), .3), -.08, 92);
  }
  function petitTitre(s, y, c) { S.texte(s, W / 2, y, { taille: 44, coul: c, esp: 8, poids: 700, max: 960 }); }

  // la lumière, une onde (modèle qui triomphe depuis un siècle)
  function onde(p, t) {
    const lt = t - p.a;
    [[OR, 0, 1], ['rgba(239,230,210,.35)', 1.6, .6]].forEach(([c, ph, a]) => {
      g.save(); g.strokeStyle = c; g.globalAlpha = a; g.lineWidth = 12; g.shadowColor = c; g.shadowBlur = 20; g.beginPath();
      for (let x = -10; x <= W + 10; x += 6) { const y = 860 + Math.sin(x * .016 - lt * 6 + ph) * 150 * cl(pr(t, p.a, .4) * 1.2); x < 0 ? g.moveTo(x, y) : g.lineTo(x, y); }
      g.stroke(); g.restore(); });
    deux(p.t || 'LA LUMIÈRE|EST UNE ONDE', 1300, 110);
    sous(p.sous || 'le modèle qui triomphe depuis un siècle', 1460, 54);
  }

  // viseur sur Einstein
  function cible(p, t, l) {
    O.carte('einstein', W / 2, 800, 600, 780, .03, 1.1 + l * .05, .5, .3, { lum: .9 });
    const k = eo(pr(t, p.a, .5)), r = lerp(520, 230, k);
    g.save(); g.strokeStyle = ROUGE; g.lineWidth = 9; g.globalAlpha = .9;
    g.beginPath(); g.arc(W / 2, 700, r, 0, 7); g.stroke(); g.beginPath(); g.arc(W / 2, 700, r * .45, 0, 7); g.stroke();
    [[0, -1], [0, 1], [-1, 0], [1, 0]].forEach(([dx, dy]) => { g.beginPath(); g.moveTo(W / 2 + dx * r * .2, 700 + dy * r * .2); g.lineTo(W / 2 + dx * (r + 80), 700 + dy * (r + 80)); g.stroke(); });
    g.restore();
    deux(p.t || 'FAIRE TOMBER|EINSTEIN', 1360, 110);
  }

  // surface de métal qui se couvre d'oxyde ; p.faux : tampon « MESURES FAUSSÉES »
  function oxyde(p, t) {
    const k = eo(pr(t, p.a + .2, .9));
    g.save(); g.fillStyle = '#9a958e'; g.fillRect(90, 860, 900, 360);
    g.fillStyle = 'rgba(255,255,255,.25)'; for (let i = 0; i < 5; i++) g.fillRect(130 + i * 170, 900 + (i % 2) * 40, 120, 8);
    // croûte d'oxyde, irrégulière, qui épaissit
    g.fillStyle = '#4d4a3f'; g.beginPath(); g.moveTo(90, 860);
    for (let x = 90; x <= 990; x += 30) g.lineTo(x, 860 - k * (40 + rnd(x) * 45)); g.lineTo(990, 860); g.closePath(); g.fill();
    for (let i = 0; i < 40 * k; i++) { g.fillStyle = 'rgba(160,90,50,.6)'; g.beginPath(); g.arc(100 + rnd(i * 5) * 880, 860 - rnd(i * 7) * 70 * k, 6 + rnd(i) * 8, 0, 7); g.fill(); }
    g.restore();
    etiquette('MÉTAL', W / 2, 1080, CREME, 50);
    pop(pr(t, p.a + .5, .3), 760, 690, () => etiquette('OXYDE', 0, 0, ROUGE, 54));
    deux(p.t || 'UNE COUCHE|D’OXYDE', 1400, 100);
    if (p.faux && t >= tps(p.faux)) O.tampon('MESURES FAUSSÉES', W / 2, 520, pr(t, tps(p.faux), .3), -.08, 80);
  }

  // l'atelier dans le vide : tube de verre, roue de cylindres de métal, couteau mû par un électroaimant extérieur
  // p.etape 0 : le tube et le vide ; 1 : couteau et aimant ; 2 : gros plan, le couteau rabote le sodium
  function tube(p, t, l) {
    const lt = t - p.a, e = p.etape || 0;
    if (e < 2) {
      // tube
      g.save(); g.fillStyle = VERRE; g.strokeStyle = 'rgba(200,230,240,.75)'; g.lineWidth = 7;
      g.beginPath(); g.roundRect(110, 560, 860, 620, 160); g.fill(); g.stroke();
      g.strokeStyle = 'rgba(255,255,255,.35)'; g.lineWidth = 5; g.beginPath(); g.moveTo(230, 600); g.quadraticCurveTo(540, 580, 850, 600); g.stroke(); g.restore();
      // roue et trois cylindres (sodium, potassium, lithium)
      const ang = e === 0 ? lt * .8 : 0;
      g.save(); g.translate(400, 870); g.rotate(ang); g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(0, 0, 150, 0, 7); g.stroke();
      ['Na', 'K', 'Li'].forEach((s, i) => { const a = i * 2.094; g.save(); g.translate(Math.cos(a) * 110, Math.sin(a) * 110);
        g.fillStyle = '#b8b2a6'; g.beginPath(); g.arc(0, 0, 48, 0, 7); g.fill(); g.rotate(-ang); S.texte(s, 0, 2, { taille: 38, coul: NOIR }); g.restore(); });
      g.restore();
      if (e === 0) { // pompe : le vide
        const k = pr(t, p.a + .2, .6); for (let i = 0; i < 10; i++) { const u = ((lt * .9 + i / 10) % 1);
          g.save(); g.globalAlpha = (1 - u) * .8 * k; g.fillStyle = CREME; g.beginPath(); g.arc(lerp(700, 1060, u), 870 + Math.sin(i * 3 + u * 9) * 60, 7, 0, 7); g.fill(); g.restore(); }
        pop(pr(t, p.a + .4, .3), 790, 720, () => etiquette('VIDE', 0, 0, OR, 70));
        deux(p.t || 'UN ATELIER|DANS LE VIDE', 1390, 110);
      } else { // couteau à l'intérieur, électroaimant à l'extérieur, qui avancent ensemble
        const av = Math.sin(lt * 4) * .5 + .5, kx = lerp(700, 560, av);
        g.save(); g.fillStyle = CREME; g.beginPath(); g.moveTo(kx, 840); g.lineTo(kx + 130, 830); g.lineTo(kx + 130, 910); g.lineTo(kx, 900); g.closePath(); g.fill();
        g.fillStyle = '#8f8a82'; g.fillRect(kx + 130, 855, 150, 30); g.restore();
        g.save(); g.fillStyle = ROUGE; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.roundRect(kx + 170, 1200, 120, 90, 10); g.fill(); g.stroke();
        g.strokeStyle = OR; g.lineWidth = 4; for (let i = 0; i < 5; i++) { g.beginPath(); g.moveTo(kx + 180, 1212 + i * 16); g.lineTo(kx + 280, 1212 + i * 16); g.stroke(); }
        g.setLineDash([12, 12]); g.strokeStyle = 'rgba(200,55,45,.7)'; g.beginPath(); g.moveTo(kx + 230, 1195); g.lineTo(kx + 230, 900); g.stroke(); g.restore();
        etiquette('COUTEAU', kx + 60, 780, CREME, 40); etiquette('AIMANT', kx + 230, 1330, ROUGE, 40); etiquette('SODIUM', 400 + 110, 1010, OR, 36);
        S.texte('un couteau guidé de l’extérieur', W / 2, 470, { taille: 50, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 });
      }
    } else { // gros plan : copeaux de sodium, surface neuve et brillante
      const av = (lt * 1.6) % 1;
      g.save(); g.fillStyle = '#c9c4b8'; g.beginPath(); g.arc(380, 900, 300, 0, 7); g.fill();
      const net = cl(lt / 1.6); g.save(); g.beginPath(); g.arc(380, 900, 300, 0, 7); g.clip();
      g.fillStyle = `rgba(250,250,245,${.2 + .6 * net})`; g.fillRect(80, 600, 600 * net, 600); g.restore();
      g.fillStyle = 'rgba(255,255,255,.6)'; g.fillRect(200, 760, 260 * net, 10);
      g.restore();
      // lame
      const lx = lerp(160, 620, av);
      g.save(); g.fillStyle = CREME; g.strokeStyle = NOIR; g.lineWidth = 4; g.beginPath(); g.moveTo(lx, 560); g.lineTo(lx + 40, 560); g.lineTo(lx + 200, 1250); g.lineTo(lx + 120, 1250); g.closePath(); g.fill(); g.stroke(); g.restore();
      for (let i = 0; i < 8; i++) { const u = ((lt * 1.6 + i / 8) % 1); g.save(); g.translate(lx + 60 + u * 420, 700 + i * 50 - u * 200); g.rotate(u * 6 + i);
        g.strokeStyle = '#d8d3c8'; g.lineWidth = 8; g.globalAlpha = 1 - u; g.beginPath(); g.arc(0, 0, 22, 0, 4.5); g.stroke(); g.restore(); }
      etiquette('SODIUM', 380, 1240, OR, 54);
      deux(p.t || 'RABOTÉ|SOUS VIDE', 1420, 110);
    }
  }

  // mesures fréquence après fréquence : la couleur de la lampe change, le compteur d'énergie aussi
  function mesure(p, t) {
    const lt = t - p.a, COUL = ['#ffd84a', '#5fd36b', '#4f8dff', VIOLET, '#c79bff'], NOMS = ['JAUNE', 'VERT', 'BLEU', 'VIOLET', 'UV'];
    const i = Math.min(4, Math.floor(lt / .55)), c = COUL[i];
    g.save(); g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(80, 560, 200, 160, 20); g.fill(); g.stroke();
    g.fillStyle = c; g.shadowColor = c; g.shadowBlur = 40; g.beginPath(); g.arc(280, 640, 34, 0, 7); g.fill(); g.restore();
    g.save(); g.globalAlpha = .35; g.fillStyle = c; g.beginPath(); g.moveTo(300, 610); g.lineTo(760, 860); g.lineTo(760, 960); g.lineTo(300, 670); g.fill(); g.restore();
    g.save(); g.fillStyle = '#c9c4b8'; g.beginPath(); g.arc(800, 920, 80, 0, 7); g.fill(); g.restore();
    etiquette('SODIUM', 800, 1040, OR, 36);
    etiquette(NOMS[i], 180, 790, c, 44);
    // énergie des électrons mesurée : barre qui grandit avec la fréquence
    g.save(); g.fillStyle = 'rgba(239,230,210,.1)'; g.fillRect(140, 1130, 800, 60); g.fillStyle = OR; g.fillRect(140, 1130, 160 * (i + 1) * eo(pr(lt % .55, 0, .3)), 60); g.restore();
    S.texte('ÉNERGIE DES ÉLECTRONS', W / 2, 1090, { taille: 36, coul: GRIS, esp: 6 });
    deux(p.t || 'FRÉQUENCE|APRÈS FRÉQUENCE', 1380, 100);
  }

  // le graphique Ec = f(ν) : p.etape 1 points ; 2 droite + tampon ; 3 pente = h
  function droite(p, t) {
    const e = p.etape || 1, X0 = 170, Y0 = 1150, LX = 820, LY = 640;
    const px = u => X0 + u * LX, py = v => Y0 - v * LY, f = u => 1.05 * (u - .3);
    g.save(); g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(X0, Y0 + 20); g.lineTo(X0, Y0 - LY - 30); g.stroke(); g.beginPath(); g.moveTo(X0 - 20, Y0); g.lineTo(X0 + LX + 30, Y0); g.stroke(); g.restore();
    S.texte('fréquence ν', X0 + LX - 80, Y0 + 55, { taille: 40, it: true, police: 'Spectral', poids: 400, coul: CREME });
    S.texte('énergie des électrons', X0 + 20, Y0 - LY - 60, { taille: 40, it: true, police: 'Spectral', poids: 400, coul: CREME, align: 'left' });
    const U = [.38, .48, .58, .68, .8, .92];
    const kl = e === 1 ? (p.ligne ? eo(pr(t, tps(p.ligne), .5)) : 0) : 1;
    if (kl > 0) { g.save(); g.strokeStyle = OR; g.lineWidth = 10; g.shadowColor = OR; g.shadowBlur = 18; g.beginPath(); g.moveTo(px(.3), py(0)); g.lineTo(px(lerp(.3, 1, kl)), py(f(lerp(.3, 1, kl)))); g.stroke(); g.restore(); }
    U.forEach((u, i) => { const k = e === 1 ? pr(t, p.a + .15 + i * .2, .2) : 1, v = f(u) + (e === 1 && kl < 1 ? (rnd(i) - .5) * .05 * (1 - kl) : 0);
      pop(k, px(u), py(v), () => { g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 17, 0, 7); g.fill(); g.strokeStyle = CREME; g.lineWidth = 4; g.stroke(); }); });
    if (e === 1) S.texte('MESURES DE 1916', W / 2, 330, { taille: 44, coul: OR, esp: 8, poids: 700 });
    if (e === 2) {
      S.texte('Ec = h × ν − Φ', W / 2, 360, { taille: 90, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 10 });
      O.tampon('EINSTEIN AVAIT RAISON', W / 2, 1380, pr(t, p.a + .05, .3), -.07, 74);
    }
    if (e === 3) {
      const k = eo(pr(t, p.a + .15, .4)), u1 = .55, u2 = .85;
      g.save(); g.globalAlpha = k; g.strokeStyle = CREME; g.lineWidth = 6; g.setLineDash([16, 12]);
      g.beginPath(); g.moveTo(px(u1), py(f(u1))); g.lineTo(px(u2), py(f(u1))); g.lineTo(px(u2), py(f(u2))); g.stroke(); g.restore();
      pop(pr(t, p.a + .4, .3), px(u2) + 20, py((f(u1) + f(u2)) / 2) + 150, () => S.texte('PENTE = h', 0, 0, { taille: 76, coul: OR, contour: NOIR, contourL: 10 }));
      if (p.h && t >= tps(p.h)) pop(pr(t, tps(p.h), .3), W / 2, 1380, () => {
        S.texte('LA CONSTANTE DE PLANCK', 0, -70, { taille: 50, coul: CREME, esp: 4 });
        S.texte('h ≈ 6,6 × 10⁻³⁴ J·s', 0, 30, { taille: 92, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 10 }); });
    }
  }

  // l'article de 1916 : la phrase sur l'hypothèse « téméraire »
  function article(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1450, 880, k)); g.rotate(.025);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#e9dfc8'; g.fillRect(-420, -520, 840, 1040); g.shadowColor = 'transparent';
    S.texte('THE PHYSICAL REVIEW · 1916', 0, -450, { taille: 34, coul: GRIS, esp: 4 });
    S.texte('A Direct Photoelectric', 0, -370, { taille: 52, police: 'Spectral', poids: 600, coul: NOIR });
    S.texte('Determination of Planck’s « h »', 0, -305, { taille: 52, police: 'Spectral', poids: 600, coul: NOIR, max: 760 });
    S.texte('R. A. Millikan', 0, -235, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: NOIR });
    for (let i = 0; i < 12; i++) if (i !== 4 && i !== 5) { g.fillStyle = 'rgba(0,0,0,.14)'; g.fillRect(-360, -160 + i * 52, 720 - (i % 4 === 3 ? 200 : 0), 8); }
    S.texte('« the bold, not to say', 0, 52, { taille: 46, police: 'Spectral', it: true, poids: 600, coul: NOIR });
    S.texte('the reckless, hypothesis »', 0, 104, { taille: 46, police: 'Spectral', it: true, poids: 600, coul: NOIR });
    const kc = pr(t, p.a + .35, .5); g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.ellipse(0, 80, 400, 95, -.03, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    if (p.tampon && t >= tps(p.tampon)) O.tampon('TÉMÉRAIRE', W / 2, 1430, pr(t, tps(p.tampon), .3), -.1, 150);
    else S.texte('« audacieuse, pour ne pas dire téméraire »', W / 2, 1480, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 980 });
  }

  // médaille Nobel avec le portrait du lauréat
  function nobel(p, t, l) {
    O.carte(p.img, 300, 760, 420, 560, -.05, 1.05 + l * .03, .5, .3, { lum: .95 });
    const k = back(pr(t, p.a + .15, .35));
    g.save(); g.translate(760, 760); g.scale(k, k);
    const gr = g.createRadialGradient(-60, -60, 20, 0, 0, 230); gr.addColorStop(0, '#f6dc8c'); gr.addColorStop(1, '#a8812d');
    g.fillStyle = gr; g.shadowColor = 'rgba(217,180,90,.6)'; g.shadowBlur = 50; g.beginPath(); g.arc(0, 0, 220, 0, 7); g.fill(); g.shadowBlur = 0;
    g.strokeStyle = '#7a5c1c'; g.lineWidth = 8; g.beginPath(); g.arc(0, 0, 195, 0, 7); g.stroke();
    S.texte('PRIX NOBEL', 0, -60, { taille: 46, coul: '#4a3610', esp: 4 });
    S.texte(p.an, 0, 30, { taille: 110, police: 'Spectral', poids: 600, coul: '#3a2a0c' });
    S.texte('PHYSIQUE', 0, 115, { taille: 34, coul: '#4a3610', esp: 6 });
    g.restore();
    O.multi([[p.t, OR]], 1220, 110);
    if (p.sous) { const ks = eo(pr(t, p.asous ? tps(p.asous) : p.a + .4, .3)); g.save(); g.globalAlpha = ks; sous(p.sous, 1350, 60); g.restore(); }
  }

  // copie du bac de physique-chimie
  function sujetpc(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 880, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-380, -480, 760, 960); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
    S.texte('PHYSIQUE-CHIMIE', 0, -315, { taille: 40, coul: GRIS, esp: 8, poids: 600 });
    g.fillStyle = NOIR; g.fillRect(-300, -260, 600, 3);
    S.texte(p.ex || 'Exercice 1 · L’effet photoélectrique', -300, -190, { taille: 36, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400, max: 600 });
    (p.sujet || ['Établir la relation', 'd’Einstein']).forEach((s, i) => S.texte(s, 0, -90 + i * 86, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, max: 680 }));
    if (p.formule) S.texte(p.formule, 0, 130, { taille: 62, police: 'Spectral', poids: 600, coul: ROUGE, max: 680 });
    for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-300, 240 + i * 50, 600 - (i === 3 ? 250 : 0), 6); }
    const kc = pr(t, p.a + .35, .5); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(0, -48, 360, 120, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['QUESTION DE ', CREME], ['BAC', ROUGE]], 1560, 110);
  }

  return { annees, tort, grains, metal, onde, cible, oxyde, tube, mesure, droite, article, nobel, sujetpc };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'annees') for (let k = 0; k < (p.n || 10); k++) L.push([p.a + .9 * (1 - Math.pow(1 - (k + 1) / (p.n || 10), 1 / 3)), 'tic', .45]);
  if (p.type === 'tort') { L.push([p.a + .1, 'stylo', .6]); if (p.raison) L.push([tps(p.raison) + .05, 'tampon', .9]); }
  if (p.type === 'grains') L.push([p.a, 'whoosh', .5]);
  if (p.type === 'metal') { L.push([p.a, p.mode === 'uv' ? 'pop' : 'souffle', .5]); if (p.pas) L.push([tps(p.pas) + .05, 'tampon', .9]); }
  if (p.type === 'onde') L.push([p.a, 'souffle', .5]);
  if (p.type === 'cible') L.push([p.a, 'lame', .5]);
  if (p.type === 'oxyde') { L.push([p.a + .2, 'frotte', .5]); if (p.faux) L.push([tps(p.faux) + .05, 'tampon', .9]); }
  if (p.type === 'tube') L.push([p.a, p.etape === 0 ? 'aspire' : p.etape === 1 ? 'clic' : 'frotte', .5]);
  if (p.type === 'mesure') for (let k = 0; k < 5; k++) L.push([p.a + k * .55, 'blip', .35]);
  if (p.type === 'droite' && (p.etape || 1) === 1) for (let k = 0; k < 6; k++) L.push([p.a + .15 + k * .2, 'pop', .35]);
  if (p.type === 'droite' && p.etape === 2) L.push([p.a + .05, 'tampon', 1]);
  if (p.type === 'droite' && p.etape === 3 && p.h) L.push([tps(p.h), 'valide', .5]);
  if (p.type === 'article') { L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .5]); if (p.tampon) L.push([tps(p.tampon) + .05, 'tampon', 1]); }
  if (p.type === 'nobel') L.push([p.a + .15, 'gong', .45]);
  if (p.type === 'sujetpc') L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .6]);
};
