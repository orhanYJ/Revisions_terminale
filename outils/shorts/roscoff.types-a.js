// Plans propres au short Roscoff (« Il a arrêté de manger »), dans le style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Le ver et ses micro-algues sont les seuls éléments verts du short.
window.SANS_ST_A = ['bacsvt', 'compte', 'vrai'];
window.PROPRES_A = ['vrai', 'ver', 'avale', 'compte', 'compteur', 'photo', 'plage', 'soleil', 'echange', 'genome', 'bacsvt'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const VERT = '#5a9a3c', ALGUE = '#9fd36a', SABLE = '#6b5a40', MER = 'rgba(90,120,140,.45)';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };
  const melange = (a, b, k) => { const h = s => [1, 3, 5].map(i => parseInt(s.slice(i, i + 2), 16)); const [x, y] = [h(a), h(b)]; return `rgb(${x.map((v, i) => Math.round(lerp(v, y[i], k))).join(',')})`; };

  // ---------- le ver : corps plat allongé, avant arrondi, arrière effilé ; tête vers la droite
  // o.vert (0 translucide → 1 vert), o.algues (nombre de points verts), o.alpha
  function ver(cx, cy, L, rot, t, o = {}) {
    const n = 26, pts = [], v = o.vert || 0;
    for (let i = 0; i <= n; i++) {
      const u = i / n, x = lerp(L / 2, -L / 2, u);
      const w = L * .085 * (u < .2 ? Math.sqrt(u / .2) * .85 + .15 : Math.pow((1 - u) / .8, .8));
      const y = Math.sin(u * 5 - t * 4) * L * .03 * u - Math.sin(u * Math.PI) * L * .05;
      pts.push([x, y, Math.max(2, w)]);
    }
    g.save(); g.translate(cx, cy); g.rotate(rot); g.globalAlpha = o.alpha ?? 1;
    g.beginPath(); pts.forEach(([x, y, w], i) => i ? g.lineTo(x, y - w) : g.moveTo(x, y - w));
    for (let i = n; i >= 0; i--) { const [x, y, w] = pts[i]; g.lineTo(x, y + w); } g.closePath();
    g.fillStyle = v > 0 ? melange('#2a2a24', VERT, v) : 'rgba(239,230,210,.08)'; g.fill();
    g.strokeStyle = v > .5 ? '#cfe8a8' : CREME; g.lineWidth = Math.max(3, L * .012); g.stroke();
    // algues sous la peau
    const na = Math.floor(o.algues || 0);
    g.save(); g.clip();
    for (let i = 0; i < na; i++) { const u = .04 + rnd(i * 12.9898 + .31) * .9, k = Math.floor(u * n), [x, y, w] = pts[k];
      const yy = y + (rnd(i * 78.233 + 1.7) - .5) * 1.7 * w; rond(x + (rnd(i * 37.719 + 4.1) - .5) * L / n * 1.4, yy, Math.max(2.5, L * .009), ALGUE); }
    g.restore();
    // statocyste (organe d'équilibre, à l'avant)
    rond(L / 2 - L * .06, pts[1][1], Math.max(3, L * .012), v > .5 ? '#e8f4d0' : OR);
    g.restore();
  }
  function regle(x, y, w) {
    g.save(); g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath(); g.moveTo(x, y); g.lineTo(x + w, y); g.stroke();
    for (let i = 0; i <= 5; i++) { g.beginPath(); g.moveTo(x + i * w / 5, y); g.lineTo(x + i * w / 5, y - (i % 5 ? 16 : 28)); g.stroke(); }
    S.texte('quelques millimètres', x + w / 2, y + 45, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore();
  }

  // p.mode : 'oeuf' | 'jeune' | 'algues' (repère p.mult : elles se multiplient) | 'vert' ; p.regle
  function verPlan(p, t) {
    const lt = t - p.a;
    if (p.mode === 'oeuf') {
      const kc = pr(lt, .2, .5), ks = eo(pr(lt, .5, .8));
      g.save(); g.translate(540, 860);
      [[-1, -.3], [1, .3]].forEach(([s, r]) => { g.save(); g.translate(s * 60 * kc, 20 * kc); g.rotate(r * kc); g.beginPath(); g.ellipse(0, 0, 200, 150, 0, s < 0 ? Math.PI / 2 : -Math.PI / 2, s < 0 ? Math.PI * 1.5 : Math.PI / 2);
        g.fillStyle = 'rgba(239,230,210,.1)'; g.fill(); g.strokeStyle = CREME; g.lineWidth = 6; g.stroke(); g.restore(); });
      g.restore();
      ver(lerp(540, 600, ks), 860, lerp(150, 380, ks), -.05, t);
      S.texte('translucide', 540, 1120, { taille: 50, police: 'Spectral', it: true, poids: 400, coul: CREME });
    } else {
      const v = p.mode === 'vert' ? 1 : p.mode === 'algues' ? lerp(0, .35, pr(t, tps(p.mult || p.a), 1.2)) : 0;
      let na = p.mode === 'vert' ? 220 : 0;
      if (p.mode === 'algues') { na = lerp(0, 14, eo(pr(lt, .1, .8))); if (p.mult) na += lerp(0, 90, eo(pr(t, tps(p.mult), 1.4))); }
      const z = 1 + lt * .02;
      ver(540, 860, 760 * z, -.06, t, { vert: v, algues: na });
      if (p.regle) regle(390, 1120, 300);
      if (p.mode === 'algues') { const k = pr(lt, .1, .5); g.save(); g.globalAlpha = k; g.strokeStyle = ALGUE; g.lineWidth = 4; g.beginPath(); g.moveTo(600, 840); g.lineTo(760, 620); g.stroke();
        S.texte('MICRO-ALGUES', 800, 580, { taille: 46, coul: ALGUE, esp: 3 }); g.restore(); }
    }
    if (p.t) deux(p.t, 1420, 104);
  }

  // le jeune avale des micro-algues (une seule fois)
  function avale(p, t) {
    const lt = t - p.a;
    ver(560, 900, 520, -.05, t, { algues: Math.floor(cl((lt - .7) / .8) * 10) });
    for (let i = 0; i < 10; i++) { const k = eo(pr(lt, .1 + i * .07, .8)), a = rnd(i * 5) * 6.28, d = lerp(420, 0, k);
      if (k < 1) rond(560 + Math.cos(a) * d, 900 + Math.sin(a) * d * .8, 13, ALGUE, '#e8f4d0', 3); }
    O.petitTitre('UNE SEULE FOIS DANS TA VIE', 480);
    if (p.t) deux(p.t, 1420, 104);
  }

  // sans algues : 20 jours au plus
  function compte(p, t) {
    const lt = t - p.a, j = Math.min(20, 1 + Math.floor(lt / .055));
    ver(540, 760, 460, -.05, t, { alpha: lerp(1, .25, cl(j / 20)) });
    const k = back(pr(t, p.a, .3)); g.save(); g.translate(W / 2, 1180); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
    S.texte(String(j), 0, 0, { taille: 260, police: 'Spectral', poids: 600, coul: j >= 20 ? ROUGE : CREME, contour: NOIR, contourL: 14 }); g.restore();
    S.texte('JOURS, AU PLUS', W / 2, 1380, { taille: 70, coul: OR, esp: 6 });
    S.texte('sans algues, le jeune ver ne survit pas', W / 2, 1480, { taille: 46, police: 'Spectral', it: true, poids: 400, coul: CREME });
  }

  // compteur d'algues jusqu'à environ 40 000, le ver verdit
  function compteur(p, t) {
    const k = eo(pr(t, p.a + .1, 1.3)), n = Math.round(lerp(10, 40000, k * k) / 10) * 10;
    ver(540, 760, 820, -.06, t, { vert: k * .9, algues: 30 + k * 190 });
    S.texte('environ', W / 2, 1010, { taille: 50, police: 'Spectral', it: true, poids: 400, coul: CREME });
    S.texte(String(n).replace(/\B(?=(\d{3})+$)/g, ' '), W / 2, 1130, { taille: 170, police: 'Spectral', poids: 600, coul: ALGUE, contour: NOIR, contourL: 12 });
    S.texte('MICRO-ALGUES SOUS TA PEAU', W / 2, 1280, { taille: 50, coul: CREME, esp: 4 });
  }

  // soleil ; p.ver : le ver vert dessous
  function soleilDessin(x, y, r, t) {
    g.save(); g.shadowColor = OR; g.shadowBlur = 60; rond(x, y, r, '#f0d27a'); g.restore();
    g.strokeStyle = OR; g.lineWidth = 8; for (let i = 0; i < 12; i++) { const a = i / 12 * 6.28 + t * .3; g.beginPath(); g.moveTo(x + Math.cos(a) * (r + 25), y + Math.sin(a) * (r + 25)); g.lineTo(x + Math.cos(a) * (r + 70), y + Math.sin(a) * (r + 70)); g.stroke(); }
  }
  function soleil(p, t) {
    soleilDessin(540, 520, 110, t);
    ver(540, 1060, 760, -.05, t, { vert: 1, algues: 200 });
    if (p.t) deux(p.t, 1420, 110);
  }

  // photosynthèse : la lumière tombe sur les algues ; p.partage : les nutriments passent au ver
  function photo(p, t) {
    const lt = t - p.a;
    soleilDessin(220, 440, 80, t);
    for (let i = 0; i < 5; i++) { const k = ((lt * 1.2 + i / 5) % 1); g.save(); g.globalAlpha = (1 - k) * .8; g.strokeStyle = '#f0d27a'; g.lineWidth = 6; g.setLineDash([20, 16]);
      g.beginPath(); g.moveTo(300 + i * 30, 520 + i * 10); g.lineTo(lerp(300 + i * 30, 470 + i * 90, k), lerp(520 + i * 10, 900, k)); g.stroke(); g.restore(); }
    // gros plan : une portion du ver avec ses algues
    g.save(); g.fillStyle = '#2f4a26'; g.strokeStyle = '#cfe8a8'; g.lineWidth = 6; g.beginPath(); g.roundRect(150, 820, 780, 380, 120); g.fill(); g.stroke(); g.restore();
    S.texte('TON CORPS', 260, 860, { taille: 30, coul: '#cfe8a8', esp: 4 });
    const AL = [[300, 960], [420, 1080], [520, 940], [640, 1060], [740, 950], [830, 1090], [380, 1150], [700, 1160]];
    AL.forEach(([x, y], i) => { g.save(); g.shadowColor = ALGUE; g.shadowBlur = 20 + 10 * Math.sin(t * 5 + i); rond(x, y, 30, ALGUE, '#e8f4d0', 3); g.restore(); });
    if (p.partage) {
      const kp = pr(t, tps(p.partage), .3);
      AL.forEach(([x, y], i) => { for (let j = 0; j < 2; j++) { const k = ((lt * .9 + j / 2 + i * .13) % 1); g.save(); g.globalAlpha = kp * (1 - k);
        const a = rnd(i * 7 + j) * 6.28; rond(x + Math.cos(a) * k * 110, y + Math.sin(a) * k * 70, 9, OR); g.restore(); } });
      g.save(); g.globalAlpha = kp; S.texte('nutriments', 820, 790, { taille: 46, police: 'Spectral', it: true, poids: 400, coul: OR }); g.restore();
    }
    O.petitTitre('PHOTOSYNTHÈSE', 640, ALGUE);
    if (p.t) deux(p.t, 1420, 104);
  }

  // la plage en coupe : p.maree 'basse' | 'haute' ; p.monte (les vers remontent) ; p.foule (taches vertes)
  function plage(p, t) {
    const lt = t - p.a, SURF = 1000;
    if (p.maree === 'basse') soleilDessin(860, 420, 70, t);
    // sable
    g.fillStyle = SABLE; g.fillRect(0, SURF, W, 360);
    for (let i = 0; i < 220; i++) { g.fillStyle = `rgba(239,230,210,${.08 + rnd(i) * .12})`; g.fillRect(rnd(i * 3.1) * W, SURF + 10 + rnd(i * 7.7) * 340, 4, 4); }
    g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(0, SURF); g.lineTo(W, SURF); g.stroke();
    // mer
    const kh = p.maree === 'haute' ? eo(pr(lt, 0, .9)) : 0;
    const xm = p.maree === 'haute' ? lerp(820, -40, kh) : 880 + Math.sin(t) * 10, hm = p.maree === 'haute' ? lerp(60, 420, kh) : 60;
    g.fillStyle = MER; g.beginPath(); g.moveTo(xm, SURF);
    for (let x = xm; x <= W; x += 10) g.lineTo(x, SURF - hm + Math.sin(x * .03 + t * 3) * 10); g.lineTo(W, SURF); g.closePath(); g.fill();
    g.strokeStyle = 'rgba(239,230,210,.6)'; g.lineWidth = 4; g.beginPath(); for (let x = xm; x <= W; x += 10) g.lineTo(x, SURF - hm + Math.sin(x * .03 + t * 3) * 10); g.stroke();
    S.texte(p.maree === 'haute' ? 'MARÉE HAUTE' : 'MARÉE BASSE', 280, 560, { taille: 46, coul: OR, esp: 5 });
    // les vers
    const n = p.foule ? 70 : 14;
    for (let i = 0; i < n; i++) {
      const groupe = Math.floor(rnd(i * 2.3) * 4), x0 = 110 + groupe * 200 + rnd(i * 5.1) * 150;
      let y;
      if (p.maree === 'haute') y = lerp(SURF - 4, SURF + 90 + rnd(i) * 200, eo(pr(lt, .3 + rnd(i) * .3, .8)));
      else if (p.monte) y = lerp(SURF + 90 + rnd(i) * 200, SURF - 4, eo(pr(lt, .1 + rnd(i) * .4, .9)));
      else y = p.foule ? SURF - 4 - rnd(i * 9) * 6 : SURF + 90 + rnd(i) * 200;
      if (p.foule && i >= 14) { const k = pr(lt, .1 + rnd(i) * .6, .4); if (k <= 0) continue; }
      if (x0 > (p.maree === 'haute' ? 2000 : xm - 20)) continue;
      ver(x0, y, 60, -.1 + rnd(i) * .2 + (y < SURF ? 0 : -1.3), t + i, { vert: 1, algues: 0 });
    }
    if (p.foule) for (let k = 0; k < 4; k++) { const kk = pr(lt, .4 + k * .1, .5); g.save(); g.globalAlpha = kk * .35; g.fillStyle = VERT; g.beginPath(); g.ellipse(185 + k * 200, SURF - 6, 110, 18, 0, 0, 7); g.fill(); g.restore(); }
    if (p.t) deux(p.t, 1500, 100);
  }

  // ce que gagne chacun : p.toi, p.alg (repères) ; p.lien : symbiose
  function echange(p, t) {
    const kt = p.toi ? pr(t, tps(p.toi), .35) : 1, ka = p.alg ? pr(t, tps(p.alg), .35) : 1;
    rond(290, 820, 190, '#1b1712', CREME, 6); ver(290, 820, 280, -.1, t, { vert: 1, algues: 60 });
    S.texte('TOI', 290, 1060, { taille: 60, coul: CREME, esp: 6 });
    rond(790, 820, 190, '#1b1712', ALGUE, 6);
    for (let i = 0; i < 9; i++) { const a = i / 9 * 6.28 + t * .4, r = i % 3 ? 90 : 30; rond(790 + Math.cos(a) * r, 820 + Math.sin(a) * r, 26, ALGUE, '#e8f4d0', 3); }
    S.texte('LES ALGUES', 790, 1060, { taille: 56, coul: ALGUE, esp: 4 });
    // flèches : la photosynthèse vers toi, l'abri vers les algues
    if (kt > 0) { S.d.fleche(660, 700, 420, 700, eo(kt), { trait: OR, ep: 10 }); g.save(); g.globalAlpha = cl(kt * 2); S.texte('la photosynthèse', 540, 640, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: OR }); g.restore(); }
    if (ka > 0) { S.d.fleche(420, 940, 660, 940, eo(ka), { trait: CREME, ep: 10 }); g.save(); g.globalAlpha = cl(ka * 2); S.texte('un abri stable', 540, 1000, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME }); g.restore(); }
    if (p.lien) { const k = eo(pr(t, p.a + .2, .7)); g.save(); g.strokeStyle = OR; g.lineWidth = 8; g.setLineDash([26, 16]); g.lineDashOffset = -t * 40;
      g.beginPath(); g.ellipse(540, 840, 500, 300, 0, -Math.PI / 2, -Math.PI / 2 + 6.3 * k); g.stroke(); g.restore(); }
    if (p.t) deux(p.t, 1400, 104);
  }

  function helice(x0, x1, y, amp) {
    g.save(); g.lineCap = 'round';
    for (let i = 0; i <= 14; i++) { const u = i / 14, x = lerp(x0, x1, u), a = Math.sin(u * 9) * amp; g.strokeStyle = 'rgba(239,230,210,.45)'; g.lineWidth = 5; g.beginPath(); g.moveTo(x, y + a); g.lineTo(x, y - a); g.stroke(); }
    [[1, CREME], [-1, OR]].forEach(([s, c]) => { g.strokeStyle = c; g.lineWidth = 8; g.beginPath(); for (let i = 0; i <= 60; i++) { const u = i / 60, yy = y + s * Math.sin(u * 9) * amp; i ? g.lineTo(lerp(x0, x1, u), yy) : g.moveTo(lerp(x0, x1, u), yy); } g.stroke(); });
    g.restore();
  }
  // même génome, autre phénotype ; p.asso : « + les algues »
  function genome(p, t) {
    [[290, 'JEUNE', 0], [790, 'ADULTE', 1]].forEach(([x, lab, v]) => {
      ver(x, 560, 400, -.05, t, { vert: v, algues: v ? 120 : 0 });
      S.texte(lab, x, 700, { taille: 48, coul: v ? ALGUE : CREME, esp: 6 });
      helice(x - 190, x + 190, 860, 34);
    });
    pop(pr(t, p.a + .2, .3), W / 2, 860, () => S.texte('=', 0, 0, { taille: 150, coul: OR, contour: NOIR, contourL: 10 }));
    S.texte('MÊME GÉNOME', W / 2, 980, { taille: 46, coul: OR, esp: 6 });
    if (p.asso) { const k = pr(t, p.a + .1, .3); pop(k, 790, 1080, () => S.texte('+ LES ALGUES', 0, 0, { taille: 64, coul: ALGUE, contour: NOIR, contourL: 8 }));
      O.tampon('ASSOCIATION', W / 2, 1290, pr(t, p.a + .5, .3), -.08, 90, OR); }
    if (p.t) deux(p.t, 1420, 100);
  }

  // photo en couleur (le vert des vers compte) : p.img, p.t, p.sous
  function vrai(p, t, l) {
    const k = eo(pr(t, p.a, .35)), im = S.img(p.img);
    g.save(); g.translate(W / 2 + lerp(300, 0, k), 760); g.rotate(lerp(.12, -.03, k));
    g.shadowColor = 'rgba(0,0,0,.7)'; g.shadowBlur = 50; g.shadowOffsetY = 20; g.fillStyle = CREME; g.fillRect(-334, -434, 668, 868); g.shadowColor = 'transparent';
    if (im) S.cover(im, -320, -420, 640, 840, 1.25 + l * .04, .45, .45);
    g.restore();
    O.multi([[p.t, ALGUE]], 1330, 150);
    if (p.sous) S.texte(p.sous, W / 2, 1460, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME });
  }

  // copie de bac de SVT
  function bacsvt(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 900, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-400, -480, 800, 960); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
    S.texte('SCIENCES DE LA VIE ET DE LA TERRE', 0, -315, { taille: 32, coul: GRIS, esp: 4, poids: 600, max: 700 });
    g.fillStyle = NOIR; g.fillRect(-320, -260, 640, 3);
    S.texte('Sujet type', -320, -195, { taille: 40, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400 });
    const L = p.sujet; L.forEach((s, i) => S.texte(s, 0, -110 + i * 74, { taille: 60, police: 'Spectral', poids: 600, coul: NOIR, max: 700 }));
    const yb = -110 + L.length * 74;
    for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-320, yb + 30 + i * 50, 640 - (i === 3 ? 260 : 0), 6); }
    const kc = pr(t, p.a + .35, .5), cy = -110 + (L.length - 1) * 37; g.strokeStyle = ROUGE; g.lineWidth = 9;
    g.beginPath(); g.ellipse(0, cy, 380, 60 + L.length * 40, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['SUJET TYPE ', CREME], ['BAC', ROUGE]], 1560, 110);
  }

  return { vrai, ver: verPlan, avale, compte, compteur, photo, plage, soleil, echange, genome, bacsvt };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'ver' && p.mode === 'oeuf') L.push([p.a + .2, 'frappe', .5], [p.a + .5, 'pop', .5]);
  if (p.type === 'ver' && p.mode === 'algues') { L.push([p.a + .1, 'aspire', .4]); if (p.mult) L.push([tps(p.mult), 'montee', .4]); }
  if (p.type === 'ver' && p.mode === 'vert') L.push([p.a, 'souffle', .3]);
  if (p.type === 'avale') for (let i = 0; i < 10; i += 3) L.push([p.a + .5 + i * .07, 'blip', .3]);
  if (p.type === 'compte') for (let x = p.a; x < Math.min(p.b, p.a + 1.8) - .05; x += .18) L.push([x, 'tic', .4]);
  if (p.type === 'compteur') L.push([p.a + .1, 'montee', .5]);
  if (p.type === 'photo') { L.push([p.a, 'souffle', .35]); if (p.partage) L.push([tps(p.partage), 'blip', .4]); }
  if (p.type === 'plage') L.push([p.a, p.maree === 'haute' ? 'whoosh' : 'frotte', .4]);
  if (p.type === 'soleil') L.push([p.a, 'souffle', .4]);
  if (p.type === 'echange') { if (p.toi) L.push([tps(p.toi), 'pop', .5]); if (p.alg) L.push([tps(p.alg), 'pop', .5]); if (p.lien) L.push([p.a + .2, 'valide', .5]); }
  if (p.type === 'genome') { L.push([p.a + .2, 'bip', .4]); if (p.asso) L.push([p.a + .55, 'tampon', .8]); }
  if (p.type === 'bacsvt') L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .6]);
};
