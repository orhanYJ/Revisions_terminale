// Plans propres au short Butler (Parable of the Sower), dans le style du modèle A (noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
// Tout est dessiné : aucune image de couverture ni photo de l'autrice.
window.SANS_ST_A = ['saut', 'citation', 'note', 'classement', 'silence', 'programme', 'liste', 'autrice', 'journal', 'lauren'];
window.PROPRES_A = ['livre', 'saut', 'journal', 'lauren', 'mur', 'eau', 'ville', 'yeux', 'flammes', 'empathie', 'portail',
  'visages', 'silence', 'route', 'citation', 'autrice', 'journaux', 'liste', 'note', 'classement', 'programme', 'boucle'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const ORANGE = '#e8792b';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // deux lignes « A|B » : la première en crème, la seconde en or (ou rouge)
  const deux = (txt, y, taille = 110, c2 = OR) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? c2 : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // texte courant d'une suite d'étapes [[repère, valeur], …] et instant du dernier changement
  const etape = (p, t) => { let v = p.etapes[0][1], t0 = p.a; p.etapes.forEach(([a, x]) => { const ta = a ? tps(a) : p.a; if (t >= ta) { v = x; t0 = ta; } }); return { v, t0 }; };
  const entre = (t, t0, y, txt, taille, c2) => { const k = back(pr(t, t0, .28)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille, c2); g.restore(); };

  // une flamme (base en x, y ; hauteur h), qui vacille
  function flamme(x, y, h, t, s, a = 1) {
    const f = Math.sin(t * 9 + s * 3) * .09 + Math.sin(t * 15.3 + s * 7) * .05;
    g.save(); g.translate(x, y); g.globalAlpha *= a;
    [[ROUGE, 1], [ORANGE, .74], [OR, .5], [CREME, .26]].forEach(([c, k]) => {
      const hh = h * k * (1 + f), w = h * k * .4;
      g.fillStyle = c; g.beginPath(); g.moveTo(-w, 0);
      g.bezierCurveTo(-w * 1.1, -hh * .45, -w * .3 + f * w, -hh * .7, f * w * 2.2, -hh);
      g.bezierCurveTo(w * .3 + f * w, -hh * .7, w * 1.1, -hh * .45, w, 0);
      g.quadraticCurveTo(0, h * k * .12, -w, 0); g.fill();
    });
    g.restore();
  }
  // rangée de flammes + lueur orangée et fumée
  function incendie(y, h, t, k = 1, n = 9) {
    const lu = g.createLinearGradient(0, y - h * 2.2, 0, y); lu.addColorStop(0, 'rgba(232,121,43,0)'); lu.addColorStop(1, `rgba(232,121,43,${.45 * k})`);
    g.fillStyle = lu; g.fillRect(0, y - h * 2.2, W, h * 2.2);
    for (let i = 0; i < 6; i++) { const ph = ((t * .25 + i / 6) % 1); g.fillStyle = `rgba(30,24,20,${.5 * (1 - ph) * k})`;
      g.beginPath(); g.arc(150 + rnd(i * 5) * 780, y - h - ph * 700, 90 + ph * 160, 0, 7); g.fill(); }
    for (let i = 0; i < n; i++) flamme(60 + i * (960 / (n - 1)) + (rnd(i) - .5) * 60, y, h * (.6 + rnd(i * 3) * .6) * k, t, i);
  }
  // silhouette (tête + épaules), centre de la tête (x, y), taille r
  function silhouette(x, y, r, fond = '#16120e', trait = CREME, cheveux = false) {
    g.save(); g.fillStyle = fond; g.strokeStyle = trait; g.lineWidth = 7;
    if (cheveux) { g.beginPath(); g.arc(x, y - r * .1, r * 1.22, 0, 7); g.fill(); g.stroke(); }
    g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(x - r * 1.9, y + r * 3.4); g.quadraticCurveTo(x - r * 1.8, y + r * 1.25, x, y + r * 1.2);
    g.quadraticCurveTo(x + r * 1.8, y + r * 1.25, x + r * 1.9, y + r * 3.4); g.closePath(); g.fill(); g.stroke();
    g.restore();
  }
  // ciel de nuit étoilé
  function nuit(t) { for (let i = 0; i < 40; i++) { g.fillStyle = `rgba(239,230,210,${.25 + .35 * Math.abs(Math.sin(t * 2 + i))})`; g.fillRect(rnd(i) * W, 260 + rnd(i + 40) * 600, 3, 3); } }

  // le roman (couverture dessinée, pas celle d'un éditeur)
  function livre(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1350, 830, k)); g.rotate(lerp(.2, -.05, k));
    g.shadowColor = 'rgba(0,0,0,.7)'; g.shadowBlur = 50; g.shadowOffsetY = 20;
    g.fillStyle = '#5a1a14'; g.fillRect(-300, -420, 600, 840); g.shadowColor = 'transparent';
    g.fillStyle = '#3c100c'; g.fillRect(-300, -420, 40, 840);
    g.strokeStyle = OR; g.lineWidth = 4; g.strokeRect(-230, -380, 490, 760);
    S.texte('PARABLE', 15, -230, { taille: 92, police: 'Spectral', poids: 600, coul: OR });
    S.texte('OF THE SOWER', 15, -140, { taille: 58, police: 'Spectral', poids: 600, coul: OR });
    flamme(15, 170, 190, t, 2);
    g.fillStyle = OR; g.fillRect(-130, 200, 290, 4);
    S.texte('OCTAVIA E. BUTLER', 15, 280, { taille: 40, coul: CREME, esp: 4 });
    g.restore();
    O.petitTitre('— UN ROMAN —', 330);
  }

  // calendrier qui s'effeuille : de p.de à p.vers, arrivée au repère p.cle ; p.ans : affiche « +N ANS »
  function saut(p, t) {
    const t1 = p.cle ? tps(p.cle) : p.a + .8, k = eo(cl((t - p.a - .1) / Math.max(.3, t1 - p.a - .1)));
    const x = lerp(p.de, p.vers, k), v = Math.floor(x + 1e-6), f = x - v;
    const lab = n => p.ans ? '+' + n + ' ANS' : String(n);
    if (p.sous) O.petitTitre(`— ${p.sous} —`, 470);
    const page = (n, dy, rot, a) => { g.save(); g.globalAlpha = a; g.translate(W / 2, 900 + dy); g.rotate(rot);
      g.fillStyle = CREME; g.fillRect(-330, -300, 660, 600); g.fillStyle = ROUGE; g.fillRect(-330, -300, 660, 120);
      S.texte(p.ans ? 'DURÉE' : 'ANNÉE', 0, -240, { taille: 50, coul: CREME, esp: 10 });
      S.texte(lab(n), 0, 60, { taille: p.ans ? 150 : 230, police: 'Spectral', poids: 600, coul: NOIR, max: 600 }); g.restore(); };
    page(v === p.vers ? p.vers : v + 1, 0, 0, 1);
    if (v !== p.vers) page(v, -f * 420, -f * .5, 1 - f);
    g.save(); g.fillStyle = '#26221d'; for (let i = 0; i < 6; i++) { g.beginPath(); g.arc(W / 2 - 250 + i * 100, 600, 16, 0, 7); g.fill(); } g.restore();
    if (p.t && t >= t1) entre(t, t1, 1420, p.t, 110);
  }

  // page de journal intime ; p.date en tête ; p.mot écrit sur la page ; p.etapes = texte du bas
  function journal(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1250, 860, k)); g.rotate(-.03);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#ece2c9'; g.fillRect(-380, -420, 760, 840); g.shadowColor = 'transparent';
    g.strokeStyle = 'rgba(200,55,45,.5)'; g.lineWidth = 3; g.beginPath(); g.moveTo(-290, -420); g.lineTo(-290, 420); g.stroke();
    g.strokeStyle = 'rgba(60,80,120,.25)'; for (let i = 0; i < 12; i++) { g.beginPath(); g.moveTo(-380, -300 + i * 62); g.lineTo(380, -300 + i * 62); g.stroke(); }
    if (p.date) { const n = Math.floor(cl((t - p.a - .2) / .7) * p.date.length);
      S.texte(p.date.slice(0, n), -250, -330, { taille: 64, police: 'Spectral', it: true, poids: 500, coul: NOIR, align: 'left' }); }
    // lignes d'écriture
    for (let i = 0; i < 7; i++) { const kk = cl((t - p.a - .4 - i * .18) / .3); g.fillStyle = 'rgba(13,11,9,.55)'; g.fillRect(-250, -205 + i * 62, (i === 6 ? 300 : 560) * kk, 5); }
    if (p.mot && t >= tps(p.mot[1])) { const kk = back(pr(t, tps(p.mot[1]), .3)); g.save(); g.translate(30, 300); g.rotate(-.06); g.scale(kk, kk);
      S.texte(p.mot[0], 0, 0, { taille: 96, coul: ROUGE, police: 'Spectral', poids: 600 }); g.restore(); }
    g.restore();
    if (p.etapes) { const { v, t0 } = etape(p, t); entre(t, t0, 1440, v, 105); }
  }

  // Lauren : silhouette, prénom, puis « 15 ANS » au repère p.age
  function lauren(p, t, l) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.globalAlpha = k; silhouette(W / 2, 700 - (1 - k) * 60, 150, '#1b1712', OR, true); g.restore();
    g.save(); g.translate(lerp(-700, 0, eo(pr(t, p.a + .15, .3))), 0);
    g.fillStyle = CREME; g.fillRect(140, 1150, 800, 190);
    S.texte('LAUREN', W / 2, 1210, { taille: 100, coul: NOIR });
    S.texte('le personnage principal', W / 2, 1300, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: ROUGE });
    g.restore();
    if (p.age && t >= tps(p.age)) O.tampon('15 ANS', W / 2, 1480, pr(t, tps(p.age), .3), -.08, 110, OR);
  }

  // le mur du quartier ; p.feu : il brûle derrière ; p.lieu : étiquette en haut
  function mur(p, t, l) {
    nuit(t);
    const kf = p.feu ? eo(pr(t, p.a, .6)) : 0;
    // toits des maisons derrière le mur
    for (let i = 0; i < 5; i++) { const x = 90 + i * 210, y = 930 - (i % 2) * 40;
      g.fillStyle = '#2b241d'; g.strokeStyle = 'rgba(239,230,210,.5)'; g.lineWidth = 4;
      g.beginPath(); g.moveTo(x, y); g.lineTo(x + 90, y - 110); g.lineTo(x + 180, y); g.closePath(); g.fill(); g.stroke();
      g.fillStyle = kf > .3 ? ORANGE : OR; g.fillRect(x + 70, y - 50, 40, 40); }
    if (p.feu) incendie(960, 260, t, kf, 8);
    // le mur, en parpaings, avec barbelés
    for (let r = 0; r < 6; r++) for (let c = -1; c < 9; c++) { const x = c * 140 + (r % 2) * 70, y = 960 + r * 70;
      g.fillStyle = `rgb(${92 + rnd(r * 9 + c) * 22},${84 + rnd(r + c * 5) * 18},${74})`; g.fillRect(x + 4, y + 4, 132, 62); }
    g.strokeStyle = GRIS; g.lineWidth = 4; g.beginPath(); for (let x = 0; x <= W; x += 6) g.lineTo(x, 940 + Math.sin(x * .05) * 10); g.stroke();
    for (let x = 30; x < W; x += 70) { g.beginPath(); g.moveTo(x - 10, 930); g.lineTo(x + 10, 950); g.moveTo(x + 10, 930); g.lineTo(x - 10, 950); g.stroke(); }
    if (p.lieu) O.petitTitre(`— ${p.lieu} —`, 360);
    if (p.t) deux(p.t, 1440, 115, p.feu ? ROUGE : OR);
  }

  // l'eau plus chère que l'essence : deux étiquettes de prix
  function eau(p, t) {
    O.petitTitre('— LES PRIX, DEHORS —', 380);
    const k = eo(pr(t, p.a + .15, .8));
    const barre = (x, h, coul, nom) => { g.fillStyle = '#26221d'; g.fillRect(x - 130, 1150 - 560, 260, 560);
      g.fillStyle = coul; g.fillRect(x - 110, 1150 - h * k, 220, h * k); S.texte(nom, x, 1210, { taille: 54, coul: CREME, esp: 4 }); };
    barre(340, 520, '#6fa7c8', 'EAU'); barre(740, 150, OR, 'ESSENCE');
    // goutte et bidon
    g.fillStyle = '#6fa7c8'; g.beginPath(); g.moveTo(340, 470); g.quadraticCurveTo(400, 540, 340, 560); g.quadraticCurveTo(280, 540, 340, 470); g.fill();
    g.fillStyle = OR; g.fillRect(705, 480, 70, 80); g.fillRect(735, 460, 30, 24);
    if (t > p.a + .7) S.texte('>', W / 2 + 0, 900, { taille: 160, coul: ROUGE, contour: NOIR, contourL: 10 });
    deux('L’EAU|PLUS CHÈRE QUE L’ESSENCE', 1420, 100);
  }

  // la ville qui brûle (Los Angeles, au loin)
  function ville(p, t, l) {
    nuit(t);
    const k = eo(pr(t, p.a, .5));
    incendie(1180, 300, t, k, 10);
    for (let i = 0; i < 12; i++) { const w = 70 + rnd(i * 2) * 60, h = 180 + rnd(i * 7) * 420, x = i * 92 - 20;
      g.fillStyle = '#100d0a'; g.fillRect(x, 1180 - h, w, h);
      g.fillStyle = 'rgba(232,121,43,.5)'; for (let j = 0; j < h / 60 - 1; j++) if (rnd(i * 31 + j) > .55) g.fillRect(x + 16, 1180 - h + 30 + j * 60, 18, 24); }
    g.fillStyle = '#100d0a'; g.fillRect(0, 1180, W, 120);
    deux(p.t || 'LES INCENDIES|NE S’ARRÊTENT PLUS', 1420, 110, ROUGE);
  }

  // des yeux où se reflètent des flammes qui grandissent
  function yeux(p, t, l) {
    const k = eo(pr(t, p.a, 1.2));
    [[330, 820], [750, 820]].forEach(([x, y], i) => {
      g.save(); g.fillStyle = CREME; g.beginPath(); g.moveTo(x - 190, y); g.quadraticCurveTo(x, y - 170, x + 190, y); g.quadraticCurveTo(x, y + 170, x - 190, y); g.fill();
      g.clip(); g.fillStyle = '#2a1a10'; g.beginPath(); g.arc(x, y, 105, 0, 7); g.fill();
      g.fillStyle = NOIR; g.beginPath(); g.arc(x, y, 50 + 20 * k, 0, 7); g.fill();
      flamme(x, y + 55, 120 * k + 10, t, i * 4, .9);
      g.restore();
      g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(x - 190, y); g.quadraticCurveTo(x, y - 170, x + 190, y); g.stroke();
    });
    deux(p.t || 'ELLE DONNE|ENVIE DE…', 1400, 110);
  }

  // plein feu
  function flammes(p, t, l) {
    incendie(1900, 700, t, eo(pr(t, p.a, .35)), 7);
    entre(t, p.a, 880, p.t || 'METTRE|LE FEU', 180, ROUGE);
  }

  // l'hyperempathie : la douleur de l'autre passe dans ton corps (p.mal, p.toi = repères)
  function empathie(p, t, l) {
    const tm = tps(p.mal), tt = tps(p.toi);
    silhouette(300, 700, 110, '#1b1712', CREME); silhouette(780, 700, 110, '#1b1712', OR, true);
    S.texte('QUELQU’UN', 300, 520, { taille: 40, coul: CREME, esp: 4 }); S.texte('TOI', 780, 520, { taille: 40, coul: OR, esp: 4 });
    const douleur = (x, k) => { if (k <= 0) return; g.save(); const r = g.createRadialGradient(x, 900, 10, x, 900, 230); r.addColorStop(0, `rgba(200,55,45,${.9 * k})`); r.addColorStop(1, 'rgba(200,55,45,0)');
      g.fillStyle = r; g.beginPath(); g.arc(x, 900, 230, 0, 7); g.fill(); g.restore(); };
    douleur(300, t >= tm ? .6 + .4 * Math.sin((t - tm) * 9) : 0);
    // l'onde qui traverse l'espace
    if (t >= tt) { for (let i = 0; i < 3; i++) { const ph = ((t - tt) * 1.4 + i / 3) % 1; g.save(); g.strokeStyle = ROUGE; g.globalAlpha = 1 - ph; g.lineWidth = 8;
      g.beginPath(); g.arc(lerp(300, 780, ph), 900, 60, -1.2, 1.2); g.stroke(); g.restore(); }
      douleur(780, eo(pr(t, tt + .25, .4)) * (.7 + .3 * Math.sin((t - tt) * 9))); }
    const { v, t0 } = etape(p, t); entre(t, t0, 1420, v, 105, ROUGE);
  }

  // le portail ; p.crash : un camion l'enfonce
  function portail(p, t, l) {
    nuit(t);
    const lt = t - p.a, kc = p.crash ? eo(pr(t, p.a, .25)) : 0;
    // phares qui approchent (derrière le portail)
    const kp = p.crash ? 1 : eo(cl(lt / 1.6));
    [[-130], [130]].forEach(([dx]) => { const r = g.createRadialGradient(W / 2 + dx * (.5 + kp * .5), 880, 5, W / 2 + dx * (.5 + kp * .5), 880, 60 + kp * 220);
      r.addColorStop(0, 'rgba(255,248,220,.95)'); r.addColorStop(1, 'rgba(255,248,220,0)'); g.fillStyle = r; g.fillRect(0, 500, W, 800); });
    // murs de part et d'autre
    g.fillStyle = '#5e564b'; g.fillRect(0, 620, 200, 640); g.fillRect(880, 620, 200, 640);
    // barreaux : droits, puis projetés
    g.strokeStyle = '#a69d8c'; g.lineWidth = 16;
    for (let i = 0; i < 9; i++) { const x0 = 230 + i * 77.5;
      g.save(); if (kc > 0) { g.translate(x0, 1250); g.rotate((i - 4) * .12 * kc); g.translate(-x0 + (i - 4) * 60 * kc, -kc * 120 * (1 - Math.abs(i - 4) / 5)); }
      g.beginPath(); g.moveTo(x0, 640); g.lineTo(x0, 1250); g.stroke(); g.restore(); }
    if (!kc) { g.lineWidth = 12; [700, 1180].forEach(y => { g.beginPath(); g.moveTo(200, y); g.lineTo(880, y); g.stroke(); }); }
    else { // calandre du camion
      g.save(); g.translate(W / 2, 1000); g.scale(lerp(.6, 1.15, kc), lerp(.6, 1.15, kc));
      g.fillStyle = '#2b2620'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(-330, -180, 660, 360, 20); g.fill(); g.stroke();
      g.fillStyle = '#fff6d8'; [[-240], [240]].forEach(([x]) => { g.beginPath(); g.arc(x, -40, 55, 0, 7); g.fill(); });
      g.strokeStyle = GRIS; g.lineWidth = 8; for (let i = -3; i <= 3; i++) { g.beginPath(); g.moveTo(i * 40, -120); g.lineTo(i * 40, 60); g.stroke(); }
      g.restore(); }
    if (p.t) deux(p.t, 1440, 115, p.crash ? ROUGE : OR);
  }

  // visages peints, devant l'incendie
  function visages(p, t, l) {
    incendie(1250, 330, t, eo(pr(t, p.a, .5)), 8);
    const coul = ['#3f8f5a', '#3f6fb0', ROUGE, OR];
    [[260, 760, 115], [540, 700, 135], [820, 760, 115]].forEach(([x, y, r], i) => {
      const k = eo(pr(t, p.a + i * .12, .3));
      g.save(); g.globalAlpha = k; silhouette(x, y + (1 - k) * 80, r, '#120f0c', 'rgba(239,230,210,.7)');
      g.beginPath(); g.arc(x, y, r - 4, 0, 7); g.clip();
      for (let j = 0; j < 3; j++) { g.fillStyle = coul[(i + j) % 4]; g.globalAlpha = .85 * k; g.fillRect(x - r, y - r * .5 + j * r * .38, r * 2, r * .2); }
      g.restore(); });
    deux(p.t || 'DES VISAGES|PEINTS', 1440, 115, ROUGE);
  }

  // silence : braises qui retombent
  function silence(p, t, l) {
    g.fillStyle = '#000'; g.fillRect(0, 0, W, H);
    for (let i = 0; i < 26; i++) { const ph = ((t - p.a) * .35 + rnd(i)) % 1; g.fillStyle = `rgba(232,121,43,${(1 - ph) * .8})`;
      g.beginPath(); g.arc(80 + rnd(i * 3) * 920 + Math.sin(t * 2 + i) * 20, 500 + ph * 900, 3 + rnd(i * 7) * 4, 0, 7); g.fill(); }
    const k = pr(t, p.a + .15, .5); g.save(); g.globalAlpha = k;
    S.texte(p.t || '…', W / 2, 960, { taille: 70, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore();
  }

  // la route vers le nord, à pied
  function route(p, t, l) {
    nuit(t);
    g.fillStyle = '#1e1a15'; g.beginPath(); g.moveTo(80, 1500); g.lineTo(500, 640); g.lineTo(580, 640); g.lineTo(1000, 1500); g.closePath(); g.fill();
    g.strokeStyle = 'rgba(239,230,210,.5)'; g.lineWidth = 5; g.beginPath(); g.moveTo(80, 1500); g.lineTo(500, 640); g.moveTo(1000, 1500); g.lineTo(580, 640); g.stroke();
    // pointillés qui défilent
    for (let i = 0; i < 8; i++) { const u = ((i / 8) + (t - p.a) * .35) % 1, y = lerp(660, 1500, u * u), w = lerp(4, 26, u * u), h = lerp(10, 90, u * u);
      g.fillStyle = OR; g.fillRect(W / 2 - w / 2, y, w, h); }
    // panneau
    g.fillStyle = '#2f5d3a'; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.roundRect(700, 430, 300, 170, 14); g.fill(); g.stroke();
    S.texte('NORD ↑', 850, 515, { taille: 66, coul: CREME });
    // marcheuse avec sac
    const b = Math.abs(Math.sin((t - p.a) * 6)) * 14;
    g.save(); g.translate(W / 2 - 40, 1180 - b); g.fillStyle = NOIR; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.arc(0, -150, 42, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.roundRect(-45, -100, 90, 170, 20); g.fill(); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.roundRect(-70, -90, 40, 110, 10); g.fill();
    const ph = Math.sin((t - p.a) * 6) * 30; g.beginPath(); g.moveTo(-15, 70); g.lineTo(-15 - ph, 200); g.moveTo(15, 70); g.lineTo(15 + ph, 200); g.stroke();
    g.restore();
    deux(p.t || 'VERS LE NORD|À PIED', 1440, 110);
  }

  // « God is Change » tapé à la machine ; traduction au repère p.trad
  function citation(p, t) {
    const txt = 'God is Change.', n = Math.floor(cl((t - p.a) / .8) * txt.length);
    O.petitTitre('— LA PHRASE DU ROMAN —', 560);
    S.texte(txt.slice(0, n), W / 2, 860, { taille: 150, police: 'Spectral', it: true, poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 40, max: 980 });
    if (p.trad && t >= tps(p.trad)) { const k = eo(pr(t, tps(p.trad), .35)); g.save(); g.globalAlpha = k;
      S.texte('« Dieu est changement. »', W / 2, 1060, { taille: 76, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore();
      O.barreRouge(1140, k, 10, -.02); }
    S.texte('Parable of the Sower, 1993', W / 2, 1300, { taille: 40, police: 'JetBrains Mono', poids: 500, coul: GRIS });
  }

  // l'autrice : machine à écrire, fiche ; tampon au repère p.tampon
  function autrice(p, t) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1100, 760, k));
    g.fillStyle = CREME; g.fillRect(-230, -330, 460, 300);
    for (let i = 0; i < 5; i++) { g.fillStyle = 'rgba(13,11,9,.5)'; g.fillRect(-180, -280 + i * 50, (i === 4 ? 200 : 360) * cl((t - p.a - i * .12) / .25), 6); }
    g.fillStyle = '#2b2620'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(-340, -40, 680, 260, 30); g.fill(); g.stroke();
    g.fillStyle = '#3d362e'; g.fillRect(-360, -70, 720, 50);
    for (let r = 0; r < 3; r++) for (let c = 0; c < 10 - r; c++) { g.fillStyle = CREME; g.beginPath(); g.arc(-270 + r * 30 + c * 60, 30 + r * 55, 20, 0, 7); g.fill(); }
    g.restore();
    g.save(); g.translate(lerp(-700, 0, eo(pr(t, p.a + .1, .3))), 0);
    g.fillStyle = CREME; g.fillRect(90, 1130, 900, 250);
    S.texte('OCTAVIA E. BUTLER', W / 2, 1210, { taille: 88, coul: NOIR, max: 840 });
    S.texte('1947 – 2006 · autrice de science-fiction', W / 2, 1310, { taille: 48, it: true, poids: 400, police: 'Spectral', coul: ROUGE, max: 840 });
    g.restore();
    if (p.tampon) O.tampon('RIEN DEVINÉ', W / 2, 1520, pr(t, tps(p.tampon), .3), -.08, 92);
  }

  // coupures de presse du début des années 1990, sous la loupe
  function journaux(p, t, l) {
    O.petitTitre('— LES ANNÉES 1990 —', 380);
    [['SÉCHERESSE', -.08, 300, 620], ['ÉMEUTES À LOS ANGELES', .05, 640, 840], ['INCENDIES', -.03, 360, 1080]].forEach(([s, rot, x, y], i) => {
      const k = eo(pr(t, p.a + i * .15, .3)); if (k <= 0) return;
      g.save(); g.translate(x, y + (1 - k) * 300); g.rotate(rot); g.globalAlpha = k;
      g.fillStyle = '#e4d9bf'; g.fillRect(-250, -130, 500, 260);
      S.texte(s, 0, -60, { taille: 54, police: 'Spectral', poids: 600, coul: NOIR, max: 450 });
      for (let j = 0; j < 4; j++) { g.fillStyle = 'rgba(13,11,9,.3)'; g.fillRect(-210, -5 + j * 32, 420 - (j === 3 ? 160 : 0), 8); }
      g.restore(); });
    // loupe
    const a = (t - p.a) * 1.3, lx = 540 + Math.cos(a) * 200, ly = 850 + Math.sin(a * .8) * 220;
    g.save(); g.strokeStyle = OR; g.lineWidth = 16; g.beginPath(); g.arc(lx, ly, 120, 0, 7); g.stroke();
    g.lineWidth = 26; g.beginPath(); g.moveTo(lx + 85, ly + 85); g.lineTo(lx + 190, ly + 190); g.stroke(); g.restore();
    deux(p.t || 'LES PROBLÈMES|QU’ON NÉGLIGE', 1440, 110);
  }

  // liste cochée : p.items = [[texte, repère], …] ; p.fin = repère de la conclusion
  function liste(p, t) {
    p.items.forEach(([s, a], i) => { const ta = tps(a), y = 600 + i * 190, k = pr(t, ta, .25);
      g.strokeStyle = CREME; g.lineWidth = 7; g.strokeRect(150, y - 55, 110, 110);
      if (k > 0) { g.save(); g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round'; g.beginPath(); g.moveTo(170, y);
        g.lineTo(lerp(170, 200, cl(k * 2)), lerp(y, y + 35, cl(k * 2))); if (k > .5) g.lineTo(lerp(200, 250, (k - .5) * 2), lerp(y + 35, y - 50, (k - .5) * 2)); g.stroke(); g.restore(); }
      S.texte(s, 300, y, { taille: 76, coul: t >= ta ? CREME : 'rgba(239,230,210,.35)', align: 'left', max: 700 }); });
    if (p.fin && t >= tps(p.fin)) entre(t, tps(p.fin), 1340, 'TOUT ÉTAIT|DÉJÀ LÀ', 130);
  }

  // son carnet : « I shall be a bestselling writer » écrit au repère p.ecrit ; p.zoom : gros plan et traduction
  function note(p, t) {
    const z = p.zoom ? lerp(1, 1.18, eo(pr(t, p.a, .5))) : eo(pr(t, p.a, .35));
    O.petitTitre('— SON CARNET —', 360);
    g.save(); g.translate(W / 2, 860); g.scale(z, z); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#ece2c9'; g.fillRect(-400, -330, 800, 660); g.shadowColor = 'transparent';
    for (let i = 0; i < 9; i++) { g.strokeStyle = GRIS; g.lineWidth = 6; g.beginPath(); g.arc(-320 + i * 80, -330, 22, Math.PI, 0); g.stroke(); }
    g.strokeStyle = 'rgba(60,80,120,.25)'; g.lineWidth = 3; for (let i = 0; i < 8; i++) { g.beginPath(); g.moveTo(-400, -200 + i * 70); g.lineTo(400, -200 + i * 70); g.stroke(); }
    const L = ['I shall be a', 'bestselling', 'writer.'], tot = L.join('').length, te = p.ecrit ? tps(p.ecrit) : 1e9;
    const n = Math.floor(cl((t - te) / 1.3) * tot);
    let c = 0; L.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte(vis, -330, -160 + i * 120, { taille: 92, police: 'Spectral', it: true, poids: 500, coul: '#1d2a4a', align: 'left' }); });
    if (n >= tot) { const k = pr(t, te + 1.3, .4); g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.moveTo(-330, 140); g.lineTo(-330 + 560 * k, 130); g.stroke(); }
    g.restore();
    if (p.zoom && t >= te + .3) { const k = eo(pr(t, te + .3, .4)); g.save(); g.globalAlpha = k;
      deux('JE SERAI UNE AUTRICE|DE BEST-SELLERS', 1420, 95); g.restore(); }
  }

  // la liste des meilleures ventes ; p.etape 1 : elle n'y est pas ; 2 : le roman entre à la 14ᵉ place (repère p.entre)
  function classement(p, t) {
    const e = p.etape;
    O.petitTitre('— NEW YORK TIMES —', 380);
    S.texte(e === 1 ? 'DE SON VIVANT' : '2020', W / 2, 500, { taille: e === 1 ? 70 : 120, police: 'Spectral', poids: 600, coul: e === 1 ? CREME : OR });
    const te = e === 2 ? tps(p.entre) : 1e9;
    for (let i = 0; i < 15; i++) { const y = 620 + i * 52, ici = e === 2 && i === 13 && t >= te;
      S.texte(String(i + 1), 170, y, { taille: 34, police: 'JetBrains Mono', poids: 500, coul: ici ? OR : GRIS, align: 'right' });
      if (ici) { const k = eo(pr(t, te, .35)); g.save(); g.translate(lerp(900, 0, k), 0);
        g.fillStyle = OR; g.fillRect(200, y - 22, 700, 44); S.texte('PARABLE OF THE SOWER · O. E. BUTLER', 550, y, { taille: 30, coul: NOIR, max: 660 }); g.restore(); }
      else { g.fillStyle = 'rgba(239,230,210,.18)'; g.fillRect(200, y - 10, 380 + rnd(i * 13) * 320, 20); } }
    if (e === 1 && t >= p.a + .4) O.tampon('ABSENTE', W / 2, 1480, pr(t, p.a + .4, .3), -.1, 120);
    if (e === 2 && p.quatorze && t >= tps(p.quatorze)) { const k = back(pr(t, tps(p.quatorze), .3)); g.save(); g.translate(W / 2, 1490); g.scale(k, k);
      S.texte('14 ANS APRÈS SA MORT', 0, 0, { taille: 80, coul: ROUGE, contour: NOIR, contourL: 10, max: 960 }); g.restore(); }
  }

  // le roman au programme (fiche d'épreuve)
  function programme(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 880, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-380, -440, 760, 880); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT · BFI', 0, -350, { taille: 48, coul: NOIR, esp: 4 });
    S.texte('APPROFONDISSEMENT CULTUREL', 0, -280, { taille: 32, coul: GRIS, esp: 4, poids: 600 });
    S.texte('ET LINGUISTIQUE · ORAL', 0, -235, { taille: 32, coul: GRIS, esp: 4, poids: 600 });
    g.fillStyle = NOIR; g.fillRect(-300, -190, 600, 3);
    S.texte('Œuvre au programme', -300, -120, { taille: 40, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400 });
    S.texte('Parable of the Sower', 0, -10, { taille: 74, police: 'Spectral', it: true, poids: 600, coul: NOIR, max: 680 });
    S.texte('Octavia E. Butler, 1993', 0, 80, { taille: 48, police: 'Spectral', poids: 400, coul: NOIR });
    for (let i = 0; i < 5; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-300, 180 + i * 50, 600 - (i === 4 ? 250 : 0), 6); }
    const kc = pr(t, p.a + .35, .5); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(0, 30, 360, 120, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['AU ', CREME], ['PROGRAMME', ROUGE]], 1560, 110);
  }

  // fin (boucle) : la feuille tapée en 1993
  function boucle(p, t, l) {
    const k = eo(pr(t, p.a, .4));
    incendie(1900, 380, t, .5 * k, 7);
    g.save(); g.translate(W / 2, 800); g.rotate(-.03); g.globalAlpha = k;
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#ece2c9'; g.fillRect(-330, -420, 660, 760); g.shadowColor = 'transparent';
    S.texte('1993', 230, -360, { taille: 40, police: 'JetBrains Mono', poids: 500, coul: GRIS });
    S.texte('Chapitre 1', -250, -280, { taille: 40, police: 'JetBrains Mono', poids: 500, coul: NOIR, align: 'left' });
    S.texte('Samedi 20 juillet 2024', -250, -200, { taille: 40, police: 'JetBrains Mono', poids: 500, coul: NOIR, align: 'left' });
    for (let i = 0; i < 9; i++) { g.fillStyle = 'rgba(13,11,9,.45)'; g.fillRect(-250, -110 + i * 48, (i === 8 ? 240 : 500) * cl((t - p.a - .3 - i * .1) / .2), 6); }
    g.restore();
    deux(p.t || 'ET TOUT ÇA…|UNE FEMME L’AVAIT ÉCRIT', 1440, 105);
  }

  return { livre, saut, journal, lauren, mur, eau, ville, yeux, flammes, empathie, portail, visages, silence, route, citation, autrice, journaux, liste, note, classement, programme, boucle };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'livre') L.push([p.a, 'papier', .5]);
  if (p.type === 'saut') { const t1 = p.cle ? tps(p.cle) : p.a + .8, n = Math.min(12, Math.abs(p.vers - p.de));
    L.push([p.a, 'whoosh', .5]); for (let k = 0; k < n; k++) L.push([p.a + .1 + (t1 - p.a - .1) * k / n, 'tic', .4]); L.push([t1, 'clic', .6]); }
  if (p.type === 'journal') { L.push([p.a + .2, 'stylo', .5]); (p.etapes || []).slice(1).forEach(([a]) => L.push([tps(a), 'papier', .3])); if (p.mot) L.push([tps(p.mot[1]), 'pop', .5]); }
  if (p.type === 'lauren') { L.push([p.a, 'frotte', .3]); if (p.age) L.push([tps(p.age) + .05, 'tampon', .7]); }
  if (p.type === 'mur') L.push([p.a, p.feu ? 'souffle' : 'frotte', p.feu ? .8 : .3]);
  if (p.type === 'eau') L.push([p.a + .2, 'blip', .4], [p.a + .7, 'bip', .4]);
  if (p.type === 'ville' || p.type === 'visages') L.push([p.a, 'souffle', .6]);
  if (p.type === 'yeux') L.push([p.a, 'aspire', .5]);
  if (p.type === 'flammes') L.push([p.a, 'souffle', 1]);
  if (p.type === 'empathie') L.push([tps(p.mal), 'coeur', .9], [tps(p.toi), 'coeur', 1], [tps(p.toi) + .45, 'coeur', .8]);
  if (p.type === 'portail') L.push(p.crash ? [p.a, 'glitch', .4] : [p.a, 'montee', .6]);
  if (p.type === 'route') L.push([p.a, 'whoosh', .4]);
  if (p.type === 'citation') { for (let k = 0; k < 14; k += 2) L.push([p.a + .8 * k / 14, 'tic', .3]); if (p.trad) L.push([tps(p.trad), 'lame', .5]); }
  if (p.type === 'autrice') { for (let k = 0; k < 6; k++) L.push([p.a + .1 + k * .12, 'frappe', .25]); if (p.tampon) L.push([tps(p.tampon) + .05, 'tampon', 1]); }
  if (p.type === 'journaux') L.push([p.a, 'papier', .5], [p.a + .3, 'papier', .4]);
  if (p.type === 'liste') { p.items.forEach(([, a]) => L.push([tps(a), 'valide', .5])); if (p.fin) L.push([tps(p.fin), 'clic', .5]); }
  if (p.type === 'note') { if (p.ecrit) L.push([tps(p.ecrit), 'stylo', .6]); else L.push([p.a, 'papier', .4]); }
  if (p.type === 'classement') { L.push([p.a, 'papier', .4]); if (p.etape === 1) L.push([p.a + .45, 'tampon', .9]); if (p.entre) L.push([tps(p.entre), 'valide', .9]); }
  if (p.type === 'programme') L.push([p.a, 'papier', .4], [p.a + .35, 'stylo', .5]);
  if (p.type === 'boucle') for (let k = 0; k < 6; k++) L.push([p.a + .3 + k * .1, 'frappe', .2]);
};
