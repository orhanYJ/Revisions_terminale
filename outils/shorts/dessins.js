// Dessins vectoriels communs aux modèles de shorts ; le style (couleurs, lueur, épaisseur) vient du modèle.
// st = {trait, fond, ep, lueur} ; lueur = couleur du halo (néon) ou rien.
(function () {
  const g = S.g;
  function style(st) {
    g.strokeStyle = st.trait || '#fff'; g.fillStyle = st.fond || 'transparent';
    g.lineWidth = st.ep || 8; g.lineCap = 'round'; g.lineJoin = 'round';
    if (st.lueur) { g.shadowColor = st.lueur; g.shadowBlur = st.flou || 28; } else g.shadowBlur = 0;
  }

  // horloge de Libet : cadran, 60 graduations, point qui fait un tour en 2,56 s
  function horloge(cx, cy, r, ang, st, marque) {
    g.save(); style(st);
    g.beginPath(); g.arc(cx, cy, r, 0, 2 * Math.PI); if (st.fond) g.fill(); g.stroke();
    for (let i = 0; i < 60; i++) {
      const a = i / 60 * 2 * Math.PI - Math.PI / 2, l = i % 5 ? r * .06 : r * .13;
      g.lineWidth = i % 5 ? (st.ep || 8) * .4 : (st.ep || 8) * .8;
      g.beginPath(); g.moveTo(cx + Math.cos(a) * (r * .9), cy + Math.sin(a) * (r * .9));
      g.lineTo(cx + Math.cos(a) * (r * .9 - l), cy + Math.sin(a) * (r * .9 - l)); g.stroke();
    }
    if (marque !== undefined) {
      const a = marque - Math.PI / 2;
      g.strokeStyle = st.marque || st.trait; g.lineWidth = (st.ep || 8) * .9; g.setLineDash([18, 14]);
      g.beginPath(); g.moveTo(cx, cy); g.lineTo(cx + Math.cos(a) * r * 1.12, cy + Math.sin(a) * r * 1.12); g.stroke(); g.setLineDash([]);
    }
    const a = ang - Math.PI / 2;
    g.fillStyle = st.point || '#e33'; if (st.lueurPoint) { g.shadowColor = st.lueurPoint; g.shadowBlur = 40; }
    g.beginPath(); g.arc(cx + Math.cos(a) * r * .68, cy + Math.sin(a) * r * .68, r * .07, 0, 2 * Math.PI); g.fill();
    g.restore();
  }

  // avant-bras et main de profil, poignet plié de ang (radians) ; (x, y) = poignet
  function main(x, y, ang, st, k = 1) {
    g.save(); style(st); g.translate(x, y); g.scale(k, k);
    // avant-bras
    g.beginPath(); g.moveTo(-420, -48); g.quadraticCurveTo(-200, -62, 0, -42); g.lineTo(0, 42); g.quadraticCurveTo(-200, 60, -420, 56);
    if (st.fond) g.fill(); g.stroke();
    // main (tourne autour du poignet)
    g.rotate(-ang);
    g.beginPath();
    g.moveTo(0, -42); g.quadraticCurveTo(70, -60, 150, -48); g.quadraticCurveTo(250, -40, 300, -20);
    g.quadraticCurveTo(320, -8, 300, 4); g.quadraticCurveTo(240, 14, 170, 18);
    g.quadraticCurveTo(200, 40, 190, 58); g.quadraticCurveTo(150, 62, 110, 48); g.quadraticCurveTo(60, 46, 0, 42); g.closePath();
    if (st.fond) g.fill(); g.stroke();
    g.lineWidth = (st.ep || 8) * .5;
    [[-8], [12]].forEach(([dy]) => { g.beginPath(); g.moveTo(170, dy - 16); g.quadraticCurveTo(230, dy - 14, 290, dy - 10); g.stroke(); });
    g.restore();
  }

  // tête de profil (regard à droite), centre (cx, cy), hauteur ~ 2r
  function tete(cx, cy, r, st) {
    g.save(); style(st); g.translate(cx, cy); g.scale(r / 300, r / 300);
    g.beginPath();
    g.moveTo(-60, 300); g.lineTo(-40, 170); g.bezierCurveTo(-200, 120, -230, -90, -150, -200);
    g.bezierCurveTo(-60, -320, 160, -320, 220, -170); g.bezierCurveTo(240, -110, 230, -60, 240, -30);
    g.lineTo(290, 40); g.lineTo(250, 55); g.lineTo(260, 110); g.bezierCurveTo(250, 160, 200, 160, 150, 150);
    g.lineTo(150, 300);
    if (st.fond) g.fill(); g.stroke();
    g.restore();
  }

  // cerveau stylisé (contour + circonvolutions), centre (cx, cy), largeur ~ 2r
  function cerveau(cx, cy, r, st, k = 1) {
    g.save(); style(st); g.translate(cx, cy); g.scale(r / 300, r / 300);
    const p = new Path2D('M-250,40 C-300,-60 -240,-200 -120,-220 C-60,-290 60,-290 110,-230 C220,-240 300,-150 280,-50 C320,20 280,120 200,130 C170,200 80,210 30,170 C-20,220 -120,210 -150,150 C-230,160 -280,110 -250,40 Z');
    if (st.fond) g.fill(p);
    g.setLineDash(k < 1 ? [3000 * k, 3000] : []); g.stroke(p);
    g.lineWidth = (st.ep || 8) * .6;
    const plis = ['M-180,-120 C-130,-90 -150,-40 -100,-20', 'M-60,-230 C-40,-170 -90,-130 -40,-80', 'M60,-220 C30,-160 90,-130 60,-70',
      'M190,-160 C140,-120 190,-60 140,-20', 'M-200,60 C-140,40 -120,100 -60,80', 'M-20,20 C30,-20 80,40 130,0', 'M40,120 C80,80 150,110 190,70', 'M-110,140 C-80,100 -30,140 0,110'];
    plis.forEach((d, i) => { if (k >= (i + 1) / plis.length * .9 || k >= 1) g.stroke(new Path2D(d)); });
    g.setLineDash([]); g.restore();
  }

  // pierre irrégulière
  function pierre(x, y, r, rot, st) {
    g.save(); style(st); g.translate(x, y); g.rotate(rot);
    g.beginPath();
    const n = 9; for (let i = 0; i <= n; i++) { const a = i / n * 2 * Math.PI, rr = r * (.78 + .22 * S.rnd(i * 7.3 + 1)); i ? g.lineTo(Math.cos(a) * rr, Math.sin(a) * rr * .82) : g.moveTo(Math.cos(a) * rr, Math.sin(a) * rr * .82); }
    g.closePath(); if (st.fond) g.fill(); g.stroke();
    g.restore();
  }

  // tracé EEG : de x0 à x1 autour de y ; décalage (défilement) ; amp ; bruit = pas de bosse
  function eeg(x0, x1, y, t, amp, st, opt = {}) {
    g.save(); style(st); g.beginPath();
    for (let x = x0; x <= x1; x += 4) {
      const u = (x - x0) / (x1 - x0), tt = t * 1.6 + u * 3;
      let v = Math.sin(tt * 9.1) * .18 + Math.sin(tt * 23.7 + 1) * .12 + Math.sin(tt * 4.3) * .15;
      if (opt.bruit) v += (S.rnd(Math.floor(x / 4) + Math.floor(t * 25) * 977) - .5) * .9;
      else if (opt.rampe !== undefined) { const d = u - opt.rampe; v -= d > -.35 && d < 0 ? (d + .35) / .35 * 1.1 : 0; }
      x === x0 ? g.moveTo(x, y + v * amp) : g.lineTo(x, y + v * amp);
    }
    g.stroke(); g.restore();
  }

  // flèche de (x0, y0) à (x1, y1), tracée jusqu'à k
  function fleche(x0, y0, x1, y1, k, st) {
    if (k <= 0) return;
    g.save(); style(st);
    const x = x0 + (x1 - x0) * k, y = y0 + (y1 - y0) * k, a = Math.atan2(y1 - y0, x1 - x0), L = (st.ep || 8) * 4;
    g.beginPath(); g.moveTo(x0, y0); g.lineTo(x, y); g.stroke();
    g.beginPath(); g.moveTo(x + Math.cos(a + 2.6) * L, y + Math.sin(a + 2.6) * L); g.lineTo(x, y); g.lineTo(x + Math.cos(a - 2.6) * L, y + Math.sin(a - 2.6) * L); g.stroke();
    g.restore();
  }

  // bouton lecture (logo de la chaîne)
  function lecture(cx, cy, r, coul, fond) {
    g.save(); g.fillStyle = fond; g.beginPath();
    const w = r * 1.45, h = r, rr = r * .28;
    g.roundRect(cx - w, cy - h, 2 * w, 2 * h, rr); g.fill();
    g.fillStyle = coul; g.beginPath(); g.moveTo(cx - r * .38, cy - r * .55); g.lineTo(cx + r * .6, cy); g.lineTo(cx - r * .38, cy + r * .55); g.closePath(); g.fill();
    g.restore();
  }

  S.d = { horloge, main, tete, cerveau, pierre, eeg, fleche, lecture };
})();
