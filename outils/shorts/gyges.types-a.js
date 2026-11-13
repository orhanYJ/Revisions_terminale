// Plans propres au short « L'anneau de Gygès », dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
// Zone de dessin : y de 300 à 1250 ; titre vers 1400 ; les sous-titres du modèle sont à 1660.
window.SANS_ST_A = [];
window.PROPRES_A = ['oeil', 'berger', 'tableau', 'orage', 'faille', 'cheval', 'geant', 'anneau', 'chaton', 'bergers', 'essais',
  'palais', 'cour', 'justes', 'rouleau'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const BRONZE = '#8a6436', SOMBRE = '#1b1712';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const sous = (s, y) => S.texte(s, W / 2, y, { taille: 58, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8, max: 960 });

  // silhouette debout, (x, y) = pieds, hauteur ~ 410 × s ; o : fond, trait, a (opacité), pointille, couronne, baton
  function homme(x, y, s, o = {}) {
    g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha *= (o.a ?? 1);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || CREME; g.lineWidth = o.ep || 7; g.lineJoin = 'round';
    if (o.pointille) { g.setLineDash([16, 14]); g.fillStyle = 'rgba(0,0,0,0)'; }
    g.beginPath(); g.moveTo(-58, -300); g.quadraticCurveTo(0, -322, 58, -300); g.lineTo(88, -95); g.lineTo(58, -95); g.lineTo(48, 0);
    g.lineTo(10, 0); g.lineTo(0, -85); g.lineTo(-10, 0); g.lineTo(-48, 0); g.lineTo(-58, -95); g.lineTo(-88, -95); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.arc(0, -362, 50, 0, 7); g.fill(); g.stroke();
    g.setLineDash([]);
    if (o.couronne) { g.fillStyle = OR; g.beginPath(); g.moveTo(-44, -398); g.lineTo(-44, -444); g.lineTo(-22, -420); g.lineTo(0, -454); g.lineTo(22, -420); g.lineTo(44, -444); g.lineTo(44, -398); g.closePath(); g.fill(); }
    if (o.baton) { g.strokeStyle = o.trait || CREME; g.lineWidth = 9; g.beginPath(); g.moveTo(105, 0); g.lineTo(105, -380); g.quadraticCurveTo(105, -440, 62, -425); g.stroke(); }
    g.restore();
  }
  // silhouette assise, (x, y) = sol, hauteur ~ 330 × s
  function assis(x, y, s, o = {}) {
    g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha *= (o.a ?? 1);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || CREME; g.lineWidth = o.ep || 7; g.lineJoin = 'round';
    if (o.pointille) { g.setLineDash([16, 14]); g.fillStyle = 'rgba(0,0,0,0)'; }
    g.beginPath(); g.moveTo(-55, -225); g.quadraticCurveTo(0, -245, 55, -225); g.lineTo(78, -72); g.quadraticCurveTo(125, -62, 115, 0);
    g.lineTo(-115, 0); g.quadraticCurveTo(-125, -62, -78, -72); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.arc(0, -285, 47, 0, 7); g.fill(); g.stroke();
    g.restore();
  }
  // bague vue de trois quarts : anneau d'or, chaton (pierre) en haut ; tourne = largeur apparente (0..1)
  function bague(cx, cy, R, tourne = 1, lueur = 0) {
    const rx = R * (.22 + .78 * Math.abs(tourne)), ry = R * .42;
    g.save();
    if (lueur) { const gl = g.createRadialGradient(cx, cy, 10, cx, cy, R * 2.2); gl.addColorStop(0, `rgba(217,180,90,${.45 * lueur})`); gl.addColorStop(1, 'rgba(217,180,90,0)'); g.fillStyle = gl; g.fillRect(cx - R * 2.5, cy - R * 2.5, R * 5, R * 5); }
    g.lineWidth = R * .2; g.strokeStyle = '#8f6a26'; g.beginPath(); g.ellipse(cx, cy + R * .05, rx, ry, 0, 0, 7); g.stroke();
    g.lineWidth = R * .14; g.strokeStyle = OR; g.beginPath(); g.ellipse(cx, cy, rx, ry, 0, 0, 7); g.stroke();
    g.lineWidth = R * .04; g.strokeStyle = '#fff3c4'; g.beginPath(); g.ellipse(cx, cy - R * .02, rx, ry, 0, Math.PI * 1.1, Math.PI * 1.6); g.stroke();
    // chaton
    g.fillStyle = OR; g.beginPath(); g.ellipse(cx, cy - ry - R * .06, R * .3, R * .2, 0, 0, 7); g.fill();
    g.fillStyle = ROUGE; g.beginPath(); g.ellipse(cx, cy - ry - R * .08, R * .2, R * .13, 0, 0, 7); g.fill();
    g.fillStyle = 'rgba(255,255,255,.7)'; g.beginPath(); g.arc(cx - R * .07, cy - ry - R * .13, R * .04, 0, 7); g.fill();
    g.restore();
  }

  // l'œil : etat 'ferme' (il se ferme : personne ne te voit), 'peur' (grand ouvert, il te surveille)
  function oeil(p, t) {
    const lt = t - p.a, peur = p.etat === 'peur';
    const ouv = peur ? lerp(.25, 1, eo(pr(t, p.a, .35))) : lerp(1, .04, eo(pr(t, p.a + .5, 1.7)));
    const cx = W / 2, cy = 820, L = 430, h = 250 * ouv;
    if (peur) for (let i = 0; i < 3; i++) { const k = (lt * .9 + i / 3) % 1; g.save(); g.globalAlpha = (1 - k) * .6; g.strokeStyle = ROUGE; g.lineWidth = 8;
      g.beginPath(); g.ellipse(cx, cy, L + k * 160, 260 + k * 160, 0, 0, 7); g.stroke(); g.restore(); }
    const amande = () => { g.beginPath(); g.moveTo(cx - L, cy); g.quadraticCurveTo(cx, cy - h * 2, cx + L, cy); g.quadraticCurveTo(cx, cy + h * 2, cx - L, cy); g.closePath(); };
    g.save(); amande(); g.fillStyle = '#e9dfc8'; g.fill(); g.clip();
    const dx = peur ? Math.sin(lt * 2.4) * 70 : 0;
    g.fillStyle = peur ? ROUGE : '#6b5434'; g.beginPath(); g.arc(cx + dx, cy, 160, 0, 7); g.fill();
    g.fillStyle = NOIR; g.beginPath(); g.arc(cx + dx, cy, peur ? 50 : 72, 0, 7); g.fill();
    g.fillStyle = 'rgba(255,255,255,.8)'; g.beginPath(); g.arc(cx + dx + 45, cy - 50, 22, 0, 7); g.fill();
    g.restore();
    g.strokeStyle = CREME; g.lineWidth = 12; g.lineJoin = 'round'; amande(); g.stroke();
    for (let i = -4; i <= 4; i++) { const x = cx + i * 85, y = cy - h * 2 * (1 - (i / 5) ** 2) / 2 - 4; g.lineWidth = 7; g.beginPath(); g.moveTo(x, y); g.lineTo(x + i * 8, y - 50 * Math.max(.3, ouv)); g.stroke(); }
    deux(p.t, 1400, 115);
  }

  function mouton(x, y, s, ph) {
    g.save(); g.translate(x, y + Math.sin(ph) * 4); g.scale(s, s);
    g.strokeStyle = CREME; g.lineWidth = 6; [-35, 30].forEach(dx => { g.beginPath(); g.moveTo(dx, 20); g.lineTo(dx, 70); g.stroke(); });
    g.fillStyle = '#d9cdb2'; [[-50, 0, 40], [-10, -20, 46], [35, 0, 42], [-5, 22, 40], [15, 15, 38]].forEach(([a, b, r]) => { g.beginPath(); g.arc(a, b, r, 0, 7); g.fill(); });
    g.fillStyle = '#16120e'; g.beginPath(); g.ellipse(80, -10, 26, 34, .3, 0, 7); g.fill();
    g.restore();
  }
  // le berger et le troupeau, sur les collines de Lydie
  function berger(p, t) {
    const lt = t - p.a;
    const gr = g.createLinearGradient(0, 380, 0, 1250); gr.addColorStop(0, '#0d0b09'); gr.addColorStop(1, '#4a3520'); g.fillStyle = gr; g.fillRect(0, 380, W, 870);
    const sol = g.createRadialGradient(820, 900, 10, 820, 900, 300); sol.addColorStop(0, 'rgba(217,180,90,.6)'); sol.addColorStop(1, 'rgba(217,180,90,0)'); g.fillStyle = sol; g.fillRect(400, 500, 680, 700);
    g.fillStyle = '#26201a'; g.beginPath(); g.moveTo(0, 1000); g.quadraticCurveTo(300, 860, 620, 960); g.quadraticCurveTo(860, 1030, W, 920); g.lineTo(W, 1250); g.lineTo(0, 1250); g.closePath(); g.fill();
    g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(0, 1120); g.quadraticCurveTo(540, 1040, W, 1110); g.lineTo(W, 1250); g.lineTo(0, 1250); g.closePath(); g.fill(); g.stroke();
    homme(250, 1180, .95, { baton: true, trait: OR, fond: '#16120e' });
    [[520, 1170, .75], [680, 1150, .7], [840, 1175, .75], [600, 1225, .8], [960, 1215, .72]].forEach(([x, y, s], i) => mouton(x + Math.sin(lt * .8 + i) * 8, y, s, lt * 3 + i));
    deux(p.t, 1400, 110);
  }

  // une image du domaine public en carte découpée, recadrée sur (fx, fy) ; légende en petit
  function tableau(p, t, l) {
    const k = eo(pr(t, p.a, .35)), w = p.w || 800, h = p.h || 880, cy = lerp(800, 760, k);
    O.carte(p.img, W / 2, cy, w, h, lerp(.05, -.025, k), (p.z || 1) * (1 + l * .03), p.fx ?? .5, p.fy ?? .5, { lum: .95 });
    const yb = 760 + h / 2;
    if (p.t) deux(p.t, yb + 140, 110);
    if (p.sous) sous(p.sous, yb + 265);
    if (p.leg) S.texte(p.leg, W / 2, p.sous ? yb + 335 : yb + 275, { taille: 32, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 960 });
  }

  // l'orage ; p.tremble : la terre tremble
  function orage(p, t) {
    const lt = t - p.a;
    g.fillStyle = '#0a0908'; g.fillRect(0, 330, W, 920);
    for (let i = 0; i < 8; i++) { g.fillStyle = i % 2 ? '#2a241d' : '#221d17'; g.beginPath(); g.ellipse((i * 170 + lt * 30) % (W + 300) - 150, 420 + (i % 3) * 60, 230, 95, 0, 0, 7); g.fill(); }
    g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 3;
    for (let i = 0; i < 80; i++) { const x = (rnd(i) * (W + 200) + lt * 150) % (W + 200) - 100, y = 440 + (rnd(i + 7) * 800 + lt * 1700) % 800; g.beginPath(); g.moveTo(x, y); g.lineTo(x - 18, y + 55); g.stroke(); }
    let fl = 0; [.1, .75, 1.5].forEach(f => { if (t >= p.a + f) fl = Math.max(fl, 1 - pr(t, p.a + f, .3)); });
    if (fl > 0) {
      g.save(); g.globalAlpha = fl * .35; g.fillStyle = '#fff6d8'; g.fillRect(0, 330, W, 920); g.restore();
      g.save(); g.globalAlpha = fl; g.strokeStyle = '#fff3c4'; g.shadowColor = OR; g.shadowBlur = 40; g.lineWidth = 12; g.lineJoin = 'round';
      g.beginPath(); let x = 600, y = 440; g.moveTo(x, y); for (let s = 0; s < 7; s++) { x += (rnd(s * 3 + Math.floor((t - p.a) / .75)) - .5) * 160; y += 95; g.lineTo(x, y); } g.stroke(); g.restore();
    }
    const sec = p.tremble ? Math.sin(lt * 70) * 18 * (1 - pr(t, p.a, 1.5)) : 0;
    g.save(); g.translate(sec, p.tremble ? Math.cos(lt * 53) * 8 * (1 - pr(t, p.a, 1.5)) : 0);
    g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(-40, 1130); g.lineTo(W + 40, 1110); g.lineTo(W + 40, 1260); g.lineTo(-40, 1260); g.closePath(); g.fill(); g.stroke();
    if (p.tremble) { const n = Math.floor(lerp(1, 5, pr(t, p.a, 1.2))); g.strokeStyle = ROUGE; g.lineWidth = 6;
      for (let f = 0; f < n; f++) { g.beginPath(); let x = 200 + f * 170, y = 1122; g.moveTo(x, y); for (let s = 0; s < 4; s++) { x += (rnd(f * 9 + s) - .5) * 80; y += 30; g.lineTo(x, y); } g.stroke(); } }
    g.restore();
    deux(p.t, 1400, 115);
  }

  // la faille qui s'ouvre ; p.descente : la descente entre les parois
  function faille(p, t) {
    const lt = t - p.a;
    if (!p.descente) {
      const w = lerp(10, 300, eo(pr(t, p.a + .1, 1.1))), cx = W / 2;
      g.fillStyle = '#0a0908'; g.fillRect(0, 330, W, 920);
      const gl = g.createRadialGradient(cx, 1250, 10, cx, 1250, 400); gl.addColorStop(0, `rgba(217,180,90,${.5 * pr(t, p.a + .3, 1)})`); gl.addColorStop(1, 'rgba(217,180,90,0)'); g.fillStyle = gl; g.fillRect(0, 800, W, 450);
      const bord = (sgn) => { g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath();
        const xb = cx + sgn * w / 2; g.moveTo(sgn < 0 ? -40 : W + 40, 900); g.lineTo(xb + sgn * 40, 900);
        for (let s = 1; s <= 7; s++) g.lineTo(xb + sgn * (rnd(s + (sgn > 0 ? 20 : 0)) * 70), 900 + s * 50);
        g.lineTo(sgn < 0 ? -40 : W + 40, 1250); g.closePath(); g.fill(); g.stroke(); };
      bord(-1); bord(1);
      for (let i = 0; i < 6; i++) { const k = cl((lt - .2 - i * .15) / .9); if (k <= 0 || k >= 1) continue; g.fillStyle = '#5b5247';
        g.beginPath(); g.arc(cx + (rnd(i) - .5) * w * .6, 880 + k * k * 380, 10 + rnd(i + 3) * 12, 0, 7); g.fill(); }
      deux(p.t, 1400, 115);
    } else {
      g.fillStyle = '#070605'; g.fillRect(0, 330, W, 920);
      const gl = g.createLinearGradient(0, 330, 0, 1250); gl.addColorStop(0, 'rgba(217,180,90,0)'); gl.addColorStop(1, `rgba(217,180,90,${.15 + .3 * pr(t, p.a, 1.5)})`); g.fillStyle = gl; g.fillRect(260, 330, 560, 920);
      [[0, 300], [780, W]].forEach(([x0, x1], j) => {
        g.fillStyle = '#26201a'; g.fillRect(x0, 330, x1 - x0, 920);
        g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 4;
        for (let i = 0; i < 12; i++) { const y = 330 + ((i * 95 - lt * 380) % 1140 + 1140) % 1140; g.beginPath(); g.moveTo(x0, y); g.lineTo(x1, y + (j ? -20 : 20)); g.stroke(); }
        g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(j ? x0 : x1, 330); g.lineTo(j ? x0 : x1, 1250); g.stroke();
      });
      homme(W / 2, 900 + Math.sin(lt * 3) * 12, .6, { trait: OR });
      deux(p.t, 1400, 115);
    }
  }

  // le cheval de bronze, creux, avec des portes ; p.portes : repère où les portes s'allument ; p.ouvre : la porte s'ouvre
  const CHEVAL = [[-280, -60], [-250, -100], [-150, -110], [40, -115], [110, -140], [170, -215], [215, -285], [228, -330], [245, -292],
    [275, -270], [335, -195], [350, -160], [330, -138], [255, -165], [200, -110], [175, -20], [178, 200], [188, 232], [142, 232], [136, 45],
    [100, 40], [96, 200], [104, 232], [58, 232], [60, 40], [-120, 40], [-140, 200], [-130, 232], [-176, 232], [-190, 60], [-240, 40],
    [-232, 200], [-222, 232], [-268, 232], [-286, 0]];
  function cheval(p, t) {
    const lt = t - p.a, s = 1.35, cx = W / 2 + 10, cy = 880;
    const gl = g.createRadialGradient(cx, cy, 50, cx, cy, 650); gl.addColorStop(0, 'rgba(217,180,90,.22)'); gl.addColorStop(1, 'rgba(217,180,90,0)'); g.fillStyle = gl; g.fillRect(0, 330, W, 920);
    const z = p.ouvre ? lerp(1, 1.9, eo(pr(t, p.a, 1.3))) : 1 + lt * .02, px = cx - 5 * s, py = cy - 30 * s;
    g.save(); g.translate(px, py); g.scale(z, z); g.translate(-px, -py);
    g.save(); g.translate(cx, cy); g.scale(s, s);
    const br = g.createLinearGradient(0, -330, 0, 232); br.addColorStop(0, '#b08a4e'); br.addColorStop(1, '#4e381c');
    g.fillStyle = br; g.strokeStyle = OR; g.lineWidth = 5; g.lineJoin = 'round';
    g.beginPath(); CHEVAL.forEach(([x, y], i) => i ? g.lineTo(x, y) : g.moveTo(x, y)); g.closePath(); g.fill(); g.stroke();
    g.lineWidth = 9; g.strokeStyle = BRONZE; g.beginPath(); g.moveTo(-272, -70); g.quadraticCurveTo(-345, -10, -322, 130); g.stroke();
    g.strokeStyle = 'rgba(255,243,196,.5)'; g.lineWidth = 3; for (let i = 0; i < 5; i++) { g.beginPath(); g.moveTo(120 + i * 22, -150 - i * 30); g.lineTo(150 + i * 22, -135 - i * 30); g.stroke(); }
    g.fillStyle = NOIR; g.beginPath(); g.arc(290, -228, 7, 0, 7); g.fill();
    // la porte (et sa jumelle de l'autre côté, invisible)
    const dx = -70, dy = -82, dw = 130, dh = 105;
    if (p.ouvre) { const ko = eo(pr(t, p.a + .15, .6)); g.fillStyle = '#050403'; g.fillRect(dx, dy, dw, dh);
      g.save(); g.globalAlpha = .4 * ko; const gi = g.createRadialGradient(dx + dw / 2, dy + dh / 2, 2, dx + dw / 2, dy + dh / 2, 70); gi.addColorStop(0, OR); gi.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = gi; g.fillRect(dx, dy, dw, dh); g.restore();
      g.fillStyle = '#6b4e28'; g.strokeStyle = OR; g.lineWidth = 3; g.fillRect(dx, dy, dw * (1 - ko * .85), dh); g.strokeRect(dx, dy, dw * (1 - ko * .85), dh); }
    else { const on = p.portes && t >= tps(p.portes), kp = on ? .5 + .5 * Math.sin((t - tps(p.portes)) * 10) : 0;
      g.strokeStyle = on ? `rgba(217,180,90,${.6 + .4 * kp})` : 'rgba(255,243,196,.55)'; g.lineWidth = on ? 7 : 3; g.strokeRect(dx, dy, dw, dh);
      g.fillStyle = OR; g.beginPath(); g.arc(dx + dw - 18, dy + dh / 2, 6, 0, 7); g.fill(); }
    g.restore(); g.restore();
    if (p.portes && t >= tps(p.portes)) { const k = back(pr(t, tps(p.portes), .3)); g.save(); g.translate(W / 2 - 230, 560); g.scale(k, k);
      S.texte('DES PORTES', 0, 0, { taille: 70, coul: ROUGE, contour: NOIR, contourL: 8 }); g.restore();
      S.d.fleche(W / 2 - 230, 610, cx - 80, cy - 70, eo(pr(t, tps(p.portes), .35)), { trait: ROUGE, ep: 9 }); }
    deux(p.t, 1400, 115);
  }

  // dans le cheval : un mort, plus grand qu'un homme, l'anneau au doigt ; p.grand : la comparaison
  function geant(p, t) {
    const lt = t - p.a;
    g.fillStyle = '#070605'; g.fillRect(0, 330, W, 920);
    g.strokeStyle = 'rgba(217,180,90,.35)'; g.lineWidth = 8; for (let i = 0; i < 5; i++) { g.beginPath(); g.arc(W / 2, 1300, 560 + i * 70, Math.PI * 1.08, Math.PI * 1.92); g.stroke(); }
    // le mort, allongé
    g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.arc(150, 1080, 62, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.roundRect(215, 1030, 420, 115, 50); g.fill(); g.stroke();
    g.beginPath(); g.roundRect(625, 1050, 160, 80, 30); g.fill(); g.stroke();
    // l'anneau
    const lu = .6 + .4 * Math.sin(lt * 6); bague(560, 1015, 34, Math.cos(lt * 2), lu);
    // un homme, pour comparer
    const kg = p.grand ? eo(pr(t, tps(p.grand), .4)) : 0;
    homme(935, 1150, .82, { pointille: true, trait: GRIS, a: .4 + .6 * kg });
    if (kg > 0) { g.save(); g.globalAlpha = kg; g.strokeStyle = OR; g.lineWidth = 6;
      g.beginPath(); g.moveTo(88, 960); g.lineTo(88 + 697 * kg, 960); g.stroke(); [88, 785].forEach(x => { g.beginPath(); g.moveTo(x, 940); g.lineTo(x, 980); g.stroke(); });
      g.beginPath(); g.moveTo(1035, 1150); g.lineTo(1035, 1150 - 336 * kg); g.stroke(); [1150, 814].forEach(y => { g.beginPath(); g.moveTo(1015, y); g.lineTo(1055, y); g.stroke(); });
      S.texte('PLUS GRAND QU’UN HOMME', W / 2, 600, { taille: 64, coul: ROUGE, contour: NOIR, contourL: 8, max: 960 }); g.restore(); }
    deux(p.t, 1400, 120);
  }

  // l'anneau d'or ; p.prend : la main le saisit ; p.doigt : au doigt (fin, boucle)
  function anneau(p, t) {
    const lt = t - p.a;
    if (!p.prend && !p.doigt) {
      g.save(); g.translate(W / 2, 820); g.rotate(lt * .3); g.fillStyle = 'rgba(217,180,90,.08)';
      for (let i = 0; i < 12; i++) { g.rotate(Math.PI / 6); g.beginPath(); g.moveTo(0, 0); g.lineTo(-60, -700); g.lineTo(60, -700); g.closePath(); g.fill(); }
      g.restore();
      const k = back(pr(t, p.a, .5)); bague(W / 2, lerp(600, 840, eo(pr(t, p.a, .6))), 230 * k, Math.cos(lt * 1.6), 1);
    } else {
      S.d.main(300, 900, .05, { trait: CREME, fond: '#2a241d', ep: 8 }, 1.4);
      if (p.prend) { const k = eo(pr(t, p.a + .15, .7)); bague(lerp(W / 2, 300 + 230 * 1.4, k), lerp(560, 860, k), lerp(160, 45, k), lerp(Math.cos(lt * 2), .35, k), 1 - k * .5);
        if (k >= 1) { const kv = pr(t, p.a + .85, .4); g.save(); g.globalAlpha = 1 - kv; g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.arc(300 + 322, 860, 40 + kv * 120, 0, 7); g.stroke(); g.restore(); } }
      else { bague(300 + 322, 860, 45, .35, .8 + .2 * Math.sin(lt * 5));
        const ke = pr(t, p.a + .4, .8); homme(860, 1180, .6, { pointille: true, trait: GRIS, a: 1 - .7 * ke }); }
    }
    deux(p.t, 1400, p.doigt ? 100 : 115);
  }

  // le chaton tourné vers la paume (sens 1) ou vers l'extérieur (sens -1) : coupe du doigt
  function chaton(p, t) {
    const cx = W / 2, cy = 830, k = eo(pr(t, p.a + .2, .8)), th = p.sens > 0 ? lerp(-Math.PI / 2, Math.PI / 2, k) : lerp(Math.PI / 2, -Math.PI / 2, k);
    S.texte('DOS DE LA MAIN', cx, cy - 330, { taille: 44, coul: GRIS, esp: 6, poids: 600 });
    S.texte('PAUME', cx, cy + 330, { taille: 44, coul: OR, esp: 6, poids: 600 });
    g.fillStyle = '#d8b48c'; g.strokeStyle = NOIR; g.lineWidth = 6; g.beginPath(); g.arc(cx, cy, 170, 0, 7); g.fill(); g.stroke();
    g.fillStyle = '#efd2b0'; g.beginPath(); g.arc(cx - 40, cy - 40, 60, 0, 7); g.fill();
    g.strokeStyle = OR; g.lineWidth = 38; g.beginPath(); g.arc(cx, cy, 196, 0, 7); g.stroke();
    g.strokeStyle = '#fff3c4'; g.lineWidth = 6; g.beginPath(); g.arc(cx, cy, 190, Math.PI * 1.1, Math.PI * 1.5); g.stroke();
    g.strokeStyle = ROUGE; g.lineWidth = 8; g.setLineDash([18, 14]); g.beginPath(); g.arc(cx, cy, 275, p.sens > 0 ? -Math.PI / 2 : Math.PI / 2, th, p.sens < 0); g.stroke(); g.setLineDash([]);
    g.save(); g.translate(cx + Math.cos(th) * 215, cy + Math.sin(th) * 215); g.rotate(th + Math.PI / 2);
    g.fillStyle = OR; g.beginPath(); g.roundRect(-55, -40, 110, 60, 12); g.fill();
    g.fillStyle = ROUGE; g.beginPath(); g.ellipse(0, -14, 38, 26, 0, 0, 7); g.fill(); g.restore();
    deux(p.t, 1400, 110);
  }

  // les bergers assis en cercle ; p.parle : bulles ; p.invisible : tu disparais (contour en pointillé)
  function bergers(p, t) {
    const lt = t - p.a;
    g.fillStyle = SOMBRE; g.fillRect(0, 1180, W, 70);
    const f = (Math.sin(lt * 13) + Math.sin(lt * 7.3)) * .5;
    const gl = g.createRadialGradient(W / 2, 850, 10, W / 2, 850, 320); gl.addColorStop(0, 'rgba(217,180,90,.5)'); gl.addColorStop(1, 'rgba(217,180,90,0)'); g.fillStyle = gl; g.fillRect(200, 650, 680, 600);
    const autres = [[170, 1150, .85], [370, 1010, .72], [710, 1010, .72], [910, 1150, .85]];
    autres.forEach(([x, y, s]) => assis(x, y, s, { fond: '#16120e', trait: CREME }));
    g.fillStyle = OR; g.beginPath(); g.moveTo(W / 2 - 40, 880); g.quadraticCurveTo(W / 2 - 20 + f * 10, 770, W / 2, 740 + f * 15); g.quadraticCurveTo(W / 2 + 25, 800, W / 2 + 40, 880); g.closePath(); g.fill();
    g.fillStyle = ROUGE; g.beginPath(); g.moveTo(W / 2 - 20, 880); g.quadraticCurveTo(W / 2, 820 + f * 10, W / 2 + 20, 880); g.closePath(); g.fill();
    const ki = p.invisible ? eo(pr(t, p.a, .7)) : 0;
    if (ki < 1) assis(W / 2, 1240, 1.05, { fond: '#16120e', trait: OR, ep: 9, a: 1 - ki });
    if (ki > 0) assis(W / 2, 1240, 1.05, { pointille: true, trait: OR, ep: 6, a: ki * (.35 + .2 * Math.sin(lt * 4)) });
    if (p.parle) autres.forEach(([x, y, s], i) => { const k = back(pr(t, p.a + .1 + i * .18, .3)); if (k <= 0) return;
      g.save(); g.translate(x + (x < W / 2 ? 40 : -40), y - 420 * s); g.scale(k, k); g.fillStyle = CREME; g.beginPath(); g.roundRect(-85, -55, 170, 110, 40); g.fill();
      g.beginPath(); g.moveTo(-10, 50); g.lineTo(x < W / 2 ? 10 : -30, 95); g.lineTo(20, 50); g.fill();
      S.texte(p.invisible ? '?' : '…', 0, -6, { taille: 80, coul: NOIR }); g.restore(); });
    deux(p.t, 1420, 110);
  }

  // les essais : visible, invisible, visible… ; p.compte : « ça marche à chaque fois » (coches)
  function essais(p, t) {
    const n = Math.floor((t - p.a) / .5), vis = n % 2 === 0, tc = tps(p.compte);
    const cx = 270, cy = 820;
    g.fillStyle = '#d8b48c'; g.beginPath(); g.arc(cx, cy, 90, 0, 7); g.fill();
    g.strokeStyle = OR; g.lineWidth = 22; g.beginPath(); g.arc(cx, cy, 104, 0, 7); g.stroke();
    const th = vis ? -Math.PI / 2 : Math.PI / 2;
    g.fillStyle = ROUGE; g.beginPath(); g.arc(cx + Math.cos(th) * 112, cy + Math.sin(th) * 112, 26, 0, 7); g.fill();
    S.texte(vis ? 'CHATON DEHORS' : 'CHATON DEDANS', cx, cy + 190, { taille: 34, coul: vis ? CREME : OR, poids: 600 });
    if (vis) homme(740, 1100, .95, { fond: '#16120e', trait: OR }); else homme(740, 1100, .95, { pointille: true, trait: GRIS, a: .5 });
    S.texte(vis ? 'VISIBLE' : 'INVISIBLE', 740, 1170, { taille: 44, coul: vis ? OR : GRIS, poids: 600 });
    if (t >= tc) for (let i = 0; i < 3; i++) { const k = back(pr(t, tc + i * .2, .25)); if (k <= 0) continue; g.save(); g.translate(270 + i * 0 + (i - 1) * 130, 1130); g.scale(k, k);
      g.fillStyle = OR; g.beginPath(); g.arc(0, 0, 48, 0, 7); g.fill(); S.texte('✓', 0, 4, { taille: 62, coul: NOIR }); g.restore(); }
    deux(t >= tc ? p.tbis : p.t, 1420, 110);
  }

  // le palais : tu marches vers la porte
  function palais(p, t) {
    const k = eo(pr(t, p.a, 2));
    g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(150, 640); g.lineTo(540, 450); g.lineTo(930, 640); g.closePath(); g.fill(); g.stroke();
    g.fillRect(150, 640, 780, 40); g.strokeRect(150, 640, 780, 40);
    for (let i = 0; i < 6; i++) { const x = 200 + i * 136; g.fillStyle = '#2a241d'; g.fillRect(x, 690, 56, 330); g.strokeRect(x, 690, 56, 330);
      g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 3; for (let j = 1; j < 3; j++) { g.beginPath(); g.moveTo(x + j * 18, 700); g.lineTo(x + j * 18, 1010); g.stroke(); } g.strokeStyle = CREME; g.lineWidth = 6; }
    for (let j = 0; j < 3; j++) { g.fillStyle = SOMBRE; g.fillRect(130 - j * 30, 1020 + j * 40, 820 + j * 60, 40); g.strokeRect(130 - j * 30, 1020 + j * 40, 820 + j * 60, 40); }
    g.fillStyle = 'rgba(217,180,90,.35)'; g.fillRect(476, 830, 128, 190);
    g.fillStyle = OR; g.beginPath(); g.arc(540, 560, 26, 0, 7); g.fill();
    homme(lerp(170, 540, k), lerp(1250, 1030, k), lerp(.95, .45, k), { pointille: true, trait: OR, a: .85 });
    deux(p.t, 1420, 115);
  }

  // à la cour : etape 'reine', 'roi' (il tombe), 'trone' (la couronne)
  function cour(p, t) {
    const lt = t - p.a;
    g.fillStyle = 'rgba(200,55,45,.25)'; g.beginPath(); g.moveTo(420, 1250); g.lineTo(480, 700); g.lineTo(600, 700); g.lineTo(660, 1250); g.closePath(); g.fill();
    [[90, 140], [880, 940]].forEach(([x0]) => { g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 5; g.fillRect(x0, 420, 90, 830); g.strokeRect(x0, 420, 90, 830); });
    g.fillStyle = SOMBRE; g.fillRect(0, 1200, W, 50);
    if (p.etape === 'reine') {
      homme(340, 1200, 1, { pointille: true, trait: OR });
      homme(720, 1200, 1, { couronne: true, fond: '#3a2c1a', trait: CREME });
      const k = back(pr(t, p.a + .3, .35)); if (k > 0) { g.save(); g.translate(530, 760); g.scale(k * (1 + .06 * Math.sin(lt * 8)), k * (1 + .06 * Math.sin(lt * 8)));
        g.fillStyle = ROUGE; g.beginPath(); g.moveTo(0, 40); g.bezierCurveTo(-90, -20, -50, -90, 0, -45); g.bezierCurveTo(50, -90, 90, -20, 0, 40); g.fill(); g.restore(); }
    } else if (p.etape === 'roi') {
      homme(460, 1200, .75, { couronne: true, fond: '#3a2c1a', trait: GRIS, a: .6 });
      homme(270, 1200, 1, { pointille: true, trait: OR });
      const kc = eo(pr(t, p.a + .45, .6));
      g.save(); g.translate(700, 1200); g.rotate(kc * 1.35); homme(0, 0, 1.05, { couronne: true, fond: '#16120e', trait: CREME }); g.restore();
      const ks = pr(t, p.a + .25, .2); if (ks > 0) { g.save(); g.globalAlpha = 1 - pr(t, p.a + .7, .6); g.strokeStyle = ROUGE; g.lineWidth = 22; g.lineCap = 'round';
        g.beginPath(); g.moveTo(540, 640); g.lineTo(lerp(540, 900, ks), lerp(640, 960, ks)); g.stroke(); g.restore(); }
    } else {
      g.fillStyle = '#3a2c1a'; g.strokeStyle = OR; g.lineWidth = 7;
      g.beginPath(); g.roundRect(400, 560, 280, 520, 20); g.fill(); g.stroke(); g.beginPath(); g.roundRect(360, 1000, 360, 80, 12); g.fill(); g.stroke();
      [400, 680].forEach(x => { g.beginPath(); g.moveTo(x, 1080); g.lineTo(x, 1200); g.stroke(); });
      assis(W / 2, 1060, 1, { pointille: true, trait: OR, ep: 8 });
      const k = eo(pr(t, p.a + .1, .8)), y = lerp(380, 1060 - 285 - 48, k);
      g.save(); g.translate(W / 2, y); g.scale(1.3, 1.3); g.fillStyle = OR; g.shadowColor = OR; g.shadowBlur = 30 * k;
      g.beginPath(); g.moveTo(-44, 0); g.lineTo(-44, -46); g.lineTo(-22, -22); g.lineTo(0, -56); g.lineTo(22, -22); g.lineTo(44, -46); g.lineTo(44, 0); g.closePath(); g.fill(); g.restore();
    }
    deux(p.t, 1420, 115);
  }

  // le juste et l'injuste ; p.pareil : avec l'anneau, ils font pareil
  function justes(p, t) {
    const lt = t - p.a, kp = p.pareil ? eo(pr(t, p.a, .6)) : 0;
    [[320, 'LE JUSTE', OR], [760, 'L’INJUSTE', ROUGE]].forEach(([x, nom, c], i) => {
      if (kp < 1) homme(x, 1130, .95, { fond: '#16120e', trait: c, a: 1 - kp });
      if (kp > 0) homme(x + kp * (i ? -40 : 40), 1130, .95, { pointille: true, trait: c, a: kp * .8 });
      S.texte(nom, x, 1200, { taille: 50, coul: c, poids: 700 });
    });
    if (!p.pareil) { const k = eo(pr(t, p.a + .2, .8)); bague(lerp(W / 2, 395, k), lerp(450, 905, k), lerp(110, 36, k), Math.cos(lt * 2), 1); }
    else { bague(395, 905, 36, .4, .6); bague(835, 905, 36, .4, .6);
      const k = back(pr(t, p.a + .35, .3)); g.save(); g.translate(W / 2, 760); g.scale(k, k); S.texte('=', 0, 0, { taille: 220, coul: ROUGE, contour: NOIR, contourL: 12 }); g.restore(); }
    deux(p.t, 1400, 115);
  }

  // la République : le rouleau qui se déroule, sous le portrait de Platon
  function rouleau(p, t) {
    O.carte('platon', W / 2, 560, 300, 380, -.03, 1.05, .5, .3, { lum: .95 });
    const k = eo(pr(t, p.a + .1, .7)), w = lerp(60, 780, k), x0 = W / 2 - w / 2;
    g.fillStyle = '#e9dfc8'; g.fillRect(x0, 860, w, 280);
    g.fillStyle = OR; [x0 - 26, x0 + w - 4].forEach(x => { g.beginPath(); g.roundRect(x, 835, 30, 330, 14); g.fill(); });
    g.save(); g.beginPath(); g.rect(x0, 860, w, 280); g.clip();
    S.texte('LA RÉPUBLIQUE', W / 2, 950, { taille: 76, police: 'Spectral', poids: 600, coul: NOIR });
    S.texte('Platon · livres I à X', W / 2, 1030, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    for (let i = 0; i < 3; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(W / 2 - 300, 1075 + i * 18, 600 - i * 120, 5); }
    g.restore();
    deux(p.t, 1340, 110);
    if (p.sous) sous(p.sous, 1480);
  }

  return { oeil, berger, tableau, orage, faille, cheval, geant, anneau, chaton, bergers, essais, palais, cour, justes, rouleau };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'oeil') L.push([p.a, p.etat === 'peur' ? 'coeur' : 'souffle', .5]);
  if (p.type === 'berger') L.push([p.a, 'souffle', .3]);
  if (p.type === 'tableau') L.push([p.a, 'papier', .3]);
  if (p.type === 'orage') { L.push([p.a + .1, 'boum', p.tremble ? .5 : .7], [p.a + .75, 'souffle', .4]); if (p.tremble) L.push([p.a + .3, 'frotte', .6]); }
  if (p.type === 'faille') L.push([p.a, p.descente ? 'whoosh' : 'frotte', .45]);
  if (p.type === 'cheval') { if (p.ouvre) L.push([p.a + .15, 'aspire', .55]); else L.push([p.a, 'gong', .35]); if (p.portes) L.push([tps(p.portes), 'blip', .5]); }
  if (p.type === 'geant') { L.push([p.a, 'coeur', .7]); if (p.grand) L.push([tps(p.grand), 'montee', .4]); }
  if (p.type === 'anneau') L.push([p.a, p.prend ? 'valide' : 'pop', .5]);
  if (p.type === 'chaton') L.push([p.a + .2, 'aspire', .5]);
  if (p.type === 'bergers') { if (p.invisible) L.push([p.a, 'aspire', .6]); if (p.parle) L.push([p.a + .1, 'pop', .3], [p.a + .46, 'pop', .3]); }
  if (p.type === 'essais') { for (let k = 0; k < 4; k++) L.push([p.a + k * .5, 'blip', .3]); for (let i = 0; i < 3; i++) L.push([tps(p.compte) + i * .2, 'valide', .35]); }
  if (p.type === 'palais') L.push([p.a, 'frotte', .3]);
  if (p.type === 'cour') { if (p.etape === 'roi') L.push([p.a + .25, 'lame', .9]); else if (p.etape === 'trone') L.push([p.a + .85, 'gong', .5]); else L.push([p.a + .3, 'pop', .4]); }
  if (p.type === 'justes') L.push([p.a + .35, p.pareil ? 'tampon' : 'pop', p.pareil ? .7 : .35]);
  if (p.type === 'rouleau') L.push([p.a + .1, 'papier', .5]);
};
