// Plans propres au short « Vrai ou faux : la Seconde Guerre mondiale », dans le style du modèle A (noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs). Les plans vraifaux sont communs (formats-a.js).
window.SANS_ST_A = ['chrono', 'stalingrad', 'prisonniers', 'commentaire'];
window.PROPRES_A = ['archive', 'chrono', 'pologne', 'urss', 'globe', 'stalingrad', 'prisonniers', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const milliers = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  const zone = (pts, fond, trait = CREME, ep = 5) => { g.fillStyle = fond; g.strokeStyle = trait; g.lineWidth = ep; g.beginPath(); pts.forEach(([x, y], i) => i ? g.lineTo(x, y) : g.moveTo(x, y)); g.closePath(); g.fill(); g.stroke(); };

  // photo d'archive en carte + titre
  function archive(p, t, l) {
    const k = eo(pr(t, p.a, .35));
    O.carte(p.img, W / 2 + lerp(260, 0, k), 760, 760, 620, lerp(.12, -.03, k), 1.1 + l * .03, .5, .5, { lum: .9 });
    deux(p.t, 1330, 120);
    if (p.legende) S.texte(p.legende, W / 2, 1470, { taille: 34, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 960 });
  }

  // chronomètre « top chrono »
  function chrono(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = '#1b1712'; g.strokeStyle = CREME; g.lineWidth = 12;
    g.fillRect(-40, -390, 80, 50); g.strokeRect(-40, -390, 80, 50);
    g.beginPath(); g.arc(0, 0, 320, 0, 7); g.fill(); g.stroke();
    for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; g.lineWidth = 8; g.beginPath(); g.moveTo(Math.sin(a) * 280, -Math.cos(a) * 280); g.lineTo(Math.sin(a) * 240, -Math.cos(a) * 240); g.stroke(); }
    const a = lt * 4; g.strokeStyle = ROUGE; g.lineWidth = 12; g.lineCap = 'round'; g.beginPath(); g.moveTo(0, 0); g.lineTo(Math.sin(a) * 250, -Math.cos(a) * 250); g.stroke();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 22, 0, 7); g.fill();
    g.restore();
    O.multi([['TOP ', CREME], ['CHRONO', OR]], 1410, 150);
  }

  // le partage secret de la Pologne (schéma)
  function pologne(p, t) {
    O.petitTitre('— AOÛT 1939 · SCHÉMA —', 470);
    const k = eo(pr(t, p.a + .15, .6));
    zone([[80, 640], [330, 600], [360, 820], [330, 1080], [80, 1100]], '#3a2f25');
    zone([[750, 560], [1020, 540], [1020, 1140], [760, 1120], [720, 900]], '#3a2f25');
    S.texte('ALLEMAGNE', 205, 1160, { taille: 38, coul: CREME, poids: 700 });
    S.texte('URSS', 880, 1180, { taille: 44, coul: CREME, poids: 700 });
    // la Pologne, coupée en deux par la ligne secrète
    const PL = [[360, 640], [560, 600], [730, 640], [720, 900], [760, 1100], [560, 1140], [330, 1080], [360, 820]];
    zone(PL, '#1b1712', OR, 7);
    g.save(); g.beginPath(); PL.forEach(([x, y], i) => i ? g.lineTo(x, y) : g.moveTo(x, y)); g.closePath(); g.clip();
    g.fillStyle = `rgba(239,230,210,${.28 * k})`; g.fillRect(300, 560, 250 * k, 620);
    g.fillStyle = `rgba(200,55,45,${.35 * k})`; g.fillRect(780 - 230 * k, 560, 230 * k, 620);
    g.restore();
    g.save(); g.setLineDash([22, 14]); g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.moveTo(560, 600); g.lineTo(560, 600 + 540 * k); g.stroke(); g.restore();
    S.texte('POLOGNE', 560, 870, { taille: 54, coul: OR, contour: NOIR, contourL: 8 });
    O.tampon('SECRET', W / 2, 1360, pr(t, p.a + .5, .3), -.1, 130);
  }

  // pas de débarquement : la Grande-Bretagne tient, Hitler se tourne vers l'URSS
  function urss(p, t) {
    const k = eo(pr(t, p.a, .5));
    zone([[150, 450], [330, 420], [380, 620], [300, 760], [130, 720]], '#3a2f25');
    S.texte('GRANDE-BRETAGNE', 260, 820, { taille: 34, coul: CREME, poids: 700 });
    O.tampon('REPORTÉE', 300, 600, pr(t, p.a + .1, .3), -.14, 62);
    zone([[330, 900], [560, 870], [580, 1180], [340, 1200]], '#3a2f25');
    S.texte('ALLEMAGNE', 455, 1250, { taille: 38, coul: CREME, poids: 700 });
    zone([[720, 700], [1040, 660], [1040, 1340], [740, 1320], [700, 1000]], '#3a2f25');
    S.texte('URSS', 880, 1390, { taille: 48, coul: CREME, poids: 700 });
    S.d.fleche(560, 1030, 820, 1010, k, { trait: ROUGE, ep: 18 });
    O.multi([['VERS ', CREME], ['L’URSS', OR]], 1540, 130);
  }

  // le globe qui s'embrase
  function globe(p, t) {
    const lt = t - p.a, cx = W / 2, cy = 830, r = 330;
    g.fillStyle = '#1b1712'; g.strokeStyle = OR; g.lineWidth = 8; g.beginPath(); g.arc(cx, cy, r, 0, 7); g.fill(); g.stroke();
    g.save(); g.beginPath(); g.arc(cx, cy, r, 0, 7); g.clip(); g.strokeStyle = 'rgba(217,180,90,.3)'; g.lineWidth = 3;
    for (let i = 0; i < 6; i++) { const ph = (i / 6 + lt * .08) % 1, w = Math.cos(ph * Math.PI) * r; g.beginPath(); g.ellipse(cx, cy, Math.abs(w), r, 0, 0, 7); g.stroke(); }
    for (let j = -2; j <= 2; j++) { g.beginPath(); g.moveTo(cx - r, cy + j * r * .38); g.lineTo(cx + r, cy + j * r * .38); g.stroke(); }
    g.restore();
    [[-.15, -.45], [.25, -.5], [-.05, -.08], [.55, .05], [-.6, .15], [.4, -.18], [-.35, -.3], [.1, .4]].forEach(([x, y], i) => {
      const k = pr(t, p.a + .1 + i * .14, .5); if (k <= 0) return;
      g.save(); g.strokeStyle = ROUGE; g.globalAlpha = 1 - ((lt * 1.2 + i * .3) % 1); g.lineWidth = 5; g.beginPath(); g.arc(cx + x * r, cy + y * r, 14 + ((lt * 1.2 + i * .3) % 1) * 50, 0, 7); g.stroke(); g.restore();
      g.fillStyle = ROUGE; g.beginPath(); g.arc(cx + x * r, cy + y * r, 14 * back(k), 0, 7); g.fill();
    });
    deux(p.t || 'LA GUERRE DEVIENT|MONDIALE', 1390, 130);
  }

  // Stalingrad : ville en ruines sous la neige, la capitulation
  function stalingrad(p, t) {
    const lt = t - p.a;
    g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 5;
    g.beginPath(); g.moveTo(0, 1000);
    [[60, 820], [140, 820], [140, 900], [220, 900], [220, 760], [270, 740], [300, 900], [380, 900], [380, 700], [450, 700], [470, 780], [520, 780],
      [520, 860], [600, 860], [610, 720], [700, 700], [700, 880], [780, 880], [790, 800], [860, 760], [880, 900], [960, 900], [960, 780], [1080, 760]].forEach(([x, y]) => g.lineTo(x, y));
    g.lineTo(1080, 1000); g.closePath(); g.fill(); g.stroke();
    for (let i = 0; i < 70; i++) { const x = (rnd(i) * W + lt * 40) % W, y = 300 + ((rnd(i + 70) * 900 + lt * (80 + rnd(i) * 80)) % 900);
      g.fillStyle = 'rgba(239,230,210,.7)'; g.beginPath(); g.arc(x, y, 2 + rnd(i + 3) * 4, 0, 7); g.fill(); }
    O.petitTitre('— STALINGRAD —', 1080, OR);
    const k = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1230); g.scale(k, k);
    S.texte('31 JANVIER 1943', 0, 0, { taille: 110, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 10 }); g.restore();
    O.tampon('PAULUS CAPITULE', W / 2, 1430, pr(t, p.a + .5, .3), -.06, 80);
  }

  // les prisonniers : compteur jusqu'à 91 000
  function prisonniers(p, t) {
    const tn = p.n ? tps(p.n) : p.a, u = eo(pr(t, tn, 1.0)), n = Math.round(lerp(0, 91000, u));
    const tot = 120, vis = Math.floor(tot * u);
    for (let i = 0; i < tot; i++) {
      const x = 130 + (i % 12) * 74, y = 480 + Math.floor(i / 12) * 64, on = i < vis;
      g.fillStyle = on ? 'rgba(239,230,210,.8)' : 'rgba(239,230,210,.12)';
      g.beginPath(); g.arc(x, y - 12, 11, 0, 7); g.fill(); g.beginPath(); g.ellipse(x, y + 14, 17, 13, 0, Math.PI, 0); g.fill();
    }
    S.texte('ENVIRON', W / 2, 1200, { taille: 56, coul: CREME, esp: 8 });
    S.texte(milliers(n), W / 2, 1350, { taille: 220, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 14 });
    S.texte('PRISONNIERS ALLEMANDS', W / 2, 1500, { taille: 64, coul: CREME, contour: NOIR, contourL: 8, max: 960 });
  }

  // une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .3)), txt = 'J’en ai eu 4 sur 5 !', n = Math.floor(cl((t - p.a - .3) / .8) * txt.length);
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-300, 165); g.lineTo(-340, 260); g.lineTo(-220, 165); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-330, -60, 50, 0, 7); g.fill();
    S.texte('toi', -230, -60, { taille: 44, coul: GRIS, align: 'left', poids: 600 });
    S.texte(txt.slice(0, n), -360, 60, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, align: 'left', max: 760 });
    const kc = pr(t, p.a + 1.2, .3); if (kc > 0) { g.save(); g.translate(350, -80); g.scale(back(kc), back(kc)); g.fillStyle = ROUGE;
      g.beginPath(); g.moveTo(0, 30); g.bezierCurveTo(-60, -10, -30, -60, 0, -30); g.bezierCurveTo(30, -60, 60, -10, 0, 30); g.fill(); g.restore(); }
    g.restore();
    deux('DIS TON SCORE|EN COMMENTAIRE', 1350, 110);
  }

  return { archive, chrono, pologne, urss, globe, stalingrad, prisonniers, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'archive') L.push([p.a, 'papier', .45]);
  if (p.type === 'chrono') L.push([p.a, 'clic', .7], [p.a + .3, 'tic', .5], [p.a + .6, 'tic', .5]);
  if (p.type === 'pologne') L.push([p.a + .15, 'lame', .5], [p.a + .52, 'tampon', .9]);
  if (p.type === 'urss') L.push([p.a + .12, 'tampon', .7], [p.a + .2, 'whoosh', .5]);
  if (p.type === 'globe') L.push([p.a + .1, 'souffle', .4]);
  if (p.type === 'stalingrad') L.push([p.a, 'souffle', .4], [p.a + .52, 'tampon', .9]);
  if (p.type === 'prisonniers') L.push([p.n ? tps(p.n) : p.a, 'montee', .45]);
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .3 + k * .1, 'tic', .25]); L.push([p.a + 1.2, 'pop', .5]); }
};
