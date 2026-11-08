// Plans propres au short Pearl Harbor (« Personne ne te croit »), dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
// L'écran du radar est un « A-scope » (une ligne horizontale, l'écho est un pic), comme celui de la station SCR-270 d'Opana.
window.SANS_ST_A = ['reponse', 'radio', 'bach', 'declare', 'bilan'];
window.PROPRES_A = ['ascope', 'heure', 'ile', 'colline', 'vol', 'telephone', 'reponse', 'b17', 'attaque', 'japonais', 'radio',
  'bilan', 'declare', 'globe', 'bach'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const milliers = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');

  // avion vu de dessus (nez vers le haut), centre (x, y), envergure ~ 2s ; marque : 'jp' (disques rouges), 'us' (étoile), rien
  function avion(x, y, s, rot, o = {}) {
    g.save(); g.translate(x, y); g.rotate(rot); g.scale(s / 100, s / 100);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || CREME; g.lineWidth = o.ep || 7; g.lineJoin = 'round';
    g.beginPath();
    g.moveTo(0, -95); g.quadraticCurveTo(14, -80, 14, -40);       // nez, fuselage droit
    g.lineTo(100, -18); g.lineTo(100, 4); g.lineTo(14, 8);         // aile droite
    g.lineTo(10, 70); g.lineTo(42, 82); g.lineTo(42, 94); g.lineTo(0, 92);   // empennage droit
    g.lineTo(-42, 94); g.lineTo(-42, 82); g.lineTo(-10, 70);       // empennage gauche
    g.lineTo(-14, 8); g.lineTo(-100, 4); g.lineTo(-100, -18); g.lineTo(-14, -40);   // aile gauche
    g.quadraticCurveTo(-14, -80, 0, -95); g.closePath(); g.fill(); g.stroke();
    if (o.moteurs) [-72, -40, 40, 72].forEach(dx => { g.fillStyle = o.trait || CREME; g.fillRect(dx - 6, -36, 12, 22); });
    if (o.marque === 'jp') [-62, 62].forEach(dx => { g.fillStyle = ROUGE; g.beginPath(); g.arc(dx, -7, 13, 0, 7); g.fill(); });
    if (o.marque === 'us') [-62, 62].forEach(dx => { g.fillStyle = CREME; g.beginPath(); g.arc(dx, -7, 13, 0, 7); g.fill();
      g.fillStyle = '#16120e'; g.beginPath(); for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, r = i % 2 ? 4.5 : 11; g.lineTo(dx + Math.cos(a) * r, -7 + Math.sin(a) * r); } g.closePath(); g.fill(); });
    g.restore();
  }
  // cuirassé de profil, (x, y) = ligne de flottaison au centre
  function cuirasse(x, y, s, feu, t) {
    g.save(); g.translate(x, y); g.scale(s, s);
    g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 4;
    g.beginPath(); g.moveTo(-170, 0); g.lineTo(-150, -26); g.lineTo(150, -26); g.lineTo(185, -4); g.lineTo(170, 0); g.closePath(); g.fill(); g.stroke();
    g.fillRect(-70, -60, 120, 34); g.strokeRect(-70, -60, 120, 34);
    g.fillRect(-20, -110, 30, 50); g.strokeRect(-20, -110, 30, 50);
    [[-120, -34], [100, -34]].forEach(([cx, cy]) => { g.beginPath(); g.rect(cx - 22, cy - 10, 44, 18); g.fill(); g.stroke(); g.beginPath(); g.moveTo(cx + 20, cy - 2); g.lineTo(cx + 62, cy - 6); g.stroke(); });
    if (feu) {
      for (let i = 0; i < 8; i++) { const ph = ((t * .35 + i / 8) % 1); g.fillStyle = `rgba(70,62,52,${.7 * (1 - ph)})`;
        g.beginPath(); g.arc(-10 + Math.sin(i * 3 + t) * 20 + ph * 60, -110 - ph * 360, 26 + ph * 70, 0, 7); g.fill(); }
      for (let i = 0; i < 6; i++) { const h = 30 + rnd(i + Math.floor(t * 14)) * 40; g.fillStyle = i % 2 ? OR : ROUGE;
        g.beginPath(); g.moveTo(-60 + i * 22, -26); g.quadraticCurveTo(-50 + i * 22, -26 - h, -40 + i * 22, -26); g.fill(); }
    }
    g.restore();
  }

  // écran du radar (A-scope) : etat 'veille' (bruit), 'echo' (le pic monte à p.pic), 'gros', 'suit' (le pic se rapproche),
  // 'perdu' (le pic s'éteint), 'fin' (boucle)
  function ascope(p, t) {
    const X0 = 130, X1 = 950, Y = 1010, km = x => (x - X0) / (X1 - X0) * 250, xk = k => X0 + k / 250 * (X1 - X0);
    g.fillStyle = '#1f1a14'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(70, 470, 940, 760, 40); g.fill(); g.stroke();
    g.fillStyle = '#080706'; g.beginPath(); g.roundRect(105, 540, 870, 560, 26); g.fill();
    g.strokeStyle = 'rgba(217,180,90,.13)'; g.lineWidth = 2;
    for (let k = 0; k <= 250; k += 25) { g.beginPath(); g.moveTo(xk(k), 560); g.lineTo(xk(k), 1080); g.stroke(); }
    for (let y = 600; y < 1080; y += 80) { g.beginPath(); g.moveTo(115, y); g.lineTo(965, y); g.stroke(); }
    S.texte('RADAR · 7 DÉC. 1941', 120, 505, { taille: 26, police: 'JetBrains Mono', poids: 500, coul: GRIS, align: 'left' });
    S.texte('NORD D’OAHU', 960, 505, { taille: 26, police: 'JetBrains Mono', poids: 500, coul: GRIS, align: 'right' });
    [0, 50, 100, 150, 200, 250].forEach(k => S.texte(String(k), xk(k), 1140, { taille: 26, police: 'JetBrains Mono', poids: 500, coul: CREME }));
    S.texte('DISTANCE (KM)', W / 2, 1190, { taille: 24, police: 'JetBrains Mono', poids: 500, coul: GRIS, esp: 4 });
    const e = p.etat || 'veille', lt = t - p.a;
    let pos = 220, amp = 0, w = 6;
    if (e === 'echo') amp = 330 * eo(pr(t, p.pic ? tps(p.pic) : p.a + .15, .5));
    if (e === 'gros') { amp = 380 + Math.sin(lt * 9) * 18; w = 9; }
    if (e === 'suit') { pos = lerp(205, 95, cl(lt / 2.6)); amp = 370; w = 8; }
    if (e === 'perdu') { pos = 45; amp = 360 * (1 - pr(t, p.a + .05, .55)); w = 8; }
    if (e === 'fin') { amp = 360 + Math.sin(lt * 7) * 20; w = 9; }
    g.save(); g.strokeStyle = OR; g.shadowColor = OR; g.shadowBlur = 16; g.lineWidth = 4; g.beginPath();
    for (let x = X0; x <= X1; x += 3) {
      const k = km(x); let v = (rnd(x * .37 + Math.floor(t * 24) * 13) - .5) * 16;
      v -= 440 * Math.exp(-(((k - 3) / 3.5) ** 2));                                        // impulsion émise
      v -= 70 * Math.exp(-(((k - 22) / 13) ** 2)) * (.7 + .3 * rnd(Math.floor(t * 10) + x));  // échos du relief
      v -= amp * Math.exp(-(((k - pos) / w) ** 2)) * (.88 + .12 * Math.sin(t * 31));
      x === X0 ? g.moveTo(x, Y + v) : g.lineTo(x, Y + v);
    }
    g.stroke(); g.restore();
    if (amp > 120) {
      const x = xk(pos), y = Y - amp - 40;
      g.save(); g.strokeStyle = ROUGE; g.lineWidth = 5; g.beginPath(); g.moveTo(x - 40, y); g.lineTo(x - 40, y - 24); g.lineTo(x + 40, y - 24); g.lineTo(x + 40, y); g.stroke(); g.restore();
      S.texte('ÉCHO', x, y - 52, { taille: 34, coul: ROUGE, poids: 700 });
    }
    if (p.t) deux(p.t, 1385, p.taille || 105);
  }

  // horloge à aiguilles + heure écrite ; l'aiguille des minutes arrive sur p.m
  function heure(p, t) {
    const k = eo(pr(t, p.a, .55)), tot = p.h * 60 + lerp(p.m - 12, p.m, k);
    g.save(); g.translate(W / 2, 800);
    g.fillStyle = '#1b1712'; g.strokeStyle = CREME; g.lineWidth = 10; g.beginPath(); g.arc(0, 0, 300, 0, 7); g.fill(); g.stroke();
    for (let i = 0; i < 60; i++) { const a = i / 60 * 6.283, L = i % 5 ? 14 : 36; g.lineWidth = i % 5 ? 3 : 8; g.strokeStyle = i % 5 ? GRIS : CREME;
      g.beginPath(); g.moveTo(Math.sin(a) * 270, -Math.cos(a) * 270); g.lineTo(Math.sin(a) * (270 - L), -Math.cos(a) * (270 - L)); g.stroke(); }
    const ah = ((tot / 60) % 12) / 12 * 6.283, am = (tot % 60) / 60 * 6.283;
    g.lineCap = 'round'; g.strokeStyle = CREME; g.lineWidth = 18; g.beginPath(); g.moveTo(0, 0); g.lineTo(Math.sin(ah) * 150, -Math.cos(ah) * 150); g.stroke();
    g.strokeStyle = OR; g.lineWidth = 11; g.beginPath(); g.moveTo(0, 0); g.lineTo(Math.sin(am) * 235, -Math.cos(am) * 235); g.stroke();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 18, 0, 7); g.fill();
    g.restore();
    const kt = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1255); g.scale(kt, kt);
    S.texte(`${p.h} H ${String(p.m).padStart(2, '0')}`, 0, 0, { taille: 190, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 }); g.restore();
    if (p.t) deux(p.t, 1450, 90);
  }

  // Oahu vu du ciel, nord en haut : le radar au nord, Pearl Harbor au sud ; p.fleche : l'écho au nord ; p.approche : il fonce sur l'île
  const OAHU = [[-.1, -1], [.22, -.78], [.5, -.3], [.88, .1], [.82, .42], [.95, .74], [.45, .8], [.12, .66], [.02, .74], [-.08, .64],
    [-.38, .62], [-.72, .56], [-.86, .12], [-.97, -.26], [-.6, -.58], [-.32, -.8]];
  function ile(p, t) {
    const cx = 560, cy = 1010, R = 250, P = ([x, y]) => [cx + x * R, cy + y * R * .95];
    g.strokeStyle = 'rgba(217,180,90,.12)'; g.lineWidth = 3;
    for (let i = 0; i < 9; i++) { g.beginPath(); for (let x = 0; x <= W; x += 20) { const y = 380 + i * 140 + Math.sin(x * .012 + t * 1.2 + i) * 10; x ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); }
    g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); OAHU.forEach((q, i) => { const [x, y] = P(q); i ? g.lineTo(x, y) : g.moveTo(x, y); }); g.closePath(); g.fill(); g.stroke();
    g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 4; g.beginPath(); g.moveTo(...P([-.75, .2])); g.lineTo(...P([-.5, -.55])); g.stroke();
    g.beginPath(); g.moveTo(...P([.1, -.6])); g.lineTo(...P([.75, .55])); g.stroke();
    // Pearl Harbor
    const [px, py] = P([.02, .6]); g.fillStyle = '#0d0b09'; g.beginPath(); g.ellipse(px, py, 34, 22, .2, 0, 7); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(px, py, 10, 0, 7); g.fill();
    S.texte('PEARL HARBOR', px, py + 70, { taille: 40, coul: OR, contour: NOIR, contourL: 6 });
    // le radar
    const [rx, ry] = P([-.1, -.95]); const pu = (t * 1.4) % 1;
    g.save(); g.strokeStyle = ROUGE; g.globalAlpha = 1 - pu; g.lineWidth = 5; g.beginPath(); g.arc(rx, ry, 16 + pu * 60, 0, 7); g.stroke(); g.restore();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(rx, ry, 13, 0, 7); g.fill();
    S.texte('RADAR', rx - 90, ry + 10, { taille: 34, coul: ROUGE, contour: NOIR, contourL: 6 });
    S.texte('N', 960, 400, { taille: 56, coul: CREME }); S.d.fleche(960, 520, 960, 440, 1, { trait: CREME, ep: 6 });
    S.texte('OAHU · HAWAÏ', cx + 120, cy + 300, { taille: 30, coul: GRIS, esp: 6, poids: 600 });
    if (p.fleche) {
      const u = p.approche ? eo(cl((t - p.a) / 2.4)) : 0, bx = rx + 10, by = lerp(330, ry - 150, u);
      g.save(); g.setLineDash([16, 14]); g.strokeStyle = 'rgba(200,55,45,.7)'; g.lineWidth = 4; g.beginPath(); g.moveTo(rx, ry); g.lineTo(bx, by); g.stroke(); g.restore();
      for (let i = 0; i < 7; i++) avion(bx + (i - 3) * 34, by - Math.abs(i - 3) * 26, 26, Math.PI, { fond: '#16120e', trait: ROUGE, ep: 9 });
      if (p.km && t >= tps(p.km) && !p.approche) { const k = back(pr(t, tps(p.km), .3)); g.save(); g.translate(bx + 250, (by + ry) / 2); g.scale(k, k);
        S.texte('+ 200 KM', 0, 0, { taille: 64, coul: ROUGE, contour: NOIR, contourL: 8 }); g.restore(); }
    }
    if (p.t) deux(p.t, 1440, 100);
    if (p.sous) S.texte(p.sous, W / 2, 1545, { taille: 60, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
  }

  // la colline à l'aube, l'antenne du radar qui tourne, le camion
  function colline(p, t) {
    const gr = g.createLinearGradient(0, 300, 0, 1300); gr.addColorStop(0, '#0d0b09'); gr.addColorStop(1, '#4a321c');
    g.fillStyle = gr; g.fillRect(0, 300, W, 1000);
    const gl = g.createRadialGradient(780, 1240, 20, 780, 1240, 420); gl.addColorStop(0, 'rgba(217,180,90,.55)'); gl.addColorStop(1, 'rgba(217,180,90,0)');
    g.fillStyle = gl; g.fillRect(0, 700, W, 600);
    g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-20, 1400); g.quadraticCurveTo(300, 1040, 540, 1060); g.quadraticCurveTo(820, 1080, 1100, 1300); g.lineTo(1100, 1450); g.lineTo(-20, 1450); g.closePath(); g.fill(); g.stroke();
    // mât et antenne (réseau de dipôles), qui tourne lentement
    g.beginPath(); g.moveTo(500, 1060); g.lineTo(540, 800); g.lineTo(580, 1060); g.stroke();
    const sx = Math.max(.12, Math.abs(Math.cos((t - p.a) * 1.1)));
    g.save(); g.translate(540, 720); g.scale(sx, 1);
    g.fillStyle = 'rgba(22,18,14,.9)'; g.fillRect(-190, -110, 380, 200); g.strokeRect(-190, -110, 380, 200);
    g.lineWidth = 3; for (let i = -150; i <= 150; i += 50) { g.beginPath(); g.moveTo(i, -100); g.lineTo(i, 80); g.stroke(); }
    for (let j = -80; j <= 60; j += 46) { g.beginPath(); g.moveTo(-180, j); g.lineTo(180, j); g.stroke(); }
    g.restore();
    // camion-abri
    g.lineWidth = 5; g.beginPath(); g.roundRect(700, 1010, 170, 80, 8); g.fill(); g.stroke();
    [[730, 1095], [840, 1095]].forEach(([x, y]) => { g.beginPath(); g.arc(x, y, 18, 0, 7); g.fill(); g.stroke(); });
    g.fillStyle = OR; g.fillRect(720, 1030, 34, 22);
    deux(p.t || 'UN RADAR|SUR UNE COLLINE', 1500, 100);
  }

  // des avions sans nom, de plus en plus nombreux (à p.n : beaucoup)
  function vol(p, t) {
    const lt = t - p.a, nmax = p.n && t >= tps(p.n) ? Math.floor(lerp(5, 30, cl((t - tps(p.n)) / .8))) : 5;
    for (let i = 0; i < nmax; i++) {
      const rang = Math.floor(Math.sqrt(i)), j = i - rang * rang, x = W / 2 + (j - rang) * 110 + (rnd(i) - .5) * 30, y = 520 + rang * 150 + lt * 40 + (rnd(i + 9) - .5) * 30;
      avion(x, y, 60 - rang * 4, Math.PI, { fond: '#16120e', trait: CREME, ep: 8 });
    }
    const beau = p.n && t >= tps(p.n);
    O.multi(beau ? [['BEAUCOUP ', CREME], ['D’AVIONS', OR]] : [['DES ', CREME], ['AVIONS', OR]], 1450, 130);
  }

  // le téléphone de campagne, qui sonne ; p.bulle : la réponse arrive
  function telephone(p, t) {
    const lt = t - p.a, vib = p.bulle ? 0 : Math.sin(lt * 60) * 4 * (Math.sin(lt * 6) > 0 ? 1 : 0);
    g.save(); g.translate(W / 2 + vib, 880);
    g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 7;
    g.beginPath(); g.moveTo(-230, 200); g.lineTo(-170, -10); g.lineTo(170, -10); g.lineTo(230, 200); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.arc(0, 90, 80, 0, 7); g.stroke(); for (let i = 0; i < 10; i++) { const a = i / 10 * 6.283; g.beginPath(); g.arc(Math.cos(a) * 55, 90 + Math.sin(a) * 55, 9, 0, 7); g.stroke(); }
    g.beginPath(); g.moveTo(-260, -60); g.quadraticCurveTo(-250, -150, -150, -150); g.lineTo(150, -150); g.quadraticCurveTo(250, -150, 260, -60);
    g.lineTo(200, -40); g.quadraticCurveTo(180, -90, 120, -95); g.lineTo(-120, -95); g.quadraticCurveTo(-180, -90, -200, -40); g.closePath(); g.fill(); g.stroke();
    g.restore();
    g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath(); for (let i = 0; i <= 40; i++) { const x = W / 2 + 230 + i * 6, y = 1060 + Math.sin(i * .9) * 18 + i * 3; i ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke();
    if (!p.bulle) for (let i = 0; i < 3; i++) { const k = ((lt * 1.6 + i / 3) % 1); g.save(); g.globalAlpha = 1 - k; g.strokeStyle = OR; g.lineWidth = 7;
      [-1, 1].forEach(s => { g.beginPath(); g.arc(W / 2, 820, 290 + k * 120, s > 0 ? -.5 : Math.PI - .5, s > 0 ? .5 : Math.PI + .5); g.stroke(); }); g.restore(); }
    else { const k = back(pr(t, p.a + .15, .3)); g.save(); g.translate(W / 2, 520); g.scale(k, k); g.fillStyle = CREME; g.beginPath(); g.roundRect(-220, -80, 440, 160, 50); g.fill();
      g.beginPath(); g.moveTo(-30, 75); g.lineTo(10, 140); g.lineTo(40, 75); g.fill(); S.texte('…', 0, -10, { taille: 120, coul: NOIR }); g.restore(); }
    if (p.t) deux(p.t, 1440, 105);
  }

  // la réponse du lieutenant, tapée à la machine
  function reponse(p, t) {
    const txt = p.t, d = p.duree || .9, n = Math.floor(cl((t - p.a) / d) * txt.length);
    S.texte('LE LIEUTENANT', W / 2, 700, { taille: 36, coul: GRIS, esp: 8 });
    S.texte('« ' + txt.slice(0, n) + (n >= txt.length ? ' »' : ''), W / 2, 920, { taille: 100, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 980 });
    const k = eo(pr(t, p.a + d, .35)); O.barreRouge(1030, k, 12, -.02);
    g.save(); g.globalAlpha = k; S.texte(p.en || '“Don’t worry about it.”', W / 2, 1140, { taille: 52, police: 'Spectral', it: true, poids: 400, coul: GRIS }); g.restore();
  }

  // ce que croit le lieutenant : des B-17 américains
  function b17(p, t) {
    const lt = t - p.a;
    [[540, 760, 120], [330, 940, 95], [750, 940, 95]].forEach(([x, y, s], i) => avion(x, y - lt * 30, s, 0, { fond: '#3a3328', trait: CREME, ep: 6, moteurs: true, marque: 'us' }));
    O.multi([['DES ', CREME], ['B-17 AMÉRICAINS', OR]], 1330, 110);
    S.texte('c’est ce qu’il croit', W / 2, 1450, { taille: 64, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
  }

  // l'attaque : avions en piqué, cuirassés, explosions
  function attaque(p, t) {
    const lt = t - p.a;
    g.fillStyle = '#16120e'; g.fillRect(0, 1180, W, 260);
    [[250, 1180, .9], [620, 1185, 1.0], [930, 1180, .8]].forEach(([x, y, s], i) => cuirasse(x, y, s, lt > .45 + i * .3, t));
    for (let i = 0; i < 5; i++) {
      const k = cl((lt - i * .18) / 1.1), x0 = -80 + i * 140, y0 = 280 + i * 40, x1 = 220 + i * 170, y1 = 1050;
      if (k <= 0 || k >= 1) continue;
      const x = lerp(x0, x1, k), y = lerp(y0, y1, k);
      g.save(); g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 4; g.beginPath(); g.moveTo(x0, y0); g.lineTo(x, y); g.stroke(); g.restore();
      avion(x, y, 42, Math.atan2(y1 - y0, x1 - x0) + Math.PI / 2, { fond: '#16120e', trait: CREME, ep: 9, marque: 'jp' });
    }
    [.5, .85, 1.2, 1.5].forEach((c, i) => { const k = pr(t, p.a + c, .45); if (k > 0 && k < 1) { g.save(); g.globalAlpha = 1 - k; g.fillStyle = i % 2 ? OR : '#fff3c4';
      g.beginPath(); g.arc(220 + i * 230, 1150, 40 + k * 160, 0, 7); g.fill(); g.restore(); } });
    O.multi([['PEARL ', CREME], ['HARBOR', OR]], 1560, 130);
  }

  // révélation : un avion japonais
  function japonais(p, t) {
    const k = eo(pr(t, p.a, .4));
    avion(W / 2, 800, lerp(150, 330, k), -.12 + Math.sin(t * 2) * .03, { fond: '#2a241d', trait: CREME, ep: 4, marque: 'jp' });
    deux('ILS SONT|JAPONAIS', 1400, 135);
  }

  // le message radio, avec sa traduction au fil de la voix
  function radio(p, t) {
    O.petitTitre('— MESSAGE AUTHENTIQUE · 7 H 55 —', 470, ROUGE);
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1300, 920, k)); g.rotate(-.02);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#e9dfc8'; g.fillRect(-460, -360, 920, 720); g.shadowColor = 'transparent';
    g.strokeStyle = NOIR; g.lineWidth = 3; g.strokeRect(-430, -330, 860, 660);
    S.texte('RADIO · NAVY · HAWAII', 0, -280, { taille: 30, police: 'JetBrains Mono', poids: 500, coul: GRIS, esp: 4 });
    const tape = (s, ta, y, c, d = .7) => { const n = Math.floor(cl((t - ta) / d) * s.length); S.texte(s.slice(0, n), 0, y, { taille: 70, police: 'JetBrains Mono', poids: 500, coul: c, max: 820 }); };
    tape('AIR RAID', p.a + .1, -170, NOIR, .35); tape('PEARL HARBOR', p.a + .45, -80, NOIR, .45);
    const f1 = tps(p.fr1); if (t >= f1) { g.save(); g.globalAlpha = eo(pr(t, f1, .3)); S.texte('raid aérien sur Pearl Harbor', 0, 0, { taille: 48, police: 'Spectral', it: true, poids: 400, coul: GRIS }); g.restore(); }
    const l2 = tps(p.l2); if (t >= l2) { tape('THIS IS NOT DRILL', l2, 130, ROUGE, .55);
      g.save(); g.globalAlpha = eo(pr(t, l2 + .4, .3)); S.texte('ceci n’est pas un exercice', 0, 220, { taille: 52, police: 'Spectral', it: true, poids: 600, coul: ROUGE }); g.restore(); }
    g.restore();
  }

  // le bilan : cuirassés en feu, compteur
  function bilan(p, t) {
    g.fillStyle = '#16120e'; g.fillRect(0, 980, W, 120);
    [[230, 980, .85], [600, 985, 1], [920, 980, .8]].forEach(([x, y, s]) => cuirasse(x, y, s, true, t));
    const tn = tps(p.n), n = Math.round(lerp(0, 2400, eo(pr(t, tn, .9))));
    S.texte('PLUS DE', W / 2, 1180, { taille: 60, coul: CREME, esp: 8 });
    S.texte(milliers(n), W / 2, 1330, { taille: 220, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 14 });
    S.texte('MORTS AMÉRICAINS', W / 2, 1480, { taille: 70, coul: CREME, contour: NOIR, contourL: 8 });
  }

  // les déclarations de guerre : etape 1, le 8 décembre ; etape 2, le 11 décembre (photo : Hitler au Reichstag)
  function declare(p, t) {
    const e2 = p.etape === 2;
    if (e2) O.fondImg('reichstag', 1.2, .5, .45, .4);
    O.petitTitre(e2 ? '— 11 DÉCEMBRE 1941 —' : '— 8 DÉCEMBRE 1941 —', 520);
    const boite = (s, y, k, c) => { g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(.7, 1, eo(k)), lerp(.7, 1, eo(k)));
      g.fillStyle = '#1b1712'; g.strokeStyle = c; g.lineWidth = 6; g.beginPath(); g.roundRect(-400, -85, 800, 170, 20); g.fill(); g.stroke();
      S.texte(s, 0, 4, { taille: 76, coul: c, max: 740 }); g.restore(); };
    boite(e2 ? 'ALLEMAGNE · ITALIE' : 'ÉTATS-UNIS', 700, pr(t, p.a, .3), CREME);
    S.d.fleche(W / 2, 800, W / 2, 960, eo(pr(t, p.a + .25, .3)), { trait: ROUGE, ep: 14 });
    boite(e2 ? 'ÉTATS-UNIS' : 'JAPON', 1070, pr(t, p.a + .45, .3), OR);
    O.tampon('GUERRE', W / 2 + 160, 880, pr(t, p.a + .7, .3), -.12, 96);
    if (e2) S.texte('Hitler au Reichstag, 11 décembre 1941', W / 2, 1640, { taille: 34, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    O.multi(e2 ? [['L’AXE ', CREME], ['ENTRE EN GUERRE', OR]] : [['ILS ', CREME], ['ENTRENT EN GUERRE', OR]], 1340, 100);
    if (e2) S.texte('contre les États-Unis', W / 2, 1450, { taille: 60, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
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

  // copie du sujet (histoire)
  function bach(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 900, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-380, -480, 760, 960); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
    S.texte('HISTOIRE-GÉOGRAPHIE', 0, -315, { taille: 40, coul: GRIS, esp: 6, poids: 600, max: 680 });
    g.fillStyle = NOIR; g.fillRect(-300, -260, 600, 3);
    S.texte('Question problématisée', -300, -180, { taille: 40, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400 });
    S.texte(p.sujet[0], 0, -80, { taille: 64, police: 'Spectral', poids: 600, coul: NOIR, max: 680 });
    S.texte(p.sujet[1], 0, 10, { taille: 64, police: 'Spectral', poids: 600, coul: NOIR, max: 680 });
    for (let i = 0; i < 6; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-300, 120 + i * 50, 600 - (i === 5 ? 250 : 0), 6); }
    const kc = pr(t, p.a + .35, .5); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(0, -35, 360, 130, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['SUJET TYPE ', CREME], ['BAC', ROUGE]], 1560, 110);
  }

  return { ascope, heure, ile, colline, vol, telephone, reponse, b17, attaque, japonais, radio, bilan, declare, globe, bach };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'ascope') {
    L.push([p.a, 'bip', .3]);
    if (p.etat === 'echo') L.push([p.pic ? tps(p.pic) : p.a + .15, 'blip', .6]);
    if (p.etat === 'gros' || p.etat === 'fin') L.push([p.a + .1, 'coeur', .7]);
    if (p.etat === 'suit') for (let k = 0; k < 4; k++) L.push([p.a + .2 + k * .6, 'blip', .35]);
    if (p.etat === 'perdu') L.push([p.a, 'statique', .4]);
  }
  if (p.type === 'heure') for (let k = 0; k < 6; k++) L.push([p.a + k * .09, 'tic', .45]);
  if (p.type === 'ile') { L.push([p.a, 'frotte', .25]); if (p.km) L.push([tps(p.km), 'blip', .5]); if (p.approche) L.push([p.a, 'montee', .4]); }
  if (p.type === 'colline') L.push([p.a, 'souffle', .35]);
  if (p.type === 'vol') { L.push([p.a, 'souffle', .45]); if (p.n) L.push([tps(p.n), 'montee', .4]); }
  if (p.type === 'b17') L.push([p.a, 'souffle', .4]);
  if (p.type === 'telephone') { if (p.bulle) L.push([p.a + .15, 'pop', .5]); else L.push([p.a, 'bip', .45], [p.a + .35, 'bip', .45]); }
  if (p.type === 'reponse') { const n = p.t.length, d = p.duree || .9; for (let k = 0; k < n; k += 2) L.push([p.a + d * k / n, 'tic', .3]); L.push([p.a + d + .05, 'lame', .6]); }
  if (p.type === 'attaque') L.push([p.a, 'whoosh', .6], [p.a + .5, 'boum', .7], [p.a + .85, 'boum', .5], [p.a + 1.2, 'boum', .6]);
  if (p.type === 'radio') { L.push([p.a, 'statique', .35]); for (let k = 0; k < 10; k++) L.push([p.a + .1 + k * .08, 'tic', .3]); for (let k = 0; k < 7; k++) L.push([tps(p.l2) + k * .08, 'tic', .35]); }
  if (p.type === 'bilan') L.push([tps(p.n), 'montee', .4]);
  if (p.type === 'declare') L.push([p.a + .72, 'tampon', .9]);
  if (p.type === 'bach') L.push([p.a + .35, 'stylo', .6]);
};
