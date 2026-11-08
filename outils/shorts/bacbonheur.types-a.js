// Plans propres au short « bacbonheur » (« Faut-il renoncer à ses désirs pour être heureux ? »), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
window.SANS_ST_A = ['chrono', 'loupe', 'cite', 'erreur', 'reglage'];
window.PROPRES_A = ['chrono', 'loupe', 'tonneau', 'phone', 'pierres', 'cite', 'ailes', 'erreur', 'reglage'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const PAPIER = '#f3ecdc', EAU = '#8fb6cf';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // texte de l'étape courante : etapes = [[repère ou null, texte], …]
  const etapeTxt = (p, t) => { let s = p.etapes[0][1], a = p.a; p.etapes.forEach(([r, x]) => { if (!r || t >= tps(r)) { s = x; a = r ? tps(r) : p.a; } }); return [s, a]; };

  // compte à rebours de 60 s ; p.run : il tourne
  function chrono(p, t) {
    const u = p.run ? cl((t - p.a) / 60) : 0, reste = p.run ? Math.max(0, 60 - Math.floor(t - p.a)) : 60;
    const k = back(pr(t, p.a, .35)), cx = W / 2, cy = 760, r = 250;
    g.save(); g.translate(cx, cy); g.scale(lerp(.6, 1, k), lerp(.6, 1, k));
    g.strokeStyle = 'rgba(239,230,210,.15)'; g.lineWidth = 26; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
    g.strokeStyle = p.run ? ROUGE : OR; g.lineCap = 'round'; g.beginPath(); g.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
    for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(Math.cos(a) * (r - 50), Math.sin(a) * (r - 50)); g.lineTo(Math.cos(a) * (r - 30), Math.sin(a) * (r - 30)); g.stroke(); }
    S.texte(String(reste), 0, -10, { taille: 230, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 40 });
    S.texte('SECONDES', 0, 120, { taille: 40, coul: CREME, esp: 10, poids: 600 });
    g.restore();
    if (p.t) { const kt = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1290); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt)); g.translate(-W / 2, -1290); deux(p.t, 1290, 110); g.restore(); }
  }

  // le sujet sur une fiche ; cercles = [[repère, mot], …] entourés au stylo rouge ; lignes = [[repère, texte, style], …]
  function loupe(p, t) {
    const k = eo(pr(t, p.a, .35));
    const L1 = 'Faut-il renoncer à ses désirs', L2 = 'pour être heureux ?';
    let taille = 64; const w1 = S.largeur(L1, { taille, police: 'Spectral', poids: 600 }); if (w1 > 860) taille *= 860 / w1;
    const o = { taille, police: 'Spectral', poids: 600, coul: NOIR };
    g.save(); g.translate(W / 2, lerp(900, 620, k)); g.rotate(-.02);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = PAPIER; g.fillRect(-470, -210, 940, 420); g.shadowColor = 'transparent';
    S.texte('SUJET · PHILOSOPHIE', 0, -140, { taille: 30, coul: GRIS, esp: 6 });
    const x0 = -S.largeur(L1, o) / 2;
    const actifs = (p.cercles || []).filter(([r]) => t >= tps(r)).map(([, m]) => m);
    // première ligne mot à mot (les mots entourés passent en rouge)
    let x = x0; L1.split(' ').forEach((m, i) => { const s = (i ? ' ' : '') + m, ws = S.largeur(s, o);
      S.texte(s, x + ws / 2, -30, Object.assign({}, o, { coul: actifs.includes(m) ? ROUGE : NOIR })); x += ws; });
    S.texte(L2, 0, 60, o);
    (p.cercles || []).forEach(([r, m]) => {
      const kc = pr(t, tps(r), .4); if (kc <= 0) return;
      const i = L1.split(' ').indexOf(m), avant = L1.split(' ').slice(0, i).join(' ') + (i ? ' ' : '');
      const cx = x0 + S.largeur(avant, o) + S.largeur(m, o) / 2, rx = S.largeur(m, o) / 2 + 26;
      g.strokeStyle = ROUGE; g.lineWidth = 7; g.beginPath(); g.ellipse(cx, -30, rx, 48, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    });
    g.restore();
    if (p.t) { const kt = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1010); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt)); g.translate(-W / 2, -1010); deux(p.t, 1010, 110); g.restore(); }
    (p.lignes || []).forEach(([r, s, st], j) => {
      const tr = tps(r); if (t < tr) return;
      const kl = back(pr(t, tr, .3)), y = 1240 + j * 140;
      g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, kl), lerp(1.5, 1, kl));
      const coul = st === 'or' ? OR : st === 'barre' ? GRIS : CREME;
      const r2 = S.texte(s, 0, 0, { taille: 92, coul, contour: NOIR, contourL: 10, max: 960 });
      if (st === 'barre') { const kb = eo(pr(t, tr + .25, .3)); g.strokeStyle = ROUGE; g.lineWidth = 12; g.beginPath(); g.moveTo(-r2.w / 2 - 20, 6); g.lineTo(-r2.w / 2 - 20 + (r2.w + 40) * kb, -4); g.stroke(); }
      g.restore();
    });
  }

  // le tonneau percé : on verse sans fin, l'eau fuit par les trous
  function tonneau(p, t, l) {
    O.fondImg('danaides', 1.25, .5, .45, .3);
    const cx = W / 2, top = 640, bot = 1180, rx = 230, ry = 60;
    // filet versé d'en haut
    g.save(); g.strokeStyle = EAU; g.lineWidth = 26; g.lineCap = 'round'; g.setLineDash([60, 24]); g.lineDashOffset = -t * 900;
    g.beginPath(); g.moveTo(cx - 20, 300); g.quadraticCurveTo(cx - 10, 450, cx, top + 30); g.stroke(); g.setLineDash([]); g.restore();
    // cruche
    g.save(); g.translate(cx - 130, 270); g.rotate(.6 + Math.sin(t * 3) * .04); g.fillStyle = '#7a5a3a'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-60, -90); g.quadraticCurveTo(-110, 0, -60, 90); g.lineTo(60, 90); g.quadraticCurveTo(110, 0, 60, -90); g.closePath(); g.fill(); g.stroke(); g.restore();
    // corps du tonneau (renflé)
    const corps = () => { g.beginPath(); g.moveTo(cx - rx, top); g.bezierCurveTo(cx - rx - 70, top + 180, cx - rx - 70, bot - 180, cx - rx, bot);
      g.lineTo(cx + rx, bot); g.bezierCurveTo(cx + rx + 70, bot - 180, cx + rx + 70, top + 180, cx + rx, top); g.closePath(); };
    g.fillStyle = '#5a3f28'; corps(); g.fill();
    // niveau d'eau qui ne monte jamais : visible en coupe
    const niv = bot - 90 - (Math.sin(t * 2.4) * .5 + .5) * 70;
    g.save(); corps(); g.clip(); g.fillStyle = 'rgba(143,182,207,.35)'; g.fillRect(cx - rx - 80, niv, 2 * rx + 160, bot - niv); g.restore();
    g.strokeStyle = 'rgba(0,0,0,.35)'; g.lineWidth = 5; for (let i = -3; i <= 3; i++) { g.beginPath(); g.moveTo(cx + i * 62, top + 4); g.quadraticCurveTo(cx + i * 80, (top + bot) / 2, cx + i * 62, bot - 4); g.stroke(); }
    g.strokeStyle = CREME; g.lineWidth = 7; corps(); g.stroke();
    g.fillStyle = OR; [top + 90, bot - 90].forEach(y => { g.fillRect(cx - rx - 46, y - 12, 2 * rx + 92, 24); });
    g.fillStyle = '#2a1d12'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.ellipse(cx, top, rx, ry, 0, 0, 7); g.fill(); g.stroke();
    // trous et fuites
    [[-150, 980], [-40, 1060], [90, 940], [175, 1040]].forEach(([dx, y], i) => {
      const s = dx < 0 ? -1 : 1;
      g.save(); g.strokeStyle = EAU; g.lineWidth = 12; g.lineCap = 'round'; g.setLineDash([26, 16]); g.lineDashOffset = -t * 500 - i * 13;
      g.beginPath(); g.moveTo(cx + dx, y); g.quadraticCurveTo(cx + dx + s * 140, y + 20, cx + dx + s * 190, 1340); g.stroke(); g.restore();
      g.fillStyle = NOIR; g.beginPath(); g.arc(cx + dx, y, 16, 0, 7); g.fill();
    });
    g.fillStyle = 'rgba(143,182,207,.25)'; g.beginPath(); g.ellipse(cx, 1340, 420, 40, 0, 0, 7); g.fill();
    if (p.t) O.multi([[p.t, CREME]], 1420, 92);
    if (p.t2 && t >= tps(p.a2)) O.tampon(p.t2, W / 2, 1545, pr(t, tps(p.a2), .3), -.06, 80);
  }

  // le téléphone : vidéo après vidéo ; coups = repères où l'on passe à la suivante
  function phone(p, t) {
    const cx = W / 2, cy = 820, pw = 520, ph = 920;
    const passes = (p.coups || []).filter(r => t >= tps(r)), n = passes.length;
    const kd = n ? eo(pr(t, tps(passes[n - 1]), .35)) : 1, off = (n - 1 + kd) * (ph - 60);
    g.save(); g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.roundRect(cx - pw / 2, cy - ph / 2, pw, ph, 60); g.fill(); g.stroke();
    g.beginPath(); g.roundRect(cx - pw / 2 + 22, cy - ph / 2 + 22, pw - 44, ph - 44, 42); g.clip();
    const coul = ['#4a3324', '#2f3a44', '#4a2526', '#33402c'];
    for (let i = 0; i < 4; i++) {
      const y = cy - ph / 2 + 30 + i * (ph - 60) - off; if (y > cy + ph / 2 || y + ph < cy - ph / 2) continue;
      g.fillStyle = coul[i]; g.fillRect(cx - pw / 2 + 22, y, pw - 44, ph - 64);
      S.d.lecture(cx, y + (ph - 60) / 2 - 40, 60, CREME, 'rgba(0,0,0,.45)');
      S.texte('VIDÉO ' + (i + 1), cx, y + (ph - 60) / 2 + 90, { taille: 52, coul: CREME, esp: 4 });
      g.fillStyle = 'rgba(239,230,210,.3)'; g.fillRect(cx - pw / 2 + 60, y + ph - 150, pw - 120, 8);
      g.fillStyle = ROUGE; g.fillRect(cx - pw / 2 + 60, y + ph - 150, (pw - 120) * ((t * .35 + i * .3) % 1), 8);
    }
    g.restore();
    // doigt qui balaie vers le haut à chaque passage
    if (n) { const kf = pr(t, tps(passes[n - 1]), .35); if (kf < 1) { g.save(); g.globalAlpha = 1 - kf; S.d.fleche(cx + 300, cy + 220, cx + 300, cy - 200 * kf - 20, 1, { trait: OR, ep: 12 }); g.restore(); } }
    const msg = n === 0 ? 'LA VIDÉO SUIVANTE…' : 'PUIS LA SUIVANTE…';
    const km = back(pr(t, n ? tps(passes[n - 1]) : p.a, .3)); g.save(); g.translate(W / 2, 1420); g.scale(lerp(1.4, 1, km), lerp(1.4, 1, km)); g.translate(-W / 2, -1420);
    O.multi([[msg, n >= 2 ? OR : CREME]], 1420, 92); g.restore();
  }

  // les pierres de Calliclès : la plus heureuse reçoit une couronne
  function pierres(p, t) {
    O.fondImg('pierres', 1.2, .5, .6, .3);
    O.petitTitre('— CALLICLÈS —', 430);
    [[200, 1130, 70, .4], [860, 1140, 85, 1.3], [330, 1180, 50, 2.1], [740, 1190, 55, .9]].forEach(([x, y, r, rot]) => S.d.pierre(x, y, r, rot, { trait: 'rgba(239,230,210,.6)', fond: '#4a423a', ep: 6 }));
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 960); g.scale(k, k);
    S.d.pierre(0, 0, 200, .2, { trait: CREME, fond: '#5b5247', ep: 10 });
    const kc = t >= tps(p.couronne) ? back(pr(t, tps(p.couronne), .35)) : 0;
    // visage paisible
    g.strokeStyle = NOIR; g.lineWidth = 9; g.lineCap = 'round';
    [-60, 60].forEach(dx => { g.beginPath(); g.arc(dx, -20, 22, Math.PI * 1.1, Math.PI * 1.9, false); g.stroke(); });
    g.beginPath(); g.arc(0, 30, 50 + kc * 10, .2 * Math.PI, .8 * Math.PI); g.stroke();
    if (kc > 0) { g.save(); g.translate(0, lerp(-400, -200, kc)); g.fillStyle = OR; g.strokeStyle = NOIR; g.lineWidth = 6;
      g.beginPath(); g.moveTo(-110, 40); g.lineTo(-110, -40); g.lineTo(-55, 5); g.lineTo(0, -60); g.lineTo(55, 5); g.lineTo(110, -40); g.lineTo(110, 40); g.closePath(); g.fill(); g.stroke();
      g.fillStyle = ROUGE; [-55, 0, 55].forEach(x => { g.beginPath(); g.arc(x, 18, 11, 0, 7); g.fill(); }); g.restore(); }
    g.restore();
    if (p.t) deux(p.t, 1420, 110);
  }

  // un portrait et sa citation, tapée au fil de la voix (aq = repère où commence la citation)
  function cite(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte(p.img, W / 2 + lerp(260, 0, k), 620, 500, 620, lerp(.12, -.03, k), 1.05 + (t - p.a) * .03, .5, .35, { lum: .95 });
    S.texte(p.nom, W / 2, 1010, { taille: 92, coul: OR, contour: NOIR, contourL: 10 });
    const lignes = p.q.split('|'), tot = lignes.join('').length, n = Math.floor(cl((t - tps(p.aq || p.a)) / (p.duree || 1.6)) * tot);
    let c = 0; lignes.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte(vis, W / 2, 1150 + i * 86, { taille: 66, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 980 }); });
    if (p.src) { const ks = eo(pr(t, tps(p.aq || p.a) + (p.duree || 1.6), .4)); g.save(); g.globalAlpha = ks;
      S.texte(p.src, W / 2, 1170 + lignes.length * 86, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: '#b8ad97', max: 960 }); g.restore(); }
  }

  // un oiseau vole, tu restes au sol, sans souffrir
  function ailes(p, t) {
    const lt = t - p.a;
    // oiseau
    const bx = p.vole ? W / 2 + Math.cos(lt * 1.6) * 300 : lerp(-100, 820, cl(lt / 2.6)), by = p.vole ? 560 + Math.sin(lt * 1.6) * 110 : 640 - Math.sin(cl(lt / 2.6) * Math.PI) * 140;
    const bat = Math.sin(lt * 14) * 40;
    g.save(); g.strokeStyle = CREME; g.lineWidth = 12; g.lineCap = 'round'; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(bx - 110, by - bat); g.quadraticCurveTo(bx - 50, by - 50 - bat * .3, bx, by); g.quadraticCurveTo(bx + 50, by - 50 - bat * .3, bx + 110, by - bat); g.stroke(); g.restore();
    // toi, au sol, qui regardes en l'air (calme)
    g.strokeStyle = 'rgba(239,230,210,.4)'; g.lineWidth = 6; g.beginPath(); g.moveTo(80, 1250); g.lineTo(1000, 1250); g.stroke();
    S.d.tete(430, 960, 150, { trait: CREME, fond: '#1b1712', ep: 8 });
    g.strokeStyle = CREME; g.lineWidth = 9; g.lineCap = 'round';
    g.beginPath(); g.moveTo(420, 1110); g.lineTo(420, 1250); g.stroke();
    // sourire paisible (profil tourné vers la droite)
    g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.arc(520, 975, 22, .1 * Math.PI, .6 * Math.PI); g.stroke();
    const [txt, ta] = etapeTxt(p, t), kt = back(pr(t, ta, .3));
    g.save(); g.translate(W / 2, 1420); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt)); g.translate(-W / 2, -1420); deux(txt, 1420, 100); g.restore();
  }

  // l'erreur : un III « ça dépend », barré
  function erreur(p, t) {
    O.petitTitre('L’ERREUR À NE PAS FAIRE', 400, ROUGE);
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1300, 860, k)); g.rotate(-.025);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = PAPIER; g.fillRect(-460, -300, 920, 600); g.shadowColor = 'transparent';
    g.strokeStyle = 'rgba(80,110,160,.25)'; g.lineWidth = 2; for (let y = -220; y < 300; y += 70) { g.beginPath(); g.moveTo(-430, y); g.lineTo(430, y); g.stroke(); }
    g.strokeStyle = 'rgba(200,55,45,.5)'; g.beginPath(); g.moveTo(-360, -300); g.lineTo(-360, 300); g.stroke();
    const txt = 'III. Ça dépend…', n = Math.floor(cl((t - p.a - .2) / .7) * txt.length);
    S.texte(txt.slice(0, n), -330, -80, { taille: 92, police: 'Spectral', it: true, poids: 500, coul: NOIR, align: 'left' });
    S.texte('… de chacun.'.slice(0, Math.max(0, n - 8)), -330, 50, { taille: 70, police: 'Spectral', it: true, poids: 400, coul: NOIR, align: 'left' });
    const kb = pr(t, tps(p.barre), .25), kb2 = pr(t, tps(p.barre) + .15, .25);
    g.strokeStyle = ROUGE; g.lineWidth = 16; g.lineCap = 'round';
    if (kb > 0) { g.beginPath(); g.moveTo(-380, -200); g.lineTo(lerp(-380, 400, kb), lerp(-200, 200, kb)); g.stroke(); }
    if (kb2 > 0) { g.beginPath(); g.moveTo(400, -200); g.lineTo(lerp(400, -380, kb2), lerp(-200, 200, kb2)); g.stroke(); }
    g.restore();
    if (t >= tps(p.barre) + .3) O.tampon('À ÉVITER', W / 2, 1400, pr(t, tps(p.barre) + .3, .3), -.1, 120);
  }

  // le curseur des désirs : supprimer (zéro) ou régler (au milieu)
  function reglage(p, t) {
    O.petitTitre('DÉPLACER LA QUESTION', 420);
    S.texte('TES DÉSIRS', W / 2, 640, { taille: 64, coul: CREME, esp: 6 });
    const x0 = 160, x1 = 920, y = 860;
    const ts = tps(p.sup), tr = tps(p.reg);
    let u = .9, coul = CREME;
    if (t >= ts) { u = lerp(.9, 0, eo(pr(t, ts, .45))); coul = ROUGE; }
    if (t >= tr) { u = lerp(0, .5, eo(pr(t, tr, .5))); coul = OR; }
    g.fillStyle = 'rgba(239,230,210,.18)'; g.beginPath(); g.roundRect(x0, y - 16, x1 - x0, 32, 16); g.fill();
    g.fillStyle = coul; g.beginPath(); g.roundRect(x0, y - 16, (x1 - x0) * u + 1, 32, 16); g.fill();
    for (let i = 0; i <= 10; i++) { g.fillStyle = 'rgba(239,230,210,.4)'; g.fillRect(x0 + (x1 - x0) * i / 10 - 2, y + 34, 4, i % 5 ? 14 : 28); }
    const kx = x0 + (x1 - x0) * u;
    g.save(); if (coul === OR) { g.shadowColor = OR; g.shadowBlur = 40; } g.fillStyle = coul; g.strokeStyle = NOIR; g.lineWidth = 6;
    g.beginPath(); g.arc(kx, y, 48, 0, 7); g.fill(); g.stroke(); g.restore();
    S.texte('ZÉRO', x0, y + 110, { taille: 40, coul: GRIS, poids: 600 });
    S.texte('SANS FIN', x1, y + 110, { taille: 40, coul: GRIS, poids: 600 });
    S.d.pierre(x0, y - 120, 46, .3, { trait: 'rgba(239,230,210,.6)', fond: '#4a423a', ep: 5 });
    // petit tonneau stylisé à droite
    g.strokeStyle = 'rgba(239,230,210,.6)'; g.lineWidth = 5; g.beginPath(); g.ellipse(x1, y - 150, 34, 10, 0, 0, 7); g.stroke();
    g.beginPath(); g.moveTo(x1 - 34, y - 150); g.quadraticCurveTo(x1 - 48, y - 115, x1 - 34, y - 80); g.lineTo(x1 + 34, y - 80); g.quadraticCurveTo(x1 + 48, y - 115, x1 + 34, y - 150); g.stroke();
    if (t >= ts && t < tr) { const k = back(pr(t, ts, .3)); g.save(); g.translate(W / 2, 1180); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
      S.texte('SUPPRIMER ✗', 0, 0, { taille: 120, coul: ROUGE, contour: NOIR, contourL: 12, max: 960 }); g.restore();
      S.texte('ne plus vivre', W / 2, 1300, { taille: 60, police: 'Spectral', it: true, poids: 400, coul: CREME }); }
    if (t >= tr) { const k = back(pr(t, tr, .3)); g.save(); g.translate(W / 2, 1180); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
      S.texte('RÉGLER ✓', 0, 0, { taille: 130, coul: OR, contour: NOIR, contourL: 12, max: 960 }); g.restore();
      S.texte('désirer ce qui est à ta portée', W / 2, 1300, { taille: 60, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 }); }
  }

  return { chrono, loupe, tonneau, phone, pierres, cite, ailes, erreur, reglage };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono') { if (p.run) for (let x = p.a; x < p.b - .1; x += 1) L.push([x, 'tic', .5]); else L.push([p.a + .1, 'tic', .4]); }
  if (p.type === 'loupe') { (p.cercles || []).forEach(([r]) => L.push([tps(r), 'stylo', .5])); (p.lignes || []).forEach(([r]) => L.push([tps(r), 'pop', .35])); }
  if (p.type === 'tonneau') { L.push([p.a, 'souffle', .4]); if (p.a2) L.push([tps(p.a2), 'tampon', .7]); }
  if (p.type === 'phone') { L.push([p.a, 'pop', .3]); (p.coups || []).forEach(r => L.push([tps(r), 'whoosh', .45])); }
  if (p.type === 'pierres') { L.push([p.a, 'frotte', .3]); if (p.couronne) L.push([tps(p.couronne), 'pop', .55]); }
  if (p.type === 'cite') { L.push([p.a, 'papier', .4]); const d = p.duree || 1.6, n = p.q.length; for (let k = 0; k < n; k += 6) L.push([tps(p.aq || p.a) + d * k / n, 'tic', .2]); }
  if (p.type === 'ailes') L.push([p.a, 'whoosh', .35]);
  if (p.type === 'erreur') { L.push([p.a + .2, 'stylo', .5], [tps(p.barre), 'lame', .6], [tps(p.barre) + .35, 'tampon', 1]); }
  if (p.type === 'reglage') { L.push([tps(p.sup), 'clic', .5], [tps(p.sup) + .3, 'buzz', .35], [tps(p.reg), 'clic', .5], [tps(p.reg) + .4, 'valide', .6]); }
};
