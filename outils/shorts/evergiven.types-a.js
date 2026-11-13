// Plans propres au short Ever Given (« Un seul bateau »), dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
// Le canal est vu du ciel, nord en haut : le navire remonte vers la Méditerranée, la file d'attente est au sud (mer Rouge).
window.SANS_ST_A = ['canal', 'argent', 'route', 'choke', 'pelleteuse', 'chantier', 'lune', 'maree'];
window.PROPRES_A = ['canal', 'navire', 'tempete', 'route', 'argent', 'pelleteuse', 'chantier', 'lune', 'maree', 'choke'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const EAU = '#14202a', SABLE = '#5e4b31', SABLE2 = '#73603f', COQUE = '#2b2520';
  const COUL = [ROUGE, OR, '#4f6f7d', CREME, '#8b5a3c', '#3f5a48'];
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // valeur d'une suite d'étapes [[repère, valeur], …] (repère null = début du plan), avec la valeur précédente
  function etape(p, t) {
    let v = p.etapes[0][1], v0 = v, t0 = p.a;
    p.etapes.forEach(([a, x], i) => { const ta = a ? tps(a) : p.a; if (t >= ta) { v0 = i ? p.etapes[i - 1][1] : x; v = x; t0 = ta; } });
    return { v, v0, t0 };
  }

  // porte-conteneurs vu du ciel, proue vers le haut ; (cx, cy) centre, L longueur, l largeur, ang rotation
  function navireHaut(cx, cy, L, l, ang) {
    g.save(); g.translate(cx, cy); g.rotate(ang);
    g.fillStyle = COQUE; g.strokeStyle = CREME; g.lineWidth = 4;
    g.beginPath(); g.moveTo(0, -L / 2); g.quadraticCurveTo(l / 2, -L / 2 + l * .3, l / 2, -L / 2 + l * 1.1); g.lineTo(l / 2, L / 2 - 6);
    g.quadraticCurveTo(l / 2, L / 2, l / 2 - 6, L / 2); g.lineTo(-l / 2 + 6, L / 2); g.quadraticCurveTo(-l / 2, L / 2, -l / 2, L / 2 - 6);
    g.lineTo(-l / 2, -L / 2 + l * 1.1); g.quadraticCurveTo(-l / 2, -L / 2 + l * .3, 0, -L / 2); g.closePath(); g.fill(); g.stroke();
    const cw = (l - 12) / 4, ch = Math.max(8, L / 26);
    for (let y = -L / 2 + l * 1.15, r = 0; y < L / 2 - l * .9; y += ch + 2, r++) {
      if (Math.abs(y - (L / 2 - l * 1.3)) < ch) continue;   // passerelle
      for (let c = 0; c < 4; c++) { g.fillStyle = COUL[Math.floor(rnd(r * 7 + c * 3 + 1) * COUL.length)]; g.globalAlpha = .85; g.fillRect(-l / 2 + 6 + c * cw, y, cw - 2, ch); }
    }
    g.globalAlpha = 1; g.fillStyle = CREME; g.fillRect(-l / 2 + 4, L / 2 - l * 1.3 - ch / 2, l - 8, ch * 1.2);
    g.restore();
  }
  // porte-conteneurs de profil, proue à droite ; (x, y) = milieu de la ligne de flottaison, L longueur
  function navireProfil(x, y, L, o = {}) {
    const h = L * .075;
    g.save(); g.translate(x, y); if (o.rot) g.rotate(o.rot);
    g.fillStyle = '#6e2a22'; g.fillRect(-L / 2 + 10, 0, L - 30, h * .35);          // carène rouge sous l'eau
    g.fillStyle = COQUE; g.strokeStyle = CREME; g.lineWidth = 5;
    g.beginPath(); g.moveTo(-L / 2, -h); g.lineTo(L / 2 - h * .4, -h); g.quadraticCurveTo(L / 2 + h * .5, -h * .2, L / 2 - h * .2, h * .35);
    g.lineTo(-L / 2 + 14, h * .35); g.lineTo(-L / 2, -h * .2); g.closePath(); g.fill(); g.stroke();
    // piles de conteneurs
    const n = 22, cw = (L * .82) / n, x0 = -L / 2 + L * .04;
    for (let i = 0; i < n; i++) {
      if (i === 3) continue;
      const hh = 5 + Math.floor(rnd(i * 5.1) * 2);
      for (let k = 0; k < hh; k++) { g.fillStyle = COUL[Math.floor(rnd(i * 13 + k * 7) * COUL.length)]; g.fillRect(x0 + i * cw, -h - (k + 1) * h * .42, cw - 2, h * .42 - 2); }
    }
    // passerelle (château) à l'arrière
    g.fillStyle = CREME; g.fillRect(x0 + 3 * cw, -h - h * 3.3, cw * .95, h * 3.3);
    g.fillStyle = NOIR; for (let k = 0; k < 4; k++) g.fillRect(x0 + 3 * cw + 4, -h - h * 3.1 + k * h * .75, cw * .95 - 8, h * .25);
    g.restore();
  }
  // berges et canal (vue du ciel) ; renvoie la géométrie
  const CX0 = 360, CX1 = 720, CY0 = 250, CY1 = 1010;
  function decor(t) {
    g.fillStyle = SABLE; g.fillRect(0, CY0, W, CY1 - CY0 + 380);
    for (let i = 0; i < 260; i++) { const x = rnd(i) * W, y = CY0 + rnd(i + 99) * (CY1 - CY0); if (x > CX0 - 6 && x < CX1 + 6) continue;
      g.fillStyle = i % 3 ? SABLE2 : '#4a3b27'; g.fillRect(x, y, 4 + rnd(i * 3) * 6, 3); }
    // mer au sud (golfe de Suez)
    g.fillStyle = EAU; g.fillRect(0, CY1, W, 390);
    g.beginPath(); g.moveTo(CX0, CY0); g.lineTo(CX1, CY0); g.lineTo(CX1, CY1); g.lineTo(CX0, CY1); g.closePath(); g.fill();
    g.strokeStyle = 'rgba(217,180,90,.14)'; g.lineWidth = 3;
    for (let i = 0; i < 12; i++) { const y = CY0 + ((i * 97 + t * 40) % (CY1 - CY0 + 380)); g.beginPath(); g.moveTo(CX0 + 30 + rnd(i) * 200, y); g.lineTo(CX0 + 90 + rnd(i) * 200, y); g.stroke(); }
    g.strokeStyle = CREME; g.lineWidth = 5; [CX0, CX1].forEach(x => { g.beginPath(); g.moveTo(x, CY0); g.lineTo(x, CY1); g.stroke(); });
    S.texte('CANAL DE SUEZ', 175, 300, { taille: 30, coul: CREME, poids: 700, esp: 3 });
    S.texte('N ↑', 960, 300, { taille: 40, coul: CREME });
    S.texte('MER ROUGE ↓', W / 2, CY1 + 30, { taille: 26, coul: GRIS, esp: 6, poids: 600 });
  }
  function sable(t, a, force = 1) {
    for (let i = 0; i < 90; i++) { const v = 700 + rnd(i * 3) * 900, x = ((rnd(i) * W + (t - a) * v) % (W + 200)) - 100, y = 280 + rnd(i + 7) * 1250;
      g.fillStyle = `rgba(214,170,100,${.25 + rnd(i * 5) * .45 * force})`; g.fillRect(x, y, 18 + rnd(i * 9) * 40, 3); }
  }
  function bouffee(x, y, k) {
    if (k <= 0 || k >= 1) return;
    g.save(); g.globalAlpha = 1 - k; g.fillStyle = '#c9a66b';
    for (let i = 0; i < 8; i++) { const a = i / 8 * 6.28, r = 20 + k * 90; g.beginPath(); g.arc(x + Math.cos(a) * r, y + Math.sin(a) * r, 14 * (1 - k) + 6, 0, 7); g.fill(); }
    g.restore();
  }

  // le canal vu du ciel : etat 'route', 'derape', 'travers', 'file' (p.etapes = nombre de navires), 'libre'
  function canal(p, t) {
    decor(t);
    const TH = 50 * Math.PI / 180, L = 480, l = 62, e = p.etat || 'travers', lt = t - p.a;
    let cx = 540, cy = 600, ang = TH;
    if (e === 'route') { ang = 0; cy = lerp(900, 640, eo(cl(lt / 3))); }
    if (e === 'derape') { ang = TH * eo(pr(t, p.a + .15, 1.1)); cy = lerp(660, 600, eo(pr(t, p.a, 1.2))); }
    if (e === 'libre') { const k = eo(pr(t, p.a + .1, 1.1)); ang = TH * (1 - k); cy = 600 - eo(pr(t, p.a + 1.2, 1.5)) * 260; }
    if (e === 'route' || e === 'libre') for (let i = 1; i < 6; i++) { g.strokeStyle = `rgba(239,230,210,${.25 - i * .04})`; g.lineWidth = 4;
      g.beginPath(); g.moveTo(cx - 30 - i * 8, cy + L / 2 + i * 40); g.lineTo(cx + 30 + i * 8, cy + L / 2 + i * 40); g.stroke(); }
    // file d'attente : petits navires dans le canal puis dans la mer
    if (e === 'file') {
      const { v, v0, t0 } = etape(p, t), n = Math.round(lerp(v0, v, eo(pr(t, t0, .6))));
      for (let i = 0; i < n; i++) {
        let x, y, w = 22, h = 54;
        if (i < 4) { x = 540 + (i % 2 ? 60 : -60); y = 880 + Math.floor(i / 2) * 75 - 40; }
        else { const j = i - 4, c = j % 24, r = Math.floor(j / 24); x = 60 + c * 41; y = CY1 + 62 + r * 18; w = 30; h = 12; if (r > 15) continue; }
        g.fillStyle = i % 7 ? CREME : OR; g.globalAlpha = .9; g.fillRect(x - w / 2, y, w, h);
      }
      g.globalAlpha = 1;
      const kn = back(pr(t, t0, .3)); g.save(); g.translate(W / 2, 1470); g.scale(lerp(1.4, 1, kn), lerp(1.4, 1, kn));
      S.texte((n >= 400 ? '+ DE ' : '') + n, 0, 0, { taille: 170, police: 'Spectral', poids: 600, coul: v >= 400 ? ROUGE : OR, contour: NOIR, contourL: 12 }); g.restore();
      S.texte('NAVIRES BLOQUÉS', W / 2, 1590, { taille: 50, coul: CREME, esp: 6, contour: NOIR, contourL: 8 });
    }
    g.save(); g.beginPath(); g.rect(0, CY0, W, 1200); g.clip(); navireHaut(cx, cy, L, l, ang); g.restore();
    if (p.sable) sable(t, p.a, 1);
    // chocs contre les berges
    const proue = [cx + Math.sin(ang) * L / 2, cy - Math.cos(ang) * L / 2], poupe = [cx - Math.sin(ang) * L / 2, cy + Math.cos(ang) * L / 2];
    if (p.avant) bouffee(...proue, pr(t, tps(p.avant), .7));
    if (p.arriere) bouffee(...poupe, pr(t, tps(p.arriere), .7));
    if (p.bloque && t >= tps(p.bloque)) O.tampon('BLOQUÉ', W / 2, 800, pr(t, tps(p.bloque), .3), -.1, 130);
    if (p.t && e !== 'file') deux(p.t, 1470, p.taille || 105);
  }

  // le navire de profil ; p.eiffel : il se dresse à côté de la tour Eiffel (400 m contre 330 m)
  function navire(p, t) {
    const lt = t - p.a;
    if (!p.eiffel) {
      g.strokeStyle = 'rgba(217,180,90,.18)'; g.lineWidth = 3;
      for (let i = 0; i < 6; i++) { g.beginPath(); for (let x = 0; x <= W; x += 20) { const y = 1020 + i * 45 + Math.sin(x * .02 + t * 2 + i) * 6; x ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); }
      const x = lerp(700, 540, eo(pr(t, p.a, .8))), z = p.zoom ? lerp(1, 1.25, eo(pr(t, p.a, 1.5))) : 1;
      g.save(); g.translate(540, 980); g.scale(z, z); g.translate(-540, -980);
      navireProfil(x, 1000, 980); g.restore();
      if (p.t) deux(p.t, 1400, p.taille || 110);
      if (p.sous) S.texte(p.sous, W / 2, 1540, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
      return;
    }
    // échelle : 1 m = 2,6 px ; sol à y = 1400
    const Y = 1400, s = 2.6, k = eo(pr(t, p.a + .1, .8));
    g.fillStyle = '#1b1712'; g.fillRect(0, Y, W, 30); g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath(); g.moveTo(40, Y); g.lineTo(1040, Y); g.stroke();
    // la tour (330 m), dessin au trait
    const tx = 760, th = 330 * s * eo(pr(t, p.a, .6)), base = 260;
    g.save(); g.strokeStyle = CREME; g.lineWidth = 5; g.lineJoin = 'round';
    const larg = u => base / 2 * Math.pow(1 - u, 2.1) + 6;   // u = 0 au pied, 1 au sommet
    g.beginPath(); for (let i = 0; i <= 30; i++) { const u = i / 30; g.lineTo(tx - larg(u), Y - u * th); } for (let i = 30; i >= 0; i--) { const u = i / 30; g.lineTo(tx + larg(u), Y - u * th); } g.stroke();
    [.18, .38, .62].forEach(u => { g.beginPath(); g.moveTo(tx - larg(u) - 10, Y - u * th); g.lineTo(tx + larg(u) + 10, Y - u * th); g.stroke(); });
    g.beginPath(); g.arc(tx, Y, base * .28, Math.PI, 0); g.stroke();
    g.lineWidth = 2; for (let i = 0; i < 26; i++) { const u0 = i / 26 * .95, u1 = u0 + .036; g.beginPath(); g.moveTo(tx - larg(u0), Y - u0 * th); g.lineTo(tx + larg(u1), Y - u1 * th); g.stroke(); }
    g.restore();
    // le navire qui se dresse (proue en haut)
    const L = 400 * s;
    g.save(); g.translate(330, Y); g.rotate(-Math.PI / 2 * k); navireProfil(L / 2, 0, L); g.restore();
    const ka = pr(t, p.a + .7, .3);
    if (ka > 0) {
      g.save(); g.globalAlpha = ka;
      g.strokeStyle = OR; g.lineWidth = 4; g.setLineDash([12, 10]); g.beginPath(); g.moveTo(140, Y - L); g.lineTo(1000, Y - L); g.stroke();
      g.strokeStyle = CREME; g.beginPath(); g.moveTo(560, Y - 330 * s); g.lineTo(1000, Y - 330 * s); g.stroke(); g.restore();
      S.texte('400 M', 470, Y - L - 40, { taille: 70, coul: OR, contour: NOIR, contourL: 8 });
      S.texte('330 M', 920, Y - 330 * s - 40, { taille: 60, coul: CREME, contour: NOIR, contourL: 8 });
    }
    S.texte('LE NAVIRE', 330, Y + 70, { taille: 40, coul: OR, poids: 700 });
    S.texte('LA TOUR EIFFEL', tx, Y + 70, { taille: 40, coul: CREME, poids: 700 });
  }

  // tempête de sable : le navire de profil, le vent pousse sur le mur de conteneurs ; p.voile : flèches et contour
  function tempete(p, t) {
    const gr = g.createLinearGradient(0, 300, 0, 1400); gr.addColorStop(0, '#3b2c1a'); gr.addColorStop(1, '#0d0b09'); g.fillStyle = gr; g.fillRect(0, 300, W, 1100);
    g.fillStyle = EAU; g.fillRect(0, 1060, W, 300);
    const pen = (p.voile ? eo(pr(t, p.a, 1.2)) : 0) * .05 + Math.sin(t * 3) * .008;
    navireProfil(560, 1060, 900, { rot: pen });
    sable(t, p.a, 1.3);
    if (p.voile) {
      const k = pr(t, p.a + .2, .5);
      g.save(); g.globalAlpha = k; g.strokeStyle = OR; g.lineWidth = 6; g.setLineDash([16, 10]); g.strokeRect(150, 760, 780, 240); g.restore();
      for (let i = 0; i < 4; i++) { const kk = pr(t, p.a + .3 + i * .12, .4); S.d.fleche(-40, 800 + i * 60, 130, 800 + i * 60, eo(kk), { trait: ROUGE, ep: 12 }); }
    }
    if (p.t) deux(p.t, 1440, p.taille || 110);
  }

  // l'Asie, l'Europe, l'Afrique en schéma ; Suez au milieu ; p.etape 2 : le détour par le Cap
  const EUROPE = [[60, 400], [300, 370], [520, 420], [560, 560], [430, 620], [250, 600], [80, 560]];
  const AFRIQUE = [[110, 700], [470, 690], [600, 760], [640, 980], [560, 1200], [440, 1400], [330, 1430], [270, 1200], [160, 960], [80, 800]];
  const ASIE = [[620, 380], [1040, 360], [1040, 1100], [900, 1040], [820, 900], [700, 860], [650, 760], [610, 640]];
  function poly(P, f, s) { g.beginPath(); P.forEach(([x, y], i) => i ? g.lineTo(x, y) : g.moveTo(x, y)); g.closePath(); g.fillStyle = f; g.fill(); g.strokeStyle = s; g.lineWidth = 4; g.stroke(); }
  function route(p, t) {
    g.fillStyle = EAU; g.fillRect(0, 330, W, 1180);
    poly(EUROPE, '#2a241d', CREME); poly(AFRIQUE, '#2a241d', CREME); poly(ASIE, '#2a241d', CREME);
    S.texte('EUROPE', 290, 490, { taille: 46, coul: CREME, poids: 700, esp: 4 });
    S.texte('AFRIQUE', 360, 1000, { taille: 46, coul: CREME, poids: 700, esp: 4 });
    S.texte('ASIE', 880, 560, { taille: 56, coul: CREME, poids: 700, esp: 4 });
    const sx = 600, sy = 690, k = eo(pr(t, p.a + .1, .9));
    // route courte Asie → Suez → Europe
    const pts = [[1000, 1180], [760, 1000], [640, 820], [sx, sy], [520, 650], [300, 660]];
    g.save(); g.strokeStyle = OR; g.lineWidth = 12; g.lineCap = 'round'; g.beginPath();
    const n = pts.length - 1, m = k * n; pts.forEach(([x, y], i) => { if (i <= m) i ? g.lineTo(x, y) : g.moveTo(x, y); });
    const i0 = Math.floor(m); if (i0 < n) { const u = m - i0; g.lineTo(lerp(pts[i0][0], pts[i0 + 1][0], u), lerp(pts[i0][1], pts[i0 + 1][1], u)); }
    g.stroke(); g.restore();
    const pu = (t * 1.3) % 1; g.save(); g.strokeStyle = ROUGE; g.globalAlpha = 1 - pu; g.lineWidth = 6; g.beginPath(); g.arc(sx, sy, 20 + pu * 70, 0, 7); g.stroke(); g.restore();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(sx, sy, 16, 0, 7); g.fill();
    S.texte('SUEZ', sx + 95, sy - 30, { taille: 44, coul: ROUGE, contour: NOIR, contourL: 6 });
    if (p.etape === 2) {
      const kd = eo(pr(t, p.a + .1, 1.3)), D = [[1000, 1180], [700, 1420], [420, 1480], [150, 1300], [30, 900], [40, 640], [300, 660]];
      g.save(); g.setLineDash([20, 16]); g.strokeStyle = 'rgba(200,55,45,.85)'; g.lineWidth = 7; g.beginPath();
      const nd = D.length - 1, md = kd * nd; D.forEach(([x, y], i) => { if (i <= md) i ? g.lineTo(x, y) : g.moveTo(x, y); });
      const j0 = Math.floor(md); if (j0 < nd) { const u = md - j0; g.lineTo(lerp(D[j0][0], D[j0 + 1][0], u), lerp(D[j0][1], D[j0 + 1][1], u)); }
      g.stroke(); g.restore();
      if (kd > .8) S.texte('SANS SUEZ : LE TOUR DE L’AFRIQUE', W / 2, 1560, { taille: 44, coul: ROUGE, contour: NOIR, contourL: 6, max: 980 });
    } else {
      const kk = back(pr(t, p.a + .3, .35)); g.save(); g.translate(W / 2 + 120, 1290); g.scale(kk, kk);
      S.texte('12 %', 0, 0, { taille: 210, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14 }); g.restore();
      S.texte('du commerce mondial', W / 2 + 120, 1430, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
    }
  }

  // près de 10 milliards de dollars par jour : un mur de conteneurs qui monte et un compteur
  function argent(p, t) {
    const k = eo(pr(t, p.a + .1, 1.6)), nb = Math.floor(k * 60);
    for (let i = 0; i < nb; i++) { const c = i % 6, r = Math.floor(i / 6); g.fillStyle = COUL[Math.floor(rnd(i * 3.3) * COUL.length)];
      g.fillRect(150 + c * 132, 1250 - r * 62, 124, 54); g.strokeStyle = NOIR; g.lineWidth = 3; for (let s = 1; s < 6; s++) { g.beginPath(); g.moveTo(150 + c * 132 + s * 20, 1254 - r * 62); g.lineTo(150 + c * 132 + s * 20, 1300 - r * 62); g.stroke(); } }
    g.fillStyle = 'rgba(13,11,9,.55)'; g.fillRect(0, 560, W, 330);
    const v = k * 10 > 9.94 ? '10' : (k * 10).toFixed(1).replace('.', ',');
    S.texte('PRÈS DE', W / 2, 600, { taille: 50, coul: CREME, esp: 6 });
    S.texte(v + ' MILLIARDS $', W / 2, 720, { taille: 120, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12, max: 980 });
    S.texte('de marchandises bloquées', W / 2, 860, { taille: 58, police: 'Spectral', it: true, poids: 400, coul: CREME });
    S.texte('estimation de la presse maritime', W / 2, 1400, { taille: 32, coul: GRIS, esp: 3 });
  }

  // la proue géante et la petite pelleteuse ; p.meme : cadre de réseau social, cœurs, tampon MÈME
  function pelleteuse(p, t) {
    const lt = t - p.a;
    if (p.meme) { g.fillStyle = '#1b1712'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(110, 330, 860, 1140, 40); g.fill(); g.stroke();
      g.fillStyle = GRIS; g.beginPath(); g.arc(180, 400, 30, 0, 7); g.fill(); g.fillRect(230, 380, 260, 16); g.fillRect(230, 408, 160, 12); }
    g.save(); if (p.meme) { g.beginPath(); g.rect(140, 450, 800, 860); g.clip(); g.translate(540, 880); g.scale(.78, .78); g.translate(-540, -880); }
    // ciel, berge
    g.fillStyle = '#2d241a'; g.fillRect(0, 300, W, 1100);
    g.fillStyle = SABLE; g.beginPath(); g.moveTo(0, 1150); g.quadraticCurveTo(500, 1080, W, 1130); g.lineTo(W, 1400); g.lineTo(0, 1400); g.fill();
    // proue gigantesque, plantée dans la berge
    g.fillStyle = COQUE; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-50, 300); g.lineTo(560, 300); g.quadraticCurveTo(700, 700, 620, 1170); g.lineTo(-50, 1170); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = '#6e2a22'; g.beginPath(); g.moveTo(-50, 1020); g.lineTo(650, 1020); g.quadraticCurveTo(640, 1100, 620, 1170); g.lineTo(-50, 1170); g.fill();
    g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 4; for (let y = 380; y < 1000; y += 90) { g.beginPath(); g.moveTo(-50, y); g.lineTo(560 + (y - 300) * .18, y); g.stroke(); }
    // la pelleteuse (toute petite)
    const ex = 830, ey = 1130, sc = .55, bras = Math.sin(lt * 4) * .25;
    g.save(); g.translate(ex, ey); g.scale(sc, sc);
    g.fillStyle = OR; g.strokeStyle = NOIR; g.lineWidth = 6;
    g.beginPath(); g.roundRect(-70, -20, 140, 34, 14); g.fillStyle = '#3a332b'; g.fill(); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.roundRect(-55, -90, 110, 70, 8); g.fill(); g.stroke();
    g.fillStyle = '#8fb3c4'; g.fillRect(-40, -80, 40, 34);
    g.save(); g.translate(-50, -60); g.rotate(-.5 + bras); g.fillStyle = OR; g.fillRect(-150, -10, 150, 20); g.strokeRect(-150, -10, 150, 20);
    g.translate(-150, 0); g.rotate(1.2 - bras * 1.5); g.fillRect(-10, 0, 20, 110); g.strokeRect(-10, 0, 20, 110);
    g.fillStyle = '#3a332b'; g.beginPath(); g.moveTo(-26, 110); g.lineTo(26, 110); g.lineTo(10, 150); g.lineTo(-30, 140); g.closePath(); g.fill(); g.stroke(); g.restore();
    g.restore();
    // échelle
    const ke = pr(t, p.a + .3, .4);
    if (ke > 0 && !p.meme) { g.save(); g.globalAlpha = ke; g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath(); g.arc(ex - 20, ey - 30, 90, 0, 7); g.stroke(); g.restore();
      S.texte('ELLE', ex - 20, ey - 170, { taille: 50, coul: ROUGE, contour: NOIR, contourL: 6 }); }
    g.restore();
    if (p.meme) {
      for (let i = 0; i < 10; i++) { const ph = ((lt * .7 + i / 10) % 1); g.save(); g.globalAlpha = 1 - ph; g.translate(860 + Math.sin(i * 2 + lt * 3) * 30, 1260 - ph * 700); g.scale(1.2, 1.2);
        g.fillStyle = ROUGE; g.beginPath(); g.moveTo(0, 12); g.bezierCurveTo(-26, -8, -12, -26, 0, -10); g.bezierCurveTo(12, -26, 26, -8, 0, 12); g.fill(); g.restore(); }
      if (p.tampon && t >= tps(p.tampon)) O.tampon('MÈME', W / 2, 1380, pr(t, tps(p.tampon), .3), -.12, 140);
    }
    if (p.t) deux(p.t, p.meme ? 1560 : 1470, p.taille || 100);
  }

  // le sauvetage vu du ciel : remorqueurs, drague, sable retiré (p.m3 : repère du compteur)
  function chantier(p, t) {
    decor(t);
    const TH = 50 * Math.PI / 180, lt = t - p.a, cx = 540, cy = 600, L = 480;
    const proue = [cx + Math.sin(TH) * L / 2, cy - Math.cos(TH) * L / 2], poupe = [cx - Math.sin(TH) * L / 2, cy + Math.cos(TH) * L / 2];
    // remorqueurs et câbles
    [[poupe, [470, 960], 0], [poupe, [610, 980], .3], [proue, [600, 330], .6], [proue, [470, 300], .9]].forEach(([[ax, ay], [bx, by], d]) => {
      const k = eo(pr(t, p.a + d * .5, .5)); if (k <= 0) return;
      const jx = bx + Math.sin(lt * 3 + d * 5) * 6, jy = by;
      g.strokeStyle = CREME; g.lineWidth = 3; g.beginPath(); g.moveTo(ax, ay); g.lineTo(lerp(ax, jx, k), lerp(ay, jy, k)); g.stroke();
      g.save(); g.translate(lerp(ax, jx, k), lerp(ay, jy, k)); g.rotate(Math.atan2(jy - ay, jx - ax) + Math.PI / 2);
      g.fillStyle = ROUGE; g.strokeStyle = NOIR; g.lineWidth = 3; g.beginPath(); g.ellipse(0, 0, 16, 34, 0, 0, 7); g.fill(); g.stroke();
      g.fillStyle = CREME; g.fillRect(-8, -8, 16, 16); g.restore();
    });
    navireHaut(cx, cy, L, 62, TH);
    // drague sur la berge est, panache de sable
    for (let i = 0; i < 12; i++) { const ph = ((lt * .8 + i / 12) % 1); g.fillStyle = `rgba(201,166,107,${.6 * (1 - ph)})`;
      g.beginPath(); g.arc(proue[0] + 60 + ph * 160, proue[1] - 20 - ph * 120 + Math.sin(i) * 20, 10 + ph * 26, 0, 7); g.fill(); }
    g.fillStyle = OR; g.strokeStyle = NOIR; g.lineWidth = 3; g.fillRect(proue[0] + 40, proue[1] - 10, 50, 26); g.strokeRect(proue[0] + 40, proue[1] - 10, 50, 26);
    S.texte('REMORQUEURS', 230, 1000, { taille: 32, coul: ROUGE, contour: NOIR, contourL: 6 });
    S.texte('DRAGUE', proue[0] + 150, proue[1] + 60, { taille: 32, coul: OR, contour: NOIR, contourL: 6 });
    if (p.m3 && t >= tps(p.m3)) {
      const k = eo(pr(t, tps(p.m3), .8)), n = Math.round(k * 30);
      const kk = back(pr(t, tps(p.m3), .3)); g.save(); g.translate(W / 2, 1460); g.scale(kk, kk);
      S.texte(n + ' 000 M³', 0, 0, { taille: 150, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 }); g.restore();
      S.texte('de sable retirés', W / 2, 1580, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
    } else if (p.t) deux(p.t, 1470, 100);
  }

  // la pleine Lune (photo NASA) au-dessus du canal
  function lune(p, t) {
    const k = eo(pr(t, p.a, .8));
    g.save(); g.beginPath(); g.arc(W / 2, lerp(900, 780, k), 330, 0, 7); g.clip();
    const im = S.img('lune'); if (im) { g.filter = 'grayscale(1) contrast(1.2) brightness(1.05) sepia(.35)'; S.cover(im, W / 2 - 330, lerp(900, 780, k) - 330, 660, 660, 4.0 + (t - p.a) * .08, .508, .525); g.filter = 'none'; }
    g.restore();
    g.save(); g.shadowColor = 'rgba(217,180,90,.6)'; g.shadowBlur = 80; g.strokeStyle = 'rgba(239,230,210,.6)'; g.lineWidth = 4; g.beginPath(); g.arc(W / 2, lerp(900, 780, k), 332, 0, 7); g.stroke(); g.restore();
    if (p.t) deux(p.t, 1360, p.taille || 130);
    if (p.sous) S.texte(p.sous, W / 2, 1490, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });
  }

  // coupe : la coque échouée dans la berge, l'eau qui monte (p.monte = repère), le navire se soulève
  function maree(p, t) {
    const tm = p.monte ? tps(p.monte) : p.a + .2, k = eo(pr(t, tm, 1.6)), lt = t - p.a;
    g.fillStyle = '#211a13'; g.fillRect(0, 300, W, 1150);
    const niv = lerp(1010, 900, k), lift = p.leve ? eo(pr(t, tm + .5, 1.2)) * 50 : 0;
    // berge en coupe
    g.fillStyle = SABLE; g.beginPath(); g.moveTo(560, 1450); g.lineTo(760, 1120); g.lineTo(1080, 1100); g.lineTo(1080, 1450); g.fill();
    navireProfil(380, 1080 - lift, 760, { rot: -.03 + lift * .0004 });
    g.fillStyle = 'rgba(20,32,42,.82)'; g.beginPath(); g.moveTo(0, niv);
    for (let x = 0; x <= W; x += 20) g.lineTo(x, niv + Math.sin(x * .02 + lt * 2.5) * 8); g.lineTo(W, 1450); g.lineTo(0, 1450); g.fill();
    g.strokeStyle = OR; g.lineWidth = 4; g.beginPath(); for (let x = 0; x <= W; x += 20) { const y = niv + Math.sin(x * .02 + lt * 2.5) * 8; x ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke();
    // jauge
    g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(980, 760); g.lineTo(980, 1060); g.stroke();
    for (let y = 780; y <= 1040; y += 40) { g.beginPath(); g.moveTo(960, y); g.lineTo(1000, y); g.stroke(); }
    if (k > .05) S.d.fleche(920, 1040, 920, lerp(1040, niv - 10, k), 1, { trait: OR, ep: 10 });
    if (p.t) deux(p.t, 1520, p.taille || 100);
  }

  // un choke point : les routes convergent dans un passage étroit ; p.tampon : tampon CHOKE POINT
  function choke(p, t) {
    const lt = t - p.a, k = eo(pr(t, p.a, .7));
    g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(0, 330); g.lineTo(W, 330); g.lineTo(W, 760); g.quadraticCurveTo(620, 760, 560, 900); g.quadraticCurveTo(480, 760, 0, 760); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(0, 1500); g.lineTo(W, 1500); g.lineTo(W, 1080); g.quadraticCurveTo(620, 1080, 560, 960); g.quadraticCurveTo(480, 1080, 0, 1080); g.closePath(); g.fill(); g.stroke();
    // flux de navires
    for (let i = 0; i < 26; i++) {
      const ph = ((lt * .35 + rnd(i) ) % 1), y0 = 800 + rnd(i * 3) * 260, y = ph < .5 ? lerp(y0, 930, Math.pow(ph * 2, 2)) : lerp(930, 800 + rnd(i * 7) * 260, Math.pow((ph - .5) * 2, .5));
      const x = lerp(-40, W + 40, ph); g.fillStyle = i % 5 ? CREME : OR; g.globalAlpha = k; g.fillRect(x - 14, y - 5, 28, 10);
    }
    g.globalAlpha = 1;
    O.petitTitre(p.sur || 'DÉTROITS ET CANAUX', 420, OR);
    S.texte('passage étroit', 560, 1010 + 150, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME });
    g.save(); g.strokeStyle = ROUGE; g.lineWidth = 6; g.globalAlpha = .5 + .5 * Math.sin(lt * 5); g.beginPath(); g.arc(560, 930, 90, 0, 7); g.stroke(); g.restore();
    if (p.tampon && t >= tps(p.tampon)) O.tampon('CHOKE POINT', W / 2, 1340, pr(t, tps(p.tampon), .3), -.08, 110);
    else if (p.t) deux(p.t, 1340, p.taille || 100);
    if (p.sous) S.texte(p.sous, W / 2, 1560, { taille: 50, coul: CREME, poids: 600, esp: 3, contour: NOIR, contourL: 6 });
  }

  return { canal, navire, tempete, route, argent, pelleteuse, chantier, lune, maree, choke };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'canal') {
    if (p.etat === 'derape') L.push([p.a + .1, 'frotte', .7], [p.a + .5, 'souffle', .6]);
    if (p.avant) L.push([tps(p.avant), 'boum', .9]);
    if (p.arriere) L.push([tps(p.arriere), 'boum', .8]);
    if (p.bloque) L.push([tps(p.bloque) + .05, 'tampon', 1]);
    if (p.etapes) p.etapes.forEach(([a], i) => { if (i) L.push([tps(a), 'blip', .5]); });
    if (p.etat === 'libre') L.push([p.a + 1.1, 'whoosh', .6]);
  }
  if (p.type === 'tempete') L.push([p.a, 'souffle', p.voile ? .5 : .8]);
  if (p.type === 'navire' && p.eiffel) L.push([p.a + .1, 'montee', .6], [p.a + .75, 'pop', .5]);
  if (p.type === 'route') L.push([p.a + .1, 'whoosh', .4], ...(p.etape === 2 ? [] : [[p.a + .3, 'pop', .6]]));
  if (p.type === 'argent') for (let k = 0; k < 12; k++) L.push([p.a + .1 + k * .13, 'tic', .35]);
  if (p.type === 'pelleteuse') { L.push([p.a, 'clic', .4]); if (p.tampon) L.push([tps(p.tampon) + .05, 'tampon', 1]); if (p.meme) L.push([p.a + .1, 'pop', .5]); }
  if (p.type === 'chantier' && p.m3) L.push([tps(p.m3), 'montee', .5]);
  if (p.type === 'lune') L.push([p.a, 'souffle', .5]);
  if (p.type === 'maree') L.push([p.monte ? tps(p.monte) : p.a + .2, 'montee', .6]);
  if (p.type === 'choke' && p.tampon) L.push([tps(p.tampon) + .05, 'tampon', 1]);
};
