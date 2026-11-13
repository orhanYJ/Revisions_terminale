// Plans propres au short « quidit » (« Qui a dit ça ? », quatre citations), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
window.SANS_ST_A = ['cases', 'trois', 'num', 'citation', 'auteur', 'choix', 'nuage', 'roseau', 'prison', 'score'];
window.PROPRES_A = ['cases', 'trois', 'num', 'citation', 'auteur', 'choix', 'nuage', 'roseau', 'prison', 'score', 'quatre'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const PAPIER = '#f3ecdc', PALE = '#b8ad97';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const claque = (s, y, ta, t, o) => { const k = back(pr(t, ta, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
    S.texte(s, 0, 0, Object.assign({ taille: 100, coul: CREME, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };
  const deuxClaque = (txt, y, ta, t, taille = 110) => { const k = back(pr(t, ta, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };

  // quatre cases « ? » ; p.fin : la question de la fin (boucle)
  function cases(p, t) {
    if (!p.fin) claque('4 CITATIONS', 520, p.a + .05, t, { taille: 150, coul: OR });
    for (let i = 0; i < 4; i++) {
      const k = back(pr(t, p.a + .2 + i * .12, .3)), x = 165 + i * 250, y = 880;
      if (k <= 0) continue;
      g.save(); g.translate(x, y); g.scale(k, k); g.rotate((i % 2 ? .04 : -.04));
      const cl2 = p.fin && Math.floor((t - p.a) * 4 + i) % 4 === 0;
      g.fillStyle = cl2 ? 'rgba(217,180,90,.25)' : 'rgba(239,230,210,.07)'; g.strokeStyle = cl2 ? OR : CREME; g.lineWidth = 6;
      g.beginPath(); g.roundRect(-100, -100, 200, 200, 22); g.fill(); g.stroke();
      S.texte('?', 0, 6, { taille: 130, coul: cl2 ? OR : CREME, police: 'Spectral', poids: 600 });
      g.restore();
    }
    if (p.fin) deuxClaque('ET TOI…|COMBIEN SUR 4 ?', 1300, p.a + .1, t, 110);
    else if (t >= tps(p.q)) deuxClaque('COMBIEN TU EN|RECONNAIS ?', 1300, tps(p.q), t, 110);
  }

  // trois auteurs mystère ; à p.un, la roulette : un seul l'a écrite
  function trois(p, t) {
    const tu = tps(p.un), roul = t >= tu ? Math.floor((t - tu) * 9) % 3 : -1;
    ['A', 'B', 'C'].forEach((s, i) => {
      const k = back(pr(t, p.a + i * .15, .3)), x = 200 + i * 340, y = 840;
      if (k <= 0) return;
      const on = roul === i;
      g.save(); g.translate(x, y); g.scale(k, k);
      if (on) { g.shadowColor = OR; g.shadowBlur = 40; }
      g.fillStyle = on ? 'rgba(217,180,90,.2)' : 'rgba(239,230,210,.06)'; g.strokeStyle = on ? OR : 'rgba(239,230,210,.5)'; g.lineWidth = 6;
      g.beginPath(); g.roundRect(-140, -210, 280, 420, 26); g.fill(); g.stroke(); g.shadowBlur = 0;
      S.d.tete(10, -30, 150, { trait: on ? OR : CREME, fond: '#1b1712', ep: 7 });
      S.texte('?', 20, -50, { taille: 110, coul: on ? OR : CREME, police: 'Spectral', poids: 600 });
      S.texte(s, 0, 160, { taille: 70, coul: OR });
      g.restore();
    });
    if (t < tu) claque('TROIS AUTEURS', 1350, p.a + .2, t, { taille: 120 });
    else deuxClaque('UN SEUL|L’A ÉCRITE', 1350, tu, t, 120);
  }

  // le numéro de la citation
  function num(p, t) {
    O.petitTitre(p.t || 'CITATION', 520, p.t ? ROUGE : OR);
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2 - 60, 880); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k));
    S.texte(String(p.n), 0, 0, { taille: 480, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 50 });
    g.restore();
    S.texte('/ 4', W / 2 + 190, 980, { taille: 110, police: 'Spectral', poids: 600, coul: CREME });
    for (let i = 0; i < 4; i++) { g.fillStyle = i < p.n ? OR : 'rgba(239,230,210,.2)'; g.beginPath(); g.arc(W / 2 - 150 + i * 100, 1260, 22, 0, 7); g.fill(); }
  }

  // la citation, écrite au fil de la voix ; jusqua : n lignes seulement ; deja : n lignes déjà écrites
  function citation(p, t) {
    O.petitTitre('CITATION ' + p.n + ' / 4', 420);
    S.texte('«', 150, 560, { taille: 300, police: 'Spectral', poids: 600, coul: 'rgba(217,180,90,.25)' });
    const L = p.q.split('|'), d0 = p.deja || 0, d1 = p.jusqua || L.length;
    const aEcrire = L.slice(d0, d1).join('').length, dur = Math.max(.6, (p.b - p.a) * .85), n = Math.floor(cl((t - p.a) / dur) * aEcrire);
    let c = 0;
    L.forEach((s, i) => {
      if (i >= d1) return;
      let vis = s; if (i >= d0) { vis = s.slice(0, Math.max(0, n - c)); c += s.length; }
      const y = 860 + (i - (L.length - 1) / 2) * 125, neuf = d0 > 0 && i >= d0;
      S.texte(vis, W / 2, y, { taille: 84, police: 'Spectral', it: true, poids: 500, coul: neuf ? OR : CREME, max: 980 });
    });
    const kq = eo(pr(t, p.a + dur * .7, .4)); if (kq > 0 && (!p.jusqua)) { g.save(); g.globalAlpha = kq * (.75 + .25 * Math.sin(t * 8));
      S.texte('QUI A DIT ÇA ?', W / 2, 1380, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 10 }); g.restore(); }
  }

  // l'auteur révélé : portrait, nom, œuvre, date
  function auteur(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte(p.img, W / 2 + lerp(300, 0, k), 700, 580, 740, lerp(.15, -.03, k), 1.05 + (t - p.a) * .03, .5, .35, { lum: .95 });
    claque(p.t, 1210, p.a + .1, t, { taille: 150, coul: OR, contourL: 12 });
    const ko = eo(pr(t, p.a + .25, .35)); g.save(); g.globalAlpha = ko;
    S.texte(p.oeuvre, W / 2, 1345, { taille: 58, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 960 });
    S.texte(p.date, W / 2, 1450, { taille: 84, police: 'Spectral', poids: 600, coul: CREME });
    g.restore();
  }

  // Sartre : le carrefour ; ne pas choisir, c'est encore choisir
  function choix(p, t) {
    O.fondImg('chemins', 1.2 + (t - p.a) * .02, .5, .5, .4);
    const te = tps(p.encore), enc = t >= te;
    g.save(); g.strokeStyle = CREME; g.lineWidth = 16; g.lineCap = 'round';
    g.beginPath(); g.moveTo(540, 1240); g.lineTo(540, 960); g.stroke();
    const kb = eo(pr(t, p.a + .1, .4));
    [[-1, 300, 640], [1, 780, 640]].forEach(([s, x, y]) => { S.d.fleche(540, 960, lerp(540, x, kb), lerp(960, y, kb), 1, { trait: enc ? 'rgba(239,230,210,.35)' : CREME, ep: 14 }); });
    g.restore();
    // toi, au carrefour, qui hésites
    const hx = 540 + (enc ? 0 : Math.sin((t - p.a) * 5) * 40);
    g.save(); g.fillStyle = enc ? OR : CREME; g.shadowColor = enc ? OR : 'transparent'; g.shadowBlur = enc ? 40 : 0;
    g.beginPath(); g.arc(hx, 920, 40, 0, 7); g.fill(); g.restore();
    if (enc) { g.save(); g.strokeStyle = OR; g.lineWidth = 8; const r = 70 + 30 * eo(pr(t, te, .4)); g.beginPath(); g.arc(540, 920, r, 0, 7); g.stroke(); g.restore(); }
    claque('NE PAS CHOISIR…', 1350, p.a + .1, t, { taille: 110, coul: enc ? GRIS : CREME });
    if (enc) claque('… C’EST ENCORE CHOISIR', 1480, te, t, { taille: 96, coul: OR });
  }

  // Kant : tout le monde veut être heureux ; personne ne sait ce qu'il veut (p.etape 1 ou 2)
  function nuage(p, t) {
    O.fondImg('jeunesse', 1.35 + (t - p.a) * .02, .75, .3, .45);
    const ic = [
      (x, y) => { g.fillStyle = ROUGE; g.beginPath(); g.moveTo(x, y + 30); g.bezierCurveTo(x - 60, y - 5, x - 38, y - 52, x, y - 26); g.bezierCurveTo(x + 38, y - 52, x + 60, y - 5, x, y + 30); g.fill(); },
      (x, y) => { g.fillStyle = OR; g.beginPath(); g.arc(x, y, 34, 0, 7); g.fill(); S.texte('€', x, y + 2, { taille: 44, coul: NOIR }); },
      (x, y) => { g.fillStyle = OR; g.beginPath(); for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, r = i % 2 ? 16 : 38; g.lineTo(x + Math.cos(a) * r, y + Math.sin(a) * r); } g.closePath(); g.fill(); },
    ];
    [250, 540, 830].forEach((x, i) => {
      const k = back(pr(t, p.a + i * .12, .3)); if (k <= 0) return;
      g.save(); g.translate(x, 1050); g.scale(k, k);
      S.d.tete(0, 0, 120, { trait: CREME, fond: '#1b1712', ep: 7 });
      // bulle de pensée
      g.fillStyle = PAPIER; g.beginPath(); g.ellipse(20, -250, 110, 80, 0, 0, 7); g.fill();
      [[0, -150, 16], [-10, -115, 10]].forEach(([a, b, r]) => { g.beginPath(); g.arc(a, b, r, 0, 7); g.fill(); });
      if (p.etape === 1) ic[i](20, -250);
      else { const bo = Math.sin(t * 6 + i) * 8; S.texte('?', 20, -248 + bo, { taille: 120, coul: ROUGE, police: 'Spectral', poids: 600 }); }
      g.restore();
    });
    if (p.etape === 1) deuxClaque('TOUT LE MONDE VEUT|ÊTRE HEUREUX', 1380, p.a + .1, t, 100);
    else deuxClaque('PERSONNE NE SAIT|CE QU’IL VEUT', 1380, p.a + .1, t, 100);
  }

  // Pascal : le roseau sous l'univers ; à p.sait, il s'allume
  function roseau(p, t) {
    O.fondImg('roseaux', 1.2, .5, .6, .25);
    const ts = tps(p.sait), sait = t >= ts, lt = t - p.a;
    // l'univers qui pèse : un ciel étoilé qui descend
    const desc = eo(pr(t, p.a, 1.2)) * 260;
    g.save(); const gr = g.createLinearGradient(0, 0, 0, 520 + desc); gr.addColorStop(0, 'rgba(10,12,30,.95)'); gr.addColorStop(1, 'rgba(10,12,30,0)'); g.fillStyle = gr; g.fillRect(0, 0, W, 520 + desc);
    for (let i = 0; i < 60; i++) { const x = rnd(i) * W, y = 200 + rnd(i + 99) * (300 + desc); g.globalAlpha = .4 + .6 * Math.abs(Math.sin(t * 2 + i)); g.fillStyle = CREME; g.fillRect(x, y, 4, 4); }
    g.restore();
    // le roseau, qui plie
    const b = .35 + .25 * Math.sin(lt * 2.4) * (sait ? .4 : 1) + (sait ? 0 : eo(pr(t, p.a, 1.2)) * .2);
    const tx = 540 + b * 280, ty = 620 + b * 220;
    g.save(); g.strokeStyle = sait ? OR : '#8a9a5b'; g.lineWidth = 16; g.lineCap = 'round'; if (sait) { g.shadowColor = OR; g.shadowBlur = 40; }
    g.beginPath(); g.moveTo(540, 1280); g.quadraticCurveTo(540, 900, tx, ty); g.stroke();
    g.lineWidth = 9; g.beginPath(); g.moveTo(540, 1080); g.quadraticCurveTo(470, 980, 420, 1000); g.stroke();
    g.fillStyle = sait ? OR : '#6b5a3a'; g.beginPath(); g.ellipse(tx, ty, 22, 50, b + .4, 0, 7); g.fill();
    g.restore();
    g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(200, 1280); g.lineTo(880, 1280); g.stroke();
    if (!sait) deuxClaque('L’UNIVERS PEUT|L’ÉCRASER', 1420, p.a + .1, t, 100);
    else deuxClaque('MAIS IL SAIT|QU’IL MEURT', 1420, ts, t, 110);
  }

  // Rousseau : les fers, puis les barreaux de la prison
  function prison(p, t) {
    O.fondImg('carceri', 1.25 + (t - p.a) * .02, .5, .5, .4);
    const tb = tps(p.barreaux), kb = pr(t, tb, .3);
    // chaîne qui traverse l'écran
    const kc = eo(pr(t, p.a, .5));
    for (let i = 0; i < 12; i++) { const x = -40 + i * 100, y = 880 + Math.sin(i * .6 + t) * 18;
      if (x > W * kc + 40) break;
      g.save(); g.translate(x, y); g.rotate(i % 2 ? 0 : .0); g.strokeStyle = i % 2 ? CREME : GRIS; g.lineWidth = 14;
      g.beginPath(); g.ellipse(0, 0, 58, i % 2 ? 30 : 12, 0, 0, 7); g.stroke(); g.restore(); }
    // barreaux qui tombent
    if (t >= tb) for (let i = 0; i < 7; i++) { const x = 120 + i * 140, y1 = lerp(-900, 0, eo(kb)) + 1250;
      g.fillStyle = '#2b2620'; g.strokeStyle = CREME; g.lineWidth = 4; g.fillRect(x - 14, y1 - 900, 28, 900); g.strokeRect(x - 14, y1 - 900, 28, 900); }
    deuxClaque('QUELLE SOCIÉTÉ…|NE SERAIT PAS UNE PRISON ?', 1400, p.a + .1, t, 92);
  }

  // « Dis-le en commentaire » : une bulle où l'on tape son score
  function score(p, t) {
    const k = back(pr(t, p.a, .3));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = PAPIER; g.beginPath(); g.roundRect(-430, -150, 860, 300, 40); g.fill();
    g.beginPath(); g.moveTo(-300, 150); g.lineTo(-340, 230); g.lineTo(-220, 150); g.fill();
    g.fillStyle = GRIS; g.beginPath(); g.arc(-330, -10, 60, 0, 7); g.fill();
    const s = 'Mon score : ' + (1 + Math.floor((t - p.a) * 4) % 4) + ' / 4', curseur = Math.floor(t * 3) % 2 ? '|' : '';
    S.texte(s + curseur, -240, -10, { taille: 66, police: 'Spectral', poids: 600, coul: NOIR, align: 'left', max: 640 });
    g.restore();
    claque('EN COMMENTAIRE', 1300, p.a + .15, t, { taille: 110, coul: OR });
  }

  // les quatre auteurs et leur série
  function quatre(p, t) {
    O.petitTitre('LES 4 AUTEURS, EXPLIQUÉS', 380);
    [['sartre', 'SARTRE', 'La liberté'], ['kant', 'KANT', 'Le bonheur'], ['pascal', 'PASCAL', 'La conscience'], ['rousseau', 'ROUSSEAU', 'La liberté']].forEach(([im, nom, serie], i) => {
      const k = eo(pr(t, p.a + i * .18, .35)); if (k <= 0) return;
      const x = i % 2 ? 790 : 290, y = i < 2 ? 680 : 1150;
      g.save(); g.globalAlpha = cl(k * 2);
      O.carte(im, x + lerp(i % 2 ? 200 : -200, 0, k), y, 330, 340, (i % 2 ? .03 : -.03), 1.1, .5, .3, { lum: .95 });
      S.texte(nom, x, y + 215, { taille: 54, coul: OR, contour: NOIR, contourL: 8 });
      S.texte('série « ' + serie + ' »', x, y + 268, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 460 });
      g.restore();
    });
  }

  return { cases, trois, num, citation, auteur, choix, nuage, roseau, prison, score, quatre };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'cases') for (let i = 0; i < 4; i++) L.push([p.a + .2 + i * .12, 'blip', .4]);
  if (p.type === 'trois') { L.push([p.a, 'pop', .35]); for (let x = tps(p.un); x < p.b - .1; x += .11) L.push([x, 'tic', .25]); }
  if (p.type === 'num') L.push([p.a, 'chapitre', .6]);
  if (p.type === 'citation') { const n = p.q.length, d = Math.max(.6, (p.b - p.a) * .85); for (let k = 0; k < n; k += 7) L.push([p.a + d * k / n, 'tic', .15]); }
  if (p.type === 'auteur') L.push([p.a, 'whoosh', .4]);
  if (p.type === 'choix') { L.push([p.a, 'souffle', .3]); L.push([tps(p.encore), 'valide', .5]); }
  if (p.type === 'nuage') L.push([p.a, p.etape === 1 ? 'pop' : 'blip', .4]);
  if (p.type === 'roseau') { L.push([p.a, 'souffle', .45]); L.push([tps(p.sait), 'gong', .45]); }
  if (p.type === 'prison') { L.push([p.a, 'frotte', .4]); L.push([tps(p.barreaux), 'boum', .7]); }
  if (p.type === 'score') L.push([p.a, 'pop', .5]);
  if (p.type === 'quatre') for (let i = 0; i < 4; i++) L.push([p.a + i * .18, 'papier', .25]);
};
