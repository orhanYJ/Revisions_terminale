// Plans propres au short « Pourquoi le krach de 1929 devient-il une crise mondiale ? » (format question de bac),
// dans le style du modèle A (noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre,
// fondImg, C = couleurs). La copie (plan commun « copie ») revient plusieurs fois : « copie2 » la remontre déjà en place
// (sans l'entrée de la feuille ni les sons de stylo, déjà posés par le premier plan « copie »).
window.SANS_ST_A = ['copie2'];
window.PROPRES_A = ['krach', 'monde', 'chrono', 'copie2', 'canaux', 'circuit', 'banque', 'taux', 'lingots', 'tarif', 'commerce', 'nue', 'preuves'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const BRUN = '#26221d';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const claque = (txt, x, y, a, t, o) => { if (t < a) return; const k = back(pr(t, a, .28)); g.save(); g.translate(x, y); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k)); g.globalAlpha = cl((t - a) * 6);
    S.texte(txt, 0, 0, Object.assign({ taille: 90, coul: OR, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };
  let F = null;   // plans communs (formats-a.js), chargés après ce fichier dans le vérificateur
  // boîte étiquetée (pays, banque…)
  function boite(txt, cx, cy, w, h, coul = CREME, fond = BRUN, taille = 64) {
    g.fillStyle = fond; g.strokeStyle = coul; g.lineWidth = 6; g.beginPath(); g.roundRect(cx - w / 2, cy - h / 2, w, h, 20); g.fill(); g.stroke();
    S.texte(txt, cx, cy + 3, { taille, coul, max: w - 40 });
  }
  // pièce d'or ou billet qui circule
  function piece(x, y, r, coul = OR, sym = '$') {
    g.fillStyle = coul; g.strokeStyle = NOIR; g.lineWidth = 4; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.stroke();
    S.texte(sym, x, y + 2, { taille: r * 1.3, coul: NOIR });
  }

  // courbe de la Bourse qui monte puis s'effondre (Wall Street, octobre 1929)
  function krach(p, t) {
    O.petitTitre('— WALL STREET · OCT. 1929 —', 420);
    g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 3;
    for (let y = 600; y <= 1200; y += 100) { g.beginPath(); g.moveTo(110, y); g.lineTo(970, y); g.stroke(); }
    const pts = []; for (let i = 0; i <= 60; i++) { const u = i / 60, x = lerp(120, 960, u);
      const y = u < .72 ? lerp(1150, 640, Math.pow(u / .72, 1.6)) + Math.sin(i * 1.7) * 14 : lerp(640, 1210, eo((u - .72) / .28)) + Math.sin(i * 2.3) * 10; pts.push([x, y]); }
    const k = cl((t - p.a) / 1.3), n = Math.max(2, Math.floor(k * pts.length));
    g.lineWidth = 12; g.lineJoin = 'round'; g.lineCap = 'round';
    for (let i = 1; i < n; i++) { g.strokeStyle = i > 43 ? ROUGE : OR; g.beginPath(); g.moveTo(...pts[i - 1]); g.lineTo(...pts[i]); g.stroke(); }
    if (n >= pts.length) { const s = .5 + .5 * Math.sin((t - p.a) * 12); g.fillStyle = ROUGE; g.beginPath(); g.arc(960, 1210, 18 + s * 8, 0, 7); g.fill(); }
    if (p.t) deux(p.t, 1420, 110);
  }

  // le globe : une onde rouge part de New York et gagne les autres continents
  function monde(p, t) {
    const cx = W / 2, cy = 860, R = 330, lt = t - p.a;
    g.save(); g.fillStyle = '#1b1712'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(cx, cy, R, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.arc(cx, cy, R, 0, 7); g.clip();
    g.strokeStyle = 'rgba(217,180,90,.25)'; g.lineWidth = 3;
    for (let k = -2; k <= 2; k++) { g.beginPath(); g.ellipse(cx, cy, Math.abs(k) * R / 2.6 + 1, R, 0, 0, 7); g.stroke(); g.beginPath(); g.moveTo(cx - R, cy + k * R / 3); g.lineTo(cx + R, cy + k * R / 3); g.stroke(); }
    const ny = [cx - 170, cy - 90];
    for (let i = 0; i < 3; i++) { const k = ((lt * .9 + i / 3) % 1); g.strokeStyle = ROUGE; g.globalAlpha = (1 - k) * .8; g.lineWidth = 8;
      g.beginPath(); g.arc(ny[0], ny[1], 40 + k * 520, 0, 7); g.stroke(); }
    g.globalAlpha = 1;
    // villes touchées les unes après les autres (Londres, Berlin, Vienne, Tokyo, Buenos Aires, Sydney)
    [[cx + 40, cy - 150], [cx + 110, cy - 130], [cx + 120, cy - 80], [cx + 290, cy - 70], [cx - 90, cy + 210], [cx + 260, cy + 200]].forEach(([x, y], i) => {
      const k = back(pr(t, p.a + .25 + i * .18, .25)); if (k <= 0) return; g.fillStyle = ROUGE; g.beginPath(); g.arc(x, y, 16 * k, 0, 7); g.fill(); });
    g.restore();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(ny[0], ny[1], 20, 0, 7); g.fill();
    S.texte('NEW YORK', ny[0], ny[1] - 46, { taille: 34, coul: CREME, contour: NOIR, contourL: 6 });
    if (p.t) deux(p.t, 1420, 110);
  }

  // « Tu as 60 secondes » : anneau qui se vide
  function chrono(p, t) {
    const lt = t - p.a, u = cl(lt / 6);
    g.save(); g.translate(W / 2, 860);
    g.strokeStyle = 'rgba(239,230,210,.2)'; g.lineWidth = 30; g.beginPath(); g.arc(0, 0, 280, 0, 7); g.stroke();
    g.strokeStyle = OR; g.beginPath(); g.arc(0, 0, 280, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
    const k = back(pr(t, p.a, .3)); g.scale(k, k);
    S.texte(String(60 - Math.floor(lt)), 0, 0, { taille: 250, police: 'Spectral', poids: 600, coul: CREME });
    S.texte('SECONDES', 0, 150, { taille: 44, coul: OR, esp: 8 });
    g.restore();
    if (p.t) deux(p.t, 1420, 110);
  }

  // la copie, déjà posée sur la table
  function copie2(p, t) { F = F || window.FORMATS_A(O); F.copie(Object.assign({}, p, { a: p.a - 1 }), t); }

  // trois canaux des États-Unis vers le monde : crédit, or, commerce (p.r = repères des étiquettes ; sinon en cascade)
  function canaux(p, t) {
    boite('ÉTATS-UNIS', W / 2, 520, 620, 150, OR);
    boite('LE MONDE', W / 2, 1180, 620, 150, CREME);
    const noms = ['CRÉDIT', 'OR', 'COMMERCE'], xs = [250, 540, 830];
    noms.forEach((s, i) => {
      const ta = p.r ? tps(p.r[i]) : p.a + .35 + i * .3, k = eo(pr(t, ta, .4)), on = t >= ta;
      const x = xs[i];
      g.save(); g.strokeStyle = on ? OR : 'rgba(239,230,210,.18)'; g.lineWidth = 16; g.setLineDash([26, 18]); g.lineDashOffset = -(t - p.a) * 120;
      g.beginPath(); g.moveTo(lerp(W / 2, x, .6), 600); g.lineTo(x, 1100); g.stroke(); g.restore();
      if (on) { S.d.fleche(x, 1000, x, 1100, 1, { trait: OR, ep: 14 });
        g.save(); g.translate(x, 840); g.scale(back(k), back(k)); g.fillStyle = NOIR; g.fillRect(-140, -40, 280, 80);
        S.texte(s, 0, 3, { taille: 52, coul: OR, max: 260 }); g.restore(); }
    });
    if (p.t) deux(p.t, 1430, 105);
    else O.multi([['TROIS ', CREME], ['CANAUX', OR]], 1430, 130);
  }

  // le circuit du plan Dawes : l'argent américain part vers l'Allemagne (étape 1) puis repart (étape 2)
  function circuit(p, t) {
    const e = p.etape || 1, lt = t - p.a;
    O.petitTitre(e === 1 ? '— PLAN DAWES, 1924 —' : '— APRÈS LE KRACH —', 400, e === 1 ? OR : ROUGE);
    const sh = e === 2 ? (rnd(t * 70) - .5) * 14 * (1 - pr(t, p.a, 1.2)) : 0;
    boite('ÉTATS-UNIS', W / 2, 560, 600, 140, OR);
    boite('ALLEMAGNE', W / 2 + sh, 1180, 600, 140, e === 2 ? ROUGE : CREME);
    for (let i = 0; i < 5; i++) { const u = ((lt * .8 + i / 5) % 1), y = e === 1 ? lerp(660, 1080, u) : lerp(1080, 660, u);
      g.globalAlpha = Math.sin(u * Math.PI); piece(W / 2 + Math.sin(u * 6 + i) * 60, y, 42, OR, '$'); g.globalAlpha = 1; }
    if (e === 1) { const k = back(pr(t, p.a + .3, .3)); g.save(); g.translate(W / 2, 1420); g.scale(k, k);
      S.texte('800 MILLIONS', 0, -50, { taille: 120, coul: OR, contour: NOIR, contourL: 12 });
      S.texte('de marks prêtés à l’Allemagne', 0, 60, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore(); }
    else deux('LES PRÊTS SONT|RAPPELÉS', 1420, 110);
  }

  // la Creditanstalt, Vienne : façade de banque ; p.faillite : tampon FAILLITE et fissure
  function banque(p, t) {
    const cx = W / 2, y0 = 560;
    g.fillStyle = '#3a3128'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(cx - 400, y0 + 120); g.lineTo(cx, y0); g.lineTo(cx + 400, y0 + 120); g.closePath(); g.fill(); g.stroke();
    g.fillRect(cx - 380, y0 + 130, 760, 50); g.strokeRect(cx - 380, y0 + 130, 760, 50);
    S.texte('CREDITANSTALT', cx, y0 + 157, { taille: 40, coul: OR, esp: 6 });
    for (let i = 0; i < 5; i++) { const x = cx - 300 + i * 150; g.fillStyle = '#4a4038'; g.fillRect(x - 32, y0 + 190, 64, 420); g.strokeRect(x - 32, y0 + 190, 64, 420); }
    g.fillStyle = '#3a3128'; g.fillRect(cx - 400, y0 + 610, 800, 50); g.strokeRect(cx - 400, y0 + 610, 800, 50);
    S.texte('VIENNE · MAI 1931', cx, y0 + 730, { taille: 50, coul: CREME, esp: 6 });
    if (p.faillite) {
      const ta = p.a, k = pr(t, ta, .3);
      g.strokeStyle = NOIR; g.lineWidth = 8; g.beginPath(); let x = cx + 20, y = y0 + 20; g.moveTo(x, y);
      for (let s = 0; s < 9 * cl(k * 2); s++) { x += (rnd(s * 7) - .5) * 120; y += 70; g.lineTo(x, y); } g.stroke();
      O.tampon('FAILLITE', cx, y0 + 400, k, -.12, 130);
      deux('LA PLUS GRANDE|BANQUE D’AUTRICHE', 1440, 95);
    } else deux('LA PLUS GRANDE|BANQUE D’AUTRICHE', 1440, 95);
  }

  // la Réserve fédérale relève ses taux (p.monte = repère) pour défendre le dollar
  function taux(p, t) {
    O.petitTitre('— RÉSERVE FÉDÉRALE —', 420);
    const k = back(pr(t, p.a, .35)); g.save(); g.translate(330, 860); g.scale(k, k); piece(0, 0, 190, OR, '$'); g.restore();
    const tm = p.monte ? tps(p.monte) : p.a + .6, km = eo(pr(t, tm, .7));
    g.fillStyle = BRUN; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(700, 560, 140, 620, 70); g.fill(); g.stroke();
    const h = lerp(140, 560, km); g.fillStyle = ROUGE; g.beginPath(); g.roundRect(722, 1160 - h, 96, h, 48); g.fill();
    S.texte('TAUX', 770, 1250, { taille: 56, coul: CREME });
    if (t >= tm) S.d.fleche(900, 1060, 900, 640, km, { trait: ROUGE, ep: 16 });
    deux(t >= tm ? 'LES TAUX|MONTENT' : 'DÉFENDRE|LE DOLLAR', 1440, 110);
  }

  // l'or quitte les autres pays pour les États-Unis
  function lingots(p, t) {
    const lt = t - p.a;
    S.texte('LES AUTRES PAYS', 260, 470, { taille: 44, coul: CREME, esp: 4 });
    S.texte('ÉTATS-UNIS', 820, 470, { taille: 44, coul: OR, esp: 4 });
    const lingot = (x, y) => { g.fillStyle = OR; g.strokeStyle = NOIR; g.lineWidth = 4; g.beginPath();
      g.moveTo(x - 80, y + 30); g.lineTo(x + 80, y + 30); g.lineTo(x + 55, y - 30); g.lineTo(x - 55, y - 30); g.closePath(); g.fill(); g.stroke(); };
    for (let i = 0; i < 9; i++) {
      const r = Math.floor(i / 3), c = i % 3, x0 = 140 + c * 120 + (r % 2) * 60, y0 = 1100 - r * 70;
      const k = eo(pr(t, p.a + .15 + i * .12, .55)), x = lerp(x0, x0 + 520, k), y = y0 - Math.sin(k * Math.PI) * 260;
      lingot(x, y);
    }
    g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 4; g.setLineDash([14, 12]); g.beginPath(); g.moveTo(540, 520); g.lineTo(540, 1180); g.stroke(); g.setLineDash([]);
    deux('L’OR QUITTE|LES AUTRES PAYS', 1420, 105);
  }

  // barrière de douane qui s'abaisse : Smoot-Hawley (étape 1), riposte du Canada (étape 2)
  function tarif(p, t) {
    const barriere = (x, y, k, lab, coul, sens = 1) => {
      g.fillStyle = BRUN; g.strokeStyle = CREME; g.lineWidth = 6; g.fillRect(x - 30, y - 40, 60, 360); g.strokeRect(x - 30, y - 40, 60, 360);
      g.save(); g.translate(x, y); g.rotate(sens * lerp(-1.25, 0, k));
      for (let i = 0; i < 6; i++) { g.fillStyle = i % 2 ? CREME : coul; g.fillRect(sens > 0 ? i * 70 : -(i + 1) * 70, -24, 70, 48); }
      g.restore();
      S.texte(lab, x + sens * 210, y + 120, { taille: 46, coul, max: 420 });
    };
    O.petitTitre('— DROITS DE DOUANE —', 400);
    const k1 = p.etape === 2 ? 1 : eo(pr(t, p.a + .2, .45));
    barriere(150, 760, k1, 'ÉTATS-UNIS', ROUGE, 1);
    if (p.etape === 2) { const k2 = eo(pr(t, p.a + .15, .45)); barriere(930, 1060, k2, 'CANADA', OR, -1);
      deux('LE CANADA|RIPOSTE', 1420, 115); }
    else { const k = back(pr(t, p.a + .5, .3)); g.save(); g.translate(W / 2, 1300); g.scale(k, k);
      S.texte('SMOOT-HAWLEY', 0, 0, { taille: 120, coul: OR, contour: NOIR, contourL: 12, max: 960 });
      S.texte('17 juin 1930 · signé par Hoover', 0, 110, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore(); }
  }

  // le commerce mondial perd environ deux tiers de sa valeur (1929 → 1934)
  function commerce(p, t) {
    O.petitTitre('— COMMERCE MONDIAL —', 400);
    const k = eo(pr(t, p.a + .15, .9)), base = 1180, hmax = 640;
    const barre = (x, h, coul, lab) => { g.fillStyle = coul; g.fillRect(x - 130, base - h, 260, h); g.strokeStyle = CREME; g.lineWidth = 5; g.strokeRect(x - 130, base - h, 260, h);
      S.texte(lab, x, base + 60, { taille: 60, police: 'Spectral', poids: 600, coul: CREME }); };
    barre(310, hmax, OR, '1929');
    barre(770, lerp(hmax, hmax / 3, k), ROUGE, '1934');
    g.strokeStyle = 'rgba(239,230,210,.4)'; g.lineWidth = 4; g.setLineDash([16, 12]); g.beginPath(); g.moveTo(640, base - hmax); g.lineTo(900, base - hmax); g.stroke(); g.setLineDash([]);
    claque('−2/3', W / 2, 1420, p.a + .9, t, { taille: 200, coul: ROUGE, contourL: 16 });
  }

  // l'erreur : une liste de titres sans aucun exemple, barrée
  function nue(p, t) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1300, 880, k)); g.rotate(.02);
    g.fillStyle = '#f3ecdc'; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillRect(-400, -360, 800, 720); g.shadowColor = 'transparent';
    ['I. Les prêts', 'II. L’or', 'III. Le commerce'].forEach((s, i) => S.texte(s, -320, -200 + i * 150, { taille: 62, police: 'Spectral', it: true, poids: 600, coul: NOIR, align: 'left' }));
    g.restore();
    const tx = p.x ? tps(p.x) : p.a + .6;
    if (t >= tx) { const kx = eo(pr(t, tx, .3)); g.strokeStyle = ROUGE; g.lineWidth = 22; g.lineCap = 'round';
      g.beginPath(); g.moveTo(220, 600); g.lineTo(lerp(220, 860, kx), lerp(600, 1160, kx)); g.stroke();
      if (kx > .5) { g.beginPath(); g.moveTo(860, 600); g.lineTo(lerp(860, 220, (kx - .5) * 2), lerp(600, 1160, (kx - .5) * 2)); g.stroke(); } }
    deux(p.t || 'UNE LISTE|SANS EXEMPLES', 1440, 105);
  }

  // les preuves : une date, un chiffre, un nom (p.r = trois repères)
  function preuves(p, t) {
    O.petitTitre('— CHAQUE ARGUMENT VEUT —', 420);
    [['MAI 1931', 'UNE DATE'], ['−2/3', 'UN CHIFFRE'], ['DAWES', 'UN NOM']].forEach(([s, lab], i) => {
      const ta = p.r ? tps(p.r[i]) : p.a + .3 + i * .5, y = 640 + i * 300; if (t < ta) return;
      O.tampon(s, W / 2, y, pr(t, ta, .3), i % 2 ? .06 : -.08, 100, i === 1 ? ROUGE : OR);
      S.texte(lab, W / 2, y + 125, { taille: 40, coul: CREME, esp: 6 });
    });
  }

  return { krach, monde, chrono, copie2, canaux, circuit, banque, taux, lingots, tarif, commerce, nue, preuves };
};

// sons propres à ces plans (discrets ; la copie a déjà ses sons de stylo)
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'krach') L.push([p.a + .9, 'drop', .7]);
  if (p.type === 'monde') L.push([p.a, 'whoosh', .5]);
  if (p.type === 'chrono') for (let k = 0; k < Math.floor((p.b - p.a) / .5); k++) L.push([p.a + k * .5, 'tic', .4]);
  if (p.type === 'canaux') [0, 1, 2].forEach(i => L.push([p.r ? tps(p.r[i]) : p.a + .35 + i * .3, 'blip', .4]));
  if (p.type === 'circuit') L.push([p.a, 'whoosh', .45]);
  if (p.type === 'banque' && p.faillite) L.push([p.a + .05, 'tampon', 1]);
  if (p.type === 'taux') L.push([p.monte ? tps(p.monte) : p.a + .6, 'montee', .5]);
  if (p.type === 'lingots') L.push([p.a + .1, 'whoosh', .5]);
  if (p.type === 'tarif') L.push([p.a + .45, 'frappe', .7]);
  if (p.type === 'nue') L.push([p.x ? tps(p.x) : p.a + .6, 'buzz', .55]);
  if (p.type === 'preuves') (p.r || [p.a + .3, p.a + .8, p.a + 1.3]).forEach(a => L.push([tps(a) + .05, 'tampon', .7]));
};
