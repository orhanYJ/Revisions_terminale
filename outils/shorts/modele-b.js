// Modèle B « Néon » : schémas plats lumineux sur fond sombre quadrillé, une couleur néon par chapitre,
// barre de progression en haut, chiffres qui défilent, petits sons d'interface. Inspiré des tops scientifiques.
(function () {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const FOND = '#06080d', BLANC = '#eef3ff', GRIS = '#6b7488';
  const NEON = ['#3be8ff', '#b6ff3b', '#ff4b6e', '#ffb43b', '#c77dff'];   // un par chapitre
  let coul = NEON[0];

  function chap(t) { let c = 0; S.PLANS.forEach(p => { if (p.a <= t && p.ch !== undefined) c = p.ch; }); return c; }
  const st = (o = {}) => Object.assign({ trait: coul, ep: 8, lueur: coul, flou: 26 }, o);
  function neon(s, x, y, taille, c = coul, o = {}) { return S.texte(s, x, y, Object.assign({ taille, coul: BLANC, ombre: c, flou: 34, ombre2: c }, o)); }
  function etiquette(s, y, c = coul) { S.texte(s, W / 2, y, { taille: 34, police: 'JetBrains Mono', poids: 500, coul: c, esp: 6 }); }
  function compteur(v, dec, suffixe, x, y, taille, c) { neon(v.toFixed(dec).replace('.', ',') + suffixe, x, y, taille, c, { police: 'JetBrains Mono', poids: 500 }); }

  function grille(t) {
    g.save(); g.strokeStyle = 'rgba(120,150,200,.07)'; g.lineWidth = 2;
    const dec = (t * 18) % 90;
    for (let x = -90 + dec; x < W; x += 90) { g.beginPath(); g.moveTo(x, 0); g.lineTo(x, H); g.stroke(); }
    for (let y = -90 + dec; y < H; y += 90) { g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); }
    g.restore();
  }
  function progression(t) {
    const c = chap(t), n = window.CHAPITRES.length, w = 150, e = 18, x0 = W / 2 - (n * w + (n - 1) * e) / 2;
    window.CHAPITRES.forEach((s, i) => {
      const x = x0 + i * (w + e), on = i === c, fait = i < c;
      g.save(); g.lineWidth = 4; g.strokeStyle = on ? NEON[i] : fait ? 'rgba(238,243,255,.35)' : 'rgba(238,243,255,.15)';
      if (on) { g.shadowColor = NEON[i]; g.shadowBlur = 24; g.fillStyle = NEON[i] + '33'; g.beginPath(); g.roundRect(x, 150, w, 56, 12); g.fill(); }
      g.beginPath(); g.roundRect(x, 150, w, 56, 12); g.stroke(); g.restore();
      S.texte(String(i + 1).padStart(2, '0'), x + w / 2, 179, { taille: 28, police: 'JetBrains Mono', poids: 500, coul: on ? BLANC : fait ? 'rgba(238,243,255,.5)' : 'rgba(238,243,255,.25)' });
    });
    S.texte(window.CHAPITRES[c], W / 2, 250, { taille: 30, police: 'JetBrains Mono', poids: 500, coul: NEON[c], esp: 8 });
  }
  // portrait en bichromie néon
  function duo(nom, cx, cy, w, h, z, fy) {
    const im = S.img(nom); if (!im) return;
    g.save(); g.beginPath(); g.roundRect(cx - w / 2, cy - h / 2, w, h, 30); g.clip();
    g.filter = 'grayscale(1) contrast(1.5) brightness(.9)'; S.cover(im, cx - w / 2, cy - h / 2, w, h, z, .5, fy); g.filter = 'none';
    g.globalCompositeOperation = 'multiply'; g.fillStyle = coul; g.fillRect(cx - w / 2, cy - h / 2, w, h);
    g.globalCompositeOperation = 'source-over'; g.restore();
    g.save(); g.strokeStyle = coul; g.lineWidth = 6; g.shadowColor = coul; g.shadowBlur = 30; g.beginPath(); g.roundRect(cx - w / 2, cy - h / 2, w, h, 30); g.stroke(); g.restore();
  }

  const R = {
    mot(p, t) {
      const k = back(pr(t, p.a, .3)), y = 900;
      if (p.img === 'penseur') S.d.tete(540, 700, 220, st({ ep: 7 }));
      const yy = p.img ? 1180 : y;
      g.save(); g.translate(W / 2, yy); g.scale(lerp(.4, 1, k), lerp(.4, 1, k));
      const mots = p.t.split(' ');
      if (mots.length >= 3) { neon(mots.slice(0, -1).join(' '), 0, -80, 110); neon(mots[mots.length - 1], 0, 60, 150, coul); }
      else neon(p.t, 0, 0, p.petit ? 120 : 160, p.sombre ? NEON[2] : coul, { max: 960 });
      g.restore();
      if (p.sous) S.texte(p.sous, W / 2, yy + 130, { taille: 54, coul: GRIS, poids: 600 });
      if (p.t2 && t >= S.T(...p.a2) - .05) {
        const k2 = pr(t, S.T(...p.a2) - .05, .25);
        g.save(); g.strokeStyle = NEON[2]; g.lineWidth = 12; g.shadowColor = NEON[2]; g.shadowBlur = 30;
        g.beginPath(); g.moveTo(140, yy + 10); g.lineTo(lerp(140, 940, eo(k2)), yy - 10); g.stroke(); g.restore();
        g.save(); g.translate(W / 2, yy + 230); const s = back(k2); g.scale(s, s); neon(p.t2, 0, 0, 140, NEON[2], { max: 960 }); g.restore();
      }
      if (p.bruit) { for (let i = 0; i < 40; i++) { g.fillStyle = coul + '55'; g.fillRect(rnd(i + t * 30) * W, rnd(i * 3 + t * 20) * H, 40 + rnd(i) * 200, 3); } }
    },
    cerveau(p, t) {
      const k = cl((t - p.a) / .7);
      S.d.cerveau(540, 850, 360, st({ ep: 10 }), k);
      // influx qui courent
      for (let i = 0; i < 9; i++) { const a = rnd(i) * 6.28, r = ((t - p.a) * 300 + i * 70) % 330; g.save(); g.fillStyle = BLANC; g.shadowColor = coul; g.shadowBlur = 20;
        g.beginPath(); g.arc(540 + Math.cos(a) * r, 830 + Math.sin(a) * r * .7, 9, 0, 7); g.fill(); g.restore(); }
      neon('TON CERVEAU', W / 2, 1360, 130);
    },
    tampon(p, t) {
      const k = back(pr(t, p.a, .25));
      g.save(); g.translate(W / 2, 900); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k));
      const w = Math.min(980, S.largeur(p.t, { taille: p.t.length > 6 ? 110 : 230 }) + 90), h = p.t.length > 6 ? 200 : 330;
      g.strokeStyle = NEON[2]; g.lineWidth = 12; g.shadowColor = NEON[2]; g.shadowBlur = 40; g.beginPath(); g.roundRect(-w / 2, -h / 2, w, h, 26); g.stroke();
      g.restore();
      g.save(); g.translate(W / 2, 900); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k)); neon(p.t, 0, 4, p.t.length > 6 ? 110 : 230, NEON[2], { max: 900 }); g.restore();
      if (p.t === 'DÉJÀ EN MARCHE') S.d.cerveau(540, 1320, 160, st({ trait: NEON[2], lueur: NEON[2], ep: 6 }));
    },
    date(p, t) {
      const k = eo(pr(t, p.a, .7));
      etiquette('ANNÉE', 700);
      compteur(Math.round(lerp(p.de, +p.t, k)), 0, '', W / 2, 900, 280, coul);
      etiquette('ÉTATS-UNIS', 1100, GRIS);
    },
    perso(p, t) {
      // silhouette (pas de photo libre de Libet) + fiche
      const k = eo(pr(t, p.a, .35));
      g.save(); g.globalAlpha = .9; S.d.tete(540, 760, 260, st({ fond: coul + '22' })); g.restore();
      S.texte('?', 560, 700, { taille: 150, coul: coul, ombre: coul, flou: 30 });
      g.save(); g.translate(0, lerp(80, 0, k)); g.globalAlpha = k;
      neon(p.t, W / 2, 1230, 100, coul, { max: 960 });
      S.texte(p.sous.toUpperCase(), W / 2, 1330, { taille: 34, police: 'JetBrains Mono', poids: 500, coul: GRIS, esp: 4 });
      g.restore();
    },
    poignet(p, t) {
      const lt = t - p.a, ang = Math.max(0, Math.sin(lt * 3.2)) * .75;
      S.d.main(640, 900, ang, st({ ep: 9 }), 1.35);
      // arc qui montre l'angle
      g.save(); g.strokeStyle = BLANC; g.lineWidth = 4; g.setLineDash([10, 10]); g.beginPath(); g.arc(640, 900, 260, -ang, 0); g.stroke(); g.restore();
      neon('PLIE LE POIGNET', W / 2, 1360, 110);
    },
    horloge(p, t) {
      const base = S.T('s3', 'horloge') - .06, lt = t - p.a;
      const ang = ((p.fige ? (p.a - base) + Math.min(lt, .25) : t - base) / 2.56) * 2 * Math.PI;
      const k = back(pr(t, p.a, .3));
      g.save(); g.translate(W / 2, 860); g.scale(lerp(.6, 1, k), lerp(.6, 1, k));
      S.d.horloge(0, 0, 320, ang, st({ ep: 8, point: NEON[2], lueurPoint: NEON[2], marque: NEON[3] }), p.fige ? ang + .02 : undefined);
      g.restore();
      etiquette('1 TOUR = 2,56 s', 1250, GRIS);
      neon(p.t, W / 2, 1360, 100, p.fige ? NEON[3] : coul);
    },
    eeg(p, t) {
      if (!p.bruit) { S.d.tete(540, 640, 190, st({ ep: 6 })); [[470, 470], [560, 450], [640, 480], [420, 530]].forEach(([x, y], i) => { g.save(); g.fillStyle = BLANC; g.shadowColor = coul; g.shadowBlur = 24; g.beginPath(); g.arc(x, y, 14, 0, 7); g.fill(); g.restore(); }); }
      const y = p.bruit ? 900 : 1080;
      g.save(); g.strokeStyle = 'rgba(238,243,255,.12)'; g.lineWidth = 3; g.strokeRect(60, y - 150, 960, 300); g.restore();
      S.d.eeg(80, 1000, y, t, 110, st({ ep: 5, trait: p.bruit ? NEON[2] : coul, lueur: p.bruit ? NEON[2] : coul }), { bruit: p.bruit });
      neon(p.t, W / 2, p.bruit ? 1200 : 1340, 100, p.bruit ? NEON[2] : coul);
    },
    frise(p, t) {
      const x = s => lerp(110, 970, (s + .6) / .7), y = 900, e = p.etape, k = eo(pr(t, p.a, .45));
      etiquette(e >= 4 ? 'LE VETO DE LIBET' : 'ÉCHELLE DE TEMPS (s)', 600);
      g.save(); g.strokeStyle = 'rgba(238,243,255,.5)'; g.lineWidth = 6; g.beginPath(); g.moveTo(90, y); g.lineTo(990, y); g.stroke();
      for (let s = -.6; s <= .1001; s += .1) { g.beginPath(); g.moveTo(x(s), y - 14); g.lineTo(x(s), y + 14); g.stroke(); } g.restore();
      const rep = (s, c, haut, bas, kk) => {
        if (kk <= 0) return;
        g.save(); g.strokeStyle = c; g.shadowColor = c; g.shadowBlur = 26; g.lineWidth = 9; g.beginPath(); g.moveTo(x(s), y + 60); g.lineTo(x(s), lerp(y + 60, y - 90, eo(kk))); g.stroke();
        g.fillStyle = BLANC; g.beginPath(); g.arc(x(s), y, 14, 0, 7); g.fill(); g.restore();
        compteur(s, 1, ' s', x(s), y - 150, 60, c);
        S.texte(bas, x(s), y + 110, { taille: 30, police: 'JetBrains Mono', poids: 500, coul: c, max: 300 });
      };
      rep(0, BLANC, '', 'GESTE', 1);
      rep(-.5, NEON[2], '', 'CERVEAU', e === 1 ? k : 1);
      if (e >= 2) rep(-.2, NEON[3], '', 'TU VEUX', e === 2 ? k : 1);
      if (e === 3) {
        g.save(); g.fillStyle = NEON[2] + '55'; g.shadowColor = NEON[2]; g.shadowBlur = 30; g.fillRect(x(-.5), y - 40, (x(-.2) - x(-.5)) * k, 80); g.restore();
        compteur(lerp(0, .3, k), 1, ' s', W / 2, 1270, 220, NEON[2]);
        S.texte('SANS TOI', W / 2, 1420, { taille: 44, police: 'JetBrains Mono', poids: 500, coul: GRIS, esp: 10 });
      }
      if (e >= 4) {
        g.save(); g.fillStyle = NEON[4] + '55'; g.shadowColor = NEON[4]; g.shadowBlur = 30; g.fillRect(x(-.2), y - 40, (x(0) - x(-.2)) * (e === 4 ? k : 1), 80); g.restore();
        if (e === 4) neon('TON POUVOIR', W / 2, 1270, 110, NEON[4]);
        else { const kk = back(pr(t, p.a, .3)); g.save(); g.translate(W / 2, 1290); g.scale(lerp(2, 1, kk), lerp(2, 1, kk)); neon('VETO', 0, 0, 200, NEON[2]); g.restore(); }
      }
    },
    portrait(p, t) {
      const k = back(pr(t, p.a, .35));
      g.save(); g.translate(W / 2, 760); g.scale(lerp(.5, 1, k), lerp(.5, 1, k)); g.translate(-W / 2, -760);
      duo(p.img, W / 2, 760, 560, 740, 1.05, .35); g.restore();
      neon(p.t, W / 2, 1270, 160);
      S.texte(p.sous, W / 2, 1390, { taille: 44, police: 'JetBrains Mono', poids: 500, coul: GRIS });
    },
    pierre(p, t) {
      const lt = t - p.a;
      if (p.etape === 1) {
        // trajectoire en pointillé + pierre
        g.save(); g.strokeStyle = 'rgba(238,243,255,.3)'; g.lineWidth = 4; g.setLineDash([14, 14]); g.beginPath();
        for (let k = 0; k <= 1; k += .02) { const x = lerp(120, 960, k), y = 1250 - Math.sin(k * Math.PI) * 700; k ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); g.restore();
        const k = cl(lt / 1.6); S.d.pierre(lerp(120, 960, k), 1250 - Math.sin(k * Math.PI) * 700, 80, k * 9, st({ fond: coul + '33' }));
        neon('UNE PIERRE', W / 2, 1440, 120);
      } else {
        S.d.pierre(540, 700, 150, .3, st({ fond: coul + '33', ep: 10 }));
        const k = back(pr(t, p.a, .35)); g.save(); g.translate(540, 1100); g.scale(k, k);
        g.strokeStyle = coul; g.lineWidth = 6; g.shadowColor = coul; g.shadowBlur = 26; g.fillStyle = FOND; g.beginPath(); g.roundRect(-450, -120, 900, 240, 60); g.fill(); g.stroke();
        S.texte(p.bulle, 0, 0, { taille: 50, poids: 600, coul: BLANC, max: 820 }); g.restore();
      }
    },
    causes(p, t) {
      S.d.tete(660, 880, 260, st({ ep: 8 }));
      [[60, 640], [40, 880], [60, 1120]].forEach(([x0, y0], i) => {
        const k = eo(pr(t, p.a + i * .15, .35)), c = NEON[(i + 2) % 5];
        S.d.fleche(x0 + 120, y0, 400, 840 + (i - 1) * 80, k, { trait: c, lueur: c, ep: 10 });
        if (k > .4) { g.save(); g.strokeStyle = c; g.shadowColor = c; g.shadowBlur = 20; g.lineWidth = 5; g.beginPath(); g.arc(x0 + 60, y0, 52, 0, 7); g.stroke(); g.restore(); S.texte('?', x0 + 60, y0 + 4, { taille: 70, coul: BLANC }); }
      });
      neon(p.t, W / 2, 1370, 130);
      S.texte(p.sous.toUpperCase(), W / 2, 1480, { taille: 40, police: 'JetBrains Mono', poids: 500, coul: GRIS, esp: 6 });
    },
    stop(p, t) {
      const lt = t - p.a;
      // bug d'écran : tranches décalées
      for (let i = 0; i < 12; i++) { g.fillStyle = NEON[i % 5] + '22'; g.fillRect((rnd(i + Math.floor(lt * 30)) - .5) * 200, i * 160, W, 60); }
      const k = back(pr(t, p.a + .05, .25));
      S.texte('⏸', W / 2, 700, { taille: 220, coul: BLANC, ombre: NEON[2], flou: 30 });
      g.save(); g.translate(W / 2, 1000); g.scale(lerp(2, 1, k), lerp(2, 1, k)); neon(p.t, 0, 0, 140, NEON[2], { max: 960 }); g.restore();
    },
    bac(p, t) {
      const k = eo(pr(t, p.a, .4));
      g.save(); g.translate(0, lerp(300, 0, k)); g.globalAlpha = k;
      g.strokeStyle = coul; g.lineWidth = 6; g.shadowColor = coul; g.shadowBlur = 30; g.beginPath(); g.roundRect(150, 500, 780, 760, 30); g.stroke(); g.shadowBlur = 0;
      etiquette('BAC · PHILOSOPHIE', 590);
      S.texte('Sommes-nous libres', W / 2, 800, { taille: 72, poids: 700, coul: BLANC });
      S.texte('de nos choix ?', W / 2, 890, { taille: 72, poids: 700, coul: BLANC });
      for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(238,243,255,.12)'; g.fillRect(230, 1010 + i * 50, 620 - (i === 3 ? 260 : 0), 8); }
      g.restore();
      const kc = pr(t, p.a + .4, .3); if (kc > 0) { g.save(); g.translate(820, 560); g.scale(back(kc), back(kc)); g.fillStyle = NEON[1]; g.shadowColor = NEON[1]; g.shadowBlur = 30; g.beginPath(); g.arc(0, 0, 70, 0, 7); g.fill(); S.texte('✓', 0, 4, { taille: 90, coul: FOND }); g.restore(); }
      neon('QUESTION DE BAC', W / 2, 1430, 110);
    },
    chaine(p, t) {
      const k = back(pr(t, p.a, .35));
      g.save(); g.translate(W / 2, 760); g.scale(k, k); g.shadowColor = '#ff2a2a'; g.shadowBlur = 50; S.d.lecture(0, 0, 120, BLANC, '#ff2a2a'); g.restore();
      neon('RÉVISIONS', W / 2, 1010, 150, coul);
      neon('ANIMÉES', W / 2, 1160, 150, NEON[3]);
      const k2 = eo(pr(t, p.a + .4, .4)); g.save(); g.globalAlpha = k2;
      S.texte('▶ SÉRIE « LA LIBERTÉ » SUR YOUTUBE', W / 2, 1300, { taille: 34, police: 'JetBrains Mono', poids: 500, coul: GRIS }); g.restore();
    },
  };

  const SANS_ST = new Set(['mot', 'tampon', 'stop', 'date', 'chaine', 'bac']);
  function rendu(t) {
    const p = S.planA(t), l = t - p.a;
    coul = NEON[chap(t)];
    g.fillStyle = FOND; g.fillRect(0, 0, W, H);
    grille(t);
    // halo de couleur du chapitre
    const h = g.createRadialGradient(W / 2, 900, 50, W / 2, 900, 900); h.addColorStop(0, coul + '22'); h.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = h; g.fillRect(0, 0, W, H);
    // entrée de plan : glissement rapide latéral (whip) puis léger zoom
    const kw = eo(pr(t, p.a, .18)), dx = (1 - kw) * (p.i % 2 ? -260 : 260), z = (1 + l * .01) * (1 + .05 * eo(S.coup(t)));
    let sx = 0, sy = 0; if (p.choc && l < .3) { const a = (1 - l / .3) * 18; sx = (rnd(t * 91) - .5) * a; sy = (rnd(t * 57) - .5) * a; }
    g.save(); g.translate(W / 2 + dx + sx, H / 2 + sy); g.scale(z, z); g.translate(-W / 2, -H / 2);
    g.globalAlpha = cl(kw * 1.5);
    R[p.type](p, t, l);
    g.restore();
    progression(t);
    const gr = S.groupeA(t);
    if (gr && !SANS_ST.has(p.type)) {
      const txt = gr.mots.map(m => m[2].toUpperCase()).join(' ');
      const w = Math.min(960, S.largeur(txt, { taille: 58 }) + 70);
      g.save(); g.fillStyle = 'rgba(6,8,13,.85)'; g.beginPath(); g.roundRect(W / 2 - w / 2, 1610, w, 100, 22); g.fill(); g.restore();
      let x = W / 2 - (w - 70) / 2; const k = Math.min(1, 890 / S.largeur(txt, { taille: 58 }));
      gr.mots.forEach(m => { const s = m[2].toUpperCase() + ' ', on = t >= m[0] - .02 && t < m[0] + m[1] + .05; const ww = S.largeur(s, { taille: 58 * k });
        S.texte(s, x + ww / 2, 1662, { taille: 58 * k, coul: on ? coul : t >= m[0] ? BLANC : 'rgba(238,243,255,.3)', ombre: on ? coul : undefined, flou: 20 }); x += ww; });
    }
    if (l < .05) { g.fillStyle = coul + '55'; g.fillRect(0, 0, W, H); }
    if (t > S.D.dur - .25) { g.fillStyle = `rgba(0,0,0,${pr(t, S.D.dur - .25, .25)})`; g.fillRect(0, 0, W, H); }
  }

  function sons() {
    const L = [];
    S.PLANS.forEach(p => {
      L.push([p.a, p.choc ? 'drop' : 'whoosh', p.choc ? 1 : .55]);
      L.push([p.a + .02, 'pop', .5]);
      if (p.ch !== undefined && p.i > 0) L.push([p.a, 'chapitre', .7]);
      if (p.type === 'date') for (let k = 0; k < 12; k++) L.push([p.a + k * .055, 'blip', .4]);
      if (p.type === 'horloge' && !p.fige) for (let k = 0; k < Math.floor((p.b - p.a) / .25); k++) L.push([p.a + k * .25, 'tic', .4]);
      if (p.type === 'horloge' && p.fige) L.push([p.a + .2, 'blip', .8]);
      if (p.t2) L.push([S.T(...p.a2) - .05, 'glitch', .8]);
      if (p.type === 'frise') L.push([p.a + .1, 'blip', .7]);
      if (p.type === 'frise' && p.etape === 3) for (let k = 0; k < 8; k++) L.push([p.a + k * .055, 'blip', .35]);
      if (p.type === 'stop') L.push([p.a, 'glitch', 1]);
      if (p.type === 'pierre' && p.etape === 1) L.push([p.a, 'souffle', .8]);
      if (p.type === 'bac') L.push([p.a + .4, 'valide', .7]);
      if (p.bruit) L.push([p.a, 'statique', .5]);
      if (p.type === 'chaine') L.push([p.a, 'valide', .9]);
    });
    return { sons: L, musique: 'pulse', bpm: 112 };
  }

  window.MODELE = { images: window.IMAGES, rendu, sons };
})();
