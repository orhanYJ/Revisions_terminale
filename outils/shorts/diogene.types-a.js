// Plans propres au short « Ôte-toi de mon soleil » (Diogène), dans le style du modèle A (archives : noir, crème, or, rouge).
// O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C = couleurs).
// Zone de dessin : y de 300 à 1250 ; titre vers 1400 ; les sous-titres du modèle sont à 1660.
window.SANS_ST_A = ['parole', 'etymo'];
window.PROPRES_A = ['offre', 'tableau', 'inventaire', 'jarre', 'agora', 'gobelet', 'lampe', 'chien', 'etymo', 'soleil', 'armee',
  'parole', 'tentations', 'rires', 'besoin'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const SOMBRE = '#1b1712', TERRE = '#8a5a3a';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i || L.length === 1 ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const sous = (s, y) => S.texte(s, W / 2, y, { taille: 58, police: 'Spectral', it: true, poids: 400, coul: CREME, contour: NOIR, contourL: 8, max: 960 });

  // silhouette debout, (x, y) = pieds, hauteur ~ 410 × s ; o : fond, trait, a, couronne, lampe (allumée), bras (bras levé)
  function homme(x, y, s, o = {}) {
    g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha *= (o.a ?? 1);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || CREME; g.lineWidth = o.ep || 7; g.lineJoin = 'round'; g.lineCap = 'round';
    g.beginPath(); g.moveTo(-58, -300); g.quadraticCurveTo(0, -322, 58, -300); g.lineTo(88, -95); g.lineTo(58, -95); g.lineTo(48, 0);
    g.lineTo(10, 0); g.lineTo(0, -85); g.lineTo(-10, 0); g.lineTo(-48, 0); g.lineTo(-58, -95); g.lineTo(-88, -95); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.arc(0, -362, 50, 0, 7); g.fill(); g.stroke();
    if (o.couronne) { g.fillStyle = OR; g.beginPath(); g.moveTo(-44, -398); g.lineTo(-44, -444); g.lineTo(-22, -420); g.lineTo(0, -454); g.lineTo(22, -420); g.lineTo(44, -444); g.lineTo(44, -398); g.closePath(); g.fill(); }
    if (o.lampe) { g.lineWidth = 12; g.beginPath(); g.moveTo(55, -280); g.lineTo(150, -230); g.stroke();
      g.lineWidth = 5; g.beginPath(); g.moveTo(150, -230); g.lineTo(150, -200); g.stroke();
      g.fillStyle = '#3a2c1a'; g.beginPath(); g.roundRect(125, -200, 50, 70, 8); g.fill(); g.stroke();
      g.fillStyle = OR; g.shadowColor = OR; g.shadowBlur = 40; g.beginPath(); g.ellipse(150, -165, 12, 20, 0, 0, 7); g.fill(); g.shadowBlur = 0; }
    if (o.bras) { g.lineWidth = 12; g.beginPath(); g.moveTo(50, -285); g.lineTo(120, -360); g.lineTo(150, -440); g.stroke(); }
    g.restore();
  }
  // silhouette assise, (x, y) = sol, hauteur ~ 330 × s
  function assis(x, y, s, o = {}) {
    g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha *= (o.a ?? 1);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || CREME; g.lineWidth = o.ep || 7; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(-55, -225); g.quadraticCurveTo(0, -245, 55, -225); g.lineTo(78, -72); g.quadraticCurveTo(125, -62, 115, 0);
    g.lineTo(-115, 0); g.quadraticCurveTo(-125, -62, -78, -72); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.arc(0, -285, 47, 0, 7); g.fill(); g.stroke();
    g.restore();
  }
  // silhouette allongée (tête à gauche) ; lev = buste redressé (0..1)
  function allonge(x, y, s, lev, o = {}) {
    g.save(); g.translate(x, y); g.scale(s, s);
    g.fillStyle = o.fond || '#16120e'; g.strokeStyle = o.trait || OR; g.lineWidth = 7; g.lineJoin = 'round';
    g.beginPath(); g.roundRect(0, -70, 240, 70, 30); g.fill(); g.stroke();                 // jambes
    g.save(); g.translate(20, -35); g.rotate(-lev * .7);
    g.beginPath(); g.roundRect(-230, -45, 240, 90, 40); g.fill(); g.stroke();             // buste
    g.beginPath(); g.arc(-285, -10, 48, 0, 7); g.fill(); g.stroke();                        // tête
    g.restore(); g.restore();
  }
  function piece(x, y, r) { g.fillStyle = OR; g.strokeStyle = '#8f6a26'; g.lineWidth = 4; g.beginPath(); g.ellipse(x, y, r, r * .35, 0, 0, 7); g.fill(); g.stroke(); }
  function soleilDessin(x, y, r, lt, a = 1) {
    g.save(); g.globalAlpha *= a; const gl = g.createRadialGradient(x, y, r * .3, x, y, r * 3); gl.addColorStop(0, 'rgba(255,230,160,.55)'); gl.addColorStop(1, 'rgba(255,230,160,0)');
    g.fillStyle = gl; g.fillRect(x - r * 3, y - r * 3, r * 6, r * 6);
    g.strokeStyle = OR; g.lineWidth = 10; g.lineCap = 'round'; for (let i = 0; i < 12; i++) { const an = i / 12 * 6.283 + lt * .3; g.beginPath(); g.moveTo(x + Math.cos(an) * r * 1.25, y + Math.sin(an) * r * 1.25); g.lineTo(x + Math.cos(an) * r * 1.6, y + Math.sin(an) * r * 1.6); g.stroke(); }
    g.fillStyle = '#f3d27a'; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.restore();
  }

  // Alexandre et ses présents (ouverture et boucle de fin)
  function offre(p, t) {
    const lt = t - p.a;
    g.save(); g.translate(720, 760); g.rotate(lt * .2); g.fillStyle = 'rgba(217,180,90,.09)';
    for (let i = 0; i < 12; i++) { g.rotate(Math.PI / 6); g.beginPath(); g.moveTo(0, 0); g.lineTo(-70, -800); g.lineTo(70, -800); g.closePath(); g.fill(); }
    g.restore();
    homme(720, 1200, 1.55, { couronne: true, fond: '#2a2016', trait: OR, ep: 6 });
    const n = Math.floor(lerp(0, 18, eo(pr(t, p.a + .1, 1.2))));
    for (let i = 0; i < n; i++) piece(230 + (i % 3) * 70 + (Math.floor(i / 3) % 2) * 35, 1180 - Math.floor(i / 3) * 34, 50);
    const k = back(pr(t, p.a + .3, .35)); g.save(); g.translate(330, 640); g.scale(k, k);
    g.fillStyle = CREME; g.beginPath(); g.roundRect(-210, -80, 420, 160, 50); g.fill(); g.beginPath(); g.moveTo(120, 70); g.lineTo(200, 130); g.lineTo(160, 60); g.fill();
    S.texte('CE QUE TU VEUX', 0, 4, { taille: 50, coul: NOIR, max: 380 }); g.restore();
    deux(p.t, 1410, 105);
  }

  // une image du domaine public en carte découpée, recadrée sur (fx, fy) ; légende en petit
  function tableau(p, t, l) {
    const k = eo(pr(t, p.a, .35)), w = p.w || 800, h = p.h || 880, cy = lerp(800, 760, k);
    O.carte(p.img, W / 2, cy, w, h, lerp(.05, -.025, k), (p.z || 1) * (1 + l * .03), p.fx ?? .5, p.fy ?? .5, { lum: .95 });
    const yb = 760 + h / 2;
    if (p.t) deux(p.t, yb + 140, 110);
    if (p.sous) sous(p.sous, yb + 265);
    if (p.leg) S.texte(p.leg, W / 2, p.sous ? yb + 335 : yb + 275, { taille: 32, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 960 });
  }

  // manteau, sac, bâton : chaque objet à son repère
  function inventaire(p, t) {
    O.petitTitre('TOUT TON BAGAGE', 470);
    const dessins = {
      manteau(x, y) { g.fillStyle = '#5b4a36'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(x - 60, y - 120); g.lineTo(x + 60, y - 120); g.lineTo(x + 110, y + 120);
        g.quadraticCurveTo(x, y + 150, x - 110, y + 120); g.closePath(); g.fill(); g.stroke(); g.beginPath(); g.moveTo(x - 20, y - 110); g.lineTo(x - 40, y + 130); g.moveTo(x + 25, y - 110); g.lineTo(x + 45, y + 130); g.stroke(); },
      sac(x, y) { g.fillStyle = '#7a5a36'; g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); g.moveTo(x - 40, y - 60); g.quadraticCurveTo(x - 110, y + 120, x, y + 120); g.quadraticCurveTo(x + 110, y + 120, x + 40, y - 60); g.closePath(); g.fill(); g.stroke();
        g.beginPath(); g.moveTo(x - 45, y - 60); g.quadraticCurveTo(x, y - 200, x + 45, y - 60); g.stroke(); g.strokeStyle = OR; g.beginPath(); g.moveTo(x - 42, y - 50); g.lineTo(x + 42, y - 50); g.stroke(); },
      baton(x, y) { g.strokeStyle = '#a07a4a'; g.lineWidth = 18; g.lineCap = 'round'; g.beginPath(); g.moveTo(x - 30, y + 150); g.quadraticCurveTo(x - 10, y, x + 25, y - 150); g.stroke();
        g.strokeStyle = CREME; g.lineWidth = 4; g.beginPath(); g.moveTo(x - 30, y + 150); g.quadraticCurveTo(x - 10, y, x + 25, y - 150); g.stroke(); },
    };
    p.items.forEach(([a, nom, lab], i) => { const ta = tps(a); if (t < ta) return; const k = back(pr(t, ta, .3)), x = 200 + i * 340, y = 800;
      g.save(); g.translate(x, y); g.scale(k * 1.35, k * 1.35); g.translate(-x, -y); dessins[nom](x, y); g.restore();
      S.texte(lab, x, 1110, { taille: 54, coul: i === p.items.length - 1 ? OR : CREME, max: 320 }); });
  }

  // la jarre (pithos) couchée, en pleine ville ; Diogène dedans
  function jarre(p, t) {
    const lt = t - p.a;
    g.strokeStyle = 'rgba(239,230,210,.18)'; g.lineWidth = 4;
    for (let i = 0; i < 6; i++) { const x = 60 + i * 190; g.strokeRect(x, 520, 120, 520); }
    g.fillStyle = SOMBRE; g.fillRect(0, 1150, W, 100); g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(0, 1150); g.lineTo(W, 1150); g.stroke();
    const cx = 600, cy = 900;
    g.fillStyle = TERRE; g.strokeStyle = CREME; g.lineWidth = 7;
    g.beginPath(); g.ellipse(cx + 80, cy, 360, 250, 0, 0, 7); g.fill(); g.stroke();
    g.fillStyle = '#6e4529'; g.beginPath(); g.ellipse(cx - 230, cy, 90, 220, 0, 0, 7); g.fill(); g.stroke();
    g.fillStyle = '#0d0907'; g.beginPath(); g.ellipse(cx - 230, cy, 62, 180, 0, 0, 7); g.fill();
    g.strokeStyle = 'rgba(239,230,210,.3)'; g.lineWidth = 4; [-.6, .1, .7].forEach(f => { g.beginPath(); g.ellipse(cx + 80 + f * 300, cy, 40, 240 * Math.sqrt(1 - f * f), 0, -1.5, 1.5); g.stroke(); });
    g.save(); g.beginPath(); g.ellipse(cx - 230, cy, 62, 180, 0, 0, 7); g.clip();
    g.fillStyle = '#16120e'; g.strokeStyle = OR; g.lineWidth = 5; g.beginPath(); g.arc(cx - 225, cy - 40 + Math.sin(lt * 2) * 3, 34, 0, 7); g.fill(); g.stroke();
    g.beginPath(); g.roundRect(cx - 265, cy + 0, 80, 170, 30); g.fill(); g.stroke(); g.restore();
    // ronflement
    for (let i = 0; i < 3; i++) { const k = ((lt * .8 + i / 3) % 1); g.save(); g.globalAlpha = 1 - k; S.texte('z', cx - 300 - k * 60, cy - 200 - k * 160, { taille: 50 + i * 12, coul: CREME }); g.restore(); }
    deux(p.t, 1400, 115);
  }

  // la place publique : colonnes, Diogène qui mange ; p.doigts : les passants montrent du doigt
  function agora(p, t) {
    const lt = t - p.a;
    g.fillStyle = SOMBRE; g.strokeStyle = CREME; g.lineWidth = 5;
    g.fillRect(80, 470, 920, 40); g.strokeRect(80, 470, 920, 40);
    for (let i = 0; i < 5; i++) { const x = 110 + i * 200; g.fillStyle = '#2a241d'; g.fillRect(x, 510, 60, 600); g.strokeRect(x, 510, 60, 600); }
    g.fillStyle = SOMBRE; g.fillRect(0, 1180, W, 70); g.beginPath(); g.moveTo(0, 1180); g.lineTo(W, 1180); g.stroke();
    assis(W / 2, 1180, 1.05, { fond: '#16120e', trait: OR, ep: 8 });
    // l'écuelle, la main qui porte à la bouche
    const m = Math.max(0, Math.sin(lt * 4));
    g.fillStyle = TERRE; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.ellipse(W / 2, 1090, 80, 26, 0, 0, Math.PI); g.fill(); g.stroke();
    g.fillStyle = CREME; g.beginPath(); g.arc(W / 2 + 40, lerp(1080, 900, m), 12, 0, 7); g.fill();
    [[150, .85], [930, .85]].forEach(([x, s], i) => homme(x, 1180, s, { fond: '#16120e', trait: CREME, a: .85 }));
    if (p.doigts) [[150, 1], [930, -1]].forEach(([x, sg], i) => { const k = eo(pr(t, p.a + .1 + i * .15, .3));
      g.strokeStyle = ROUGE; g.lineWidth = 12; g.lineCap = 'round'; g.beginPath(); g.moveTo(x + sg * 50, 980); g.lineTo(x + sg * lerp(50, 230, k), lerp(980, 950, k)); g.stroke();
      if (k > .8) S.texte('!', x, 640, { taille: 120, coul: ROUGE, contour: NOIR, contourL: 8 }); });
    deux(p.t, 1400, 115);
  }

  // etape 1 : l'enfant boit dans ses mains ; etape 2 : tu jettes ton gobelet
  function gobelet(p, t) {
    const lt = t - p.a;
    g.fillStyle = SOMBRE; g.fillRect(0, 1180, W, 70); g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(0, 1180); g.lineTo(W, 1180); g.stroke();
    // la fontaine
    g.fillStyle = '#2a241d'; g.fillRect(820, 640, 120, 540); g.strokeRect(820, 640, 120, 540);
    g.fillStyle = '#5b5247'; g.beginPath(); g.moveTo(820, 760); g.lineTo(740, 770); g.lineTo(740, 790); g.lineTo(820, 790); g.closePath(); g.fill(); g.stroke();
    g.strokeStyle = 'rgba(150,190,220,.8)'; g.lineWidth = 8; g.beginPath(); g.moveTo(745, 790); g.quadraticCurveTo(730, 850, 720, 960); g.stroke();
    for (let i = 0; i < 5; i++) { const k = ((lt * 2 + i / 5) % 1); g.fillStyle = 'rgba(150,190,220,.8)'; g.beginPath(); g.arc(720 + (rnd(i) - .5) * 30, 960 + k * 40, 6, 0, 7); g.fill(); }
    // l'enfant, mains en coupe
    homme(690, 1180, .6, { fond: '#16120e', trait: CREME });
    g.strokeStyle = CREME; g.fillStyle = '#16120e'; g.lineWidth = 6; g.beginPath(); g.ellipse(718, 985, 34, 16, 0, 0, Math.PI); g.fill(); g.stroke();
    // Diogène
    homme(300, 1180, 1, { fond: '#16120e', trait: OR, bras: p.etape === 2 });
    if (p.etape === 1) { g.fillStyle = TERRE; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(360, 900); g.lineTo(420, 900); g.lineTo(410, 960); g.lineTo(370, 960); g.closePath(); g.fill(); g.stroke(); }
    else { const k = cl(lt / 1.1), x = lerp(450, 560, k), y = 760 - Math.sin(k * Math.PI) * 300 + k * 520;
      if (k < 1) { g.save(); g.translate(x, y); g.rotate(k * 9); g.fillStyle = TERRE; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(-30, -30); g.lineTo(30, -30); g.lineTo(20, 30); g.lineTo(-20, 30); g.closePath(); g.fill(); g.stroke(); g.restore(); }
      else for (let i = 0; i < 5; i++) { g.fillStyle = TERRE; g.beginPath(); g.arc(520 + i * 22, 1170 - rnd(i) * 10, 9, 0, 7); g.fill(); } }
    deux(p.t, 1400, 105);
  }

  // en plein jour, une lampe ; p.cherche : la lumière passe sur les passants
  function lampe(p, t) {
    const lt = t - p.a;
    soleilDessin(860, 520, 90, lt);
    g.fillStyle = SOMBRE; g.fillRect(0, 1180, W, 70); g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(0, 1180); g.lineTo(W, 1180); g.stroke();
    if (p.cherche) {
      const xs = [480, 660, 840, 1000], cible = lerp(430, 1020, (Math.sin(lt * 1.6 - 1.5) + 1) / 2);
      xs.forEach(x => homme(x, 1180, .75, { fond: '#16120e', trait: GRIS, a: .7 }));
      g.save(); g.globalAlpha = .35; g.fillStyle = OR; g.beginPath(); g.moveTo(330, 960); g.lineTo(cible - 90, 1180); g.lineTo(cible + 90, 1180); g.closePath(); g.fill(); g.restore();
      xs.forEach(x => { if (Math.abs(x - cible) < 80) S.texte('?', x, 780, { taille: 90, coul: OR, contour: NOIR, contourL: 8 }); });
    }
    homme(p.cherche ? 200 : 420, 1180, 1.05, { fond: '#16120e', trait: OR, lampe: true });
    deux(p.t, 1400, 110);
  }

  // le chien
  function chien(p, t) {
    const lt = t - p.a, k = back(pr(t, p.a, .4));
    g.save(); g.translate(W / 2, 1150); g.scale(1.25 * k, 1.25 * k);
    g.fillStyle = '#16120e'; g.strokeStyle = OR; g.lineWidth = 7; g.lineJoin = 'round';
    g.beginPath(); g.moveTo(-150, 0); g.quadraticCurveTo(-170, -150, -90, -230); g.lineTo(-40, -380); g.lineTo(-30, -460); g.lineTo(0, -420);
    g.lineTo(40, -470); g.lineTo(50, -400); g.quadraticCurveTo(120, -380, 150, -340); g.lineTo(140, -310); g.lineTo(60, -320);
    g.quadraticCurveTo(40, -250, 60, -150); g.lineTo(80, 0); g.lineTo(40, 0); g.lineTo(20, -140); g.lineTo(-10, 0); g.closePath(); g.fill(); g.stroke();
    g.beginPath(); g.moveTo(-150, -10); g.quadraticCurveTo(-240 + Math.sin(lt * 8) * 20, -40, -230, -120 + Math.sin(lt * 8) * 15); g.stroke();
    g.fillStyle = OR; g.beginPath(); g.arc(50, -370, 8, 0, 7); g.fill();
    g.restore();
    deux(p.t, 1400, 150);
  }

  // l'étymologie : kuôn → kunikos → cynique
  function etymo(p, t) {
    const tc = tps(p.cyn);
    const boite = (txt, s2, y, k, c) => { if (k <= 0) return; g.save(); g.globalAlpha = cl(k * 2); g.translate(W / 2, y); g.scale(lerp(.7, 1, eo(k)), lerp(.7, 1, eo(k)));
      g.fillStyle = SOMBRE; g.strokeStyle = c; g.lineWidth = 6; g.beginPath(); g.roundRect(-400, -105, 800, 210, 24); g.fill(); g.stroke();
      S.texte(txt, 0, -22, { taille: 96, coul: c, max: 740 }); S.texte(s2, 0, 60, { taille: 44, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 740 }); g.restore(); };
    O.petitTitre('D’OÙ VIENT LE MOT', 420);
    boite('KUÔN', 'en grec : « chien »', 600, pr(t, p.a, .3), CREME);
    S.d.fleche(W / 2, 720, W / 2, 800, eo(pr(t, p.a + .3, .3)), { trait: OR, ep: 10 });
    boite('KUNIKOS', '« comme un chien »', 920, pr(t, p.a + .45, .3), CREME);
    S.d.fleche(W / 2, 1040, W / 2, 1120, eo(pr(t, Math.max(p.a + .7, tc - .3), .3)), { trait: OR, ep: 10 });
    boite('CYNIQUE', 'Diogène, le philosophe « chien »', 1240, pr(t, Math.max(p.a + .9, tc), .3), OR);
  }

  // allongé au soleil ; p.ombre : une ombre se pose sur toi ; p.redresse : tu te redresses
  function soleil(p, t) {
    const lt = t - p.a, ko = p.ombre ? eo(pr(t, p.a + (p.redresse ? -1 : .1), .7)) : 0;
    soleilDessin(820, 560, 110, lt, 1 - ko * .75);
    g.fillStyle = '#3a2c1a'; g.fillRect(0, 1140, W, 110); g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(0, 1140); g.lineTo(W, 1140); g.stroke();
    // la lumière sur Diogène
    g.save(); g.globalAlpha = .3 * (1 - ko); g.fillStyle = '#f3d27a'; g.beginPath(); g.moveTo(820, 560); g.lineTo(120, 1140); g.lineTo(640, 1140); g.closePath(); g.fill(); g.restore();
    const lev = p.redresse ? eo(pr(t, p.a + .3, .7)) * .9 : 0;
    allonge(330, 1138, 1, lev, { trait: OR });
    if (ko > 0) { g.save(); g.globalAlpha = ko;
      homme(720, 1140, 1.75, { fond: 'rgba(0,0,0,.85)', trait: 'rgba(239,230,210,.25)', ep: 4, couronne: p.redresse });
      g.fillStyle = 'rgba(0,0,0,.55)'; g.beginPath(); g.moveTo(640, 1140); g.lineTo(160, 1140); g.lineTo(140, 1200); g.lineTo(660, 1200); g.closePath(); g.fill(); g.restore(); }
    deux(p.t, 1400, 110);
  }

  // les Grecs choisissent Alexandre pour chef : rangs de casques et de lances
  function armee(p, t) {
    const lt = t - p.a;
    homme(W / 2, 820, .95, { couronne: true, fond: '#2a2016', trait: OR });
    g.fillStyle = '#2a241d'; g.strokeStyle = OR; g.lineWidth = 5; g.fillRect(W / 2 - 160, 820, 320, 40); g.strokeRect(W / 2 - 160, 820, 320, 40);
    for (let r = 0; r < 3; r++) for (let c = 0; c < 7 - r; c++) {
      const k = eo(pr(t, p.a + .1 + (r * 7 + c) * .03, .3)), x = 130 + r * 55 + c * 140, y = 1220 - r * 120 + (1 - k) * 60, up = Math.sin(lt * 5 + c + r) > .6 ? -20 : 0;
      g.save(); g.globalAlpha = k;
      g.strokeStyle = GRIS; g.lineWidth = 5; g.beginPath(); g.moveTo(x + 45, y + 20); g.lineTo(x + 45, y - 190 + up); g.stroke();
      g.fillStyle = GRIS; g.beginPath(); g.moveTo(x + 45, y - 215 + up); g.lineTo(x + 35, y - 185 + up); g.lineTo(x + 55, y - 185 + up); g.closePath(); g.fill();
      g.fillStyle = '#16120e'; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.arc(x, y - 30, 40, Math.PI, 0); g.lineTo(x + 40, y + 10); g.lineTo(x - 40, y + 10); g.closePath(); g.fill(); g.stroke();
      g.fillStyle = ROUGE; g.beginPath(); g.ellipse(x, y - 78, 36, 14, 0, 0, 7); g.fill();
      g.restore();
    }
    deux(p.t, 1420, 120);
  }

  // une parole, tapée à la machine ; p.qui : qui parle ; p.tampon : la phrase claque en rouge
  function parole(p, t) {
    if (p.fond) O.fondImg(p.fond, 1.3, p.fond === 'alexandre' ? .25 : .72, .5, .35);
    const txt = p.t, d = p.duree || .9, n = Math.floor(cl((t - p.a) / d) * txt.replace(/\|/g, '').length);
    S.texte(p.qui, W / 2, 700, { taille: 40, coul: p.qui === 'DIOGÈNE' ? OR : GRIS, esp: 8, poids: 600 });
    const lignes = txt.split('|'), tot = txt.replace(/\|/g, '').length;
    let c = 0; lignes.forEach((s, i) => { const vis = s.slice(0, Math.max(0, n - c)); c += s.length;
      S.texte((i === 0 ? '« ' : '') + vis + (i === lignes.length - 1 && n >= tot ? ' »' : ''), W / 2, 900 + i * 125,
        { taille: p.taille || 96, police: 'Spectral', it: true, poids: 500, coul: p.tampon ? ROUGE : CREME, max: 980, contour: NOIR, contourL: 6 }); });
    if (p.tampon) { const k = pr(t, p.a + d, .3); if (k > 0) soleilDessin(W / 2, 1300, 70 * eo(k), t, k); }
    else O.barreRouge(1000 + lignes.length * 60, eo(pr(t, p.a + d, .3)), 12, -.02);
  }

  // de l'or ? un palais ?
  function tentations(p, t) {
    const tp = tps(p.palais), k1 = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 880); g.scale(k1, k1); g.translate(-W / 2, -880);
    for (let i = 0; i < 24; i++) piece(W / 2 + ((i % 6) - 2.5) * 70 + (Math.floor(i / 6) % 2) * 35, 1060 - Math.floor(i / 6) * 34, 52);
    g.restore();
    if (t >= tp) { const k = back(pr(t, tp, .35)); g.save(); g.translate(W / 2, 700); g.scale(k, k);
      g.fillStyle = SOMBRE; g.strokeStyle = OR; g.lineWidth = 6; g.beginPath(); g.moveTo(-240, -60); g.lineTo(0, -180); g.lineTo(240, -60); g.closePath(); g.fill(); g.stroke();
      for (let i = 0; i < 5; i++) { g.fillRect(-210 + i * 100, -50, 30, 200); g.strokeRect(-210 + i * 100, -50, 30, 200); }
      g.fillRect(-250, 150, 500, 30); g.strokeRect(-250, 150, 500, 30); g.restore(); }
    deux(t >= tp ? 'DE L’OR ?|UN PALAIS ?' : 'DE L’OR ?', 1400, 120);
  }

  // les compagnons rient
  function rires(p, t) {
    const lt = t - p.a;
    [[200, .9], [420, 1], [660, 1], [880, .9]].forEach(([x, s], i) => { const sec = Math.sin(lt * 14 + i) * 6;
      homme(x, 1200 + sec, s, { fond: '#16120e', trait: CREME });
      const k = back(pr(t, p.a + .1 + i * .15, .25)); if (k > 0) { g.save(); g.translate(x + (i % 2 ? 30 : -30), 650 + (i % 2) * 70); g.scale(k, k); g.rotate((i % 2 ? .12 : -.12));
        S.texte('HA !', 0, 0, { taille: 80, coul: OR, contour: NOIR, contourL: 8 }); g.restore(); } });
    deux(p.t, 1400, 110);
  }

  // besoin de rien : divin ; p.peu : besoin de peu, presque divin
  function besoin(p, t) {
    const lt = t - p.a;
    const ligne = (y, a, b, kk, plein) => { if (kk <= 0) return; g.save(); g.globalAlpha = cl(kk * 2); g.translate(lerp(-300, 0, eo(kk)), 0);
      g.fillStyle = 'rgba(217,180,90,.1)'; g.fillRect(70, y - 130, 940, 260);
      g.strokeStyle = OR; g.lineWidth = 10; g.shadowColor = OR; g.shadowBlur = 25; g.beginPath(); g.arc(190, y, 70, plein ? 0 : Math.PI, plein ? 7 : 2 * Math.PI); g.stroke(); g.shadowBlur = 0;
      S.texte(a, 300, y - 45, { taille: 62, coul: CREME, align: 'left', max: 680 });
      S.texte(b, 300, y + 50, { taille: 92, coul: OR, align: 'left', max: 680 }); g.restore(); };
    O.petitTitre('— CE QUE DISAIT DIOGÈNE —', 520);
    if (!p.peu) ligne(760, 'BESOIN DE RIEN', 'DIVIN', pr(t, tps(p.rien), .35), true);
    else { ligne(760, 'BESOIN DE RIEN', 'DIVIN', 1, true); ligne(1100, 'BESOIN DE PEU', 'PRESQUE DIVIN', pr(t, p.a + .1, .35), false); }
    if (!p.peu) { const k = eo(pr(t, p.a, .4)); g.save(); g.globalAlpha = .5 * (1 - pr(t, tps(p.rien), .3)) * k; S.texte('?', W / 2, 1100, { taille: 200, coul: GRIS }); g.restore(); }
  }

  return { offre, tableau, inventaire, jarre, agora, gobelet, lampe, chien, etymo, soleil, armee, parole, tentations, rires, besoin };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'offre') { for (let k = 0; k < 6; k++) L.push([p.a + .1 + k * .2, 'blip', .25]); L.push([p.a + .3, 'pop', .4]); }
  if (p.type === 'tableau') L.push([p.a, 'papier', .3]);
  if (p.type === 'inventaire') p.items.forEach(([a]) => L.push([tps(a), 'pop', .45]));
  if (p.type === 'jarre') L.push([p.a, 'souffle', .35]);
  if (p.type === 'agora') L.push([p.a + (p.doigts ? .1 : 0), p.doigts ? 'buzz' : 'frotte', .35]);
  if (p.type === 'gobelet') L.push(p.etape === 2 ? [p.a + 1.1, 'disque', .5] : [p.a, 'souffle', .3]);
  if (p.type === 'lampe') L.push([p.a, p.cherche ? 'whoosh' : 'blip', .4]);
  if (p.type === 'chien') L.push([p.a, 'pop', .45]);
  if (p.type === 'etymo') L.push([p.a, 'clic', .4], [p.a + .45, 'clic', .4], [Math.max(p.a + .9, tps(p.cyn)), 'tampon', .7]);
  if (p.type === 'soleil') L.push([p.a, p.ombre ? 'aspire' : 'souffle', .4]);
  if (p.type === 'armee') L.push([p.a + .1, 'montee', .45]);
  if (p.type === 'parole') { const n = p.t.length, d = p.duree || .9; for (let k = 0; k < n; k += 2) L.push([p.a + d * k / n, 'tic', .3]); L.push([p.a + d + .05, p.tampon ? 'gong' : 'lame', p.tampon ? .7 : .5]); }
  if (p.type === 'tentations') { L.push([p.a, 'blip', .4]); L.push([tps(p.palais), 'pop', .5]); }
  if (p.type === 'rires') for (let i = 0; i < 4; i++) L.push([p.a + .1 + i * .15, 'pop', .3]);
  if (p.type === 'besoin') L.push([p.peu ? p.a + .1 : tps(p.rien), 'valide', .5]);
};
