// Plans propres au short Lughnasa (« Deux sœurs disparaissent »), dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
window.SANS_ST_A = ['billet', 'aveu', 'rideau', 'compteur', 'vrai', 'memory', 'miroir'];
window.PROPRES_A = ['maison', 'billet', 'soeurs', 'tricot', 'compteur', 'londres', 'froid', 'hospice', 'rideau', 'vrai', 'arbre', 'valises',
  'nuit', 'aveu', 'archives', 'cantine', 'fenetre', 'encre', 'foyer', 'miroir', 'memory'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const SOMBRE = '#16120e';
  const eio = k => k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // deux lignes « A|B » : la première crème, la seconde or
  const deux = (txt, y, taille = 110) => { if (!txt) return; const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // texte qui entre en rebond
  function surgit(txt, x, y, k, o) { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); S.texte(txt, 0, 0, o); g.restore(); }

  // silhouette de femme (robe longue, châle, chignon), pieds en (x, y), hauteur h ; o.marche : balancement ; o.trait : contour
  function femme(x, y, h, coul, o = {}) {
    const s = h / 600, b = o.marche ? Math.sin(o.marche) * 6 : 0;
    g.save(); g.translate(x, y + b * s); g.scale(s * (o.dir || 1), s);
    g.fillStyle = coul; g.strokeStyle = o.trait || 'transparent'; g.lineWidth = 7 / s; g.lineJoin = 'round';
    g.beginPath(); g.arc(0, -535, 50, 0, 7); g.fill(); if (o.trait) g.stroke();                 // tête
    g.beginPath(); g.arc(-34, -560, 26, 0, 7); g.fill();                                       // chignon
    g.beginPath(); g.moveTo(-22, -490); g.lineTo(22, -490); g.lineTo(80, -440);                  // épaules, châle
    g.quadraticCurveTo(110, -330, 90, -250); g.lineTo(150, 0); g.lineTo(-150, 0); g.lineTo(-90, -250);
    g.quadraticCurveTo(-110, -330, -80, -440); g.closePath(); g.fill(); if (o.trait) g.stroke();
    if (o.sac) { g.fillRect(95, -230, 70, 55); g.strokeStyle = coul; g.lineWidth = 8; g.beginPath(); g.arc(130, -230, 22, Math.PI, 0); g.stroke(); }
    g.restore();
  }
  // buste (tête et épaules) pour les fenêtres et le comptoir
  function buste(x, y, r, coul) {
    g.fillStyle = coul; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill();
    g.beginPath(); g.arc(x - r * .7, y - r * .45, r * .5, 0, 7); g.fill();
    g.beginPath(); g.moveTo(x - r * 1.7, y + r * 2.8); g.quadraticCurveTo(x - r * 1.6, y + r * 1.1, x, y + r * 1.1); g.quadraticCurveTo(x + r * 1.6, y + r * 1.1, x + r * 1.7, y + r * 2.8); g.fill();
  }
  // pluie fine
  function pluie(t, a = .25) {
    g.save(); g.strokeStyle = `rgba(239,230,210,${a})`; g.lineWidth = 2;
    for (let i = 0; i < 70; i++) { const x = rnd(i) * W, y = ((rnd(i + 99) * H) + t * 1400) % H; g.beginPath(); g.moveTo(x, y); g.lineTo(x - 10, y + 40); g.stroke(); }
    g.restore();
  }

  // le cottage à l'aube ; p.partir : les deux sœurs s'éloignent sur la route
  function maison(p, t, l) {
    const ciel = g.createLinearGradient(0, 300, 0, 1100); ciel.addColorStop(0, '#120e0a'); ciel.addColorStop(.7, '#5a4120'); ciel.addColorStop(1, '#c99a4a');
    g.fillStyle = ciel; g.fillRect(0, 0, W, 1110);
    const sy = lerp(1130, 1070, eo(pr(t, p.a, 3)));
    g.save(); g.fillStyle = '#f0cf7a'; g.shadowColor = '#f0cf7a'; g.shadowBlur = 80; g.beginPath(); g.arc(800, sy, 95, Math.PI, 0); g.fill(); g.restore();
    // collines du Donegal
    g.fillStyle = '#1d1711'; g.beginPath(); g.moveTo(0, 1060); for (let x = 0; x <= W; x += 40) g.lineTo(x, 1060 - Math.sin(x / 170) * 40 - Math.sin(x / 61) * 12); g.lineTo(W, H); g.lineTo(0, H); g.fill();
    g.fillStyle = '#100c09'; g.fillRect(0, 1110, W, H - 1110);
    // route qui monte vers l'horizon
    const route = u => { const a = [430, 1620], c = [760, 1330], b = [850, 1112]; const v = 1 - u; return [v * v * a[0] + 2 * v * u * c[0] + u * u * b[0], v * v * a[1] + 2 * v * u * c[1] + u * u * b[1]]; };
    for (let i = 0; i < 40; i++) { const [x0, y0] = route(i / 40), [x1, y1] = route((i + 1) / 40); g.strokeStyle = '#4a3b28'; g.lineWidth = lerp(150, 8, i / 40); g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); }
    // cottage blanchi à la chaux, toit de chaume
    g.fillStyle = '#cfc2a6'; g.fillRect(70, 1000, 400, 300);
    g.fillStyle = '#6b5530'; g.beginPath(); g.moveTo(40, 1010); g.lineTo(150, 860); g.lineTo(390, 860); g.lineTo(500, 1010); g.closePath(); g.fill();
    g.fillStyle = '#3a2f25'; g.fillRect(380, 820, 40, 70);
    g.fillStyle = '#f0c45a'; g.fillRect(120, 1080, 80, 70); g.strokeStyle = SOMBRE; g.lineWidth = 6; g.strokeRect(120, 1080, 80, 70);
    const ko = p.partir ? 1 : eo(pr(t, p.a + .3, .6));
    g.fillStyle = '#2a1d12'; g.fillRect(280, 1150, 90, 150); g.fillStyle = '#e8c070'; g.fillRect(280, 1150, 90 * ko, 150);   // porte qui s'ouvre
    if (p.partir) {
      const t0 = tps(p.partir), u = lerp(.1, .97, eo(pr(t, t0, 3.2)));
      if (t >= t0 - .3) { const [x, y] = route(u), h = lerp(330, 34, Math.pow(u, .8)), m = (t - t0) * 9;
        const tr = 'rgba(239,230,210,.85)'; femme(x - h * .2, y, h, '#0b0907', { marche: m, sac: true, trait: tr }); femme(x + h * .2, y, h * .95, '#0b0907', { marche: m + 1.5, dir: -1, sac: true, trait: tr }); }
    }
    deux(p.t, 560, 110);
  }

  // le mot appuyé contre le pot à lait (citation courte, en anglais, traduite dessous)
  function billet(p, t) {
    g.fillStyle = '#3b2a1c'; g.fillRect(0, 1180, W, H - 1180);
    for (let i = 0; i < 6; i++) { g.strokeStyle = 'rgba(0,0,0,.35)'; g.lineWidth = 3; g.beginPath(); g.moveTo(0, 1220 + i * 70); g.lineTo(W, 1230 + i * 70); g.stroke(); }
    // pot à lait
    g.fillStyle = CREME; g.strokeStyle = SOMBRE; g.lineWidth = 6;
    g.beginPath(); g.moveTo(690, 1200); g.quadraticCurveTo(650, 900, 720, 760); g.lineTo(700, 720); g.lineTo(900, 720); g.lineTo(880, 760); g.quadraticCurveTo(950, 900, 910, 1200); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.arc(925, 900, 70, -1.2, 1.2); g.lineWidth = 22; g.strokeStyle = CREME; g.stroke();
    // le mot
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(lerp(380, 450, k), 960); g.rotate(-.12);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 30; g.fillStyle = '#efe6d2'; g.fillRect(-300, -230, 560, 420); g.shadowColor = 'transparent';
    for (let i = 0; i < 6; i++) { g.fillStyle = 'rgba(80,110,160,.25)'; g.fillRect(-270, -140 + i * 60, 500, 2); }
    const txt = 'We are gone for good.', n = Math.floor(cl((t - p.a - .3) / 1.4) * txt.length);
    S.texte(txt.slice(0, n), -260, -40, { taille: 62, police: 'Spectral', it: true, poids: 500, coul: '#1f2a44', align: 'left', max: 500 });
    g.restore();
    O.petitTitre('— SUR LA TABLE —', 430);
    const kf = eo(pr(t, p.a + 1.6, .4)); g.save(); g.globalAlpha = kf;
    S.texte('« Nous partons pour de bon. »', W / 2, 1420, { taille: 66, police: 'Spectral', it: true, poids: 500, coul: OR, contour: NOIR, contourL: 8, max: 960 });
    S.texte('Brian Friel, Dancing at Lughnasa (1990)', W / 2, 1520, { taille: 30, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    g.restore();
  }

  // les deux sœurs de la pièce, nommées au fil de la voix
  function soeurs(p, t, l) {
    O.fondImg('donegal', 1.2 + l * .03, .5, .5, .3);
    O.petitTitre('— DANS LA PIÈCE —', 430);
    const k = eo(pr(t, p.a, .4));
    [[360, p.n1, 'AGNES'], [720, p.n2, 'ROSE']].forEach(([x, a, nom], i) => {
      femme(x, lerp(1350, 1300, k), 640, SOMBRE, { trait: CREME, dir: i ? -1 : 1 });
      const ka = pr(t, tps(a), .3); surgit(nom, x, 1400, ka, { taille: 110, coul: OR, contour: NOIR, contourL: 12 });
    });
  }

  // gant tricoté et aiguilles
  function tricot(p, t, l) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(500, 900); g.scale(k, k); g.rotate(-.08);
    g.fillStyle = '#b89a66'; g.strokeStyle = CREME; g.lineWidth = 7;
    [[-130, -330], [-50, -380], [30, -360], [110, -300]].forEach(([x, y]) => { g.beginPath(); g.roundRect(x, y, 70, 330, 35); g.fill(); g.stroke(); });
    g.beginPath(); g.save(); g.translate(160, 40); g.rotate(-.7); g.roundRect(-35, -200, 70, 220, 35); g.fill(); g.stroke(); g.restore();
    g.beginPath(); g.roundRect(-150, -60, 330, 330, 60); g.fill(); g.stroke();
    g.fillStyle = '#8f7646'; g.beginPath(); g.roundRect(-140, 250, 310, 130, 20); g.fill(); g.stroke();
    g.strokeStyle = 'rgba(239,230,210,.45)'; g.lineWidth = 4; for (let x = -120; x < 160; x += 26) { g.beginPath(); g.moveTo(x, 262); g.lineTo(x, 368); g.stroke(); }
    // mailles
    g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 3;
    for (let r = 0; r < 6; r++) for (let c = 0; c < 6; c++) { const x = -120 + c * 50, y = -30 + r * 46; g.beginPath(); g.moveTo(x, y); g.lineTo(x + 12, y + 18); g.lineTo(x + 24, y); g.stroke(); }
    g.restore();
    // aiguilles qui travaillent
    const w = Math.sin((t - p.a) * 9) * .12;
    g.save(); g.strokeStyle = '#d9d0bc'; g.lineWidth = 12; g.lineCap = 'round';
    [[w, 640, 380, 1000, 760], [-w, 1000, 400, 640, 760]].forEach(([a, x0, y0, x1, y1]) => { g.save(); g.translate(810, 580); g.rotate(a); g.translate(-810, -580); g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); g.restore(); });
    g.strokeStyle = ROUGE; g.lineWidth = 5; g.beginPath(); g.moveTo(860, 1100); g.quadraticCurveTo(900, 800, 810, 590); g.stroke();
    g.restore();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(860, 1180, 90, 0, 7); g.fill(); g.strokeStyle = '#8a221b'; g.lineWidth = 5;
    for (let i = 0; i < 5; i++) { g.beginPath(); g.arc(860, 1180, 90, i, i + 1.8); g.stroke(); }
    deux(p.t, 1420, 110);
  }

  // « 25 ans plus tard » : feuilles qui s'envolent, compteur
  function compteur(p, t) {
    for (let i = 0; i < 25; i++) {
      const ti = p.a + i * .06, k = pr(t, ti, .9); if (k <= 0) continue;
      g.save(); g.globalAlpha = 1 - k; g.translate(lerp(540, 540 + (rnd(i) - .5) * 1200, k), lerp(900, -100, eo(k))); g.rotate((rnd(i + 7) - .5) * 4 * k);
      g.fillStyle = CREME; g.fillRect(-120, -150, 240, 300); g.fillStyle = ROUGE; g.fillRect(-120, -150, 240, 60);
      g.fillStyle = 'rgba(13,11,9,.3)'; for (let j = 0; j < 4; j++) g.fillRect(-90, -50 + j * 50, 180, 8); g.restore();
    }
    const n = Math.round(25 * eo(pr(t, p.a, 1.5)));
    S.texte('+' + n, W / 2, 880, { taille: 320, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.5)', flou: 40 });
    S.texte('ANS PLUS TARD', W / 2, 1110, { taille: 100, coul: CREME, contour: NOIR, contourL: 10 });
  }

  // Londres : le Nocturne de Whistler (vieux pont de Battersea), pluie
  function londres(p, t, l) {
    const k = eo(pr(t, p.a, .4));
    O.carte('nocturne', W / 2, lerp(900, 820, k), 820, 920, -.025, 1.1 + l * .04, .5, .45, { lum: 1, contraste: 1.2 });
    pluie(t, .18);
    O.multi([['À ', CREME], ['LONDRES', OR]], 1420, 150);
    S.texte('Whistler, Nocturne, le vieux pont de Battersea', W / 2, 1520, { taille: 28, it: true, poids: 400, police: 'Spectral', coul: GRIS });
  }

  // une silhouette recroquevillée sous un porche, souffle et neige
  function froid(p, t, l) {
    g.fillStyle = '#211a14'; g.fillRect(0, 300, W, 1100);
    g.fillStyle = '#0a0806'; g.beginPath(); g.moveTo(300, 1300); g.lineTo(300, 720); g.arc(540, 720, 240, Math.PI, 0); g.lineTo(780, 1300); g.fill();
    g.strokeStyle = '#4a3b2c'; g.lineWidth = 18; g.beginPath(); g.moveTo(290, 1300); g.lineTo(290, 720); g.arc(540, 720, 250, Math.PI, 0); g.lineTo(790, 1300); g.stroke();
    g.fillStyle = '#3a3027'; g.fillRect(220, 1300, 640, 40);
    // silhouette assise, genoux repliés, châle sur la tête
    g.fillStyle = '#6a5d50'; g.beginPath(); g.moveTo(420, 1300); g.quadraticCurveTo(400, 1080, 500, 1010); g.quadraticCurveTo(560, 980, 600, 1050);
    g.quadraticCurveTo(680, 1120, 660, 1300); g.closePath(); g.fill();
    g.beginPath(); g.arc(540, 1000, 60, 0, 7); g.fill();
    // souffle
    for (let i = 0; i < 3; i++) { const ph = ((t - p.a) * .7 + i / 3) % 1; g.fillStyle = `rgba(239,230,210,${.35 * (1 - ph)})`; g.beginPath(); g.arc(610 + ph * 90, 990 - ph * 60, 18 + ph * 40, 0, 7); g.fill(); }
    // neige
    g.fillStyle = 'rgba(239,230,210,.7)';
    for (let i = 0; i < 60; i++) { const x = (rnd(i) * W + Math.sin(t + i) * 30), y = (rnd(i + 40) * H + t * 120) % H; g.beginPath(); g.arc(x, y, 3 + rnd(i + 3) * 4, 0, 7); g.fill(); }
    deux(p.t, 1450, 110);
  }

  // un lit de fer sous une fenêtre, lumière basse
  function hospice(p, t, l) {
    g.fillStyle = '#1b1612'; g.fillRect(0, 300, W, 1200);
    const kl = .6 + .1 * Math.sin((t - p.a) * 2);
    g.save(); g.globalAlpha = kl; const lu = g.createRadialGradient(780, 640, 20, 780, 640, 420); lu.addColorStop(0, 'rgba(217,180,90,.5)'); lu.addColorStop(1, 'rgba(217,180,90,0)');
    g.fillStyle = lu; g.fillRect(300, 200, 780, 900); g.restore();
    g.fillStyle = '#2e3a4a'; g.fillRect(640, 480, 280, 340); g.strokeStyle = '#4a3b2c'; g.lineWidth = 14; g.strokeRect(640, 480, 280, 340);
    g.beginPath(); g.moveTo(780, 480); g.lineTo(780, 820); g.moveTo(640, 650); g.lineTo(920, 650); g.stroke();
    // lit
    g.strokeStyle = '#8d8371'; g.lineWidth = 12;
    g.beginPath(); g.moveTo(140, 1300); g.lineTo(140, 900); g.moveTo(140, 960); g.lineTo(940, 960); g.moveTo(940, 1300); g.lineTo(940, 1050); g.stroke();
    g.fillStyle = CREME; g.beginPath(); g.roundRect(160, 1000, 760, 90, 20); g.fill();
    g.fillStyle = '#e9dfc8'; g.beginPath(); g.ellipse(250, 990, 90, 40, 0, 0, 7); g.fill();
    g.fillStyle = '#7d7262'; g.beginPath(); g.moveTo(300, 1010); g.quadraticCurveTo(500, 900, 900, 1000); g.lineTo(900, 1060); g.lineTo(300, 1060); g.fill();
    g.fillStyle = '#5b4f42'; g.beginPath(); g.arc(250, 970, 42, 0, 7); g.fill();
    deux(p.t, 1450, 110);
  }

  // le théâtre : titre de la pièce, puis le rideau tombe
  function rideau(p, t) {
    const lu = g.createRadialGradient(W / 2, 900, 50, W / 2, 900, 600); lu.addColorStop(0, 'rgba(217,180,90,.28)'); lu.addColorStop(1, 'rgba(217,180,90,0)');
    g.fillStyle = lu; g.fillRect(0, 300, W, 1300);
    S.texte('ÇA, C’EST', W / 2, 620, { taille: 70, coul: CREME, esp: 6 });
    S.texte('LA PIÈCE', W / 2, 740, { taille: 120, coul: OR, contour: NOIR, contourL: 10 });
    const kt = eo(pr(t, tps(p.titre), .5));
    g.save(); g.globalAlpha = kt;
    S.texte('Dancing', W / 2, 930, { taille: 130, police: 'Spectral', it: true, poids: 600, coul: CREME });
    S.texte('at Lughnasa', W / 2, 1070, { taille: 130, police: 'Spectral', it: true, poids: 600, coul: CREME });
    S.texte('BRIAN FRIEL · 1990', W / 2, 1210, { taille: 50, coul: OR, esp: 8 });
    g.restore();
    // rideau rouge qui se ferme à la fin du plan
    const kr = eio(pr(t, p.b - .9, .9)), lr = lerp(140, W / 2, kr);
    [[0, 1], [W, -1]].forEach(([x0, s]) => {
      g.fillStyle = '#7a1f19'; g.beginPath(); g.moveTo(x0, 280); g.lineTo(x0 + s * lr, 280); g.quadraticCurveTo(x0 + s * lr * .8, 900, x0 + s * lr, 1560); g.lineTo(x0, 1560); g.fill();
      g.strokeStyle = 'rgba(0,0,0,.35)'; g.lineWidth = 6; for (let i = 1; i < 6; i++) { const x = x0 + s * lr * i / 6; g.beginPath(); g.moveTo(x, 280); g.lineTo(x, 1560); g.stroke(); }
    });
    g.fillStyle = OR; g.fillRect(0, 260, W, 30); g.fillRect(0, 1560, W, 20);
  }

  // révélation : les deux silhouettes, tampon VRAI
  function vrai(p, t, l) {
    O.fondImg('glenties', 1.2 + l * .03, .5, .5, .35);
    g.save(); g.translate(W / 2, 860); g.rotate(-.03);
    g.fillStyle = CREME; g.fillRect(-330, -380, 660, 640); g.fillStyle = '#5a4a36'; g.fillRect(-300, -350, 600, 580);
    g.restore();
    femme(430, 1110, 560, '#1b140e', {}); femme(650, 1110, 540, '#1b140e', { dir: -1 });
    O.tampon('VRAI', W / 2, 1000, pr(t, p.a + .15, .3), -.12, 190);
    deux('ELLES ONT|VRAIMENT EXISTÉ', 1430, 100);
  }

  // l'auteur : la sculpture de Brian Friel à Dublin
  function friel(p, t, l) {
    O.carte('friel', W / 2, 720, 800, 760, -.02, 2.1 + l * .04, .68, .36, { contraste: 1.5 });
    S.texte('sculpture à Dublin · photo Spleodrach, CC BY-SA 4.0', W / 2, 1135, { taille: 24, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    const k = eo(pr(t, p.a + .1, .3));
    g.save(); g.translate(lerp(-600, 0, k), 0);
    g.fillStyle = CREME; g.fillRect(90, 1180, 900, 250);
    S.texte('BRIAN FRIEL', W / 2, 1260, { taille: 100, coul: NOIR, max: 840 });
    S.texte('l’auteur · 1929 – 2015', W / 2, 1360, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: ROUGE });
    g.restore();
  }

  // arbre : la mère de Friel et quatre de ses sœurs (famille MacLoone, Glenties)
  function arbre(p, t, l) {
    O.fondImg('glenties', 1.2 + l * .03, .5, .5, .25);
    O.petitTitre('LA FAMILLE MACLOONE · GLENTIES', 430);
    const S5 = [['KATE', 1882], ['MAGGIE', 1884], ['ROSE', 1889], ['AGNES', 1891], ['CHRIS', 1896]];
    g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(140, 600); g.lineTo(940, 600); g.moveTo(540, 540); g.lineTo(540, 600); g.stroke();
    const kr = pr(t, p.a + .6, .35);
    S5.forEach(([nom, an], i) => {
      const x = 140 + i * 200, k = eo(pr(t, p.a + i * .08, .3)), rouge = (nom === 'ROSE' || nom === 'AGNES') && kr > 0;
      g.save(); g.globalAlpha = k;
      g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(x, 600); g.lineTo(x, 650); g.stroke();
      if (rouge) { g.shadowColor = ROUGE; g.shadowBlur = 40 * kr; }
      buste(x, 720, 42, rouge ? ROUGE : (nom === 'CHRIS' ? OR : '#8d8371'));
      g.shadowBlur = 0;
      S.texte(nom, x, 880, { taille: 40, coul: rouge ? ROUGE : nom === 'CHRIS' ? OR : CREME, max: 190 });
      S.texte(String(an), x, 930, { taille: 30, police: 'JetBrains Mono', poids: 500, coul: GRIS });
      g.restore();
    });
    const kc = eo(pr(t, p.a + .9, .4));
    g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.moveTo(940, 958); g.lineTo(940, lerp(958, 1110, kc)); g.stroke();
    g.save(); g.globalAlpha = kc; g.fillStyle = CREME; g.fillRect(600, 1110, 380, 90); S.texte('BRIAN FRIEL', 790, 1156, { taille: 50, coul: NOIR }); g.restore();
    S.texte('sa mère', 1005, 1040, { taille: 30, it: true, poids: 400, police: 'Spectral', coul: OR });
    if (kr > 0) surgit('SES TANTES', 640, 995, kr, { taille: 56, coul: ROUGE, contour: NOIR, contourL: 8 });
    deux('LES SŒURS|DE SA MÈRE', 1380, 100);
  }

  // le bateau pour l'Angleterre, deux valises
  function valises(p, t, l) {
    const ciel = g.createLinearGradient(0, 300, 0, 1000); ciel.addColorStop(0, '#120e0a'); ciel.addColorStop(1, '#3d3020'); g.fillStyle = ciel; g.fillRect(0, 0, W, 1000);
    g.fillStyle = '#0f1418'; g.fillRect(0, 1000, W, 600);
    const x = lerp(160, 760, eo(pr(t, p.a, 3)));
    // vapeur
    g.fillStyle = SOMBRE; g.beginPath(); g.moveTo(x - 190, 960); g.lineTo(x + 210, 960); g.lineTo(x + 170, 1030); g.lineTo(x - 160, 1030); g.fill();
    g.fillRect(x - 120, 900, 240, 60); g.fillStyle = '#7a1f19'; g.fillRect(x - 20, 820, 50, 80);
    for (let i = 0; i < 5; i++) { const ph = ((t - p.a) * .8 + i / 5) % 1; g.fillStyle = `rgba(141,131,113,${.5 * (1 - ph)})`; g.beginPath(); g.arc(x + 5 - ph * 200, 800 - ph * 160, 20 + ph * 50, 0, 7); g.fill(); }
    // vagues
    g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 3;
    for (let r = 0; r < 6; r++) { g.beginPath(); for (let xx = 0; xx <= W; xx += 20) { const y = 1060 + r * 50 + Math.sin(xx / 60 + t * 2 + r) * 6; xx ? g.lineTo(xx, y) : g.moveTo(xx, y); } g.stroke(); }
    // valises au premier plan
    [[300, 1240, 260, 170], [620, 1270, 220, 140]].forEach(([vx, vy, w, h], i) => {
      g.fillStyle = i ? '#6b5530' : '#5a3d24'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(vx, vy, w, h, 14); g.fill(); g.stroke();
      g.strokeStyle = CREME; g.beginPath(); g.roundRect(vx + w / 2 - 40, vy - 30, 80, 34, 10); g.stroke();
      g.fillStyle = OR; g.fillRect(vx + 20, vy + 10, 20, h - 20); g.fillRect(vx + w - 40, vy + 10, 20, h - 20);
    });
    deux(p.t, 560, 110);
  }

  // la nuit à Londres : porches, sans-abri endormis
  function nuit(p, t, l) {
    O.fondImg('nocturne', 1.25 + l * .03, .5, .4, .5);
    g.fillStyle = 'rgba(13,11,9,.6)'; g.fillRect(0, 900, W, 700);
    for (let i = 0; i < 3; i++) {
      const x = 60 + i * 340;
      g.fillStyle = '#0a0806'; g.beginPath(); g.moveTo(x, 1400); g.lineTo(x, 1080); g.arc(x + 130, 1080, 130, Math.PI, 0); g.lineTo(x + 260, 1400); g.fill();
      g.strokeStyle = '#4a3b2c'; g.lineWidth = 10; g.beginPath(); g.moveTo(x - 6, 1400); g.lineTo(x - 6, 1080); g.arc(x + 130, 1080, 136, Math.PI, 0); g.lineTo(x + 266, 1400); g.stroke();
      // forme endormie sous une couverture
      const r = 1 + Math.sin((t - p.a) * 2 + i) * .02;
      g.fillStyle = ['#5b5247', '#4d453b', '#62584c'][i]; g.beginPath(); g.ellipse(x + 130, 1370, 115, 38 * r, 0, Math.PI, 0); g.fill();
      g.beginPath(); g.arc(x + 30, 1352, 24, 0, 7); g.fill();
    }
    // réverbère
    g.strokeStyle = '#2a241d'; g.lineWidth = 14; g.beginPath(); g.moveTo(1040, 1400); g.lineTo(1040, 760); g.stroke();
    g.save(); g.fillStyle = '#f0cf7a'; g.shadowColor = '#f0cf7a'; g.shadowBlur = 70; g.beginPath(); g.arc(1040, 740, 26, 0, 7); g.fill(); g.restore();
    deux(p.t, 560, 105);
  }

  // l'aveu de Friel, tapé à la machine ; « je crois » entouré
  function aveu(p, t) {
    O.fondImg('nocturne', 1.3, .5, .4, .3);
    S.texte('BRIAN FRIEL', W / 2, 600, { taille: 40, coul: GRIS, esp: 8 });
    const L = ['J’avais deux tantes', 'qui, je crois,', 'ont fini comme ça.'], tot = L.join('').length, d = p.duree || 2.2;
    const n = Math.floor(cl((t - p.a) / d) * tot); let c = 0;
    L.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte((i === 0 ? '« ' : '') + vis + (i === 2 && n >= tot ? ' »' : ''), W / 2, 820 + i * 130, { taille: 92, police: 'Spectral', it: true, poids: 500, coul: i === 1 && t >= tps(p.cercle) ? OR : CREME, max: 980 }); });
    const kc = pr(t, tps(p.cercle), .45); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(W / 2, 950, 330, 85, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    S.texte('propos rapportés par The Irish Times (2015)', W / 2, 1260, { taille: 30, it: true, poids: 400, police: 'Spectral', coul: GRIS });
  }

  // les archives : registres, loupe
  function archives(p, t, l) {
    for (let i = 0; i < 3; i++) {
      g.save(); g.translate(540 + (i - 1) * 40, 900 + i * 30); g.rotate((i - 1) * .06);
      g.fillStyle = '#e9dfc8'; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 30; g.fillRect(-380, -420, 760, 760); g.shadowColor = 'transparent';
      g.fillStyle = 'rgba(13,11,9,.15)'; g.fillRect(-380, -420, 760, 70);
      for (let r = 0; r < 12; r++) { g.fillStyle = 'rgba(13,11,9,.45)'; g.fillRect(-340, -310 + r * 52, 200 + rnd(r + i * 13) * 120, 6); g.fillRect(40, -310 + r * 52, 100 + rnd(r * 3 + i) * 180, 6); }
      g.strokeStyle = 'rgba(13,11,9,.25)'; g.lineWidth = 2; g.beginPath(); g.moveTo(0, -350); g.lineTo(0, 340); g.stroke();
      g.restore();
    }
    // loupe qui parcourt la page
    const u = (t - p.a) * .9, lx = 540 + Math.sin(u * 2) * 220, ly = 900 + Math.cos(u * 1.3) * 200;
    g.save(); g.strokeStyle = '#3a2f25'; g.lineWidth = 28; g.lineCap = 'round'; g.beginPath(); g.moveTo(lx + 110, ly + 110); g.lineTo(lx + 260, ly + 260); g.stroke();
    g.fillStyle = 'rgba(217,180,90,.18)'; g.strokeStyle = OR; g.lineWidth = 14; g.beginPath(); g.arc(lx, ly, 150, 0, 7); g.fill(); g.stroke(); g.restore();
    deux(p.t, 1450, 110);
  }

  // la cantine : comptoir, fontaine à thé, deux femmes en tablier
  function cantine(p, t, l) {
    O.petitTitre('PIMLICO · 1939', 430);
    g.fillStyle = '#2a221a'; g.fillRect(0, 500, W, 900);
    [[360, 800], [700, 790]].forEach(([x, y]) => { buste(x, y, 70, '#0d0a07'); g.fillStyle = CREME; g.fillRect(x - 70, y + 110, 140, 120); });
    g.fillStyle = '#5a3d24'; g.fillRect(0, 1000, W, 120); g.fillStyle = '#3a2716'; g.fillRect(0, 1120, W, 280);
    g.fillStyle = OR; g.fillRect(0, 990, W, 14);
    // fontaine à thé
    g.fillStyle = '#8d8371'; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.roundRect(820, 760, 170, 240, 20); g.fill(); g.stroke();
    g.fillStyle = '#5b5247'; g.fillRect(800, 740, 210, 30); g.fillRect(890, 900, 40, 20);
    for (let i = 0; i < 4; i++) { const ph = ((t - p.a) * .8 + i / 4) % 1; g.fillStyle = `rgba(239,230,210,${.35 * (1 - ph)})`; g.beginPath(); g.arc(905 + Math.sin(ph * 6 + i) * 20, 720 - ph * 220, 20 + ph * 30, 0, 7); g.fill(); }
    // tasses
    [150, 260, 520, 630].forEach(x => { g.fillStyle = CREME; g.beginPath(); g.moveTo(x - 35, 950); g.lineTo(x + 35, 950); g.lineTo(x + 25, 995); g.lineTo(x - 25, 995); g.fill(); });
    deux(p.t, 1450, 110);
  }

  // l'immeuble de nuit, une fenêtre allumée ; p.etat 1 : deux silhouettes, 2 : l'une disparaît, 3 : une seule
  function fenetre(p, t, l) {
    g.fillStyle = '#2b1d16'; g.fillRect(0, 300, W, 1100);
    for (let r = 0; r < 16; r++) for (let c = -1; c < 9; c++) { g.fillStyle = `rgba(0,0,0,${.15 + rnd(r * 7 + c) * .2})`; g.fillRect(c * 140 + (r % 2) * 70, 300 + r * 70, 134, 64); }
    [[180, 520], [720, 520], [180, 1000], [720, 1000]].forEach(([x, y]) => { g.fillStyle = '#0d0a07'; g.fillRect(x, y, 180, 260); });
    const lum = p.etat === 3 ? .55 : 1;
    g.fillStyle = `rgba(240,196,90,${lum})`; g.fillRect(380, 700, 320, 420);
    const k2 = p.etat === 2 ? 1 - eo(pr(t, p.a + .4, .8)) : p.etat === 3 ? 0 : 1;
    g.save(); g.globalAlpha = k2; buste(470, 880, 55, '#1b140e'); g.restore();
    buste(610, 890, 55, '#1b140e');
    g.strokeStyle = '#4a3b2c'; g.lineWidth = 14; g.strokeRect(380, 700, 320, 420); g.beginPath(); g.moveTo(540, 700); g.lineTo(540, 1120); g.moveTo(380, 910); g.lineTo(700, 910); g.stroke();
    if (p.ans) { const k = back(pr(t, p.a + .5, .35)); g.save(); g.translate(W / 2, 470); g.scale(k, k); S.texte('+ DE 10 ANS', 0, 0, { taille: 90, coul: OR, contour: NOIR, contourL: 10 }); g.restore(); }
    deux(p.t, 1400, 105);
    if (p.sous) S.texte(p.sous, W / 2, 1565, { taille: 58, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 8 });
  }

  // l'encre qui noircit l'image dorée
  function encre(p, t, l) {
    g.save(); const or = g.createRadialGradient(W / 2, 880, 50, W / 2, 880, 520); or.addColorStop(0, '#c99a4a'); or.addColorStop(1, '#4a3820');
    g.fillStyle = or; g.fillRect(140, 420, 800, 900); g.restore();
    femme(430, 1250, 640, '#2a1d12', {}); femme(660, 1250, 620, '#2a1d12', { dir: -1 });
    const k = eo(pr(t, p.a, 1.1));
    g.fillStyle = '#050403';
    for (let i = 0; i < 9; i++) { const cx = 160 + rnd(i) * 760, cy = 460 + rnd(i + 20) * 820, r = (60 + rnd(i + 5) * 220) * cl(k * 1.3 - i * .05);
      if (r <= 0) continue; g.beginPath(); for (let a = 0; a <= 24; a++) { const ang = a / 24 * 6.283, rr = r * (.8 + .3 * rnd(i * 31 + a)); a ? g.lineTo(cx + Math.cos(ang) * rr, cy + Math.sin(ang) * rr) : g.moveTo(cx + Math.cos(ang) * rr, cy + Math.sin(ang) * rr); } g.fill(); }
    g.strokeStyle = CREME; g.lineWidth = 12; g.strokeRect(140, 420, 800, 900);
    deux(p.t, 1450, 110);
  }

  // le foyer de Southwark : bâtiment austère sous la pluie
  function foyer(p, t, l) {
    g.fillStyle = '#16120e'; g.fillRect(0, 300, W, 1300);
    g.fillStyle = '#3a2a20'; g.fillRect(80, 560, 920, 760);
    g.fillStyle = '#2a1e17'; g.beginPath(); g.moveTo(60, 570); g.lineTo(540, 440); g.lineTo(1020, 570); g.fill();
    for (let r = 0; r < 4; r++) for (let c = 0; c < 7; c++) { const on = rnd(r * 7 + c) > .82; g.fillStyle = on ? 'rgba(240,196,90,.55)' : '#0d0a07'; g.fillRect(130 + c * 125, 620 + r * 165, 70, 110); }
    // grille
    g.strokeStyle = '#0a0806'; g.lineWidth = 8; for (let x = 20; x < W; x += 50) { g.beginPath(); g.moveTo(x, 1180); g.lineTo(x, 1400); g.stroke(); }
    g.beginPath(); g.moveTo(0, 1200); g.lineTo(W, 1200); g.stroke();
    g.fillStyle = CREME; g.fillRect(250, 470, 580, 70); S.texte('NEWINGTON LODGE', 540, 508, { taille: 46, coul: NOIR, esp: 4, max: 540 });
    pluie(t, .3);
    deux(p.t, 1430, 100);
    S.texte('SOUTHWARK · LONDRES', W / 2, 1585, { taille: 40, coul: GRIS, esp: 6 });
  }

  // la pièce et la réalité, côte à côte
  function miroir(p, t) {
    g.fillStyle = '#1b1712'; g.fillRect(40, 420, 480, 1000); g.fillStyle = '#231d16'; g.fillRect(560, 420, 480, 1000);
    S.texte('LA PIÈCE', 280, 500, { taille: 56, coul: CREME, esp: 4 }); S.texte('LA RÉALITÉ', 800, 500, { taille: 56, coul: OR, esp: 4 });
    femme(280, 1050, 380, '#5b5247', {}); femme(800, 1050, 380, '#8d8371', { dir: -1 });
    S.texte('un hospice', 280, 1130, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: CREME });
    S.texte('un foyer', 800, 1130, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: CREME });
    const k = pr(t, p.a + .15, .3);
    surgit('SOUTHWARK', 280, 1250, k, { taille: 70, coul: ROUGE, contour: NOIR, contourL: 8, max: 440 });
    surgit('SOUTHWARK', 800, 1250, k, { taille: 70, coul: ROUGE, contour: NOIR, contourL: 8, max: 440 });
    surgit('=', W / 2, 1250, pr(t, p.a + .35, .3), { taille: 160, coul: OR, contour: NOIR, contourL: 10 });
    deux('COMME DANS|LA PIÈCE', 1490, 100);
  }

  // memory play : le souvenir doré (Corot), étiquette
  function memory(p, t, l) {
    O.carte('corot', W / 2, 780, 820, 760, .02, 1.1 + l * .03, .5, .5, { lum: 1, teinte: '#d9b45a' });
    O.petitTitre('ŒUVRE AU PROGRAMME · ACL', 340);
    O.tampon('MEMORY PLAY', W / 2, 1230, pr(t, p.a + .15, .3), -.07, 96, OR);
    S.texte('… ou il invente ?', W / 2, 1420, { taille: 90, police: 'Spectral', it: true, poids: 600, coul: CREME, contour: NOIR, contourL: 8 });
    S.texte('Corot, Souvenir de Mortefontaine, 1864', W / 2, 1530, { taille: 28, it: true, poids: 400, police: 'Spectral', coul: GRIS });
  }

  return { maison, billet, soeurs, tricot, compteur, londres, froid, hospice, rideau, vrai, friel, arbre, valises, nuit, aveu, archives, cantine, fenetre, encre, foyer, miroir, memory };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'maison') { L.push([p.a, 'souffle', .5]); if (p.partir) L.push([tps(p.partir), 'frotte', .35]); else L.push([p.a + .3, 'frotte', .3]); }
  if (p.type === 'billet') L.push([p.a, 'papier', .6], [p.a + .3, 'stylo', .5]);
  if (p.type === 'soeurs') L.push([tps(p.n1), 'pop', .4], [tps(p.n2), 'pop', .4]);
  if (p.type === 'tricot') L.push([p.a, 'frotte', .35]);
  if (p.type === 'compteur') for (let k = 0; k < 25; k++) L.push([p.a + k * .06, 'tic', .3]);
  if (p.type === 'londres' || p.type === 'valises') L.push([p.a, 'whoosh', .5]);
  if (p.type === 'froid' || p.type === 'foyer' || p.type === 'nuit') L.push([p.a, 'souffle', .45]);
  if (p.type === 'hospice') L.push([p.a + .1, 'coeur', .6], [p.a + 1, 'coeur', .45]);
  if (p.type === 'rideau') L.push([tps(p.titre), 'pop', .4], [p.b - .9, 'frotte', .6]);
  if (p.type === 'vrai') L.push([p.a + .2, 'tampon', 1]);
  if (p.type === 'arbre') L.push([p.a + .6, 'blip', .45], [p.a + .9, 'stylo', .4]);
  if (p.type === 'aveu') { const d = p.duree || 2.2; for (let k = 0; k < 24; k++) L.push([p.a + d * k / 24, 'tic', .3]); L.push([tps(p.cercle), 'stylo', .6]); }
  if (p.type === 'archives') L.push([p.a, 'papier', .5], [p.a + .5, 'papier', .35]);
  if (p.type === 'cantine') L.push([p.a, 'clic', .3]);
  if (p.type === 'fenetre' && p.etat === 2) L.push([p.a + .4, 'clic', .6]);
  if (p.type === 'encre') L.push([p.a + .05, 'drop', .7]);
  if (p.type === 'miroir') L.push([p.a + .35, 'tampon', .8]);
  if (p.type === 'memory') L.push([p.a + .2, 'tampon', .7]);
};
