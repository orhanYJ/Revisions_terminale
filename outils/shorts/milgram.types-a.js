// Plans propres au short Milgram, dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
window.SANS_ST_A = ['annonce', 'ordre', 'silence', 'sondage'];
window.PROPRES_A = ['panneau', 'mur', 'ordre', 'silence', 'annonce', 'sondage', 'acteur', 'sueur'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const GROUPES = ['CHOC LÉGER', 'CHOC MODÉRÉ', 'CHOC FORT', 'CHOC TRÈS FORT', 'CHOC INTENSE', 'CHOC EXTRÊMEMENT INTENSE', 'DANGER : CHOC VIOLENT', 'XXX'];
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const groupe = v => GROUPES[Math.min(7, Math.floor((v - 15) / 60))];
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // valeur courante d'une suite d'étapes [[repère, valeur], …] (le premier repère peut être null = début du plan)
  function etape(p, t) {
    let v = p.etapes[0][1], v0 = v, t0 = p.a;
    p.etapes.forEach(([a, x], i) => { const ta = a ? tps(a) : p.a; if (t >= ta) { v0 = i ? p.etapes[i - 1][1] : x; v = x; t0 = ta; } });
    return { v, v0, t0 };
  }

  // tableau des 30 interrupteurs (15 à 450 volts), lampes rouges jusqu'à la tension courante
  function panneau(p, t, l) {
    const { v, v0, t0 } = etape(p, t), k = eo(pr(t, t0, .35)), vv = Math.round(lerp(v0, v, k) / 15) * 15;
    const z = p.zoom ? lerp(1, 1.18, eo(pr(t, p.a, .6))) : 1;
    g.save();
    if (p.zoom) { const idx = Math.max(0, v / 15 - 1), cx = 110 + (idx % 15) * 62, cy = idx < 15 ? 820 : 1060; g.translate(cx, cy); g.scale(z, z); g.translate(-cx, -cy); }
    // compteur
    const r = cl(vv / 450), coul = `rgb(${Math.round(lerp(217, 220, r))},${Math.round(lerp(180, 55, r))},${Math.round(lerp(90, 45, r))})`;
    S.texte(vv + ' V', W / 2, 470, { taille: 210, police: 'Spectral', poids: 600, coul, ombre: r > .6 ? 'rgba(200,55,45,.6)' : 'rgba(217,180,90,.4)', flou: 40 });
    if (vv > 0) S.texte(groupe(vv), W / 2, 610, { taille: 44, coul: r > .6 ? ROUGE : CREME, esp: 6, max: 960 });
    // boîtier
    g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.roundRect(50, 680, 980, 500, 18); g.fill(); g.stroke();
    S.texte('GÉNÉRATEUR DE CHOCS · 15 – 450 VOLTS', W / 2, 720, { taille: 26, police: 'JetBrains Mono', poids: 500, coul: GRIS });
    for (let i = 0; i < 30; i++) {
      const volts = 15 * (i + 1), x = 110 + (i % 15) * 62, y = i < 15 ? 820 : 1060, on = volts <= vv, cur = volts === vv && vv > 0;
      g.fillStyle = on ? ROUGE : '#4a4038'; if (on) { g.shadowColor = ROUGE; g.shadowBlur = cur ? 40 : 14; }
      g.beginPath(); g.arc(x, y - 52, 11, 0, 7); g.fill(); g.shadowBlur = 0;
      g.fillStyle = '#efe6d2'; g.fillRect(x - 20, y - 30, 40, 70);
      g.fillStyle = cur ? ROUGE : NOIR; g.fillRect(x - 8, on ? y + 4 : y - 24, 16, 30);
      S.texte(volts >= 435 ? 'XXX' : String(volts), x, y + 64, { taille: 20, police: 'JetBrains Mono', poids: 500, coul: volts >= 435 ? ROUGE : CREME });
    }
    g.restore();
    if (p.t) deux(p.t, 1330, p.taille || 110);
    // étincelle à chaque nouvelle tension
    const ke = pr(t, t0, .25); if (ke > 0 && ke < 1 && v > v0) { g.save(); g.globalAlpha = (1 - ke) * .3; g.fillStyle = '#fff6d8'; g.fillRect(0, 0, W, H); g.restore(); }
  }

  function annonce(p, t) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1300, 880, k)); g.rotate(-.035);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#e9dfc8'; g.fillRect(-420, -430, 840, 860); g.shadowColor = 'transparent';
    g.strokeStyle = NOIR; g.lineWidth = 4; g.strokeRect(-390, -400, 780, 800);
    S.texte('PETITES ANNONCES · NEW HAVEN', 0, -350, { taille: 30, coul: GRIS, esp: 4 });
    S.texte('ON RECHERCHE', 0, -250, { taille: 86, coul: NOIR });
    S.texte('des volontaires', 0, -165, { taille: 60, police: 'Spectral', it: true, poids: 400, coul: NOIR });
    S.texte('pour une étude', 0, -60, { taille: 56, police: 'Spectral', poids: 600, coul: NOIR });
    S.texte('sur la MÉMOIRE', 0, 10, { taille: 56, police: 'Spectral', poids: 600, coul: NOIR });
    S.texte('4,50 $', 0, 150, { taille: 130, coul: NOIR });
    S.texte('pour une heure · Université Yale', 0, 260, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: NOIR });
    const kc = pr(t, tps(p.cercle), .45); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(0, 150, 220, 95, -.05, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.petitTitre('— ANNONCE AUTHENTIQUE, 1961 —', 330);
  }

  // homme assis attaché ; p.zoom : gros plan sur le poignet et l'électrode
  function chaise(p, t, l) {
    const zz = p.zoom ? eo(pr(t, p.a, .5)) : 0, z = lerp(1, 2.4, zz);
    g.save(); g.translate(W / 2, 900); g.scale(z, z); g.translate(-lerp(540, 735, zz), -lerp(900, 878, zz));
    // chaise
    g.fillStyle = '#3a2f25'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.roundRect(380, 560, 60, 520, 10); g.fill(); g.stroke();      // dossier
    g.beginPath(); g.roundRect(380, 900, 360, 50, 10); g.fill(); g.stroke();      // assise
    [[400, 950], [700, 950]].forEach(([x, y]) => { g.beginPath(); g.moveTo(x, y); g.lineTo(x, 1200); g.stroke(); });
    // homme (silhouette)
    g.fillStyle = '#16120e'; g.lineWidth = 7;
    g.beginPath(); g.arc(500, 560, 75, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(440, 650); g.lineTo(580, 650); g.lineTo(600, 900); g.lineTo(440, 900); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(560, 880); g.lineTo(760, 900); g.lineTo(760, 1180); g.lineTo(700, 1180); g.lineTo(700, 950); g.lineTo(560, 940); g.closePath(); g.fill(); g.stroke();
    // bras sur l'accoudoir, sangles
    g.beginPath(); g.moveTo(560, 700); g.lineTo(640, 840); g.lineTo(760, 860); g.lineTo(760, 900); g.lineTo(620, 880); g.lineTo(530, 740); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = OR; [[450, 760], [700, 862], [470, 860]].forEach(([x, y]) => g.fillRect(x - 40, y - 10, 80, 22));
    // électrode et fil
    g.fillStyle = ROUGE; g.beginPath(); g.arc(735, 878, 16, 0, 7); g.fill();
    g.strokeStyle = ROUGE; g.lineWidth = 5; g.beginPath(); g.moveTo(735, 878); g.bezierCurveTo(820, 900, 860, 700, 1100, 650); g.stroke();
    if (p.zoom) for (let i = 0; i < 6; i++) { const a = rnd(i + Math.floor(t * 20)) * 6.3, r = 20 + rnd(i * 3 + Math.floor(t * 20)) * 30; g.strokeStyle = '#fff3c4'; g.lineWidth = 3;
      g.beginPath(); g.moveTo(735, 878); g.lineTo(735 + Math.cos(a) * r, 878 + Math.sin(a) * r); g.stroke(); }
    g.restore();
    if (p.t) deux(p.t, 1420, 100);
  }

  // mur de briques qui tremble à chaque coup
  function mur(p, t, l) {
    const coups = (p.coups || [0, .45]).map(x => p.a + x);
    let sec = 0; coups.forEach(c => { if (t >= c) sec = Math.max(sec, 1 - pr(t, c, .35)); });
    const sx = (rnd(t * 91) - .5) * 40 * sec, sy = (rnd(t * 37) - .5) * 30 * sec;
    g.save(); g.translate(sx, sy);
    for (let r = 0; r < 18; r++) for (let c = -1; c < 9; c++) {
      const x = c * 140 + (r % 2) * 70, y = 300 + r * 70;
      g.fillStyle = `rgb(${70 + rnd(r * 9 + c) * 25},${40 + rnd(r + c * 5) * 15},${30})`; g.fillRect(x + 4, y + 4, 132, 62);
    }
    // fissures qui s'étendent
    const nf = coups.filter(c => t >= c).length;
    g.strokeStyle = NOIR; g.lineWidth = 6;
    for (let f = 0; f < nf * 3; f++) { g.beginPath(); let x = 540, y = 900; g.moveTo(x, y); for (let s = 0; s < 6; s++) { x += (rnd(f * 7 + s) - .5) * 160; y += (rnd(f * 3 + s + 1) - .5) * 160; g.lineTo(x, y); } g.stroke(); }
    g.restore();
    coups.forEach((c, i) => { const k = pr(t, c, .3); if (k > 0) { g.save(); g.translate(W / 2 + (i % 2 ? 120 : -120), 820 + i * 140); g.rotate((i % 2 ? .12 : -.1)); const s = lerp(2.2, 1, back(k));
      g.scale(s, s); S.texte('BOUM', 0, 0, { taille: 170, coul: ROUGE, contour: NOIR, contourL: 16 }); g.restore(); } });
    if (p.t) deux(p.t, 1480, 100);
  }

  // l'expérimentateur en blouse grise
  function blouse(p, t, l) {
    const k = eo(pr(t, p.a, .4)), x = lerp(760, 540, k);
    g.save(); g.translate(x, 0);
    g.fillStyle = '#8f8a82'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-170, 1300); g.lineTo(-150, 760); g.quadraticCurveTo(0, 700, 150, 760); g.lineTo(170, 1300); g.closePath(); g.fill(); g.stroke();
    g.strokeStyle = '#5d5952'; g.beginPath(); g.moveTo(0, 740); g.lineTo(0, 1300); g.stroke();
    g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.beginPath(); g.arc(0, 620, 100, 0, 7); g.fill(); g.stroke();
    // bloc-notes
    g.fillStyle = CREME; g.save(); g.translate(120, 980); g.rotate(-.2); g.fillRect(-70, -95, 140, 190); g.fillStyle = NOIR; for (let i = 0; i < 5; i++) g.fillRect(-50, -60 + i * 30, 100, 6); g.restore();
    g.restore();
    O.multi([['BLOUSE ', CREME], ['GRISE', OR]], 1460, 120);
  }

  // une phrase de l'expérimentateur, tapée à la machine ; p.tampon : version tampon rouge
  function ordre(p, t, l) {
    O.fondImg(p.fond || 'nuremberg', 1.3, .5, .4, .0);
    const txt = p.t, n = Math.floor(cl((t - p.a) / (p.duree || .9)) * txt.length);
    S.texte('L’EXPÉRIMENTATEUR', W / 2, 700, { taille: 36, coul: GRIS, esp: 8 });
    const lignes = txt.split('|');
    let c = 0; lignes.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte((i === 0 ? '« ' : '') + vis + (i === lignes.length - 1 && n >= txt.replace(/\|/g, '').length ? ' »' : ''), W / 2, 900 + i * 125,
        { taille: p.taille || 92, police: 'Spectral', it: true, poids: 500, coul: p.tampon ? ROUGE : CREME, max: 980 }); });
    if (p.tampon) O.tampon('ORDRE', W / 2, 1220, pr(t, p.a + (p.duree || .9), .3), -.08, 120);
    else O.barreRouge(1000 + lignes.length * 60, eo(pr(t, p.a + (p.duree || .9), .3)), 12, -.02);
  }

  function silence(p, t, l) {
    g.fillStyle = '#000'; g.fillRect(0, 0, W, H);
    // tracé plat
    g.strokeStyle = 'rgba(239,230,210,.6)'; g.lineWidth = 4; g.beginPath(); g.moveTo(60, 960);
    for (let x = 60; x <= 1020; x += 6) g.lineTo(x, 960 + (x < 300 ? Math.sin(x * .2 + t * 8) * 30 * (1 - pr(t, p.a, .6)) : 0)); g.stroke();
    const k = pr(t, p.a + .3, .5); g.save(); g.globalAlpha = k;
    S.texte(p.t || '… plus rien.', W / 2, 1120, { taille: 70, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore();
  }

  // sondage : p.etape 1 = 100 têtes, 1 rouge, « 1 % » ; p.etape 2 = 40 têtes, 26 deviennent rouges
  function sondage(p, t, l) {
    const e = p.etape, n = e === 1 ? 100 : 40, cols = e === 1 ? 10 : 8, taille = e === 1 ? 74 : 100;
    const x0 = W / 2 - (cols - 1) * taille / 2, y0 = e === 1 ? 560 : 600;
    const nr = e === 1 ? 1 : Math.floor(26 * cl((t - tps(p.rouges)) / 1.3));
    for (let i = 0; i < n; i++) {
      const x = x0 + (i % cols) * taille, y = y0 + Math.floor(i / cols) * taille * 1.05, r = e === 1 ? i === 44 && t >= p.a + .4 : i < nr;
      g.fillStyle = r ? ROUGE : 'rgba(239,230,210,.75)';
      g.beginPath(); g.arc(x, y - taille * .18, taille * .17, 0, 7); g.fill();
      g.beginPath(); g.ellipse(x, y + taille * .2, taille * .27, taille * .2, 0, Math.PI, 0); g.fill();
    }
    if (e === 1) {
      S.texte('LE PRONOSTIC DES ÉTUDIANTS DE YALE', W / 2, 420, { taille: 38, coul: CREME, esp: 6, poids: 600, max: 960 });
      const k = back(pr(t, p.a + .4, .3)); g.save(); g.translate(W / 2, 1500); g.scale(k, k);
      S.texte('1 %', 0, 0, { taille: 230, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14 }); g.restore();
      S.texte('à peine 1 personne sur 100', W / 2, 1650, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME });
    } else {
      O.petitTitre('LE RÉSULTAT RÉEL', 470, ROUGE);
      S.texte(nr + ' / 40', W / 2, 1210, { taille: 170, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 12 });
      if (p.pct && t >= tps(p.pct)) { const k = back(pr(t, tps(p.pct), .3)); g.save(); g.translate(W / 2, 1400); g.scale(k, k);
        S.texte('PRESQUE 2 SUR 3', 0, 0, { taille: 100, coul: CREME, contour: NOIR, contourL: 10 }); g.restore(); }
    }
  }

  // sueur, tremblement
  function sueur(p, t, l) {
    const tr = (rnd(t * 60) - .5) * 14;
    S.d.tete(560 + tr, 800, 320, { trait: CREME, fond: '#1b1712', ep: 9 });
    for (let i = 0; i < 9; i++) { const ph = ((t - p.a) * .9 + i / 9) % 1, x = 420 + rnd(i) * 300, y = 600 + ph * 600;
      g.fillStyle = `rgba(150,190,220,${1 - ph})`; g.beginPath(); g.moveTo(x, y - 26); g.quadraticCurveTo(x + 16, y, x, y + 14); g.quadraticCurveTo(x - 16, y, x, y - 26); g.fill(); }
    let lab = p.etapes[0][1]; p.etapes.forEach(([a, s]) => { if (!a || t >= tps(a)) lab = s; });
    const ka = p.etapes.map(([a]) => a ? tps(a) : p.a).filter(x => x <= t).pop();
    const k = back(pr(t, ka, .25)); g.save(); g.translate(W / 2, 1400); g.scale(lerp(1.6, 1, k), lerp(1.6, 1, k)); g.translate(-W / 2, 0);
    O.multi([[lab, OR]], 0, 120); g.restore();
  }

  // révélation : c'était un acteur
  function acteur(p, t, l) {
    O.carte('masques', W / 2, 760, 760, 700, .02, 1.05 + l * .03, .5, .5, { lum: .85 });
    O.tampon('ACTEUR', W / 2, 1300, pr(t, tps(p.tampon), .3), -.1, 150);
    if (p.zero && t >= tps(p.zero)) { const k = back(pr(t, tps(p.zero), .3)); g.save(); g.translate(W / 2, 1560); g.scale(k, k);
      S.texte('0 DÉCHARGE', 0, 0, { taille: 110, coul: OR, contour: NOIR, contourL: 12 }); g.restore(); }
  }

  // le doigt qui hésite au-dessus du dernier interrupteur (fin, boucle)
  function doigt(p, t, l) {
    g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(240, 700, 600, 640, 26); g.fill(); g.stroke();
    S.texte('XXX', W / 2, 800, { taille: 80, coul: ROUGE });
    S.texte('450 V', W / 2, 1270, { taille: 70, police: 'JetBrains Mono', poids: 500, coul: CREME });
    g.fillStyle = '#efe6d2'; g.fillRect(440, 880, 200, 300); g.fillStyle = NOIR; g.fillRect(500, 900, 80, 120);
    // doigt qui descend et hésite
    const y = 560 + Math.sin((t - p.a) * 5) * 30 + eo(pr(t, p.a, .6)) * 120;
    g.save(); g.fillStyle = '#d8b48c'; g.strokeStyle = NOIR; g.lineWidth = 6;
    g.beginPath(); g.roundRect(495, y - 400, 90, 420, 45); g.fill(); g.stroke();
    g.fillStyle = '#f1d9c0'; g.beginPath(); g.ellipse(540, y - 20, 30, 22, 0, 0, 7); g.fill(); g.restore();
    deux(p.t, 1480, 110);
  }

  return { panneau, annonce, chaise, mur, blouse, ordre, silence, sondage, sueur, acteur, doigt };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'panneau') p.etapes.forEach(([a, v], i) => { const t = a ? tps(a) : p.a; if (i || !a) { L.push([t, 'clic', .7], [t + .02, 'buzz', .55]); } });
  if (p.type === 'mur') (p.coups || [0, .45]).forEach(c => L.push([p.a + c, 'boum', 1]));
  if (p.type === 'ordre') { const n = p.t.length, d = p.duree || .9; for (let k = 0; k < n; k += 2) L.push([p.a + d * k / n, 'tic', .3]); if (p.tampon) L.push([p.a + d + .05, 'tampon', 1]); }
  if (p.type === 'annonce') L.push([p.a, 'papier', .5], [tps(p.cercle), 'stylo', .5]);
  if (p.type === 'sondage') { if (p.etape === 2) for (let k = 0; k < 26; k++) L.push([tps(p.rouges) + 1.3 * k / 26, 'blip', .3]); else L.push([p.a + .4, 'bip', .4]); }
  if (p.type === 'acteur') L.push([tps(p.tampon) + .05, 'tampon', 1]);
  if (p.type === 'sueur') L.push([p.a, 'coeur', .9], [p.a + .9, 'coeur', .9]);
  if (p.type === 'chaise' && p.zoom) L.push([p.a, 'buzz', .4]);
  if (p.type === 'blouse') L.push([p.a, 'frotte', .4]);
};
