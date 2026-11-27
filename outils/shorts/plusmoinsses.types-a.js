// Plans propres au short « SES : plus ou moins ? » (habillage jeu télé). O = outils du modèle (carte, multi, tampon,
// barreRouge, petitTitre, fondImg, photo, al, C = couleurs de l'habillage). Couleurs : O.C et O.al seulement.
// Convention : OR = PLUS (▲) ou premier rôle, ROUGE = MOINS (▼) ou second rôle.
window.SANS_ST_A = ['titre', 'score', 'duel'];
window.PROPRES_A = ['titre', 'score', 'duel', 'tertiaire', 'thermo', 'taux', 'balance', 'barres', 'camembert', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const deux = (txt, y, taille = 110, c2 = OR) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? c2 : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };
  // cadre de plateau télé : ampoules qui clignotent autour d'un rectangle arrondi
  function ampoules(x, y, w, h, t, c = OR) {
    g.save(); g.strokeStyle = c; g.lineWidth = 8; g.beginPath(); g.roundRect(x, y, w, h, 40); g.stroke();
    const n = 34, per = 2 * (w + h);
    for (let i = 0; i < n; i++) {
      let d = i / n * per, px, py;
      if (d < w) { px = x + d; py = y; } else if ((d -= w) < h) { px = x + w; py = y + d; } else if ((d -= h) < w) { px = x + w - d; py = y + h; } else { d -= w; px = x; py = y + h - d; }
      const on = (i + Math.floor(t * 8)) % 3 === 0;
      g.fillStyle = on ? CREME : al(c, .45); if (on) { g.shadowColor = c; g.shadowBlur = 20; } else g.shadowBlur = 0;
      g.beginPath(); g.arc(px, py, 11, 0, 7); g.fill();
    }
    g.restore();
  }
  // silhouette simple (tête + buste), pour les personnes des schémas
  function perso(x, y, s, c) {
    g.save(); g.fillStyle = c; g.beginPath(); g.arc(x, y - s * .55, s * .28, 0, 7); g.fill();
    g.beginPath(); g.moveTo(x - s * .45, y + s * .45); g.quadraticCurveTo(x - s * .45, y - s * .2, x, y - s * .2); g.quadraticCurveTo(x + s * .45, y - s * .2, x + s * .45, y + s * .45); g.closePath(); g.fill(); g.restore();
  }

  // ---------- titre : PLUS ▲ / OU / MOINS ▼, bandeau « SPÉCIALITÉ SES »
  function titre(p, t) {
    const lt = t - p.a, k1 = back(pr(lt, 0, .3)), k2 = back(pr(lt, .2, .3)), k3 = back(pr(lt, .4, .3));
    const b = Math.sin(t * 7) * 18;
    pop(k1, W / 2, 540 - b, () => { S.texte('▲', 0, -150, { taille: 170, coul: OR }); S.texte('PLUS', 0, 30, { taille: 210, coul: OR, contour: NOIR, contourL: 14 }); });
    pop(k2, W / 2, 880, () => { rond(0, 0, 95, ROUGE, CREME, 8); S.texte('OU', 0, 6, { taille: 90, coul: CREME }); });
    pop(k3, W / 2, 1220 + b, () => { S.texte('MOINS', 0, -30, { taille: 210, coul: ROUGE, contour: NOIR, contourL: 14 }); S.texte('▼', 0, 150, { taille: 170, coul: ROUGE }); });
    const kb = back(pr(lt, .6, .3)); pop(kb, W / 2, 1520, () => { g.fillStyle = CREME; g.beginPath(); g.roundRect(-300, -55, 600, 110, 55); g.fill();
      S.texte('SPÉCIALITÉ SES', 0, 4, { taille: 60, coul: NOIR, esp: 4 }); });
  }

  // ---------- score : etape 0 = quatre cases vides ; etape 1 = les quatre bonnes réponses, puis « TON SCORE ? »
  const REPONSES = [['TRAVAIL', 0], ['CHÔMAGE', 1], ['INÉGALITÉS', 0], ['MONDIALISATION', 1]];
  function score(p, t) {
    const lt = t - p.a;
    if (!p.etape) {
      ampoules(110, 430, 860, 640, t);
      for (let i = 0; i < 4; i++) pop(pr(lt, .1 + i * .12, .3), 260 + i * 187, 750, () => {
        g.fillStyle = al(CREME, .1); g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.roundRect(-75, -110, 150, 220, 22); g.fill(); g.stroke();
        S.texte('?', 0, 6, { taille: 120, coul: OR });
      });
      S.texte('0 / 4', W / 2, 980, { taille: 80, coul: CREME });
      deux('COMPTE TES|POINTS', 1370, 120);
      return;
    }
    S.texte('LES BONNES RÉPONSES', W / 2, 400, { taille: 62, coul: OR, max: 960 });
    REPONSES.forEach(([m, plus], i) => {
      const k = pr(lt, i * .2, .3), y = 560 + i * 190; if (k <= 0) return;
      g.save(); g.globalAlpha = cl(k * 2); g.translate(lerp(500, 0, eo(k)), 0);
      g.fillStyle = al(CREME, .1); g.beginPath(); g.roundRect(110, y - 75, 860, 150, 30); g.fill();
      S.texte(`${i + 1} · ${m}`, 150, y, { taille: 52, coul: CREME, align: 'left', max: 480 });
      S.texte(plus ? '▲ PLUS' : '▼ MOINS', 930, y, { taille: 66, coul: plus ? OR : ROUGE, align: 'right' });
      g.restore();
    });
    const kf = back(pr(lt, 1, .35)); g.save(); g.translate(W / 2, 1380); g.scale(kf, kf);
    S.texte('TON SCORE : … / 4', 0, 0, { taille: 100, coul: OR, contour: NOIR, contourL: 10, max: 960 }); g.restore();
  }

  // ---------- duel : « DUEL n » dans un cadre d'ampoules, le thème, une image ou une balance dessinée
  function fleau(x, y, s, ang, c) {   // balance : pied, fléau incliné de ang, deux plateaux
    g.save(); g.translate(x, y); g.strokeStyle = c; g.fillStyle = c; g.lineWidth = s * .05; g.lineCap = 'round';
    g.beginPath(); g.moveTo(0, -s * .55); g.lineTo(0, s * .6); g.stroke(); g.fillRect(-s * .35, s * .58, s * .7, s * .08);
    g.save(); g.translate(0, -s * .55); g.rotate(ang);
    g.beginPath(); g.moveTo(-s * .8, 0); g.lineTo(s * .8, 0); g.stroke();
    [-1, 1].forEach(d => { g.save(); g.translate(d * s * .8, 0); g.rotate(-ang);
      g.beginPath(); g.moveTo(0, 0); g.lineTo(-s * .25, s * .45); g.moveTo(0, 0); g.lineTo(s * .25, s * .45); g.stroke();
      g.beginPath(); g.ellipse(0, s * .47, s * .3, s * .07, 0, 0, 7); g.fill(); g.restore(); });
    g.restore(); g.restore();
  }
  function duel(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    ampoules(80, 280, 920, 1300, t, p.n === 4 ? ROUGE : OR);
    g.save(); g.translate(W / 2, 470); g.scale(lerp(2, 1, k), lerp(2, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(p.n === 4 ? 'DERNIER DUEL' : 'DUEL ' + p.n, 0, 0, { taille: p.n === 4 ? 130 : 170, coul: OR, contour: NOIR, contourL: 14, max: 860 }); g.restore();
    const kv = eo(pr(lt, .15, .4));
    if (p.img) { g.save(); g.globalAlpha = kv; O.carte(p.img, W / 2, 920, 620, 520, .03, 1.1 + lt * .04, .5, .45, { couleur: true }); g.restore(); }
    else if (p.icone === 'balance') { g.save(); g.globalAlpha = kv; fleau(W / 2, 940, 420, Math.sin(t * 3) * .18, CREME); g.restore(); }
    const km = back(pr(lt, .3, .3)); g.save(); g.translate(W / 2, 1360); g.scale(km, km);
    g.fillStyle = ROUGE; g.beginPath(); g.roundRect(-400, -80, 800, 160, 80); g.fill();
    S.texte(p.matiere, 0, 6, { taille: 84, coul: CREME, max: 720 }); g.restore();
  }

  // ---------- tertiaire : l'usine rétrécit, les bureaux et commerces grandissent (schéma, sans chiffres)
  function usine(x, y, s, c) {
    g.save(); g.translate(x, y); g.fillStyle = c; g.beginPath(); g.moveTo(-s, s * .5); g.lineTo(-s, -s * .1);
    for (let i = 0; i < 3; i++) { g.lineTo(-s + i * s * .5, -s * .45); g.lineTo(-s + (i + 1) * s * .5, -s * .1); }
    g.lineTo(s * .5, -s * .1); g.lineTo(s * .5, -s * .9); g.lineTo(s * .8, -s * .9); g.lineTo(s * .8, s * .5); g.closePath(); g.fill(); g.restore();
  }
  function bureau(x, y, s, c) {
    g.save(); g.translate(x, y); g.fillStyle = c; g.fillRect(-s * .55, -s, s * 1.1, s * 1.5);
    g.fillStyle = al(NOIR, .55); for (let r = 0; r < 5; r++) for (let q = 0; q < 3; q++) g.fillRect(-s * .42 + q * s * .32, -s * .85 + r * s * .26, s * .2, s * .14);
    g.restore();
  }
  function tertiaire(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .1, 1.2));
    S.texte('L’EMPLOI EN FRANCE', W / 2, 350, { taille: 60, coul: OR });
    g.save(); g.globalAlpha = lerp(1, .55, k); usine(300, 820, lerp(200, 110, k), CREME); g.restore();
    bureau(760, 820, lerp(110, 230, k), OR);
    S.texte('INDUSTRIE ▼', 300, 1020, { taille: 58, coul: ROUGE });
    S.texte('SERVICES ▲', 760, 1120, { taille: 58, coul: OR });
    const kt = back(pr(lt, .9, .3)); g.save(); g.translate(W / 2, 1420); g.scale(lerp(1.6, 1, kt), lerp(1.6, 1, kt)); g.globalAlpha = cl(kt * 2);
    S.texte('TERTIARISATION', 0, 0, { taille: 120, coul: OR, contour: NOIR, contourL: 12, max: 980 }); g.restore();
  }

  // ---------- thermo : jauge du taux de chômage, France 2025 : 7,7 %
  function thermo(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .2, 1.3)), v = 7.7 * k, x = W / 2, y0 = 1180, hmax = 640;   // échelle : 0 à 25 %
    S.texte('TAUX DE CHÔMAGE', W / 2, 340, { taille: 72, coul: CREME });
    S.texte('France, 2025', W / 2, 420, { taille: 48, it: true, poids: 400, police: 'Spectral', coul: OR });
    g.save(); g.fillStyle = al(CREME, .12); g.beginPath(); g.roundRect(x - 60, y0 - hmax, 120, hmax, 60); g.fill(); g.restore();
    [0, 5, 10, 15, 20, 25].forEach(m => { const y = y0 - m / 25 * hmax; g.fillStyle = al(CREME, .5); g.fillRect(x + 75, y - 2, 40, 4);
      S.texte(m + ' %', x + 140, y, { taille: 36, coul: GRIS, align: 'left' }); });
    const h = v / 25 * hmax; g.save(); g.fillStyle = ROUGE; g.beginPath(); g.roundRect(x - 45, y0 - h, 90, h, 45); g.fill(); g.restore();
    rond(x, y0 + 60, 95, ROUGE, CREME, 8);
    S.texte(v.toFixed(1).replace('.', ',') + ' %', x - 150, y0 - h, { taille: 100, coul: OR, contour: NOIR, contourL: 10, align: 'right', police: 'Spectral', poids: 700 });
    S.texte('des actifs', W / 2, 1420, { taille: 60, it: true, poids: 400, police: 'Spectral', coul: CREME });
  }

  // ---------- taux : chômeurs / actifs ; les jeunes en études (inactifs) ne comptent pas (schéma qualitatif)
  function taux(p, t) {
    const lt = t - p.a, k1 = eo(pr(lt, 0, .4)), k2 = eo(pr(lt, .6, .4)), k3 = back(pr(lt, 1.2, .3));
    // fraction en haut
    g.save(); g.globalAlpha = k1;
    S.texte('TAUX DE CHÔMAGE', W / 2, 360, { taille: 56, coul: OR, esp: 4 });
    S.texte('CHÔMEURS', W / 2, 470, { taille: 76, coul: ROUGE });
    g.fillStyle = CREME; g.fillRect(W / 2 - 260, 530, 520, 8);
    S.texte('ACTIFS', W / 2, 600, { taille: 76, coul: CREME });
    g.restore();
    // 20 silhouettes : les jeunes en études (grisés, hors du calcul) et les actifs, dont 1 sur 5 au chômage
    for (let i = 0; i < 20; i++) {
      const x = 170 + (i % 5) * 185, y = 760 + Math.floor(i / 5) * 165 + (i >= 10 ? 40 : 0), etude = i < 10, chom = !etude && i % 5 === 1;
      const ki = pr(lt, .3 + i * .03, .25); if (ki <= 0) continue;
      g.save(); g.globalAlpha = ki * (etude && k2 > 0 ? lerp(1, .25, k2) : 1);
      perso(x, y, 110, etude ? GRIS : chom ? ROUGE : OR); g.restore();
    }
    if (k2 > 0) { g.save(); g.globalAlpha = k2; S.texte('en études : pas comptés', W / 2, 1000, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 6 }); g.restore(); }
    pop(k3, W / 2, 1460, () => S.texte('1 JEUNE ACTIF SUR 5', 0, 0, { taille: 82, coul: OR, contour: NOIR, contourL: 10, max: 960 }));
  }

  // ---------- balance : 1995, la balance des salaires penche du côté des hommes
  function balance(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .2, .8)), ang = lerp(0, .28, k) + Math.sin(t * 4) * .01, s = 480, py0 = 900 - s * .55;
    S.texte('REVENU SALARIAL · PRIVÉ', W / 2, 340, { taille: 54, coul: OR, max: 960 });
    fleau(W / 2, 900, s, ang, CREME);
    // plateaux : femmes à gauche (revenu plus faible : plateau plus léger, qui monte), hommes à droite
    const px = s * .8 * Math.cos(ang), py = s * .8 * Math.sin(ang), yG = py0 - py + s * .47, yD = py0 + py + s * .47;
    perso(W / 2 - px, yG - 64, 120, OR); perso(W / 2 + px, yD - 64, 120, ROUGE);
    S.texte('FEMMES', W / 2 - px, yG + 70, { taille: 50, coul: OR });
    S.texte('HOMMES', W / 2 + px, yD + 70, { taille: 50, coul: ROUGE });
    const kt = back(pr(lt, 1, .3)); pop(kt, W / 2, 1440, () => S.texte('1995 : − 34 %', 0, 0, { taille: 120, coul: OR, contour: NOIR, contourL: 12, police: 'Spectral', poids: 700 }));
  }

  // ---------- barres : salaire annuel moyen en équivalent temps plein, privé, 2024 (Insee) : 31 200 € contre 36 270 €
  function barres(p, t) {
    const lt = t - p.a, base = 1200, hmax = 560;
    S.texte('À TEMPS DE TRAVAIL ÉGAL', W / 2, 340, { taille: 60, coul: OR, max: 960 });
    S.texte('salaire annuel moyen, privé, 2024', W / 2, 420, { taille: 44, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 });
    [[330, 31200, 'FEMMES', OR], [750, 36270, 'HOMMES', ROUGE]].forEach(([x, v, nom, c], i) => {
      const k = eo(pr(lt, i * .15, .8)), h = v / 37000 * hmax * k;
      g.save(); g.fillStyle = c; g.beginPath(); g.roundRect(x - 140, base - h, 280, h, 20); g.fill(); g.restore();
      if (k > .3) S.texte(Math.round(v * k).toLocaleString('fr-FR') + ' €', x, base - h - 55, { taille: 62, coul: CREME, police: 'Spectral', poids: 700, max: 380 });
      S.texte(nom, x, base + 60, { taille: 56, coul: c });
    });
    const kt = pr(lt, 1.1, .3); if (kt > 0) O.tampon('− 14 %', W / 2, 1450, kt, -.08, 110, ROUGE);
  }

  // ---------- camembert : part de la Chine dans les exportations mondiales de marchandises, 1983 : 1,2 %
  function camembert(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .1, .7)), ks = eo(pr(lt, .8, .6)), cx = W / 2, cy = 1000, r = 320;
    S.texte('EXPORTATIONS MONDIALES', W / 2, 340, { taille: 60, coul: OR, max: 960 });
    S.texte('de marchandises, 1983', W / 2, 420, { taille: 46, it: true, poids: 400, police: 'Spectral', coul: CREME });
    const a0 = -Math.PI / 2, part = .012 * 6.2832;
    g.save(); g.fillStyle = al(CREME, .2); g.beginPath(); g.moveTo(cx, cy); g.arc(cx, cy, r * k, a0 + part, a0 + 6.2832 * k); g.closePath(); g.fill();
    g.strokeStyle = al(CREME, .5); g.lineWidth = 4; g.stroke(); g.restore();
    if (ks > 0) {   // la part chinoise, sortie du disque et grossie à la loupe
      const ex = 40 * ks; g.save(); g.fillStyle = ROUGE; g.beginPath(); g.moveTo(cx + ex * Math.cos(a0 + part / 2), cy + ex * Math.sin(a0 + part / 2));
      g.arc(cx + ex * Math.cos(a0 + part / 2), cy + ex * Math.sin(a0 + part / 2), r, a0, a0 + part); g.closePath(); g.fill(); g.restore();
      g.save(); g.globalAlpha = ks; g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath(); g.moveTo(cx + 20, cy - r - 30); g.lineTo(cx + 180, cy - r - 120); g.stroke(); g.restore();
      pop(ks, cx + 290, cy - r - 140, () => S.texte('CHINE : 1,2 %', 0, 0, { taille: 64, coul: ROUGE, contour: NOIR, contourL: 8 }));
    }
    S.texte('le reste du monde', cx, cy + 60, { taille: 50, it: true, poids: 400, police: 'Spectral', coul: CREME });
  }

  // ---------- commentaire : une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    g.save(); g.translate(W / 2, 800); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-250, 160); g.lineTo(-320, 280); g.lineTo(-160, 160); g.fill();
    const msg = 'J’ai eu … / 4', n = Math.floor(cl((lt - .25) / .6) * msg.length);
    S.texte(msg.slice(0, n), 0, 0, { taille: 90, coul: NOIR, max: 780 });
    g.restore();
    deux('DIS-LE EN|COMMENTAIRE', 1300, 110, ROUGE);
  }

  return { titre, score, duel, tertiaire, thermo, taux, balance, barres, camembert, commentaire };
};
window.SONS_A = (p, L) => {
  if (p.type === 'titre') L.push([p.a, 'montee', .5], [p.a + .4, 'pop', .5]);
  if (p.type === 'score') for (let i = 0; i < 4; i++) L.push([p.a + .1 + i * (p.etape ? .2 : .12), 'pop', .4]);
  if (p.type === 'duel') L.push([p.a, 'gong', .6], [p.a + .3, 'pop', .5]);
  if (p.type === 'tertiaire') L.push([p.a + .1, 'whoosh', .4], [p.a + .9, 'pop', .5]);
  if (p.type === 'thermo') L.push([p.a + .2, 'montee', .45]);
  if (p.type === 'taux') { for (let i = 0; i < 4; i++) L.push([p.a + .3 + i * .15, 'pop', .3]); L.push([p.a + 1.2, 'valide', .5]); }
  if (p.type === 'balance') L.push([p.a + .2, 'frotte', .5], [p.a + 1, 'pop', .5]);
  if (p.type === 'barres') L.push([p.a, 'montee', .4], [p.a + 1.1, 'tampon', .8]);
  if (p.type === 'camembert') L.push([p.a + .1, 'whoosh', .4], [p.a + .8, 'pop', .6]);
  if (p.type === 'commentaire') L.push([p.a + .25, 'clic', .4]);
};
