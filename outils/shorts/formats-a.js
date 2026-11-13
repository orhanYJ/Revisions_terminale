// Plans communs aux formats « question de bac », « résumé express » et « vrai ou faux » (modèle A).
// Chargé par short.html pour tous les shorts ; un short peut ajouter ses propres plans dans <code>.types-a.js.
//
// copie    : copie de bac qui s'écrit. Champs : matiere ('PHILOSOPHIE'), sujet (texte, « | » = retour à la ligne),
//            lignes = [[repère, texte, style], …] ; style : 'titre' (rouge, gras : « Problématique »), 'partie'
//            (gras : « I. … »), 'ex' (exemple, en retrait), '' (normal). Chaque ligne s'écrit à son repère
//            ([passage, mot]) ; au-delà de 9 lignes, les plus anciennes remontent et disparaissent.
//            souligne : [repère, n° de ligne] → coup de stylo rouge sous la ligne n.
// fiche    : fiche résumé. Champs : t (titre), sur (petit sur-titre), items = [[repère, texte, sous], …]
//            (5 au plus, chacun coché à son repère).
// vraifaux : une affirmation, un chrono, le verdict. Champs : n ('1 / 5'), t (affirmation, « | » = retour à la ligne),
//            rep (repère du verdict), v (true = VRAI, false = FAUX), expl (explication courte, après le verdict),
//            chrono (repère où le compte à rebours démarre, par ex. [passage, 'vrai'] ; sinon dès le début du plan),
//            doux: true (verdict sans buzzer, pour un sujet grave).
window.FORMATS_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const VERT = '#7fbf6a';

  function copie(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 930, k)); g.rotate(-.02);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#f3ecdc'; g.fillRect(-470, -640, 940, 1280); g.shadowColor = 'transparent';
    // lignes et marge de la copie
    g.strokeStyle = 'rgba(80,110,160,.25)'; g.lineWidth = 2; for (let y = -380; y < 620; y += 70) { g.beginPath(); g.moveTo(-440, y); g.lineTo(440, y); g.stroke(); }
    g.strokeStyle = 'rgba(200,55,45,.5)'; g.beginPath(); g.moveTo(-370, -640); g.lineTo(-370, 640); g.stroke();
    S.texte('BACCALAURÉAT · ' + (p.matiere || 'PHILOSOPHIE'), 0, -585, { taille: 34, coul: NOIR, esp: 5 });
    const suj = (p.sujet || '').split('|');
    suj.forEach((s, i) => S.texte(s, 0, -510 + i * 58, { taille: 50, police: 'Spectral', poids: 600, coul: NOIR, max: 860 }));
    // lignes écrites au fil de la voix
    const vis = (p.lignes || []).filter(([a]) => t >= tps(a));
    const debut = Math.max(0, vis.length - 9);
    vis.slice(debut).forEach(([a, txt, st], j) => {
      const ta = tps(a), n = Math.floor(cl((t - ta) / Math.max(.35, txt.length * .028)) * txt.length);
      const y = -345 + j * 70, x = st === 'ex' ? -330 : -350;
      const o = { taille: st === 'titre' ? 44 : 42, police: 'Spectral', it: st !== 'partie', poids: st === 'partie' || st === 'titre' ? 600 : 400,
        coul: st === 'titre' ? ROUGE : NOIR, align: 'left', max: 780 };
      S.texte(txt.slice(0, n), x, y, o);
      if (p.souligne && p.souligne[1] === debut + j && t >= tps(p.souligne[0])) {
        const ks = eo(pr(t, tps(p.souligne[0]), .35)); g.strokeStyle = ROUGE; g.lineWidth = 6;
        g.beginPath(); g.moveTo(x, y + 30); g.lineTo(x + Math.min(780, S.largeur(txt, o)) * ks, y + 26); g.stroke();
      }
    });
    g.restore();
  }

  function fiche(p, t) {
    if (p.sur) S.texte(p.sur, W / 2, 330, { taille: 36, coul: OR, esp: 8, poids: 600, max: 960 });
    const kt = back(pr(t, p.a, .3)); g.save(); g.translate(W / 2, 450); g.scale(lerp(1.6, 1, kt), lerp(1.6, 1, kt));
    S.texte(p.t, 0, 0, { taille: 96, coul: CREME, contour: NOIR, contourL: 10, max: 980 }); g.restore();
    const items = (p.items || []);
    items.forEach(([a, txt, sous], j) => {
      const ta = tps(a); if (t < ta) return;
      const k = back(pr(t, ta, .3)), y = 640 + j * 190, actif = !items[j + 1] || t < tps(items[j + 1][0]);
      g.save(); g.globalAlpha = actif ? 1 : .55; g.translate(lerp(-300, 0, eo(pr(t, ta, .25))), 0);
      g.fillStyle = actif ? 'rgba(217,180,90,.14)' : 'rgba(239,230,210,.05)'; g.fillRect(70, y - 75, 940, 160);
      g.save(); g.translate(140, y); g.scale(k, k); g.fillStyle = OR; g.beginPath(); g.arc(0, 0, 42, 0, 7); g.fill();
      S.texte('✓', 0, 3, { taille: 54, coul: NOIR }); g.restore();
      S.texte(txt, 210, sous ? y - 20 : y, { taille: 56, coul: CREME, align: 'left', max: 770 });
      if (sous) S.texte(sous, 210, y + 42, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: GRIS === '#8d8371' ? '#b8ad97' : GRIS, align: 'left', max: 770 });
      g.restore();
    });
  }

  function vraifaux(p, t) {
    const tr = tps(p.rep), avant = t < tr;
    if (p.n) S.texte(p.n, W / 2, 330, { taille: 44, coul: OR, esp: 10, poids: 600 });
    // carte de l'affirmation
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 700); g.scale(lerp(.6, 1, k), lerp(.6, 1, k));
    g.fillStyle = '#f3ecdc'; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillRect(-480, -230, 960, 460); g.shadowColor = 'transparent';
    const L = p.t.split('|'); L.forEach((s, i) => S.texte(s, 0, (i - (L.length - 1) / 2) * 92, { taille: 74, police: 'Spectral', poids: 600, coul: NOIR, max: 880 }));
    g.restore();
    // chrono
    const tc = p.chrono ? tps(p.chrono) : p.a;
    if (avant && t >= tc) {
      const tot = Math.max(.6, tr - tc), u = cl((t - tc) / tot), reste = Math.ceil((tr - t));
      g.save(); g.translate(W / 2, 1110); g.strokeStyle = 'rgba(239,230,210,.2)'; g.lineWidth = 18; g.beginPath(); g.arc(0, 0, 110, 0, 7); g.stroke();
      g.strokeStyle = u > .7 ? ROUGE : OR; g.beginPath(); g.arc(0, 0, 110, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
      S.texte(String(Math.max(0, reste)), 0, 4, { taille: 110, coul: CREME }); g.restore();
      // les deux boutons
      [['VRAI', -230, VERT], ['FAUX', 230, ROUGE]].forEach(([s, dx, c]) => { g.save(); g.translate(W / 2 + dx, 1390); g.strokeStyle = c; g.lineWidth = 6;
        g.beginPath(); g.roundRect(-180, -70, 360, 140, 30); g.stroke(); S.texte(s, 0, 4, { taille: 72, coul: c }); g.restore(); });
    } else if (!avant) {
      const kv = pr(t, tr, .3), c = p.v ? VERT : ROUGE;
      O.tampon(p.v ? 'VRAI' : 'FAUX', W / 2, 1130, kv, -.08, 190, c);
      if (p.expl) { const ke = eo(pr(t, tr + .35, .35)); g.save(); g.globalAlpha = ke;
        const E = p.expl.split('|'); E.forEach((s, i) => S.texte(s, W / 2, 1370 + i * 66, { taille: 54, coul: CREME, max: 960, contour: NOIR, contourL: 8 })); g.restore(); }
    }
  }

  // quiz3 : une question (souvent une citation : « Qui a dit ça ? »), trois réponses avec portrait facultatif,
  // un chrono, puis la bonne réponse s'allume. Champs : n ('1 / 4'), q (texte, « | » = retour à la ligne),
  // sur (petit titre au-dessus, ex. 'QUI A DIT ÇA ?'), options = [{t: 'Kant', img: 'kant', sous: '1724-1804'}, …] (3),
  // bonne (indice 0, 1 ou 2), chrono (repère du début du compte), rep (repère du verdict), expl (une phrase).
  function quiz3(p, t) {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a, avant = t < tr;
    if (p.sur) S.texte(p.sur, W / 2, 300, { taille: 40, coul: OR, esp: 8, poids: 600, max: 960 });
    if (p.n) S.texte(p.n, W / 2, 360, { taille: 34, coul: GRIS, esp: 8, poids: 600 });
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 560); g.scale(lerp(.6, 1, k), lerp(.6, 1, k));
    g.fillStyle = '#f3ecdc'; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillRect(-480, -150, 960, 300); g.shadowColor = 'transparent';
    const L = p.q.split('|'); L.forEach((s, i) => S.texte(s, 0, (i - (L.length - 1) / 2) * 80, { taille: 64, police: 'Spectral', it: true, poids: 500, coul: NOIR, max: 900 }));
    g.restore();
    (p.options || []).forEach((o, i) => {
      const ki = eo(pr(t, p.a + .25 + i * .12, .3)); if (ki <= 0) return;
      const y = 870 + i * 230, bon = i === p.bonne, revele = !avant;
      g.save(); g.globalAlpha = ki * (revele && !bon ? .35 : 1); g.translate(lerp(400, 0, ki), 0);
      g.fillStyle = revele && bon ? 'rgba(127,191,106,.22)' : 'rgba(239,230,210,.07)'; g.fillRect(90, y - 95, 900, 190);
      g.strokeStyle = revele && bon ? VERT : 'rgba(239,230,210,.35)'; g.lineWidth = revele && bon ? 8 : 3; g.strokeRect(90, y - 95, 900, 190);
      S.texte('ABC'[i], 150, y, { taille: 60, coul: OR });
      const im = o.img && S.img(o.img); let x0 = 200;
      if (im) { g.save(); g.filter = 'grayscale(1) contrast(1.2)'; S.cover(im, 200, y - 80, 130, 160, 1.1, .5, .3); g.restore(); x0 = 360; }
      S.texte(o.t, x0, o.sous ? y - 18 : y, { taille: 62, coul: CREME, align: 'left', max: 600 });
      if (o.sous) S.texte(o.sous, x0, y + 40, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: '#b8ad97', align: 'left', max: 600 });
      if (revele && bon) { const kv = back(pr(t, tr, .3)); g.save(); g.translate(930, y); g.scale(kv, kv); g.fillStyle = VERT; g.beginPath(); g.arc(0, 0, 44, 0, 7); g.fill(); S.texte('✓', 0, 4, { taille: 60, coul: NOIR }); g.restore(); }
      g.restore();
    });
    if (avant && t >= tc) {
      const u = cl((t - tc) / Math.max(.6, tr - tc)), reste = Math.ceil(tr - t);
      g.save(); g.translate(W / 2, 1620); g.strokeStyle = 'rgba(239,230,210,.2)'; g.lineWidth = 14; g.beginPath(); g.arc(0, 0, 80, 0, 7); g.stroke();
      g.strokeStyle = u > .7 ? ROUGE : OR; g.beginPath(); g.arc(0, 0, 80, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
      S.texte(String(Math.max(0, reste)), 0, 4, { taille: 80, coul: CREME }); g.restore();
    }
    if (!avant && p.expl) { const ke = eo(pr(t, tr + .35, .35)); g.save(); g.globalAlpha = ke;
      p.expl.split('|').forEach((s, i) => S.texte(s, W / 2, 1600 + i * 62, { taille: 50, coul: CREME, max: 960, contour: NOIR, contourL: 8 })); g.restore(); }
  }

  return { copie, fiche, vraifaux, quiz3 };
};
window.SONS_FORMATS = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'copie') { L.push([p.a, 'papier', .5]); (p.lignes || []).forEach(([a]) => L.push([tps(a), 'stylo', .35])); }
  if (p.type === 'fiche') (p.items || []).forEach(([a]) => L.push([tps(a), 'valide', .5]));
  if (p.type === 'quiz3') {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a;
    (p.options || []).forEach((o, i) => L.push([p.a + .25 + i * .12, 'pop', .4]));
    for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]);
    L.push([tr, 'valide', .9]);
  }
  if (p.type === 'vraifaux') {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a;
    for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]);
    L.push([tr, p.v ? 'valide' : (p.doux ? 'gong' : 'buzz'), p.doux ? .5 : .9]);
  }
};
window.TYPES_FORMATS = ['copie', 'fiche', 'vraifaux', 'quiz3'];
