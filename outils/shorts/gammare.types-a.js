// Plans propres au short Gammare (« Ce n'est pas lui qui décide »), dans le style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Le parasite est toujours dessiné en rouge.
window.SANS_ST_A = ['bacsvt'];
window.PROPRES_A = ['riviere', 'marionnette', 'ver', 'bec', 'cycle', 'genes', 'etendu', 'bacsvt'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const SOMBRE = '#1b1712', CORPS = '#4a3d2c';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };
  const SURF = 470, FOND = 1190;

  // ---------- dessins
  // gammare de profil, tête à droite ; (x, y) = centre, s = échelle ; o.parasite : kyste rouge ; renvoie les points d'attache
  function gammare(x, y, s, rot, t, o = {}) {
    const pts = [];
    g.save(); g.translate(x, y); g.rotate(rot); g.scale(s, s);
    const P = u => { const a = lerp(Math.PI * .92, Math.PI * .08, u); return [Math.cos(a) * 120, -Math.sin(a) * 70 + 40]; };
    const nage = Math.sin(t * 14) * .35;
    // pattes
    g.strokeStyle = 'rgba(239,230,210,.8)'; g.lineWidth = 4; g.lineCap = 'round';
    for (let i = 0; i < 7; i++) { const u = .2 + i * .1, [px, py] = P(u), a = Math.PI / 2 + Math.sin(t * 14 + i) * .35 - .2;
      const ex = px + Math.cos(a) * 55, ey = py + 30 + Math.sin(a) * 40; g.beginPath(); g.moveTo(px, py + 20); g.lineTo(px + 10, py + 45); g.lineTo(ex, ey); g.stroke(); pts.push([ex, ey]); }
    // queue (uropodes)
    const [qx, qy] = P(0); [-.5, 0, .5].forEach(d => { g.beginPath(); g.moveTo(qx, qy); g.lineTo(qx - 40, qy + 30 + d * 40 + nage * 10); g.stroke(); });
    // segments du corps
    for (let i = 0; i <= 10; i++) { const u = i / 10, [px, py] = P(u), r = 30 + 14 * Math.sin(Math.PI * u);
      g.fillStyle = CORPS; g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath(); g.ellipse(px, py, r * .75, r, 0, 0, 7); g.fill(); g.stroke(); }
    for (let i = 1; i <= 9; i++) { const [px, py] = P(i / 10); g.strokeStyle = 'rgba(217,180,90,.55)'; g.lineWidth = 3; g.beginPath(); g.moveTo(px, py - 34); g.lineTo(px, py + 20); g.stroke(); }
    // tête, œil, antennes
    const [hx, hy] = P(1); rond(hx + 18, hy + 4, 30, CORPS, CREME, 4); rond(hx + 26, hy - 4, 7, NOIR);
    g.strokeStyle = CREME; g.lineWidth = 3;
    [[-.9, 120], [-.5, 100]].forEach(([a, L], i) => { g.beginPath(); g.moveTo(hx + 34, hy - 10); g.quadraticCurveTo(hx + 34 + L * .6, hy - 10 + a * L * .7 + nage * 8, hx + 34 + L, hy - 10 + a * L * .3 + nage * 14); g.stroke();
      pts.push([hx + 34 + L, hy - 10 + a * L * .3 + nage * 14]); });
    let kyste = null;
    if (o.parasite) { const [cx, cy] = P(.55); kyste = [cx, cy - 5]; g.shadowColor = ROUGE; g.shadowBlur = 30 + 15 * Math.sin(t * 6); rond(cx, cy - 5, 15, ROUGE); g.shadowBlur = 0; rond(cx, cy - 5, 21, null, OR, 3); }
    g.restore();
    // points en coordonnées de l'écran
    const vers = ([px, py]) => { const c = Math.cos(rot), si = Math.sin(rot); return [x + (px * c - py * si) * s, y + (px * si + py * c) * s]; };
    return { pattes: pts.map(vers), kyste: kyste && vers(kyste), P: u => vers(P(u)) };
  }
  // oiseau (silhouette en vol), ailes battantes
  function oiseau(x, y, s, t) {
    const b = Math.sin(t * 9) * 40;
    g.save(); g.translate(x, y); g.scale(s, s); g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-160, -20 - b); g.quadraticCurveTo(-70, -60 - b * .5, 0, 0); g.quadraticCurveTo(70, -60 - b * .5, 160, -20 - b);
    g.quadraticCurveTo(70, -10, 0, 30); g.quadraticCurveTo(-70, -10, -160, -20 - b); g.fill(); g.stroke();
    g.beginPath(); g.ellipse(0, 10, 26, 40, 0, 0, 7); g.fill(); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.moveTo(-8, 45); g.lineTo(0, 75); g.lineTo(8, 45); g.fill();
    g.restore();
  }
  // le ver parasite : un trait rouge ondulant
  function verDessin(x, y, L, t, ep = 7) {
    g.save(); g.strokeStyle = ROUGE; g.lineWidth = ep; g.lineCap = 'round'; g.shadowColor = ROUGE; g.shadowBlur = 14; g.beginPath();
    for (let i = 0; i <= 14; i++) { const u = i / 14, xx = x - L / 2 + u * L, yy = y + Math.sin(u * 9 + t * 10) * L * .08; i ? g.lineTo(xx, yy) : g.moveTo(xx, yy); }
    g.stroke(); g.restore();
  }
  function helice(x0, x1, y, amp) {
    g.save(); g.lineCap = 'round';
    for (let i = 0; i <= 14; i++) { const u = i / 14, x = lerp(x0, x1, u), a = Math.sin(u * 9) * amp; g.strokeStyle = 'rgba(239,230,210,.45)'; g.lineWidth = 5; g.beginPath(); g.moveTo(x, y + a); g.lineTo(x, y - a); g.stroke(); }
    [[1, CREME], [-1, OR]].forEach(([s, c]) => { g.strokeStyle = c; g.lineWidth = 8; g.beginPath(); for (let i = 0; i <= 60; i++) { const u = i / 60, yy = y + s * Math.sin(u * 9) * amp; i ? g.lineTo(lerp(x0, x1, u), yy) : g.moveTo(lerp(x0, x1, u), yy); } g.stroke(); });
    g.restore();
  }
  // décor : surface, lumière, fond caillouteux
  function decor(lum, t) {
    const gr = g.createLinearGradient(0, SURF, 0, FOND + 120); gr.addColorStop(0, 'rgba(60,70,62,.55)'); gr.addColorStop(1, 'rgba(13,11,9,0)');
    g.fillStyle = gr; g.fillRect(0, SURF, W, FOND + 120 - SURF);
    if (lum > 0) { g.save(); g.globalAlpha = lum * .5; for (let i = 0; i < 5; i++) { const x = 140 + i * 200 + Math.sin(t + i) * 20; const r = g.createLinearGradient(0, 200, 0, FOND);
      r.addColorStop(0, 'rgba(255,236,170,.75)'); r.addColorStop(1, 'rgba(255,236,170,0)'); g.fillStyle = r; g.beginPath(); g.moveTo(x - 30, 200); g.lineTo(x + 30, 200); g.lineTo(x + 140, FOND); g.lineTo(x - 80, FOND); g.fill(); } g.restore();
      g.save(); g.globalAlpha = lum; g.shadowColor = OR; g.shadowBlur = 60; rond(W / 2, 290, 70, '#f3dc96'); g.restore(); }
    g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); for (let x = 0; x <= W; x += 10) g.lineTo(x, SURF + Math.sin(x * .02 + t * 3) * 10); g.stroke();
    for (let i = 0; i < 16; i++) S.d.pierre(30 + i * 70 + rnd(i) * 30, FOND + 70 + rnd(i + 5) * 40, 34 + rnd(i + 9) * 20, rnd(i) * 3, { trait: 'rgba(239,230,210,.5)', fond: '#2a241d', ep: 4 });
  }

  // ---------- plans
  // la rivière : p.pos 'fond' | 'monte' | 'surface' ; p.parasite, p.lumiere, p.tournoie, p.oiseau ('ombre'), p.cible
  function riviere(p, t, l) {
    const dur = Math.max(.8, (p.b || p.a + 2) - p.a);
    decor(p.lumiere ? eo(pr(t, p.a, .5)) : 0, t);
    let x = 540, y = FOND - 40, rot = .05;
    if (p.pos === 'monte') { const k = eo(pr(t, p.a, dur)); y = lerp(FOND - 40, SURF + 110, k); x = lerp(420, 600, k); rot = -.7 + Math.sin(t * 6) * .08; }
    if (p.pos === 'surface') { const w = 7; x = 540 + Math.cos(t * w) * 170; y = SURF + 110 + Math.sin(t * w) * 45; rot = t * w + Math.PI / 2; }
    if (p.pos === 'fond') x = 540 + Math.sin(t * 1.5) * 30;
    gammare(x, y, 1.15, rot, t, { parasite: p.parasite });
    if (p.oiseau === 'ombre') { const k = pr(t, p.a, dur); oiseau(lerp(1250, -200, k), 260 + Math.sin(k * 6) * 20, .9, t); }
    if (p.cible) { const k = back(pr(t, p.a + .1, .3)); g.save(); g.translate(x, y); g.scale(k, k); g.strokeStyle = ROUGE; g.lineWidth = 7;
      rond(0, 0, 190 + Math.sin(t * 8) * 10, null, ROUGE, 7); [[0, -1], [0, 1], [1, 0], [-1, 0]].forEach(([a, b]) => { g.beginPath(); g.moveTo(a * 150, b * 150); g.lineTo(a * 240, b * 240); g.stroke(); }); g.restore(); }
    if (p.t) deux(p.t, 1460, 104);
  }

  // un gammare « marionnette » : des fils rouges partent du kyste vers ses pattes et ses antennes
  function marionnette(p, t, l) {
    const z = p.zoom ? lerp(1, 1.35, eo(pr(t, p.a, .6))) : 1;
    g.save(); g.translate(W / 2, 880); g.scale(z, z); g.translate(-W / 2, -880);
    const r = gammare(W / 2, 880, 2.5, -.05, t, { parasite: true });
    const k = eo(pr(t, p.a + .15, .5));
    g.strokeStyle = 'rgba(200,55,45,.85)'; g.lineWidth = 3;
    r.pattes.forEach(([x, y], i) => { const [cx, cy] = r.kyste; g.beginPath(); g.moveTo(cx, cy); g.lineTo(lerp(cx, x, k), lerp(cy, y, k)); g.stroke(); });
    g.restore();
    if (p.t) deux(p.t, 1440, 104);
  }

  // le ver entre (p.etape 'entre') puis s'enkyste (p.etape 'kyste', repère p.kyste)
  function ver(p, t, l) {
    const r = gammare(W / 2, 860, 2.4, 0, t, { parasite: p.etape === 'kyste' && t >= tps(p.kyste) });
    const [cx, cy] = r.P(.55);
    if (p.etape === 'entre') { const k = eo(pr(t, p.a + .1, 1.0)); verDessin(lerp(60, cx - 10, k), lerp(1250, cy - 10, k), 90, t); }
    else {
      const kk = pr(t, tps(p.kyste), .35);
      if (kk < 1) { g.save(); g.translate(cx, cy - 12); g.scale(1 - kk * .6, 1 - kk * .6); verDessin(0, 0, 80, t); g.restore(); }
      if (kk > 0) { pop(kk, cx, cy - 12, () => { rond(0, 0, 50, null, OR, 8); });
        g.save(); g.globalAlpha = kk; g.strokeStyle = OR; g.lineWidth = 4; g.beginPath(); g.moveTo(cx + 30, cy - 50); g.lineTo(cx + 170, cy - 260); g.stroke();
        S.texte('KYSTE', cx + 200, cy - 300, { taille: 70, coul: OR, contour: NOIR, contourL: 8 }); g.restore(); }
    }
    if (p.t) deux(p.t, 1440, 104);
  }

  // le bec de l'oiseau plonge dans l'eau
  function bec(p, t, l) {
    const y0 = 900, k = eo(pr(t, p.a, .3));
    g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); for (let x = 0; x <= W; x += 10) g.lineTo(x, y0 + Math.sin(x * .02 + t * 3) * 10); g.stroke();
    if (k < .95) gammare(560, y0 + 90, 1, t * 7, t, { parasite: true });
    const hy = lerp(-200, 560, k);
    g.save(); g.translate(540, hy);
    g.fillStyle = OR; g.strokeStyle = NOIR; g.lineWidth = 6; g.beginPath(); g.moveTo(-40, 120); g.lineTo(0, 470); g.lineTo(40, 120); g.closePath(); g.fill(); g.stroke();
    rond(0, 40, 170, SOMBRE, CREME, 8); rond(60, 0, 18, CREME); rond(64, 0, 8, NOIR);
    g.restore();
    const ks = pr(t, p.a + .25, .5);
    if (ks > 0 && ks < 1) for (let i = 0; i < 12; i++) { const a = -Math.PI * (i + .5) / 12, d = ks * 260; rond(540 + Math.cos(a) * d, y0 + Math.sin(a) * d * .8 + ks * ks * 200, 12 * (1 - ks), CREME); }
    if (p.t) deux(p.t, 1460, 120);
  }

  // le voyage du parasite : du gammare à l'oiseau (etape 1), puis adulte dans son intestin (etape 2, repère p.repro)
  function cycle(p, t, l) {
    if (p.etape === 1) {
      gammare(250, 1080, .9, -.3, t, { parasite: true });
      oiseau(780, 650, 1.1, t);
      S.texte('L’OISEAU', 780, 850, { taille: 50, coul: CREME, esp: 6 }); S.texte('son hôte définitif', 780, 905, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: CREME });
      const k = eo(pr(t, p.a + .15, .9)); g.strokeStyle = ROUGE; g.lineWidth = 8; g.setLineDash([22, 16]);
      g.beginPath(); for (let i = 0; i <= 40 * k; i++) { const u = i / 40, x = lerp(330, 720, u), y = lerp(990, 740, u) - Math.sin(u * Math.PI) * 220; i ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); g.setLineDash([]);
      const u = k, vx = lerp(330, 720, u), vy = lerp(990, 740, u) - Math.sin(u * Math.PI) * 220; verDessin(vx, vy, 60, t);
    } else {
      // silhouette de l'oiseau posé, intestin doré, ver adulte
      g.save(); g.translate(W / 2, 830); g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 8;
      g.beginPath(); g.ellipse(0, 60, 300, 210, -.15, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.arc(250, -190, 110, 0, 7); g.fill(); g.stroke(); rond(280, -215, 14, CREME);
      g.fillStyle = OR; g.beginPath(); g.moveTo(350, -210); g.lineTo(470, -170); g.lineTo(350, -150); g.fill();
      g.strokeStyle = 'rgba(217,180,90,.7)'; g.lineWidth = 26; g.beginPath(); g.moveTo(170, -60);
      g.bezierCurveTo(60, 0, 200, 80, 40, 110); g.bezierCurveTo(-120, 140, -20, -20, -170, 40); g.bezierCurveTo(-240, 70, -230, 140, -300, 160); g.stroke();
      g.restore();
      const k = eo(pr(t, p.a + .1, .9)); verDessin(W / 2, 900, lerp(40, 200, k), t, lerp(6, 14, k));
      S.texte('INTESTIN', W / 2 - 230, 1090, { taille: 38, coul: GRIS, esp: 5 });
      if (p.repro && t >= tps(p.repro)) { const kr = pr(t, tps(p.repro), .5);
        for (let i = 0; i < 9; i++) { const a = i * .7, d = kr * (80 + i * 14); rond(W / 2 + Math.cos(a) * d, 900 + Math.sin(a) * d * .6, 8, CREME); } }
    }
    if (p.t) deux(p.t, 1440, 104);
  }

  // gènes identiques, comportement différent ; p.pirate : tampon « PIRATÉ »
  function genes(p, t, l) {
    [[290, 'SAIN', false], [790, 'PARASITÉ', true]].forEach(([x, lab, par]) => {
      gammare(x, 560, .9, par ? -.6 : .05, t, { parasite: par });
      S.texte(lab, x, 720, { taille: 50, coul: par ? ROUGE : CREME, esp: 6 });
      helice(x - 190, x + 190, 860, 34);
    });
    const k = back(pr(t, p.a + .2, .3)); pop(pr(t, p.a + .2, .3), W / 2, 860, () => S.texte('=', 0, 0, { taille: 150, coul: OR, contour: NOIR, contourL: 10 }));
    S.texte('MÊMES GÈNES', W / 2, 980, { taille: 46, coul: OR, esp: 6 });
    if (p.pirate) {
      const kc = eo(pr(t, p.a, .4));
      S.d.fleche(290, 1080, 290, 1080 + 120 * kc, kc, { trait: CREME, ep: 10 }); S.texte('au fond', 290, 1250, { taille: 44, it: true, poids: 400, police: 'Spectral', coul: CREME });
      S.d.fleche(790, 1200, 790, 1200 - 120 * kc, kc, { trait: ROUGE, ep: 10 }); S.texte('vers la surface', 790, 1250, { taille: 44, it: true, poids: 400, police: 'Spectral', coul: CREME });
      O.tampon('PIRATÉ', W / 2, 1110, pr(t, tps(p.pirate), .3), -.12, 110);
    }
    if (p.t) deux(p.t, 1440, 100);
  }

  // phénotype étendu : le cercle du parasite s'agrandit jusqu'à englober le comportement du gammare
  function etendu(p, t, l) {
    const cx = W / 2, cy = 820, k = eo(pr(t, p.a + .2, .9));
    gammare(cx + 40, cy + 60, 1.3, -.5, t, { parasite: true });
    g.save(); g.globalAlpha = .9; S.d.fleche(cx + 250, cy + 200, cx + 250, cy - 80, k, { trait: ROUGE, ep: 8 }); g.restore();
    rond(cx - 230, cy - 230, 60, '#2a1a17', ROUGE, 6); verDessin(cx - 230, cy - 230, 70, t, 6);
    S.texte('LE PARASITE', cx - 230, cy - 330, { taille: 40, coul: ROUGE, esp: 5 });
    g.save(); g.setLineDash([24, 18]); g.lineDashOffset = -t * 40; g.strokeStyle = OR; g.lineWidth = 7;
    g.beginPath(); g.ellipse(lerp(cx - 230, cx, k), lerp(cy - 230, cy, k), lerp(90, 430, k), lerp(90, 400, k), 0, 0, 7); g.stroke(); g.restore();
    if (p.t) deux(p.t, 1440, 120);
  }

  // copie de bac de SVT (le plan « bac » du modèle est celui de philosophie)
  function bacsvt(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 900, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-400, -480, 800, 960); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
    S.texte('SCIENCES DE LA VIE ET DE LA TERRE', 0, -315, { taille: 32, coul: GRIS, esp: 4, poids: 600, max: 700 });
    g.fillStyle = NOIR; g.fillRect(-320, -260, 640, 3);
    S.texte('Sujet type', -320, -195, { taille: 40, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400 });
    const L = p.sujet; L.forEach((s, i) => S.texte(s, 0, -110 + i * 74, { taille: 60, police: 'Spectral', poids: 600, coul: NOIR, max: 700 }));
    const yb = -110 + L.length * 74;
    for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-320, yb + 30 + i * 50, 640 - (i === 3 ? 260 : 0), 6); }
    const kc = pr(t, p.a + .35, .5), cy = -110 + (L.length - 1) * 37; g.strokeStyle = ROUGE; g.lineWidth = 9;
    g.beginPath(); g.ellipse(0, cy, 380, 60 + L.length * 40, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['SUJET TYPE ', CREME], ['BAC', ROUGE]], 1560, 110);
  }

  return { riviere, marionnette, ver, bec, cycle, genes, etendu, bacsvt };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'riviere' && p.pos === 'monte') L.push([p.a, 'montee', .35]);
  if (p.type === 'riviere' && p.oiseau) L.push([p.a + .3, 'whoosh', .45]);
  if (p.type === 'riviere' && p.cible) L.push([p.a + .1, 'bip', .45]);
  if (p.type === 'riviere' && p.lumiere) L.push([p.a, 'souffle', .4]);
  if (p.type === 'riviere' && p.pos === 'surface' && !p.oiseau && !p.cible) L.push([p.a, 'frotte', .35]);
  if (p.type === 'marionnette') L.push([p.a + .15, 'glitch', .35]);
  if (p.type === 'ver' && p.etape === 'entre') L.push([p.a + .1, 'aspire', .5]);
  if (p.type === 'ver' && p.etape === 'kyste') L.push([tps(p.kyste), 'tampon', .6]);
  if (p.type === 'bec') L.push([p.a + .25, 'lame', .6]);
  if (p.type === 'cycle' && p.etape === 1) L.push([p.a + .15, 'whoosh', .5]);
  if (p.type === 'cycle' && p.etape === 2) { L.push([p.a + .1, 'montee', .3]); if (p.repro) L.push([tps(p.repro), 'pop', .6]); }
  if (p.type === 'genes') L.push([p.a + .2, 'bip', .4]);
  if (p.type === 'genes' && p.pirate) L.push([tps(p.pirate), 'tampon', .9], [tps(p.pirate) - .1, 'glitch', .4]);
  if (p.type === 'etendu') L.push([p.a + .2, 'montee', .45]);
  if (p.type === 'bacsvt') L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .6]);
};
