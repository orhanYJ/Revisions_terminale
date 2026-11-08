// Plans propres au short « 5 affirmations sur l'évolution » (format vrai ou faux), dans le style du modèle A
// (noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
window.SANS_ST_A = [];
window.PROPRES_A = ['cinq', 'helice', 'score', 'phago', 'bacteries', 'tubes', 'fourmis', 'conjugaison', 'resist', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const VERT = '#7fbf6a', BRUN = '#26221d', BLEU = '#9ec3d6';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const deuxR = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? ROUGE : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };

  // bactérie en bâtonnet ; o.plasmide : petit anneau rouge ; o.chromo : ADN replié
  function bacterie(x, y, s, rot, coul, o = {}) {
    g.save(); g.translate(x, y); g.rotate(rot);
    g.fillStyle = coul; g.strokeStyle = o.trait || NOIR; g.lineWidth = Math.max(3, s * .07);
    g.beginPath(); g.roundRect(-s, -s * .45, 2 * s, s * .9, s * .45); g.fill(); g.stroke();
    if (o.chromo) { g.strokeStyle = 'rgba(13,11,9,.6)'; g.lineWidth = s * .06; g.beginPath();
      for (let i = 0; i <= 20; i++) { const u = i / 20, xx = lerp(-s * .6, s * .45, u), yy = Math.sin(u * 14) * s * .18; i ? g.lineTo(xx, yy) : g.moveTo(xx, yy); } g.stroke(); }
    if (o.plasmide) { g.strokeStyle = ROUGE; g.lineWidth = s * .09; g.beginPath(); g.arc(s * .6, -s * .1, s * .17, 0, 7); g.stroke(); }
    g.restore();
  }
  // fourmi de profil, (x, y) = centre du thorax
  function fourmi(x, y, s, coul, t) {
    g.save(); g.translate(x, y); g.strokeStyle = coul; g.fillStyle = coul; g.lineWidth = s * .05; g.lineCap = 'round';
    for (let i = 0; i < 3; i++) { const a = Math.sin(t * 10 + i * 2) * .12, x0 = -s * .15 + i * s * .15;
      g.beginPath(); g.moveTo(x0, 0); g.lineTo(x0 + (i - 1) * s * .35, s * .35); g.lineTo(x0 + (i - 1) * s * .5 + a * s, s * .7); g.stroke(); }
    g.beginPath(); g.ellipse(-s * .75, -s * .05, s * .48, s * .32, -.2, 0, 7); g.fill();     // abdomen
    g.beginPath(); g.ellipse(0, -s * .02, s * .3, s * .16, 0, 0, 7); g.fill();                // thorax
    g.beginPath(); g.ellipse(s * .5, -s * .12, s * .22, s * .18, 0, 0, 7); g.fill();          // tête
    g.beginPath(); g.moveTo(s * .6, -s * .25); g.quadraticCurveTo(s * .75, -s * .7, s * 1.0, -s * .55); g.stroke();
    g.restore();
  }
  // simulation du protocole de Buri (schéma) : 107 populations, 32 copies du gène, 19 générations
  const BURI = []; for (let i = 0; i < 107; i++) { let f = .5; const L = [f];
    for (let gen = 1; gen <= 19; gen++) { let n = 0; for (let k = 0; k < 32; k++) if (rnd(i * 1013 + gen * 37 + k * .7 + 3) < f) n++; f = n / 32; L.push(f); } BURI.push(L); }

  // cinq cartes retournées
  function cinq(p, t) {
    for (let i = 0; i < 5; i++) {
      const k = back(pr(t, p.a + i * .12, .3)); if (k <= 0) continue;
      const x = 150 + i * 195, y = 860 + Math.abs(i - 2) * 30, r = (i - 2) * .08;
      g.save(); g.translate(x, lerp(1300, y, eo(pr(t, p.a + i * .12, .3)))); g.rotate(r); g.scale(k, k);
      g.fillStyle = i % 2 ? '#f3ecdc' : '#e9dfc8'; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 30; g.fillRect(-85, -125, 170, 250); g.shadowColor = 'transparent';
      g.strokeStyle = OR; g.lineWidth = 5; g.strokeRect(-72, -112, 144, 224);
      S.texte(String(i + 1), 0, -70, { taille: 44, coul: GRIS }); S.texte('?', 0, 25, { taille: 120, coul: ROUGE });
      g.restore();
    }
    deux('5|AFFIRMATIONS', 1420, 120);
  }

  // double hélice d'ADN qui tourne
  function helice(p, t) {
    const lt = t - p.a, k = eo(pr(t, p.a, .5));
    for (let i = 0; i < 26; i++) {
      const y = 480 + i * 34, ph = i * .45 + lt * 3, a = Math.sin(ph) * 230 * k, b = -a, z = Math.cos(ph);
      g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 6; g.beginPath(); g.moveTo(W / 2 + a, y); g.lineTo(W / 2 + b, y); g.stroke();
      g.fillStyle = z > 0 ? OR : '#8a7440'; g.beginPath(); g.arc(W / 2 + a, y, 14, 0, 7); g.fill();
      g.fillStyle = z > 0 ? '#7c2a24' : ROUGE; g.beginPath(); g.arc(W / 2 + b, y, 14, 0, 7); g.fill();
    }
    deux('SUR|L’ÉVOLUTION', 1440, 120);
  }

  // le score : « ? / 5 » ; étape 2 : les cinq réponses V F V F V
  function score(p, t) {
    if (p.etape === 2) {
      O.petitTitre('— LES RÉPONSES —', 520);
      ['V', 'F', 'V', 'F', 'V'].forEach((s, i) => { const k = back(pr(t, p.a + .1 + i * .18, .3)); if (k <= 0) return;
        const x = 160 + i * 190, c = s === 'V' ? VERT : ROUGE; g.save(); g.translate(x, 780); g.scale(k, k);
        g.fillStyle = BRUN; g.strokeStyle = c; g.lineWidth = 8; g.beginPath(); g.roundRect(-80, -80, 160, 160, 26); g.fill(); g.stroke();
        S.texte(s, 0, 4, { taille: 100, coul: c }); S.texte(String(i + 1), 0, 125, { taille: 40, coul: GRIS }); g.restore(); });
      const k = back(pr(t, p.a + 1.1, .3)); g.save(); g.translate(W / 2, 1130); g.scale(k, k);
      S.texte('? / 5', 0, 0, { taille: 200, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 }); g.restore();
      deux('COMBIEN|TU EN AS JUSTES ?', 1420, 100);
    } else {
      const s = 1 + .04 * Math.sin((t - p.a) * 8), k = back(pr(t, p.a, .3));
      g.save(); g.translate(W / 2, 860); g.scale(k * s, k * s);
      S.texte('? / 5', 0, 0, { taille: 260, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.5)', flou: 40 }); g.restore();
      deux(p.t || 'COMBIEN|TU EN AS JUSTES ?', 1420, 110);
    }
  }

  // une cellule avale une bactérie ; étape 2 : la bactérie vit dedans, entourée de deux membranes, jamais digérée
  function phago(p, t) {
    const cx = W / 2, cy = 880, R = 360, lt = t - p.a;
    g.fillStyle = 'rgba(239,230,210,.08)'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath();
    for (let i = 0; i <= 80; i++) { const a = i / 80 * 6.283, r = R + Math.sin(a * 5 + lt * 2) * 10; i ? g.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r) : g.moveTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r); }
    g.closePath(); g.fill(); g.stroke();
    g.fillStyle = 'rgba(217,180,90,.15)'; g.strokeStyle = OR; g.lineWidth = 5; g.beginPath(); g.arc(cx - 140, cy - 60, 90, 0, 7); g.fill(); g.stroke();
    S.texte('NOYAU', cx - 140, cy - 60, { taille: 30, coul: OR });
    const k = p.etape === 2 ? 1 : eo(pr(t, p.a + .1, 1.1)), bx = lerp(cx + 560, cx + 130, k), by = lerp(cy + 40, cy + 90, k);
    if (k > .75) { const kv = pr(t, p.a + .9, .4) + (p.etape === 2 ? 1 : 0); g.strokeStyle = CREME; g.lineWidth = 6; g.setLineDash([16, 10]);
      g.beginPath(); g.ellipse(bx, by, 130, 82, .2, 0, 6.283 * cl(kv)); g.stroke(); g.setLineDash([]); }
    bacterie(bx, by, 95, .2, OR, { chromo: true, trait: NOIR });
    if (p.etape === 2) {
      const s = .5 + .5 * Math.sin(lt * 6); g.strokeStyle = `rgba(127,191,106,${.5 + .5 * s})`; g.lineWidth = 8; g.beginPath(); g.ellipse(bx, by, 145, 96, .2, 0, 7); g.stroke();
      O.tampon('INTACTE', cx, cy + 300, pr(t, p.a + .35, .3), -.08, 80, VERT);
      deux('MAIS JAMAIS|DIGÉRÉE', 1440, 110);
    } else deux('AVALÉE PAR|UNE CELLULE', 1440, 110);
  }

  // une boîte de bactéries ; étape 1 : quelques mutations au hasard ; étape 2 : l'antibiotique tue les autres
  function bacteries(p, t) {
    const cx = W / 2, cy = 860, R = 380, lt = t - p.a;
    g.fillStyle = 'rgba(158,195,214,.06)'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.arc(cx, cy, R, 0, 7); g.fill(); g.stroke();
    const tue = p.etape === 2 ? eo(pr(t, p.a + .2, 1.2)) : 0;
    if (p.etape === 2) { g.fillStyle = 'rgba(158,195,214,.18)'; g.beginPath(); g.arc(cx, cy, R * tue, 0, 7); g.fill(); }
    for (let i = 0; i < 34; i++) {
      const a = rnd(i * 3.1) * 6.283, r = Math.sqrt(rnd(i * 7.7 + 1)) * (R - 70), x = cx + Math.cos(a) * r, y = cy + Math.sin(a) * r, rot = rnd(i * 5.3) * 3;
      const mut = rnd(i * 11.3 + 2) < .16, tm = p.a + .3 + rnd(i * 2.9) * 1.2, rouge = mut && (p.etape === 2 || t >= tm);
      if (p.etape === 2 && !mut) { const d = r / R; if (tue > d) { const kk = cl((tue - d) * 4); g.globalAlpha = 1 - kk; } }
      bacterie(x, y, 40, rot, rouge ? ROUGE : CREME);
      g.globalAlpha = 1;
      if (mut && p.etape !== 2 && t >= tm && t < tm + .35) { const ks = 1 - (t - tm) / .35; g.strokeStyle = OR; g.lineWidth = 6; g.globalAlpha = ks;
        for (let j = 0; j < 6; j++) { const aj = j * 1.047; g.beginPath(); g.moveTo(x + Math.cos(aj) * 50, y + Math.sin(aj) * 50); g.lineTo(x + Math.cos(aj) * 85, y + Math.sin(aj) * 85); g.stroke(); } g.globalAlpha = 1; }
    }
    if (p.etape === 2) { O.petitTitre('— ANTIBIOTIQUE —', 400, BLEU); deuxR(p.t || 'L’ANTIBIOTIQUE|SÉLECTIONNE', 1440, 105); }
    else deux(p.t || 'MUTATIONS|AU HASARD', 1440, 110);
  }

  // l'expérience de Buri (schéma simulé) : 107 tubes ; étape 1 départ à 0,5 ; 2 générations ; 3 allèle perdu ; 4 allèle fixé
  function tubes(p, t) {
    const e = p.etape || 1, lt = t - p.a;
    const gen = e === 1 ? 0 : e === 2 ? Math.min(19, Math.floor(lt / 1.8 * 19)) : 19;
    O.petitTitre(e === 1 ? '— 107 POPULATIONS · 16 DROSOPHILES —' : `— GÉNÉRATION ${gen} —`, 380, e >= 3 ? CREME : OR);
    for (let i = 0; i < 107; i++) {
      const c = i % 15, r = Math.floor(i / 15), x = 106 + c * 62, y = 470 + r * 108;
      const kin = e === 1 ? back(pr(t, p.a + i * .006, .25)) : 1; if (kin <= 0) continue;
      const f = BURI[i][gen], perdu = f === 0 && e >= 3, fixe = f === 1 && e >= 4;
      g.save(); g.translate(x, y); g.scale(kin, kin);
      g.fillStyle = 'rgba(239,230,210,.07)'; g.strokeStyle = perdu ? ROUGE : fixe ? OR : 'rgba(239,230,210,.6)'; g.lineWidth = perdu || fixe ? 5 : 3;
      g.beginPath(); g.roundRect(-20, -42, 40, 84, [4, 4, 18, 18]); g.fill(); g.stroke();
      if (f > 0) { g.fillStyle = fixe ? OR : 'rgba(217,180,90,.85)'; const h = 76 * f; g.beginPath(); g.roundRect(-16, 38 - h, 32, h, [2, 2, 15, 15]); g.fill(); }
      if (perdu) { g.strokeStyle = ROUGE; g.lineWidth = 5; g.beginPath(); g.moveTo(-14, -14); g.lineTo(14, 14); g.moveTo(14, -14); g.lineTo(-14, 14); g.stroke(); }
      g.restore();
    }
    S.texte('schéma : simulation du protocole de Buri', W / 2, 1290, { taille: 32, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    if (e === 1) deux(p.t || '0,5 AU DÉPART|PARTOUT', 1440, 100);
    else if (e === 2) deux('LE HASARD|SEUL', 1440, 110);
    else if (e === 3) deuxR('L’ALLÈLE|A DISPARU', 1440, 110);
    else deux('ICI, IL EST|LE SEUL', 1440, 110);
  }

  // deux fourmis des bois : étape 0 une fourmi ; 1 deux fourmis identiques ; 2 leur ADN diffère
  function fourmis(p, t) {
    const e = p.etape || 0, lt = t - p.a;
    O.petitTitre('— FOURMIS DES BOIS —', 420);
    if (e === 0) { fourmi(W / 2, 860, 340, CREME, lt); deux('DEUX FOURMIS|DES BOIS', 1440, 105); return; }
    const k = eo(pr(t, p.a, .4));
    fourmi(lerp(W / 2, 280, k), 820, 220, CREME, lt); fourmi(lerp(W / 2, 800, k), 820, 220, CREME, lt + .3);
    if (e === 1) { S.texte('=', W / 2, 820, { taille: 160, coul: OR }); deux('LONGTEMPS|CONFONDUES', 1440, 110); return; }
    // code-barres ADN sous chaque fourmi : identiques au début, puis différents
    const kd = pr(t, p.a + .2, .6);
    [[280, 0], [800, 1]].forEach(([x, j]) => { for (let b = 0; b < 14; b++) { const diff = j === 1 && rnd(b * 3.3) < .45 && kd > b / 14;
      g.fillStyle = diff ? ROUGE : OR; g.fillRect(x - 200 + b * 29, 1010, 18, 120); }
      S.texte('ADN', x, 1180, { taille: 40, coul: CREME, esp: 6 }); });
    const kn = back(pr(t, p.a + .5, .3)); g.save(); g.translate(W / 2, 820); g.scale(kn, kn); S.texte('≠', 0, 0, { taille: 170, coul: ROUGE }); g.restore();
    S.texte('Formica lugubris · Formica paralugubris', W / 2, 1270, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
    deuxR('1996 :|DEUX ESPÈCES', 1440, 115);
  }

  // conjugaison : étape 1 un pont se forme ; étape 2 une copie du plasmide passe
  function conjugaison(p, t) {
    const lt = t - p.a, kp = p.etape === 2 ? 1 : eo(pr(t, p.a + .2, .7));
    O.petitTitre('— DEUX ESPÈCES DE BACTÉRIES —', 420);
    g.strokeStyle = CREME; g.lineWidth = 22; g.lineCap = 'round'; g.beginPath(); g.moveTo(400, 860); g.lineTo(lerp(400, 680, kp), 860); g.stroke();
    bacterie(270, 860, 170, 0, OR, { chromo: true });
    bacterie(810, 860, 170, 0, BLEU, { chromo: true, plasmide: p.etape === 2 && t >= p.a + 1.2 });
    g.strokeStyle = ROUGE; g.lineWidth = 15; g.beginPath(); g.arc(372, 843, 29, 0, 7); g.stroke();   // plasmide de la donneuse
    if (p.etape === 2) { const kc = eo(pr(t, p.a + .1, 1.1)); if (kc < 1) { g.strokeStyle = ROUGE; g.lineWidth = 12; g.beginPath(); g.arc(lerp(372, 912, kc), lerp(843, 843, kc), 24, 0, 7); g.stroke(); } }
    S.texte('DONNEUSE', 270, 1060, { taille: 40, coul: OR, esp: 4 }); S.texte('RECEVEUSE', 810, 1060, { taille: 40, coul: BLEU, esp: 4 });
    S.texte('plasmide', 372, 740, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: ROUGE });
    deux(p.etape === 2 ? 'UNE COPIE|D’ADN PASSE' : 'UN PONT|SE FORME', 1440, 110);
  }

  // les résistances voyagent : le plasmide rouge gagne les bactéries voisines
  function resist(p, t) {
    const lt = t - p.a, B = [];
    for (let i = 0; i < 24; i++) B.push([140 + rnd(i * 4.1) * 800, 520 + rnd(i * 9.7 + 2) * 760, rnd(i * 6.3) * 3, rnd(i * 1.9 + 5) < .5 ? OR : BLEU]);
    const d0 = B.map(b => Math.hypot(b[0] - B[0][0], b[1] - B[0][1]));
    B.forEach(([x, y, r, c], i) => { const on = lt >= d0[i] / 700; bacterie(x, y, 48, r, c, { plasmide: on });
      if (on && lt < d0[i] / 700 + .25) { g.strokeStyle = ROUGE; g.lineWidth = 4; g.globalAlpha = 1 - (lt - d0[i] / 700) / .25; g.beginPath(); g.arc(x, y, 70, 0, 7); g.stroke(); g.globalAlpha = 1; } });
    deuxR('LES RÉSISTANCES|VOYAGENT', 1440, 105);
  }

  // « Dis ton score en commentaire »
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-420, -170, 840, 300, 50); g.fill();
    g.beginPath(); g.moveTo(-250, 120); g.lineTo(-300, 230); g.lineTo(-170, 125); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-300, -20, 70, 0, 7); g.fill();
    S.texte('MOI', -300, -16, { taille: 38, coul: NOIR });
    S.texte('Mon score :', 40, -60, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: NOIR });
    const n = Math.floor(((t - p.a) * 3) % 6);
    S.texte(n + ' / 5', 40, 40, { taille: 110, police: 'Spectral', poids: 600, coul: ROUGE });
    g.restore();
    deux('DIS TON SCORE|EN COMMENTAIRE', 1440, 105);
  }

  return { cinq, helice, score, phago, bacteries, tubes, fourmis, conjugaison, resist, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  if (p.type === 'cinq') for (let i = 0; i < 5; i++) L.push([p.a + i * .12, 'pop', .35]);
  if (p.type === 'helice') L.push([p.a, 'whoosh', .45]);
  if (p.type === 'score' && p.etape === 2) for (let i = 0; i < 5; i++) L.push([p.a + .1 + i * .18, 'blip', .4]);
  if (p.type === 'phago' && p.etape !== 2) L.push([p.a + .1, 'aspire', .6]);
  if (p.type === 'bacteries' && p.etape !== 2) L.push([p.a + .4, 'pop', .3], [p.a + .9, 'pop', .3]);
  if (p.type === 'bacteries' && p.etape === 2) L.push([p.a + .2, 'souffle', .6]);
  if (p.type === 'tubes' && p.etape === 2) for (let k = 0; k < 10; k++) L.push([p.a + k * .18, 'tic', .35]);
  if (p.type === 'tubes' && p.etape === 4) L.push([p.a + .05, 'valide', .5]);
  if (p.type === 'conjugaison') L.push([p.a + .15, p.etape === 2 ? 'whoosh' : 'frotte', .45]);
  if (p.type === 'resist') L.push([p.a + .1, 'pop', .3], [p.a + .5, 'pop', .3], [p.a + .9, 'pop', .3]);
  if (p.type === 'commentaire') L.push([p.a, 'pop', .5]);
};
