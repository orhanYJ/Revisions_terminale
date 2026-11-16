// Plans propres au short « devinephilo » (« Devine le philosophe en 3 indices »), modèle A, habillage « terminal ».
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
window.SANS_ST_A = ['dossiers', 'dossier', 'score', 'trio'];
window.PROPRES_A = ['dossiers', 'dossier', 'scanner', 'score', 'trio'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const MONO = 'JetBrains Mono';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const claque = (s, y, ta, t, o) => { const k = back(pr(t, ta, .3)); if (k <= 0) return; g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
    S.texte(s, 0, 0, Object.assign({ taille: 100, coul: CREME, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };
  const deuxClaque = (txt, y, ta, t, taille = 110) => { const k = back(pr(t, ta, .3)); if (k <= 0) return; g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  // texte qui se tape au clavier (police à chasse fixe), curseur clignotant
  const tape = (s, x, y, ta, t, o = {}) => { if (t < ta) return; const n = Math.min(s.length, Math.floor((t - ta) / (o.vit || .045)));
    const cur = Math.floor(t * 3) % 2 ? '_' : ' ';
    S.texte(s.slice(0, n) + (n < s.length || o.curseur ? cur : ''), x, y, Object.assign({ taille: 56, police: MONO, poids: 500, coul: OR, align: 'left' }, o)); };
  // une chemise cartonnée (onglet + corps), centrée en (x, y)
  function chemise(x, y, w, h, c, a = .14) {
    g.save(); g.translate(x, y); g.fillStyle = al(c, a); g.strokeStyle = c; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-w / 2, -h / 2 + 30); g.lineTo(-w / 2, -h / 2); g.lineTo(-w / 2 + w * .38, -h / 2); g.lineTo(-w / 2 + w * .46, -h / 2 + 30);
    g.lineTo(w / 2, -h / 2 + 30); g.lineTo(w / 2, h / 2); g.lineTo(-w / 2, h / 2); g.closePath(); g.fill(); g.stroke(); g.restore();
  }

  // trois dossiers secrets « ? » ; p.fin : un quatrième dossier, verrouillé
  function dossiers(p, t) {
    if (!p.fin) {
      claque('DEVINE', 400, p.a + .05, t, { taille: 170, coul: OR, contourL: 14 });
      claque('LE PHILOSOPHE', 540, p.a + .15, t, { taille: 110 });
      [230, 540, 850].forEach((x, i) => {
        const k = back(pr(t, p.a + .3 + i * .15, .3)); if (k <= 0) return;
        g.save(); g.translate(x, 930); g.scale(k, k); g.rotate((i - 1) * .06); g.translate(-x, -930);
        chemise(x, 930, 270, 220, OR);
        S.texte('TOP SECRET', x, 870, { taille: 26, coul: ROUGE, esp: 4, police: MONO, poids: 500 });
        S.texte('?', x, 960, { taille: 130, coul: CREME, police: 'Spectral', poids: 600 }); g.restore();
      });
      if (t > p.a + .8) deuxClaque('EN 3|INDICES', 1340, p.a + .8, t, 130);
    } else {
      const k = back(pr(t, p.a, .35)), pulse = 1 + .04 * Math.sin((t - p.a) * 7);
      g.save(); g.translate(W / 2, 860); g.scale(k * pulse, k * pulse); g.translate(-W / 2, -860);
      chemise(W / 2, 860, 600, 460, OR);
      S.texte('DOSSIER 4', W / 2, 740, { taille: 60, coul: OR, police: MONO, poids: 500, esp: 6 });
      S.texte('?', W / 2, 900, { taille: 240, coul: CREME, police: 'Spectral', poids: 600 }); g.restore();
      O.tampon('VERROUILLÉ', W / 2, 1110, pr(t, p.a + .3, .3), -.1, 70, ROUGE);
      deuxClaque('EN COMBIEN|D’INDICES ?', 1380, p.a + .5, t, 110);
    }
  }

  // le scanner : une silhouette analysée ligne à ligne
  function scanner(p, t) {
    const lt = t - p.a, x = 240, y = 430, w = 600, h = 760;
    g.save(); g.strokeStyle = al(OR, .25); g.lineWidth = 2;
    for (let i = 1; i < 8; i++) { g.beginPath(); g.moveTo(x, y + i * h / 8); g.lineTo(x + w, y + i * h / 8); g.stroke(); g.beginPath(); g.moveTo(x + i * w / 8, y); g.lineTo(x + i * w / 8, y + h); g.stroke(); }
    g.strokeStyle = OR; g.lineWidth = 6; g.strokeRect(x, y, w, h); g.restore();
    S.d.tete(W / 2 + 20, y + h / 2 + 20, 250, { trait: CREME, fond: NOIR, ep: 8 });
    S.texte('?', W / 2 + 40, y + h / 2 - 20, { taille: 220, coul: OR, police: 'Spectral', poids: 600 });
    const u = (lt * .9) % 1, yl = y + (u < .5 ? u * 2 : 2 - u * 2) * h;
    g.save(); g.fillStyle = al(OR, .25); g.fillRect(x, yl - 30, w, 60); g.fillStyle = OR; g.fillRect(x, yl - 3, w, 6); g.restore();
    const pct = Math.min(99, Math.round(eo(pr(t, p.a, 2.2)) * 99));
    tape('ANALYSE… ' + pct + ' %', x, y + h + 70, p.a, t, { taille: 48, vit: .02 });
    deuxClaque('TROUVE-LE|LE PLUS TÔT', 1420, p.a + .1, t, 110);
  }

  // un dossier s'ouvre : « DOSSIER n / 3 », tampon, « ACCÈS AUTORISÉ » tapé au clavier
  function dossier(p, t) {
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 900); g.scale(k, k); g.translate(-W / 2, -900);
    chemise(W / 2, 900, 820, 640, OR, .1);
    // feuille qui sort de la chemise
    const kf = eo(pr(t, p.a + .15, .4)), yf = lerp(1000, 880, kf);
    g.fillStyle = al(CREME, .92); g.fillRect(W / 2 - 330, yf - 230, 660, 420);
    S.texte('DOSSIER ' + p.n + ' / 3', W / 2, yf - 160, { taille: 64, coul: NOIR, police: MONO, poids: 500 });
    for (let i = 0; i < 5; i++) { const kb = eo(pr(t, p.a + .3 + i * .08, .25)); g.fillStyle = NOIR; g.fillRect(W / 2 - 280, yf - 80 + i * 52, (i % 2 ? 420 : 560) * kb, 26); }
    g.restore();
    O.tampon('CONFIDENTIEL', W / 2 + 120, 640, pr(t, p.a + .25, .3), .12, 64, ROUGE);
    tape('> ACCÈS AUTORISÉ', 250, 1340, p.a + .45, t, { taille: 60, curseur: true });
    for (let i = 0; i < 3; i++) { g.fillStyle = i < p.n ? OR : al(CREME, .2); g.beginPath(); g.arc(W / 2 - 100 + i * 100, 1480, 20, 0, 7); g.fill(); }
  }

  // le score : trois cases qui hésitent entre ✓ et ✗, « ? / 3 »
  function score(p, t) {
    deuxClaque('COMBIEN TU EN AS|TROUVÉ ?', 430, p.a + .05, t, 110);
    [230, 540, 850].forEach((x, i) => {
      const k = back(pr(t, p.a + .2 + i * .12, .3)); if (k <= 0) return;
      const ok = Math.floor((t - p.a) * 4 + i * 1.7) % 2 === 0;
      g.save(); g.translate(x, 850); g.scale(k, k);
      g.fillStyle = al(ok ? OR : ROUGE, .15); g.strokeStyle = ok ? OR : ROUGE; g.lineWidth = 8;
      g.beginPath(); g.roundRect(-120, -120, 240, 240, 26); g.fill(); g.stroke();
      S.texte(ok ? '✓' : '✗', 0, 8, { taille: 160, coul: ok ? OR : ROUGE }); g.restore();
    });
    claque('? / 3', 1160, p.a + .5, t, { taille: 200, coul: CREME, police: 'Spectral', poids: 600, contourL: 12 });
    if (p.dis) tape('> DIS-LE EN COMMENTAIRE', 150, 1400, tps(p.dis), t, { taille: 52, vit: .03, curseur: true });
  }

  // les trois philosophes démasqués
  function trio(p, t) {
    const L = [['socrate', 'SOCRATE', 'v. 470 – 399 av. J.-C.'], ['spinoza', 'SPINOZA', '1632 – 1677'], ['kant', 'KANT', '1724 – 1804']];
    L.forEach(([img, nom, d], i) => {
      const k = back(pr(t, p.a + i * .15, .35)); if (k <= 0) return;
      const x = 200 + i * 340, y = 800;
      g.save(); g.translate(x, lerp(y + 600, y, k)); g.rotate((i - 1) * .05);
      O.carte(img, 0, 0, 290, 380, 0, 1.05, .5, .35); g.restore();
      const kn = eo(pr(t, p.a + .3 + i * .15, .3)); g.save(); g.globalAlpha = kn;
      S.texte(nom, x, 1060, { taille: 58, coul: OR, max: 320 });
      S.texte(d, x, 1120, { taille: 32, police: MONO, poids: 500, coul: CREME, max: 320 }); g.restore();
    });
    deuxClaque('TOUS EXPLIQUÉS|EN VIDÉO', 1380, p.a + .6, t, 110);
  }

  return { dossiers, scanner, dossier, score, trio };
};
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'dossiers' && !p.fin) [0, 1, 2].forEach(i => L.push([p.a + .3 + i * .15, 'pop', .5]));
  if (p.type === 'dossiers' && p.fin) L.push([p.a, 'whoosh', .5], [p.a + .3, 'tampon', .8]);
  if (p.type === 'scanner') { L.push([p.a, 'statique', .35]); for (let x = .2; x < 1.8; x += .45) L.push([p.a + x, 'bip', .35]); }
  if (p.type === 'dossier') { L.push([p.a, 'papier', .6], [p.a + .25, 'tampon', .8]); for (let k = 0; k < 6; k++) L.push([p.a + .45 + k * .1, 'clic', .35]); }
  if (p.type === 'score') { [0, 1, 2].forEach(i => L.push([p.a + .2 + i * .12, 'pop', .5])); L.push([p.a + .5, 'blip', .7]); if (p.dis) L.push([tps(p.dis), 'clic', .4]); }
  if (p.type === 'trio') [0, 1, 2].forEach(i => L.push([p.a + i * .15, 'pop', .5]));
};
