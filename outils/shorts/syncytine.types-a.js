// Plans propres au short Syncytine (« Sans un virus, tu ne serais pas né »), dans le style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Le gène venu du virus est toujours dessiné en rouge.
window.SANS_ST_A = ['nom', 'compare', 'genome', 'bacsvt'];
window.PROPRES_A = ['virus', 'infection', 'adn', 'germinale', 'generations', 'proteine', 'fusion', 'chromosome', 'nom',
  'embryon', 'lien', 'souris', 'compare', 'horizontal', 'genome', 'bacsvt'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const SOMBRE = '#1b1712';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const sous = (s, y, taille = 60) => S.texte(s, W / 2, y, { taille, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 8, max: 960 });
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };

  // ---------- dessins
  // particule de rétrovirus : enveloppe, spicules (protéines ENV), capside, ARN rouge
  function particule(x, y, r, rot, t) {
    g.save(); g.translate(x, y); g.rotate(rot);
    g.strokeStyle = OR; g.lineWidth = r * .05; g.lineCap = 'round';
    for (let i = 0; i < 16; i++) { const a = i / 16 * 6.283; g.beginPath(); g.moveTo(Math.cos(a) * r, Math.sin(a) * r); g.lineTo(Math.cos(a) * r * 1.22, Math.sin(a) * r * 1.22); g.stroke();
      rond(Math.cos(a) * r * 1.27, Math.sin(a) * r * 1.27, r * .08, OR); }
    rond(0, 0, r, SOMBRE, CREME, r * .045);
    g.beginPath(); for (let i = 0; i <= 6; i++) { const a = i / 6 * 6.283 + .3; i ? g.lineTo(Math.cos(a) * r * .58, Math.sin(a) * r * .58) : g.moveTo(Math.cos(a) * r * .58, Math.sin(a) * r * .58); }
    g.strokeStyle = CREME; g.lineWidth = r * .035; g.stroke();
    g.strokeStyle = ROUGE; g.lineWidth = r * .05; g.beginPath();
    for (let i = 0; i <= 30; i++) { const u = i / 30, xx = lerp(-r * .38, r * .38, u), yy = Math.sin(u * 14 + t * 3) * r * .14; i ? g.lineTo(xx, yy) : g.moveTo(xx, yy); }
    g.stroke(); g.restore();
  }
  // brin d'ADN en double hélice horizontal ; rouge : [début, fin] en fraction de largeur (le gène viral)
  function helice(x0, x1, y, amp, t, rouge, alpha = 1) {
    g.save(); g.globalAlpha = alpha; g.lineCap = 'round';
    const n = Math.floor((x1 - x0) / 30);
    for (let i = 0; i <= n; i++) { const u = i / n, x = lerp(x0, x1, u), ph = u * 12 + t * 2, a = Math.sin(ph) * amp, b = -a;
      const enR = rouge && u >= rouge[0] && u <= rouge[1];
      g.strokeStyle = enR ? ROUGE : 'rgba(239,230,210,.45)'; g.lineWidth = 6; g.beginPath(); g.moveTo(x, y + a); g.lineTo(x, y + b); g.stroke(); }
    [[1, CREME], [-1, OR]].forEach(([s, c]) => { g.strokeStyle = c; g.lineWidth = 10; g.beginPath();
      for (let i = 0; i <= 120; i++) { const u = i / 120, x = lerp(x0, x1, u), yy = y + s * Math.sin(u * 12 + t * 2) * amp; i ? g.lineTo(x, yy) : g.moveTo(x, yy); } g.stroke(); });
    if (rouge) { g.strokeStyle = ROUGE; g.lineWidth = 14; g.shadowColor = ROUGE; g.shadowBlur = 30;
      [1, -1].forEach(s => { g.beginPath(); for (let i = 0; i <= 40; i++) { const u = lerp(rouge[0], rouge[1], i / 40), x = lerp(x0, x1, u), yy = y + s * Math.sin(u * 12 + t * 2) * amp; i ? g.lineTo(x, yy) : g.moveTo(x, yy); } g.stroke(); }); }
    g.restore();
  }
  // petit personnage (tête + buste) avec, sur la poitrine, le point rouge du gène viral
  function bonhomme(x, y, s, gene = true) {
    g.save(); g.translate(x, y); g.scale(s, s);
    rond(0, -46, 26, SOMBRE, CREME, 5);
    g.beginPath(); g.ellipse(0, 22, 40, 34, 0, Math.PI, 0); g.closePath(); g.fillStyle = SOMBRE; g.fill(); g.strokeStyle = CREME; g.lineWidth = 5; g.stroke();
    if (gene) { g.shadowColor = ROUGE; g.shadowBlur = 16; rond(0, 4, 9, ROUGE); }
    g.restore();
  }
  // contour de l'union de plusieurs disques [x, y, r] (le contour disparaît là où ils se touchent : la fusion)
  function union(disques, fond, trait, ep = 8) {
    g.fillStyle = trait; disques.forEach(([x, y, r]) => { g.beginPath(); g.arc(x, y, r + ep, 0, 7); g.fill(); });
    g.fillStyle = fond; disques.forEach(([x, y, r]) => { g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); });
  }
  // embryon recroquevillé
  function foetus(x, y, s, t) {
    g.save(); g.translate(x, y); g.scale(s, s);
    g.fillStyle = '#3a2f25'; g.strokeStyle = OR; g.lineWidth = 8;
    g.beginPath(); g.arc(-10, -70, 70, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(40, -20); g.bezierCurveTo(140, 40, 90, 170, -10, 160); g.bezierCurveTo(-90, 150, -110, 60, -60, 0); g.closePath(); g.fill(); g.stroke();
    const b = 1 + .25 * Math.max(0, Math.sin(t * 8)); rond(10, 50, 12 * b, ROUGE);
    g.restore();
  }

  // ---------- plans
  function virus(p, t, l) {
    const k = back(pr(t, p.a, .35)), r = 230 * k;
    g.save(); g.globalAlpha = .25; rond(W / 2, 820, 420 + Math.sin(t * 2) * 20, 'rgba(200,55,45,.25)'); g.restore();
    if (r > 0) particule(W / 2, 820, r, l * .25, t);
    if (p.t) deux(p.t, 1380, p.taille || 110);
  }

  // un virus vient se coller à une cellule, son ADN rouge file vers le noyau
  function infection(p, t, l) {
    const cx = 620, cy = 1000, R = 360, k = eo(pr(t, p.a, .7)), ki = pr(t, p.a + .7, .6);
    rond(cx, cy, R, '#211b15', CREME, 8);
    rond(cx + 40, cy + 30, 130, '#2c241b', OR, 6);
    helice(cx - 60, cx + 140, cy + 30, 22, t, ki >= 1 ? [.35, .65] : null, .9);
    const ang = -2.4, vx = lerp(120, cx + Math.cos(ang) * (R + 85), k), vy = lerp(300, cy + Math.sin(ang) * (R + 85), k);
    particule(vx, vy, 75, l * .4, t);
    if (ki > 0 && ki < 1) { g.strokeStyle = ROUGE; g.lineWidth = 10; g.shadowColor = ROUGE; g.shadowBlur = 20;
      const x = lerp(vx, cx + 40, ki), y = lerp(vy, cy + 30, ki); g.beginPath(); g.moveTo(x - 40, y); for (let i = 0; i <= 8; i++) g.lineTo(x - 40 + i * 10, y + Math.sin(i + t * 9) * 12); g.stroke(); g.shadowBlur = 0; }
    S.texte('UNE CELLULE DU SINGE', cx, cy + R + 60, { taille: 40, coul: GRIS, esp: 6, poids: 600 });
    if (p.t) deux(p.t, 1560, 96);
  }

  // l'ADN ; p.insere : un brin rouge descend et s'insère au milieu ; sinon p.rouge : le gène viral est déjà là
  function adn(p, t, l) {
    const y = 860, ki = eo(pr(t, p.a + .15, .6));
    if (p.insere) {
      helice(60, 1020, y, 70, t, ki >= 1 ? [.42, .58] : null);
      if (ki < 1) { g.save(); g.translate(0, lerp(-520, 0, ki)); helice(60 + 960 * .42, 60 + 960 * .58, y, 70, t, [0, 1]); g.restore(); }
      else pop(pr(t, p.a + .75, .3), W / 2, 680, () => S.texte('GÈNE DU VIRUS', 0, 0, { taille: 48, coul: ROUGE, esp: 6, contour: NOIR, contourL: 8 }));
    } else {
      helice(60, 1020, y, 70, t + l * .5, [.42, .58]);
      pop(pr(t, p.a + .2, .3), W / 2, 680, () => S.texte('GÈNE DU VIRUS', 0, 0, { taille: 48, coul: ROUGE, esp: 6, contour: NOIR, contourL: 8 }));
    }
    O.petitTitre(p.sur || 'L’ADN DE LA CELLULE', 560);
    if (p.t) deux(p.t, 1340, 104);
  }

  // une cellule germinale qui donnera un ovule… ou un spermatozoïde, chacun avec le gène rouge
  function germinale(p, t, l) {
    const k = back(pr(t, p.a, .3));
    pop(pr(t, p.a, .3), W / 2, 640, () => { rond(0, 0, 150, '#211b15', CREME, 8); rond(0, 0, 55, '#2c241b', OR, 5); g.shadowColor = ROUGE; g.shadowBlur = 20; rond(0, 0, 14, ROUGE); });
    S.texte('CELLULE GERMINALE', W / 2, 860, { taille: 46, coul: OR, esp: 6, poids: 600 });
    const ko = pr(t, tps(p.ovule), .35), ks = pr(t, tps(p.spz), .35);
    if (ko > 0) { S.d.fleche(470, 900, 300, 1040, eo(ko), { trait: CREME, ep: 8 });
      pop(ko, 270, 1220, () => { rond(0, 0, 130, '#e9dfc8', OR, 8); rond(0, 0, 40, '#c9b994'); rond(0, 0, 13, ROUGE); });
      S.texte('OVULE', 270, 1420, { taille: 56, coul: CREME }); }
    if (ks > 0) { S.d.fleche(610, 900, 780, 1040, eo(ks), { trait: CREME, ep: 8 });
      pop(ks, 800, 1200, () => { g.strokeStyle = CREME; g.lineWidth = 7; g.beginPath(); for (let i = 0; i <= 30; i++) g.lineTo(-40 - i * 7, Math.sin(i * .6 + t * 14) * 14); g.stroke();
        g.beginPath(); g.ellipse(0, 0, 50, 34, 0, 0, 7); g.fillStyle = '#e9dfc8'; g.fill(); rond(5, 0, 11, ROUGE); });
      S.texte('SPERMATOZOÏDE', 760, 1420, { taille: 50, coul: CREME }); }
  }

  // arbre de générations : 1, 2, 4, 8 descendants, tous avec le gène rouge
  function generations(p, t, l) {
    const marques = p.marques.map(tps);
    const n = marques.filter(x => t >= x).length;
    O.petitTitre('LE GÈNE DU VIRUS SE TRANSMET', 420, ROUGE);
    for (let gen = 0; gen < 4; gen++) {
      const km = gen === 0 ? 1 : pr(t, marques[gen - 1], .3); if (km <= 0) continue;
      const nb = 2 ** gen, y = 600 + gen * 220, w = 900 / nb;
      for (let i = 0; i < nb; i++) {
        const x = 90 + w * (i + .5);
        if (gen) { const xp = 90 + (900 / nb * 2) * (Math.floor(i / 2) + .5); g.save(); g.globalAlpha = km; g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 4;
          g.beginPath(); g.moveTo(xp, y - 160); g.lineTo(x, y - 90); g.stroke(); g.restore(); }
        pop(km, x, y, () => bonhomme(0, 0, gen === 3 ? .8 : 1.1));
      }
    }
    const gen = Math.min(4, n + 1);
    S.texte(gen < 4 ? `GÉNÉRATION ${gen}` : 'GÉNÉRATION APRÈS GÉNÉRATION', W / 2, 1420, { taille: gen < 4 ? 90 : 70, coul: OR, contour: NOIR, contourL: 10, max: 960 });
  }

  // le gène rouge fabrique une protéine (spicule en Y)
  function proteine(p, t, l) {
    helice(160, 920, 620, 50, t, [.4, .6]);
    const k = pr(t, p.a + .2, .9);
    for (let i = 0; i < 5; i++) { const ki = cl(k * 5 - i), x = lerp(540, 220 + i * 160, eo(ki)), y = lerp(660, 1040, eo(ki));
      if (ki <= 0) continue;
      g.save(); g.translate(x, y); g.scale(ki * 1.3, ki * 1.3); g.strokeStyle = OR; g.lineWidth = 10; g.lineCap = 'round';
      g.beginPath(); g.moveTo(0, 60); g.lineTo(0, 0); g.lineTo(-34, -46); g.moveTo(0, 0); g.lineTo(34, -46); g.stroke(); rond(-34, -50, 11, OR); rond(34, -50, 11, OR); g.restore(); }
    if (p.t) deux(p.t, 1360, 110);
  }

  // fusion de membranes : mode 'virus' (le virus entre dans la cellule) ou 'cellules' (des cellules se soudent)
  function fusion(p, t, l) {
    const k = eo(pr(t, p.a + .05, .75));
    if (p.mode === 'virus') {
      const R = 330, cx = 680, cy = 900, r = lerp(110, 60, k), vx = lerp(170, cx - R + 40, k);
      union([[cx, cy, R], [vx, cy, r]], '#211b15', CREME, 9);
      rond(cx + 60, cy, 110, '#2c241b', OR, 6);
      g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); for (let i = 0; i <= 12; i++) g.lineTo(vx - 40 + i * 7, cy + Math.sin(i + t * 8) * 12); g.stroke();
      if (k < .6) for (let i = 0; i < 10; i++) { const a = i / 10 * 6.283; g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.moveTo(vx + Math.cos(a) * r, cy + Math.sin(a) * r); g.lineTo(vx + Math.cos(a) * r * 1.25, cy + Math.sin(a) * r * 1.25); g.stroke(); }
      S.texte('VIRUS', 170, cy - 190, { taille: 44, coul: GRIS, esp: 6 }); S.texte('CELLULE', cx, cy + R + 60, { taille: 44, coul: GRIS, esp: 6 });
    } else {
      const xs = [210, 430, 650, 870], d = xs.map((x, i) => [lerp(x + (i - 1.5) * 50, x, k), 880, lerp(105, 135, k)]);
      union(d, '#211b15', CREME, 9);
      d.forEach(([x, y]) => rond(x, y, 34, '#3a2f25', OR, 5));
      if (k > .95) { const ks = pr(t, p.a + .85, .3); g.save(); g.globalAlpha = ks; S.texte('UNE SEULE COUCHE GÉANTE', W / 2, 1100, { taille: 54, coul: OR, esp: 4, contour: NOIR, contourL: 8, max: 960 }); g.restore(); }
    }
    if (p.t) deux(p.t, 1380, 104);
  }

  // chromosome 7, une bande rouge sur un bras
  function chromosome(p, t, l) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    [-1, 1].forEach(s => { g.save(); g.rotate(s * .16);
      g.fillStyle = '#2c241b'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.roundRect(-55, -390, 110, 780, 55); g.fill(); g.stroke();
      [-300, -230, -120, -40, 70, 150, 250, 320].forEach((y, i) => { g.fillStyle = i % 2 ? 'rgba(239,230,210,.25)' : 'rgba(217,180,90,.35)'; g.fillRect(-50, y, 100, 26); });
      g.fillStyle = ROUGE; g.shadowColor = ROUGE; g.shadowBlur = 30 + 20 * Math.sin(t * 6); g.fillRect(-50, 190, 100, 34); g.restore(); });
    g.restore();
    const kl = eo(pr(t, p.a + .35, .3)); g.save(); g.globalAlpha = kl;
    g.strokeStyle = ROUGE; g.lineWidth = 5; g.beginPath(); g.moveTo(640, 1065); g.lineTo(820, 1160); g.stroke();
    S.texte('le gène', 860, 1195, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: CREME }); S.texte('venu du virus', 860, 1245, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: CREME });
    g.restore();
    O.multi([['CHROMOSOME ', CREME], ['7', OR]], 1420, 120);
  }

  // le nom qui s'écrit lettre à lettre
  function nom(p, t, l) {
    O.fondImg('placenta', 1.3, .5, .5, .22);
    O.petitTitre('SON NOM', 720);
    const s = p.t, n = Math.min(s.length, Math.floor((t - p.a) / .07) + 1);
    S.texte(s.slice(0, n), W / 2, 900, { taille: 170, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.5)', flou: 40, max: 980 });
    O.barreRouge(1010, eo(pr(t, p.a + s.length * .07, .3)), 14, -.02);
    if (p.sous) { g.save(); g.globalAlpha = pr(t, p.a + .6, .3); sous(p.sous, 1110); g.restore(); }
  }

  function embryon(p, t, l) {
    const k = back(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    rond(0, 0, 330, 'rgba(217,180,90,.06)', 'rgba(239,230,210,.7)', 6);
    foetus(0, 10, 1.5, t);
    g.restore();
    if (p.t) deux(p.t, 1380, 104);
  }

  // la mère, le placenta, toi : des échanges qui circulent
  function lien(p, t, l) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.globalAlpha = k;
    g.fillStyle = '#3a2420'; g.beginPath(); g.ellipse(W / 2, 620, 300, 90, 0, 0, 7); g.fill(); g.strokeStyle = ROUGE; g.lineWidth = 8; g.stroke();
    S.texte('PLACENTA', W / 2, 620, { taille: 52, coul: CREME, esp: 6 });
    S.texte('TA MÈRE', W / 2, 450, { taille: 60, coul: CREME, esp: 8 });
    g.strokeStyle = OR; g.lineWidth = 16; g.beginPath(); g.moveTo(W / 2, 700); g.bezierCurveTo(400, 820, 680, 900, W / 2, 1000); g.stroke();
    for (let i = 0; i < 6; i++) { const u = ((t - p.a) * .6 + i / 6) % 1, b = 1 - u, x = b * b * b * 540 + 3 * b * b * u * 400 + 3 * b * u * u * 680 + u * u * u * 540, y = b * b * b * 700 + 3 * b * b * u * 820 + 3 * b * u * u * 900 + u * u * u * 1000;
      rond(x, y, 10, CREME); }
    foetus(W / 2, 1110, .75, t);
    g.restore();
    if (p.t) deux(p.t, 1440, 100);
  }

  // souris ; p.mort : ses embryons s'éteignent un à un
  function souris(p, t, l) {
    const dessin = (x, y, s) => { g.save(); g.translate(x, y); g.scale(s, s); g.fillStyle = '#2c241b'; g.strokeStyle = CREME; g.lineWidth = 7;
      g.beginPath(); g.ellipse(0, 0, 170, 100, 0, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.ellipse(190, -30, 90, 62, -.3, 0, 7); g.fill(); g.stroke();
      rond(170, -105, 42, '#3a2f25', CREME, 7); rond(240, -40, 9, CREME); rond(275, -10, 8, ROUGE);
      g.beginPath(); g.moveTo(-165, 20); g.bezierCurveTo(-300, 60, -330, -120, -420, -60); g.stroke(); g.restore(); };
    if (!p.mort) { const k = back(pr(t, p.a, .35)); dessin(lerp(900, 560, eo(pr(t, p.a, .4))), 860, 1.3 * k);
      const kx = pr(t, p.a + .6, .3); if (kx > 0) { g.save(); g.globalAlpha = kx; S.texte('SANS SYNCYTINE', W / 2, 1110, { taille: 64, coul: ROUGE, esp: 4, contour: NOIR, contourL: 8 }); g.restore(); } }
    else {
      dessin(600, 520, .8);
      for (let i = 0; i < 4; i++) { const x = 180 + i * 240, y = 960, km = pr(t, p.a + .25 + i * .22, .3);
        g.save(); g.globalAlpha = 1 - km * .55; g.filter = km > .5 ? 'grayscale(1)' : 'none'; foetus(x, y, .6, km > .5 ? 0 : t); g.restore();
        if (km > 0) { g.save(); g.globalAlpha = km; g.strokeStyle = ROUGE; g.lineWidth = 12; g.beginPath(); g.moveTo(x - 70, y - 120); g.lineTo(x + 70, y + 80); g.moveTo(x + 70, y - 120); g.lineTo(x - 70, y + 80); g.stroke(); g.restore(); } }
    }
    if (p.t) deux(p.t, 1400, 100);
  }

  // comparaison schématique de deux séquences : 26 cases sur 30 identiques (≈ 87 %)
  function compare(p, t, l) {
    const DIFF = new Set([4, 11, 19, 26]), c = 10, taille = 78, x0 = W / 2 - (c - 1) * taille / 2;
    const scan = p.etape === 2 ? cl((t - tps(p.pct)) / 1.3) : 0;
    [[480, 'TA SYNCYTINE 1'], [950, 'PROTÉINE DU VIRUS MSRV']].forEach(([y0, lab], b) => {
      S.texte(lab, W / 2, y0 - 70, { taille: 42, coul: b ? ROUGE : OR, esp: 5, poids: 600 });
      for (let i = 0; i < 30; i++) {
        const x = x0 + (i % c) * taille, y = y0 + Math.floor(i / c) * taille, vu = i / 30 < scan;
        const k = pr(t, p.a + i * .015 + b * .2, .25); if (k <= 0) continue;
        g.save(); g.globalAlpha = k;
        g.fillStyle = !vu ? '#3a3229' : DIFF.has(i) ? 'rgba(200,55,45,.85)' : 'rgba(217,180,90,.9)';
        g.fillRect(x - taille * .42, y - taille * .42, taille * .84, taille * .84); g.restore();
      }
    });
    S.texte('schéma : chaque case = un morceau de la protéine', W / 2, 1220, { taille: 34, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    if (p.etape === 2) {
      const v = Math.round(87 * eo(scan));
      S.texte(v + ' %', W / 2, 1420, { taille: 210, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14, ombre: 'rgba(217,180,90,.5)', flou: 40 });
      if (scan >= 1) { g.save(); g.globalAlpha = pr(t, tps(p.pct) + 1.35, .3); sous('de ressemblance', 1580); g.restore(); }
    } else O.multi([['ON ', CREME], ['COMPARE', OR]], 1420, 130);
  }

  // transfert vertical (parents → enfants) contre transfert horizontal (virus → singe)
  function horizontal(p, t, l) {
    const kv = eo(pr(t, p.a, .4)), kh = eo(pr(t, p.a + .45, .5));
    g.save(); g.globalAlpha = .55;
    bonhomme(220, 480, 1.1); bonhomme(220, 800, 1.1);
    S.d.fleche(220, 560, 220, 700, kv, { trait: CREME, ep: 8 });
    S.texte('VERTICAL', 220, 930, { taille: 44, coul: CREME, esp: 4 }); S.texte('parents → enfants', 220, 985, { taille: 38, it: true, poids: 400, police: 'Spectral', coul: CREME });
    g.restore();
    particule(460, 700, 70, l * .4, t);
    S.d.fleche(560, 700, 800, 700, kh, { trait: ROUGE, ep: 14 });
    bonhomme(880, 720, 1.4);
    if (kh > .9) { S.texte('HORIZONTAL', 680, 860, { taille: 56, coul: ROUGE, esp: 4, contour: NOIR, contourL: 8 }); S.texte('entre espèces', 680, 920, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: CREME }); }
    if (p.t) deux(p.t, 1370, 110);
  }

  // 100 cases de ton génome : 8 rouges
  function genome(p, t, l) {
    const c = 10, taille = 72, x0 = W / 2 - (c - 1) * taille / 2, y0 = 470, ROUGES = [3, 17, 28, 44, 51, 66, 79, 92];
    O.petitTitre('TON ADN', 380);
    for (let i = 0; i < 100; i++) { const x = x0 + (i % c) * taille, y = y0 + Math.floor(i / c) * taille, ir = ROUGES.indexOf(i), kr = ir >= 0 ? pr(t, p.a + .3 + ir * .1, .2) : 0;
      g.fillStyle = kr > 0 ? ROUGE : 'rgba(239,230,210,.18)'; if (kr > 0) { g.shadowColor = ROUGE; g.shadowBlur = 20 * kr; }
      g.fillRect(x - taille * .4, y - taille * .4, taille * .8, taille * .8); g.shadowBlur = 0; }
    const k = back(pr(t, p.a + 1.1, .3)); g.save(); g.translate(W / 2, 1300); g.scale(k, k);
    S.texte('PRÈS DE 8 %', 0, 0, { taille: 140, coul: ROUGE, contour: NOIR, contourL: 12, max: 960 }); g.restore();
    if (k > 0) sous('vient de virus', 1430, 66);
  }

  // copie de bac de SVT (le plan « bac » du modèle est celui de philosophie)
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

  return { virus, infection, adn, germinale, generations, proteine, fusion, chromosome, nom, embryon, lien, souris, compare, horizontal, genome, bacsvt };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'virus') L.push([p.a, 'souffle', .5]);
  if (p.type === 'infection') L.push([p.a + .65, 'aspire', .6], [p.a + 1.25, 'pop', .5]);
  if (p.type === 'adn' && p.insere) L.push([p.a + .1, 'whoosh', .4], [p.a + .75, 'pop', .7]);
  if (p.type === 'adn' && !p.insere) L.push([p.a + .2, 'bip', .35]);
  if (p.type === 'germinale') L.push([p.a, 'pop', .4], [tps(p.ovule), 'pop', .5], [tps(p.spz), 'pop', .5]);
  if (p.type === 'generations') p.marques.forEach(a => L.push([tps(a), 'blip', .45]));
  if (p.type === 'proteine') for (let i = 0; i < 5; i++) L.push([p.a + .2 + i * .18, 'blip', .3]);
  if (p.type === 'fusion') L.push([p.a + .1, 'aspire', .6]);
  if (p.type === 'chromosome') L.push([p.a, 'bip', .45]);
  if (p.type === 'nom') for (let k = 0; k < p.t.length; k++) L.push([p.a + k * .07, 'frappe', .3]);
  if (p.type === 'embryon') L.push([p.a + .2, 'coeur', .8], [p.a + .95, 'coeur', .8]);
  if (p.type === 'lien') L.push([p.a, 'souffle', .4]);
  if (p.type === 'souris' && p.mort) for (let i = 0; i < 4; i++) L.push([p.a + .25 + i * .22, 'coupe', .45]);
  if (p.type === 'compare' && p.etape === 2) { for (let k = 0; k < 30; k += 2) L.push([tps(p.pct) + 1.3 * k / 30, 'blip', .25]); L.push([tps(p.pct) + 1.32, 'valide', .8]); }
  if (p.type === 'compare' && p.etape === 1) L.push([p.a, 'papier', .3]);
  if (p.type === 'horizontal') L.push([p.a + .45, 'whoosh', .6]);
  if (p.type === 'genome') for (let i = 0; i < 8; i++) L.push([p.a + .3 + i * .1, 'blip', .35]);
  if (p.type === 'bacsvt') L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .6]);
};
