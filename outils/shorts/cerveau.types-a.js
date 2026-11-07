// Plans propres au short « cerveau » (le cerveau divisé, patient P.S.), dans le style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Code couleur constant : cerveau gauche (celui qui parle) = or, cerveau droit (muet) = rouge.
window.SANS_ST_A = ['reponse', 'trio', 'interprete', 'croise'];
window.PROPRES_A = ['mains', 'crise', 'dessus', 'fibres', 'separe', 'nom', 'ecran', 'croise', 'voit', 'cartes', 'muet', 'reponse', 'interprete', 'trio'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const PEAU = '#d8b48c', SOMBRE = '#1b1712';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (t, a, d = .3) => back(pr(t, a, d));

  // ------------------------------------------------------------ petits dessins
  // patte de poulet : trois doigts vers le bas, un ergot
  function patte(x, y, s, coul) {
    g.save(); g.translate(x, y); g.scale(s / 100, s / 100); g.strokeStyle = coul; g.lineWidth = 12; g.lineCap = 'round'; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(0, -80); g.lineTo(0, 10); g.stroke();
    [[-60, 70], [0, 85], [60, 70]].forEach(([dx, dy]) => { g.beginPath(); g.moveTo(0, 10); g.quadraticCurveTo(dx * .4, dy * .5, dx, dy); g.stroke(); });
    g.beginPath(); g.moveTo(0, -10); g.lineTo(-32, -28); g.stroke();
    g.restore();
  }
  // paysage de neige : collines, sapin, flocons
  function neige(x, y, s, coul, t = 0) {
    g.save(); g.translate(x, y); g.scale(s / 100, s / 100); g.strokeStyle = coul; g.fillStyle = coul; g.lineWidth = 8; g.lineCap = 'round';
    g.beginPath(); g.moveTo(-95, 60); g.quadraticCurveTo(-40, 10, 10, 45); g.quadraticCurveTo(55, 15, 95, 50); g.stroke();
    g.beginPath(); g.moveTo(40, -55); g.lineTo(5, 20); g.lineTo(75, 20); g.closePath(); g.stroke();
    g.beginPath(); g.moveTo(40, 20); g.lineTo(40, 34); g.stroke();
    for (let i = 0; i < 7; i++) { const fx = -85 + rnd(i * 3.1) * 110, fy = -80 + ((rnd(i * 7.7) * 120 + t * 40) % 120);
      g.beginPath(); g.arc(fx, fy, 6, 0, 7); g.fill(); }
    g.restore();
  }
  function poulet(x, y, s, coul) {
    g.save(); g.translate(x, y); g.scale(s / 100, s / 100); g.strokeStyle = coul; g.lineWidth = 8; g.lineJoin = 'round'; g.lineCap = 'round';
    g.beginPath(); g.ellipse(-5, 15, 62, 45, -.15, 0, 7); g.stroke();
    g.beginPath(); g.arc(48, -38, 24, 0, 7); g.stroke();
    g.fillStyle = ROUGE; g.beginPath(); g.moveTo(36, -60); g.lineTo(44, -78); g.lineTo(52, -62); g.lineTo(62, -74); g.lineTo(64, -56); g.closePath(); g.fill();
    g.fillStyle = OR; g.beginPath(); g.moveTo(70, -40); g.lineTo(92, -33); g.lineTo(70, -28); g.closePath(); g.fill();
    g.beginPath(); g.moveTo(-62, 0); g.quadraticCurveTo(-95, -30, -80, -50); g.stroke();
    [[-20, 58], [15, 58]].forEach(([lx, ly]) => { g.beginPath(); g.moveTo(lx, ly); g.lineTo(lx, ly + 32); g.lineTo(lx + 14, ly + 36); g.stroke(); });
    g.restore();
  }
  function pelle(x, y, s, coul) {
    g.save(); g.translate(x, y); g.scale(s / 100, s / 100); g.strokeStyle = coul; g.lineWidth = 9; g.lineJoin = 'round'; g.lineCap = 'round';
    g.beginPath(); g.moveTo(0, -95); g.lineTo(0, 15); g.stroke();
    g.beginPath(); g.moveTo(-22, -95); g.lineTo(22, -95); g.stroke();
    g.beginPath(); g.moveTo(-42, 15); g.lineTo(42, 15); g.lineTo(36, 85); g.quadraticCurveTo(0, 100, -36, 85); g.closePath(); g.stroke();
    g.restore();
  }
  function poulailler(x, y, s, coul) {
    g.save(); g.translate(x, y); g.scale(s / 100, s / 100); g.strokeStyle = coul; g.lineWidth = 8; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(-80, -10); g.lineTo(0, -80); g.lineTo(80, -10); g.stroke();
    g.strokeRect(-65, -10, 130, 90);
    g.beginPath(); g.moveTo(-18, 80); g.lineTo(-18, 25); g.quadraticCurveTo(0, 5, 18, 25); g.lineTo(18, 80); g.stroke();
    g.restore();
  }
  const ICONES = { patte, neige, poulet, pelle, poulailler };
  // carte posée : fond crème, dessin noir ; dos = motif
  function carteDessin(nom, x, y, w, h, rot, o = {}) {
    g.save(); g.translate(x, y); g.rotate(rot);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 30; g.shadowOffsetY = 12;
    g.fillStyle = o.dos ? '#3a2f25' : CREME; g.beginPath(); g.roundRect(-w / 2, -h / 2, w, h, 16); g.fill(); g.shadowColor = 'transparent';
    g.strokeStyle = o.bord || (o.dos ? OR : NOIR); g.lineWidth = o.bord ? 10 : 4; g.stroke();
    if (o.dos) { g.strokeStyle = 'rgba(217,180,90,.4)'; g.lineWidth = 3; for (let i = -6; i < 7; i++) { g.beginPath(); g.moveTo(-w / 2 + 14, i * 40); g.lineTo(w / 2 - 14, i * 40 + 60); g.stroke(); } }
    else ICONES[nom](0, -10, w * .62, NOIR);
    if (o.nom) S.texte(o.nom, 0, h / 2 - 34, { taille: 30, coul: NOIR, esp: 4 });
    g.restore();
  }
  // bras qui sort du bas de l'image et pointe un doigt vers (x1, y1)
  function bras(x0, y0, x1, y1, k, coul = PEAU) {
    if (k <= 0) return;
    const x = lerp(x0, x1, k), y = lerp(y0, y1, k), a = Math.atan2(y - y0, x - x0);
    g.save(); g.lineCap = 'round';
    g.strokeStyle = NOIR; g.lineWidth = 128; g.beginPath(); g.moveTo(x0, y0); g.lineTo(x, y); g.stroke();
    g.strokeStyle = coul; g.lineWidth = 112; g.beginPath(); g.moveTo(x0, y0); g.lineTo(x, y); g.stroke();
    const fx = x + Math.cos(a) * 95, fy = y + Math.sin(a) * 95;
    g.strokeStyle = NOIR; g.lineWidth = 46; g.beginPath(); g.moveTo(x, y); g.lineTo(fx, fy); g.stroke();
    g.strokeStyle = coul; g.lineWidth = 32; g.beginPath(); g.moveTo(x, y); g.lineTo(fx, fy); g.stroke();
    g.restore();
  }
  // bulle de pensée ronde avec une icône
  function bulle(nom, x, y, r, k, coul, t) {
    if (k <= 0) return;
    g.save(); g.translate(x, y); g.scale(k, k);
    g.fillStyle = CREME; g.strokeStyle = coul; g.lineWidth = 8;
    g.beginPath(); g.arc(0, 0, r, 0, 7); g.fill(); g.stroke();
    [[0, r + 34, 16], [0, r + 70, 10]].forEach(([cx, cy, rr]) => { g.beginPath(); g.arc(cx, cy, rr, 0, 7); g.fill(); g.stroke(); });
    ICONES[nom](0, 0, r * 1.15, NOIR, t);
    g.restore();
  }

  // cerveau vu de dessus : deux moitiés, le corps calleux (le « pont ») entre les deux
  // o : ecart (px), pont (lueur 0..1), coupe (0..1), hg / hd (surbrillance des moitiés 0..1), lab, gris (moitié éteinte 'g' ou 'd')
  function dessus(cx, cy, s, o = {}) {
    const e = o.ecart || 0, rx = s * .5, ry = s * .72, cut = o.coupe || 0, gap = cut >= 1 ? 22 : 0, ph = s * .2, pw = s * .24;
    [-1, 1].forEach(sd => {
      const x = cx + sd * (s * .56 + e), h = sd < 0 ? (o.hg || 0) : (o.hd || 0), coul = sd < 0 ? OR : ROUGE;
      const eteint = (o.gris === 'g' && sd < 0) || (o.gris === 'd' && sd > 0);
      g.save(); g.globalAlpha = eteint ? .35 : 1;
      g.fillStyle = SOMBRE; g.strokeStyle = h > 0 ? coul : CREME; g.lineWidth = 9;
      if (h > 0) { g.shadowColor = coul; g.shadowBlur = 50 * h; }
      g.beginPath(); g.ellipse(x, cy, rx, ry, 0, 0, 7); g.fill(); g.stroke(); g.shadowBlur = 0;
      if (h > 0) { g.globalAlpha = (eteint ? .35 : 1) * .22 * h; g.fillStyle = coul; g.fill(); g.globalAlpha = eteint ? .35 : 1; }
      // circonvolutions
      g.save(); g.beginPath(); g.ellipse(x, cy, rx - 12, ry - 12, 0, 0, 7); g.clip();
      g.strokeStyle = h > 0 ? coul : 'rgba(239,230,210,.55)'; g.lineWidth = 5; g.lineCap = 'round';
      for (let i = 0; i < 9; i++) { const yy = cy - ry + 40 + i * (ry * 2 - 80) / 8; g.beginPath(); g.moveTo(x - rx, yy);
        for (let k = 1; k <= 6; k++) g.quadraticCurveTo(x - rx + (k - .5) * rx / 3, yy + (rnd(i * 13 + k + (sd > 0 ? 50 : 0)) - .5) * 50, x - rx + k * rx / 3, yy + (rnd(i * 7 + k) - .5) * 20);
        g.stroke(); }
      g.restore();
      g.restore();
      if (o.lab) S.texte(sd < 0 ? 'GAUCHE' : 'DROIT', x, cy + ry + 55, { taille: 46, coul: h > 0 ? coul : CREME, esp: 6, contour: NOIR, contourL: 8 });
    });
    // pont (corps calleux) : bande dessinée par-dessus, à cheval sur le milieu
    
    [-1, 1].forEach(sd => {
      g.save(); g.fillStyle = OR; g.globalAlpha = .55 + .45 * (o.pont || 0);
      if (o.pont) { g.shadowColor = OR; g.shadowBlur = 40 * o.pont; }
      const xi = cx + sd * (gap / 2 + e), xe = cx + sd * (pw + e);
      g.fillRect(Math.min(xi, xe), cy - ph / 2, Math.abs(xe - xi), ph);
      g.shadowBlur = 0; g.strokeStyle = NOIR; g.lineWidth = 3;
      for (let i = 1; i < 6; i++) { const yy = cy - ph / 2 + i * ph / 6; g.beginPath(); g.moveTo(xi, yy); g.lineTo(xe, yy); g.stroke(); }
      g.restore();
    });
    // coupe : trait rouge qui descend au milieu
    if (cut > 0 && cut < 1.4) { g.save(); g.strokeStyle = ROUGE; g.lineWidth = 12; g.lineCap = 'round'; g.shadowColor = ROUGE; g.shadowBlur = 30; g.globalAlpha = cl((1.4 - cut) / .4);
      g.beginPath(); g.moveTo(cx, cy - ph * 1.6); g.lineTo(cx, cy - ph * 1.6 + Math.min(1, cut) * ph * 3.2); g.stroke(); g.restore(); }
  }

  // ------------------------------------------------------------ plans
  // s1 et fin : deux cartes, la main gauche prend la pelle (p.etape 'prend') ou hésite au-dessus (p.etape 'hesite')
  function mains(p, t) {
    const lt = t - p.a;
    let lev = 0, k;
    if (p.etape === 'prend') { k = eo(pr(t, p.a + .1, .7)); lev = eo(pr(t, p.a + .9, .4)); }
    else k = .82 + Math.sin(lt * 4) * .06;
    carteDessin('pelle', 330, 820 - lev * 120, 300, 400, -.05 - lev * .1, { nom: 'PELLE', bord: lev > 0 ? ROUGE : null });
    carteDessin('poulet', 750, 820, 300, 400, .04, { nom: 'POULET' });
    bras(150, 1900, 330, 900 - lev * 120, k);
    if (p.etape === 'hesite') S.texte('?', 560, 560, { taille: 200, coul: OR, contour: NOIR, contourL: 12 });
    deux(p.t, 1330, 100);
  }

  // l'épilepsie : éclairs qui traversent les deux moitiés
  function crise(p, t) {
    const f = Math.floor(t * 14);
    dessus(W / 2, 880, 330, { hg: rnd(f) > .5 ? .6 : 0, hd: rnd(f + 3) > .5 ? .6 : 0 });
    g.save(); g.lineCap = 'round'; g.lineJoin = 'round';
    for (let e = 0; e < 3; e++) { if (rnd(f * 5 + e) < .35) continue;
      g.strokeStyle = e % 2 ? '#fff3c4' : ROUGE; g.lineWidth = 9; g.shadowColor = g.strokeStyle; g.shadowBlur = 30;
      let x = 230 + rnd(f + e * 9) * 120, y = 650 + rnd(f * 2 + e) * 450; g.beginPath(); g.moveTo(x, y);
      for (let s = 0; s < 7; s++) { x += 70 + rnd(f + s + e * 11) * 30; y += (rnd(f * 3 + s + e) - .5) * 160; g.lineTo(x, y); } g.stroke(); }
    g.restore();
    if (rnd(f * 7) > .7) { g.save(); g.globalAlpha = .12; g.fillStyle = '#fff6d8'; g.fillRect(0, 0, W, H); g.restore(); }
    deux(p.t, 1400, 120);
  }

  // le corps calleux : lueur, étiquette, puis la coupe (p.coupe = repère) ; p.mode 'pont' : pont déjà coupé + texte
  function dessusPlan(p, t) {
    const kc = p.coupe ? pr(t, tps(p.coupe), .35) : (p.mode === 'pont' ? 1 : 0);
    const kz = p.mode === 'pont' ? lerp(1, 1.25, eo(pr(t, p.a, .8))) : 1;
    g.save(); g.translate(W / 2, 880); g.scale(kz, kz); g.translate(-W / 2, -880);
    dessus(W / 2, 880, 330, { pont: p.mode === 'pont' ? .4 + .3 * Math.sin((t - p.a) * 6) : 1 - kc * .6, coupe: kc, lab: p.mode !== 'pont' });
    g.restore();
    if (p.mode !== 'pont') {
      const k = eo(pr(t, p.a + .1, .35));
      g.save(); g.globalAlpha = k; g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.moveTo(W / 2, 830); g.lineTo(W / 2, 520); g.stroke(); g.restore();
      const kk = pop(t, p.a + .1);
      g.save(); g.translate(W / 2, 470); g.scale(kk, kk); S.texte('CORPS CALLEUX', 0, 0, { taille: 92, coul: OR, contour: NOIR, contourL: 10 }); g.restore();
      if (kc > 0) { const ks = pop(t, tps(p.coupe) + .2); g.save(); g.translate(W / 2, 1420); g.scale(ks, ks); g.rotate(-.06);
        S.texte('COUPÉ', 0, 0, { taille: 170, coul: ROUGE, contour: NOIR, contourL: 14 }); g.restore(); }
    } else deux(p.t, 1440, 110);
  }

  // gros plan sur les fibres du pont, tranchées d'un coup
  function fibres(p, t) {
    const kc = pr(t, p.a + .1, .2), ret = eo(pr(t, p.a + .3, .5));
    g.save(); g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 9;
    g.beginPath(); g.ellipse(-60, 900, 330, 520, 0, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.ellipse(W + 60, 900, 330, 520, 0, 0, 7); g.fill(); g.stroke(); g.restore();
    for (let i = 0; i < 24; i++) {
      const y = 660 + i * 20, ond = (x, d) => y + Math.sin(x * .02 + i) * 8 + d;
      g.save(); g.strokeStyle = i % 4 ? OR : '#f3d98c'; g.lineWidth = 6; g.globalAlpha = .9;
      if (kc < 1) { g.beginPath(); g.moveTo(260, ond(260, 0)); for (let x = 260; x <= 820; x += 20) g.lineTo(x, ond(x, 0)); g.stroke(); }
      else { const r = ret * 70, chute = ret * (10 + rnd(i) * 30);
        g.beginPath(); g.moveTo(260, ond(260, 0)); for (let x = 260; x <= 530 - r; x += 20) g.lineTo(x, ond(x, (x - 260) / 270 * chute)); g.stroke();
        g.beginPath(); g.moveTo(820, ond(820, 0)); for (let x = 820; x >= 550 + r; x -= 20) g.lineTo(x, ond(x, (820 - x) / 270 * chute)); g.stroke(); }
      g.restore();
    }
    if (kc > 0 && pr(t, p.a + .3, .3) < 1) { g.save(); g.globalAlpha = 1 - pr(t, p.a + .3, .3); g.strokeStyle = ROUGE; g.lineWidth = 14; g.shadowColor = ROUGE; g.shadowBlur = 40;
      g.beginPath(); g.moveTo(560, 560); g.lineTo(520, 560 + Math.min(1, kc) * 600); g.stroke(); g.restore(); }
    const k = pop(t, p.a + .05, .3); g.save(); g.translate(W / 2, 1330); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k));
    S.texte('200 MILLIONS', 0, 0, { taille: 150, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14, max: 980 }); g.restore();
    S.texte('DE FIBRES', W / 2, 1470, { taille: 70, coul: CREME, esp: 10, contour: NOIR, contourL: 8 });
  }

  // les deux moitiés s'écartent ; deux bulles « ? » qui ne se rejoignent pas
  function separe(p, t) {
    const e = lerp(0, 60, eo(pr(t, p.a, .8)));
    dessus(W / 2, 900, 320, { ecart: e, coupe: 1, lab: true });
    [-1, 1].forEach((sd, i) => { const k = pop(t, p.a + .3 + i * .35), x = W / 2 + sd * 300;
      g.save(); g.translate(x, 470); g.scale(k, k); g.fillStyle = CREME; g.strokeStyle = sd < 0 ? OR : ROUGE; g.lineWidth = 8;
      g.beginPath(); g.roundRect(-95, -70, 190, 140, 40); g.fill(); g.stroke();
      g.beginPath(); g.moveTo(-sd * 10, 70); g.lineTo(sd * 30, 115); g.lineTo(sd * 40, 66); g.fill();
      S.texte('?', 0, 4, { taille: 100, coul: NOIR }); g.restore(); });
    const kx = pop(t, p.a + 1.1);
    g.save(); g.setLineDash([18, 16]); g.strokeStyle = 'rgba(239,230,210,.5)'; g.lineWidth = 6; g.beginPath(); g.moveTo(W / 2 - 180, 470); g.lineTo(W / 2 + 180, 470); g.stroke(); g.restore();
    if (kx > 0) { g.save(); g.translate(W / 2, 470); g.scale(kx, kx); S.texte('✕', 0, 0, { taille: 140, coul: ROUGE, contour: NOIR, contourL: 10 }); g.restore(); }
    deux(p.t, 1450, 110);
  }

  // fiche d'un chercheur (sans portrait : un cerveau dessiné)
  function nom(p, t, l) {
    const k0 = eo(pr(t, p.a, .5));
    g.save(); g.globalAlpha = k0; S.d.cerveau(540, 720, 260 + l * 6, { trait: OR, fond: SOMBRE, ep: 9, lueur: 'rgba(217,180,90,.5)' }, k0); g.restore();
    const k = eo(pr(t, p.a + .1, .3));
    g.save(); g.translate(lerp(-600, 0, k), 0);
    g.fillStyle = CREME; g.fillRect(90, 1140, 900, 250);
    S.texte(p.t, W / 2, 1220, { taille: 96, coul: NOIR, max: 840 });
    S.texte(p.sous, W / 2, 1320, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: ROUGE });
    g.restore();
  }

  // l'écran du test : point à fixer ; p.flash = repère où les deux images apparaissent en éclair
  function ecran(p, t) {
    g.save(); g.fillStyle = '#0a0907'; g.strokeStyle = CREME; g.lineWidth = 10; g.beginPath(); g.roundRect(100, 520, 880, 600, 24); g.fill(); g.stroke(); g.restore();
    g.fillStyle = '#26221d'; g.fillRect(470, 1120, 140, 70); g.fillRect(380, 1190, 320, 20);
    const pul = 1 + Math.sin((t - p.a) * 7) * .15;
    g.save(); g.fillStyle = OR; g.shadowColor = OR; g.shadowBlur = 30; g.beginPath(); g.arc(W / 2, 820, 16 * pul, 0, 7); g.fill(); g.restore();
    if (p.flash) {
      const tf = tps(p.flash), lt = t - tf;
      if (lt >= 0) {
        const a = lt < .45 ? 1 : Math.max(.22, 1 - (lt - .45) * 2);
        g.save(); g.globalAlpha = a; neige(290, 820, 230, CREME, t); patte(790, 810, 200, CREME); g.restore();
        if (lt < .12) { g.save(); g.globalAlpha = (1 - lt / .12) * .6; g.fillStyle = '#fff6d8'; g.fillRect(100, 520, 880, 600); g.restore(); }
        if (lt > .5) { const k = eo(pr(t, tf + .5, .3)); g.save(); g.globalAlpha = k;
          S.texte('À GAUCHE', 290, 1060, { taille: 40, coul: ROUGE, esp: 4 }); S.texte('À DROITE', 790, 1060, { taille: 40, coul: OR, esp: 4 }); g.restore(); }
      }
    }
    let lab = p.t; if (p.puis && t >= tps(p.aPuis)) lab = p.puis;
    O.multi([[lab, OR]], 1380, 110);
  }

  // le croisement : l'image de gauche ne va que dans le cerveau droit
  function croise(p, t) {
    g.save(); g.fillStyle = '#0a0907'; g.strokeStyle = CREME; g.lineWidth = 7; g.beginPath(); g.roundRect(160, 330, 760, 400, 20); g.fill(); g.stroke(); g.restore();
    g.fillStyle = OR; g.beginPath(); g.arc(W / 2, 530, 12, 0, 7); g.fill();
    neige(330, 530, 170, CREME, t);
    g.save(); g.globalAlpha = .3; patte(750, 525, 150, CREME); g.restore();
    const cy = 1180, s = 270;
    const k = p.fl ? eo(pr(t, tps(p.fl), 1.4)) : 0;
    dessus(W / 2, cy, s, { coupe: 1, lab: true, hd: cl((k - .8) * 5) });
    // yeux
    [-1, 1].forEach(sd => { g.fillStyle = CREME; g.beginPath(); g.ellipse(W / 2 + sd * 70, 860, 34, 22, 0, 0, 7); g.fill(); g.fillStyle = NOIR; g.beginPath(); g.arc(W / 2 + sd * 70, 860, 12, 0, 7); g.fill(); });
    if (k > 0) {
      // trajet : de l'image de gauche, par les yeux, jusqu'à la moitié droite
      const P = [[330, 650], [W / 2 - 30, 900], [W / 2 + 30, 1020], [W / 2 + s * .56, cy]], n = 40;
      const pt = u => { const seg = Math.min(2, Math.floor(u * 3)), v = u * 3 - seg, a = P[seg], b = P[seg + 1]; return [lerp(a[0], b[0], v), lerp(a[1], b[1], v)]; };
      g.save(); g.strokeStyle = ROUGE; g.lineWidth = 14; g.lineCap = 'round'; g.lineJoin = 'round'; g.shadowColor = ROUGE; g.shadowBlur = 25;
      g.beginPath(); for (let i = 0; i <= n * k; i++) { const [x, y] = pt(i / n); i ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); g.restore();
      const [hx, hy] = pt(Math.min(1, k)); g.save(); g.fillStyle = '#fff3c4'; g.shadowColor = ROUGE; g.shadowBlur = 30; g.beginPath(); g.arc(hx, hy, 16, 0, 7); g.fill(); g.restore();
    }
    O.petitTitre(p.t || 'LE SECRET', 260, OR);
    if (k >= 1) { const kk = pop(t, tps(p.fl) + 1.4); g.save(); g.translate(W / 2, 1560); g.scale(kk, kk);
      S.texte('CERVEAU DROIT', 0, 0, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 10 }); g.restore(); }
  }

  // chaque moitié voit son image ; p.mode 'g' (gauche seule), 'gd' (les deux), 'parle' (la gauche répond, la droite s'éteint)
  function voit(p, t) {
    const cy = 1040, s = 320, m = p.mode;
    const kg = m === 'g' ? pop(t, tps(p.bg || p.a)) : 1, kd = m === 'gd' ? pop(t, tps(p.bd || p.a)) : (m === 'g' ? 0 : 1);
    dessus(W / 2, cy, s, { coupe: 1, lab: true, hg: m === 'parle' ? .6 + .4 * Math.sin((t - p.a) * 8) : kg * .8, hd: m === 'gd' ? kd * .8 : 0, gris: m === 'parle' ? 'd' : null });
    bulle('patte', W / 2 - s * .55, 520, 140, kg, OR);
    if (m !== 'g') { g.save(); if (m === 'parle') g.globalAlpha = .3; bulle('neige', W / 2 + s * .55, 520, 140, kd, ROUGE, t); g.restore(); }
    if (m === 'parle') {
      const k = pop(t, p.a + .25); g.save(); g.translate(170, 1040); g.scale(k, k); g.fillStyle = OR;
      g.beginPath(); g.roundRect(-120, -70, 200, 140, 40); g.fill(); g.beginPath(); g.moveTo(40, 40); g.lineTo(130, 60); g.lineTo(70, 0); g.fill();
      S.texte('BLA', -20, 4, { taille: 64, coul: NOIR }); g.restore();
    }
    if (p.t) deux(p.t, 1470, 100);
  }

  // les images posées devant le patient ; p.main 'd' : la main droite montre le poulet ; 'g' : la gauche, la pelle
  function cartes(p, t) {
    const ks = [0, 1, 2, 3].map(i => eo(pr(t, p.a - (p.main ? 5 : 0) + i * .1, .35)));
    const X = [165, 405, 675, 915], Y = 700;
    carteDessin(null, X[0], Y + (1 - ks[0]) * 900, 210, 290, -.06, { dos: true });
    carteDessin('pelle', X[1], Y + (1 - ks[1]) * 900, 210, 290, .03, { nom: 'PELLE', bord: p.main === 'g' ? ROUGE : null });
    carteDessin('poulet', X[2], Y + (1 - ks[2]) * 900, 210, 290, -.03, { nom: 'POULET', bord: p.main ? OR : null });
    carteDessin(null, X[3], Y + (1 - ks[3]) * 900, 210, 290, .05, { dos: true });
    if (p.main) {
      bras(1000, 1950, X[2] + 20, Y + 200, p.main === 'd' ? eo(pr(t, p.a, .5)) : 1);
      S.texte('MAIN DROITE', 850, 1180, { taille: 44, coul: OR, esp: 4, contour: NOIR, contourL: 8 });
    }
    if (p.main === 'g') {
      bras(80, 1950, X[1] - 20, Y + 200, eo(pr(t, p.a + .1, .5)));
      const k = pop(t, p.a + .5); g.save(); g.translate(250, 1180); g.scale(k, k);
      S.texte('MAIN GAUCHE', 0, 0, { taille: 44, coul: ROUGE, esp: 4, contour: NOIR, contourL: 8 }); g.restore();
    }
    if (p.t) deux(p.t, 1420, 100);
  }

  // le cerveau droit ne parle pas : bouche barrée
  function muet(p, t) {
    dessus(W / 2, 1000, 320, { coupe: 1, lab: true, hd: .8 });
    bulle('neige', W / 2 + 176, 480, 130, 1, ROUGE, t);
    const k = pop(t, p.a + .35); g.save(); g.translate(W / 2 + 176, 1000); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-110, -70, 220, 140, 40); g.fill();
    S.texte('…', 0, -6, { taille: 90, coul: NOIR });
    g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round'; g.beginPath(); g.moveTo(-130, -90); g.lineTo(130, 90); g.stroke(); g.restore();
    deux(p.t, 1450, 100);
  }

  // la réponse du cerveau gauche, tapée dans une bulle ; p.icones = dessins au-dessus
  function reponse(p, t) {
    O.petitTitre('— TON CERVEAU GAUCHE —', 330, OR);
    (p.icones || []).forEach((nm, i, L) => { const k = pop(t, p.a + i * .15); g.save(); g.translate(W / 2 + (i - (L.length - 1) / 2) * 280, 560); g.scale(k, k);
      g.fillStyle = CREME; g.beginPath(); g.arc(0, 0, 115, 0, 7); g.fill(); ICONES[nm](0, 0, 140, NOIR, t); g.restore(); });
    g.save(); g.fillStyle = CREME; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.beginPath(); g.roundRect(70, 760, 940, 560, 50); g.fill();
    g.beginPath(); g.moveTo(200, 1300); g.lineTo(150, 1440); g.lineTo(330, 1310); g.fill(); g.restore();
    const txt = p.t, plein = txt.replace(/\|/g, '').length, n = Math.floor(cl((t - p.a) / (p.duree || .9)) * plein);
    const L = txt.split('|');
    let c = 0; L.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte((p.debut && i === 0 ? '« ' : '') + vis + (p.fin && i === L.length - 1 && n >= plein ? ' »' : ''), W / 2, 1040 + (i - (L.length - 1) / 2) * 120,
        { taille: p.taille || 84, police: 'Spectral', it: true, poids: 500, coul: NOIR, max: 860 }); });
    if (p.fin && n >= plein) O.barreRouge(1490, eo(pr(t, p.a + (p.duree || .9) + .1, .3)), 14, -.02);
  }

  // l'interprète : la moitié gauche écrit une histoire
  function interprete(p, t) {
    const lt = t - p.a;
    dessus(330, 860, 300, { hg: .7 + .3 * Math.sin(lt * 6), gris: 'd', coupe: 1 });
    // page qui se remplit
    g.save(); g.translate(800, 760); g.rotate(.05); g.fillStyle = CREME; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 30; g.fillRect(-150, -210, 300, 420); g.shadowBlur = 0;
    const nl = Math.min(8, Math.floor(lt * 7)); g.fillStyle = NOIR;
    for (let i = 0; i < nl; i++) g.fillRect(-115, -170 + i * 46, 230 - (i === 7 ? 90 : rnd(i) * 40), 8);
    const px = -115 + ((lt * 7) % 1) * 230, py = -170 + Math.min(7, nl) * 46;
    g.strokeStyle = OR; g.lineWidth = 10; g.lineCap = 'round'; g.beginPath(); g.moveTo(px, py); g.lineTo(px + 70, py - 120); g.stroke();
    g.restore();
    const ti = tps(p.titre), k = pr(t, ti, .3);
    if (t >= ti) O.tampon('L’INTERPRÈTE', W / 2, 1360, k, -.07, 120, OR);
    else S.texte('IL INVENTE UNE HISTOIRE', W / 2, 1360, { taille: 64, coul: CREME, esp: 4, max: 960 });
  }

  // Descartes, Freud, Nietzsche : trois portraits qui arrivent à leur nom
  function trio(p, t) {
    O.petitTitre('— LA SÉRIE « LA CONSCIENCE » —', 420, OR);
    const P = [['descartes', 'DESCARTES', 200, -.06], ['freud', 'FREUD', 540, .02], ['nietzsche', 'NIETZSCHE', 880, .07]];
    P.forEach(([im, nm, x, rot], i) => { const ta = tps(p.noms[i]); if (t < ta) return; const k = eo(pr(t, ta, .35));
      g.save(); g.translate(0, lerp(500, 0, k)); O.carte(im, x, 860, 290, 400, rot, 1.05, .5, .3, { lum: .95 });
      S.texte(nm, x, 1130, { taille: 54, coul: i === 1 ? OR : CREME, contour: NOIR, contourL: 8 }); g.restore(); });
    O.multi([['LEURS ', CREME], ['RÉPONSES', OR]], 1380, 120);
  }

  return { mains, crise, dessus: dessusPlan, fibres, separe, nom, ecran, croise, voit, cartes, muet, reponse, interprete, trio };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'mains') { L.push([p.a + .1, 'whoosh', .4]); if (p.etape === 'prend') L.push([p.a + .9, 'papier', .6]); else L.push([p.a, 'coeur', .8], [p.a + .8, 'coeur', .8]); }
  if (p.type === 'crise') L.push([p.a, 'statique', .5], [p.a + .05, 'buzz', .5]);
  if (p.type === 'dessus' && p.coupe) L.push([p.a + .1, 'blip', .4], [tps(p.coupe), 'lame', 1]);
  if (p.type === 'dessus' && !p.coupe) L.push([p.a, 'souffle', .5]);
  if (p.type === 'fibres') L.push([p.a + .1, 'coupe', .9]);
  if (p.type === 'separe') L.push([p.a, 'souffle', .5], [p.a + .3, 'pop', .4], [p.a + .65, 'pop', .4], [p.a + 1.1, 'buzz', .4]);
  if (p.type === 'nom') L.push([p.a + .1, 'papier', .4]);
  if (p.type === 'ecran') { if (p.flash) L.push([tps(p.flash), 'bip', .6], [tps(p.flash) + .02, 'glitch', .4]); else L.push([p.a, 'blip', .4]); }
  if (p.type === 'croise') { L.push([p.a, 'clic', .3]); if (p.fl) L.push([tps(p.fl), 'montee', .6], [tps(p.fl) + 1.4, 'pop', .6]); }
  if (p.type === 'voit') { if (p.mode === 'parle') L.push([p.a + .25, 'pop', .5]); else L.push([tps(p.bg || p.bd || p.a), 'pop', .55]); }
  if (p.type === 'cartes') { if (!p.main) for (let i = 0; i < 4; i++) L.push([p.a + i * .1, 'papier', .3]); else L.push([p.a + .4, 'clic', .5]); }
  if (p.type === 'muet') L.push([p.a + .35, 'buzz', .6]);
  if (p.type === 'reponse') { const n = p.t.length, d = p.duree || .9; for (let k = 0; k < n; k += 3) L.push([p.a + d * k / n, 'tic', .25]); }
  if (p.type === 'interprete') L.push([p.a, 'stylo', .5], [tps(p.titre), 'tampon', 1]);
  if (p.type === 'trio') p.noms.forEach(a => L.push([tps(a), 'papier', .5]));
};
