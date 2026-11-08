// Plans propres au short « La lunette astronomique en 60 secondes », style du modèle A (noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Optique : les rayons sont calculés en lentilles minces (constantes X1, F1, F2, TA ci-dessous) :
// faisceau incident parallèle incliné de α (tan α = TA) → tous les rayons passent par B1, dans le plan focal image de
// l'objectif (x = X1 + F1) ; F′1 = F2 ; chaque rayon sort de l'oculaire parallèle à (B1O2), de pente −b/F2,
// donc tan α′ = (F1/F2) tan α. Chaque rayon frappe les lentilles dans leur ouverture (A1, A2). Angles exagérés.
window.SANS_ST_A = ['sujetpc'];
window.PROPRES_A = ['chrono60', 'lunette', 'regle', 'lune', 'oeil', 'formule', 'erreur', 'photo', 'sujetpc'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const VERT = '#7fbf6a', BLEU = '#8fc6e8';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const sous = (s, y, taille = 56) => S.texte(s, W / 2, y, { taille, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 8, max: 960 });
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const lab = (s, x, y, coul = CREME, taille = 40, o = {}) => S.texte(s, x, y, Object.assign({ taille, coul, contour: NOIR, contourL: 8, poids: 700 }, o));

  // ---------- géométrie de la lunette (pixels)
  const Y0 = 880, X1 = 140, F1 = 620, F2 = 170, XF = X1 + F1, X2 = XF + F2, XE = W, TA = .12, A1 = 240, A2 = 150;
  const B = F1 * TA;                  // B1 = (XF, Y0 + B) : image intermédiaire renversée, sous l'axe
  const PENTE = -B / F2;              // pente du faisceau émergent, parallèle à (B1O2)
  const D = [-170, 0, 110];           // hauteurs d'impact sur l'objectif (0 = rayon par O1, non dévié)
  function rayon(d, oculaire) {
    const p0 = [0, Y0 + d - TA * X1], p1 = [X1, Y0 + d], yb = Y0 + B;
    const y2 = p1[1] + (yb - p1[1]) * (X2 - X1) / F1;
    if (!oculaire) return [p0, p1, [XF + 140, p1[1] + (yb - p1[1]) * (F1 + 140) / F1]];
    return [p0, p1, [X2, y2], [XE, y2 + PENTE * (XE - X2)]];
  }
  // contrôle : chaque rayon dans l'ouverture des lentilles
  D.forEach(d => { const r = rayon(d, true); if (Math.abs(r[1][1] - Y0) > A1 || Math.abs(r[2][1] - Y0) > A2) throw new Error('rayon hors lentille ' + d); });
  function poly(pts, k, coul, ep = 7, dash) {
    if (k <= 0) return;
    const L = []; let tot = 0; for (let i = 1; i < pts.length; i++) { const l = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); L.push(l); tot += l; }
    let reste = tot * cl(k);
    g.save(); g.strokeStyle = coul; g.lineWidth = ep; g.lineCap = 'round'; if (dash) g.setLineDash(dash); g.shadowColor = coul; g.shadowBlur = 12;
    g.beginPath(); g.moveTo(...pts[0]);
    for (let i = 1; i < pts.length && reste > 0; i++) { const u = Math.min(1, reste / L[i - 1]); g.lineTo(lerp(pts[i - 1][0], pts[i][0], u), lerp(pts[i - 1][1], pts[i][1], u)); reste -= L[i - 1]; }
    g.stroke(); g.restore();
  }
  // flèche de sens sur un segment, au point u
  function sens(a, b, u, coul) {
    const x = lerp(a[0], b[0], u), y = lerp(a[1], b[1], u), an = Math.atan2(b[1] - a[1], b[0] - a[0]);
    g.save(); g.translate(x, y); g.rotate(an); g.fillStyle = coul; g.beginPath(); g.moveTo(14, 0); g.lineTo(-12, -11); g.lineTo(-12, 11); g.closePath(); g.fill(); g.restore();
  }
  function lentille(x, a, coul, lueur) {
    g.save(); g.strokeStyle = coul; g.lineWidth = 8; g.lineCap = 'round'; if (lueur) { g.shadowColor = coul; g.shadowBlur = 40; }
    g.beginPath(); g.moveTo(x, Y0 - a); g.lineTo(x, Y0 + a); g.stroke();
    g.beginPath(); g.moveTo(x - 22, Y0 - a + 26); g.lineTo(x, Y0 - a); g.lineTo(x + 22, Y0 - a + 26); g.stroke();
    g.beginPath(); g.moveTo(x - 22, Y0 + a - 26); g.lineTo(x, Y0 + a); g.lineTo(x + 22, Y0 + a - 26); g.stroke();
    g.restore();
  }
  function point(x, y, coul, r = 11) { g.save(); g.fillStyle = coul; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.restore(); }

  // ---------- plans
  // ouverture : « 60 » et un anneau qui se vide
  function chrono60(p, t) {
    const k = eo(pr(t, p.a, .4)), u = cl((t - p.a) / Math.max(1, p.b - p.a));
    g.save(); g.translate(W / 2, 820);
    g.strokeStyle = 'rgba(239,230,210,.15)'; g.lineWidth = 30; g.beginPath(); g.arc(0, 0, 290, 0, 7); g.stroke();
    g.strokeStyle = OR; g.shadowColor = OR; g.shadowBlur = 30; g.beginPath(); g.arc(0, 0, 290, -Math.PI / 2, -Math.PI / 2 + k * (1 - u * .15) * 2 * Math.PI); g.stroke(); g.restore();
    pop(back(pr(t, p.a + .1, .3)), W / 2, 790, () => S.texte('60', 0, 0, { taille: 320, police: 'Spectral', poids: 600, coul: CREME }));
    S.texte('SECONDES', W / 2, 990, { taille: 54, coul: OR, esp: 14 });
    deux(p.t || 'LA LUNETTE|ASTRONOMIQUE', 1340, 110);
  }

  // schéma de la lunette ; champs : l2 (oculaire, défaut true), hl ('l1' | 'l2'), rayons (0, 1 = jusqu'à B1, 2 = jusqu'à la sortie),
  // image (A1B1), plan (repère du plan focal), f1 / f2 (repères des foyers F′1 et F2), fleches (repère du « ↑ » de sortie),
  // angles, focales, t / sous (textes), note (angles exagérés)
  function lunette(p, t) {
    const l2 = p.l2 !== false, kt = eo(pr(t, p.a + .1, p.trace || .9));
    // axe optique
    g.save(); g.strokeStyle = 'rgba(239,230,210,.45)'; g.lineWidth = 3; g.setLineDash([22, 14]); g.beginPath(); g.moveTo(30, Y0); g.lineTo(W - 20, Y0); g.stroke(); g.restore();
    lentille(X1, A1, p.hl === 'l1' ? OR : CREME, p.hl === 'l1');
    if (l2) lentille(X2, A2, p.hl === 'l2' ? OR : CREME, p.hl === 'l2');
    lab('OBJECTIF', X1 + 30, Y0 - A1 - 50, p.hl === 'l1' ? OR : CREME, 38, { align: 'left' });
    if (l2) lab('OCULAIRE', X2, Y0 - A2 - 50, p.hl === 'l2' ? OR : CREME, 38);
    lab('L₁', X1 - 50, Y0 + A1 - 10, GRIS, 36); if (l2) lab('L₂', X2 - 50, Y0 + A2 - 10, GRIS, 36);
    // plan focal image de l'objectif
    if (p.plan && t >= tps(p.plan)) { const k = eo(pr(t, tps(p.plan), .4)); g.save(); g.globalAlpha = k; g.strokeStyle = OR; g.lineWidth = 4; g.setLineDash([12, 10]);
      g.beginPath(); g.moveTo(XF, Y0 - 230); g.lineTo(XF, Y0 + 230); g.stroke(); g.restore(); g.save(); g.globalAlpha = k; lab('PLAN FOCAL IMAGE', XF, Y0 - 270, OR, 40); g.restore(); }
    // rayons
    if (p.rayons) D.forEach((d, i) => { const pts = rayon(d, p.rayons === 2 && l2); poly(pts, kt, d === 0 ? VERT : OR, 7);
      if (kt >= 1) { sens(pts[0], pts[1], .5, d === 0 ? VERT : OR); if (pts.length > 3) sens(pts[2], pts[3], .55, d === 0 ? VERT : OR); } });
    // image intermédiaire A1B1 (renversée)
    if (p.image) { const k = eo(pr(t, p.a + .7, .35)); if (k > 0) { g.save(); g.globalAlpha = k; g.strokeStyle = ROUGE; g.fillStyle = ROUGE; g.lineWidth = 8;
      g.beginPath(); g.moveTo(XF, Y0); g.lineTo(XF, Y0 + B - 10); g.stroke(); g.beginPath(); g.moveTo(XF - 14, Y0 + B - 22); g.lineTo(XF, Y0 + B); g.lineTo(XF + 14, Y0 + B - 22); g.fill(); g.restore();
      g.save(); g.globalAlpha = k; lab('B₁', XF + 40, Y0 + B + 30, ROUGE, 38); lab('A₁', XF - 42, Y0 - 28, ROUGE, 38); g.restore(); } }
    // foyers
    const kf1 = p.f1 ? eo(pr(t, tps(p.f1), .3)) : 0, kf2 = p.f2 ? eo(pr(t, tps(p.f2), .3)) : 0;
    if (kf1 > 0) { point(XF, Y0, OR, 12 * kf1); pop(kf1, XF - 10, Y0 - 60, () => lab('F′₁', 0, 0, OR, 50)); }
    if (kf2 > 0) { pop(kf2, XF + 70, Y0 + 60, () => lab('F₂', 0, 0, BLEU, 50)); }
    if (kf1 >= 1 && kf2 >= 1 && p.egal) { const k = back(pr(t, tps(p.egal), .3)); pop(pr(t, tps(p.egal), .3), W / 2, 520, () => S.texte('F′₁ = F₂', 0, 0, { taille: 110, coul: OR, contour: NOIR, contourL: 12 })); }
    // sens de propagation : ça descend, puis ça remonte
    if (p.fleches) {
      pop(pr(t, p.a + .3, .3), 330, 420, () => { lab('↘', 0, 0, OR, 110); lab('ENTRENT EN DESCENDANT', 0, 90, CREME, 34); });
      if (t >= tps(p.fleches)) pop(pr(t, tps(p.fleches), .3), 860, 420, () => { lab('↗', 0, 0, OR, 110); lab('RESSORTENT EN MONTANT', -40, 90, CREME, 34); });
    }
    // angles α (incident, en O1) et α′ (émergent, en O2) ; la droite (B1O2) en pointillés
    if (p.angles) {
      const k = eo(pr(t, p.a + .3, .4)), aa = Math.atan(TA), ab = Math.atan(-PENTE);
      g.save(); g.globalAlpha = k; g.strokeStyle = CREME; g.lineWidth = 4; g.setLineDash([10, 10]); g.beginPath(); g.moveTo(XF, Y0 + B); g.lineTo(XE, Y0 + PENTE * (XE - X2)); g.stroke(); g.restore();
      g.save(); g.globalAlpha = k; g.strokeStyle = VERT; g.lineWidth = 6; g.beginPath(); g.arc(X1, Y0, 150, 0, aa); g.stroke();
      g.strokeStyle = ROUGE; g.beginPath(); g.arc(X2, Y0, 105, -ab, 0); g.stroke(); g.restore();
      g.save(); g.globalAlpha = k; lab('α', X1 + 175, Y0 + 42, VERT, 52); lab('α′', X2 + 55, Y0 - 80, ROUGE, 52); g.restore();
    }
    // focales (schéma pas à l'échelle : seulement les noms)
    if (p.focales) { const k = eo(pr(t, p.a + .2, .4)); g.save(); g.globalAlpha = k; g.strokeStyle = OR; g.lineWidth = 5;
      [[X1, XF, 'f′₁', -300], [XF, X2, 'f′₂', -200]].forEach(([a, b, s, dy]) => { g.beginPath(); g.moveTo(a, Y0 + dy + 18); g.lineTo(a, Y0 + dy); g.lineTo(b, Y0 + dy); g.lineTo(b, Y0 + dy + 18); g.stroke(); lab(s, (a + b) / 2, Y0 + dy - 40, OR, 54); });
      g.restore(); }
    if (p.note !== false && p.rayons) S.texte('schéma : angles exagérés', W - 40, Y0 + A1 + 70, { taille: 30, it: true, poids: 400, police: 'Spectral', coul: GRIS, align: 'right' });
    if (p.t) { const k = eo(pr(t, p.at ? tps(p.at) : p.a + .2, .3)); g.save(); g.globalAlpha = k; deux(p.t, 1390, 100); g.restore(); }
    if (p.sous) { const k = eo(pr(t, p.asous ? tps(p.asous) : p.a + .4, .3)); g.save(); g.globalAlpha = k; sous(p.sous, 1530); g.restore(); }
  }

  // la lunette du TP à l'échelle : 50 cm + 5 cm = 55 cm ; p.e50, p.e5, p.e55 = repères des trois cotes
  function regle(p, t) {
    const x0 = 90, cm = 16, xf = x0 + 50 * cm, x2 = x0 + 55 * cm, y = 860;
    g.save(); g.strokeStyle = 'rgba(239,230,210,.45)'; g.lineWidth = 3; g.setLineDash([22, 14]); g.beginPath(); g.moveTo(40, y); g.lineTo(W - 40, y); g.stroke(); g.restore();
    lentille(x0, 200, CREME); lentille(x2, 120, CREME);
    point(xf, y, OR); lab('F′₁ = F₂', xf - 20, y + 60, OR, 40);
    lab('OBJECTIF', x0 + 20, y - 250, CREME, 36, { align: 'left' }); lab('OCULAIRE', x2 - 40, y - 170, CREME, 36);
    const cote = (a, b, yy, s, k, c) => { if (k <= 0) return; g.save(); g.globalAlpha = cl(k * 2); g.strokeStyle = c; g.lineWidth = 6;
      g.beginPath(); g.moveTo(a, yy - 16); g.lineTo(a, yy + 16); g.moveTo(a, yy); g.lineTo(lerp(a, b, eo(k)), yy); if (k >= 1) { g.moveTo(b, yy - 16); g.lineTo(b, yy + 16); } g.stroke(); g.restore();
      if (k >= .6) lab(s, (a + b) / 2, yy - 50, c, 56); };
    cote(x0, xf, y - 330, '50 cm', p.e50 ? pr(t, tps(p.e50), .4) : 1, OR);
    cote(xf, x2, y - 330, '5 cm', p.e5 ? pr(t, tps(p.e5), .3) : 1, BLEU);
    cote(x0, x2, y + 230, 'O₁O₂ = 55 cm', p.e55 ? pr(t, tps(p.e55), .5) : 1, CREME);
    S.texte('à l’échelle', W - 50, y + 330, { taille: 32, it: true, poids: 400, police: 'Spectral', coul: GRIS, align: 'right' });
    deux(p.t || 'O₁O₂ = f′₁ + f′₂', 1390, 100);
  }

  // Lune dessinée (mers, un cratère repéré au nord) ; p.flip : retournement dans la lunette ; p.etape 'taille' : image de 6,3 mm sur une règle
  function disque(cx, cy, r, rot, cercle) {
    g.save(); g.translate(cx, cy); g.rotate(rot);
    const gr = g.createRadialGradient(-r * .3, -r * .3, r * .1, 0, 0, r); gr.addColorStop(0, '#efe9dc'); gr.addColorStop(1, '#b9b2a2');
    g.fillStyle = gr; g.shadowColor = 'rgba(239,230,210,.35)'; g.shadowBlur = 50; g.beginPath(); g.arc(0, 0, r, 0, 7); g.fill(); g.shadowBlur = 0;
    g.fillStyle = 'rgba(90,85,75,.45)';
    [[-.35, -.1, .28], [.05, -.25, .2], [.3, .1, .22], [-.1, .3, .18], [-.45, .35, .12]].forEach(([x, y, s]) => { g.beginPath(); g.ellipse(x * r, y * r, s * r, s * r * .75, x, 0, 7); g.fill(); });
    // le cratère repéré, au nord
    g.fillStyle = 'rgba(70,65,58,.8)'; g.beginPath(); g.arc(.12 * r, -.68 * r, .09 * r, 0, 7); g.fill();
    if (cercle) { g.strokeStyle = ROUGE; g.lineWidth = Math.max(4, r * .03); g.beginPath(); g.arc(.12 * r, -.68 * r, .19 * r, 0, 7); g.stroke(); }
    g.restore();
  }
  function lune(p, t) {
    if (p.etape === 'taille') {
      // règle graduée en millimètres (1 mm = 80 px), image de la Lune : 700 mm × 9,0 × 10⁻³ rad = 6,3 mm
      const x0 = 140, mm = 80, y = 1080, k = eo(pr(t, p.a + .2, .5));
      g.save(); g.fillStyle = '#e9dfc8'; g.fillRect(x0 - 30, y, 10 * mm + 60, 110); g.strokeStyle = NOIR; g.lineWidth = 3;
      for (let i = 0; i <= 10; i++) { g.beginPath(); g.moveTo(x0 + i * mm, y); g.lineTo(x0 + i * mm, y + (i % 5 ? 36 : 56)); g.stroke(); S.texte(String(i), x0 + i * mm, y + 82, { taille: 28, coul: NOIR }); }
      g.restore();
      S.texte('mm', x0 + 10 * mm + 60, y + 82, { taille: 28, coul: CREME });
      disque(x0 + 3.15 * mm, y - 3.15 * mm - 30, 3.15 * mm * k, Math.PI, false);
      if (k > .5) { g.save(); g.strokeStyle = ROUGE; g.lineWidth = 5; g.beginPath(); g.moveTo(x0, y - 20); g.lineTo(x0 + 6.3 * mm, y - 20); g.stroke(); g.restore(); }
      pop(pr(t, p.a + .6, .3), 860, 740, () => { S.texte('≈ 6,3 mm', 0, 0, { taille: 96, coul: OR, contour: NOIR, contourL: 10 }); });
      S.texte('l’image de la Lune', 860, 840, { taille: 44, it: true, poids: 400, police: 'Spectral', coul: CREME });
      S.texte('au foyer d’un objectif de 700 mm', 860, 895, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 400 });
      deux(p.t || 'RÉELLE|ET MINUSCULE', 1420, 100);
      return;
    }
    const tf = p.flip ? tps(p.flip) : 1e9, kf = S.eio(pr(t, tf, .6)), avant = t < tf + .3;
    disque(W / 2, 830, 300, Math.PI * kf, true);
    if (avant) { lab('NORD', W / 2, 440, OR, 50); lab('À L’ŒIL NU', W / 2, 1250, CREME, 60); }
    else { pop(pr(t, tf + .3, .3), W / 2, 1250, () => lab('DANS LA LUNETTE : EN BAS', 0, 0, ROUGE, 66, { max: 980 })); }
    if (p.t) deux(p.t, 1420, 100);
  }

  // l'œil au repos : un faisceau parallèle converge sur la rétine, rétine dans le plan focal du cristallin
  function oeil(p, t) {
    const cx = 600, cy = 880, R = 270, xl = 380, xr = 860, pen = -.2, k = eo(pr(t, p.a + .1, .8));
    g.save(); g.fillStyle = '#1b1712'; g.strokeStyle = CREME; g.lineWidth = 7; g.beginPath(); g.arc(cx, cy, R, 0, 7); g.fill(); g.stroke();
    g.strokeStyle = ROUGE; g.lineWidth = 10; g.beginPath(); g.arc(cx, cy, R - 8, -.9, .9); g.stroke();
    g.fillStyle = 'rgba(143,198,232,.35)'; g.strokeStyle = BLEU; g.lineWidth = 5; g.beginPath(); g.ellipse(xl, cy, 34, 120, 0, 0, 7); g.fill(); g.stroke(); g.restore();
    // foyer sur la rétine : le rayon qui passe par le centre du cristallin n'est pas dévié
    const fy = cy + pen * (xr - xl);
    [-95, 0, 95].forEach((d, i) => { const ya = cy + d, y0 = ya - pen * xl; poly([[0, y0], [xl, ya], [xr, fy]], k, i === 1 ? VERT : OR, 6); });
    if (k >= 1) point(xr, fy, ROUGE, 14);
    lab('CRISTALLIN', xl, cy + 170, BLEU, 36); lab('RÉTINE', xr - 10, cy + 300, ROUGE, 36);
    S.texte('rayons parallèles entre eux', 230, 560, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: CREME });
    deux(p.t || 'NET|SANS ACCOMMODER', 1390, 110);
  }

  // formules qui apparaissent ligne par ligne ; lignes = [[repère, texte, style]] ; style 'cadre' (relation à retenir), 'petit', 'ok'
  function formule(p, t) {
    if (p.sur) S.texte(p.sur, W / 2, 420, { taille: 44, coul: OR, esp: 8, poids: 700, max: 960 });
    const L = (p.lignes || []).filter(([a]) => !a || t >= tps(a));
    L.forEach(([a, s, st], j) => {
      const ta = a ? tps(a) : p.a, k = pr(t, ta, .3), y = (p.y0 || 720) + j * 210;
      pop(k, W / 2, y, () => {
        if (st === 'cadre') { const w = S.largeur(s, { taille: 120, police: 'Spectral', poids: 600 }) + 100; g.strokeStyle = OR; g.lineWidth = 8; g.strokeRect(-w / 2, -95, w, 190); }
        S.texte(s, 0, 0, { taille: st === 'petit' ? 60 : 120, police: st === 'petit' ? 'Archivo' : 'Spectral', poids: 600, coul: st === 'ok' ? OR : CREME, contour: NOIR, contourL: 10, max: 960 });
      });
    });
    if (p.t) deux(p.t, 1420, 100);
  }

  // l'erreur classique : F′1 = F2, pas F1 = F′2
  function erreur(p, t) {
    S.texte('L’ERREUR CLASSIQUE', W / 2, 420, { taille: 50, coul: ROUGE, esp: 8, poids: 700 });
    const k1 = p.bon ? pr(t, tps(p.bon), .3) : 1;
    pop(k1, W / 2, 700, () => { S.texte('✓  F′₁ = F₂', 0, 0, { taille: 130, police: 'Spectral', poids: 600, coul: VERT, contour: NOIR, contourL: 10 });
      S.texte('foyer image de l’objectif = foyer objet de l’oculaire', 0, 100, { taille: 38, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 }); });
    if (p.faux) { const tf = tps(p.faux), k2 = pr(t, tf, .3);
      pop(k2, W / 2, 1060, () => { S.texte('✗  F₁ = F′₂', 0, 0, { taille: 130, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 10 }); });
      if (t >= tf + .35) { g.save(); g.strokeStyle = ROUGE; g.lineWidth = 12; g.beginPath(); g.moveTo(250, 1070); g.lineTo(lerp(250, 830, eo(pr(t, tf + .35, .25))), 1050); g.stroke(); g.restore();
        O.tampon('FAUX', W / 2, 1330, pr(t, tf + .5, .3), -.1, 150); } }
  }

  // photo d'archive en carte découpée, zoom réglable
  function photo(p, t, l) {
    O.carte(p.img, W / 2, 780, 820, 820, -.025, (p.z || 1.1) + l * .03, p.fx ?? .5, p.fy ?? .5, { lum: p.lum || .95 });
    if (p.t) deux(p.t, 1340, 110);
    if (p.sous) sous(p.sous, 1500);
  }

  // copie du bac de physique-chimie
  function sujetpc(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 880, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-380, -480, 760, 960); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
    S.texte('PHYSIQUE-CHIMIE', 0, -315, { taille: 40, coul: GRIS, esp: 8, poids: 600 });
    g.fillStyle = NOIR; g.fillRect(-300, -260, 600, 3);
    S.texte(p.ex || 'Exercice · La lunette astronomique', -300, -190, { taille: 36, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400, max: 600 });
    (p.sujet || ['Établir l’expression', 'du grossissement G']).forEach((s, i) => S.texte(s, 0, -90 + i * 86, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, max: 680 }));
    if (p.formule) S.texte(p.formule, 0, 130, { taille: 62, police: 'Spectral', poids: 600, coul: ROUGE, max: 680 });
    for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-300, 240 + i * 50, 600 - (i === 3 ? 250 : 0), 6); }
    const kc = pr(t, p.a + .35, .5); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(0, -48, 360, 120, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['À SAVOIR ', CREME], ['RÉDIGER', ROUGE]], 1560, 110);
  }

  return { chrono60, lunette, regle, lune, oeil, formule, erreur, photo, sujetpc };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono60') for (let k = 0; k < 6; k++) L.push([p.a + .2 + k * .3, 'tic', .4]);
  if (p.type === 'lunette') { if (p.rayons) L.push([p.a + .1, 'whoosh', .4]); ['plan', 'f1', 'f2', 'egal', 'fleches'].forEach(c => { if (p[c]) L.push([tps(p[c]), 'pop', .4]); }); }
  if (p.type === 'regle') ['e50', 'e5', 'e55'].forEach(c => { if (p[c]) L.push([tps(p[c]), 'blip', .4]); });
  if (p.type === 'lune') { if (p.flip) L.push([tps(p.flip), 'rembobine', .6]); else L.push([p.a + .6, 'pop', .4]); }
  if (p.type === 'oeil') L.push([p.a + .1, 'souffle', .4]);
  if (p.type === 'formule') (p.lignes || []).forEach(([a]) => L.push([a ? tps(a) : p.a, 'pop', .45]));
  if (p.type === 'erreur') { if (p.bon) L.push([tps(p.bon), 'valide', .6]); if (p.faux) L.push([tps(p.faux), 'buzz', .6], [tps(p.faux) + .55, 'tampon', 1]); }
  if (p.type === 'sujetpc') L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .6]);
};
