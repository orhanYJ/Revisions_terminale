// Plans propres au short Trotski (« Sauf les amis »), dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
// Aucune violence montrée : le piolet apparaît, l'écran se coupe ; ni blessure ni sang.
window.SANS_ST_A = ['exil', 'dossier', 'deuil', 'article'];
window.PROPRES_A = ['etoile', 'trotski', 'duel', 'expulse', 'exil', 'maison', 'porte', 'jeune', 'article', 'imper', 'bureau', 'piolet', 'deuil', 'dossier', 'monde'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const NUIT = '#10141c', MUR = '#3a2f25';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const sous = (s, y) => S.texte(s, W / 2, y, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8 });

  // tête de Trotski au trait : cheveux en broussaille, lunettes rondes, barbiche ; regard vers la droite si dir = 1
  function tete(cx, cy, s, o = {}) {
    g.save(); g.translate(cx, cy); g.scale(s * (o.dir === -1 ? -1 : 1), s);
    g.lineJoin = 'round'; g.lineCap = 'round';
    g.fillStyle = o.fond || '#1b1712'; g.strokeStyle = o.trait || CREME; g.lineWidth = 7 / s;
    // cheveux
    g.beginPath(); for (let i = 0; i <= 16; i++) { const a = Math.PI * (1.05 + i / 16 * .95), r = 128 + (i % 2 ? 18 : 0); g.lineTo(Math.cos(a) * r - 5, Math.sin(a) * r * .95 - 25); } g.closePath(); g.fill(); g.stroke();
    // visage
    g.beginPath(); g.moveTo(-95, -40); g.quadraticCurveTo(-100, 70, -40, 120); g.lineTo(40, 125); g.quadraticCurveTo(100, 70, 98, -40); g.quadraticCurveTo(0, -80, -95, -40); g.fill(); g.stroke();
    // barbiche et moustache
    g.fillStyle = o.trait || CREME;
    g.beginPath(); g.moveTo(-30, 112); g.quadraticCurveTo(0, 210, 30, 112); g.closePath(); g.fill();
    g.beginPath(); g.moveTo(-50, 72); g.quadraticCurveTo(0, 55, 50, 72); g.quadraticCurveTo(0, 90, -50, 72); g.fill();
    // lunettes rondes
    g.strokeStyle = o.verre || OR; g.lineWidth = 6 / s;
    [-42, 42].forEach(x => { g.beginPath(); g.arc(x, 0, 30, 0, 7); g.stroke(); });
    g.beginPath(); g.moveTo(-12, 0); g.lineTo(12, 0); g.stroke();
    g.restore();
  }
  // silhouette en pied (chapeau facultatif) ; (x, y) = pieds
  function silhouette(x, y, h, o = {}) {
    g.save(); g.translate(x, y); const s = h / 600; g.scale(s, s);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || CREME; g.lineWidth = 6 / s * .6;
    g.beginPath(); g.arc(0, -520, 62, 0, 7); g.fill(); g.stroke();
    if (o.chapeau) { g.fillStyle = o.trait || CREME; g.fillRect(-90, -560, 180, 16); g.fillRect(-55, -620, 110, 62); g.fillStyle = o.fond || '#16120e'; }
    g.beginPath(); g.moveTo(-95, -440); g.lineTo(95, -440); g.lineTo(120, -150); g.lineTo(60, -150); g.lineTo(55, 0); g.lineTo(-55, 0); g.lineTo(-60, -150); g.lineTo(-120, -150); g.closePath(); g.fill(); g.stroke();
    if (o.imper) { g.fillStyle = '#8f7a5a'; g.strokeStyle = NOIR; g.lineWidth = 5; g.beginPath(); g.moveTo(95, -380); g.quadraticCurveTo(170, -330, 150, -150); g.lineTo(110, -120); g.quadraticCurveTo(120, -280, 95, -380); g.fill(); g.stroke(); }
    g.restore();
  }
  // étoile rouge
  function etoileD(cx, cy, r, rot) {
    g.save(); g.translate(cx, cy); g.rotate(rot); g.fillStyle = ROUGE; g.strokeStyle = OR; g.lineWidth = 6;
    g.beginPath(); for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * .4 : r; g.lineTo(Math.cos(a) * rr, Math.sin(a) * rr); } g.closePath(); g.fill(); g.stroke(); g.restore();
  }

  function etoile(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .4));
    for (let i = 0; i < 18; i++) { const a = i / 18 * 6.283 + lt * .2; g.fillStyle = i % 2 ? 'rgba(200,55,45,.18)' : 'rgba(217,180,90,.08)';
      g.beginPath(); g.moveTo(W / 2, 800); g.arc(W / 2, 800, 900, a, a + .17); g.closePath(); g.fill(); }
    etoileD(W / 2, 800, 300 * k, Math.sin(lt * .8) * .05);
    if (p.t) deux(p.t, 1360, p.taille || 110);
  }

  // fiche d'identité dessinée
  function trotski(p, t) {
    const k = eo(pr(t, p.a, .4));
    tete(W / 2, lerp(820, 760, k), 2.1);
    const kk = eo(pr(t, p.a + .15, .3)); g.save(); g.translate(lerp(-600, 0, kk), 0);
    g.fillStyle = CREME; g.fillRect(90, 1150, 900, 240);
    S.texte(p.t || 'LÉON TROTSKI', W / 2, 1230, { taille: 110, coul: NOIR, max: 840 });
    S.texte(p.sous || 'révolutionnaire russe', W / 2, 1330, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: ROUGE });
    g.restore();
  }

  // Trotski face à Staline
  function duel(p, t) {
    const k = eo(pr(t, p.a, .4));
    O.carte('staline', lerp(1100, 760, k), 760, 500, 680, .04, 1.25, .5, .3, { lum: .85 });
    tete(lerp(-20, 280, k), 800, 1.3, { dir: 1 });
    const kz = pr(t, p.a + .35, .2); if (kz > 0) { g.save(); g.globalAlpha = kz; g.strokeStyle = ROUGE; g.lineWidth = 14;
      g.beginPath(); g.moveTo(470, 620); g.lineTo(540, 760); g.lineTo(480, 770); g.lineTo(560, 940); g.stroke(); g.restore(); }
    S.texte('TROTSKI', 280, 1090, { taille: 50, coul: CREME, esp: 4 });
    S.texte('STALINE', 760, 1150, { taille: 50, coul: CREME, esp: 4 });
    if (p.t) deux(p.t, 1400, p.taille || 130);
  }

  // p.etape 1 : carte du parti, tampon EXCLU ; 2 : frontière de l'URSS, flèche vers l'extérieur, tampon EXPULSÉ
  function expulse(p, t) {
    const k = eo(pr(t, p.a, .4));
    if (p.etape === 1) {
      g.save(); g.translate(W / 2, lerp(1300, 820, k)); g.rotate(-.05);
      g.fillStyle = '#7a2a22'; g.fillRect(-330, -230, 660, 460); g.strokeStyle = OR; g.lineWidth = 6; g.strokeRect(-300, -200, 600, 400);
      etoileD(0, -80, 70, 0);
      S.texte('CARTE DU PARTI', 0, 60, { taille: 54, coul: OR, esp: 4 }); S.texte('PARTI COMMUNISTE', 0, 130, { taille: 34, coul: CREME, esp: 4 });
      g.restore();
      O.tampon('EXCLU', W / 2, 880, pr(t, p.a + .45, .3), -.15, 160);
      deux('CHASSÉ|DU PARTI', 1400, 110);
    } else {
      // frontière
      g.strokeStyle = ROUGE; g.lineWidth = 8; g.setLineDash([26, 16]); g.beginPath(); g.moveTo(640, 320); g.quadraticCurveTo(560, 800, 680, 1300); g.stroke(); g.setLineDash([]);
      g.fillStyle = 'rgba(200,55,45,.12)'; g.beginPath(); g.moveTo(640, 320); g.quadraticCurveTo(560, 800, 680, 1300); g.lineTo(W, 1300); g.lineTo(W, 320); g.fill();
      S.texte('URSS', 860, 520, { taille: 90, coul: ROUGE, contour: NOIR, contourL: 8 });
      const kx = eo(pr(t, p.a + .1, .9)); silhouette(lerp(860, 260, kx), 1050, 380, { chapeau: true });
      S.d.fleche(760, 1150, lerp(760, 200, kx), 1150, kx, { trait: OR, ep: 12 });
      O.tampon('EXPULSÉ · 1929', W / 2, 1400, pr(t, p.a + .6, .3), -.08, 100);
    }
  }

  // passeport : un tampon par pays, chacun à son repère (p.etapes = [[repère, pays], …])
  function exil(p, t) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1400, 900, k)); g.rotate(.03);
    g.fillStyle = '#e7dcc4'; g.fillRect(-430, -560, 860, 1120); g.strokeStyle = 'rgba(0,0,0,.25)'; g.lineWidth = 3; g.strokeRect(-400, -530, 800, 1060);
    S.texte('VISAS · EXIL', 0, -470, { taille: 44, coul: NOIR, esp: 8 });
    g.restore();
    const pos = [[330, 640, -.2], [740, 800, .15], [340, 1040, .1], [720, 1230, -.12]];
    p.etapes.forEach(([a, pays], i) => {
      const ta = tps(a); if (t < ta) return;
      const [x, y, r] = pos[i]; const coul = i === 3 ? ROUGE : ['#2c4a6b', '#4a3b6b', '#2f5a3a'][i];
      O.tampon(pays, x, y, pr(t, ta, .25), r, 64, coul);
      S.texte(['1929', '1933', '1935', '1937'][i], x, y + 80, { taille: 30, police: 'JetBrains Mono', poids: 500, coul: coul });
    });
  }

  // la maison de Coyoacán ; etat : 'nuit', 'balles', 'murs', 'tours', 'forteresse'
  function maison(p, t) {
    const e = p.etat || 'nuit', lt = t - p.a;
    g.fillStyle = NUIT; g.fillRect(0, 300, W, 1070);
    g.fillStyle = '#e9e0c8'; g.beginPath(); g.arc(860, 470, 60, 0, 7); g.fill(); g.fillStyle = NUIT; g.beginPath(); g.arc(835, 455, 55, 0, 7); g.fill();
    // maison
    g.fillStyle = '#2a241d'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.rect(260, 780, 560, 380); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(230, 790); g.lineTo(540, 640); g.lineTo(850, 790); g.closePath(); g.fill(); g.stroke();
    [[330, 870], [630, 870]].forEach(([x, y]) => { g.fillStyle = e === 'nuit' ? '#c9a24a' : '#3b3227'; g.fillRect(x, y, 120, 110); g.strokeRect(x, y, 120, 110); });
    g.fillStyle = '#16120e'; g.fillRect(490, 1010, 100, 150); g.strokeRect(490, 1010, 100, 150);
    // impacts de balles (aucun blessé montré)
    if (e === 'balles') {
      const n = Math.min(60, Math.floor(lt * 40));
      for (let i = 0; i < n; i++) { const x = 270 + rnd(i * 3.1) * 540, y = 790 + rnd(i * 5.7) * 360; g.fillStyle = NOIR; g.beginPath(); g.arc(x, y, 6, 0, 7); g.fill();
        g.strokeStyle = 'rgba(239,230,210,.5)'; g.lineWidth = 2; g.beginPath(); g.arc(x, y, 11, 0, 7); g.stroke(); }
      if (Math.floor(lt * 18) % 2 === 0 && lt < 1.6) { g.fillStyle = 'rgba(255,230,160,.18)'; g.fillRect(0, 300, W, 1100); }
      for (let i = 0; i < 6; i++) { const ph = ((lt * 3 + i / 6) % 1); g.strokeStyle = `rgba(255,220,140,${1 - ph})`; g.lineWidth = 4;
        g.beginPath(); g.moveTo(1080 - ph * 300, 700 + i * 70); g.lineTo(1080 - ph * 300 - 80, 702 + i * 70); g.stroke(); }
    }
    // murs d'enceinte et miradors
    const hm = e === 'murs' ? eo(pr(t, p.a + .1, .9)) : (e === 'tours' || e === 'forteresse') ? 1 : .25;
    const yM = 1160 - 200 * hm - 80;
    g.fillStyle = MUR; g.strokeStyle = CREME; g.lineWidth = 6; g.fillRect(0, yM, W, 1370 - yM); g.strokeRect(-10, yM, W + 20, 1370 - yM);
    g.strokeStyle = 'rgba(239,230,210,.18)'; g.lineWidth = 3; for (let y = yM + 40; y < 1370; y += 40) { g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); }
    if (e === 'tours' || e === 'forteresse') {
      const ht = e === 'tours' ? eo(pr(t, p.a + .1, .8)) : 1;
      [130, 950].forEach((x, i) => {
        const top = yM - 260 * ht;
        g.fillStyle = MUR; g.strokeStyle = CREME; g.lineWidth = 6; g.fillRect(x - 60, top, 120, yM - top); g.strokeRect(x - 60, top, 120, yM - top);
        g.fillRect(x - 85, top - 20, 170, 40); g.strokeRect(x - 85, top - 20, 170, 40);
        if (ht > .9) { const a = Math.sin(lt * 1.6 + i * 2) * .6 + (i ? -2.4 : -.7); g.save(); g.fillStyle = 'rgba(239,230,210,.12)'; g.beginPath(); g.moveTo(x, top - 10);
          g.lineTo(x + Math.cos(a - .12) * 900, top - 10 + Math.sin(a - .12) * 900); g.lineTo(x + Math.cos(a + .12) * 900, top - 10 + Math.sin(a + .12) * 900); g.closePath(); g.fill(); g.restore(); }
      });
    }
    if (p.t) deux(p.t, 1470, p.taille || 95);
  }

  // la porte de la forteresse ; p.ouvre : repère d'ouverture ; p.visiteur : une silhouette entre ; p.gardes : les gardes saluent
  function porte(p, t) {
    g.fillStyle = NUIT; g.fillRect(0, 300, W, 1070);
    g.fillStyle = MUR; g.strokeStyle = CREME; g.lineWidth = 6; g.fillRect(0, 560, W, 760); g.strokeRect(-10, 560, W + 20, 760);
    g.strokeStyle = 'rgba(239,230,210,.18)'; g.lineWidth = 3; for (let y = 600; y < 1320; y += 40) { g.beginPath(); g.moveTo(0, y); g.lineTo(W, y); g.stroke(); }
    const ko = p.ouvre ? eo(pr(t, tps(p.ouvre), .8)) : 0;
    g.fillStyle = '#c9a24a'; g.globalAlpha = .25 + ko * .5; g.fillRect(360, 760, 360, 560); g.globalAlpha = 1;
    if (p.visiteur) { const kv = eo(pr(t, (p.ouvre ? tps(p.ouvre) : p.a) + .2, 1.4)); silhouette(lerp(980, 560, kv), 1320, lerp(330, 470, kv), { chapeau: true }); }
    // battants
    g.fillStyle = '#4a3a28'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.fillRect(360, 760, 180 * (1 - ko), 560); g.strokeRect(360, 760, 180 * (1 - ko), 560);
    g.fillRect(720 - 180 * (1 - ko), 760, 180 * (1 - ko), 560); g.strokeRect(720 - 180 * (1 - ko), 760, 180 * (1 - ko), 560);
    if (ko < .2) { g.fillStyle = OR; g.fillRect(500, 1000, 80, 30); }
    if (p.gardes) [200, 880].forEach((x, i) => { silhouette(x, 1320, 380, { fond: '#2b2a22' }); const a = Math.sin((t - p.a) * 6 + i) * .5;
      g.save(); g.translate(x + (i ? -40 : 40), 1050); g.rotate(i ? -1.6 - a : 1.6 + a); g.fillStyle = '#2b2a22'; g.strokeStyle = CREME; g.lineWidth = 4; g.fillRect(-10, 0, 20, 110); g.strokeRect(-10, 0, 20, 110); g.restore(); });
    if (p.t) deux(p.t, 1470, p.taille || 95);
  }

  // le jeune homme, fiche « Jacques Mornard » ; p.coeur : un cœur avec une militante
  function jeune(p, t) {
    const k = eo(pr(t, p.a, .5));
    silhouette(lerp(900, 420, k), 1180, 640, { chapeau: true });
    if (p.coeur) { silhouette(700, 1180, 560, { fond: '#2b1f1a' }); const kc = back(pr(t, p.a + .3, .35)); g.save(); g.translate(560, 560); g.scale(kc * 3, kc * 3);
      g.fillStyle = ROUGE; g.beginPath(); g.moveTo(0, 12); g.bezierCurveTo(-26, -8, -12, -26, 0, -10); g.bezierCurveTo(12, -26, 26, -8, 0, 12); g.fill(); g.restore(); }
    const kk = eo(pr(t, p.a + .2, .35)); g.save(); g.translate(lerp(600, 0, kk), 0);
    g.fillStyle = CREME; g.fillRect(90, 1230, 900, 200);
    S.texte(p.t || 'JACQUES MORNARD', W / 2, 1300, { taille: 90, coul: NOIR, max: 840 });
    S.texte(p.sous || 'un jeune homme charmant', W / 2, 1385, { taille: 48, it: true, poids: 400, police: 'Spectral', coul: ROUGE, max: 840 });
    g.restore();
  }

  // un article à relire, tapé à la machine
  function article(p, t) {
    const k = eo(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, lerp(1300, 860, k)); g.rotate(-.04);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#e9dfc8'; g.fillRect(-380, -470, 760, 940); g.shadowColor = 'transparent';
    S.texte('ARTICLE', 0, -380, { taille: 64, coul: NOIR, esp: 10 });
    S.texte('à relire, s’il vous plaît', 0, -300, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    const n = Math.floor(cl((t - p.a) / 1.6) * 16);
    for (let i = 0; i < n; i++) { g.fillStyle = 'rgba(13,11,9,.75)'; g.fillRect(-300, -210 + i * 42, i % 5 === 4 ? 320 : 600, 10); }
    g.restore();
    deux(p.t || 'UN ARTICLE|À RELIRE', 1480, 100);
  }

  // le soleil, l'imperméable sur le bras ; p.soleil : repère où le cercle rouge entoure l'imperméable
  function imper(p, t) {
    const lt = t - p.a, gr = g.createLinearGradient(0, 300, 0, 1400); gr.addColorStop(0, '#5a4220'); gr.addColorStop(1, '#1b1712'); g.fillStyle = gr; g.fillRect(0, 300, W, 1100);
    g.save(); g.translate(820, 520); g.rotate(lt * .3); g.fillStyle = OR;
    for (let i = 0; i < 12; i++) { g.rotate(Math.PI / 6); g.fillRect(110, -10, 70, 20); } g.restore();
    g.fillStyle = OR; g.beginPath(); g.arc(820, 520, 90, 0, 7); g.fill();
    silhouette(lerp(200, 460, eo(pr(t, p.a, .8))), 1300, 720, { chapeau: true, imper: true });
    if (p.soleil && t >= tps(p.soleil)) { const kc = pr(t, tps(p.soleil), .45); g.strokeStyle = ROUGE; g.lineWidth = 10;
      const x = lerp(200, 460, 1) + 70; g.beginPath(); g.ellipse(x, 1000, 120, 220, .1, -1.5, -1.5 + kc * 6.6); g.stroke(); }
    if (p.t) deux(p.t, 1470, p.taille || 95);
  }

  // le bureau : lampe, papier, Trotski penché, le visiteur debout ; p.penche : il se penche
  function bureau(p, t) {
    g.fillStyle = '#0b0a08'; g.fillRect(0, 300, W, 1100);
    const gl = g.createRadialGradient(560, 900, 30, 560, 900, 520); gl.addColorStop(0, 'rgba(217,180,90,.45)'); gl.addColorStop(1, 'rgba(217,180,90,0)'); g.fillStyle = gl; g.fillRect(0, 300, W, 1100);
    // bureau
    g.fillStyle = '#3a2f25'; g.strokeStyle = CREME; g.lineWidth = 6; g.fillRect(200, 1020, 720, 50); g.strokeRect(200, 1020, 720, 50);
    g.fillRect(230, 1070, 40, 260); g.fillRect(850, 1070, 40, 260);
    // lampe
    g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.moveTo(820, 1020); g.lineTo(780, 820); g.lineTo(700, 790); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.moveTo(640, 760); g.lineTo(740, 760); g.lineTo(720, 820); g.lineTo(660, 820); g.closePath(); g.fill();
    // papier
    g.fillStyle = '#e9dfc8'; g.fillRect(470, 1000, 200, 22);
    // Trotski assis, penché
    const kp = p.penche ? eo(pr(t, p.a + .1, .9)) : 0;
    g.save(); g.translate(560, 1000);
    g.fillStyle = '#1b1712'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(-90, -170); g.lineTo(90, -170); g.lineTo(80, 0); g.lineTo(-80, 0); g.closePath(); g.fill(); g.stroke();
    g.translate(0, -170); g.rotate(kp * .35); tete(0, -120, .7, { dir: 1 });
    g.restore();
    // le visiteur, debout derrière, dans l'ombre
    silhouette(250, 1330, 760, { fond: '#0f0d0a', trait: 'rgba(239,230,210,.55)', chapeau: false, imper: true });
    if (p.t) deux(p.t, 1470, p.taille || 95);
  }

  // l'imperméable, puis le piolet qui apparaît ; flash rouge, puis noir
  function piolet(p, t) {
    const lt = t - p.a, kr = p.revele ? eo(pr(t, tps(p.revele), .35)) : 0;
    g.fillStyle = '#0b0a08'; g.fillRect(0, 300, W, 1100);
    // imperméable
    g.save(); g.translate(540, 860); g.rotate(-.1);
    g.fillStyle = '#8f7a5a'; g.strokeStyle = NOIR; g.lineWidth = 8;
    g.beginPath(); g.moveTo(-260, -260); g.quadraticCurveTo(0, -330, 260, -260); g.lineTo(220, 300); g.quadraticCurveTo(0, 340, -220, 300); g.closePath(); g.fill(); g.stroke();
    g.strokeStyle = 'rgba(13,11,9,.4)'; g.lineWidth = 5; [-120, 0, 120].forEach(x => { g.beginPath(); g.moveTo(x, -280); g.quadraticCurveTo(x + 20, 0, x - 10, 300); g.stroke(); });
    g.restore();
    if (kr > 0) {
      // le piolet glisse hors du manteau
      g.save(); g.translate(lerp(540, 600, kr), lerp(980, 700, kr)); g.rotate(-.5);
      g.fillStyle = '#6b4a2a'; g.strokeStyle = NOIR; g.lineWidth = 5; g.fillRect(-16, -40, 32, 360); g.strokeRect(-16, -40, 32, 360);
      g.fillStyle = '#b8b2a6'; g.beginPath(); g.moveTo(-170, -60); g.lineTo(150, -70); g.lineTo(190, -40); g.lineTo(20, -20); g.lineTo(-20, -20); g.lineTo(-170, -40); g.closePath(); g.fill(); g.stroke();
      g.restore();
      const kf = pr(t, tps(p.revele), .15); if (kf < 1) { g.fillStyle = `rgba(200,55,45,${.5 * (1 - kf)})`; g.fillRect(0, 0, W, H); }
      deux('UN|PIOLET', 1450, 130);
    } else if (p.t) deux(p.t, 1460, p.taille || 95);
  }

  // date de la mort, sobre
  function deuil(p, t) {
    const k = pr(t, p.a + .1, .6);
    g.save(); g.globalAlpha = k;
    S.texte('21 AOÛT 1940', W / 2, 860, { taille: 120, police: 'Spectral', poids: 600, coul: CREME });
    g.fillStyle = CREME; g.fillRect(340, 950, 400, 3);
    S.texte(p.t || 'Tu meurs le lendemain.', W / 2, 1050, { taille: 66, police: 'Spectral', it: true, poids: 400, coul: CREME });
    g.restore();
  }

  // dossier : faux nom barré, vrai nom ; p.vrai, p.agent : repères
  function dossier(p, t) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1300, 900, k)); g.rotate(-.03);
    g.fillStyle = '#d9cba8'; g.fillRect(-440, -560, 880, 1120); g.fillStyle = '#c8b88f'; g.fillRect(-440, -600, 320, 60);
    S.texte('DOSSIER', -280, -570, { taille: 36, coul: NOIR, esp: 6 });
    g.fillStyle = '#1b1712'; g.fillRect(-370, -460, 280, 340); silhouette(-230, -120, 300, { chapeau: true, fond: '#2b2520', trait: '#8d8371' });
    S.texte('NOM :', -50, -400, { taille: 40, coul: GRIS, align: 'left' });
    S.texte('JACQUES', -50, -330, { taille: 64, coul: NOIR, align: 'left' }); S.texte('MORNARD', -50, -260, { taille: 64, coul: NOIR, align: 'left' });
    const tv = p.vrai ? tps(p.vrai) : 1e9;
    if (t >= tv) {
      const kb = eo(pr(t, tv, .25)); g.fillStyle = ROUGE; g.fillRect(-60, -300, 420 * kb, 12);
      const kn = back(pr(t, tv + .1, .3)); g.save(); g.translate(0, 60); g.scale(kn, kn);
      S.texte('VRAI NOM', 0, -40, { taille: 40, coul: GRIS, esp: 6 });
      S.texte('RAMÓN MERCADER', 0, 40, { taille: 90, coul: ROUGE, max: 800 }); g.restore();
    }
    g.restore();
    if (p.agent && t >= tps(p.agent)) O.tampon('AGENT DU NKVD', W / 2, 1250, pr(t, tps(p.agent), .3), -.1, 90);
    if (t < tv) O.tampon('FAUX NOM', 760, 760, pr(t, p.a + .5, .3), .15, 80);
  }

  // Moscou → Mexico sur un globe schématique
  function monde(p, t) {
    const cx = W / 2, cy = 860, R = 420, k = eo(pr(t, p.a + .1, 1.2));
    g.fillStyle = '#14202a'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(cx, cy, R, 0, 7); g.fill(); g.stroke();
    g.strokeStyle = 'rgba(217,180,90,.18)'; g.lineWidth = 3;
    for (let i = -2; i <= 2; i++) { g.beginPath(); g.ellipse(cx, cy, R * Math.abs(Math.cos(i * .5)), R, 0, 0, 7); g.stroke(); g.beginPath(); g.moveTo(cx - R * Math.cos(i * .4), cy + R * Math.sin(i * .4)); g.lineTo(cx + R * Math.cos(i * .4), cy + R * Math.sin(i * .4)); g.stroke(); }
    const A = [cx + 230, cy - 200], B = [cx - 260, cy + 60], C = [cx, cy - 520];
    g.save(); g.strokeStyle = ROUGE; g.lineWidth = 8; g.setLineDash([22, 14]); g.beginPath(); g.moveTo(...A);
    for (let i = 1; i <= 40 * k; i++) { const u = i / 40, x = (1 - u) ** 2 * A[0] + 2 * (1 - u) * u * C[0] + u * u * B[0], y = (1 - u) ** 2 * A[1] + 2 * (1 - u) * u * C[1] + u * u * B[1]; g.lineTo(x, y); }
    g.stroke(); g.restore();
    g.fillStyle = ROUGE; g.beginPath(); g.arc(...A, 16, 0, 7); g.fill(); S.texte('MOSCOU', A[0] + 40, A[1] + 50, { taille: 44, coul: CREME, contour: NOIR, contourL: 6 });
    if (k > .95) { g.fillStyle = OR; g.beginPath(); g.arc(...B, 18, 0, 7); g.fill(); S.texte('MEXICO', B[0] + 20, B[1] + 55, { taille: 44, coul: OR, contour: NOIR, contourL: 6 }); }
    if (p.t) deux(p.t, 1440, p.taille || 110);
  }

  return { etoile, trotski, duel, expulse, exil, maison, porte, jeune, article, imper, bureau, piolet, deuil, dossier, monde };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'etoile') L.push([p.a, 'gong', .5]);
  if (p.type === 'trotski') L.push([p.a + .15, 'papier', .5]);
  if (p.type === 'duel') L.push([p.a + .35, 'lame', .7]);
  if (p.type === 'expulse') L.push(p.etape === 1 ? [p.a + .5, 'tampon', 1] : [p.a + .65, 'tampon', 1]);
  if (p.type === 'exil') p.etapes.forEach(([a]) => L.push([tps(a) + .03, 'tampon', .8]));
  if (p.type === 'maison') { if (p.etat === 'balles') for (let k = 0; k < 14; k++) L.push([p.a + k * .09, 'clic', .6]); if (p.etat === 'murs' || p.etat === 'tours') L.push([p.a + .1, 'montee', .5]); }
  if (p.type === 'porte' && p.ouvre) L.push([tps(p.ouvre), 'frotte', .6]);
  if (p.type === 'jeune') L.push([p.a + .2, 'papier', .4]);
  if (p.type === 'article') for (let k = 0; k < 10; k++) L.push([p.a + k * .15, 'tic', .3]);
  if (p.type === 'imper' && p.soleil) L.push([tps(p.soleil), 'stylo', .5]);
  if (p.type === 'bureau') L.push([p.a, 'coeur', .7], [p.a + .8, 'coeur', .7]);
  if (p.type === 'piolet' && p.revele) L.push([tps(p.revele), 'lame', 1]);
  if (p.type === 'deuil') L.push([p.a + .1, 'souffle', .4]);
  if (p.type === 'dossier') { if (p.vrai) L.push([tps(p.vrai), 'lame', .7]); else L.push([p.a + .5, 'tampon', .8]); if (p.agent) L.push([tps(p.agent) + .05, 'tampon', 1]); }
  if (p.type === 'monde') L.push([p.a + .1, 'whoosh', .5]);
};
