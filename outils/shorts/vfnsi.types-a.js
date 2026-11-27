// Plans propres au short « NSI : vrai ou faux ? ». O = outils du modèle (carte, multi, tampon, barreRouge,
// petitTitre, fondImg, al, C = couleurs). Couleurs : uniquement O.C et O.al (l'habillage néon les remplace).
// Les plans vraifaux, photo, collage, portrait, mot et date sont communs (formats-a.js, modele-a.js).
window.SANS_ST_A = ['photo', 'collage', 'chrono', 'reseau', 'ip', 'arret', 'commentaire'];
window.PROPRES_A = ['chrono', 'reseau', 'ip', 'arret', 'commentaire'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al, MONO = 'JetBrains Mono';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  // texte à chasse fixe dessiné caractère par caractère (pas de ligature), aligné à gauche
  const mono = (s, x, y, o = {}) => {
    const q = Object.assign({ taille: 48, police: MONO, poids: 500, coul: CREME }, o, { align: 'left', max: undefined });
    const adv = S.largeur('M', q); [...s].forEach((c, i) => { if (c !== ' ') S.texte(c, x + i * adv, y, q); });
    return adv * s.length;
  };
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };

  // chronomètre « top chrono »
  function chrono(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = al(NOIR, .9); g.strokeStyle = CREME; g.lineWidth = 12;
    g.fillRect(-40, -390, 80, 50); g.strokeRect(-40, -390, 80, 50);
    g.beginPath(); g.arc(0, 0, 320, 0, 7); g.fill(); g.stroke();
    g.strokeStyle = OR; g.lineWidth = 8;
    for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; g.beginPath(); g.moveTo(Math.sin(a) * 280, -Math.cos(a) * 280); g.lineTo(Math.sin(a) * 240, -Math.cos(a) * 240); g.stroke(); }
    const a = lt * 4; g.strokeStyle = ROUGE; g.lineWidth = 12; g.lineCap = 'round'; g.beginPath(); g.moveTo(0, 0); g.lineTo(Math.sin(a) * 250, -Math.cos(a) * 250); g.stroke();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 22, 0, 7); g.fill();
    g.restore();
    O.multi([['TOP ', CREME], ['CHRONO', OR]], 1410, 150);
  }

  // Internet = le réseau (routeurs reliés, paquets qui circulent) ; le Web (repère web) et le mail (repère mail) = des services posés dessus
  const NOEUDS = [[200, 640], [470, 560], [780, 640], [330, 880], [640, 860], [900, 930], [210, 1110], [520, 1110], [820, 1170]];
  const LIENS = [[0, 1], [1, 2], [0, 3], [1, 4], [2, 4], [2, 5], [3, 4], [4, 5], [3, 6], [3, 7], [4, 7], [5, 8], [7, 8], [6, 7]];
  function reseau(p, t) {
    const tw = p.web ? tps(p.web) : 1e9, web = t >= tw, tm = p.mail ? tps(p.mail) : tw + .25, k = eo(pr(t, p.a, .5));
    g.save(); g.globalAlpha = web ? .55 : 1;
    LIENS.forEach(([i, j], n) => { const [x0, y0] = NOEUDS[i], [x1, y1] = NOEUDS[j], u = cl(k * 1.6 - n * .04);
      g.strokeStyle = al(OR, .6); g.lineWidth = 6; g.beginPath(); g.moveTo(x0, y0); g.lineTo(lerp(x0, x1, u), lerp(y0, y1, u)); g.stroke(); });
    // paquets
    LIENS.forEach(([i, j], n) => { const u = ((t - p.a) * .9 + rnd(n * 3.1)) % 1, [x0, y0] = NOEUDS[i], [x1, y1] = NOEUDS[j];
      if (k >= 1) { g.fillStyle = ROUGE; g.beginPath(); g.arc(lerp(x0, x1, u), lerp(y0, y1, u), 10, 0, 7); g.fill(); } });
    NOEUDS.forEach(([x, y], n) => { const kn = back(pr(t, p.a + n * .05, .3)); g.save(); g.translate(x, y); g.scale(kn, kn);
      g.fillStyle = NOIR; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(0, 0, 34, 0, 7); g.fill(); g.stroke();
      g.fillStyle = CREME; g.fillRect(-14, -4, 28, 8); g.restore(); });
    g.restore();
    if (!web) { O.petitTitre('— DES MILLIARDS DE MACHINES RELIÉES —', 420); titrePop('INTERNET|LE RÉSEAU', 1420, t, p.a, 116); return; }
    O.petitTitre('— DES SERVICES POSÉS DESSUS —', 420);
    // le Web : une fenêtre de navigateur ; le mail : une enveloppe
    const kw = back(pr(t, tw, .3)), km = back(pr(t, tm, .3));
    g.save(); g.translate(330, 760); g.scale(kw, kw);
    g.fillStyle = al(NOIR, .92); g.strokeStyle = OR; g.lineWidth = 7; g.beginPath(); g.roundRect(-170, -120, 340, 240, 18); g.fill(); g.stroke();
    g.fillStyle = al(OR, .25); g.fillRect(-170, -120, 340, 50);
    [0, 1, 2].forEach(i => { g.fillStyle = OR; g.beginPath(); g.arc(-140 + i * 30, -95, 9, 0, 7); g.fill(); });
    S.texte('WEB', 0, 30, { taille: 90, coul: OR }); g.restore();
    g.save(); g.translate(760, 820); g.scale(km, km);
    g.fillStyle = al(NOIR, .92); g.strokeStyle = CREME; g.lineWidth = 7; g.beginPath(); g.rect(-150, -100, 300, 200); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(-150, -100); g.lineTo(0, 20); g.lineTo(150, -100); g.stroke();
    S.texte('MAIL', 0, 145, { taille: 56, coul: CREME }); g.restore();
    titrePop(t >= tm ? 'COMME LE MAIL|UN SERVICE D’INTERNET' : 'LE WEB|UN SERVICE D’INTERNET', 1420, t, t >= tm ? tm : tw, 100);
  }

  // une adresse IPv4 : 4 octets de 8 bits, puis 2 puissance 32 adresses
  function ip(p, t) {
    const O8 = [192, 168, 0, 1];
    O.petitTitre('— UNE ADRESSE IPv4 —', 400);
    O8.forEach((v, i) => {
      const x = i % 2 ? 790 : 290, y = i < 2 ? 640 : 940, ki = back(pr(t, p.a + i * .18, .3)); if (ki <= 0) return;
      g.save(); g.translate(x, y); g.scale(ki, ki);
      g.fillStyle = al(OR, .1); g.strokeStyle = OR; g.lineWidth = 5; g.beginPath(); g.roundRect(-235, -95, 470, 190, 18); g.fill(); g.stroke();
      const b = v.toString(2).padStart(8, '0'), adv = S.largeur('M', { taille: 54, police: MONO, poids: 500 });
      mono(b, -adv * 4, -30, { taille: 54, coul: CREME });
      S.texte(String(v), 0, 50, { taille: 56, coul: OR, police: MONO, poids: 500 });
      g.restore();
      S.texte('octet ' + (i + 1), x, y - 125, { taille: 34, coul: GRIS, poids: 600 });
    });
    const ka = eo(pr(t, p.a + .9, .3)); g.save(); g.globalAlpha = ka;
    S.texte('192.168.0.1', W / 2, 1150, { taille: 80, coul: CREME, police: MONO, poids: 500 }); g.restore();
    titrePop('4 × 8 = 32 BITS|4 294 967 296 ADRESSES', 1420, t, p.a + 1.2, 96);
  }

  // le problème de l'arrêt : un programme qui tourne, la question « s'arrête ? » sans réponse sûre
  function arret(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 760); g.scale(k, k); g.translate(-W / 2, -760);
    g.fillStyle = al(NOIR, .92); g.strokeStyle = OR; g.lineWidth = 5; g.beginPath(); g.roundRect(120, 520, 840, 420, 22); g.fill(); g.stroke();
    g.fillStyle = al(OR, .16); g.fillRect(120, 520, 840, 64);
    S.texte('programme.py', W / 2, 553, { taille: 30, coul: GRIS, police: MONO, poids: 500 });
    mono('def P(x):', 180, 660, { taille: 50 });
    mono('...  # n’importe quoi', 260, 740, { taille: 50, coul: GRIS });
    mono('P(x)  # va-t-il finir ?', 180, 840, { taille: 50, coul: OR });
    // roue qui tourne : le programme calcule encore
    g.save(); g.translate(900, 660); g.rotate(lt * 6); g.strokeStyle = ROUGE; g.lineWidth = 10; g.lineCap = 'round';
    g.beginPath(); g.arc(0, 0, 38, 0, 4.6); g.stroke(); g.restore();
    g.restore();
    const kq = back(pr(t, p.a + .4, .3)); g.save(); g.translate(W / 2, 1080); g.scale(kq, kq);
    S.texte('S’ARRÊTE ?', 0, 0, { taille: 110, coul: CREME, contour: NOIR, contourL: 10 }); g.restore();
    [['OUI', 330], ['NON', 750]].forEach(([s, x], i) => { const ko = eo(pr(t, p.a + .6 + i * .1, .3)); g.save(); g.globalAlpha = ko * (.5 + .5 * Math.abs(Math.sin(lt * 5 + i * 1.6)));
      g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.roundRect(x - 150, 1180, 300, 120, 24); g.stroke(); S.texte(s + ' ?', x, 1242, { taille: 64, coul: OR }); g.restore(); });
    O.tampon('AUCUN PROGRAMME', W / 2, 1460, pr(t, p.a + 1.1, .3), -.07, 84, ROUGE);
  }

  // une bulle de commentaire qui s'écrit
  function commentaire(p, t) {
    const k = back(pr(t, p.a, .3)), txt = 'Mon score : … / 5', n = Math.floor(cl((t - p.a - .5) / .8) * txt.length);
    O.multi([['ALORS, TON ', CREME], ['SCORE ?', OR]], 480, 120);
    g.save(); g.translate(W / 2, 880); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-430, -170, 860, 340, 50); g.fill();
    g.beginPath(); g.moveTo(-300, 165); g.lineTo(-340, 260); g.lineTo(-220, 165); g.fill();
    g.fillStyle = OR; g.beginPath(); g.arc(-330, -60, 50, 0, 7); g.fill();
    S.texte('toi', -230, -60, { taille: 44, coul: GRIS, align: 'left', poids: 600 });
    S.texte(txt.slice(0, n), -360, 60, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, align: 'left', max: 760 });
    const kc = pr(t, p.a + 1.4, .3); if (kc > 0) { g.save(); g.translate(350, -80); g.scale(back(kc), back(kc)); g.fillStyle = ROUGE;
      g.beginPath(); g.moveTo(0, 30); g.bezierCurveTo(-60, -10, -30, -60, 0, -30); g.bezierCurveTo(30, -60, 60, -10, 0, 30); g.fill(); g.restore(); }
    g.restore();
    deux('DIS TON SCORE|EN COMMENTAIRE', 1380, 110);
  }

  return { chrono, reseau, ip, arret, commentaire };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono') L.push([p.a, 'clic', .7], [p.a + .3, 'tic', .5], [p.a + .6, 'tic', .5]);
  if (p.type === 'reseau') { L.push([p.a, 'whoosh', .4]); if (p.web) L.push([tps(p.web), 'pop', .5]); if (p.mail) L.push([tps(p.mail), 'pop', .5]); }
  if (p.type === 'ip') { for (let i = 0; i < 4; i++) L.push([p.a + i * .18, 'blip', .35]); L.push([p.a + 1.2, 'valide', .5]); }
  if (p.type === 'arret') { L.push([p.a, 'bip', .35]); L.push([p.a + 1.1, 'tampon', .9]); }
  if (p.type === 'commentaire') { L.push([p.a, 'pop', .6]); for (let k = 0; k < 8; k++) L.push([p.a + .5 + k * .1, 'tic', .25]); L.push([p.a + 1.4, 'pop', .5]); }
};
