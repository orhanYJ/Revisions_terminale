// Plans propres au short « conscience60 » (« La conscience en 60 secondes »), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
window.SANS_ST_A = ['chrono', 'noms', 'cite', 'proces', 'honte'];
window.PROPRES_A = ['chrono', 'foot', 'doute', 'logique', 'noms', 'trous', 'serrure', 'honte', 'cite', 'proces'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const PAPIER = '#f3ecdc', BOIS = '#3a2a1c';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // texte de l'étape courante : etapes = [[repère ou null, texte], …] → [texte, instant, n° d'étape]
  const etapeTxt = (p, t) => { let s = p.etapes[0][1], a = p.a, k = 0; p.etapes.forEach(([r, x], i) => { if (!r || t >= tps(r)) { s = x; a = r ? tps(r) : p.a; k = i; } }); return [s, a, k]; };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };

  // compte à rebours de 60 s ; p.run : il tourne
  function chrono(p, t) {
    const u = p.run ? cl((t - p.a) / 60) : 0, reste = p.run ? Math.max(0, 60 - Math.floor(t - p.a)) : 60;
    const k = back(pr(t, p.a, .35)), r = 250;
    g.save(); g.translate(W / 2, 760); g.scale(lerp(.6, 1, k), lerp(.6, 1, k));
    g.strokeStyle = 'rgba(239,230,210,.15)'; g.lineWidth = 26; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
    g.strokeStyle = ROUGE; g.lineCap = 'round'; g.beginPath(); g.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
    for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(Math.cos(a) * (r - 50), Math.sin(a) * (r - 50)); g.lineTo(Math.cos(a) * (r - 30), Math.sin(a) * (r - 30)); g.stroke(); }
    S.texte(String(reste), 0, -10, { taille: 230, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 40 });
    S.texte('SECONDES', 0, 120, { taille: 40, coul: CREME, esp: 10, poids: 600 });
    g.restore();
    if (p.t) titrePop(p.t, 1290, t, p.a + .1, 110);
  }

  // bonhomme de profil (regard à droite) ; jambe = angle de la jambe droite
  function bonhomme(x, y, s, jambe, coul = CREME) {
    g.save(); g.translate(x, y); g.scale(s, s); g.strokeStyle = coul; g.lineWidth = 12; g.lineCap = 'round'; g.lineJoin = 'round';
    g.fillStyle = '#1b1712'; g.beginPath(); g.arc(0, -300, 50, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(0, -250); g.lineTo(-10, -90); g.stroke();
    g.beginPath(); g.moveTo(-5, -210); g.lineTo(-80, -140); g.moveTo(-5, -210); g.lineTo(70, -170); g.stroke();
    g.beginPath(); g.moveTo(-10, -90); g.lineTo(-60, 0); g.stroke();
    g.beginPath(); g.moveTo(-10, -90); g.lineTo(-10 + Math.sin(jambe) * 95, -90 + Math.cos(jambe) * 95); g.stroke();
    g.restore();
  }
  function but(x, y, w, h) {
    g.save(); g.strokeStyle = CREME; g.lineWidth = 10; g.beginPath(); g.moveTo(x, y + h); g.lineTo(x, y); g.lineTo(x + w, y); g.lineTo(x + w, y + h); g.stroke();
    g.strokeStyle = 'rgba(239,230,210,.25)'; g.lineWidth = 3;
    for (let i = 1; i < 8; i++) { g.beginPath(); g.moveTo(x + w * i / 8, y); g.lineTo(x + w * i / 8, y + h); g.stroke(); }
    for (let i = 1; i < 6; i++) { g.beginPath(); g.moveTo(x, y + h * i / 6); g.lineTo(x + w, y + h * i / 6); g.stroke(); }
    g.restore();
  }
  function ballon(x, y, r) { g.save(); g.fillStyle = CREME; g.strokeStyle = NOIR; g.lineWidth = 4; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.stroke();
    g.fillStyle = NOIR; g.beginPath(); g.arc(x, y, r * .35, 0, 7); g.fill(); g.restore(); }

  // le joueur qui frappe ; p.replay : le même geste revu à l'écran, au ralenti et à l'envers
  function foot(p, t) {
    const lt = t - p.a;
    if (!p.replay) {
      const kj = pr(lt, .15, .25), kb = eo(pr(lt, .35, .8));
      g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 5; g.beginPath(); g.moveTo(60, 1250); g.lineTo(1020, 1250); g.stroke();
      but(760, 820, 240, 430);
      bonhomme(300, 1250, 1, lerp(.5, -1.1, kj));
      const bx = lerp(400, 900, kb), by = lerp(1225, 930, kb) - Math.sin(kb * Math.PI) * 120; ballon(bx, by, 30);
      // le regard va au but, pas à soi
      g.save(); g.setLineDash([16, 14]); g.strokeStyle = OR; g.lineWidth = 5; g.beginPath(); g.moveTo(350, 950); g.lineTo(lerp(350, 860, eo(pr(lt, .1, .5))), lerp(950, 980, eo(pr(lt, .1, .5)))); g.stroke(); g.restore();
      const [txt, ta] = etapeTxt(p, t); titrePop(txt, 1440, t, ta, 100);
    } else {
      // écran de télévision et bandes de retour en arrière
      g.save(); g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.roundRect(90, 520, 900, 640, 30); g.fill(); g.stroke();
      g.beginPath(); g.rect(110, 540, 860, 600); g.clip();
      const u = 1 - ((lt * .6) % 1), kj = pr(u, .15, .25), kb = eo(pr(u, .35, .6));
      g.translate(540, 840); g.scale(.55, .55); g.translate(-540, -840);
      g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 5; g.beginPath(); g.moveTo(60, 1250); g.lineTo(1020, 1250); g.stroke();
      but(760, 820, 240, 430); bonhomme(300, 1250, 1, lerp(.5, -1.1, kj));
      ballon(lerp(400, 900, kb), lerp(1225, 930, kb) - Math.sin(kb * Math.PI) * 120, 30);
      g.restore();
      for (let i = 0; i < 6; i++) { const y = 540 + ((i * 110 + lt * 900) % 600); g.fillStyle = 'rgba(239,230,210,.07)'; g.fillRect(110, y, 860, 26); }
      S.texte('◀◀ REPLAY', 250, 590, { taille: 38, coul: ROUGE, poids: 700 });
      // bulle de pensée
      if (p.bulle && t >= tps(p.bulle)) { const k = back(pr(t, tps(p.bulle), .35)); g.save(); g.translate(W / 2, 1330); g.scale(k, k);
        g.fillStyle = CREME; g.beginPath(); g.roundRect(-460, -110, 920, 220, 60); g.fill();
        [[-80, -150, 28], [-110, -200, 16]].forEach(([cx, cy, rr]) => { g.beginPath(); g.arc(cx, cy, rr, 0, 7); g.fill(); });
        S.texte('« Pourquoi j’ai tiré si vite ? »', 0, 0, { taille: 60, police: 'Spectral', it: true, poids: 500, coul: NOIR, max: 840 }); g.restore(); }
      else O.multi([['APRÈS LE ', CREME], ['MATCH', OR]], 1330, 110);
    }
  }

  // le doute de Descartes : chaque certitude reçoit un point d'interrogation rouge
  function doute(p, t) {
    O.petitTitre('JE DOUTE DE TOUT', 430, ROUGE);
    p.items.forEach(([r, s], i) => {
      const tr = tps(r); if (t < tr) return;
      const k = back(pr(t, tr, .3)), y = 700 + i * 250;
      g.save(); g.translate(lerp(-400, 0, eo(pr(t, tr, .25))), 0);
      g.fillStyle = 'rgba(239,230,210,.07)'; g.fillRect(110, y - 95, 860, 190);
      S.texte(s, 470, y, { taille: 104, coul: CREME, max: 680 });
      g.restore();
      const kq = back(pr(t, tr + .2, .3)); if (kq > 0) { g.save(); g.translate(880, y); g.rotate(.15); g.scale(kq, kq);
        S.texte('?', 0, 0, { taille: 190, coul: ROUGE, contour: NOIR, contourL: 12 }); g.restore(); }
    });
  }

  // douter → penser → être
  function logique(p, t) {
    const [, , n] = etapeTxt(p, t);
    p.etapes.forEach(([r, s], i) => {
      if (i > n) return;
      const tr = r ? tps(r) : p.a, k = back(pr(t, tr, .3)), y = 640 + i * 300, actif = i === n;
      if (i) S.d.fleche(W / 2, y - 220, W / 2, y - 90, eo(pr(t, tr, .25)), { trait: OR, ep: 12 });
      g.save(); g.translate(W / 2, y); g.scale(lerp(1.6, 1, k), lerp(1.6, 1, k));
      S.texte(s, 0, 0, { taille: actif ? 150 : 110, coul: actif ? OR : 'rgba(239,230,210,.6)', contour: NOIR, contourL: 12, ombre: actif && i === 2 ? 'rgba(217,180,90,.6)' : undefined, flou: 40 });
      g.restore();
    });
  }

  // le nom oublié : les faux noms sont barrés, le bon s'allume
  function noms(p, t) {
    O.fondImg('signorelli', 1.3, .5, .5, .35);
    O.petitTitre('LE PEINTRE D’ORVIETO ?', 430);
    p.noms.forEach(([r, s, bon], i) => {
      const tr = tps(r); if (t < tr) return;
      const n = Math.floor(cl((t - tr) / .45) * s.length), y = 700 + i * 260;
      S.texte(s.slice(0, n), W / 2, y, { taille: bon ? 130 : 110, coul: bon ? OR : CREME, contour: NOIR, contourL: 10, ombre: bon ? 'rgba(217,180,90,.6)' : undefined, flou: 40, max: 900 });
      if (!bon) { const kb = eo(pr(t, tr + .5, .2)); if (kb > 0) { const w = S.largeur(s, { taille: 110 }); g.strokeStyle = ROUGE; g.lineWidth = 14;
        g.beginPath(); g.moveTo(W / 2 - w / 2 - 20, y + 8); g.lineTo(W / 2 - w / 2 - 20 + (w + 40) * kb, y - 6); g.stroke(); } }
      else if (t >= tr + .5) O.tampon('✓', W / 2 + 400, y - 30, pr(t, tr + .5, .3), .15, 90, OR);
    });
    if (p.noms.every(([r]) => t >= tps(r))) S.texte('Luca Signorelli, fresques d’Orvieto', W / 2, 1500, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME });
  }

  // la conscience comme une page trouée : oubli, lapsus, rêve ; dessous, l'inconscient
  function trous(p, t) {
    const TR = [[330, 760], [720, 960], [380, 1170]];
    const insc = p.insc && t >= tps(p.insc);
    g.save(); g.translate(W / 2, 960); g.rotate(-.02); g.translate(-W / 2, -960);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = PAPIER; g.fillRect(130, 520, 820, 860); g.shadowColor = 'transparent';
    S.texte('TA CONSCIENCE', W / 2, 590, { taille: 44, coul: NOIR, esp: 6 });
    g.fillStyle = 'rgba(0,0,0,.14)'; for (let i = 0; i < 11; i++) g.fillRect(190, 660 + i * 62, 700 - (i % 3) * 90, 12);
    const vis = p.tous ? TR.map((x, i) => [x, p.a - 1, ['UN OUBLI', 'UN LAPSUS', 'UN RÊVE'][i]]) : (p.trous || []).map(([r, s], i) => [TR[i], tps(r), s]);
    vis.forEach(([[x, y], tr, s]) => {
      if (t < tr) return;
      const k = back(pr(t, tr, .3)), rr = 78 * k;
      const pulse = insc ? .6 + .4 * Math.sin((t - tps(p.insc)) * 8) : .35;
      const gr = g.createRadialGradient(x, y, 0, x, y, rr); gr.addColorStop(0, `rgba(200,55,45,${pulse})`); gr.addColorStop(1, '#0d0b09');
      g.fillStyle = gr; g.beginPath(); g.arc(x, y, rr, 0, 7); g.fill();
      g.strokeStyle = '#7a6a52'; g.lineWidth = 6; g.beginPath(); g.arc(x, y, rr, 0, 7); g.stroke();
      S.texte(s, x < W / 2 ? x + 270 : x - 290, y, { taille: 56, coul: NOIR, max: 380 });
    });
    g.restore();
    if (p.tous) { if (insc) { const k = back(pr(t, tps(p.insc), .3)); g.save(); g.translate(W / 2, 1490); g.scale(lerp(1.6, 1, k), lerp(1.6, 1, k));
      S.texte('L’INCONSCIENT', 0, 0, { taille: 130, coul: ROUGE, contour: NOIR, contourL: 14, max: 980 }); g.restore(); }
      else O.multi([['POUR LES ', CREME], ['EXPLIQUER…', OR]], 1490, 100); }
    else O.multi([['DES ', CREME], ['TROUS', OR]], 1490, 120);
  }

  // l'œil à la serrure ; p.pas : des pas approchent ; p.voit : une ombre surgit
  function serrure(p, t) {
    const lt = t - p.a, voit = p.voit && t >= tps(p.voit), kv = voit ? eo(pr(t, tps(p.voit), .4)) : 0;
    // porte
    g.fillStyle = BOIS; g.fillRect(140, 300, 800, 1200);
    g.strokeStyle = 'rgba(0,0,0,.35)'; g.lineWidth = 6; [[190, 360, 700, 480], [190, 900, 700, 540]].forEach(([x, y, w, h]) => g.strokeRect(x, y, w, h));
    // serrure lumineuse
    const cx = 540, cy = 860;
    g.save(); g.shadowColor = '#f4d48a'; g.shadowBlur = 60; g.fillStyle = '#f4d48a';
    g.beginPath(); g.arc(cx, cy - 30, 48, 0, 7); g.fill(); g.beginPath(); g.moveTo(cx - 28, cy); g.lineTo(cx + 28, cy); g.lineTo(cx + 44, cy + 120); g.lineTo(cx - 44, cy + 120); g.closePath(); g.fill(); g.restore();
    g.strokeStyle = OR; g.lineWidth = 8; g.beginPath(); g.ellipse(cx, cy + 20, 120, 170, 0, 0, 7); g.stroke();
    // l'œil
    const ko = eo(pr(lt, .1, .35)), ouv = lerp(10, voit ? 64 : 46, ko) * (1 + kv * .3);
    g.save(); g.translate(cx - 230, cy - 40); g.globalAlpha = ko;
    g.fillStyle = CREME; g.strokeStyle = NOIR; g.lineWidth = 6; g.beginPath(); g.moveTo(-110, 0); g.quadraticCurveTo(0, -ouv * 2, 110, 0); g.quadraticCurveTo(0, ouv * 2, -110, 0); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = '#5a3f28'; g.beginPath(); g.arc(20 + Math.sin(lt * 2) * 6, 0, 32, 0, 7); g.fill(); g.fillStyle = NOIR; g.beginPath(); g.arc(24 + Math.sin(lt * 2) * 6, 0, 14, 0, 7); g.fill();
    g.restore();
    // pas qui approchent sur le plancher
    (p.pas || []).forEach((r, i) => { const tr = tps(r); if (t < tr) return; const k = back(pr(t, tr, .25));
      g.save(); g.translate(230 + i * 230, 1250 - i * 25); g.rotate(-.3 + (i % 2) * .2); g.scale(k * .8, k * .8); g.fillStyle = 'rgba(239,230,210,.75)';
      g.beginPath(); g.ellipse(0, 0, 34, 58, 0, 0, 7); g.fill(); g.beginPath(); g.ellipse(0, 86, 26, 30, 0, 0, 7); g.fill(); g.restore(); });
    // l'ombre de quelqu'un
    if (kv > 0) { g.save(); g.globalAlpha = .85 * kv; g.fillStyle = NOIR; g.translate(lerp(1300, 860, kv), 0);
      g.beginPath(); g.arc(0, 560, 150, 0, 7); g.fill(); g.beginPath(); g.moveTo(-260, 1500); g.quadraticCurveTo(-240, 760, 0, 730); g.quadraticCurveTo(240, 760, 260, 1500); g.closePath(); g.fill(); g.restore(); }
    if (p.etapes) { const [txt, ta] = etapeTxt(p, t); g.fillStyle = 'rgba(13,11,9,.75)'; g.fillRect(0, 1340, W, 200); titrePop(txt, 1440, t, ta, 92); }
  }

  // la honte : le visage rougit
  function honte(p, t) {
    const k = eo(pr(t, p.a, .6)), tr = (rnd(t * 50) - .5) * 10 * (1 - k * .5);
    g.save(); g.translate(tr, 0);
    S.d.tete(560, 820, 330, { trait: CREME, fond: '#1b1712', ep: 10 });
    g.save(); g.beginPath(); g.rect(0, lerp(1150, 480, k), W, 900); g.clip(); g.globalAlpha = .85;
    S.d.tete(560, 820, 330, { trait: ROUGE, fond: ROUGE, ep: 10 }); g.restore();
    g.restore();
    const kt = back(pr(t, p.a + .1, .3)); g.save(); g.translate(W / 2, 1400); g.scale(lerp(2, 1, kt), lerp(2, 1, kt));
    S.texte('LA HONTE', 0, 0, { taille: 170, coul: ROUGE, contour: NOIR, contourL: 14 }); g.restore();
  }

  // un portrait et sa citation, tapée au fil de la voix (aq = repère où commence la citation)
  function cite(p, t) {
    const k = eo(pr(t, p.a, .35));
    O.carte(p.img, W / 2 + lerp(260, 0, k), 620, 500, 620, lerp(.12, -.03, k), 1.05 + (t - p.a) * .03, .5, .35, { lum: .95 });
    S.texte(p.nom, W / 2, 1010, { taille: 92, coul: OR, contour: NOIR, contourL: 10 });
    const lignes = p.q.split('|'), tot = lignes.join('').length, n = Math.floor(cl((t - tps(p.aq || p.a)) / (p.duree || 1.6)) * tot);
    let c = 0; lignes.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte(vis, W / 2, 1150 + i * 86, { taille: 66, police: 'Spectral', it: true, poids: 500, coul: CREME, max: 980 }); });
    if (p.src) { const ks = eo(pr(t, tps(p.aq || p.a) + (p.duree || 1.6), .4)); g.save(); g.globalAlpha = ks;
      S.texte(p.src, W / 2, 1170 + lignes.length * 86, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: '#b8ad97', max: 960 }); g.restore(); }
  }

  // Raskolnikov : ni témoin ni preuve… sauf lui-même (son ombre le juge)
  function proces(p, t) {
    O.fondImg('raskolnikov', 1.3, .5, .4, .25);
    O.petitTitre('CRIME ET CHÂTIMENT · DOSTOÏEVSKI', 430);
    if (p.mode !== 'sauf') {
      (p.lignes || []).forEach(([r, s], i) => { const tr = tps(r); if (t < tr) return; const y = 800 + i * 260, k = back(pr(t, tr, .3));
        g.save(); g.translate(W / 2, y); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k)); S.texte(s, -60, 0, { taille: 96, coul: CREME, contour: NOIR, contourL: 10, max: 760 }); g.restore();
        O.tampon('✗', 900, y, pr(t, tr + .2, .3), .1, 90); });
    } else {
      const ks = t >= tps(p.sauf) ? eo(pr(t, tps(p.sauf), .45)) : 0;
      // son ombre se dresse derrière lui
      if (ks > 0) { g.save(); g.globalAlpha = ks * .9; S.d.tete(640 - ks * 40, 1000 - ks * 30, 300 * (1 + ks * .25), { trait: ROUGE, fond: 'rgba(200,55,45,.35)', ep: 10 }); g.restore(); }
      S.d.tete(540, 1020, 260, { trait: CREME, fond: '#1b1712', ep: 10 });
      S.texte('PERSONNE NE L’ACCUSE…', W / 2, 600, { taille: 82, coul: CREME, contour: NOIR, contourL: 10, max: 980 });
      if (ks > 0) { const k = back(pr(t, tps(p.sauf), .3)); g.save(); g.translate(W / 2, 1450); g.scale(lerp(2, 1, k), lerp(2, 1, k));
        S.texte('SAUF LUI.', 0, 0, { taille: 160, coul: ROUGE, contour: NOIR, contourL: 14 }); g.restore(); }
    }
  }

  return { chrono, foot, doute, logique, noms, trous, serrure, honte, cite, proces };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono') { if (p.run) for (let x = p.a; x < p.b - .1; x += 1) L.push([x, 'tic', .5]); else L.push([p.a + .1, 'tic', .4]); }
  if (p.type === 'foot') { if (p.replay) { L.push([p.a, 'rembobine', .7]); if (p.bulle) L.push([tps(p.bulle), 'pop', .45]); } else L.push([p.a + .35, 'frappe', .8]); }
  if (p.type === 'doute') p.items.forEach(([r]) => L.push([tps(r) + .2, 'buzz', .3]));
  if (p.type === 'logique') p.etapes.forEach(([r]) => L.push([r ? tps(r) : p.a, 'blip', .45]));
  if (p.type === 'noms') p.noms.forEach(([r, , bon]) => L.push([tps(r), 'stylo', .35], [tps(r) + .5, bon ? 'valide' : 'lame', bon ? .7 : .4]));
  if (p.type === 'trous') { (p.trous || []).forEach(([r]) => L.push([tps(r), 'pop', .5])); if (p.insc) L.push([tps(p.insc), 'montee', .5]); }
  if (p.type === 'serrure') { L.push([p.a, 'souffle', .35]); (p.pas || []).forEach(r => L.push([tps(r), 'frappe', .45])); if (p.voit) L.push([tps(p.voit), 'coeur', .9], [tps(p.voit) + .6, 'coeur', .9]); }
  if (p.type === 'honte') L.push([p.a, 'souffle', .6]);
  if (p.type === 'cite') { L.push([p.a, 'papier', .4]); const d = p.duree || 1.6, n = p.q.length; for (let k = 0; k < n; k += 6) L.push([tps(p.aq || p.a) + d * k / n, 'tic', .2]); }
  if (p.type === 'proces') { if (p.mode === 'sauf') { if (p.sauf) L.push([tps(p.sauf), 'lame', .6]); } else (p.lignes || []).forEach(([r]) => L.push([tps(r) + .2, 'tampon', .7])); }
};
