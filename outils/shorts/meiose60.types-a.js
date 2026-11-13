// Plans propres au short « meiose60 » (« La méiose en 60 secondes »), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Code couleur des schémas : chromosome venu du père en or, chromosome venu de la mère en rouge ; schémas à 2n = 4
// (une grande paire, une petite paire). Un chromosome à deux chromatides = deux bâtonnets réunis au centromère.
window.SANS_ST_A = ['chrono', 'puissance', 'milliards', 'piege'];
window.PROPRES_A = ['chrono', 'divisions', 'bivalent', 'meta', 'puissance', 'fecond', 'milliards', 'piege'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const pop = (k, x, y, f) => { if (k <= 0) return; const s = back(k); g.save(); g.translate(x, y); g.scale(s, s); g.globalAlpha = cl(k * 3); f(); g.restore(); };
  const rond = (x, y, r, fond, trait, ep = 6) => { g.beginPath(); g.arc(x, y, r, 0, 7); if (fond) { g.fillStyle = fond; g.fill(); } if (trait) { g.strokeStyle = trait; g.lineWidth = ep; g.stroke(); } };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const note = (s, x, y, coul = CREME, taille = 40) => S.texte(s, x, y, { taille, police: 'Spectral', it: true, poids: 400, coul });

  // ---------- chromosomes
  // bâtonnet vertical centré en (x, y), hauteur h, largeur w ; haut = couleur de la partie au-dessus de yc (crossing-over)
  function baton(x, y, h, w, coul, haut, yc) {
    g.save(); g.beginPath(); g.roundRect(x - w / 2, y - h / 2, w, h, w / 2); g.fillStyle = coul; g.fill();
    if (haut) { g.save(); g.clip(); g.fillStyle = haut; g.fillRect(x - w, y - h / 2 - 2, 2 * w, yc - (y - h / 2) + 2); g.restore(); }
    g.strokeStyle = NOIR; g.lineWidth = 3; g.stroke(); g.restore();
  }
  // chromosome : deux chromatides (double) ou une seule ; s = échelle
  function chromo(x, y, h, coul, double, s = 1) {
    const w = 16 * s, e = 7 * s;
    if (double) { baton(x - w / 2 - e / 2, y, h, w, coul); baton(x + w / 2 + e / 2, y, h, w, coul); rond(x, y - h * .12, w * .55, coul, NOIR, 3); }
    else baton(x, y, h, w, coul);
  }
  // contenu d'une cellule : liste [grand/petit, couleur] ; double = chromatides doubles
  function cellule(x, y, r, contenu, double, s = 1) {
    g.save(); g.fillStyle = 'rgba(239,230,210,.06)'; g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); g.strokeStyle = CREME; g.lineWidth = 5; g.stroke(); g.restore();
    const n = contenu.length, pas = Math.min(60 * s, (r * 1.3) / n);
    contenu.forEach(([grand, c], i) => chromo(x + (i - (n - 1) / 2) * pas, y, (grand ? 150 : 90) * s, c, double, s * .9));
  }

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

  // ---------- les deux divisions : p.etape 0 (la cellule 2n) | 2 (les deux divisions, animées) | 3 (les 4 gamètes n)
  const MERE = [[1, OR], [1, ROUGE], [0, OR], [0, ROUGE]];
  function divisions(p, t) {
    const lt = t - p.a, y = 840;
    if (p.etape === 0) {
      const k = back(pr(lt, 0, .35)); g.save(); g.translate(540, y); g.scale(k, k); cellule(0, 0, 250, MERE, true, 1.25); g.restore();
      S.texte('2n = 46', 540, 470, { taille: 110, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 10 });
      note('(schéma : 2n = 4 · du père en or, de la mère en rouge)', 540, 1150, GRIS, 36);
    } else {
      const k1 = p.etape === 3 ? 1 : eo(pr(lt, .1, .7)), k2 = p.etape === 3 ? 1 : eo(pr(lt, 1.0, .7));
      if (k2 <= 0) {
        if (k1 < .5) cellule(540, y, lerp(250, 200, k1 * 2), MERE, true, 1.1);
        else [[300, [[1, OR], [0, ROUGE]]], [780, [[1, ROUGE], [0, OR]]]].forEach(([x, c]) => cellule(lerp(540, x, (k1 - .5) * 2), y, 170, c, true, 1));
      } else {
        [[300, [[1, OR], [0, ROUGE]], [150, 400]], [780, [[1, ROUGE], [0, OR]], [680, 930]]].forEach(([x, c, xs]) => xs.forEach(xx => cellule(lerp(x, xx, k2), y, lerp(170, 105, k2), c, false, .85)));
      }
      g.save(); g.globalAlpha = cl(k1 * 2); S.texte('MÉIOSE I', 300, 560, { taille: 46, coul: CREME, esp: 4 }); g.restore();
      if (k2 > 0) { g.save(); g.globalAlpha = cl(k2 * 2); S.texte('MÉIOSE II', 780, 560, { taille: 46, coul: CREME, esp: 4 }); g.restore(); }
      if (p.etape === 3) {
        pop(pr(lt, .1, .3), 540, 1110, () => S.texte('4 GAMÈTES', 0, 0, { taille: 90, coul: OR, contour: NOIR, contourL: 10 }));
        pop(pr(lt, .4, .3), 540, 1240, () => S.texte('n = 23', 0, 0, { taille: 110, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 10 }));
      }
    }
    if (p.t) deux(p.t, 1440, 100);
  }

  // ---------- le crossing-over : p.etape 'apparie' | 'chiasma' | 'echange' | 'resultat'
  // chromatides : or extérieure, or intérieure (non sœur de la rouge intérieure), rouge intérieure, rouge extérieure
  function bivalent(p, t) {
    const lt = t - p.a, y = 830, h = 640, yc = 650, haut = y - h / 2;
    const e = p.etape;
    if (e === 'apparie') {
      const k = eo(pr(lt, .1, .9)), xo = lerp(260, 505, k), xr = lerp(820, 575, k);
      [[xo, OR], [xr, ROUGE]].forEach(([x, c]) => { baton(x - 22, y, h, 34, c); baton(x + 22, y, h, 34, c); rond(x, y + 60, 18, c, NOIR, 3); });
      g.save(); g.globalAlpha = 1 - k * .3; note('venu du père', xo, haut - 50, OR); note('venu de la mère', xr, haut - 50, ROUGE); g.restore();
      if (k > .9) pop(pr(lt, 1.0, .3), 540, 1230, () => S.texte('4 CHROMATIDES', 0, 0, { taille: 70, coul: CREME, contour: NOIR, contourL: 8 }));
    } else if (e === 'chiasma' || e === 'echange') {
      const kx = e === 'chiasma' ? eo(pr(lt, .1, .5)) : 1, ke = e === 'echange' ? pr(lt, .15, .9) : 0;
      baton(461, y, h, 34, OR); baton(619, y, h, 34, ROUGE);
      rond(483, y + 60, 18, OR, NOIR, 3); rond(597, y + 60, 18, ROUGE, NOIR, 3);
      // chromatides intérieures (non sœurs) : bas → jonction (jx, yc) → haut (xt) ; cb / ch = couleurs du bas et du haut
      const brin = (xb, jx, xt, cb, ch) => {
        const bas = [[xb, y + h / 2 - 17], [xb, yc + 70], [jx, yc]], hautP = [[jx, yc], [xt, yc - 70], [xt, haut + 17]];
        [[bas, cb], [hautP, ch]].forEach(([P, c]) => { g.save(); g.lineCap = 'round'; g.lineJoin = 'round';
          [[NOIR, 40], [c, 34]].forEach(([cc, ep]) => { g.strokeStyle = cc; g.lineWidth = ep; g.beginPath(); P.forEach(([px, py], i) => i ? g.lineTo(px, py) : g.moveTo(px, py)); g.stroke(); });
          g.restore(); });
      };
      if (e === 'chiasma') { brin(505, lerp(505, 540, kx), lerp(505, 575, kx), OR, OR); brin(575, lerp(575, 540, kx), lerp(575, 505, kx), ROUGE, ROUGE); }
      else { const kj = ke < .4 ? 1 : 1 - eo((ke - .4) / .6);
        // cassure au chiasma puis recollement : la chromatide or reçoit le haut rouge, et inversement
        brin(505, lerp(505, 540, kj), 505, OR, ROUGE); brin(575, lerp(575, 540, kj), 575, ROUGE, OR); }
      if (kx > .5) { const kk = pr(lt, .4, .3); g.save(); g.globalAlpha = cl(kk * 2); g.strokeStyle = CREME; g.lineWidth = 5; rond(540, yc, 70, null, CREME, 5);
        g.beginPath(); g.moveTo(610, yc); g.lineTo(760, yc - 70); g.stroke(); S.texte('CHIASMA', 860, yc - 100, { taille: 54, coul: CREME, contour: NOIR, contourL: 8 }); g.restore(); }
      if (e === 'echange' && ke > .2 && ke < .6) { g.save(); g.globalAlpha = cl(1 - Math.abs(ke - .4) * 5); g.fillStyle = '#fff6d8'; for (let i = 0; i < 8; i++) { const a = i / 8 * 6.28; rond(540 + Math.cos(a) * 60, yc + Math.sin(a) * 60, 7, '#fff6d8'); } g.restore(); }
      if (e === 'echange') note('elles se cassent et échangent leurs segments', 540, 1210, CREME, 40);
    } else {
      // résultat : deux chromatides parentales, deux recombinées
      const k = eo(pr(lt, .1, .6));
      const L = [[lerp(461, 300, k), OR, null], [lerp(505, 344, k), OR, ROUGE], [lerp(575, 736, k), ROUGE, OR], [lerp(619, 780, k), ROUGE, null]];
      L.forEach(([x, c, hc]) => baton(x, y, h, 34, c, hc, yc));
      rond((L[0][0] + L[1][0]) / 2, y + 60, 18, OR, NOIR, 3); rond((L[2][0] + L[3][0]) / 2, y + 60, 18, ROUGE, NOIR, 3);
      g.save(); g.globalAlpha = k;
      const yl = y + h / 2 + 50, op = (s, x, yy, al) => S.texte(s, x, yy, { taille: 36, police: 'Spectral', it: true, poids: 400, coul: s === 'recombinée' ? OR : '#b8ad97', align: al });
      op('parentale', L[0][0] - 20, yl, 'right'); op('recombinée', L[1][0] + 20, yl, 'left');
      op('recombinée', L[2][0] - 20, yl + 50, 'right'); op('parentale', L[3][0] + 20, yl + 50, 'left');
      g.restore();
    }
    O.petitTitre(e === 'resultat' ? 'APRÈS LE CROSSING-OVER' : 'PROPHASE I', 380, e === 'resultat' ? OR : CREME);
    if (p.t) deux(p.t, 1440, 100);
  }

  // ---------- métaphase I (orientation au hasard) puis anaphase I (les homologues se séparent)
  function meta(p, t) {
    const lt = t - p.a, cx = 540, cy = 860;
    g.save(); g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.ellipse(cx, cy, 380, 360, 0, 0, 7); g.stroke();
    g.setLineDash([16, 14]); g.strokeStyle = OR; g.beginPath(); g.moveTo(cx - 360, cy); g.lineTo(cx + 360, cy); g.stroke(); g.setLineDash([]);
    g.strokeStyle = 'rgba(239,230,210,.18)'; g.lineWidth = 3;
    for (let i = -3; i <= 3; i++) { g.beginPath(); g.moveTo(cx, cy - 330); g.quadraticCurveTo(cx + i * 90, cy, cx, cy + 330); g.stroke(); }
    g.restore();
    note('équateur', cx + 300, cy - 30, OR, 34);
    // orientation de la petite paire : bascule pendant la métaphase, fixée en anaphase
    let f = 0;
    if (p.etape === 'meta') { const ph = (lt * .9) % 2; f = ph < 1 ? eo(cl((ph - .6) / .4)) : 1 - eo(cl((ph - 1.6) / .4)); }
    else f = 1;
    const sep = p.etape === 'ana' ? eo(pr(lt, .1, .9)) : 0, d = lerp(85, 250, sep);
    // grande paire : or en haut, rouge en bas ; petite paire : l'orientation change (f)
    chromo(cx - 110, cy - d, 150, OR, true, 1.2); chromo(cx - 110, cy + d, 150, ROUGE, true, 1.2);
    // la petite paire pivote d'un demi-tour quand son orientation change (or en haut → rouge en haut)
    const c = Math.cos(Math.PI * f), sn = Math.sin(Math.PI * f), dp = d * .9;
    chromo(cx + 110 + dp * sn * .7, cy - dp * c, 95, OR, true, 1.2); chromo(cx + 110 - dp * sn * .7, cy + dp * c, 95, ROUGE, true, 1.2);
    if (p.etape === 'meta') note(f > .5 ? 'ou l’inverse…' : 'une orientation…', cx + 110, cy + 200, CREME, 36);
    if (p.etape === 'meta') { O.petitTitre('MÉTAPHASE I', 380); pop(pr(lt, .5, .3), cx, 1300, () => S.texte('AU HASARD', 0, 0, { taille: 90, coul: OR, contour: NOIR, contourL: 10 })); }
    else { O.petitTitre('ANAPHASE I', 380, ROUGE); [[-1], [1]].forEach(([s]) => S.d.fleche(cx + 330, cy + s * 120, cx + 330, cy + s * 280, sep, { trait: CREME, ep: 8 }));
      note('chaque chromosome garde ses 2 chromatides', cx, 1290, CREME, 40); }
    if (p.t) deux(p.t, 1450, 100);
  }

  // ---------- 2 puissance 23 : p.etape 1 (2 × 2 × … ) | 2 (le compteur)
  function puissance(p, t) {
    const lt = t - p.a;
    if (p.etape === 1) {
      O.petitTitre('2 POSSIBILITÉS PAR PAIRE', 480);
      const n = Math.min(23, Math.floor(lt / .06) + 1);
      for (let i = 0; i < n; i++) { const x = 130 + (i % 8) * 117, y = 660 + Math.floor(i / 8) * 120;
        S.texte(i ? '× 2' : '2', x, y, { taille: 64, police: 'Spectral', poids: 600, coul: i % 2 ? CREME : OR }); }
      if (n >= 23) { const k = back(pr(lt, 23 * .06 + .1, .35)); g.save(); g.translate(W / 2, 1180); g.scale(k, k);
        S.texte('2²³', 0, 0, { taille: 240, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14 }); g.restore();
        S.texte('23 paires de chromosomes', W / 2, 1340, { taille: 50, police: 'Spectral', it: true, poids: 400, coul: CREME }); }
    } else {
      const k = eo(pr(lt, .05, 1.1)), n = Math.round(lerp(2, 8388608, k * k * k));
      S.texte('2²³ =', W / 2, 640, { taille: 120, police: 'Spectral', poids: 600, coul: OR });
      S.texte(String(n).replace(/\B(?=(\d{3})+$)/g, ' '), W / 2, 880, { taille: 190, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 12, max: 1000 });
      S.texte('GAMÈTES DIFFÉRENTS', W / 2, 1060, { taille: 70, coul: OR, esp: 4 });
      S.texte('possibles, pour une seule personne', W / 2, 1160, { taille: 50, police: 'Spectral', it: true, poids: 400, coul: CREME });
    }
  }

  // ---------- la fécondation : deux gamètes n se réunissent ; p.somme = repère de « 23 plus 23 »
  function fecond(p, t) {
    const lt = t - p.a, k = eo(pr(lt, .1, 1.4)), y = 820;
    // ovule
    if (lt < 1.5) { cellule(lerp(760, 600, k), y, 200, [[1, ROUGE], [0, ROUGE]], false, 1); }
    // spermatozoïde
    const xs = lerp(160, 470, k);
    if (lt < 1.5) { g.save(); g.strokeStyle = CREME; g.lineWidth = 6; g.beginPath(); for (let i = 0; i <= 30; i++) { const xx = xs - 40 - i * 8; g.lineTo(xx, y + Math.sin(i * .6 - t * 14) * 14); } g.stroke(); g.restore();
      g.save(); g.fillStyle = 'rgba(239,230,210,.12)'; g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.ellipse(xs, y, 46, 32, 0, 0, 7); g.fill(); g.stroke(); g.restore();
      chromo(xs - 10, y, 34, OR, false, .45); chromo(xs + 12, y, 22, OR, false, .45); }
    if (lt >= 1.5) { const kk = back(pr(lt, 1.5, .35)); g.save(); g.translate(560, y); g.scale(kk, kk); cellule(0, 0, 230, [[1, OR], [1, ROUGE], [0, OR], [0, ROUGE]], false, 1.1); g.restore();
      note('cellule-œuf', 560, y + 280, CREME, 46); }
    note('spermatozoïde (n)', 230, y - 130, OR, 38); note('ovule (n)', 840, y - 250, ROUGE, 38);
    if (p.somme && t >= tps(p.somme)) { const ks = back(pr(t, tps(p.somme), .35)); g.save(); g.translate(W / 2, 1300); g.scale(ks, ks);
      S.texte('23 + 23 = 46', 0, 0, { taille: 130, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 12 }); g.restore(); }
    O.petitTitre('LA FÉCONDATION, AU HASARD', 400);
  }

  // ---------- 8 millions × 8 millions ≈ 70 000 milliards ; p.big = repère du grand nombre
  function milliards(p, t) {
    const lt = t - p.a;
    const k1 = back(pr(lt, 0, .3)); g.save(); g.translate(W / 2, 640); g.scale(k1, k1);
    S.texte('8 millions × 8 millions', 0, 0, { taille: 84, police: 'Spectral', poids: 600, coul: CREME, max: 980 }); g.restore();
    if (p.big && t >= tps(p.big)) {
      const k = eo(pr(t, tps(p.big), .9)), n = Math.round(lerp(0, 70000, k) / 100) * 100;
      S.texte('de l’ordre de', W / 2, 820, { taille: 54, police: 'Spectral', it: true, poids: 400, coul: CREME });
      S.texte(String(n).replace(/\B(?=(\d{3})+$)/g, ' '), W / 2, 980, { taille: 210, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 14 });
      S.texte('MILLIARDS', W / 2, 1140, { taille: 120, coul: OR, contour: NOIR, contourL: 10 });
      S.texte('de combinaisons pour un seul couple', W / 2, 1270, { taille: 50, police: 'Spectral', it: true, poids: 400, coul: CREME });
    }
  }

  // ---------- le piège : intra / inter ; p.intra, p.inter (repères) ; p.cumul
  function piege(p, t) {
    const ki = p.intra ? pr(t, tps(p.intra), .35) : 1, ke = p.inter ? pr(t, tps(p.inter), .35) : 1;
    const carte = (x, k, titre, l1, l2, coul, dessin) => { if (k <= 0) return; g.save(); g.globalAlpha = cl(k * 2); g.translate(0, lerp(80, 0, eo(k)));
      g.fillStyle = 'rgba(239,230,210,.06)'; g.strokeStyle = coul; g.lineWidth = 6; g.beginPath(); g.roundRect(x - 230, 470, 460, 860, 30); g.fill(); g.stroke();
      S.texte(titre, x, 560, { taille: 90, coul, contour: NOIR, contourL: 8 }); dessin(x);
      S.texte(l1, x, 1080, { taille: 46, coul: CREME, max: 420 }); S.texte(l2, x, 1200, { taille: 62, coul: OR, max: 420 }); g.restore(); };
    carte(290, ki, 'INTRA', 'une même paire', 'PROPHASE I', OR, x => { baton(x - 60, 820, 300, 26, OR); baton(x - 25, 820, 300, 26, OR, ROUGE, 740); baton(x + 25, 820, 300, 26, ROUGE, OR, 740); baton(x + 60, 820, 300, 26, ROUGE);
      rond(x, 740, 40, null, CREME, 4); });
    carte(790, ke, 'INTER', 'paires différentes', 'ANAPHASE I', ROUGE, x => { chromo(x - 60, 760, 150, OR, true, 1); chromo(x - 60, 900, 150, ROUGE, true, 1); chromo(x + 60, 770, 90, ROUGE, true, 1); chromo(x + 60, 890, 90, OR, true, 1);
      g.save(); g.setLineDash([12, 10]); g.strokeStyle = OR; g.lineWidth = 4; g.beginPath(); g.moveTo(x - 160, 830); g.lineTo(x + 160, 830); g.stroke(); g.restore(); });
    if (ke > 0) note('préparé en métaphase I', 790, 1280, CREME, 34);
    if (p.cumul) O.tampon('ILS SE CUMULENT', W / 2, 1450, pr(t, p.a + .15, .3), -.08, 84, OR);
    else O.petitTitre('NE LES CONFONDS PAS', 400, ROUGE);
  }

  return { chrono, divisions, bivalent, meta, puissance, fecond, milliards, piege };
};

// sons propres à ces plans
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono') { if (p.run) for (let x = p.a; x < p.b - .1; x += 1) L.push([x, 'tic', .5]); else L.push([p.a + .1, 'tic', .4]); }
  if (p.type === 'divisions') { if (p.etape === 2) L.push([p.a + .1, 'whoosh', .4], [p.a + 1.0, 'whoosh', .4]); else L.push([p.a, 'pop', .4]); }
  if (p.type === 'bivalent') { if (p.etape === 'apparie') L.push([p.a + .1, 'aspire', .4]); if (p.etape === 'chiasma') L.push([p.a + .4, 'clic', .5]); if (p.etape === 'echange') L.push([p.a + .3, 'lame', .5]); if (p.etape === 'resultat') L.push([p.a + .1, 'frotte', .4]); }
  if (p.type === 'meta') L.push([p.a + .1, p.etape === 'ana' ? 'whoosh' : 'blip', .4]);
  if (p.type === 'puissance') { if (p.etape === 1) for (let k = 0; k < 23; k += 3) L.push([p.a + k * .06, 'tic', .35]); else L.push([p.a + .05, 'montee', .5]); }
  if (p.type === 'fecond') { L.push([p.a + 1.5, 'pop', .6]); if (p.somme) L.push([tps(p.somme), 'valide', .5]); }
  if (p.type === 'milliards') { L.push([p.a, 'blip', .4]); if (p.big) L.push([tps(p.big), 'montee', .5]); }
  if (p.type === 'piege') { if (p.intra) L.push([tps(p.intra), 'pop', .5]); if (p.inter) L.push([tps(p.inter), 'pop', .5]); if (p.cumul) L.push([p.a + .2, 'tampon', .9]); }
};
