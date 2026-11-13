// Plans propres au short Amish (« Un seul couple »), dans le style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// L'allèle muté est toujours dessiné en rouge ; symboles de généalogie : carré = homme, rond = femme,
// demi-rempli = porteur sain (un exemplaire), plein = atteint (deux exemplaires).
window.SANS_ST_A = ['bacsvt'];
window.PROPRES_A = ['arbre', 'village', 'traversee', 'chromo', 'syndrome', 'frequence', 'echantillon', 'derive', 'bacsvt'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const SOMBRE = '#1b1712';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };
  const ligne = (x0, y0, x1, y1, k, coul, ep) => { if (k <= 0) return; g.strokeStyle = coul; g.lineWidth = ep; g.lineCap = 'round'; g.beginPath(); g.moveTo(x0, y0); g.lineTo(lerp(x0, x1, k), lerp(y0, y1, k)); g.stroke(); };

  // ---------- arbre de descendance du couple fondateur
  // n = [x, y, parent, porteur (0/1), homme]
  const RACINE = [540, 420];
  const G = [
    [[270, 630, -1, 1, 1], [540, 630, -1, 0, 0], [810, 630, -1, 1, 0]],
    [[170, 840, 0, 1, 0], [370, 840, 0, 0, 1], [470, 840, 1, 0, 0], [640, 840, 1, 0, 1], [740, 840, 2, 1, 1], [920, 840, 2, 1, 0]],
    [[140, 1050, 0, 0, 1], [320, 1050, 0, 1, 0], [470, 1050, 2, 0, 1], [620, 1050, 3, 0, 0], [800, 1050, 4, 1, 1], [960, 1050, 5, 0, 0]],
  ];
  const ENFANT = [560, 1270];
  const AUTRES = [[[180, 1270], 0], [[930, 1270], 5]];   // d'autres familles atteintes (meme)
  function noeud(x, y, homme, etat, k = 1, r = 34) {
    if (k <= 0) return;
    g.save(); g.translate(x, y); const s = back(k); g.scale(s, s);
    const forme = () => { g.beginPath(); if (homme) g.rect(-r, -r, 2 * r, 2 * r); else g.arc(0, 0, r, 0, 7); };
    forme(); g.fillStyle = SOMBRE; g.fill();
    if (etat === 1) { g.save(); forme(); g.clip(); g.fillStyle = ROUGE; g.fillRect(-r, -r, r, 2 * r); g.restore(); }
    if (etat === 2) { forme(); g.fillStyle = ROUGE; g.shadowColor = ROUGE; g.shadowBlur = 30; g.fill(); g.shadowBlur = 0; }
    forme(); g.strokeStyle = CREME; g.lineWidth = 5; g.stroke();
    g.restore();
  }
  function couple(k, lueur) {
    const [x, y] = RACINE;
    if (lueur) { g.save(); g.shadowColor = ROUGE; g.shadowBlur = 50 * lueur; rond(x, y, 120, 'rgba(200,55,45,.18)'); g.restore(); }
    ligne(x - 70, y, x + 70, y, k, CREME, 6);
    noeud(x - 80, y, 1, 0, k, 40); noeud(x + 80, y, 0, 0, k, 40);
  }
  // p.etape : 'hook' | 'transmet' | 'rencontre' | 'enfant' | 'meme' | 'couple'
  function arbre(p, t) {
    const e = p.etape, anim = e === 'hook' || e === 'transmet', lt = t - p.a;
    g.save();
    const lueur = e === 'hook' || e === 'couple' ? .6 + .4 * Math.sin(t * 5) : e === 'meme' ? .5 : 0;
    couple(anim ? eo(pr(lt, 0, .3)) : 1, lueur);
    // générations (estompées quand on revient au couple)
    if (e === 'couple') g.globalAlpha = lerp(1, .4, eo(pr(t, p.a, .5)));
    G.forEach((row, gi) => row.forEach(([x, y, par, port, homme], i) => {
      const k = anim ? pr(lt, .25 + gi * .3 + i * .04, .3) : 1;
      const [px, py] = par < 0 ? RACINE : G[gi - 1][par];
      const ppor = par < 0 ? 1 : G[gi - 1][par][3];
      const rouge = port && ppor && (e !== 'hook' || true);
      ligne(px, py + 40, x, y - 36, k, rouge ? 'rgba(200,55,45,.85)' : 'rgba(239,230,210,.45)', rouge ? 7 : 4);
      noeud(x, y, homme, port, k);
    }));
    // les deux porteurs se marient, puis un enfant atteint
    const [a, b] = [G[2][1], G[2][4]];
    if (e !== 'hook' && e !== 'transmet') {
      const km = e === 'rencontre' ? eo(pr(t, p.a + .2, .6)) : 1;
      g.save(); g.strokeStyle = OR; g.lineWidth = 7; g.shadowColor = OR; g.shadowBlur = 20; g.beginPath();
      for (let i = 0; i <= 30 * km; i++) { const u = i / 30, x = lerp(a[0], b[0], u), y = a[1] + 40 + Math.sin(u * Math.PI) * 70; i ? g.lineTo(x, y) : g.moveTo(x, y); }
      g.stroke(); g.restore();
      if (e === 'rencontre') { pop(pr(t, p.a + .1, .3), a[0], a[1] - 75, () => S.texte('PORTEUR', 0, 0, { taille: 32, coul: ROUGE, esp: 3 }));
        pop(pr(t, p.a + .25, .3), b[0], b[1] - 75, () => S.texte('PORTEUSE', 0, 0, { taille: 32, coul: ROUGE, esp: 3 })); }
    }
    if (e === 'enfant' || e === 'meme' || e === 'couple') {
      const ke = e === 'enfant' ? pr(t, tps(p.enfant || p.a), .35) : 1;
      ligne(ENFANT[0], 1050 + 105, ENFANT[0], ENFANT[1] - 40, ke * 2, OR, 6);
      noeud(ENFANT[0], ENFANT[1], 1, 2, ke, 40);
    }
    if (e === 'meme' || e === 'couple') {
      AUTRES.forEach(([[x, y], par], i) => { const k = e === 'meme' ? pr(t, p.a + .2 + i * .25, .3) : 1;
        const [px, py] = G[2][par]; ligne(px, py + 36, x, y - 40, k, 'rgba(239,230,210,.45)', 4); noeud(x, y, i, 2, k, 40); });
      // les fils d'or remontent au couple
      const ko = e === 'meme' ? eo(pr(t, p.a + .7, .8)) : 1;
      [[ENFANT, G[2][1]], [ENFANT, G[2][4]], [AUTRES[0][0], G[2][0]], [AUTRES[1][0], G[2][5]]].forEach(([d, n]) => {
        let cur = n, pts = [d, [n[0], n[1]]], gi = 2;
        while (gi >= 0) { const par = cur[2]; const nx = par < 0 ? RACINE : G[gi - 1][par]; pts.push([nx[0], nx[1]]); if (par < 0) break; cur = nx; gi--; }
        g.save(); g.strokeStyle = OR; g.lineWidth = 5; g.globalAlpha = .9; g.setLineDash([14, 12]); g.lineDashOffset = -t * 60; g.beginPath();
        const n2 = Math.max(2, Math.ceil(pts.length * ko)); pts.slice(0, n2).forEach(([x, y], i) => i ? g.lineTo(x, y) : g.moveTo(x, y)); g.stroke(); g.restore();
      });
    }
    if (e === 'couple') { g.globalAlpha = 1; couple(1, 1); const k = pr(t, p.a + .2, .4); g.save(); g.strokeStyle = OR; g.lineWidth = 8; g.shadowColor = OR; g.shadowBlur = 25;
      g.beginPath(); g.ellipse(RACINE[0], RACINE[1], 190 + 8 * Math.sin(t * 6), 90, 0, -Math.PI / 2, -Math.PI / 2 + 6.3 * k); g.stroke(); g.restore();
      pop(pr(t, p.a + .5, .3), RACINE[0], RACINE[1] - 130, () => S.texte('LE COUPLE FONDATEUR', 0, 0, { taille: 44, coul: OR, esp: 4, contour: NOIR, contourL: 8 })); }
    g.restore();
    if (p.t) deux(p.t, 1480, 104);
  }

  // ---------- personnages (silhouettes sobres)
  function perso(x, y, s, o = {}) {
    g.save(); g.translate(x, y); g.scale(s, s);
    g.fillStyle = SOMBRE; g.strokeStyle = o.coul || CREME; g.lineWidth = 6;
    g.beginPath(); g.arc(0, -150, 42, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(-55, 0); g.lineTo(-48, -80); g.quadraticCurveTo(0, -112, 48, -80); g.lineTo(55, 0); g.closePath(); g.fill(); g.stroke();
    if (o.porteur) { g.shadowColor = ROUGE; g.shadowBlur = 40; rond(0, -50, 24 * o.porteur, ROUGE); g.shadowBlur = 0; rond(0, -50, 24 * o.porteur + 14 + 10 * Math.sin((o.t || 0) * 6), null, ROUGE, 4); }
    g.restore();
  }
  // la communauté : p.mode 'fonde' (les immigrants arrivent) | 'cercle' (un groupe fermé) ; p.porteur : repère
  function village(p, t) {
    const n = 8;
    g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 4; g.beginPath(); g.moveTo(60, 1180); g.lineTo(1020, 1180); g.stroke();
    // grange stylisée
    g.save(); g.strokeStyle = 'rgba(217,180,90,.5)'; g.lineWidth = 6; g.beginPath(); g.moveTo(380, 760); g.lineTo(540, 600); g.lineTo(700, 760); g.lineTo(700, 960); g.lineTo(380, 960); g.closePath(); g.stroke();
    g.beginPath(); g.rect(500, 860, 80, 100); g.stroke(); g.restore();
    const kp = p.porteur ? pr(t, tps(p.porteur), .4) : 0;
    for (let i = 0; i < n; i++) {
      let x, y, s = .95;
      if (p.mode === 'fonde') { const k = eo(pr(t, p.a + i * .1, .7)); x = lerp(-150, 140 + i * 115, k); y = 1170 + (i % 2) * 30; }
      else { const a = Math.PI / 2 + (i / n) * 2 * Math.PI; x = 540 + Math.cos(a) * 330; y = 1000 + Math.sin(a) * 200 + 100; s = .8 + .2 * (Math.sin(a) + 1) / 2; }
      perso(x, y, s, { porteur: i === 0 && kp ? back(kp) : 0, t });
    }
    if (p.mode === 'cercle') {
      const k = eo(pr(t, p.a + .1, .6)); g.save(); g.strokeStyle = OR; g.lineWidth = 7; g.setLineDash([26, 18]); g.lineDashOffset = -t * 30;
      g.beginPath(); g.ellipse(540, 1050, 470, 300, 0, 0, 6.3 * k); g.stroke(); g.restore();
    }
    if (p.t) deux(p.t, 1440, 104);
  }

  // ---------- la traversée de l'Atlantique
  function bateau(x, y, s, t) {
    g.save(); g.translate(x, y + Math.sin(t * 4) * 6); g.rotate(Math.sin(t * 3) * .04); g.scale(s, s);
    g.fillStyle = '#3a2a1c'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-120, 0); g.lineTo(120, 0); g.lineTo(90, 50); g.lineTo(-90, 50); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(0, 0); g.lineTo(0, -170); g.stroke();
    g.fillStyle = CREME; g.beginPath(); g.moveTo(8, -160); g.quadraticCurveTo(80, -100, 8, -20); g.closePath(); g.fill();
    g.beginPath(); g.moveTo(-8, -150); g.quadraticCurveTo(-70, -95, -8, -30); g.closePath(); g.fill();
    g.fillStyle = ROUGE; g.beginPath(); g.moveTo(0, -170); g.lineTo(40, -160); g.lineTo(0, -150); g.fill();
    g.restore();
  }
  function traversee(p, t) {
    const k = eo(pr(t, p.a + .1, Math.max(.8, (p.b - p.a) * .9)));
    // côtes
    g.save(); g.fillStyle = '#2a241d'; g.strokeStyle = 'rgba(239,230,210,.7)'; g.lineWidth = 5;
    g.beginPath(); g.moveTo(1080, 450); g.bezierCurveTo(930, 520, 980, 640, 900, 720); g.bezierCurveTo(860, 800, 950, 900, 880, 1000); g.lineTo(1080, 1100); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(0, 420); g.bezierCurveTo(150, 520, 90, 650, 170, 760); g.bezierCurveTo(220, 840, 120, 960, 180, 1080); g.lineTo(0, 1120); g.closePath(); g.fill(); g.stroke();
    g.restore();
    S.texte('EUROPE', 950, 790, { taille: 42, coul: OR, esp: 6 });
    S.texte('AMÉRIQUE', 150, 600, { taille: 38, coul: OR, esp: 4 });
    S.texte('Pennsylvanie', 150, 900, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: CREME });
    // vagues
    g.strokeStyle = 'rgba(239,230,210,.18)'; g.lineWidth = 3;
    for (let r = 0; r < 6; r++) { g.beginPath(); for (let x = 220; x <= 860; x += 10) g.lineTo(x, 560 + r * 90 + Math.sin(x * .03 + t * 2 + r) * 8); g.stroke(); }
    // route
    const pt = u => [lerp(880, 200, u), 760 - Math.sin(u * Math.PI) * 200 + u * 80];
    g.save(); g.setLineDash([18, 14]); g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath();
    for (let i = 0; i <= 40 * k; i++) { const [x, y] = pt(i / 40); i ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke(); g.restore();
    const [bx, by] = pt(k); bateau(bx, by - 10, .7, t);
    if (p.t) deux(p.t, 1340, 100);
  }

  // ---------- une paire de chromosomes homologues ; p.copies = nombre d'allèles mutés (1 ou 2)
  function chromo(p, t) {
    const k = eo(pr(t, p.a, .35));
    [[400, 0], [680, 1]].forEach(([x, i]) => {
      g.save(); g.translate(x, lerp(1300, 820, k));
      g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 7;
      g.beginPath(); g.roundRect(-55, -330, 110, 660, 55); g.fill(); g.stroke();
      g.fillStyle = 'rgba(239,230,210,.18)'; [-250, -170, -40, 60, 190, 260].forEach(y => g.fillRect(-52, y, 104, 22));
      g.strokeStyle = CREME; g.beginPath(); g.moveTo(-55, -20); g.quadraticCurveTo(0, 15, 55, -20); g.stroke();
      const mute = i < p.copies, km = mute ? pr(t, p.a + .3 + i * .25, .3) : 1;
      g.fillStyle = mute && km > 0 ? ROUGE : OR; if (mute && km > 0) { g.shadowColor = ROUGE; g.shadowBlur = 30 * km; }
      g.fillRect(-54, -120, 108, 46); g.shadowBlur = 0;
      g.restore();
    });
    S.texte(p.copies === 1 ? 'normal' : 'muté', 830, 720, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: p.copies === 1 ? OR : ROUGE, align: 'left' });
    S.texte('muté', 250, 720, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: ROUGE, align: 'right' });
    O.petitTitre(p.copies === 1 ? 'PORTEUR SAIN · UN EXEMPLAIRE' : 'DEUX EXEMPLAIRES', 400, p.copies === 1 ? OR : ROUGE);
    if (p.t) deux(p.t, 1340, 100);
  }

  // ---------- le syndrome : p.etape 'nom' | 'signes' (repères p.taille et p.doigt)
  function main6(x, y, s) {
    g.save(); g.translate(x, y); g.scale(s, s); g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 7; g.lineJoin = 'round';
    // pouce, puis paume par-dessus
    g.save(); g.translate(-80, 130); g.rotate(-.8); g.beginPath(); g.roundRect(-28, -190, 56, 200, 28); g.fill(); g.stroke(); g.restore();
    g.beginPath(); g.roundRect(-110, -40, 230, 230, 60); g.fill(); g.stroke();
    // quatre doigts + un sixième doigt côté auriculaire
    [[-70, 200], [-15, 230], [40, 215], [92, 180], [140, 130]].forEach(([dx, L], i) => {
      g.save(); g.translate(dx, -30); g.rotate(i === 4 ? .35 : (i - 1.5) * .06); g.beginPath(); g.roundRect(-24, -L, 48, L + 20, 24); g.fill();
      g.strokeStyle = i === 4 ? OR : CREME; g.stroke(); g.restore(); });
    g.restore();
  }
  function syndrome(p, t) {
    if (p.etape === 'nom') {
      O.petitTitre('UN SYNDROME RARE', 600);
      const k = back(pr(t, p.a, .35)); g.save(); g.translate(W / 2, 860); g.scale(lerp(1.5, 1, k), lerp(1.5, 1, k));
      S.texte('ELLIS-VAN', 0, -80, { taille: 150, coul: CREME, contour: NOIR, contourL: 12, max: 960 });
      S.texte('CREVELD', 0, 80, { taille: 170, coul: OR, contour: NOIR, contourL: 12, max: 960 }); g.restore();
      S.texte('une forme de nanisme', W / 2, 1060, { taille: 46, police: 'Spectral', it: true, poids: 400, coul: GRIS });
      return;
    }
    const k1 = pr(t, tps(p.taille), .35), k2 = pr(t, tps(p.doigt), .35);
    // une toise
    g.save(); g.globalAlpha = .35 + .65 * cl(k1 * 2); g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(250, 520); g.lineTo(250, 1240); g.stroke();
    for (let i = 0; i <= 18; i++) { const y = 1240 - i * 40; g.lineWidth = i % 5 ? 3 : 6; g.beginPath(); g.moveTo(250, y); g.lineTo(i % 5 ? 280 : 300, y); g.stroke(); }
    g.restore();
    if (k1 > 0) { const h = lerp(0, 330, eo(k1)); g.fillStyle = OR; g.fillRect(320, 1240 - h, 70, h); g.strokeStyle = 'rgba(239,230,210,.4)'; g.setLineDash([12, 10]); g.lineWidth = 4; g.strokeRect(320, 1240 - 600, 70, 600); g.setLineDash([]);
      S.texte('TRÈS PETITE', 355, 1310, { taille: 40, coul: CREME, esp: 2 }); S.texte('TAILLE', 355, 1360, { taille: 40, coul: CREME, esp: 2 }); }
    if (k2 > 0) { pop(k2, 760, 900, () => main6(0, 0, 1.15)); g.save(); g.globalAlpha = cl(k2 * 2);
      S.texte('UN SIXIÈME', 760, 1310, { taille: 40, coul: OR, esp: 2 }); S.texte('DOIGT', 760, 1360, { taille: 40, coul: OR, esp: 2 }); g.restore(); }
    O.petitTitre('LE SYNDROME D’ELLIS-VAN CREVELD', 400);
  }

  // ---------- fréquences : p.etape 1 (ailleurs : 1 sur 60 000) | 2 (chez les Amish : 7 %)
  function frequence(p, t) {
    if (p.etape === 1) {
      O.petitTitre('AILLEURS DANS LE MONDE', 400);
      for (let i = 0; i < 1600; i++) { const x = 120 + (i % 40) * 21.5, y = 520 + Math.floor(i / 40) * 15; g.fillStyle = 'rgba(239,230,210,.28)'; g.fillRect(x, y, 6, 6); }
      const kr = pr(t, p.a + .4, .3); if (kr > 0) { g.save(); g.shadowColor = ROUGE; g.shadowBlur = 30; rond(120 + 27 * 21.5 + 3, 520 + 22 * 15 + 3, 6 + 18 * (1 - kr) + 4, ROUGE); g.restore(); }
      const k = back(pr(t, p.a + .5, .35)); g.save(); g.translate(W / 2, 1300); g.scale(k, k);
      S.texte('1 / 60 000', 0, 0, { taille: 170, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 12 }); g.restore();
      S.texte('naissances, au plus', W / 2, 1430, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME });
    } else {
      O.petitTitre('CHEZ LES AMISH DE PENNSYLVANIE', 400, ROUGE);
      const nr = Math.floor(7 * cl((t - p.a - .3) / .9));
      const rouges = [3, 17, 38, 44, 61, 76, 92];
      for (let i = 0; i < 100; i++) { const x = 225 + (i % 10) * 70, y = 540 + Math.floor(i / 10) * 70, r = rouges.indexOf(i);
        const on = r >= 0 && r < nr; if (on) { g.shadowColor = ROUGE; g.shadowBlur = 24; }
        rond(x, y, 24, on ? ROUGE : 'rgba(239,230,210,.25)'); g.shadowBlur = 0; }
      const k = back(pr(t, p.a + 1.2, .35)); g.save(); g.translate(W / 2, 1320); g.scale(k, k);
      S.texte('7 %', 0, 0, { taille: 220, police: 'Spectral', poids: 600, coul: ROUGE, contour: NOIR, contourL: 14 }); g.restore();
      S.texte('des allèles · q = 0,07', W / 2, 1470, { taille: 52, police: 'Spectral', it: true, poids: 400, coul: CREME });
    }
  }

  // ---------- l'effet fondateur : quelques billes tirées au hasard d'un grand bocal
  function bocal(x, y, w, h) { g.save(); g.strokeStyle = CREME; g.lineWidth = 7; g.beginPath(); g.moveTo(x - w / 2, y - h / 2); g.lineTo(x - w / 2, y + h / 2 - 30);
    g.quadraticCurveTo(x - w / 2, y + h / 2, x - w / 2 + 30, y + h / 2); g.lineTo(x + w / 2 - 30, y + h / 2); g.quadraticCurveTo(x + w / 2, y + h / 2, x + w / 2, y + h / 2 - 30); g.lineTo(x + w / 2, y - h / 2); g.stroke(); g.restore(); }
  const TEINTES = [CREME, OR, '#8d8371', '#5f7f8c'];
  function echantillon(p, t) {
    bocal(300, 900, 420, 560); bocal(820, 1000, 240, 340);
    S.texte('LA POPULATION', 300, 560, { taille: 38, coul: CREME, esp: 4 }); S.texte('D’ORIGINE', 300, 605, { taille: 38, coul: CREME, esp: 4 });
    S.texte('LES', 820, 760, { taille: 38, coul: OR, esp: 4 }); S.texte('FONDATEURS', 820, 805, { taille: 38, coul: OR, esp: 4 });
    const pris = [5, 12, 23, 31, 47, 58, 66, 71], rouge = 47;
    for (let i = 0; i < 84; i++) {
      let x = 125 + (i % 12) * 32 + (Math.floor(i / 12) % 2) * 14, y = 1145 - Math.floor(i / 12) * 34, c = i === rouge ? ROUGE : TEINTES[Math.floor(rnd(i * 3.1) * 4)];
      const j = pris.indexOf(i);
      if (j >= 0) { const k = eo(pr(t, p.a + .2 + j * .12, .5)); const tx = 740 + (j % 4) * 50, ty = 1140 - Math.floor(j / 4) * 50;
        x = lerp(x, tx, k); y = lerp(y, ty, k) - Math.sin(k * Math.PI) * 260; }
      if (i === rouge) { g.shadowColor = ROUGE; g.shadowBlur = 22; }
      rond(x, y, 14, c); g.shadowBlur = 0;
    }
    if (p.t) deux(p.t, 1420, 100);
  }

  // ---------- dérive génétique : fréquences qui errent au hasard, génération après génération
  function derive(p, t) {
    const x0 = 140, x1 = 980, y0 = 1180, y1 = 560, k = eo(pr(t, p.a + .1, 1.2));
    g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(x0, y1 - 30); g.lineTo(x0, y0); g.lineTo(x1 + 20, y0); g.stroke();
    S.texte('fréquence', x0 + 10, y1 - 60, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: CREME, align: 'left' });
    S.texte('générations', x1, y0 + 50, { taille: 38, police: 'Spectral', it: true, poids: 400, coul: CREME, align: 'right' });
    [[.3, ROUGE, 1], [.3, OR, 2], [.3, '#8d8371', 3]].forEach(([f0, c, s]) => {
      let f = f0; g.strokeStyle = c; g.lineWidth = c === ROUGE ? 8 : 5; g.beginPath(); g.moveTo(x0, lerp(y0, y1, f));
      const n = 30; for (let i = 1; i <= n * k; i++) { f = cl(f + (rnd(i * 7 + s * 13) - .5) * .22 + (s === 1 ? .025 : s === 3 ? -.02 : 0)); g.lineTo(lerp(x0, x1, i / n), lerp(y0, y1, f)); }
      g.stroke();
    });
    S.texte('petite population', W / 2, 470, { taille: 50, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    if (p.t) deux(p.t, 1400, 110);
  }

  // ---------- copie de bac de SVT
  function bacsvt(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1500, 900, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-400, -480, 800, 960); g.shadowColor = 'transparent';
    S.texte('BACCALAURÉAT', 0, -380, { taille: 50, coul: NOIR, esp: 6 });
    S.texte('SCIENCES DE LA VIE ET DE LA TERRE', 0, -315, { taille: 32, coul: GRIS, esp: 4, poids: 600, max: 700 });
    g.fillStyle = NOIR; g.fillRect(-320, -260, 640, 3);
    S.texte('Sujet type', -320, -195, { taille: 40, coul: GRIS, align: 'left', police: 'Spectral', it: true, poids: 400 });
    const L = p.sujet; L.forEach((s, i) => S.texte(s, 0, -110 + i * 74, { taille: 60, police: 'Spectral', poids: 600, coul: NOIR, max: 700 }));
    const yb = -110 + L.length * 74;
    for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(0,0,0,.12)'; g.fillRect(-320, yb + 30 + i * 50, 640 - (i === 3 ? 260 : 0), 6); }
    const kc = pr(t, p.a + .35, .5), cy = -110 + (L.length - 1) * 37; g.strokeStyle = ROUGE; g.lineWidth = 9;
    g.beginPath(); g.ellipse(0, cy, 380, 60 + L.length * 40, -.04, -1.5, -1.5 + kc * 6.6); g.stroke();
    g.restore();
    O.multi([['SUJET TYPE ', CREME], ['BAC', ROUGE]], 1560, 110);
  }

  return { arbre, village, traversee, chromo, syndrome, frequence, echantillon, derive, bacsvt };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'arbre') {
    if (p.etape === 'hook' || p.etape === 'transmet') for (let k = 0; k < 4; k++) L.push([p.a + .25 + k * .3, 'blip', .3]);
    if (p.etape === 'rencontre') L.push([p.a + .2, 'montee', .4]);
    if (p.etape === 'enfant') L.push([tps(p.enfant || p.a), 'coeur', .8], [tps(p.enfant || p.a) + .55, 'coeur', .8]);
    if (p.etape === 'meme') L.push([p.a + .7, 'whoosh', .45]);
    if (p.etape === 'couple') L.push([p.a + .3, 'valide', .5]);
  }
  if (p.type === 'village') { if (p.mode === 'fonde') L.push([p.a, 'frotte', .35]); else L.push([p.a + .1, 'souffle', .35]); if (p.porteur) L.push([tps(p.porteur), 'coeur', .8]); }
  if (p.type === 'traversee') L.push([p.a + .1, 'whoosh', .45], [p.a + .5, 'souffle', .3]);
  if (p.type === 'chromo') for (let i = 0; i < p.copies; i++) L.push([p.a + .3 + i * .25, 'bip', .45]);
  if (p.type === 'syndrome') { if (p.etape === 'nom') L.push([p.a, 'papier', .4]); else { L.push([tps(p.taille), 'pop', .4], [tps(p.doigt), 'pop', .5]); } }
  if (p.type === 'frequence') { if (p.etape === 1) L.push([p.a + .4, 'bip', .4]); else for (let k = 0; k < 7; k++) L.push([p.a + .3 + k * .13, 'blip', .35]); }
  if (p.type === 'echantillon') for (let j = 0; j < 8; j += 2) L.push([p.a + .2 + j * .12, 'pop', .3]);
  if (p.type === 'derive') L.push([p.a + .1, 'montee', .35]);
  if (p.type === 'bacsvt') L.push([p.a, 'papier', .5], [p.a + .35, 'stylo', .6]);
};
