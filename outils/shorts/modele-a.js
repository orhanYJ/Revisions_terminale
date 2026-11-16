// Modèle A « Archives » : collage d'images découpées (statues, gravures, portraits), noir, crème, or et rouge,
// gros mots qui claquent, tampons, impacts graves. Inspiré du rythme des comptes d'éloquence et d'histoire.
(function () {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  // habillages : window.THEME = 'archives' (défaut), 'neon', 'jeu', 'alerte', 'terminal' (dans le .plan.js).
  // Les plans n'utilisent que les cinq couleurs (O.C) : le même short change d'allure selon l'habillage.
  const THEMES = {
    archives: { fond: '#0d0b09', creme: '#efe6d2', or: '#d9b45a', rouge: '#c8372d', gris: '#8d8371', deco: 'carte', grain: 22,
      filtre: c => `grayscale(1) contrast(${c}) brightness(.9) sepia(.25)`, trans: ['zoom', 'zoom', 'glisse', 'tourne'] },
    neon: { fond: '#07061a', creme: '#f1efff', or: '#2de2ff', rouge: '#ff2e88', gris: '#7c76b0', deco: 'grille', grain: 10, teinte: '#7b3cff',
      filtre: c => `grayscale(1) contrast(${c * 1.1}) brightness(1)`, trans: ['glitch', 'zoom', 'glisse', 'iris', 'glitch'] },
    jeu: { fond: '#16093d', creme: '#ffffff', or: '#ffd23f', rouge: '#ff3d5a', gris: '#a39ad8', deco: 'rayons', grain: 0,
      filtre: c => `contrast(1.1) saturate(1.25)`, trans: ['chute', 'tourne', 'zoom', 'iris'] },
    alerte: { fond: '#140303', creme: '#fff5f0', or: '#ffcc00', rouge: '#ff2a2a', gris: '#a08480', deco: 'bandes', grain: 18,
      filtre: c => `grayscale(.55) contrast(${c}) brightness(.95)`, trans: ['glisse', 'zoom', 'glitch', 'chute'] },
    terminal: { fond: '#030c07', creme: '#d9ffe8', or: '#3dff8a', rouge: '#ff4d4d', gris: '#5f8c72', deco: 'code', grain: 12, teinte: '#3dff8a',
      filtre: c => `grayscale(1) contrast(${c * 1.15}) brightness(.95)`, trans: ['glitch', 'iris', 'glitch', 'zoom'] },
  };
  const TH = THEMES[new URLSearchParams(location.search).get('theme') || window.THEME] || THEMES.archives;
  const NOIR = TH.fond, CREME = TH.creme, OR = TH.or, ROUGE = TH.rouge, GRIS = TH.gris;
  // couleur + transparence : al('#efe6d2', .3) -> 'rgba(239,230,210,.3)'
  const al = (c, a) => `rgba(${parseInt(c.slice(1, 3), 16)},${parseInt(c.slice(3, 5), 16)},${parseInt(c.slice(5, 7), 16)},${a})`;
  // tempo de la musique (pulsation de la caméra sur le temps)
  const BPM = { funk_agressif: 130, funk_agressif2: 134, funk_agressif3: 127, montagem: 125, montagem2: 128, montagem3: 121,
    automotivo: 135, automotivo2: 138, hardtekk: 160, hardtekk2: 165, terre: 112, terre2: 118, finale: 100, epopee: 150, boss: 168,
    bande_annonce: 120, phonk_tension: 0 };
  let grain, lignes;

  function init() {
    const O = { carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, theme: window.THEME || 'archives', C: { NOIR, CREME, OR, ROUGE, GRIS } };
    if (window.FORMATS_A) Object.assign(R, window.FORMATS_A(O));
    if (window.TYPES_A) Object.assign(R, window.TYPES_A(O));
    // grain de papier (deux trames, alternées pour un léger scintillement de pellicule)
    grain = [0, 1].map(k => { const c = document.createElement('canvas'); c.width = 540; c.height = 960; const x = c.getContext('2d');
      const d = x.createImageData(540, 960); for (let i = 0; i < d.data.length; i += 4) { const v = rnd(i * .37 + k * 11) * 255; d.data[i] = d.data[i + 1] = d.data[i + 2] = v; d.data[i + 3] = 22; }
      for (let i = 3; i < d.data.length; i += 4) d.data[i] = TH.grain;
      x.putImageData(d, 0, 0); return c; });
    // lignes de fond façon carte ancienne
    lignes = document.createElement('canvas'); lignes.width = W; lignes.height = H; const x = lignes.getContext('2d');
    x.strokeStyle = al(OR, .07); x.lineWidth = 3;
    for (let k = 0; k < 9; k++) { x.beginPath(); let px = -50, py = rnd(k) * H; x.moveTo(px, py);
      for (let i = 0; i < 14; i++) { const nx = px + 90 + rnd(k * 31 + i) * 60, ny = py + (rnd(k * 17 + i * 3) - .5) * 260; x.quadraticCurveTo(px + 40, py + (rnd(i + k) - .5) * 200, nx, ny); px = nx; py = ny; } x.stroke(); }
  }

  // image en carte découpée : niveaux de gris contrastés, liseré crème, ombre, légère rotation
  function carte(nom, cx, cy, w, h, rot, z, fx, fy, o = {}) {
    const im = S.img(nom); if (!im) return;
    g.save(); g.translate(cx, cy); g.rotate(rot);
    g.shadowColor = 'rgba(0,0,0,.7)'; g.shadowBlur = 50; g.shadowOffsetY = 20;
    g.fillStyle = TH.deco === 'grille' || TH.deco === 'code' ? OR : CREME; g.fillRect(-w / 2 - 14, -h / 2 - 14, w + 28, h + 28);
    g.shadowColor = 'transparent';
    g.filter = o.couleur ? 'contrast(1.1) saturate(1.15)' : TH.filtre(o.contraste || 1.35).replace('brightness(.9)', `brightness(${o.lum || .9})`);
    S.cover(im, -w / 2, -h / 2, w, h, z, fx, fy);
    g.filter = 'none';
    if (TH.teinte && !o.couleur && !o.teinte) { g.globalCompositeOperation = 'multiply'; g.fillStyle = TH.teinte; g.fillRect(-w / 2, -h / 2, w, h); g.globalCompositeOperation = 'source-over'; }
    if (o.teinte) { g.globalCompositeOperation = 'multiply'; g.fillStyle = o.teinte; g.fillRect(-w / 2, -h / 2, w, h); g.globalCompositeOperation = 'source-over'; }
    g.restore();
  }
  // image plein cadre très sombre (fond)
  function fondImg(nom, z, fx, fy, a = .35) {
    const im = S.img(nom); if (!im) return;
    g.save(); g.globalAlpha = a; g.filter = TH.filtre(1.4) + ' brightness(.6)';
    S.cover(im, 0, 0, W, H, z, fx, fy); g.restore();
  }
  // photo plein cadre (en couleur par défaut), lent travelling de `de` à `a` = [zoom, fx, fy] sur la durée du plan,
  // dégradé sombre en bas pour le texte
  function photo(nom, t, a, b, de = [1.08, .5, .5], vers = [1.22, .5, .45], o = {}) {
    const im = S.img(nom); if (!im) return;
    const k = cl((t - a) / Math.max(.5, b - a));
    g.save(); g.filter = o.couleur === false ? TH.filtre(1.3) : 'contrast(1.08) saturate(1.15)';
    S.cover(im, 0, 0, W, H, lerp(de[0], vers[0], k), lerp(de[1], vers[1], k), lerp(de[2], vers[2], k)); g.filter = 'none';
    const dg = g.createLinearGradient(0, H * .45, 0, H); dg.addColorStop(0, al(NOIR, 0)); dg.addColorStop(.55, al(NOIR, .85)); dg.addColorStop(1, al(NOIR, .95));
    g.fillStyle = dg; g.fillRect(0, 0, W, H); g.restore();
  }
  // texte en plusieurs couleurs : morceaux [[texte, couleur], …] centrés
  function multi(morceaux, y, taille, o = {}) {
    const tot = morceaux.reduce((a, [s]) => a + S.largeur(s, { taille }), 0);
    const k = Math.min(1, (o.max || 940) / tot), t2 = taille * k;
    let x = W / 2 - tot * k / 2;
    morceaux.forEach(([s, c]) => { const w = S.largeur(s, { taille: t2 }); S.texte(s, x + w / 2, y, { taille: t2, coul: c, contour: NOIR, contourL: t2 * .1 }); x += w; });
  }
  function barreRouge(y, k, h = 34, rot = -.06) {
    g.save(); g.translate(W / 2, y); g.rotate(rot); g.fillStyle = ROUGE;
    g.fillRect(-520, -h / 2, 1040 * k, h); g.restore();
  }
  function tampon(txt, cx, cy, k, rot = -.14, taille = 150, coul = ROUGE) {
    const s = lerp(2.6, 1, back(k)); g.save(); g.translate(cx, cy); g.rotate(rot); g.scale(s, s); g.globalAlpha = cl(k * 3);
    const w = S.largeur(txt, { taille }) + 80;
    // usure du tampon : des trous découpés dans le dessin du tampon seulement (le fond reste visible à travers)
    const zone = new Path2D(); zone.rect(-w, -taille * 2, w * 2, taille * 4);
    for (let i = 0; i < 70; i++) { const x = (rnd(i) - .5) * w, y = (rnd(i + 50) - .5) * taille * 1.4, r = (3 + rnd(i + 9) * 9) * taille / 150;
      zone.moveTo(x + r, y); zone.arc(x, y, r, 0, Math.PI * 2, true); }
    g.clip(zone);
    g.strokeStyle = coul; g.lineWidth = 14; g.strokeRect(-w / 2, -taille * .75, w, taille * 1.5);
    g.lineWidth = 4; g.strokeRect(-w / 2 + 16, -taille * .75 + 16, w - 32, taille * 1.5 - 32);
    S.texte(txt, 0, 6, { taille, coul });
    g.restore();
  }
  function petitTitre(s, y, coul = OR) { S.texte(s, W / 2, y, { taille: 40, coul, esp: 10, poids: 600, max: 960 }); }

  // ---------------------------------------------------------------- plans
  const R = {
    // photo plein écran en couleur. Champs : img, t (titre, « | » = deux lignes), sous, de / vers ([zoom, fx, fy]), nb: true (noir et blanc)
    photo(p, t) {
      photo(p.img, t, p.a, p.b, p.de, p.vers, { couleur: !p.nb });
      const k = back(pr(t, p.a + .1, .3));
      if (p.t) { g.save(); g.translate(0, lerp(80, 0, k)); g.globalAlpha = cl(k * 2);
        const [l1, l2] = p.t.split('|'); if (l2) { multi([[l1, CREME]], 1330, 110); multi([[l2, OR]], 1460, 130); } else multi([[l1, OR]], 1420, 130);
        g.restore(); }
      if (p.sous) S.texte(p.sous, W / 2, 1560, { taille: 52, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 });
      if (p.legende) S.texte(p.legende, W - 40, H - 60, { taille: 24, coul: al(CREME, .55), align: 'right', max: 900 });
    },
    // trois à quatre images qui tombent en éventail. Champs : imgs = [nom, …], t (titre), couleur: true
    collage(p, t) {
      const L = p.imgs || [], pos = [[300, 600, -.12], [780, 680, .1], [420, 1060, .06], [760, 1120, -.08]];
      L.forEach((nom, i) => { const k = back(pr(t, p.a + i * .18, .35)); if (k <= 0) return; const [x, y, r] = pos[i % 4];
        g.save(); g.translate(lerp(i % 2 ? W + 400 : -400, x, k), y); g.rotate(r * (2 - k)); g.translate(-x, -y);
        carte(nom, x, y, 430, 520, r, 1.05, .5, .4, { couleur: p.couleur }); g.restore(); });
      if (p.t) { const k = eo(pr(t, p.a + L.length * .18, .3)); g.save(); g.globalAlpha = k; const [l1, l2] = p.t.split('|');
        if (l2) { multi([[l1, CREME]], 1430, 100); multi([[l2, OR]], 1550, 120); } else multi([[l1, OR]], 1480, 120); g.restore(); }
    },
    mot(p, t, l) {
      if (p.img) { const k = eo(pr(t, p.a, .5)); carte(p.img, W / 2, 760, 640, 860, -.03, 1.15 + l * .02, .5, .35, { lum: .8 }); }
      const y = p.img ? (p.t.includes('|') ? 1400 : 1300) : 900, k = back(pr(t, p.a, .28));
      g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k)); g.translate(-W / 2, -y);
      const t2 = p.t2 && t >= S.T(...p.a2) - .05;
      const coul = p.sombre ? ROUGE : p.bruit ? CREME : CREME;
      const mots = p.t.split(' ');
      if (p.t.includes('|')) { const [l1, l2] = p.t.split('|'); multi([[l1, coul]], y - 95, 120); multi([[l2, OR]], y + 50, 140); }
      else if (mots.length > 2 && !p.img) { multi([[mots.slice(0, -1).join(' ') + ' ', coul]], y - 95, 130); multi([[mots[mots.length - 1], OR]], y + 50, 150); }
      else multi(mots.length > 1 ? [[mots.slice(0, -1).join(' ') + ' ', coul], [mots[mots.length - 1], OR]] : [[p.t, p.sombre ? ROUGE : OR]], y, p.petit ? 120 : 170);
      g.restore();
      if (p.sous) S.texte(p.sous, W / 2, y + 120, { taille: 64, it: true, poids: 400, police: 'Spectral', coul: CREME, contour: NOIR, contourL: 8 });
      if (t2) {
        const kk = pr(t, S.T(...p.a2) - .05, .2);
        barreRouge(y, eo(kk), 30, -.04);
        const k2 = back(kk); g.save(); g.translate(W / 2, y + 230); g.scale(lerp(2, 1, k2), lerp(2, 1, k2));
        S.texte(p.t2, 0, 0, { taille: 150, coul: ROUGE, contour: NOIR, contourL: 14, max: 940 }); g.restore();
      }
      if (p.choc && !p.t2) barreRouge(y + 110, eo(pr(t, p.a + .1, .25)), 22, -.03);
      if (p.bruit) { g.save(); g.globalAlpha = .55; for (let i = 0; i < 26; i++) { const yy = rnd(i + Math.floor(t * 20) * 3) * H; g.fillStyle = i % 3 ? CREME : ROUGE; g.fillRect(0, yy, W, 2 + rnd(i) * 5); } g.restore(); }
    },
    cerveau(p, t, l) {
      carte('neurones', W / 2, 820, 860, 980, .025, 1.25 + l * .05, .45, .5, { teinte: OR, contraste: 1.6 });
      // pouls rouges
      for (let i = 0; i < 3; i++) { const k = ((t - p.a) * 1.6 + i / 3) % 1; g.save(); g.strokeStyle = ROUGE; g.globalAlpha = (1 - k) * .9; g.lineWidth = 10;
        g.beginPath(); g.arc(W / 2 + 60, 760, 80 + k * 380, 0, 7); g.stroke(); g.restore(); }
      multi([['TON ', CREME], ['CERVEAU', OR]], 1440, 150);
    },
    tampon(p, t) {
      const k = pr(t, p.a, .3);
      fondImg('neurones', 1.4, .5, .5, .22);
      tampon(p.t, W / 2, 900, k, -.1, p.t.length > 6 ? 96 : 230);
    },
    date(p, t) {
      const k = eo(pr(t, p.a, .7)), an = Math.round(lerp(p.de, +p.t, k));
      petitTitre(p.sous ? `— ${p.sous} —` : '— ÉTATS-UNIS —', 640);
      g.save(); g.strokeStyle = OR; g.lineWidth = 6; g.strokeRect(150, 700, 780, 440); g.lineWidth = 2; g.strokeRect(170, 720, 740, 400); g.restore();
      S.texte(String(an), W / 2, 930, { taille: 300, police: 'Spectral', poids: 600, coul: OR, ombre: al(OR, .5), flou: 40 });
    },
    perso(p, t, l) {
      if (p.img) carte(p.img, W / 2, 700, 820, 700, -.02, 1.6 + l * .04, .5, .55, { contraste: 1.7 });
      else { S.d.tete(560, 760, 300, { trait: CREME, fond: '#1b1712', ep: 9 }); S.texte('?', 590, 700, { taille: 160, coul: OR }); }
      // fiche d'identité
      const k = eo(pr(t, p.a + .1, .3));
      g.save(); g.translate(lerp(-600, 0, k), 0);
      g.fillStyle = CREME; g.fillRect(90, 1140, 900, 250);
      S.texte(p.t, W / 2, 1220, { taille: 100, coul: NOIR, max: 840 });
      S.texte(p.sous, W / 2, 1320, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: ROUGE });
      g.restore();
    },
    poignet(p, t) {
      const lt = t - p.a, ang = Math.max(0, Math.sin(lt * 3.2)) * .75;
      S.d.main(640, 930, ang, { trait: CREME, fond: '#2a241d', ep: 9 }, 1.35);
      petitTitre('CONSIGNE', 560, ROUGE);
      multi([['PLIE LE ', CREME], ['POIGNET', OR]], 1330, 130);
    },
    horloge(p, t) {
      const lt = t - p.a, figer = p.fige ? Math.min(lt, .25) : lt, base = (S.T('s3', 'horloge') - .06);
      const ang = ((p.fige ? (p.a - base) + figer : t - base) / 2.56) * 2 * Math.PI;
      const k = back(pr(t, p.a, .3)), z = p.fige ? lerp(1, 1.12, eo(pr(t, p.a, .4))) : lerp(.7, 1, k);
      g.save(); g.translate(W / 2, 880); g.scale(z, z);
      S.d.horloge(0, 0, 330, ang, { trait: CREME, fond: '#1b1712', ep: 10, point: ROUGE, marque: OR }, p.fige ? ang + .02 : undefined);
      g.restore();
      multi([[p.t, p.fige ? OR : CREME]], 1390, 110);
      if (p.fige) tampon('?', 840, 600, pr(t, p.a + .15, .25), .2, 120, OR);
    },
    eeg(p, t, l) {
      fondImg('vesale', 1.6, .5, .12, .45);
      if (!p.bruit) carte('vesale', W / 2, 640, 520, 620, .03, 2.3, .5, .1, { lum: .85 });
      // bande de papier
      const y = p.bruit ? 900 : 1150;
      g.save(); g.fillStyle = CREME; g.fillRect(60, y - 140, 960, 280);
      g.strokeStyle = al(ROUGE, .25); g.lineWidth = 2; for (let x = 60; x < 1020; x += 40) { g.beginPath(); g.moveTo(x, y - 140); g.lineTo(x, y + 140); g.stroke(); }
      g.restore();
      S.d.eeg(80, 1000, y, t, 110, { trait: ROUGE, ep: 6 }, { bruit: p.bruit });
      multi([[p.t, p.bruit ? ROUGE : OR]], p.bruit ? 1200 : 1400, 110);
    },
    frise(p, t) {
      // axe de −0,6 s à +0,1 s
      const x = s => lerp(110, 970, (s + .6) / .7), y = 980, e = p.etape;
      const k = eo(pr(t, p.a, .45));
      petitTitre(e >= 4 ? 'LE VETO' : 'CE QUE MESURE LIBET', 520, e >= 4 ? OR : ROUGE);
      g.save(); g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.moveTo(90, y); g.lineTo(990, y); g.stroke(); g.restore();
      const repere = (s, coul, haut, bas, kk) => {
        g.save(); g.globalAlpha = cl(kk * 2); g.strokeStyle = coul; g.lineWidth = 10; g.beginPath(); g.moveTo(x(s), y - 70); g.lineTo(x(s), y + 70); g.stroke(); g.restore();
        if (kk > 0) { const sc = back(kk); g.save(); g.translate(x(s), y - 150); g.scale(sc, sc); S.texte(haut, 0, 0, { taille: 72, coul, contour: NOIR, contourL: 8 }); g.restore();
          S.texte(bas, x(s), y + 140, { taille: 40, coul: CREME, poids: 600, max: 330 }); }
      };
      repere(0, CREME, '0 s', 'LE GESTE', 1);
      repere(-.5, ROUGE, '−0,5 s', 'TON CERVEAU', e === 1 ? k : 1);
      if (e >= 2) repere(-.2, OR, '−0,2 s', 'TU VEUX', e === 2 ? k : 1);
      if (e === 3) {
        g.save(); g.fillStyle = al(ROUGE, .55); g.fillRect(x(-.5), y - 50, (x(-.2) - x(-.5)) * k, 100); g.restore();
        const n = (lerp(0, .3, k)).toFixed(1).replace('.', ',');
        S.texte(n + ' s', W / 2, 1330, { taille: 210, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 14 });
        S.texte('sans toi', W / 2, 1480, { taille: 70, it: true, poids: 400, police: 'Spectral', coul: CREME });
      }
      if (e >= 4) {
        g.save(); g.fillStyle = al(OR, .45); g.fillRect(x(-.2), y - 50, (x(0) - x(-.2)) * (e === 4 ? k : 1), 100); g.restore();
        if (e === 4) S.texte('TON POUVOIR', W / 2, 1330, { taille: 120, coul: OR, contour: NOIR, contourL: 12 });
        else tampon('VETO', W / 2, 1360, pr(t, p.a, .3), -.08, 170);
      }
    },
    portrait(p, t, l) {
      const k = eo(pr(t, p.a, .35));
      carte(p.img, W / 2 + lerp(300, 0, k), 760, 600, 800, lerp(.15, -.035, k), 1.05 + l * .03, .5, .35, { lum: .95 });
      multi([[p.t, OR]], 1330, 190);
      S.texte(p.sous, W / 2, 1460, { taille: 62, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
    },
    pierre(p, t) {
      const lt = t - p.a;
      if (p.etape === 1) {
        const k = cl(lt / 1.6), x = lerp(120, 960, k), y = 1300 - Math.sin(k * Math.PI) * 750;
        for (let i = 1; i < 7; i++) { const kk = cl(k - i * .03), xx = lerp(120, 960, kk), yy = 1300 - Math.sin(kk * Math.PI) * 750; S.d.pierre(xx, yy, 70, kk * 9, { trait: 'rgba(239,230,210,' + (.3 - i * .04) + ')', ep: 6 }); }
        S.d.pierre(x, y, 80, k * 9, { trait: CREME, fond: '#5b5247', ep: 8 });
        multi([['UNE ', CREME], ['PIERRE', OR]], 1500, 140);
      } else {
        S.d.pierre(540, 760, 150, .3, { trait: CREME, fond: '#5b5247', ep: 10 });
        // bulle de pensée
        const k = back(pr(t, p.a, .35));
        g.save(); g.translate(540, 1140); g.scale(k, k);
        g.fillStyle = CREME; g.beginPath(); g.roundRect(-450, -120, 900, 240, 60); g.fill();
        [[-60, -160, 30], [-90, -215, 18]].forEach(([cx, cy, r]) => { g.beginPath(); g.arc(cx, cy, r, 0, 7); g.fill(); });
        S.texte(p.bulle, 0, 0, { taille: 56, police: 'Spectral', it: true, poids: 500, coul: NOIR, max: 820 });
        g.restore();
      }
    },
    causes(p, t) {
      S.d.tete(640, 900, 280, { trait: CREME, fond: '#1b1712', ep: 9 });
      const fl = [[-60, 640, ''], [-80, 900, ''], [-60, 1160, '']];
      fl.forEach(([x0, y0], i) => { const k = eo(pr(t, p.a + i * .15, .35)); S.d.fleche(x0, y0, 360, 860 + (i - 1) * 90, k, { trait: i === 1 ? ROUGE : OR, ep: 14 });
        if (k > .5) S.texte('?', 130, y0 - 60, { taille: 90, coul: i === 1 ? ROUGE : OR, contour: NOIR, contourL: 8 }); });
      multi([[p.t, OR]], 1400, 140);
      S.texte(p.sous, W / 2, 1520, { taille: 62, it: true, poids: 400, police: 'Spectral', coul: CREME });
    },
    stop(p, t) {
      const lt = t - p.a;
      // retour en arrière : bandes horizontales décalées
      g.save(); for (let i = 0; i < 18; i++) { const y = (i * 120 + lt * 2600) % H; g.fillStyle = i % 2 ? al(CREME, .06) : al(ROUGE, .08); g.fillRect(0, y, W, 50); } g.restore();
      S.texte('◀◀', W / 2, 700, { taille: 200, coul: CREME });
      const k = back(pr(t, p.a + .05, .25)); g.save(); g.translate(W / 2, 1000); g.scale(lerp(2.2, 1, k), lerp(2.2, 1, k));
      S.texte(p.t, 0, 0, { taille: 150, coul: ROUGE, contour: NOIR, contourL: 14, max: 960 }); g.restore();
    },
    bac(p, t) {
      const k = eo(pr(t, p.a, .4));
      g.save(); g.translate(W / 2, lerp(1500, 900, k)); g.rotate(-.04);
      g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-380, -480, 760, 960); g.shadowColor = 'transparent';
      S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
      S.texte(p.matiere || 'PHILOSOPHIE', 0, -315, { taille: 40, coul: GRIS, esp: 8, poids: 600 });
      g.fillStyle = NOIR; g.fillRect(-300, -260, 600, 3);
      S.texte('Sujet 1', -300, -180, { taille: 40, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400 });
      const suj = p.sujet || ['Sommes-nous libres', 'de nos choix ?'];
      S.texte(suj[0], 0, -80, { taille: 72, police: 'Spectral', poids: 600, coul: NOIR, max: 680 });
      S.texte(suj[1], 0, 10, { taille: 72, police: 'Spectral', poids: 600, coul: NOIR, max: 680 });
      for (let i = 0; i < 6; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-300, 120 + i * 50, 600 - (i === 5 ? 250 : 0), 6); }
      // cercle rouge au stylo
      const kc = pr(t, p.a + .35, .5); g.strokeStyle = ROUGE; g.lineWidth = 9; g.beginPath(); g.ellipse(0, -35, 360, 130, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
      g.restore();
      multi([['QUESTION DE ', CREME], ['BAC', ROUGE]], 1560, 110);
    },
    chaine(p, t) {
      const k = back(pr(t, p.a, .35));
      fondImg(p.fond || 'penseur', 1.2, .5, .4, .25);
      g.save(); g.translate(W / 2, 820); g.scale(k, k);
      S.d.lecture(0, -120, 110, CREME, ROUGE);
      g.restore();
      S.texte('RÉVISIONS', W / 2, 1010, { taille: 150, coul: CREME, contour: NOIR, contourL: 12 });
      S.texte('ANIMÉES', W / 2, 1150, { taille: 150, coul: OR, contour: NOIR, contourL: 12 });
      const k2 = eo(pr(t, p.a + .4, .4)); g.save(); g.globalAlpha = k2;
      S.texte(`la série « ${p.serie || 'La liberté'} » sur YouTube`, W / 2, 1280, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 980 });
      g.restore();
    },
  };

  // ---------------------------------------------------------------- image complète
  const SANS_ST = new Set(['mot', 'tampon', 'stop', 'date', 'chaine', 'bac', 'perso', 'portrait', ...(window.SANS_ST_A || []), ...(window.TYPES_FORMATS || [])]);
  function fond(t) {
    g.fillStyle = NOIR; g.fillRect(0, 0, W, H);
    if (TH.deco === 'carte') { g.drawImage(lignes, 0, 0); return; }
    g.save();
    if (TH.deco === 'grille') {  // grille en perspective qui défile + horizon lumineux
      const hz = 1180, gl = g.createLinearGradient(0, hz - 260, 0, hz + 40); gl.addColorStop(0, al(ROUGE, 0)); gl.addColorStop(1, al(ROUGE, .28));
      g.fillStyle = gl; g.fillRect(0, hz - 260, W, 300);
      g.strokeStyle = al(OR, .28); g.lineWidth = 3;
      for (let i = -12; i <= 12; i++) { g.beginPath(); g.moveTo(W / 2 + i * 40, hz); g.lineTo(W / 2 + i * 420, H); g.stroke(); }
      for (let j = 0; j < 14; j++) { const u = ((j + (t * 1.2) % 1) / 14) ** 2, y = hz + u * (H - hz); g.globalAlpha = .3 + u * .7; g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); }
    } else if (TH.deco === 'rayons') {  // rayons de plateau de jeu qui tournent
      g.translate(W / 2, 900); g.rotate(t * .12);
      for (let i = 0; i < 18; i++) { g.fillStyle = i % 2 ? al(GRIS, .1) : al(OR, .05); g.beginPath(); g.moveTo(0, 0); g.arc(0, 0, 1800, i * Math.PI / 9, (i + 1) * Math.PI / 9); g.closePath(); g.fill(); }
      g.setTransform(1, 0, 0, 1, 0, 0);
      const sp = g.createRadialGradient(W / 2, 900, 50, W / 2, 900, 800); sp.addColorStop(0, al(OR, .16)); sp.addColorStop(1, al(OR, 0)); g.fillStyle = sp; g.fillRect(0, 0, W, H);
    } else if (TH.deco === 'bandes') {  // bandes d'alerte qui glissent + bandeau défilant en bas
      g.globalAlpha = .07; g.fillStyle = OR; for (let i = -6; i < 30; i++) { const x = i * 120 + (t * 60) % 240; g.beginPath(); g.moveTo(x, 0); g.lineTo(x + 60, 0); g.lineTo(x + 60 - H * .4, H); g.lineTo(x - H * .4, H); g.fill(); }
      g.globalAlpha = 1; g.fillStyle = ROUGE; g.fillRect(0, 1790, W, 70);
      const msg = 'ALERTE RÉVISION  ●  RÉVISIONS ANIMÉES  ●  '; const lx = -(t * 220) % (S.largeur(msg, { taille: 36 }));
      for (let x = lx; x < W; x += S.largeur(msg, { taille: 36 })) S.texte(msg, x, 1827, { taille: 36, coul: CREME, align: 'left', poids: 700 });
    } else if (TH.deco === 'code') {  // colonnes de caractères + lignes de balayage
      g.font = '600 30px monospace';
      for (let c = 0; c < 27; c++) { const v = .4 + rnd(c * 7.1) * .9, y0 = ((t * v * 300 + rnd(c) * H) % (H + 600)) - 600;
        for (let k = 0; k < 14; k++) { g.fillStyle = al(OR, .03 + .1 * (k / 14)); g.fillText('01░▒ABΣ∆'[Math.floor(rnd(c * 31 + k + Math.floor(t * 8)) * 9)], c * 40 + 8, y0 + k * 42); } }
      g.fillStyle = 'rgba(0,0,0,.18)'; for (let y = 0; y < H; y += 6) g.fillRect(0, y, W, 2);
    }
    g.restore();
  }
  // entrée d'un plan : transformation (zoom, glisse, tourne, chute) ; glitch et iris sont faits après le dessin
  function entree(p) {
    if (p.trans) return p.trans;
    if (p.choc) return 'zoom';
    const L = TH.trans; return L[Math.floor(rnd(p.i * 13.7 + 3) * L.length)];
  }
  function scene(p, t, l, sx, sy, pulse) {
    const tr = entree(p), k = eo(pr(t, p.a, .24)), kb = back(pr(t, p.a, .3));
    let z = (1 + l * .012) * (1 + .055 * eo(S.coup(t))) * pulse, dx = 0, dy = 0, rot = 0;
    if (tr === 'zoom' || tr === 'glitch' || tr === 'iris') z *= lerp(1.1, 1, k);
    if (tr === 'glisse') dx = lerp((p.i % 2 ? 1 : -1) * W * .45, 0, kb);
    if (tr === 'tourne') { rot = lerp((p.i % 2 ? 1 : -1) * .14, 0, kb); z *= lerp(1.18, 1, kb); }
    if (tr === 'chute') dy = lerp(-H * .3, 0, kb);
    g.save(); g.translate(W / 2 + sx + dx, H / 2 + sy + dy); g.rotate(rot); g.scale(z, z); g.translate(-W / 2, -H / 2);
    R[p.type](p, t, l);
    g.restore();
  }
  function rendu(t) {
    const p = S.planA(t), l = t - p.a;
    fond(t);
    let sx = 0, sy = 0; if (p.choc && l < .35) { const a = (1 - l / .35) * 22; sx = (rnd(t * 99) - .5) * a; sy = (rnd(t * 77 + 3) - .5) * a; }
    // pulsation de caméra sur le temps de la musique (sauf dans l'accroche et après la relâche)
    const bpm = BPM[window.MUSIQUE] || 0, st = S.structure(), deb = (st.sections[1] || [1e9])[0], fin = st.relache ?? 1e9;
    const ph = bpm ? (t % (60 / bpm)) : 1, pulse = bpm && t > deb && t < fin ? 1 + .018 * Math.exp(-ph * 14) : 1;
    const tr = entree(p);
    if (tr === 'iris' && l < .32 && p.i > 0) {  // le plan précédent reste dessous, le nouveau s'ouvre en cercle
      const q = S.PLANS[p.i - 1]; scene(q, t, t - q.a, 0, 0, pulse);
      g.save(); g.beginPath(); g.arc(W / 2, H / 2, eo(l / .32) * 1150 + 1, 0, 7); g.clip(); fond(t); scene(p, t, l, sx, sy, pulse);
      g.strokeStyle = OR; g.lineWidth = 10; g.stroke(); g.restore();
    } else scene(p, t, l, sx, sy, pulse);
    if (tr === 'glitch' && l < .2) {  // tranches décalées + séparation des couleurs
      const cv = g.canvas, a = 1 - l / .2;
      for (let i = 0; i < 9; i++) { const y = Math.floor(rnd(i * 5.3 + Math.floor(t * 40)) * H), h = 30 + rnd(i * 2.1) * 120, d = (rnd(i * 9.7 + t) - .5) * 180 * a;
        g.drawImage(cv, 0, y, cv.width, h * cv.height / H, d, y * 1, W, h); }
      g.save(); g.globalCompositeOperation = 'screen'; g.globalAlpha = .35 * a; g.drawImage(cv, 12 * a, 0, W, H); g.restore();
    }
    // sous-titres
    const gr = S.groupeA(t);
    if (gr && !SANS_ST.has(p.type)) {
      const morceaux = []; gr.mots.forEach((m, i) => { const on = t >= m[0] - .02; morceaux.push([m[2].toUpperCase() + ' ', on ? (t < m[0] + m[1] + .05 ? OR : CREME) : al(CREME, .35)]); });
      multi(morceaux, 1660, 66, { max: 900 });
    }
    // vignette, grain, flash d'entrée
    const v = g.createRadialGradient(W / 2, H / 2, H * .25, W / 2, H / 2, H * .75);
    v.addColorStop(0, 'rgba(0,0,0,0)'); v.addColorStop(1, p.sombre ? 'rgba(0,0,0,.9)' : 'rgba(0,0,0,.6)'); g.fillStyle = v; g.fillRect(0, 0, W, H);
    g.drawImage(grain[Math.floor(t * 12) % 2], 0, 0, W, H);
    S.texte('RÉVISIONS ANIMÉES', W / 2, 150, { taille: 30, coul: al(OR, .75), esp: 12, poids: 600 });
    if (l < .07 && (p.choc || p.i % 3 === 0)) { g.fillStyle = al(CREME, (1 - l / .07) * (p.choc ? .9 : .4)); g.fillRect(0, 0, W, H); }
    if (t > S.D.dur - .25) { g.fillStyle = `rgba(0,0,0,${pr(t, S.D.dur - .25, .25)})`; g.fillRect(0, 0, W, H); }
  }

  // ---------------------------------------------------------------- sons (mix.py) : [instant, type, gain]
  function sons() {
    const L = [];
    S.PLANS.forEach(p => {
      // son de coupe : pas à chaque plan, varié et discret (les plans qui ont leur propre son n'en prennent pas)
      const propre = ['tampon', 'date', 'horloge', 'stop', 'pierre', 'eeg', 'bac', 'chaine', ...(window.PROPRES_A || []), ...(window.TYPES_FORMATS || [])].includes(p.type) || p.t2 || p.muet;
      if (p.choc) L.push([p.a, 'boum', 1]);
      else if (entree(p) === 'glitch' && p.i > 0) L.push([p.a, 'glitch', .35]);
      else if (!propre) { const v = [['papier', .22], null, ['clic', .3], ['frotte', .25], null][p.i % 5]; if (v) L.push([p.a, v[0], v[1]]); }
      if (p.type === 'tampon') L.push([p.a + .08, 'tampon', 1]);
      if (p.type === 'date') for (let k = 0; k < 10; k++) L.push([p.a + k * .06, 'tic', .5]);
      if (p.type === 'horloge' && !p.fige) for (let k = 0; k < Math.floor((p.b - p.a) / .25); k++) L.push([p.a + k * .25, 'tic', .45]);
      if (p.type === 'horloge' && p.fige) L.push([p.a + .2, 'tampon', .7]);
      if (p.t2) L.push([S.T(...p.a2) - .05, 'lame', .9]);
      if (p.type === 'frise' && p.etape === 3) L.push([p.a, 'coeur', 1], [p.a + .8, 'coeur', 1]);
      if (p.type === 'frise' && p.etape === 5) L.push([p.a + .08, 'tampon', 1]);
      if (p.type === 'stop') L.push([p.a, 'rembobine', .9]);
      if (p.type === 'pierre' && p.etape === 1) L.push([p.a, 'souffle', .9]);
      if (p.type === 'bac') L.push([p.a + .35, 'stylo', .6]);
      if (p.type === 'eeg') L.push([p.a, 'bip', .35]);
      if (p.bruit) L.push([p.a, 'statique', .5]);
      if (p.type === 'chaine') L.push([p.a, 'gong', .8]);
      if (window.SONS_A) window.SONS_A(p, L);
      if (window.SONS_FORMATS) window.SONS_FORMATS(p, L);
    });
    return Object.assign({ sons: L, musique: window.MUSIQUE || 'phonk_tension' }, S.structure());
  }

  window.MODELE = { images: window.IMAGES, init, rendu, sons };
})();
