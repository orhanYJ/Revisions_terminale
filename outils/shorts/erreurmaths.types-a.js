// Plans propres au short « erreurmaths » (trouve l'erreur dans trois copies de maths), modèle A, habillage archives.
// Couleurs : uniquement O.C (NOIR, CREME, OR, ROUGE, GRIS) et O.al(couleur, opacité), pour suivre l'habillage.
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, photo, al, C).
// Formules : seulement des caractères présents dans Archivo et Spectral ; le signe infini est dessiné (infini()).
window.SANS_ST_A = ['photo', 'collage', 'copies', 'pret', 'manche', 'regle', 'facteur', 'retenir', 'fi', 'facto', 'courbe', 'score'];
window.PROPRES_A = ['copies', 'pret', 'manche', 'regle', 'facteur', 'retenir', 'fi', 'facto', 'courbe', 'score'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const al = O.al;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 110) => { const k = back(pr(t, a, .3)); g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const ligne = (x0, y0, x1, y1, c, ep = 6, tirets) => { g.save(); g.strokeStyle = c; g.lineWidth = ep; g.lineCap = 'round'; if (tirets) g.setLineDash(tirets);
    g.beginPath(); g.moveTo(x0, y0); g.lineTo(x1, y1); g.stroke(); g.restore(); };
  const formule = (s, x, y, taille, coul = CREME, o = {}) => S.texte(s, x, y, Object.assign({ taille, coul, police: 'Spectral', poids: 600, max: 980 }, o));
  const pop = (t, a, d = .3) => back(pr(t, a, d));
  // le signe infini, dessiné (absent des polices) : lemniscate centrée en (x, y), demi-largeur r
  function infini(x, y, r, coul, ep = 10, k = 1) {
    g.save(); g.strokeStyle = coul; g.lineWidth = ep; g.lineCap = 'round'; g.beginPath();
    for (let i = 0; i <= 80 * k; i++) { const a = i / 80 * 2 * Math.PI, d = 1 + Math.sin(a) ** 2;
      const px = x + r * Math.cos(a) / d, py = y + r * .9 * Math.sin(a) * Math.cos(a) / d; i ? g.lineTo(px, py) : g.moveTo(px, py); }
    g.stroke(); g.restore();
  }
  // feuille de copie : fond crème, lignes, marge rouge, gribouillis d'écriture
  function feuille(w, h, n = 6, rouge = -1) {
    g.shadowColor = al(NOIR, .7); g.shadowBlur = 30; g.fillStyle = CREME; g.fillRect(-w / 2, -h / 2, w, h); g.shadowColor = 'transparent';
    g.strokeStyle = al(ROUGE, .5); g.lineWidth = 3; g.beginPath(); g.moveTo(-w / 2 + w * .16, -h / 2); g.lineTo(-w / 2 + w * .16, h / 2); g.stroke();
    for (let i = 0; i < n; i++) {
      const y = -h / 2 + h * .25 + i * h * .7 / n, l = w * (.55 + rnd(i * 3.7 + w) * .22);
      g.strokeStyle = i === rouge ? ROUGE : al(NOIR, .55); g.lineWidth = 5; g.beginPath(); g.moveTo(-w / 2 + w * .22, y);
      for (let x = 0; x < l; x += 14) g.lineTo(-w / 2 + w * .22 + x, y + Math.sin(x * .35 + i) * 4);
      g.stroke();
    }
  }

  // trois copies qui tombent en éventail ; chacune a une ligne entourée de rouge et un « ? »
  function copies(p, t) {
    const L = [['LOG', -320, 760, -.14], ['EXP', 0, 700, .02], ['LIMITES', 320, 760, .14]];
    L.forEach(([nom, dx, y, r], i) => {
      const k = back(pr(t, p.a + i * .14, .35)); if (k <= 0) return;
      g.save(); g.translate(W / 2 + dx, lerp(-500, y, k)); g.rotate(r * (2 - k));
      feuille(330, 460, 6, 3);
      S.texte(nom, 0, -180, { taille: 40, coul: NOIR, esp: 4, max: 290 });
      const kc = pr(t, p.a + .5 + i * .15, .4);
      g.strokeStyle = ROUGE; g.lineWidth = 7; g.beginPath(); g.ellipse(0, 70, 150, 34, -.05, -1.5, -1.5 + kc * 6.6); g.stroke();
      if (kc > .9) S.texte('?', 120, 150, { taille: 90, coul: ROUGE });
      g.restore();
    });
    titrePop(p.t, 1320, t, p.a + .5, 120);
  }

  // « ON JOUE ! » : cercle de départ qui se remplit, trois points qui s'allument
  function pret(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 820); g.scale(k, k);
    g.strokeStyle = al(CREME, .18); g.lineWidth = 30; g.beginPath(); g.arc(0, 0, 260, 0, 7); g.stroke();
    g.strokeStyle = OR; g.lineCap = 'round'; g.beginPath(); g.arc(0, 0, 260, -Math.PI / 2, -Math.PI / 2 + eo(cl(lt / 1.1)) * 6.283); g.stroke();
    for (let i = 0; i < 3; i++) { const on = lt > .2 + i * .25; g.fillStyle = on ? (i === 2 ? ROUGE : OR) : al(CREME, .2); g.beginPath(); g.arc((i - 1) * 120, 0, 42, 0, 7); g.fill(); }
    g.restore();
    const kt = back(pr(t, p.a + .5, .3)); g.save(); g.translate(W / 2, 1300); g.scale(lerp(2, 1, kt), lerp(2, 1, kt)); g.globalAlpha = cl(kt * 2);
    S.texte(p.t, 0, 0, { taille: 160, coul: OR, contour: NOIR, contourL: 14, max: 960 }); g.restore();
  }

  // petits dessins de manche : courbe du logarithme, de l'exponentielle, signe infini
  function dessin(nom, t) {
    g.lineCap = 'round'; g.lineJoin = 'round';
    if (nom === 'infini') { infini(0, 0, 170, OR, 16, cl((t % 3) / 1.2)); return; }
    ligne(-180, 120, 190, 120, al(CREME, .6), 5); ligne(-150, 170, -150, -190, al(CREME, .6), 5);
    g.strokeStyle = nom === 'log' ? OR : ROUGE; g.lineWidth = 12; g.beginPath();
    for (let i = 0; i <= 60; i++) {
      const u = i / 60;
      const [px, py] = nom === 'log' ? [-140 + u * 320, 120 - (Math.log(.15 + u * 6) + 1.9) * 62] : [-170 + u * 340, 120 - Math.exp(-2 + u * 3.6) * 9];
      i ? g.lineTo(px, Math.max(-190, py)) : g.moveTo(px, py);
    }
    g.stroke();
    S.texte(nom === 'log' ? 'ln' : 'exp', 90, nom === 'log' ? 120 + 60 : 20, { taille: 56, coul: CREME, police: 'Spectral', it: true, poids: 600 });
  }
  // carte « MANCHE n / 3 » avec le thème et un dessin
  function manche(p, t) {
    const k = back(pr(t, p.a, .35));
    S.texte('MANCHE', W / 2, 420, { taille: 70, coul: CREME, esp: 18 });
    g.save(); g.translate(W / 2, 640); g.scale(lerp(2.4, 1, k), lerp(2.4, 1, k)); g.globalAlpha = cl(k * 2);
    S.texte(p.n + ' / 3', 0, 0, { taille: 250, police: 'Spectral', poids: 600, coul: OR, ombre: al(OR, .45), flou: 40 }); g.restore();
    const kd = eo(pr(t, p.a + .2, .4)); g.save(); g.translate(W / 2, 1100); g.scale(kd, kd); g.rotate(lerp(-.5, 0, kd));
    g.fillStyle = al(CREME, .06); g.beginPath(); g.arc(0, 0, 250, 0, 7); g.fill(); g.strokeStyle = al(OR, .5); g.lineWidth = 4; g.stroke();
    dessin(p.dessin, t); g.restore();
    const kb = eo(pr(t, p.a + .1, .3)); g.save(); g.translate(lerp(-W, 0, kb), 0);
    g.fillStyle = ROUGE; g.fillRect(0, 1420, W, 130); S.texte(p.matiere, W / 2, 1487, { taille: 90, coul: CREME, esp: 6, max: 980 }); g.restore();
  }

  // la règle du logarithme : le produit devient une somme ; ln(3 + 4) = ln(7), puis ln(3) + ln(4) = ln(12)
  function regle(p, t) {
    const t2 = tps(p.e2);
    O.petitTitre('LA SEULE RÈGLE', 400);
    g.save(); g.translate(W / 2, 590); g.fillStyle = al(OR, .12); g.beginPath(); g.roundRect(-470, -95, 940, 190, 26); g.fill();
    g.strokeStyle = OR; g.lineWidth = 5; g.stroke(); formule('ln(a × b) = ln(a) + ln(b)', 0, 4, 86, OR); g.restore();
    const k1 = pop(t, p.a + .1, .3);
    if (k1 > 0) { g.save(); g.translate(W / 2, 900); g.scale(k1, k1); formule('ln(3 + 4) = ln(7)', 0, 0, 104, CREME, { contour: NOIR, contourL: 8 }); g.restore(); }
    if (t >= t2) {
      const k2 = pop(t, t2 + .1, .3); g.save(); g.translate(W / 2, 1110); g.scale(k2, k2);
      formule('ln(3) + ln(4) = ln(3 × 4) = ln(12)', 0, 0, 76, CREME, { contour: NOIR, contourL: 8, max: 940 }); g.restore();
      const k3 = eo(pr(t, t2 + .7, .3)); g.save(); g.globalAlpha = k3;
      S.texte('7 ET 12 : PAS LE MÊME NOMBRE', W / 2, 1300, { taille: 64, coul: ROUGE, contour: NOIR, contourL: 8, max: 960 }); g.restore();
    }
    titrePop('PAS DE RÈGLE|POUR ln(a + b)', 1560, t, p.a + .4, 84);
  }

  // f(x) = exp(2x) : u = 2x, u′ = 2, le facteur 2 qui manquait tombe devant
  function facteur(p, t) {
    O.petitTitre('LA DÉRIVÉE DE exp(u)', 400);
    const L = [['u(x) = 2x', CREME, 0], ['u′(x) = 2', OR, .35], ['f′(x) = u′(x) × exp(u(x))', CREME, .7]];
    L.forEach(([s, c, d], i) => { const k = eo(pr(t, p.a + d, .3)); if (k <= 0) return; g.save(); g.globalAlpha = k; g.translate(lerp(-200, 0, k), 0);
      formule(s, W / 2, 620 + i * 160, 84, c); g.restore(); });
    const k4 = pop(t, p.a + 1.1, .35);
    if (k4 > 0) { g.save(); g.translate(W / 2, 1180); g.scale(k4, k4);
      g.fillStyle = al(CREME, .92); g.beginPath(); g.roundRect(-430, -100, 860, 200, 24); g.fill();
      formule('f′(x) = ', -120, 4, 92, NOIR, { align: 'right' }); formule('2', -70, 4, 112, ROUGE); formule(' exp(2x)', -30, 4, 92, NOIR, { align: 'left' });
      g.restore(); }
    titrePop('IL MANQUAIT|LE FACTEUR 2', 1450, t, p.a + 1.3, 100);
  }

  // fiche « à retenir » : (exp u)′ = u′ × exp u, coup de tampon
  function retenir(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1400, 860, k)); g.rotate(-.025);
    g.shadowColor = al(NOIR, .7); g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-440, -380, 880, 760); g.shadowColor = 'transparent';
    g.strokeStyle = al(ROUGE, .45); g.lineWidth = 3; g.beginPath(); g.moveTo(-340, -380); g.lineTo(-340, 380); g.stroke();
    S.texte('FICHE · DÉRIVÉES', 0, -300, { taille: 40, coul: NOIR, esp: 6 });
    formule('( exp(u) )′', 0, -120, 100, NOIR);
    formule('= u′ × exp(u)', 0, 40, 100, NOIR);
    const ks = eo(pr(t, p.a + .9, .4)); g.strokeStyle = ROUGE; g.lineWidth = 7; g.beginPath(); g.moveTo(-300, 120); g.lineTo(-300 + 600 * ks, 114); g.stroke();
    formule('exemple : (exp(2x))′ = 2 exp(2x)', 0, 230, 54, GRIS, { it: true, poids: 500, max: 800 });
    g.restore();
    O.tampon('À RETENIR', W / 2, 1450, pr(t, p.a + 1.2, .3), -.08, 110, ROUGE);
  }

  // + infini − infini : « = 0 » barré, puis le tampon FORME INDÉTERMINÉE
  function fi(p, t) {
    const t2 = tps(p.e2), k = pop(t, p.a, .3);
    O.petitTitre('LE PIÈGE', 400);
    g.save(); g.translate(W / 2, 720); g.scale(k, k);
    S.texte('+', -380, 0, { taille: 130, coul: CREME }); infini(-220, 0, 120, OR, 14);
    S.texte('−', 0, 0, { taille: 130, coul: CREME }); infini(170, 0, 120, OR, 14);
    g.restore();
    const kz = eo(pr(t, p.a + .4, .3)); g.save(); g.globalAlpha = kz; S.texte('= 0 ?', W / 2, 960, { taille: 150, coul: CREME, police: 'Spectral', poids: 600 }); g.restore();
    const kb = eo(pr(t, p.a + .9, .25)); if (kb > 0) ligne(W / 2 - 200, 990, W / 2 - 200 + 400 * kb, 930, ROUGE, 16);
    if (t >= t2) O.tampon('FORME INDÉTERMINÉE', W / 2, 1300, pr(t, t2, .3), -.07, 80, ROUGE);
    else { const ke = eo(pr(t, p.a + 1.1, .3)); g.save(); g.globalAlpha = ke; S.texte('ÇA NE FAIT PAS 0', W / 2, 1300, { taille: 96, coul: ROUGE, contour: NOIR, contourL: 10, max: 960 }); g.restore(); }
  }

  // factorisation : x² − x = x(x − 1), chaque facteur tend vers + infini
  function facto(p, t) {
    O.petitTitre('ON FACTORISE PAR x', 400);
    const k1 = eo(pr(t, p.a, .3)); g.save(); g.globalAlpha = k1; formule('x² − x', W / 2, 640, 130, CREME); g.restore();
    const k2 = pop(t, p.a + .35, .35);
    if (k2 > 0) { g.save(); g.translate(W / 2, 860); g.scale(k2, k2); formule('= x × (x − 1)', 0, 0, 130, OR, { contour: NOIR, contourL: 10 }); g.restore(); }
    const k3 = eo(pr(t, p.a + .8, .3));
    if (k3 > 0) { g.save(); g.globalAlpha = k3;
      [[330, 'x'], [700, 'x − 1']].forEach(([x, s]) => { ligne(x, 960, x, 1120 * k3 + 960 * (1 - k3), ROUGE, 8);
        g.fillStyle = ROUGE; g.beginPath(); g.moveTo(x, 1150); g.lineTo(x - 22, 1112); g.lineTo(x + 22, 1112); g.fill();
        S.texte('+', x - 60, 1230, { taille: 80, coul: CREME }); infini(x + 50, 1230, 60, CREME, 9); });
      g.restore(); }
  }

  // la parabole y = x² − x qui monte vers + infini
  function courbe(p, t) {
    const ox = 330, oy = 1100, s = 70, X = x => ox + x * s, Y = y => oy - y * s * .55;
    O.petitTitre('f(x) = x(x − 1)', 400);
    ligne(80, oy, 1010, oy, al(CREME, .5), 5); ligne(ox, oy + 120, ox, 470, al(CREME, .5), 5);
    const k = eo(pr(t, p.a, .8));
    g.save(); g.strokeStyle = OR; g.lineWidth = 10; g.lineCap = 'round'; g.beginPath();
    for (let x = -2.2; x <= -2.2 + 11 * k; x += .05) { const y = x * x - x; if (Y(y) < 480) break; x === -2.2 ? g.moveTo(X(x), Y(y)) : g.lineTo(X(x), Y(y)); } g.stroke(); g.restore();
    const ka = eo(pr(t, p.a + .7, .3)); if (ka > 0) { g.save(); g.globalAlpha = ka;
      S.d.fleche(870, 760, 960, 520, ka, { trait: ROUGE, ep: 12 }); g.restore(); }
    const kt = pop(t, p.a + .6, .35); if (kt > 0) { g.save(); g.translate(W / 2, 1360); g.scale(kt, kt);
      S.texte('TEND VERS +', -70, 0, { taille: 100, coul: OR, contour: NOIR, contourL: 10 }); infini(330, 0, 75, OR, 14); g.restore(); }
  }

  // ton score : les chiffres 0, 1, 2, 3 s'allument à leur repère (p.n), trois copies en dessous
  function score(p, t) {
    O.petitTitre('TON SCORE', 380);
    const N = p.n || [];
    N.forEach((a, i) => {
      const ta = tps(a), on = t >= ta, k = back(pr(t, ta, .3)), x = W / 2 + (i - 1.5) * 220, actif = on && (!N[i + 1] || t < tps(N[i + 1]));
      g.save(); g.translate(x, 700); g.scale(on ? lerp(.6, actif ? 1.15 : 1, k) : .8, on ? lerp(.6, actif ? 1.15 : 1, k) : .8);
      g.fillStyle = actif ? OR : al(CREME, on ? .2 : .06); g.beginPath(); g.roundRect(-90, -110, 180, 220, 24); g.fill();
      S.texte(String(i), 0, 6, { taille: 150, police: 'Spectral', poids: 600, coul: actif ? NOIR : CREME }); g.restore();
    });
    S.texte('/ 3', W / 2, 920, { taille: 90, coul: GRIS, poids: 700 });
    ['LOG', 'EXP', 'LIMITES'].forEach((s, i) => { const k = eo(pr(t, p.a + .2 + i * .12, .3)); g.save(); g.globalAlpha = k;
      g.translate(W / 2 + (i - 1) * 320, 1250); g.rotate((i - 1) * .06); feuille(260, 340, 5, 2); S.texte(s, 0, -130, { taille: 34, coul: NOIR, esp: 3, max: 230 }); g.restore(); });
    const kt = back(pr(t, p.a + .4, .3)); g.save(); g.globalAlpha = cl(kt * 2); g.translate(W / 2, 1560); g.scale(lerp(1.4, 1, kt), lerp(1.4, 1, kt));
    S.texte('COMBIEN ?', 0, 0, { taille: 110, coul: OR, contour: NOIR, contourL: 10 }); g.restore();
  }

  return { copies, pret, manche, regle, facteur, retenir, fi, facto, courbe, score };
};
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'copies') [0, 1, 2].forEach(i => L.push([p.a + i * .14, 'papier', .45]));
  if (p.type === 'pret') L.push([p.a, 'montee', .6], [p.a + .5, 'drop', .8]);
  if (p.type === 'manche') L.push([p.a, 'chapitre', .8]);
  if (p.type === 'regle') L.push([p.a + .1, 'pop', .5], [tps(p.e2) + .1, 'pop', .5], [tps(p.e2) + .7, 'buzz', .45]);
  if (p.type === 'facteur') L.push([p.a, 'stylo', .4], [p.a + 1.1, 'valide', .6]);
  if (p.type === 'retenir') L.push([p.a, 'papier', .5], [p.a + .9, 'stylo', .5], [p.a + 1.2, 'tampon', .8]);
  if (p.type === 'fi') L.push([p.a + .9, 'lame', .7], [tps(p.e2), 'tampon', .9]);
  if (p.type === 'facto') L.push([p.a + .35, 'pop', .5], [p.a + .8, 'whoosh', .4]);
  if (p.type === 'courbe') L.push([p.a, 'montee', .4], [p.a + .6, 'valide', .5]);
  if (p.type === 'score') (p.n || []).forEach(a => L.push([tps(a), 'pop', .5]));
};
