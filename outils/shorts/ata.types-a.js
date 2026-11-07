// Plans propres au short 'Ata (« le vrai Sa Majesté des mouches »), dans le style du modèle A (noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
window.SANS_ST_A = ['sans', 'regles'];
window.PROPRES_A = ['ados', 'ile', 'sans', 'bateau', 'sanscarte', 'tempete', 'compteur', 'pluie', 'gorgee', 'rocher', 'livre',
  'equipes', 'taches', 'dispute', 'feu', 'chute', 'jambe', 'capitaine', 'jumelles', 'funerailles', 'mois', 'regles'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const ROCHE = '#2a231b', MER = '#15120e';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  // apparition « qui claque » d'un texte à l'instant a
  const claque = (txt, x, y, a, t, o) => { if (t < a) return; const k = back(pr(t, a, .28)); g.save(); g.translate(x, y); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k)); g.globalAlpha = cl((t - a) * 6);
    S.texte(txt, 0, 0, Object.assign({ taille: 90, coul: OR, contour: NOIR, contourL: 10, max: 960 }, o)); g.restore(); };
  // valeur courante d'une suite d'étapes [[repère, valeur], …] (repère null = début du plan)
  const etape = (p, t) => { let v = null, ta = p.a, n = 0; p.etapes.forEach(([a, x], i) => { const tt = a ? tps(a) : p.a; if (t >= tt) { v = x; ta = tt; n = i + 1; } }); return { v, ta, n }; };

  // ---------------------------------------------------------------- dessins
  // personnage debout (tête + corps), pied en (x, y), hauteur ~ 2,2 s
  function bonhomme(x, y, s, coul = CREME, o = {}) {
    g.save(); g.translate(x, y); if (o.rot) g.rotate(o.rot);
    g.fillStyle = coul; g.strokeStyle = NOIR; g.lineWidth = s * .06;
    g.beginPath(); g.arc(0, -s * 1.85, s * .32, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.roundRect(-s * .42, -s * 1.45, s * .84, s * 1.45, [s * .4, s * .4, s * .08, s * .08]); g.fill(); g.stroke();
    g.restore();
  }
  // mer : vagues qui bougent, du niveau y jusqu'en bas
  function mer(y, t, amp = 14, coul = MER, n = 3) {
    g.fillStyle = coul; g.beginPath(); g.moveTo(0, H);
    for (let x = 0; x <= W; x += 12) g.lineTo(x, y + Math.sin(x * .012 + t * 2.2) * amp + Math.sin(x * .031 - t * 3.1) * amp * .4);
    g.lineTo(W, H); g.closePath(); g.fill();
    g.strokeStyle = 'rgba(239,230,210,.22)'; g.lineWidth = 3;
    for (let k = 0; k < n; k++) { const yy = y + 60 + k * 90; g.beginPath();
      for (let x = 0; x <= W; x += 12) { const v = yy + Math.sin(x * .016 + t * (1.6 + k * .4) + k) * amp * .6; x ? g.lineTo(x, v) : g.moveTo(x, v); } g.stroke(); }
  }
  // bateau à voile : (x, y) = ligne de flottaison, s = demi-longueur ; o.dechire 0..1 ; o.sansGouv : gouvernail parti
  function bateau(x, y, s, rot, t, o = {}) {
    g.save(); g.translate(x, y); g.rotate(rot);
    g.strokeStyle = CREME; g.lineWidth = 6; g.lineJoin = 'round';
    // mât
    g.beginPath(); g.moveTo(0, 0); g.lineTo(0, -s * 1.7); g.stroke();
    // voile (déchirée : lambeaux qui claquent)
    const d = o.dechire || 0;
    if (d < .5) { g.fillStyle = 'rgba(239,230,210,.9)'; g.beginPath(); g.moveTo(8, -s * 1.6); g.quadraticCurveTo(s * .9, -s * .9, s * .85, -s * .12); g.lineTo(8, -s * .12); g.closePath(); g.fill(); }
    else for (let i = 0; i < 3; i++) { const yy = -s * (1.5 - i * .25), f = Math.sin(t * 18 + i * 2) * s * .12;
      g.fillStyle = 'rgba(239,230,210,.85)'; g.beginPath(); g.moveTo(8, yy); g.lineTo(s * (.45 - i * .08) + f, yy + s * .08 + f * .3); g.lineTo(8, yy + s * .16); g.closePath(); g.fill(); }
    // coque
    g.fillStyle = '#3a2f25'; g.beginPath(); g.moveTo(-s, -s * .1); g.lineTo(s, -s * .1); g.lineTo(s * .72, s * .3); g.lineTo(-s * .78, s * .3); g.closePath(); g.fill(); g.stroke();
    // gouvernail
    if (!o.sansGouv) { g.fillStyle = OR; g.fillRect(-s * 1.04, -s * .05, s * .1, s * .42); }
    g.restore();
  }
  // île de profil : falaise posée sur la mer
  function rocherProfil(cx, y, w, h, coul = ROCHE) {
    g.fillStyle = coul; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(cx - w / 2, y);
    g.lineTo(cx - w * .38, y - h * .55); g.lineTo(cx - w * .2, y - h * .8); g.lineTo(cx - w * .05, y - h); g.lineTo(cx + w * .12, y - h * .92);
    g.lineTo(cx + w * .3, y - h * .7); g.lineTo(cx + w * .4, y - h * .35); g.lineTo(cx + w / 2, y); g.closePath(); g.fill(); g.stroke();
  }
  // île vue de haut : contour irrégulier, plage dorée, rides de l'eau
  function ileHaut(cx, cy, r, t) {
    for (let k = 0; k < 4; k++) { const ph = ((t * .35 + k / 4) % 1); g.strokeStyle = `rgba(239,230,210,${.25 * (1 - ph)})`; g.lineWidth = 4;
      g.beginPath(); g.ellipse(cx, cy, r * (1.05 + ph * .7), r * (.8 + ph * .55), .1, 0, 7); g.stroke(); }
    const forme = (rr) => { g.beginPath(); for (let i = 0; i <= 24; i++) { const a = i / 24 * 6.283, q = rr * (.82 + .18 * rnd(i % 24 + 3)); const x = cx + Math.cos(a) * q, y = cy + Math.sin(a) * q * .78; i ? g.lineTo(x, y) : g.moveTo(x, y); } g.closePath(); };
    g.fillStyle = OR; forme(r); g.fill();
    g.fillStyle = '#3d3427'; forme(r * .8); g.fill(); g.strokeStyle = 'rgba(13,11,9,.5)'; g.lineWidth = 4; forme(r * .5); g.stroke();
  }
  function flamme(x, y, s, t) {
    [[OR, 1], [ROUGE, .7], ['#fff3c4', .38]].forEach(([c, k], i) => { const f = Math.sin(t * 13 + i * 2) * s * .08, h = s * k * (1.4 + Math.sin(t * 9 + i) * .12);
      g.fillStyle = c; g.beginPath(); g.moveTo(x - s * .5 * k, y); g.quadraticCurveTo(x - s * .55 * k, y - h * .5, x + f, y - h); g.quadraticCurveTo(x + s * .55 * k, y - h * .5, x + s * .5 * k, y); g.closePath(); g.fill(); });
  }
  const croix = (x, y, r, k) => { if (k <= 0) return; g.save(); g.strokeStyle = ROUGE; g.lineWidth = 22; g.lineCap = 'round';
    const a = cl(k * 2), b = cl(k * 2 - 1); g.beginPath(); g.moveTo(x - r, y - r); g.lineTo(x - r + 2 * r * a, y - r + 2 * r * a); g.stroke();
    if (b > 0) { g.beginPath(); g.moveTo(x + r, y - r); g.lineTo(x + r - 2 * r * b, y - r + 2 * r * b); g.stroke(); } g.restore(); };
  // fiche d'identité qui glisse (comme le plan « perso » du modèle)
  function fiche(nom, sous, y, k) {
    g.save(); g.translate(lerp(-900, 0, k), 0);
    g.fillStyle = CREME; g.fillRect(90, y - 125, 900, 250);
    S.texte(nom, W / 2, y - 45, { taille: 100, coul: NOIR, max: 840 });
    S.texte(sous, W / 2, y + 55, { taille: 54, it: true, poids: 400, police: 'Spectral', coul: ROUGE });
    g.restore();
  }

  // ---------------------------------------------------------------- plans
  // six ados sur une île (accroche et boucle finale)
  function ados(p, t, l) {
    mer(1080, t, 10);
    rocherProfil(W / 2, 1090, 860, 230, '#2e271e');
    for (let i = 0; i < 6; i++) { const k = back(pr(t, p.a + .08 + i * .09, .25)); if (k <= 0) continue;
      g.save(); g.translate(250 + i * 116, 1000 - (i === 2 || i === 3 ? 40 : 0)); g.scale(k, k); bonhomme(0, 0, 70, i % 2 ? OR : CREME); g.restore(); }
    deux(p.t, 1380, p.taille || 130);
  }
  function ile(p, t, l) {
    const z = lerp(.55, 1, eo(pr(t, p.a, .6)));
    g.save(); g.translate(W / 2, 860); g.scale(z, z); ileHaut(0, 0, 300, t); g.restore();
    deux(p.t, 1400, 120);
  }
  // « pas d'adulte, pas de règles, pas d'État » : trois mots qui tombent, barrés en rouge
  function sans(p, t, l) {
    p.etapes.forEach(([a, txt], i) => { const ta = tps(a); if (t < ta - .02) return;
      const y = 640 + i * 300, der = i === p.etapes.length - 1, k = back(pr(t, ta - .02, .25));
      g.save(); g.translate(W / 2, y); g.scale(lerp(1.7, 1, k), lerp(1.7, 1, k));
      S.texte(txt, 0, 0, { taille: der ? 150 : 120, coul: der ? OR : CREME, contour: NOIR, contourL: 12, max: 960 }); g.restore();
      const kb = eo(pr(t, ta + .18, .2)); if (kb > 0) { g.save(); g.translate(W / 2, y); g.rotate(-.05); g.fillStyle = ROUGE; g.fillRect(-460, -14, 920 * kb, 28); g.restore(); } });
  }
  // le bateau emprunté quitte le port, la nuit
  function bateauPlan(p, t, l) {
    for (let i = 0; i < 40; i++) { const a = .3 + .7 * Math.abs(Math.sin(t * 2 + i)); g.fillStyle = `rgba(239,230,210,${a * .5})`; g.fillRect(rnd(i) * W, 260 + rnd(i + 40) * 600, 4, 4); }
    g.fillStyle = CREME; g.beginPath(); g.arc(820, 420, 60, 0, 7); g.fill(); g.fillStyle = '#0d0b09'; g.beginPath(); g.arc(845, 405, 55, 0, 7); g.fill();
    mer(1050, t, 8);
    bateau(lerp(300, 640, cl(l / 2.2)), 1040 + Math.sin(t * 2) * 8, 150, Math.sin(t * 1.7) * .04, t);
    deux(p.t, 1400, 110);
    if (p.tampon) O.tampon('SANS DEMANDER', W / 2, 640, pr(t, tps(p.tampon), .3), -.1, 100);
  }
  // ni carte ni boussole : deux objets barrés
  function sanscarte(p, t, l) {
    const k1 = eo(pr(t, p.a, .3));
    g.save(); g.globalAlpha = k1; g.translate(300, 860); g.rotate(-.06);
    g.fillStyle = '#e9dfc8'; g.fillRect(-190, -150, 380, 300);
    g.strokeStyle = 'rgba(13,11,9,.5)'; g.lineWidth = 3; [-63, 63].forEach(x => { g.beginPath(); g.moveTo(x, -150); g.lineTo(x, 150); g.stroke(); });
    g.strokeStyle = ROUGE; g.setLineDash([14, 12]); g.lineWidth = 6; g.beginPath(); g.moveTo(-150, 90); g.bezierCurveTo(-60, -80, 40, 120, 140, -90); g.stroke(); g.setLineDash([]);
    g.restore();
    g.save(); g.globalAlpha = k1; g.translate(780, 860);
    g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.arc(0, 0, 150, 0, 7); g.fill(); g.stroke();
    g.rotate(Math.sin(t * 5) * .6); g.fillStyle = ROUGE; g.beginPath(); g.moveTo(0, -115); g.lineTo(24, 0); g.lineTo(-24, 0); g.closePath(); g.fill();
    g.fillStyle = CREME; g.beginPath(); g.moveTo(0, 115); g.lineTo(24, 0); g.lineTo(-24, 0); g.closePath(); g.fill();
    g.restore();
    S.texte('CARTE', 300, 1080, { taille: 60, coul: CREME }); S.texte('BOUSSOLE', 780, 1080, { taille: 60, coul: CREME });
    croix(300, 860, 150, pr(t, tps(p.x1), .3)); croix(780, 860, 150, pr(t, tps(p.x2), .3));
    deux('NI CARTE|NI BOUSSOLE', 1360, 110);
  }
  // la tempête ; p.casse : voile déchirée (p.voile), gouvernail qui part (p.gouv)
  function tempete(p, t, l) {
    O.fondImg('tempete', 1.25 + l * .03, .5, .3, .45);
    const eclair = (l > .05 && l < .14) || (l > 1.1 && l < 1.17);
    if (eclair) { g.fillStyle = 'rgba(255,248,230,.35)'; g.fillRect(0, 0, W, H);
      g.strokeStyle = '#fff6d8'; g.lineWidth = 8; g.beginPath(); let x = 760, y = 220; g.moveTo(x, y); for (let i = 0; i < 6; i++) { x += (rnd(i + (l > 1 ? 9 : 0)) - .5) * 160; y += 95; g.lineTo(x, y); } g.stroke(); }
    g.strokeStyle = 'rgba(239,230,210,.35)'; g.lineWidth = 3;
    for (let i = 0; i < 60; i++) { const x = (rnd(i) * W + t * 900) % W, y = (rnd(i + 60) * H + t * 2200) % H; g.beginPath(); g.moveTo(x, y); g.lineTo(x - 30, y + 70); g.stroke(); }
    const vv = tps(p.voile || 0), vg = tps(p.gouv || 0);
    const yb = 1060 + Math.sin(t * 3.4) * 50;
    mer(1080, t * 2, 55, MER, 4);
    bateau(540, yb, 160, Math.sin(t * 3.4 + .8) * .28, t, { dechire: p.casse && t >= vv ? 1 : 0, sansGouv: p.casse && t >= vg + .3 });
    if (p.casse && t >= vg) { const k = cl((t - vg) / 1.5); g.fillStyle = OR; g.save(); g.translate(540 - 170 - k * 260, 1110 + k * 60); g.rotate(k * 3); g.fillRect(-8, -34, 16, 68); g.restore(); }
    mer(1180, t * 2.3 + 1, 35, 'rgba(21,18,14,.85)', 0);
    if (p.casse) { claque('VOILE DÉCHIRÉE', W / 2, 520, vv, t, { coul: CREME, taille: 100 }); claque('GOUVERNAIL CASSÉ', W / 2, 660, vg, t, { coul: ROUGE, taille: 100 }); }
    else deux(p.t || 'LA TEMPÊTE', 1440, 140);
  }
  // compteur de jours à la dérive
  function compteur(p, t, l) {
    const n = Math.max(1, Math.min(p.n, 1 + Math.floor(cl(l / (p.duree || 1.6)) * p.n)));
    mer(1150, t, 6);
    const ks = (l / (p.duree || 1.6) * p.n) % 1; g.fillStyle = OR; g.beginPath(); g.arc(lerp(120, 960, ks), 1150 - Math.sin(ks * Math.PI) * 260, 34, 0, 7); g.fill();
    mer(1150, t, 6, 'rgba(21,18,14,1)', 2);
    bateau(540, 1150, 70, Math.sin(t * 1.5) * .06, t, { dechire: 1, sansGouv: true });
    for (let i = 0; i < n; i++) { g.fillStyle = CREME; g.fillRect(W / 2 - (p.n * 50) / 2 + i * 50 + 10, 380, 14, 90); }
    S.texte(String(n), W / 2, 700, { taille: 300, police: 'Spectral', poids: 600, coul: OR, ombre: 'rgba(217,180,90,.45)', flou: 40 });
    S.texte(p.t, W / 2, 900, { taille: 64, coul: CREME, esp: 6, max: 960 });
    if (p.sous) S.texte(p.sous, W / 2, 1380, { taille: 76, police: 'Spectral', it: true, poids: 400, coul: ROUGE });
  }
  // la pluie tombe dans des coques de noix de coco
  function pluie(p, t, l) {
    g.strokeStyle = 'rgba(239,230,210,.5)'; g.lineWidth = 4;
    for (let i = 0; i < 50; i++) { const x = rnd(i) * W, y = (rnd(i + 50) * 1100 + t * 1500) % 1100 + 200; g.beginPath(); g.moveTo(x, y); g.lineTo(x - 8, y + 50); g.stroke(); }
    [[330, 1.1], [750, .9]].forEach(([x, f], i) => {
      g.fillStyle = '#5b4632'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(x, 1000, 150, 0, Math.PI); g.closePath(); g.fill(); g.stroke();
      const niv = cl(l / 2) * 60 * f; g.fillStyle = 'rgba(150,190,220,.85)'; g.beginPath(); g.ellipse(x, 1012 - niv * .2, 130 - (60 - niv), 16, 0, 0, 7); g.fill(); });
    deux("L'EAU|DE PLUIE", 1380, 120);
  }
  // une gorgée chacun, le matin et le soir
  function gorgee(p, t, l) {
    const tm = tps(p.m), ts = tps(p.s);
    g.fillStyle = '#5b4632'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.arc(W / 2, 560, 120, 0, Math.PI); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = 'rgba(150,190,220,.85)'; g.beginPath(); g.ellipse(W / 2, 572, 100, 12, 0, 0, 7); g.fill();
    for (let i = 0; i < 6; i++) { const x = 165 + i * 150;
      bonhomme(x, 1080, 58, CREME);
      [[tm, OR], [ts, CREME]].forEach(([a, c], j) => { const k = pr(t, a + i * .1, .3); if (k <= 0) return;
        const xx = lerp(W / 2, x + (j ? 34 : -34), eo(k)), yy = lerp(600, 900, eo(k)) - Math.sin(k * Math.PI) * 120;
        g.fillStyle = c; g.beginPath(); g.arc(xx, yy, 16, 0, 7); g.fill(); });
    }
    claque('MATIN : 1 GORGÉE', W / 2, 1330, tm, t, { coul: OR, taille: 84 });
    claque('SOIR : 1 GORGÉE', W / 2, 1450, ts, t, { coul: CREME, taille: 84 });
    if (t < tm) S.texte('PARTS ÉGALES', W / 2, 1330, { taille: 96, coul: OR, contour: NOIR, contourL: 10 });
  }
  // un rocher surgit de l'océan : 'Ata
  function rocher(p, t, l) {
    const k = eo(pr(t, p.a, .9));
    mer(1150, t, 10);
    g.save(); g.beginPath(); g.rect(0, 0, W, 1150); g.clip();
    rocherProfil(W / 2, 1150 + lerp(520, 0, k), 820, 520); g.restore();
    mer(1160, t + 2, 8, 'rgba(21,18,14,.9)', 0);
    claque("’ATA", W / 2, 1380, tps(p.nom), t, { taille: 200, police: 'Spectral', poids: 600, coul: OR });
    S.texte('PACIFIQUE SUD', W / 2, 1530, { taille: 46, coul: GRIS, esp: 8 });
  }
  // le roman de Golding
  function livre(p, t, l) {
    const k = eo(pr(t, p.a, .45));
    g.save(); g.translate(W / 2, lerp(1250, 860, k)); g.rotate(lerp(.2, -.04, k));
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = CREME; g.fillRect(-330, -460, 660, 920); g.shadowColor = 'transparent';
    g.fillStyle = ROUGE; g.fillRect(-330, -460, 40, 920);
    S.texte('WILLIAM GOLDING', 20, -360, { taille: 46, coul: NOIR, esp: 4 });
    S.texte('SA MAJESTÉ', 20, -150, { taille: 92, police: 'Spectral', poids: 600, coul: NOIR, max: 560 });
    S.texte('DES MOUCHES', 20, -50, { taille: 92, police: 'Spectral', poids: 600, coul: NOIR, max: 560 });
    S.texte('roman · 1954', 20, 330, { taille: 48, police: 'Spectral', it: true, poids: 400, coul: GRIS });
    g.restore();
    // une mouche qui tourne autour
    const a = t * 3.1, x = W / 2 + Math.cos(a) * 380 + Math.sin(t * 11) * 20, y = 860 + Math.sin(a * 1.3) * 480;
    g.fillStyle = 'rgba(239,230,210,.55)'; [-1, 1].forEach(s => { g.beginPath(); g.ellipse(x + s * 14, y - 14, 18, 9, s * (.5 + Math.sin(t * 60) * .3), 0, 7); g.fill(); });
    g.fillStyle = NOIR; g.strokeStyle = CREME; g.lineWidth = 3; g.beginPath(); g.ellipse(x, y, 13, 20, 0, 0, 7); g.fill(); g.stroke();
    O.petitTitre('— LE ROMAN —', 300);
  }
  // trois équipes de deux
  function equipes(p, t, l) {
    for (let e = 0; e < 3; e++) { const k = back(pr(t, p.a + .1 + e * .22, .3)); if (k <= 0) continue; const cx = 210 + e * 330;
      g.save(); g.translate(cx, 1060); g.scale(k, k);
      g.strokeStyle = OR; g.lineWidth = 7; g.beginPath(); g.roundRect(-140, -330, 280, 360, 30); g.stroke();
      bonhomme(-60, 0, 70, CREME); bonhomme(60, 0, 70, CREME); g.restore(); }
    deux('ÉQUIPES|DE 2', 1350, 130);
  }
  // le tableau de service : potager, cuisine, garde
  function taches(p, t, l) {
    O.petitTitre('LE TABLEAU DE SERVICE', 480);
    p.etapes.forEach(([a, txt], i) => { const ta = tps(a), k = back(pr(t, ta, .3)); if (k <= 0) return; const x = 200 + i * 340, y = 860;
      g.save(); g.translate(x, y); g.scale(k, k);
      g.fillStyle = '#26221d'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.roundRect(-150, -170, 300, 340, 26); g.fill(); g.stroke();
      if (i === 0) { g.fillStyle = '#5b4632'; g.fillRect(-110, 60, 220, 50); for (let j = 0; j < 3; j++) { const xx = -70 + j * 70, h = 50 + Math.sin(t * 3 + j) * 6;
          g.strokeStyle = OR; g.lineWidth = 8; g.beginPath(); g.moveTo(xx, 60); g.lineTo(xx, 60 - h); g.stroke(); g.fillStyle = OR;
          g.beginPath(); g.ellipse(xx - 18, 60 - h, 22, 10, -.5, 0, 7); g.fill(); g.beginPath(); g.ellipse(xx + 18, 60 - h + 10, 22, 10, .5, 0, 7); g.fill(); } }
      if (i === 1) { flamme(0, 110, 50, t); g.fillStyle = GRIS; g.beginPath(); g.roundRect(-80, -30, 160, 90, 12); g.fill();
        g.strokeStyle = 'rgba(239,230,210,.5)'; g.lineWidth = 5; for (let j = 0; j < 3; j++) { const yy = -60 - ((t * 60 + j * 30) % 90); g.beginPath(); g.moveTo(-30 + j * 30, yy); g.quadraticCurveTo(-15 + j * 30, yy - 20, -30 + j * 30, yy - 40); g.stroke(); } }
      if (i === 2) { g.strokeStyle = CREME; g.lineWidth = 8; g.beginPath(); g.ellipse(0, 0, 100, 55, 0, 0, 7); g.stroke();
        g.fillStyle = OR; g.beginPath(); g.arc(Math.sin(t * 2) * 30, 0, 32, 0, 7); g.fill(); g.fillStyle = NOIR; g.beginPath(); g.arc(Math.sin(t * 2) * 30, 0, 14, 0, 7); g.fill(); }
      g.restore();
      S.texte(txt, x, y + 230, { taille: 52, coul: i === 2 ? OR : CREME, max: 320 }); });
    S.texte('chacun son tour', W / 2, 1300, { taille: 70, police: 'Spectral', it: true, poids: 400, coul: CREME });
  }
  // une dispute, puis la pause imposée
  function dispute(p, t, l) {
    const tp = tps(p.pause), kp = eo(pr(t, tp, .5)), tr = t < tp ? (rnd(t * 50) - .5) * 16 : 0;
    bonhomme(lerp(400, 160, kp) + tr, 1100, 110, CREME); bonhomme(lerp(680, 920, kp) - tr, 1100, 110, OR);
    if (t < tp) { g.save(); g.translate(W / 2, 680); g.rotate(Math.sin(t * 20) * .05); g.fillStyle = ROUGE; g.beginPath();
      for (let i = 0; i < 16; i++) { const a = i / 16 * 6.283, r = i % 2 ? 90 : 150; i ? g.lineTo(Math.cos(a) * r, Math.sin(a) * r * .8) : g.moveTo(Math.cos(a) * r, Math.sin(a) * r * .8); } g.closePath(); g.fill();
      S.texte('!!', 0, 6, { taille: 120, coul: CREME }); g.restore(); deux('UNE|DISPUTE ?', 1380, 130); }
    else { const k = back(pr(t, tp, .35)); g.save(); g.translate(W / 2, 800); g.scale(k, k); g.rotate(Math.sin((t - tp) * 2) * .1);
      g.strokeStyle = CREME; g.lineWidth = 8; g.fillStyle = '#26221d'; g.beginPath(); g.moveTo(-90, -150); g.lineTo(90, -150); g.lineTo(0, 0); g.lineTo(90, 150); g.lineTo(-90, 150); g.lineTo(0, 0); g.closePath(); g.fill(); g.stroke();
      const s = cl((t - tp) / 3); g.fillStyle = OR; g.beginPath(); g.moveTo(-70 * (1 - s), -130 + 130 * s); g.lineTo(70 * (1 - s), -130 + 130 * s); g.lineTo(0, 0); g.closePath(); g.fill();
      g.beginPath(); g.moveTo(-70 * s, 140); g.lineTo(70 * s, 140); g.lineTo(0, 140 - 120 * s); g.closePath(); g.fill(); g.restore();
      deux('PAUSE|POUR SE CALMER', 1380, 120); }
  }
  // le feu, entretenu jour et nuit
  function feu(p, t, l) {
    const jour = (Math.sin(l * 6) + 1) / 2; g.fillStyle = `rgba(217,180,90,${jour * .12})`; g.fillRect(0, 0, W, H);
    const a = l * 6 - Math.PI / 2; g.fillStyle = jour > .5 ? OR : CREME; g.beginPath(); g.arc(W / 2 + Math.cos(a) * 420, 620 + Math.sin(a) * 260, 40, 0, 7); g.fill();
    for (let i = 0; i < 14; i++) { const ph = (t * .8 + i / 14) % 1; g.fillStyle = `rgba(217,180,90,${1 - ph})`; g.beginPath(); g.arc(W / 2 + (rnd(i) - .5) * 200 + Math.sin(t * 4 + i) * 20, 1050 - ph * 420, 6, 0, 7); g.fill(); }
    g.fillStyle = '#5b4632'; g.save(); g.translate(W / 2, 1110); [-.3, .3].forEach(r => { g.save(); g.rotate(r); g.fillRect(-170, -22, 340, 44); g.restore(); }); g.restore();
    g.save(); g.shadowColor = OR; g.shadowBlur = 60; flamme(W / 2, 1090, 150, t); g.restore();
    deux(p.t, 1400, 110);
  }
  // Stephen tombe de la falaise
  function chute(p, t, l) {
    g.fillStyle = ROCHE; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(0, 420); g.lineTo(420, 440); g.lineTo(460, 640); g.lineTo(520, 900); g.lineTo(560, 1250); g.lineTo(0, 1250); g.closePath(); g.fill(); g.stroke();
    mer(1250, t, 8);
    const k = cl(l / 1.0), x = lerp(400, 700, k), y = lerp(420, 1190, k * k);
    bonhomme(x, y, 60, OR, { rot: k * 2.6 });
    if (k >= 1) { for (let i = 0; i < 8; i++) { const a = -Math.PI * rnd(i), r = 30 + (l - 1) * 300; g.fillStyle = `rgba(239,230,210,${cl(1 - (l - 1) * 2)})`; g.beginPath(); g.arc(700 + Math.cos(a) * r, 1190 + Math.sin(a) * r * .5, 8, 0, 7); g.fill(); } }
    deux(p.t, 1450, 110);
  }
  // jambe cassée, puis l'attelle de bâtons et de feuilles
  function jambe(p, t, l) {
    const ta = tps(p.attelle);
    g.save(); g.translate(W / 2, 880);
    g.fillStyle = '#d8b48c'; g.strokeStyle = NOIR; g.lineWidth = 8;
    g.beginPath(); g.roundRect(-430, -60, 440, 120, 60); g.fill(); g.stroke();
    g.save(); g.rotate(t < ta ? .12 : 0); g.beginPath(); g.roundRect(-20, -55, 420, 110, 55); g.fill(); g.stroke(); g.restore();
    if (t < ta) { g.strokeStyle = ROUGE; g.lineWidth = 12; g.beginPath(); g.moveTo(-20, -90); g.lineTo(10, -40); g.lineTo(-25, 0); g.lineTo(15, 40); g.lineTo(-15, 90); g.stroke();
      claque('CRAC', 0, -260, p.a, t, { taille: 190, coul: ROUGE }); }
    else { const k = eo(pr(t, ta, .4));
      g.fillStyle = '#7a5a3a'; g.strokeStyle = NOIR; g.lineWidth = 5; [-80, 80].forEach(dy => { g.beginPath(); g.roundRect(-260, dy - 14, 520 * k, 28, 8); g.fill(); g.stroke(); });
      for (let i = 0; i < 4; i++) { if (k < (i + 1) / 4) break; g.fillStyle = OR; g.save(); g.translate(-180 + i * 120, 0); g.rotate(.5); g.beginPath(); g.ellipse(0, 0, 45, 85, 0, 0, 7); g.fill();
        g.strokeStyle = '#8a6a2a'; g.lineWidth = 4; g.beginPath(); g.moveTo(0, -80); g.lineTo(0, 80); g.stroke(); g.restore(); }
      S.texte('BÂTONS + FEUILLES', 0, 280, { taille: 80, coul: OR, contour: NOIR, contourL: 10 }); }
    g.restore();
    deux('JAMBE|CASSÉE', 1360, 120);
  }
  // le capitaine et son bateau de pêche
  function capitaine(p, t, l) {
    g.fillStyle = 'rgba(217,180,90,.25)'; g.beginPath(); g.arc(820, 480, 120, 0, 7); g.fill();
    mer(1000, t, 8);
    g.save(); g.translate(lerp(900, 560, eo(pr(t, p.a, .8))), 990 + Math.sin(t * 2) * 6);
    g.fillStyle = '#3a2f25'; g.strokeStyle = CREME; g.lineWidth = 6;
    g.beginPath(); g.moveTo(-260, -40); g.lineTo(280, -40); g.lineTo(220, 50); g.lineTo(-230, 50); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.rect(-60, -150, 170, 110); g.fill(); g.stroke(); g.beginPath(); g.moveTo(-180, -40); g.lineTo(-180, -260); g.stroke();
    bonhomme(170, -40, 42, OR);
    g.restore();
    fiche('PETER WARNER', 'capitaine australien', 1330, eo(pr(t, p.a + .15, .35)));
  }
  // aux jumelles : des traces de feu sur la falaise
  function jumelles(p, t, l) {
    g.save(); g.beginPath(); g.arc(360, 850, 300, 0, 7); g.arc(720, 850, 300, 0, 7); g.clip();
    const dx = Math.sin(t * .9) * 30;
    g.fillStyle = '#3d4a2c'; g.fillRect(0, 0, W, H); g.fillStyle = '#2e3822'; for (let i = 0; i < 30; i++) { g.beginPath(); g.arc(rnd(i) * W + dx, 500 + rnd(i + 30) * 700, 40 + rnd(i + 60) * 60, 0, 7); g.fill(); }
    const taches = [[400, 760], [650, 900], [760, 700]];
    taches.forEach(([x, y], i) => { const k = pr(t, p.a + .2 + i * .25, .3); g.fillStyle = `rgba(13,11,9,${.85 * k})`; g.beginPath(); g.ellipse(x + dx, y, 70, 45, .3, 0, 7); g.fill();
      const kc = pr(t, p.a + .5 + i * .25, .4); if (kc > 0) { g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.ellipse(x + dx, y, 105, 75, .3, -1.5, -1.5 + kc * 6.6); g.stroke(); } });
    g.restore();
    g.strokeStyle = CREME; g.lineWidth = 10; g.beginPath(); g.arc(360, 850, 300, 0, 7); g.stroke(); g.beginPath(); g.arc(720, 850, 300, 0, 7); g.stroke();
    deux('DES TRACES|DE FEU', 1350, 120);
  }
  // six bougies : on les croyait morts
  function funerailles(p, t, l) {
    for (let i = 0; i < 6; i++) { const x = 190 + i * 140, k = pr(t, p.a + i * .1, .3); if (k <= 0) continue;
      g.fillStyle = CREME; g.fillRect(x - 24, 820, 48, 260); g.save(); g.globalAlpha = k; g.shadowColor = OR; g.shadowBlur = 40; flamme(x, 818, 30, t + i); g.restore(); }
    deux('FUNÉRAILLES', 1300, 150);
    S.texte('des 6 garçons', W / 2, 1440, { taille: 66, police: 'Spectral', it: true, poids: 400, coul: CREME });
  }
  // 15 mois, ensemble
  function mois(p, t, l) {
    const n = Math.min(15, Math.floor(cl(l / 1.1) * 15) + 1), te = tps(p.ens);
    for (let i = 0; i < 15; i++) { const x = 220 + (i % 5) * 160, y = 420 + Math.floor(i / 5) * 160, on = i < n;
      g.fillStyle = on ? OR : '#26221d'; g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath(); g.roundRect(x - 65, y - 65, 130, 130, 14); g.fill(); g.stroke();
      if (on) S.texte(String(i + 1), x, y + 4, { taille: 56, coul: NOIR, police: 'Spectral', poids: 600 }); }
    S.texte(n + ' MOIS', W / 2, 1000, { taille: 190, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 });
    if (t >= te) { const k = back(pr(t, te, .35));
      for (let i = 0; i < 6; i++) bonhomme(240 + i * 120, 1330, 55 * k, CREME);
      g.strokeStyle = OR; g.lineWidth = 8; g.beginPath(); g.moveTo(180, 1345); g.lineTo(180 + 720 * eo(pr(t, te, .5)), 1345); g.stroke();
      claque('ENSEMBLE.', W / 2, 1480, te, t, { taille: 130, coul: CREME }); }
  }
  // les règles de l'île, écrites sur un parchemin
  function regles(p, t, l) {
    const k = eo(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, lerp(1400, 860, k)); g.rotate(-.03);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#e9dfc8'; g.fillRect(-420, -470, 840, 940); g.shadowColor = 'transparent';
    S.texte('LES RÈGLES DE L’ÎLE', 0, -380, { taille: 58, coul: NOIR, esp: 4 });
    g.fillStyle = NOIR; g.fillRect(-330, -330, 660, 3);
    ['équipes de 2', 'potager, cuisine, garde', 'une dispute ? une pause', 'le feu ne s’éteint jamais'].forEach((s, i) => {
      g.save(); g.globalAlpha = cl((t - p.a - .3 - i * .25) * 4); S.texte('· ' + s, -330, -230 + i * 120, { taille: 54, police: 'Spectral', it: true, poids: 500, coul: NOIR, align: 'left', max: 680 }); g.restore(); });
    g.restore();
    O.tampon('DES RÈGLES', W / 2, 1270, pr(t, tps(p.tampon), .3), -.1, 120);
    if (t >= tps(p.tampon) + .3) S.texte('= déjà un ordre politique', W / 2, 1480, { taille: 66, police: 'Spectral', it: true, poids: 400, coul: OR, contour: NOIR, contourL: 8 });
  }

  return { ados, ile, sans, bateau: bateauPlan, sanscarte, tempete, compteur, pluie, gorgee, rocher, livre, equipes, taches, dispute, feu, chute, jambe,
    capitaine, jumelles, funerailles, mois, regles };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const T = p.type;
  if (T === 'ados') for (let i = 0; i < 6; i++) L.push([p.a + .08 + i * .09, 'pop', .45]);
  if (T === 'ile') L.push([p.a, 'souffle', .5]);
  if (T === 'sans') p.etapes.forEach(([a]) => L.push([tps(a) - .02, 'frappe', .6], [tps(a) + .18, 'lame', .45]));
  if (T === 'bateau') { L.push([p.a, 'souffle', .35]); if (p.tampon) L.push([tps(p.tampon) + .05, 'tampon', 1]); }
  if (T === 'sanscarte') L.push([tps(p.x1), 'frappe', .7], [tps(p.x2), 'frappe', .7]);
  if (T === 'tempete') { L.push([p.a, 'statique', .45], [p.a + .05, 'drop', .7]); if (p.casse) L.push([tps(p.voile), 'lame', .6], [tps(p.gouv), 'frappe', .7]); }
  if (T === 'compteur') for (let k = 0; k < p.n; k++) L.push([p.a + k * (p.duree || 1.6) / p.n, 'tic', .5]);
  if (T === 'pluie') for (let k = 0; k < 6; k++) L.push([p.a + .1 + k * .15, 'blip', .22]);
  if (T === 'gorgee') [p.m, p.s].forEach(a => { for (let i = 0; i < 6; i++) L.push([tps(a) + i * .1 + .25, 'pop', .3]); });
  if (T === 'rocher') L.push([p.a, 'montee', .6], [tps(p.nom), 'tampon', .8]);
  if (T === 'livre') L.push([p.a, 'papier', .5]);
  if (T === 'equipes') for (let e = 0; e < 3; e++) L.push([p.a + .1 + e * .22, 'clic', .45]);
  if (T === 'taches') p.etapes.forEach(([a]) => L.push([tps(a), 'pop', .5]));
  if (T === 'dispute') L.push([p.a, 'buzz', .35], [tps(p.pause), 'valide', .6]);
  if (T === 'feu') L.push([p.a, 'souffle', .5]);
  if (T === 'chute') L.push([p.a, 'whoosh', .8]);
  if (T === 'jambe') L.push([tps(p.attelle), 'frotte', .5]);
  if (T === 'capitaine') L.push([p.a, 'whoosh', .35]);
  if (T === 'jumelles') L.push([p.a, 'clic', .5], [p.a + .5, 'stylo', .5]);
  if (T === 'funerailles') L.push([p.a, 'coeur', .6], [p.a + .8, 'coeur', .6]);
  if (T === 'mois') { for (let k = 0; k < 15; k++) L.push([p.a + k * 1.1 / 15, 'tic', .4]); L.push([tps(p.ens), 'valide', .7]); }
  if (T === 'regles') { L.push([p.a, 'papier', .5]); for (let i = 0; i < 4; i++) L.push([p.a + .3 + i * .25, 'stylo', .25]); L.push([tps(p.tampon) + .05, 'tampon', 1]); }
};
