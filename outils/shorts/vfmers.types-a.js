// Plans propres au short « Vrai ou faux : les océans », dans le style du modèle A (noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs). Les plans vraifaux sont communs (formats-a.js).
window.SANS_ST_A = ['archive', 'chrono', 'part', 'eiffel', 'suez', 'cable', 'saisons', 'brise', 'zee', 'km2', 'commentaire'];
window.PROPRES_A = ['archive', 'chrono', 'part', 'eiffel', 'suez', 'cable', 'saisons', 'brise', 'zee', 'km2', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const MER = '#14202a', MER2 = '#1d3140', SABLE = '#4a3e2e', GLACE = '#dfe7ea';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const croix = (x, y, r, k) => { if (k <= 0) return; g.save(); g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round'; g.beginPath();
    g.moveTo(x - r, y - r); g.lineTo(x - r + 2 * r * cl(k * 2), y - r + 2 * r * cl(k * 2)); if (k > .5) { const k2 = cl(k * 2 - 1); g.moveTo(x + r, y - r); g.lineTo(x + r - 2 * r * k2, y - r + 2 * r * k2); } g.stroke(); g.restore(); };

  // porte-conteneurs de profil, proue à droite ; (x, y) = milieu de la ligne de flottaison, L = longueur
  function navire(x, y, L, coul = OR) {
    g.save(); g.translate(x, y);
    const h = L * .09;
    g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 5;
    g.beginPath(); g.moveTo(-L / 2, -h); g.lineTo(L / 2 - L * .04, -h); g.lineTo(L / 2, -h * 1.15); g.lineTo(L / 2 - L * .06, h * .45); g.lineTo(-L / 2 + L * .03, h * .45); g.closePath(); g.fill(); g.stroke();
    // conteneurs empilés
    const cols = 14, cw = (L * .72) / cols;
    for (let c = 0; c < cols; c++) for (let r = 0; r < 4; r++) {
      g.fillStyle = [coul, ROUGE, '#8f8a82', '#5d7f8f'][(c * 3 + r * 5) % 4];
      g.fillRect(-L / 2 + L * .14 + c * cw + 1, -h - (r + 1) * cw * .62, cw - 2, cw * .62 - 2);
    }
    // passerelle
    g.fillStyle = CREME; g.fillRect(-L / 2 + L * .03, -h - cw * 3.4, L * .08, cw * 3.4);
    g.fillStyle = NOIR; g.fillRect(-L / 2 + L * .04, -h - cw * 3.1, L * .06, cw * .5);
    g.restore();
  }

  // photo en carte + titre
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

  // 80 % du commerce mondial en volume : le navire, puis la barre qui se remplit
  function part(p, t, l) {
    O.petitTitre('— LE COMMERCE MONDIAL —', 420);
    const k = eo(pr(t, p.a + .1, .9));
    // mer et navire qui avance
    g.fillStyle = MER2; g.fillRect(0, 760, W, 60);
    navire(lerp(380, 600, eo(pr(t, p.a, 2.5))), 770, 640);
    // barre
    g.fillStyle = 'rgba(239,230,210,.12)'; g.fillRect(90, 930, 900, 110);
    g.fillStyle = OR; g.fillRect(90, 930, 900 * .8 * k, 110);
    g.strokeStyle = CREME; g.lineWidth = 4; g.strokeRect(90, 930, 900, 110);
    S.texte('PAR LA MER', 90 + 360, 986, { taille: 52, coul: NOIR, max: 680 });
    const n = Math.round(80 * k);
    S.texte(n + ' %', W / 2, 1250, { taille: 250, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14, ombre: 'rgba(217,180,90,.4)', flou: 40 });
    S.texte('en volume', W / 2, 1420, { taille: 74, police: 'Spectral', it: true, poids: 500, coul: CREME });
  }

  // l'Ever Given couché à côté de la tour Eiffel debout
  function eiffel(p, t) {
    const k = eo(pr(t, p.a, .5)), kn = eo(pr(t, p.a + .4, .6));
    // la tour (hauteur 560)
    const bx = 250, by = 1230, Ht = 560;
    g.save(); g.globalAlpha = k; g.strokeStyle = CREME; g.lineWidth = 6; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(bx - 120, by); g.quadraticCurveTo(bx - 40, by - Ht * .45, bx - 10, by - Ht); g.lineTo(bx + 10, by - Ht); g.quadraticCurveTo(bx + 40, by - Ht * .45, bx + 120, by); g.stroke();
    g.beginPath(); g.arc(bx, by, 70, Math.PI, 0); g.stroke();
    [[.28, 80], [.55, 45], [.8, 22]].forEach(([u, w]) => { g.beginPath(); g.moveTo(bx - w, by - Ht * u); g.lineTo(bx + w, by - Ht * u); g.stroke(); });
    g.beginPath(); g.moveTo(bx, by - Ht); g.lineTo(bx, by - Ht - 50); g.stroke();
    g.restore();
    S.texte('LA TOUR EIFFEL', bx, by + 60, { taille: 34, coul: CREME, poids: 700 });
    // le navire, plus long que la tour n'est haute
    const L = Ht * 1.2;
    g.save(); g.globalAlpha = kn; navire(lerp(W + 400, 680, kn), 1150, L * .62); g.restore();
    if (kn > .9) {
      g.save(); g.strokeStyle = OR; g.lineWidth = 4; g.setLineDash([12, 10]);
      g.beginPath(); g.moveTo(bx + 150, by - Ht); g.lineTo(bx + 150, by); g.stroke(); g.restore();
    }
    O.petitTitre('— 23 MARS 2021 —', 420);
    deux('L’EVER GIVEN|PLUS LONG QUE LA TOUR', 1450, 96);
  }

  // le canal de Suez vu du ciel : le navire pivote et bouche tout
  function suez(p, t) {
    const k = eo(pr(t, p.a + .1, .6));
    g.fillStyle = SABLE; g.fillRect(0, 380, W, 1080);
    g.fillStyle = MER2; g.beginPath(); g.moveTo(450, 380); g.lineTo(630, 380); g.lineTo(620, 1460); g.lineTo(460, 1460); g.closePath(); g.fill();
    S.texte('MÉDITERRANÉE', W / 2, 340, { taille: 40, coul: CREME, esp: 6 });
    S.texte('MER ROUGE', W / 2, 1510, { taille: 40, coul: CREME, esp: 6 });
    S.texte('CANAL', 240, 900, { taille: 44, coul: CREME, poids: 700 });
    S.texte('DE SUEZ', 240, 960, { taille: 44, coul: CREME, poids: 700 });
    g.save(); g.translate(540, 920); g.rotate(lerp(Math.PI / 2, Math.PI / 2 + .9, k));
    navire(0, 0, 330); g.restore();
    // navires qui attendent
    for (let i = 0; i < 4; i++) { const kk = eo(pr(t, p.a + .4 + i * .1, .3)); if (kk <= 0) continue;
      g.save(); g.globalAlpha = kk; g.fillStyle = CREME; g.beginPath(); g.ellipse(540, 450 + i * 70, 14, 28, 0, 0, 7); g.fill();
      g.beginPath(); g.ellipse(540, 1400 - i * 70, 14, 28, 0, 0, 7); g.fill(); g.restore(); }
    croix(540, 920, 120, pr(t, p.a + .7, .3));
    S.texte('BLOQUÉ', 820, 1180, { taille: 70, coul: ROUGE, contour: NOIR, contourL: 8 });
  }

  // vue en coupe : la surface, l'eau, le câble posé au fond, des données qui filent ; le satellite barré
  function cable(p, t) {
    const lt = t - p.a, ys = 640, yf = 1180;
    const gr = g.createLinearGradient(0, ys, 0, yf); gr.addColorStop(0, MER2); gr.addColorStop(1, '#0b1218'); g.fillStyle = gr; g.fillRect(0, ys, W, yf - ys);
    g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath();
    for (let x = 0; x <= W; x += 10) g.lineTo(x, ys + Math.sin(x * .03 + lt * 3) * 8); g.stroke();
    g.fillStyle = SABLE; g.beginPath(); g.moveTo(0, yf); for (let x = 0; x <= W; x += 60) g.lineTo(x, yf + Math.sin(x * .02) * 18); g.lineTo(W, 1300); g.lineTo(0, 1300); g.closePath(); g.fill();
    // le câble et les impulsions
    const k = eo(pr(t, p.a, .7));
    g.strokeStyle = '#111'; g.lineWidth = 16; g.beginPath(); g.moveTo(0, yf - 6); for (let x = 0; x <= W * k; x += 20) g.lineTo(x, yf - 6 + Math.sin(x * .02) * 18); g.stroke();
    g.strokeStyle = OR; g.lineWidth = 6; g.stroke();
    for (let i = 0; i < 6; i++) { const x = ((lt * 520 + i * 190) % (W + 100)) - 50; if (x > W * k) continue;
      g.save(); g.fillStyle = '#fff3c4'; g.shadowColor = OR; g.shadowBlur = 30; g.beginPath(); g.arc(x, yf - 6 + Math.sin(x * .02) * 18, 12, 0, 7); g.fill(); g.restore(); }
    // satellite barré
    g.save(); g.translate(860, 430); g.rotate(-.3); g.fillStyle = '#5d7f8f'; g.fillRect(-90, -16, 60, 32); g.fillRect(30, -16, 60, 32);
    g.fillStyle = CREME; g.fillRect(-26, -26, 52, 52); g.restore();
    croix(860, 430, 80, pr(t, p.a + .3, .35));
    S.texte('PAS LE SATELLITE', 380, 430, { taille: 48, coul: GRIS, poids: 700 });
    deux('DES CÂBLES|AU FOND DE LA MER', 1450, 104);
  }

  // l'Arctique vu du pôle : la banquise recule un temps, la route s'entrouvre
  function saisons(p, t) {
    const lt = t - p.a, cx = W / 2, cy = 850, R = 380;
    g.fillStyle = MER2; g.beginPath(); g.arc(cx, cy, R + 60, 0, 7); g.fill();
    const fonte = .5 + .5 * Math.sin(lt * 2.2 - Math.PI / 2), rg = lerp(R, R * .66, fonte);
    g.fillStyle = GLACE; g.beginPath();
    for (let i = 0; i <= 40; i++) { const a = i / 40 * 6.283, rr = rg * (.9 + .1 * rnd(i % 40 * 3.1)); i ? g.lineTo(cx + Math.cos(a) * rr, cy + Math.sin(a) * rr) : g.moveTo(cx + Math.cos(a) * rr, cy + Math.sin(a) * rr); }
    g.closePath(); g.fill();
    // continents en bordure (schéma)
    g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.arc(cx, cy, R + 60, 0, 7); g.stroke();
    // la route, ouverte seulement quand la glace recule
    g.save(); g.setLineDash([22, 16]); g.strokeStyle = fonte > .6 ? OR : 'rgba(217,180,90,.25)'; g.lineWidth = 9;
    g.beginPath(); g.arc(cx, cy, R * .82, Math.PI * .85, Math.PI * 2.15); g.stroke(); g.restore();
    S.texte(fonte > .6 ? 'OUVERT' : 'FERMÉ', cx, cy, { taille: 76, coul: fonte > .6 ? OR : NOIR });
    O.petitTitre('— L’ARCTIQUE · SCHÉMA —', 380);
    deux('PEU DE TEMPS|À LA FIN DE L’ÉTÉ', 1450, 104);
  }

  // un brise-glace ouvre la voie, un navire suit
  function brise(p, t) {
    const lt = t - p.a, xb = lerp(-100, 760, eo(pr(t, p.a, 2.2))), y = 1000;
    g.fillStyle = MER2; g.fillRect(0, y - 40, W, 120);
    // banquise découpée devant le brise-glace
    for (let i = 0; i < 18; i++) { const x = i * 64, de = x < xb + 120; if (de) continue;
      g.fillStyle = GLACE; g.beginPath(); g.moveTo(x, y - 40); g.lineTo(x + 60, y - 44 + rnd(i) * 8); g.lineTo(x + 60, y + 80); g.lineTo(x, y + 80); g.closePath(); g.fill(); }
    for (let i = 0; i < 10; i++) { const x = xb - 60 - i * 70; if (x < 0) break; g.fillStyle = 'rgba(223,231,234,.7)'; g.beginPath(); g.arc(x + rnd(i) * 30, y + 10 + rnd(i + 4) * 50, 10 + rnd(i + 7) * 14, 0, 7); g.fill(); }
    // le brise-glace (coque rouge)
    g.save(); g.translate(xb, y); g.fillStyle = ROUGE; g.strokeStyle = CREME; g.lineWidth = 5;
    g.beginPath(); g.moveTo(-160, -40); g.lineTo(120, -40); g.lineTo(190, 10); g.lineTo(110, 40); g.lineTo(-150, 40); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = CREME; g.fillRect(-120, -120, 110, 80); g.fillStyle = NOIR; g.fillRect(-100, -105, 70, 20); g.restore();
    S.texte('BRISE-GLACE', xb, y + 140, { taille: 40, coul: ROUGE, poids: 700 });
    // le cargo qui suit
    navire(xb - 520, y + 30, 420);
    deux('DERRIÈRE|DES BRISE-GLACE', 1450, 110);
  }

  // la ZEE française (schéma) : la métropole minuscule, les outre-mer et leurs cercles de 200 milles
  function zee(p, t) {
    const lt = t - p.a;
    g.fillStyle = MER; g.fillRect(40, 440, 1000, 860); g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 3; g.strokeRect(40, 440, 1000, 860);
    const ILES = [[230, 560, 'MÉTROPOLE', 0], [160, 860, 'MARTINIQUE', 0], [300, 1000, 'GUYANE', 0], [560, 1100, 'LA RÉUNION', 0],
      [830, 1090, 'NOUVELLE-CALÉDONIE', 0], [930, 860, 'POLYNÉSIE', 1]];
    ILES.forEach(([x, y, nom, poly], i) => {
      const k = eo(pr(t, p.a + .15 + i * .18, .5)); if (k <= 0) return;
      const r = (poly ? 150 : i === 0 ? 70 : 58) * k;
      g.save(); g.fillStyle = 'rgba(217,180,90,.28)'; g.strokeStyle = OR; g.lineWidth = 4; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.stroke(); g.restore();
      g.fillStyle = CREME; g.beginPath(); g.arc(x, y, i === 0 ? 16 : 7, 0, 7); g.fill();
      S.texte(nom, x, y + (i === 0 ? -95 : poly ? -175 : -80), { taille: 30, coul: CREME, poids: 700, max: 300 });
    });
    S.texte('schéma, pas à l’échelle', 1010, 1270, { taille: 28, police: 'Spectral', it: true, poids: 400, coul: GRIS, align: 'right' });
    O.petitTitre('— LA ZEE FRANÇAISE —', 380);
    deux('ZONE ÉCONOMIQUE|EXCLUSIVE', 1430, 100);
    S.texte('les ressources jusqu’à 200 milles des côtes', W / 2, 1560, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  // plus de 10 millions de km², deuxième du monde
  function km2(p, t) {
    const u = eo(pr(t, p.a, 1.0)), n = Math.round(lerp(0, 10, u));
    S.texte('PLUS DE', W / 2, 640, { taille: 70, coul: CREME, esp: 8 });
    S.texte(n + ' MILLIONS', W / 2, 820, { taille: 160, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12, max: 980 });
    S.texte('de km²', W / 2, 960, { taille: 84, police: 'Spectral', it: true, poids: 500, coul: CREME });
    O.tampon('2e DU MONDE', W / 2, 1250, pr(t, p.a + 1.0, .3), -.08, 120);
  }

  // une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .3)), txt = 'Mon score : … / 5', n = Math.floor(cl((t - p.a - .3) / .8) * txt.length);
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

  return { archive, chrono, part, eiffel, suez, cable, saisons, brise, zee, km2, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  if (p.type === 'archive') L.push([p.a, 'papier', .45]);
  if (p.type === 'chrono') L.push([p.a, 'clic', .7], [p.a + .3, 'tic', .5], [p.a + .6, 'tic', .5]);
  if (p.type === 'part') L.push([p.a + .1, 'montee', .45]);
  if (p.type === 'eiffel') L.push([p.a + .4, 'whoosh', .5]);
  if (p.type === 'suez') L.push([p.a + .1, 'frotte', .5], [p.a + .7, 'buzz', .45]);
  if (p.type === 'cable') L.push([p.a, 'blip', .4], [p.a + .3, 'coupe', .4]);
  if (p.type === 'saisons') L.push([p.a, 'souffle', .4]);
  if (p.type === 'brise') L.push([p.a, 'frotte', .5]);
  if (p.type === 'zee') for (let i = 0; i < 6; i++) L.push([p.a + .15 + i * .18, 'pop', .35]);
  if (p.type === 'km2') L.push([p.a, 'montee', .45], [p.a + 1.0, 'tampon', .9]);
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .3 + k * .1, 'tic', .25]); L.push([p.a + 1.2, 'pop', .5]); }
};
