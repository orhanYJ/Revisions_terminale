// Plans propres au short « Seconde Guerre mondiale : niveau 1 → 10 » (modèle A, habillage « alerte »).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, al, C = couleurs).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al, pour que l'habillage s'applique.
// Les plans niveau sont communs (formats-a.js).
window.SANS_ST_A = ['echelle', 'chronometre', 'carto', 'radio', 'commentaire', 'collage'];
window.PROPRES_A = ['echelle', 'chronometre', 'carto', 'radio', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  // formats-a.js (plan niveau avec image) appelle carte() sans le préfixe O. : on lui donne l'outil du modèle.
  if (typeof window.carte !== 'function') window.carte = O.carte;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.1, i ? taille : taille * .85)); };
  const coulNiv = i => i < 3 ? CREME : i < 6 ? OR : ROUGE;   // i de 0 (niveau 1) à 9 (niveau 10)
  const zone = (pts, fond, trait, ep = 5) => { g.save(); g.fillStyle = fond; g.strokeStyle = trait; g.lineWidth = ep; g.lineJoin = 'round'; g.beginPath(); pts.forEach(([x, y], i) => i ? g.lineTo(x, y) : g.moveTo(x, y)); g.closePath(); g.fill(); g.stroke(); g.restore(); };
  const fl = (x0, y0, x1, y1, k, c, ep = 16) => S.d.fleche(x0, y0, x1, y1, eo(k), { trait: c, ep });
  const etiquette = (s, x, y, taille = 44, c = CREME) => S.texte(s, x, y, { taille, coul: c, contour: NOIR, contourL: 8, poids: 700, max: 600 });

  // échelle des dix niveaux. mode 'stop' : les niveaux s'allument, un curseur « ? » hésite ; mode 'dernier' : le 10 clignote.
  function echelle(p, t) {
    const lt = t - p.a, x0 = W / 2 - 230, wB = 460, hB = 54, y1 = 1180, pas = 82;
    for (let i = 0; i < 10; i++) {
      const y = y1 - i * pas, c = coulNiv(i);
      const k = p.mode === 'dernier' ? 1 : eo(pr(t, p.a + i * .08, .18));
      g.save(); g.fillStyle = al(CREME, .08); g.beginPath(); g.roundRect(x0, y - hB / 2, wB, hB, 14); g.fill();
      let kk = 1; if (p.mode === 'dernier' && i === 9) kk = 1 + .08 * Math.abs(Math.sin(lt * 9));
      g.translate(x0 + wB / 2, y); g.scale(kk, kk); g.translate(-(x0 + wB / 2), -y);
      g.fillStyle = p.mode === 'dernier' && i === 9 ? ROUGE : al(c === CREME ? CREME : c, i === 9 && p.mode === 'dernier' ? 1 : .85);
      g.beginPath(); g.roundRect(x0, y - hB / 2, wB * k, hB, 14); g.fill(); g.restore();
      S.texte(String(i + 1), x0 - 60, y + 2, { taille: 48, coul: k > .5 ? c : GRIS, poids: 700 });
    }
    S.texte('FACILE', x0 + wB + 30, y1, { taille: 32, coul: CREME, align: 'left', esp: 4 });
    S.texte('IMPOSSIBLE', x0 + wB + 30, y1 - 9 * pas, { taille: 32, coul: ROUGE, align: 'left', esp: 4, max: 220 });
    if (p.mode === 'stop') {   // curseur qui monte et redescend : où tu t'arrêtes ?
      const u = .5 + .45 * Math.sin(Math.max(0, lt - .8) * 3.1 - 1.4), y = y1 - u * 9 * pas, ka = back(pr(t, p.a + .8, .3));
      g.save(); g.translate(x0 - 140, y); g.scale(ka, ka); g.fillStyle = OR;
      g.beginPath(); g.moveTo(-40, -40); g.lineTo(30, 0); g.lineTo(-40, 40); g.closePath(); g.fill();
      S.texte('?', -95, 4, { taille: 80, coul: OR, contour: NOIR, contourL: 8 }); g.restore();
    } else {
      O.tampon('10', x0 + wB + 140, y1 - 9 * pas + 10, pr(t, p.a + .15, .3), .12, 70, ROUGE);
    }
    const kt = back(pr(t, p.a + .2, .3)); g.save(); g.globalAlpha = cl(kt); deux(p.t, 1430, 105); g.restore();
  }

  // chronomètre : l'aiguille tourne, l'arc rouge grignote le cadran
  function chronometre(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3)), r = 290;
    g.save(); g.translate(W / 2, 820); g.scale(k, k);
    g.fillStyle = al(CREME, .06); g.strokeStyle = CREME; g.lineWidth = 14;
    g.beginPath(); g.roundRect(-45, -r - 80, 90, 60, 10); g.fill(); g.stroke();
    g.beginPath(); g.arc(0, 0, r, 0, 7); g.fill(); g.stroke();
    const u = cl(lt / 1.6);
    g.fillStyle = al(ROUGE, .45); g.beginPath(); g.moveTo(0, 0); g.arc(0, 0, r - 24, -Math.PI / 2, -Math.PI / 2 + u * 6.283); g.closePath(); g.fill();
    for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; g.lineWidth = i % 3 ? 6 : 12; g.strokeStyle = CREME;
      g.beginPath(); g.moveTo(Math.sin(a) * (r - 30), -Math.cos(a) * (r - 30)); g.lineTo(Math.sin(a) * (r - 70), -Math.cos(a) * (r - 70)); g.stroke(); }
    const a = lt * 5; g.strokeStyle = OR; g.lineWidth = 14; g.lineCap = 'round';
    g.beginPath(); g.moveTo(0, 0); g.lineTo(Math.sin(a) * (r - 50), -Math.cos(a) * (r - 50)); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.arc(0, 0, 24, 0, 7); g.fill();
    g.restore();
    deux(p.t, 1340, 115);
  }

  // cartes schématiques (pas à l'échelle) : v = 'pologne', 'monde', 'barbarossa', 'asie'
  function carto(p, t) {
    const lt = t - p.a, k = eo(pr(t, p.a, .4));
    S.texte('SCHÉMA', W - 80, 260, { taille: 28, coul: GRIS, align: 'right', esp: 8, poids: 700 });
    g.save(); g.globalAlpha = k;
    if (p.v === 'pologne') {
      O.petitTitre('— LE PACTE DU 23 AOÛT 1939 —', 380, OR);
      zone([[70, 560], [330, 520], [360, 820], [330, 1120], [70, 1140]], al(CREME, .1), CREME);
      zone([[760, 500], [1020, 480], [1020, 1180], [760, 1160], [720, 860]], al(ROUGE, .16), CREME);
      const PL = [[360, 600], [560, 560], [730, 600], [720, 860], [760, 1100], [560, 1150], [330, 1100], [360, 820]];
      zone(PL, al(OR, .14), OR, 7);
      etiquette('ALLEMAGNE', 200, 1200, 40); etiquette('URSS', 890, 1230, 48); etiquette('POLOGNE', 545, 760, 54, OR);
      g.save(); g.setLineDash([22, 14]); g.strokeStyle = ROUGE; g.lineWidth = 8; const kd = eo(pr(t, p.a + .3, .5));
      g.beginPath(); g.moveTo(560, 560); g.lineTo(560, 560 + 590 * kd); g.stroke(); g.restore();
      fl(240, 900, 470, 900, pr(t, p.a + .1, .4), ROUGE, 18);
      etiquette('1ER SEPT. 1939', 330, 830, 34, OR);
      O.tampon('PARTAGE SECRET', W / 2, 1400, pr(t, p.a + .6, .3), -.08, 72, ROUGE);
    } else if (p.v === 'monde') {
      const cx = W / 2, cy = 820, R = 360;
      g.save(); g.fillStyle = al(CREME, .06); g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(cx, cy, R, 0, 7); g.fill(); g.stroke();
      g.strokeStyle = al(CREME, .25); g.lineWidth = 3;
      for (let i = 1; i < 6; i++) { const w = R * Math.abs(Math.cos((i / 6) * Math.PI + lt * .4)); g.beginPath(); g.ellipse(cx, cy, w, R, 0, 0, 7); g.stroke(); }
      for (let j = -2; j <= 2; j++) { const y = cy + j * R * .38, w = Math.sqrt(R * R - (j * R * .38) ** 2); g.beginPath(); g.moveTo(cx - w, y); g.lineTo(cx + w, y); g.stroke(); }
      g.restore();
      [[cx - 170, cy - 120, 'EUROPE', .1], [cx + 190, cy + 40, 'PACIFIQUE', .45]].forEach(([x, y, s, d]) => {
        for (let i = 0; i < 3; i++) { const u = ((lt - d) * 1.4 + i / 3) % 1; if (lt < d) continue;
          g.save(); g.strokeStyle = ROUGE; g.globalAlpha = (1 - u) * .9; g.lineWidth = 8; g.beginPath(); g.arc(x, y, 20 + u * 130, 0, 7); g.stroke(); g.restore(); }
        g.fillStyle = ROUGE; g.beginPath(); g.arc(x, y, 18, 0, 7); g.fill();
        if (lt > d) etiquette(s, x, y + 70, 40, OR);
      });
      etiquette('PEARL HARBOR', cx + 190, cy - 60, 36, CREME);
      deux('LA GUERRE DEVIENT|MONDIALE', 1350, 110);
    } else if (p.v === 'barbarossa') {
      O.petitTitre('— 22 JUIN 1941 · BARBAROSSA —', 380, OR);
      zone([[560, 470], [1040, 440], [1040, 1300], [600, 1320], [520, 900]], al(ROUGE, .14), CREME);
      etiquette('URSS', 900, 1260, 52);
      g.save(); g.setLineDash([18, 12]); g.strokeStyle = al(CREME, .6); g.lineWidth = 5; g.beginPath(); g.moveTo(530, 470); g.lineTo(530, 1320); g.stroke(); g.restore();
      S.texte('BALTIQUE', 400, 470, { taille: 30, coul: GRIS, poids: 700 }); S.texte('MER NOIRE', 400, 1330, { taille: 30, coul: GRIS, poids: 700 });
      [[620, 'LENINGRAD'], [880, 'MOSCOU'], [1140, 'KIEV · ROSTOV']].forEach(([y, s], i) => {
        const kk = pr(t, p.a + .2 + i * .35, .5); fl(120, y, 760, y - 20, kk, OR, 20);
        if (kk > .6) etiquette(s, 860, y - 70, 42, OR);
      });
      deux('TROIS|POUSSÉES', 1490, 100);
    } else if (p.v === 'asie') {
      O.petitTitre('— LA GUERRE COMMENCE EN ASIE —', 380, OR);
      zone([[90, 620], [420, 520], [700, 560], [760, 760], [700, 1060], [520, 1240], [200, 1200], [80, 920]], al(CREME, .1), CREME);
      zone([[460, 470], [700, 450], [740, 600], [560, 640], [450, 590]], al(OR, .18), OR, 5);
      etiquette('CHINE', 330, 900, 64); etiquette('MANDCHOURIE · 1931', 595, 690, 32, OR);
      zone([[900, 640], [960, 600], [990, 700], [950, 900], [890, 1000], [860, 940], [910, 800]], al(ROUGE, .2), CREME);
      etiquette('JAPON', 930, 1060, 46);
      fl(870, 860, 560, 900, pr(t, p.a + .2, .5), ROUGE, 20);
      const kd = back(pr(t, p.a + .6, .3)); g.save(); g.translate(560, 1100); g.scale(kd, kd);
      S.texte('1937', 0, 0, { taille: 120, coul: ROUGE, contour: NOIR, contourL: 12, police: 'Spectral', poids: 600 }); g.restore();
      deux('LE JAPON ATTAQUE|LA CHINE', 1420, 100);
    }
    g.restore();
  }

  // poste de radio : ondes qui partent de Londres
  function radio(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 900); g.scale(k, k);
    for (let i = 0; i < 4; i++) { const u = (lt * .9 + i / 4) % 1; g.strokeStyle = OR; g.globalAlpha = (1 - u) * .8; g.lineWidth = 9;
      g.beginPath(); g.arc(0, -150, 120 + u * 360, -Math.PI * .85, -Math.PI * .15); g.stroke(); }
    g.globalAlpha = 1;
    g.fillStyle = al(OR, .2); g.strokeStyle = CREME; g.lineWidth = 10;
    g.beginPath(); g.roundRect(-300, -130, 600, 380, 60); g.fill(); g.stroke();
    g.fillStyle = al(CREME, .12); g.beginPath(); g.roundRect(-250, -80, 300, 280, 30); g.fill();
    g.strokeStyle = al(CREME, .5); g.lineWidth = 6; for (let i = 0; i < 6; i++) { g.beginPath(); g.moveTo(-230, -50 + i * 45); g.lineTo(30, -50 + i * 45); g.stroke(); }
    g.fillStyle = OR; [[170, 0], [170, 140]].forEach(([x, y], i) => { g.beginPath(); g.arc(x, y, 48, 0, 7); g.fill();
      g.strokeStyle = NOIR; g.lineWidth = 8; const a = i ? lt * 2 : -lt; g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * 40, y + Math.sin(a) * 40); g.stroke(); });
    g.restore();
    S.texte('LA BBC · LONDRES', W / 2, 1310, { taille: 90, coul: OR, contour: NOIR, contourL: 10, max: 960 });
    S.texte('18 juin 1940', W / 2, 1430, { taille: 64, police: 'Spectral', it: true, poids: 400, coul: CREME });
  }

  // bulle de commentaire : le niveau défile, puis « ? »
  function commentaire(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .35));
    deux(p.t, 520, 100);
    g.save(); g.translate(W / 2, 980); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-260, 160); g.lineTo(-330, 270); g.lineTo(-170, 165); g.closePath(); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-320, -60, 56, 0, 7); g.fill();
    S.texte('toi', -320, -58, { taille: 36, coul: NOIR });
    const n = lt < 1.6 ? String(1 + Math.floor(lt * 9) % 10) : '?';
    S.texte('Moi : niveau', -230, -60, { taille: 60, police: 'Spectral', poids: 600, coul: NOIR, align: 'left' });
    S.texte(n, 230, -62, { taille: 110, coul: lt < 1.6 ? ROUGE : OR, contour: NOIR, contourL: 6 });
    g.fillStyle = al(NOIR, .15); g.fillRect(-370, 40, 600, 22); g.fillRect(-370, 90, 420, 22);
    g.restore();
    const kf = .5 + .5 * Math.sin(lt * 7); S.texte('↓', W / 2, 1380 + kf * 20, { taille: 120, coul: OR });
  }

  return { echelle, chronometre, carto, radio, commentaire };
};

// sons propres à ces plans (discrets)
window.SONS_A = (p, L) => {
  if (p.type === 'echelle' && p.mode === 'stop') L.push([p.a, 'montee', .45]);
  if (p.type === 'echelle' && p.mode === 'dernier') L.push([p.a + .15, 'tampon', .7]);
  if (p.type === 'chronometre') [0, .5, 1, 1.5].forEach(d => L.push([p.a + d, 'tic', .5]));
  if (p.type === 'carto') L.push([p.a + .2, 'whoosh', .4]);
  if (p.type === 'carto' && p.v === 'pologne') L.push([p.a + .65, 'tampon', .6]);
  if (p.type === 'radio') L.push([p.a, 'statique', .35]);
  if (p.type === 'commentaire') L.push([p.a, 'pop', .5]);
};
