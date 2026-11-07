// Plans propres au short Stockdale, dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
window.SANS_ST_A = ['murmure', 'cellule', 'jours', 'colonnes', 'lieu', 'citadelle', 'flou', 'medaille'];
window.PROPRES_A = ['avion', 'ejection', 'chute', 'murmure', 'mondes', 'lieu', 'cellule', 'jours', 'tetelivre', 'colonnes',
  'rasoir', 'camera', 'crane', 'tabouret', 'flou', 'medaille', 'citadelle'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const BOIS = '#2a241d', SOMBRE = '#1b1712';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, f) => { const s = back(k); g.save(); g.globalAlpha = cl(k * 3); f(s); g.restore(); };
  const sous = (s, y, taille = 62) => S.texte(s, W / 2, y, { taille, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 8, max: 960 });

  // ---------- dessins
  // avion de chasse de profil (nez à droite), en feu ; (x, y) = centre, k = échelle
  function jet(x, y, k, rot, t, feu = 1) {
    g.save(); g.translate(x, y); g.rotate(rot); g.scale(k, k);
    // flammes (derrière l'avion)
    if (feu) for (let i = 0; i < 7; i++) {
      const f = Math.floor(t * 24), L = 70 + rnd(i * 5 + f) * 110, h = 14 + rnd(i * 3 + f + 7) * 18;
      const [ox, oy] = i < 4 ? [-175, 0] : [-50, 34];
      g.save(); g.shadowColor = ROUGE; g.shadowBlur = 30;
      g.fillStyle = i % 3 === 0 ? ROUGE : i % 3 === 1 ? OR : '#ffd98a';
      g.beginPath(); g.moveTo(ox, oy - h); g.quadraticCurveTo(ox - L * .6, oy - h * 1.6 - i * 3, ox - L, oy - 10 - i * 4);
      g.quadraticCurveTo(ox - L * .5, oy + h * .4, ox, oy + h); g.closePath(); g.fill(); g.restore();
    }
    g.fillStyle = BOIS; g.strokeStyle = CREME; g.lineWidth = 5; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(-120, -10); g.lineTo(-170, -80); g.lineTo(-195, -80); g.lineTo(-172, -8); g.closePath(); g.fill(); g.stroke();   // dérive
    g.beginPath(); g.moveTo(-172, -9); g.lineTo(120, -15); g.quadraticCurveTo(195, -8, 205, 0); g.quadraticCurveTo(195, 8, 120, 14); g.lineTo(-172, 12); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(40, 6); g.lineTo(-95, 72); g.lineTo(-125, 72); g.lineTo(-60, 8); g.closePath(); g.fill(); g.stroke();      // aile
    g.fillStyle = 'rgba(217,180,90,.55)'; g.beginPath(); g.ellipse(80, -14, 42, 15, 0, Math.PI, 2 * Math.PI); g.fill(); g.stroke();      // verrière
    g.restore();
  }
  function fumee(x, y, rot, t, n = 26) {
    for (let i = n; i >= 1; i--) {
      const d = i * 30, xx = x - Math.cos(rot) * d + Math.sin(t * 2 + i) * 6, yy = y - Math.sin(rot) * d - i * 4;
      g.fillStyle = `rgba(120,110,100,${.4 * (1 - i / n)})`; g.beginPath(); g.arc(xx, yy, 22 + i * 3.6, 0, 7); g.fill();
    }
  }
  function lueurBas(a = .18) {
    const v = g.createLinearGradient(0, 1000, 0, H); v.addColorStop(0, 'rgba(200,55,45,0)'); v.addColorStop(1, `rgba(200,55,45,${a})`);
    g.fillStyle = v; g.fillRect(0, 0, W, H);
  }
  // parachute et pilote ; (x, y) = centre de la voile
  function parachute(x, y, rot) {
    g.save(); g.translate(x, y); g.rotate(rot);
    const voile = new Path2D(); voile.moveTo(-260, 0); voile.bezierCurveTo(-260, -330, 260, -330, 260, 0);
    for (let i = 0; i < 6; i++) voile.quadraticCurveTo(260 - i * 86.7 - 43, 28, 260 - (i + 1) * 86.7, 0);
    g.save(); g.clip(voile); g.fillStyle = CREME; g.fillRect(-270, -300, 540, 340);
    g.fillStyle = ROUGE; for (let i = 0; i < 6; i += 2) g.fillRect(-260 + i * 86.7, -300, 86.7, 340); g.restore();
    g.strokeStyle = NOIR; g.lineWidth = 5; g.stroke(voile);
    g.strokeStyle = 'rgba(239,230,210,.8)'; g.lineWidth = 3;
    for (let i = 0; i <= 6; i++) { g.beginPath(); g.moveTo(-260 + i * 86.7, 4); g.lineTo(0, 330); g.stroke(); }
    g.strokeStyle = CREME; g.lineWidth = 8; g.lineCap = 'round';
    g.fillStyle = SOMBRE; g.beginPath(); g.arc(0, 352, 24, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(-26, 300); g.lineTo(0, 390); g.lineTo(26, 300); g.moveTo(0, 376); g.lineTo(0, 450); g.lineTo(-22, 530); g.moveTo(0, 450); g.lineTo(24, 528); g.stroke();
    g.restore();
  }
  function barreaux(a = 1) {
    g.save(); g.globalAlpha = a;
    for (let x = 60; x < W; x += 120) {
      const v = g.createLinearGradient(x - 14, 0, x + 14, 0); v.addColorStop(0, '#2b2621'); v.addColorStop(.5, '#6a6258'); v.addColorStop(1, '#2b2621');
      g.fillStyle = v; g.fillRect(x - 14, 260, 28, 1440);
    }
    g.fillStyle = '#3b352e'; g.fillRect(0, 400, W, 26); g.fillRect(0, 1560, W, 26);
    g.restore();
  }

  // ---------- plans
  // l'avion en feu (début, et boucle de fin avec p.bis au repère p.abis)
  function avion(p, t, l) {
    lueurBas(.22);
    const rot = .2, x = 330 + l * 80 + (rnd(t * 50) - .5) * 8, y = 720 + l * 30 + (rnd(t * 31) - .5) * 8;
    fumee(x - 180, y - 30, rot, t); jet(x, y, 2, rot, t);
    const bis = p.bis && t >= tps(p.abis);
    if (bis) pop(pr(t, tps(p.abis), .25), s => { g.translate(W / 2, 1380); g.scale(lerp(1.4, 1, s), lerp(1.4, 1, s)); g.translate(-W / 2, -1380); deux(p.bis, 1380, 120); });
    else deux(p.t, 1380, 120);
  }
  // l'éjection : le siège jaillit du cockpit
  function ejection(p, t, l) {
    lueurBas(.3);
    const x = 470 + l * 140, y = 1180;
    fumee(x - 360, y - 60, .18, t, 18); jet(x, y, 1.7, .18, t);
    const k = eo(pr(t, p.a, .6)), sx = x + 120, sy = y - 60 - k * 700 - l * 60;
    // traînée et flamme sous le siège
    g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 10; g.beginPath(); g.moveTo(x + 120, y - 50); g.lineTo(sx, sy + 70); g.stroke();
    g.save(); g.fillStyle = OR; g.shadowColor = OR; g.shadowBlur = 40; const fl = 60 + rnd(Math.floor(t * 30)) * 50;
    g.beginPath(); g.moveTo(sx - 16, sy + 50); g.lineTo(sx, sy + 50 + fl); g.lineTo(sx + 16, sy + 50); g.fill(); g.restore();
    // siège et pilote
    g.save(); g.translate(sx, sy); g.fillStyle = BOIS; g.strokeStyle = CREME; g.lineWidth = 5;
    g.beginPath(); g.roundRect(-34, -80, 20, 125, 6); g.fill(); g.stroke(); g.beginPath(); g.roundRect(-34, 30, 78, 18, 6); g.fill(); g.stroke();
    g.fillStyle = CREME; g.beginPath(); g.arc(0, -66, 20, 0, 7); g.fill();
    g.fillStyle = OR; g.fillRect(-12, -44, 26, 72); g.restore();
    // verrière arrachée
    g.save(); g.translate(x + 140 + k * 260, y - 80 - k * 380); g.rotate(k * 5); g.fillStyle = 'rgba(217,180,90,.7)';
    g.beginPath(); g.ellipse(0, 0, 70, 24, 0, Math.PI, 2 * Math.PI); g.fill(); g.restore();
    const kf = pr(t, p.a, .2); if (kf < 1) { g.fillStyle = `rgba(255,246,216,${(1 - kf) * .8})`; g.beginPath(); g.arc(x + 120, y - 50, 80 + kf * 500, 0, 7); g.fill(); }
    // traits de vitesse
    for (let i = 0; i < 10; i++) { const xx = 120 + rnd(i) * 840, yy = ((rnd(i + 3) * H + l * 2400) % H); g.fillStyle = 'rgba(239,230,210,.18)'; g.fillRect(xx, yy, 4, 160); }
    deux(p.t, 1520, 130);
  }
  // descente en parachute ; p.chrono : compte à rebours ; p.village : toits au sol
  function chute(p, t, l) {
    const sol = lerp(1640, 1460, eo(pr(t, p.a, 3)));
    g.fillStyle = '#17120d'; g.fillRect(0, sol, W, H - sol);
    g.strokeStyle = 'rgba(217,180,90,.5)'; g.lineWidth = 4; g.beginPath(); g.moveTo(0, sol); g.lineTo(W, sol); g.stroke();
    if (p.village) for (let i = 0; i < 8; i++) {
      const x = 30 + i * 140 + rnd(i) * 30, h = 50 + rnd(i + 4) * 40, w = 90;
      g.fillStyle = BOIS; g.strokeStyle = CREME; g.lineWidth = 3;
      g.beginPath(); g.rect(x, sol - h, w, h); g.fill(); g.stroke();
      g.beginPath(); g.moveTo(x - 14, sol - h); g.lineTo(x + w / 2, sol - h - 46); g.lineTo(x + w + 14, sol - h); g.closePath(); g.fill(); g.stroke();
    }
    const sw = Math.sin(l * 1.7);
    parachute(540 + sw * 34, 640 + l * 30, sw * .07);
    if (p.chrono) {
      const n = Math.max(0, p.chrono - Math.floor(l));
      S.texte('0:' + String(n).padStart(2, '0'), W / 2, 330, { taille: 120, police: 'JetBrains Mono', poids: 500, coul: ROUGE, ombre: 'rgba(200,55,45,.6)', flou: 30 });
    }
    O.multi([[p.t, OR]], 1300, 130);
    if (p.sous) sous(p.sous, 1410);
  }
  // la phrase qu'il se murmure, tapée
  function murmure(p, t, l) {
    S.texte('9 SEPTEMBRE 1965 · EN PARACHUTE', W / 2, 680, { taille: 34, coul: GRIS, esp: 6 });
    const txt = p.t, plat = txt.replace(/\|/g, ''), n = Math.floor(cl((t - p.a) / (p.duree || 1)) * plat.length);
    let c = 0; txt.split('|').forEach((s, i, L) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte((i === 0 ? '« ' : '') + vis + (i === L.length - 1 && n >= plat.length ? ' »' : ''), W / 2, 880 + i * 130,
        { taille: 100, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 980 }); });
    const k = eo(pr(t, p.a + (p.duree || 1), .4)); g.save(); g.globalAlpha = k;
    S.texte('— James Stockdale', W / 2, 1200, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: OR }); g.restore();
  }
  // « le monde de la technologie » : cadrans, barrés au repère p.barre
  function mondes(p, t, l) {
    O.petitTitre('JE QUITTE…', 520);
    const tb = tps(p.barre), fini = t >= tb;
    g.save(); g.globalAlpha = fini ? lerp(1, .3, pr(t, tb, .4)) : 1;
    [270, 540, 810].forEach((cx, i) => {
      const cy = 820, r = 115;
      g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(cx, cy, r, 0, 7); g.fill(); g.stroke();
      for (let j = 0; j < 12; j++) { const a = Math.PI * .75 + j / 11 * Math.PI * 1.5; g.lineWidth = 3; g.beginPath();
        g.moveTo(cx + Math.cos(a) * r * .78, cy + Math.sin(a) * r * .78); g.lineTo(cx + Math.cos(a) * r * .9, cy + Math.sin(a) * r * .9); g.stroke(); }
      const a = Math.PI * .75 + (.5 + .45 * Math.sin(t * (2 + i) + i)) * Math.PI * 1.5;
      g.strokeStyle = i === 1 ? ROUGE : OR; g.lineWidth = 7; g.beginPath(); g.moveTo(cx, cy); g.lineTo(cx + Math.cos(a) * r * .75, cy + Math.sin(a) * r * .75); g.stroke();
    });
    g.restore();
    O.multi([['LE MONDE DE', CREME]], 1110, 105);
    O.multi([['LA TECHNOLOGIE', OR]], 1250, 125);
    if (fini) O.barreRouge(1180, eo(pr(t, tb, .3)), 26, -.05);
  }
  // un lieu : photo en paysage, nom, surnom au repère p.surnom
  function lieu(p, t, l) {
    O.petitTitre('— HANOÏ —', 400);
    const k = eo(pr(t, p.a, .35));
    O.carte(p.img, W / 2 + lerp(260, 0, k), 820, 940, 620, lerp(.1, -.025, k), 1.05 + l * .04, .55, .4, { lum: .95 });
    O.multi([[p.t, OR]], 1300, 180);
    if (p.surnom && t >= tps(p.surnom)) pop(pr(t, tps(p.surnom), .3), s => { g.translate(W / 2, 1440); g.scale(s, s);
      S.texte(p.sous, 0, 0, { taille: 90, police: 'Spectral', it: true, poids: 500, coul: CREME, contour: NOIR, contourL: 10 }); });
  }
  // barreaux et mots empilés
  function cellule(p, t, l) {
    barreaux(.9);
    p.mots.forEach(([a, s], i) => {
      const ta = tps(a); if (t < ta) return;
      const y = 700 + i * 240, k = pr(t, ta, .25);
      g.fillStyle = 'rgba(13,11,9,.82)'; g.fillRect(0, y - 85, W, 170);
      pop(k, sc => { g.translate(W / 2, y); g.scale(lerp(1.8, 1, sc), lerp(1.8, 1, sc)); g.translate(-W / 2, -y); O.multi([[s, i === 2 ? ROUGE : CREME]], y, 130); });
    });
  }
  // « il avait dit 5 ans » : barré, puis les jours s'accumulent (bâtons) jusqu'à 2 713
  function jours(p, t, l) {
    O.petitTitre('IL AVAIT DIT', 470);
    S.texte('5 ANS', W / 2, 610, { taille: 170, coul: CREME, contour: NOIR, contourL: 12 });
    const tc = tps(p.court), kc = pr(t, p.a + .25, Math.max(.5, p.b - p.a - .4)), f = 1 - (1 - kc) * (1 - kc), ng = Math.round(f * 60);
    if (t >= tc) O.barreRouge(610, eo(pr(t, tc, .25)), 26, -.05);
    g.strokeStyle = CREME; g.lineWidth = 6; g.lineCap = 'round';
    for (let i = 0; i < ng; i++) {
      const x = 110 + (i % 10) * 88, y = 790 + Math.floor(i / 10) * 95;
      for (let j = 0; j < 4; j++) { g.beginPath(); g.moveTo(x + j * 14, y); g.lineTo(x + j * 14 + 2, y + 66); g.stroke(); }
      g.strokeStyle = ROUGE; g.beginPath(); g.moveTo(x - 8, y + 54); g.lineTo(x + 52, y + 10); g.stroke(); g.strokeStyle = CREME;
    }
    const n = String(Math.round(f * 2713)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    S.texte(n + ' JOURS', W / 2, 1450, { taille: 130, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 });
  }
  // un livre s'allume dans sa tête (p.livre)
  function tetelivre(p, t, l) {
    S.d.tete(560, 800, 330, { trait: CREME, fond: SOMBRE, ep: 9 });
    const tl = tps(p.livre);
    if (t >= tl) {
      const k = pr(t, tl, .35), r = 200 + Math.sin(t * 4) * 20;
      const v = g.createRadialGradient(600, 690, 10, 600, 690, r); v.addColorStop(0, 'rgba(217,180,90,.55)'); v.addColorStop(1, 'rgba(217,180,90,0)');
      g.fillStyle = v; g.beginPath(); g.arc(600, 690, r, 0, 7); g.fill();
      pop(k, s => { g.translate(600, 690); g.scale(s, s); g.fillStyle = CREME; g.strokeStyle = OR; g.lineWidth = 5; g.shadowColor = OR; g.shadowBlur = 40;
        g.beginPath(); g.moveTo(0, -50); g.quadraticCurveTo(-50, -66, -100, -54); g.lineTo(-100, 50); g.quadraticCurveTo(-50, 38, 0, 54); g.closePath(); g.fill(); g.stroke();
        g.beginPath(); g.moveTo(0, -50); g.quadraticCurveTo(50, -66, 100, -54); g.lineTo(100, 50); g.quadraticCurveTo(50, 38, 0, 54); g.closePath(); g.fill(); g.stroke();
        g.shadowBlur = 0; g.fillStyle = 'rgba(13,11,9,.5)'; for (let i = 0; i < 4; i++) { g.fillRect(-84, -30 + i * 20, 66, 5); g.fillRect(18, -30 + i * 20, 66, 5); } });
    }
    O.multi(p.t.split(' ').map((m, i, L) => [m + (i < L.length - 1 ? ' ' : ''), i === L.length - 1 ? OR : CREME]), 1380, 130);
  }
  // les deux colonnes d'Épictète, remplies au fil de s8 et s9
  function colonnes(p, t, l) {
    const ap = a => tps(a), vu = a => t >= ap(a), kk = a => pr(t, ap(a), .3);
    O.petitTitre('ÉPICTÈTE · MANUEL, I', 430);
    g.strokeStyle = 'rgba(239,230,210,.45)'; g.lineWidth = 4; g.beginPath(); g.moveTo(540, 520); g.lineTo(540, 1420); g.stroke();
    const fin = vu(['s9', 'oui']), kf = fin ? eo(kk(['s9', 'oui'])) : 0;
    if (fin) { g.save(); g.strokeStyle = OR; g.lineWidth = 8; g.shadowColor = OR; g.shadowBlur = 40 * kf; g.globalAlpha = kf;
      g.beginPath(); g.roundRect(50, 500, 460, 760, 30); g.stroke(); g.restore(); }
    const bloc = (a, x, lignes, y0, coul, taille, dim) => { if (!vu(a)) return; pop(kk(a), s => {
      g.translate(x, y0); g.scale(lerp(.6, 1, s), lerp(.6, 1, s)); if (dim) g.globalAlpha *= lerp(1, .4, kf);
      lignes.forEach((m, i) => S.texte(m, 0, i * taille * 1.12, { taille, coul, contour: NOIR, contourL: 8, max: 440 })); }); };
    bloc(['s8', 0], 280, ['CE QUI', 'DÉPEND', 'DE NOUS'], 580, OR, 62);
    bloc(['s8', 'et'], 800, ['CE QUI NE', 'DÉPEND PAS', 'DE NOUS'], 580, CREME, 62, true);
    bloc(['s9', 'corps'], 800, ['SON CORPS'], 930, CREME, 60, true);
    bloc(['s9', 'douleur'], 800, ['LA DOULEUR'], 1090, CREME, 60, true);
    bloc(['s9', 'accepte'], 280, ['CE QU’IL', 'ACCEPTE'], 900, OR, 60);
    bloc(['s9', 'refuse'], 280, ['CE QU’IL', 'REFUSE'], 1090, OR, 60);
  }
  // rasoir ouvert qui glisse
  function rasoir(p, t, l) {
    const k = eo(pr(t, p.a, .45));
    g.save(); g.translate(lerp(1300, 600, k), 820); g.rotate(lerp(.7, -.22, k));
    g.fillStyle = '#3a2f25'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(-360, -22, 340, 44, 22); g.fill(); g.stroke();
    const lame = new Path2D(); lame.moveTo(0, -46); lame.lineTo(330, -46); lame.quadraticCurveTo(370, -26, 352, 34); lame.lineTo(16, 34); lame.closePath();
    g.fillStyle = '#cfc8bb'; g.fill(lame); g.stroke(lame);
    const kg = pr(t, p.a + .5, .5); if (kg > 0 && kg < 1) { g.save(); g.clip(lame); const x = lerp(-60, 420, kg), v = g.createLinearGradient(x - 50, 0, x + 50, 0);
      v.addColorStop(0, 'rgba(255,255,255,0)'); v.addColorStop(.5, 'rgba(255,255,255,.9)'); v.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = v; g.fillRect(-60, -60, 480, 120); g.restore(); }
    g.fillStyle = OR; g.beginPath(); g.arc(0, 0, 14, 0, 7); g.fill();
    g.restore();
    O.multi(p.t.split(' ').map((m, i, L) => [m + (i < L.length - 1 ? ' ' : ''), i === L.length - 1 ? OR : CREME]), 1360, 150);
  }
  // caméra de propagande ; p.prop : tampon « PROPAGANDE » ; p.coupe : la caméra s'arrête, croix rouge
  function camera(p, t, l) {
    g.save(); g.translate(560, 840);
    const ang = p.coupe ? 0 : l * 5;
    [[-120, -210], [70, -210]].forEach(([x, y]) => { g.fillStyle = BOIS; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(x, y, 90, 0, 7); g.fill(); g.stroke();
      for (let i = 0; i < 3; i++) { const a = ang + i * 2.09; g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * 80, y + Math.sin(a) * 80); g.stroke(); } });
    g.fillStyle = SOMBRE; g.beginPath(); g.roundRect(-230, -115, 360, 230, 16); g.fill(); g.stroke();
    g.beginPath(); g.rect(130, -55, 70, 110); g.fill(); g.stroke(); g.beginPath(); g.arc(250, 0, 62, 0, 7); g.fill(); g.stroke();
    g.fillStyle = 'rgba(217,180,90,.35)'; g.beginPath(); g.arc(250, 0, 38, 0, 7); g.fill();
    const rec = !p.coupe && Math.floor(t * 2.5) % 2 === 0;
    g.fillStyle = rec ? ROUGE : '#4a4038'; if (rec) { g.shadowColor = ROUGE; g.shadowBlur = 30; } g.beginPath(); g.arc(-180, -70, 16, 0, 7); g.fill(); g.shadowBlur = 0;
    S.texte('REC', -120, -70, { taille: 34, police: 'JetBrains Mono', poids: 500, coul: rec ? ROUGE : GRIS });
    g.restore();
    if (p.coupe) { const k = eo(pr(t, p.a + .1, .3)); g.save(); g.strokeStyle = ROUGE; g.lineWidth = 34; g.lineCap = 'round';
      g.beginPath(); g.moveTo(240, 560); g.lineTo(lerp(240, 860, k), lerp(560, 1060, k)); g.stroke();
      const k2 = eo(pr(t, p.a + .3, .3)); if (k2 > 0) { g.beginPath(); g.moveTo(860, 560); g.lineTo(lerp(860, 240, k2), lerp(560, 1060, k2)); g.stroke(); } g.restore(); }
    if (p.prop && t >= tps(p.prop)) O.tampon('PROPAGANDE', W / 2, 1150, pr(t, tps(p.prop), .3), -.1, 100);
    deux(p.t, 1390, 110);
  }
  // tête de face : une bande se rase au milieu du crâne
  function crane(p, t, l) {
    const cx = 540, cy = 830, k = eo(pr(t, p.a, 2.4));
    g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 8;
    g.beginPath(); g.rect(cx - 70, cy + 230, 140, 200); g.fill(); g.stroke();                      // cou
    [-1, 1].forEach(s => { g.beginPath(); g.ellipse(cx + s * 225, cy + 20, 30, 60, 0, 0, 7); g.fill(); g.stroke(); });
    const tete = new Path2D(); tete.ellipse(cx, cy, 220, 290, 0, 0, 7);
    g.fill(tete);
    // cheveux (haut du crâne) et bande rasée
    g.save(); g.clip(tete); g.fillStyle = '#4a4038'; g.beginPath(); g.ellipse(cx, cy - 60, 240, 260, 0, Math.PI, 2 * Math.PI); g.fill();
    g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 3; for (let i = 0; i < 22; i++) { const x = cx - 200 + i * 19; g.beginPath(); g.moveTo(x, cy - 330); g.quadraticCurveTo(x + 10, cy - 200, x - 6, cy - 70); g.stroke(); }
    const yb = lerp(cy - 300, cy - 70, k); g.fillStyle = '#b8a888'; g.fillRect(cx - 32, cy - 300, 64, yb - (cy - 300));
    g.restore();
    g.strokeStyle = CREME; g.lineWidth = 8; g.stroke(tete);
    g.lineWidth = 6; [-1, 1].forEach(s => { g.beginPath(); g.moveTo(cx + s * 60 - 34, cy + 40); g.lineTo(cx + s * 60 + 34, cy + 40); g.stroke(); });
    g.beginPath(); g.moveTo(cx - 50, cy + 170); g.lineTo(cx + 50, cy + 170); g.stroke();
    // petit rasoir au bout de la bande
    if (k < 1) { g.save(); g.translate(cx + 40, yb); g.rotate(-.5); g.fillStyle = '#cfc8bb'; g.strokeStyle = NOIR; g.lineWidth = 3; g.fillRect(-10, -12, 90, 24); g.strokeRect(-10, -12, 90, 24); g.restore(); }
    deux(p.t, 1440, 110);
  }
  // le tabouret : élan, puis un seul impact (éclair, onde), sans rien montrer de plus
  function tabouret(p, t, l) {
    const tc = tps(p.coup), k = eo(pr(t, p.a, Math.max(.3, tc - p.a))), apres = t >= tc;
    const sec = apres ? 1 - pr(t, tc, .35) : 0;
    g.save(); g.translate((rnd(t * 91) - .5) * 40 * sec, (rnd(t * 37) - .5) * 30 * sec);
    g.save(); g.translate(lerp(820, 560, k), lerp(980, 820, k)); g.rotate(lerp(.9, -.2, k));
    g.fillStyle = '#5b4636'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.lineCap = 'round'; [[-110, 20, -170, 330], [110, 20, 170, 330], [0, 20, 0, 320]].forEach(([a, b, c, d], i) => { g.lineWidth = i === 2 ? 14 : 22; g.strokeStyle = '#5b4636';
      g.beginPath(); g.moveTo(a, b); g.lineTo(c, d); g.stroke(); });
    g.lineWidth = 6; g.strokeStyle = CREME; g.beginPath(); g.roundRect(-160, -24, 320, 48, 14); g.fill(); g.stroke();
    g.restore();
    if (apres) { const ki = pr(t, tc, .4); g.strokeStyle = `rgba(239,230,210,${1 - ki})`; g.lineWidth = 8;
      for (let i = 0; i < 10; i++) { const a = i / 10 * 6.28, r0 = 60 + ki * 120, r1 = r0 + 80; g.beginPath(); g.moveTo(420 + Math.cos(a) * r0, 640 + Math.sin(a) * r0); g.lineTo(420 + Math.cos(a) * r1, 640 + Math.sin(a) * r1); g.stroke(); } }
    g.restore();
    if (apres) { const kf = pr(t, tc, .2); if (kf < 1) { g.fillStyle = `rgba(255,248,230,${(1 - kf) * .6})`; g.fillRect(0, 0, W, H); } }
    deux(p.t, 1340, 110);
    if (p.sous) sous(p.sous, 1490);
  }
  // portrait pixelisé : méconnaissable
  let pix;
  function flou(p, t, l) {
    const im = S.img('stockdale'); if (!im) return;
    const n = Math.round(lerp(60, 10, eo(pr(t, p.a, .35))));
    if (!pix) pix = document.createElement('canvas');
    pix.width = n; pix.height = Math.round(n * 4 / 3); const x = pix.getContext('2d'); x.drawImage(im, 0, 0, pix.width, pix.height);
    g.save(); g.translate(W / 2, 760); g.rotate(-.03);
    g.fillStyle = CREME; g.shadowColor = 'rgba(0,0,0,.7)'; g.shadowBlur = 50; g.fillRect(-314, -414, 628, 828); g.shadowColor = 'transparent';
    g.imageSmoothingEnabled = false; g.filter = 'grayscale(1) contrast(1.3) brightness(.85) sepia(.25)';
    g.drawImage(pix, -300, -400, 600, 800); g.filter = 'none'; g.imageSmoothingEnabled = true;
    g.restore();
    O.tampon(p.t, W / 2, 1320, pr(t, p.a + .08, .3), -.08, 92);
  }
  // la Medal of Honor : zoom du portrait officiel vers la médaille
  function medaille(p, t, l) {
    O.petitTitre('— 1976 —', 340);
    const z = lerp(1, 2.9, eo(pr(t, p.a, 1.3)));
    O.carte('stockdale', W / 2, 800, 760, 800, .02, z, .44, .86, { lum: .95, contraste: 1.2 });
    O.multi([[p.t, OR]], 1330, 130);
    sous(p.sous, 1440, 50);
  }
  // ce qu'on ne peut pas lui prendre : une lumière dans la tête, derrière les barreaux
  function citadelle(p, t, l) {
    barreaux(.45);
    O.petitTitre('CE QUI DÉPEND DE LUI', 470);
    S.d.tete(560, 860, 300, { trait: CREME, fond: SOMBRE, ep: 9 });
    const k = eo(pr(t, p.a, .5)), r = (140 + Math.sin(t * 3) * 14) * k;
    if (r > 1) { const v = g.createRadialGradient(600, 760, 4, 600, 760, r); v.addColorStop(0, 'rgba(255,236,180,.95)'); v.addColorStop(.35, 'rgba(217,180,90,.7)'); v.addColorStop(1, 'rgba(217,180,90,0)');
      g.fillStyle = v; g.beginPath(); g.arc(600, 760, r, 0, 7); g.fill(); }
    O.multi([['SON ', CREME], ['JUGEMENT', OR]], 1380, 140);
  }

  return { avion, ejection, chute, murmure, mondes, lieu, cellule, jours, tetelivre, colonnes, rasoir, camera, crane, tabouret, flou, medaille, citadelle };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'avion') { L.push([p.a, 'souffle', .7]); if (p.abis) L.push([tps(p.abis), 'pop', .5]); }
  if (p.type === 'ejection') L.push([p.a + .03, 'whoosh', 1]);
  if (p.type === 'chute') { L.push([p.a, 'souffle', .45]); if (p.chrono) for (let k = 0; k < Math.floor(p.b - p.a); k++) L.push([p.a + k + .05, 'tic', .55]); }
  if (p.type === 'murmure') { const n = p.t.length, d = p.duree || 1; for (let k = 0; k < n; k += 2) L.push([p.a + d * k / n, 'tic', .25]); }
  if (p.type === 'mondes') { L.push([p.a, 'bip', .35]); L.push([tps(p.barre), 'stylo', .7]); }
  if (p.type === 'lieu') { L.push([p.a, 'papier', .5]); if (p.surnom) L.push([tps(p.surnom), 'pop', .4]); }
  if (p.type === 'cellule') p.mots.forEach(([a]) => L.push([tps(a), 'frappe', .8]));
  if (p.type === 'jours') { const d = Math.max(.5, p.b - p.a - .4); L.push([tps(p.court), 'lame', .8]); for (let k = 0; k < 16; k++) L.push([p.a + .25 + d * (1 - Math.sqrt(1 - k / 16)), 'tic', .35]); }
  if (p.type === 'tetelivre') L.push([tps(p.livre), 'pop', .6]);
  if (p.type === 'colonnes') [['s8', 0], ['s8', 'et'], ['s9', 'corps'], ['s9', 'douleur'], ['s9', 'accepte'], ['s9', 'refuse'], ['s9', 'oui']].forEach(a => {
    const t = tps(a); if (t >= p.a - .01 && t < p.b) L.push([t, a[1] === 'oui' ? 'valide' : 'stylo', a[1] === 'oui' ? .6 : .35]); });
  if (p.type === 'rasoir') L.push([p.a + .1, 'lame', .9]);
  if (p.type === 'camera') { if (p.coupe) L.push([p.a + .1, 'coupe', .9]); else L.push([p.a, 'clic', .6], [p.a + .1, 'disque', .4]); if (p.prop) L.push([tps(p.prop) + .05, 'tampon', 1]); }
  if (p.type === 'crane') [0, .8, 1.6].forEach(d => L.push([p.a + d, 'frotte', .45]));
  if (p.type === 'tabouret') { L.push([p.a, 'whoosh', .5]); L.push([tps(p.coup), 'frappe', 1]); }
  if (p.type === 'flou') L.push([p.a, 'glitch', .7]);
  if (p.type === 'medaille') L.push([p.a, 'valide', .7]);
  if (p.type === 'citadelle') L.push([p.a, 'souffle', .6]);
};
