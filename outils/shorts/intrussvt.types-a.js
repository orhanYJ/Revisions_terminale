// Plans propres au short « SVT : trouve l'intrus » (habillage néon). O = outils du modèle (carte, multi, tampon,
// barreRouge, petitTitre, fondImg, photo, al, C = couleurs de l'habillage). Couleurs : O.C et O.al seulement.
// Convention des dessins : OR = premier rôle (allèle, chromosome paternel, algues), ROUGE = second rôle ou alerte.
window.SANS_ST_A = ['titre', 'score', 'manche', 'compteur'];
window.PROPRES_A = ['titre', 'score', 'manche', 'crossing', 'compteur', 'vertical', 'virus', 'derive', 'tri', 'roscoff', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // titre sur deux lignes : la première en crème, la seconde en couleur vive
  const deux = (txt, y, taille = 110, c2 = OR) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? c2 : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const lueur = (c, f = 26) => { g.shadowColor = c; g.shadowBlur = f; };
  const ligne = (x0, y0, x1, y1, c, ep) => { g.strokeStyle = c; g.lineWidth = ep; g.lineCap = 'round'; g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); };
  function fleche(x0, y0, x1, y1, k, c, ep = 10) {
    if (k <= 0) return; const x = lerp(x0, x1, k), y = lerp(y0, y1, k), a = Math.atan2(y1 - y0, x1 - x0);
    g.save(); lueur(c, 18); ligne(x0, y0, x, y, c, ep);
    g.fillStyle = c; g.beginPath(); g.moveTo(x + Math.cos(a) * ep * 2.4, y + Math.sin(a) * ep * 2.4);
    g.lineTo(x + Math.cos(a + 2.4) * ep * 2.6, y + Math.sin(a + 2.4) * ep * 2.6); g.lineTo(x + Math.cos(a - 2.4) * ep * 2.6, y + Math.sin(a - 2.4) * ep * 2.6); g.fill(); g.restore();
  }
  // chromatide : bâtonnet arrondi de (x, y0) à (x, y1), coupé en deux couleurs à ys (échange)
  function chromatide(x, y0, y1, c, w = 46, ys, c2) {
    g.save(); g.beginPath(); g.roundRect(x - w / 2, y0, w, y1 - y0, w / 2); g.clip();
    g.fillStyle = c; g.fillRect(x - w / 2, y0, w, y1 - y0);
    if (ys !== undefined) { g.fillStyle = c2; g.fillRect(x - w / 2, ys, w, y1 - ys); }
    for (let y = y0 + 30; y < y1; y += 46) { g.fillStyle = al(NOIR, .22); g.fillRect(x - w / 2, y, w, 8); }
    g.restore();
    g.save(); lueur(c, 22); g.strokeStyle = al(CREME, .55); g.lineWidth = 3; g.beginPath(); g.roundRect(x - w / 2, y0, w, y1 - y0, w / 2); g.stroke(); g.restore();
  }
  // bactérie en bâtonnet, avec un petit anneau (plasmide) facultatif
  function bacterie(x, y, s, rot, c, plasmide) {
    g.save(); g.translate(x, y); g.rotate(rot); lueur(c, 20);
    g.strokeStyle = c; g.lineWidth = s * .09; g.fillStyle = al(c, .15);
    g.beginPath(); g.roundRect(-s, -s * .45, 2 * s, s * .9, s * .45); g.fill(); g.stroke();
    g.shadowBlur = 0; g.strokeStyle = al(CREME, .6); g.lineWidth = s * .06; g.beginPath();
    for (let i = 0; i <= 20; i++) { const u = i / 20, xx = lerp(-s * .6, s * .3, u), yy = Math.sin(u * 14) * s * .16; i ? g.lineTo(xx, yy) : g.moveTo(xx, yy); } g.stroke();
    if (plasmide) { g.strokeStyle = ROUGE; g.lineWidth = s * .09; g.beginPath(); g.arc(s * .6, -s * .05, s * .17, 0, 7); g.stroke(); }
    g.restore();
  }
  // moustique de profil, centre du corps en (x, y)
  function moustique(x, y, s, c, t, rot = 0) {
    g.save(); g.translate(x, y); g.rotate(rot); g.strokeStyle = c; g.fillStyle = c; g.lineCap = 'round';
    g.lineWidth = s * .05;
    for (let i = 0; i < 3; i++) { const x0 = -s * .1 + i * s * .14; g.beginPath(); g.moveTo(x0, s * .05); g.lineTo(x0 + (i - 1) * s * .3, s * .45); g.lineTo(x0 + (i - 1) * s * .45, s * .8); g.stroke(); }
    g.beginPath(); g.ellipse(-s * .55, 0, s * .5, s * .12, -.08, 0, 7); g.fill();      // abdomen
    g.beginPath(); g.ellipse(s * .05, -s * .02, s * .2, s * .15, 0, 0, 7); g.fill();    // thorax
    g.beginPath(); g.arc(s * .32, -s * .04, s * .1, 0, 7); g.fill();                     // tête
    g.lineWidth = s * .035; g.beginPath(); g.moveTo(s * .4, -s * .02); g.lineTo(s * .8, s * .12); g.stroke();   // trompe
    const b = Math.sin(t * 60) * .25;
    g.fillStyle = al(CREME, .35); g.beginPath(); g.ellipse(-s * .15, -s * .3, s * .42, s * .12, -.5 + b, 0, 7); g.fill();
    g.restore();
  }

  // ---------- titre : quatre cases, l'une devient l'intrus ; « TROUVE L'INTRUS » qui grésille
  function titre(p, t) {
    const lt = t - p.a;
    for (let i = 0; i < 4; i++) {
      const x = i % 2 ? 730 : 350, y = i < 2 ? 560 : 940, k = back(pr(lt, i * .08, .3)), bad = i === 2 && lt > .55;
      pop(k, x, y, () => {
        if (bad) g.translate(Math.sin(t * 70) * 8, 0);
        g.save(); lueur(bad ? ROUGE : OR, bad ? 40 : 18); g.strokeStyle = bad ? ROUGE : OR; g.lineWidth = 8;
        g.fillStyle = bad ? al(ROUGE, .2) : al(OR, .08); g.beginPath(); g.roundRect(-160, -160, 320, 320, 30); g.fill(); g.stroke(); g.restore();
        S.texte(bad ? '!' : '?', 0, 8, { taille: 200, coul: bad ? ROUGE : CREME });
      });
    }
    const fl = lt < .5 ? (rnd(Math.floor(t * 30)) > .4 ? 1 : .3) : 1;
    g.save(); g.globalAlpha = fl; S.texte('TROUVE', W / 2, 1290, { taille: 120, coul: CREME, ombre: OR, flou: 30 });
    S.texte('L’INTRUS', W / 2, 1440, { taille: 170, coul: ROUGE, contour: NOIR, contourL: 12, ombre2: ROUGE, flou: 30 }); g.restore();
  }

  // ---------- score : etape 0 = quatre cases vides « ? / 4 » ; etape 1 = les quatre intrus rappelés, puis « TON SCORE ? »
  const INTRUS = ['MITOSE', 'POIS', 'BURI', 'ROSCOFF'];
  function score(p, t) {
    const lt = t - p.a;
    if (!p.etape) {
      pop(back(pr(lt, 0, .35)), W / 2, 640, () => S.texte('? / 4', 0, 0, { taille: 260, coul: OR, contour: NOIR, contourL: 14, ombre: OR, flou: 40 }));
      for (let i = 0; i < 4; i++) pop(pr(lt, .25 + i * .12, .3), 210 + i * 220, 1000, () => {
        g.save(); lueur(ROUGE, 20); g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.roundRect(-85, -85, 170, 170, 24); g.stroke(); g.restore();
        S.texte(String(i + 1), 0, 6, { taille: 90, coul: al(CREME, .5) });
      });
      deux('COMBIEN TU|EN TROUVES ?', 1330, 110);
      return;
    }
    S.texte('LES 4 INTRUS', W / 2, 420, { taille: 60, coul: OR, esp: 8 });
    INTRUS.forEach((s, i) => {
      const k = pr(lt, i * .22, .3), y = 560 + i * 170;
      if (k <= 0) return;
      g.save(); g.globalAlpha = cl(k * 2); g.translate(lerp(-400, 0, eo(k)), 0);
      g.fillStyle = al(OR, .1); g.beginPath(); g.roundRect(150, y - 65, 780, 130, 24); g.fill();
      S.texte(String(i + 1), 230, y + 4, { taille: 70, coul: OR });
      S.texte(s, 560, y + 4, { taille: 80, coul: CREME });
      g.restore();
      pop(pr(lt, i * .22 + .2, .3), 860, y, () => { g.save(); lueur(ROUGE, 20); g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 44, 0, 7); g.fill(); g.restore(); S.texte('✓', 0, 4, { taille: 60, coul: NOIR }); });
    });
    const kf = back(pr(lt, 1.1, .35)); g.save(); g.translate(W / 2, 1360); g.scale(kf, kf);
    S.texte('TON SCORE : … / 4', 0, 0, { taille: 100, coul: ROUGE, contour: NOIR, contourL: 10, max: 960 }); g.restore();
  }

  // ---------- manche : « MANCHE n », quatre voyants, une image ou une icône dessinée, le thème
  function icone(nom, t, k) {
    if (nom === 'chromo') {   // deux paires de chromosomes qui se rapprochent
      [[-1, OR], [1, ROUGE]].forEach(([s, c]) => { const x = s * lerp(130, 70, k);
        g.save(); g.translate(x, 0); g.rotate(s * .5); chromatide(-26, -150, 150, c, 44); chromatide(26, -150, 150, c, 44); g.restore(); });
    } else if (nom === 'bacteries') {   // un plasmide passe d'une bactérie à l'autre
      bacterie(-140, -40, 110, .2, OR); bacterie(150, 60, 110, -.15, ROUGE);
      const u = (t * .7) % 1; g.save(); lueur(ROUGE, 20); g.strokeStyle = ROUGE; g.lineWidth = 12;
      g.beginPath(); g.arc(lerp(-80, 100, u), lerp(-20, 50, u), 24, 0, 7); g.stroke(); g.restore();
    } else if (nom === 'feu') {   // compte à rebours qui brûle : 4 / 4
      for (let i = 0; i < 3; i++) { const r = 150 + ((t * 2 + i / 3) % 1) * 140; g.save(); g.globalAlpha = 1 - ((t * 2 + i / 3) % 1); lueur(ROUGE, 30);
        g.strokeStyle = ROUGE; g.lineWidth = 10; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke(); g.restore(); }
      S.texte('4 / 4', 0, 0, { taille: 150, coul: CREME, ombre: ROUGE, flou: 40 });
    }
  }
  function manche(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    S.texte(p.n === 4 ? 'MANCHE FINALE' : 'MANCHE', W / 2, 330, { taille: 54, coul: GRIS, esp: 14 });
    g.save(); g.translate(W / 2, 520); g.scale(lerp(2.2, 1, k), lerp(2.2, 1, k)); g.globalAlpha = cl(k * 2);
    g.save(); lueur(OR, 40); g.strokeStyle = OR; g.lineWidth = 12; g.beginPath(); g.arc(0, 0, 140, 0, 7); g.stroke();
    g.setLineDash([22, 18]); g.lineDashOffset = -t * 60; g.lineWidth = 5; g.beginPath(); g.arc(0, 0, 172, 0, 7); g.stroke(); g.restore();
    S.texte(String(p.n), 0, 10, { taille: 190, coul: CREME, ombre: OR, flou: 30 }); g.restore();
    for (let i = 0; i < 4; i++) {
      const on = i < p.n, ki = pr(lt, .2 + i * .08, .25), c = i === p.n - 1 ? ROUGE : OR;
      g.save(); g.globalAlpha = .25 + .75 * ki; if (on) lueur(c, 24); g.fillStyle = on ? c : al(CREME, .15);
      g.beginPath(); g.roundRect(W / 2 - 250 + i * 130, 735, 110, 26, 13); g.fill(); g.restore();
    }
    const kv = eo(pr(lt, .15, .4));
    if (p.img) { g.save(); g.globalAlpha = kv; O.carte(p.img, W / 2, 1060, 440, 480, -.03, 1.08 + lt * .03, .5, .35); g.restore(); }
    else if (p.icone) { g.save(); g.translate(W / 2, 1060); g.scale(lerp(.6, 1, kv), lerp(.6, 1, kv)); g.globalAlpha = kv; icone(p.icone, t, kv); g.restore(); }
    const kt = eo(pr(lt, .25, .3)); g.save(); g.globalAlpha = kt; g.translate(0, lerp(60, 0, kt)); deux(p.t, 1470, 120, p.n === 4 ? ROUGE : OR); g.restore();
  }

  // ---------- crossing : deux chromosomes homologues (2 chromatides chacun) s'apparient, se croisent, échangent un morceau
  function crossing(p, t) {
    const lt = t - p.a, k1 = eo(pr(lt, 0, .7)), k2 = eo(pr(lt, .8, .6)), k3 = eo(pr(lt, 1.6, .6));
    const y0 = 380, y1 = 1180, ys = 900, xA = lerp(330, 450, k1) - k3 * 90, xB = lerp(750, 630, k1) + k3 * 90;
    const croise = k2 > 0 && k3 < 1;
    chromatide(xA - 30, y0, y1, OR, 46);
    chromatide(xB + 30, y0, y1, ROUGE, 46);
    // chromatides internes : échange de la partie basse après le croisement
    const ech = k2 >= 1;
    chromatide(xA + 30 + (croise ? Math.sin(k2 * Math.PI) * 30 * (1 - k3) : 0), y0, y1, OR, 46, ech ? ys : undefined, ROUGE);
    chromatide(xB - 30 - (croise ? Math.sin(k2 * Math.PI) * 30 * (1 - k3) : 0), y0, y1, ROUGE, 46, ech ? ys : undefined, OR);
    if (k2 > 0 && k3 < .9) {   // le chiasma
      g.save(); g.globalAlpha = Math.sin(Math.min(1, k2) * Math.PI) * .9 + (ech ? .3 : 0) * (1 - k3); lueur(CREME, 40);
      g.strokeStyle = CREME; g.lineWidth = 10; g.beginPath(); g.arc(W / 2, ys, 70, 0, 7); g.stroke(); g.restore();
    }
    pop(pr(lt, 1.7, .3), W / 2, ys + 160, () => S.texte('ÉCHANGE', 0, 0, { taille: 64, coul: CREME, ombre: OR, flou: 20 }));
    deux('CROSSING-|OVER', 1410, 120);
  }

  // ---------- compteur : 2 puissance 23 gamètes ; le nombre défile, des gamètes de toutes les couleurs apparaissent
  function compteur(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .1, 1.5)), n = Math.round(lerp(2, 8388608, k * k));
    for (let i = 0; i < 90; i++) {
      const ki = pr(lt, i * .02, .25); if (ki <= 0) continue;
      const x = 80 + rnd(i * 3.1) * 920, y = 380 + rnd(i * 7.7) * 1150, r = 16 + rnd(i) * 14;
      if (y > 700 && y < 1150) continue;
      g.save(); g.globalAlpha = .55 * ki; g.fillStyle = rnd(i * 5.3) > .5 ? OR : ROUGE; g.beginPath(); g.arc(x, y, r * back(ki), 0, 7); g.fill();
      g.fillStyle = al(NOIR, .6); g.beginPath(); g.arc(x + r * .2, y - r * .1, r * .35, 0, 7); g.fill(); g.restore();
    }
    S.texte('2²³ =', W / 2, 770, { taille: 90, coul: GRIS, poids: 700 });
    S.texte(n.toLocaleString('fr-FR'), W / 2, 920, { taille: 170, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14, ombre: OR, flou: 40, max: 1000 });
    S.texte('GAMÈTES DIFFÉRENTS', W / 2, 1080, { taille: 70, coul: CREME, esp: 4 });
    const kf = pr(lt, 1.7, .3); if (kf > 0) O.tampon('+ DE 8 MILLIONS', W / 2, 1420, kf, -.06, 90, ROUGE);
  }

  // ---------- vertical : des parents aux descendants (vertical), contre le passage entre bactéries (horizontal)
  function vertical(p, t) {
    const lt = t - p.a;
    // colonne verticale : deux parents, un enfant
    const kp = eo(pr(lt, 0, .3));
    g.save(); g.globalAlpha = kp;
    [[230, OR], [430, ROUGE]].forEach(([x, c]) => { g.save(); lueur(c, 24); g.strokeStyle = c; g.lineWidth = 10; g.fillStyle = al(c, .15); g.beginPath(); g.arc(x, 520, 70, 0, 7); g.fill(); g.stroke(); g.restore(); });
    g.restore();
    fleche(330, 610, 330, 870, eo(pr(lt, .3, .4)), OR, 12);
    pop(pr(lt, .6, .3), 330, 960, () => { g.save(); lueur(OR, 30); g.strokeStyle = CREME; g.lineWidth = 10; g.fillStyle = al(OR, .25); g.beginPath(); g.arc(0, 0, 70, 0, 7); g.fill(); g.stroke(); g.restore(); });
    S.texte('VERTICAL', 330, 1120, { taille: 66, coul: OR, ombre: OR, flou: 20 });
    S.texte('des parents', 330, 1190, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: CREME });
    S.texte('aux descendants', 330, 1240, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: CREME });
    // colonne horizontale, estompée
    g.save(); g.globalAlpha = .45;
    bacterie(760, 620, 70, 0, CREME); bacterie(840, 860, 70, 0, CREME);
    fleche(760, 690, 830, 800, 1, GRIS, 8);
    S.texte('HORIZONTAL', 800, 1120, { taille: 56, coul: GRIS });
    g.restore();
    g.save(); g.strokeStyle = al(CREME, .2); g.lineWidth = 4; g.setLineDash([14, 14]); g.beginPath(); g.moveTo(W / 2 + 40, 420); g.lineTo(W / 2 + 40, 1260); g.stroke(); g.restore();
    const kt = eo(pr(lt, .5, .3)); g.save(); g.globalAlpha = kt; deux('L’INTRUS EST|VERTICAL', 1440, 100); g.restore();
  }

  // ---------- virus : un rétrovirus dépose un gène dans l'ADN ; ce gène devient la syncytine
  function virus(p, t) {
    const lt = t - p.a, k1 = eo(pr(lt, 0, .8)), k2 = eo(pr(lt, .8, .5)), k3 = pr(lt, 1.4, .4);
    // ADN : double brin horizontal ondulé
    const yA = 1000, x0 = 80, x1 = 1000, mid = 540, ouv = k2 * 90;
    for (let b = 0; b < 2; b++) {
      g.save(); lueur(CREME, 14); g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath();
      for (let x = x0; x <= x1; x += 8) { const y = yA + (b ? 1 : -1) * (40 + Math.sin(x * .02 + t * 2) * 10); const dx = x < mid ? -ouv : ouv;
        x === x0 ? g.moveTo(x + (Math.abs(x - mid) < 200 ? dx * (1 - Math.abs(x - mid) / 200) : 0), y) : g.lineTo(x + (Math.abs(x - mid) < 200 ? dx * (1 - Math.abs(x - mid) / 200) : 0), y); }
      g.stroke(); g.restore();
    }
    // segment viral inséré (rouge)
    if (k2 > 0) { g.save(); g.globalAlpha = k2; lueur(ROUGE, 30); g.fillStyle = ROUGE; g.beginPath(); g.roundRect(mid - 80, yA - 50, 160, 100, 20); g.fill(); g.restore();
      S.texte('GÈNE VIRAL', mid, yA + 110, { taille: 46, coul: ROUGE, poids: 700 }); }
    // le virus arrive du haut
    const vx = mid, vy = lerp(360, 760, k1) - k2 * 120;
    g.save(); g.translate(vx, vy); g.rotate(t * .8); g.globalAlpha = 1 - k3 * .6; lueur(ROUGE, 26); g.strokeStyle = ROUGE; g.lineWidth = 10; g.fillStyle = al(ROUGE, .18);
    g.beginPath(); for (let i = 0; i < 6; i++) { const a = i * Math.PI / 3; i ? g.lineTo(Math.cos(a) * 90, Math.sin(a) * 90) : g.moveTo(90, 0); } g.closePath(); g.fill(); g.stroke();
    for (let i = 0; i < 12; i++) { const a = i * Math.PI / 6; ligne(Math.cos(a) * 95, Math.sin(a) * 95, Math.cos(a) * 130, Math.sin(a) * 130, ROUGE, 6); }
    g.restore();
    if (k3 > 0) { const kk = back(k3); g.save(); g.translate(W / 2, 1300); g.scale(kk, kk); S.texte('= SYNCYTINE', 0, 0, { taille: 110, coul: OR, contour: NOIR, contourL: 10, ombre: OR, flou: 30 }); g.restore(); }
    S.texte('UN GÈNE VENU D’UN VIRUS', W / 2, 1460, { taille: 62, coul: CREME, max: 960 });
  }

  // ---------- derive : fréquences d'un allèle dans des petites populations (simulation) : fixé ou perdu au hasard
  function derive(p, t) {
    const lt = t - p.a, gx = 140, gy = 420, gw = 840, gh = 760, NG = 19;
    g.save(); g.strokeStyle = al(CREME, .5); g.lineWidth = 4; g.beginPath(); g.moveTo(gx, gy); g.lineTo(gx, gy + gh); g.lineTo(gx + gw, gy + gh); g.stroke();
    g.setLineDash([10, 12]); g.strokeStyle = al(CREME, .2); [0, .5].forEach(f => { g.beginPath(); g.moveTo(gx, gy + f * gh); g.lineTo(gx + gw, gy + f * gh); g.stroke(); }); g.restore();
    S.texte('1', gx - 40, gy, { taille: 40, coul: GRIS }); S.texte('0,5', gx - 50, gy + gh / 2, { taille: 36, coul: GRIS }); S.texte('0', gx - 40, gy + gh, { taille: 40, coul: GRIS });
    S.texte('générations →', gx + gw - 150, gy + gh + 50, { taille: 36, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    const k = cl(lt / 1.6);
    for (let c = 0; c < 8; c++) {
      let f = .5; const pts = [[0, f]];
      for (let i = 1; i <= NG; i++) { if (f > 0 && f < 1) f = cl(f + (rnd(c * 37 + i * 3.3) - .5) * .32); pts.push([i, f]); }
      const n = Math.floor(k * NG) + 1, col = f >= 1 ? OR : f <= 0 ? ROUGE : al(CREME, .6);
      g.save(); lueur(col, 14); g.strokeStyle = col; g.lineWidth = 7; g.beginPath();
      pts.slice(0, n + 1).forEach(([i, v], j) => { const x = gx + i / NG * gw, y = gy + (1 - v) * gh; j ? g.lineTo(x, y) : g.moveTo(x, y); }); g.stroke(); g.restore();
    }
    if (k >= 1) { pop(pr(lt, 1.6, .3), gx + gw - 60, gy - 40, () => S.texte('FIXÉ', 0, 0, { taille: 50, coul: OR }));
      pop(pr(lt, 1.75, .3), gx + gw - 60, gy + gh + 0, () => S.texte('PERDU', 0, -40, { taille: 50, coul: ROUGE })); }
    S.texte('simulation', gx + 110, gy + gh + 50, { taille: 30, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    deux('LA DÉRIVE :|LE HASARD', 1440, 110);
  }

  // ---------- tri : l'insecticide élimine les moustiques sensibles ; les porteurs de l'allèle de résistance restent
  function tri(p, t) {
    const lt = t - p.a, ks = pr(lt, .3, .9), kg = eo(pr(lt, 1.4, .6));
    const pos = i => [180 + (i % 4) * 240, 520 + Math.floor(i / 4) * 230];
    for (let i = 0; i < 12; i++) {
      const res = i % 4 === 1 || i === 10, [x, y] = pos(i), touche = ks * 1100 > x - 60;
      if (!res && touche && kg > 0) continue;
      const tombe = !res && touche ? pr(lt, .3 + (x - 120) / 1100 * .9, .5) : 0;
      g.save(); g.globalAlpha = 1 - tombe; moustique(x + Math.sin(t * 3 + i) * 6, y + tombe * 200 + Math.cos(t * 2.5 + i) * 5, 120, res ? ROUGE : CREME, t + i, tombe * 2); g.restore();
    }
    if (ks > 0 && ks < 1) { g.save(); const x = ks * 1100; const gr = g.createLinearGradient(x - 260, 0, x, 0); gr.addColorStop(0, al(GRIS, 0)); gr.addColorStop(1, al(GRIS, .45)); g.fillStyle = gr; g.fillRect(x - 260, 400, 260, 820); g.restore(); }
    // la génération suivante : les résistants se multiplient
    if (kg > 0) for (let i = 0; i < 12; i++) { const [x, y] = pos(i), res = i % 4 === 1 || i === 10; if (res) continue;
      const k = pr(lt, 1.4 + i * .04, .3); g.save(); g.globalAlpha = cl(k); moustique(x, y, 120 * back(k), ROUGE, t + i); g.restore(); }
    S.texte('● porteur de l’allèle de résistance', W / 2, 1270, { taille: 40, coul: ROUGE, poids: 600 });
    deux('L’INSECTICIDE|TRIE', 1440, 120, ROUGE);
  }

  // ---------- roscoff : un ver plat, et des micro-algues logées sous sa peau
  function roscoff(p, t) {
    const lt = t - p.a, k = eo(pr(lt, 0, .5)), ka = pr(lt, .4, 1.2);
    const corps = () => { g.beginPath(); for (let i = 0; i <= 40; i++) { const u = i / 40, x = lerp(140, 940, u), w = Math.sin(u * Math.PI) ** .7 * 150 + 20, y = 820 + Math.sin(u * 5 + t * 3) * 30;
      i ? g.lineTo(x, y - w) : g.moveTo(x, y - w); } for (let i = 40; i >= 0; i--) { const u = i / 40, x = lerp(140, 940, u), w = Math.sin(u * Math.PI) ** .7 * 150 + 20, y = 820 + Math.sin(u * 5 + t * 3) * 30; g.lineTo(x, y + w); } g.closePath(); };
    g.save(); g.globalAlpha = k; corps(); g.fillStyle = al(CREME, .07); g.fill(); lueur(CREME, 20); g.strokeStyle = CREME; g.lineWidth = 8; g.stroke(); g.restore();
    g.save(); corps(); g.clip();
    for (let i = 0; i < 160; i++) { if (rnd(i * 2.3) > ka) continue; const u = .06 + rnd(i * 1.7) * .88, x = lerp(140, 940, u), w = Math.sin(u * Math.PI) ** .7 * 150 + 10, y = 820 + Math.sin(u * 5 + t * 3) * 30 + (rnd(i * 4.1) - .5) * 1.8 * w;
      g.fillStyle = al(OR, .85); lueur(OR, 12); g.beginPath(); g.arc(x, y, 9 + rnd(i) * 6, 0, 7); g.fill(); }
    g.restore();
    pop(pr(lt, .9, .3), 760, 560, () => { fleche(0, 0, -60, 120, 1, OR, 7); S.texte('micro-algues', 40, -40, { taille: 48, coul: OR, poids: 700 }); });
    S.texte('1 à 5 mm', 260, 1080, { taille: 40, it: true, poids: 400, police: 'Spectral', coul: GRIS });
    deux('DES ALGUES|DANS SON CORPS', 1440, 110);
  }

  // ---------- commentaire : une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const lt = t - p.a, k = back(pr(lt, 0, .35));
    g.save(); g.translate(W / 2, 800); g.scale(k, k);
    g.save(); lueur(OR, 30); g.fillStyle = al(CREME, .1); g.strokeStyle = OR; g.lineWidth = 8;
    g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(-250, 170); g.lineTo(-320, 280); g.lineTo(-160, 170); g.fill(); g.stroke(); g.restore();
    const msg = 'J’en ai trouvé … / 4', n = Math.floor(cl((lt - .25) / .7) * msg.length);
    S.texte(msg.slice(0, n), 0, 0, { taille: 76, coul: CREME, max: 780 });
    if (n < msg.length && Math.floor(t * 4) % 2) S.texte('|', S.largeur(msg.slice(0, n), { taille: 76 }) / 2 + 14, 0, { taille: 76, coul: OR });
    g.restore();
    deux('DIS-LE EN|COMMENTAIRE', 1300, 110, ROUGE);
  }

  return { titre, score, manche, crossing, compteur, vertical, virus, derive, tri, roscoff, commentaire };
};
window.SONS_A = (p, L) => {
  if (p.type === 'titre') L.push([p.a + .55, 'buzz', .5]);
  if (p.type === 'score') for (let i = 0; i < 4; i++) L.push([p.a + .25 + i * (p.etape ? .22 : .12), 'pop', .4]);
  if (p.type === 'manche') L.push([p.a, 'gong', .55], [p.a + .2, 'montee', .35]);
  if (p.type === 'crossing') L.push([p.a + .8, 'frotte', .5], [p.a + 1.7, 'pop', .5]);
  if (p.type === 'compteur') { for (let k = 0; k < 12; k++) L.push([p.a + .1 + k * .12, 'tic', .35]); L.push([p.a + 1.7, 'tampon', .8]); }
  if (p.type === 'vertical') L.push([p.a + .3, 'whoosh', .4], [p.a + .6, 'pop', .5]);
  if (p.type === 'virus') L.push([p.a + .8, 'aspire', .5], [p.a + 1.4, 'valide', .5]);
  if (p.type === 'derive') L.push([p.a, 'montee', .4]);
  if (p.type === 'tri') L.push([p.a + .3, 'souffle', .6]);
  if (p.type === 'roscoff') L.push([p.a + .9, 'pop', .4]);
  if (p.type === 'commentaire') L.push([p.a + .25, 'clic', .4]);
};
