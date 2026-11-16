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
// Formats « le spectateur joue » (15/11/2026) : niveau, ordre, intrus, devine, plusmoins, erreur (champs en tête de
// chaque fonction ci-dessous). Plans de modele-a.js utiles avec eux : photo (photo couleur plein écran), collage.
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

  // ---------------------------------------------------------------- formats « le spectateur joue » (15/11/2026)
  const al = O.al;
  function chrono(t, tc, tr, x, y, r = 95) {
    if (t < tc || t >= tr) return;
    const u = cl((t - tc) / Math.max(.6, tr - tc)), reste = Math.ceil(tr - t);
    g.save(); g.translate(x, y); g.strokeStyle = al(CREME, .2); g.lineWidth = r * .16; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
    g.strokeStyle = u > .7 ? ROUGE : OR; g.beginPath(); g.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + (1 - u) * 6.283); g.stroke();
    S.texte(String(Math.max(0, reste)), 0, 4, { taille: r, coul: CREME }); g.restore();
  }
  function carteTexte(txt, x, y, w, h, o = {}) {  // carte claire avec un texte sombre centré
    g.save(); g.translate(x, y); g.fillStyle = o.fond || '#f3ecdc'; g.shadowColor = 'rgba(0,0,0,.55)'; g.shadowBlur = 30;
    g.beginPath(); g.roundRect(-w / 2, -h / 2, w, h, 22); g.fill(); g.shadowColor = 'transparent';
    if (o.bord) { g.strokeStyle = o.bord; g.lineWidth = o.ep || 8; g.stroke(); }
    const L = String(txt).split('|'); L.forEach((s, i) => S.texte(s, 0, (o.dy || 0) + (i - (L.length - 1) / 2) * (o.taille || 60) * 1.2, { taille: o.taille || 60, police: o.police || 'Spectral', poids: 600, coul: o.coul || '#16120d', max: w - 60 }));
    g.restore();
  }

  // niveau : échelle de difficulté (« Niveau 1 → 10, à quel niveau tu t'arrêtes ? »). Champs : n, total (10),
  // q (question, « | »), r (réponse), expl, chrono, rep, img (image facultative au-dessus de la question).
  function niveau(p, t) {
    const tot = p.total || 10, tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a + .5, avant = t < tr;
    const k = back(pr(t, p.a, .35)), u = (p.n - 1) / Math.max(1, tot - 1);
    const coulN = u < .34 ? VERT : u < .67 ? OR : ROUGE, lab = u < .25 ? 'FACILE' : u < .5 ? 'MOYEN' : u < .8 ? 'DIFFICILE' : 'IMPOSSIBLE';
    g.save(); g.translate(W / 2, 330); g.scale(lerp(1.8, 1, k), lerp(1.8, 1, k));
    S.texte('NIVEAU ' + p.n, 0, 0, { taille: 120, coul: coulN, contour: NOIR, contourL: 12 }); g.restore();
    S.texte(lab, W / 2, 430, { taille: 40, coul: coulN, esp: 12, poids: 700 });
    for (let i = 0; i < tot; i++) {  // barre de difficulté
      const x = W / 2 - tot * 42 + i * 84 + 42, on = i < p.n, c = i / (tot - 1) < .34 ? VERT : i / (tot - 1) < .67 ? OR : ROUGE;
      const ki = i === p.n - 1 ? 1 + .25 * Math.abs(Math.sin(t * 8)) : 1;
      g.save(); g.translate(x, 500); g.scale(ki, ki); g.fillStyle = on ? c : al(CREME, .12); g.beginPath(); g.roundRect(-34, -14, 68, 28, 10); g.fill(); g.restore();
    }
    let yq = 760;
    if (p.img) { O.carte(p.img, W / 2, 790, 520, 360, -.02, 1.05, .5, .4); yq = 1110; }
    const kq = eo(pr(t, p.a + .15, .3)); g.save(); g.globalAlpha = kq; carteTexte(p.q, W / 2, yq, 960, p.img ? 230 : 320, { taille: p.img ? 56 : 66 }); g.restore();
    if (avant) chrono(t, tc, tr, W / 2, p.img ? 1400 : 1180, 100);
    else {
      const kv = back(pr(t, tr, .3)); g.save(); g.translate(W / 2, p.img ? 1360 : 1180); g.scale(kv, kv);
      carteTexte(p.r, 0, 0, 860, 150, { fond: VERT, coul: '#0b1a07', taille: 72, police: 'Archivo' }); g.restore();
      if (p.expl) { const ke = eo(pr(t, tr + .3, .3)); g.save(); g.globalAlpha = ke;
        p.expl.split('|').forEach((x, i) => S.texte(x, W / 2, (p.img ? 1500 : 1340) + i * 62, { taille: 50, coul: CREME, max: 960, contour: NOIR, contourL: 8 })); g.restore(); }
    }
  }

  // ordre : remets dans l'ordre. Champs : sur ('REMETS DANS L'ORDRE'), cartes = [{t, d}] (dans l'ordre montré, mélangé),
  // ordre = [indices des cartes montrées, dans le bon ordre], chrono, rep, expl. Au verdict, les cartes glissent à leur place
  // et leur date (d) apparaît.
  function ordre(p, t) {
    const C = p.cartes || [], tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a + .6, avant = t < tr;
    S.texte(p.sur || 'REMETS DANS L’ORDRE', W / 2, 320, { taille: 54, coul: OR, esp: 6, max: 980 });
    const rang = C.map((_, i) => (p.ordre || []).indexOf(i)), km = eo(pr(t, tr, .7)), h = 190, y0 = 560;
    C.forEach((c, i) => {
      const ki = back(pr(t, p.a + .15 + i * .12, .3)); if (ki <= 0) return;
      const yA = y0 + i * (h + 30), yB = y0 + rang[i] * (h + 30), y = lerp(yA, yB, km) + (avant ? Math.sin(t * 6 + i) * 4 : 0);
      g.save(); g.translate(lerp(i % 2 ? 700 : -700, 0, ki), 0);
      const kd = !avant && c.d ? eo(pr(t, tr + .6 + rang[i] * .12, .3)) : 0;
      carteTexte(c.t, W / 2 + 40, y, 820, h, { taille: 56, bord: !avant ? VERT : null, ep: 6, dy: -24 * kd });
      const lbl = avant ? 'ABCDEF'[i] : String(rang[i] + 1);
      g.fillStyle = avant ? OR : VERT; g.beginPath(); g.arc(110, y, 54, 0, 7); g.fill(); S.texte(lbl, 110, y + 4, { taille: 64, coul: NOIR });
      if (kd > 0) { g.globalAlpha = kd; S.texte(c.d, W / 2 + 40, y + 46, { taille: 40, coul: '#9a2b20', poids: 700, max: 760 }); }
      g.restore();
    });
    if (avant) chrono(t, tc, tr, W / 2, 1520, 90);
    else if (p.expl) { const ke = eo(pr(t, tr + 1, .3)); g.save(); g.globalAlpha = ke;
      p.expl.split('|').forEach((x, i) => S.texte(x, W / 2, 1500 + i * 60, { taille: 48, coul: CREME, max: 960, contour: NOIR, contourL: 8 })); g.restore(); }
  }

  // intrus : trouve l'intrus. Champs : sur, options = [{t, img, sous}] (4, en grille 2 × 2), intrus (indice), chrono, rep, expl.
  function intrus(p, t) {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a + .6, avant = t < tr;
    S.texte(p.sur || 'TROUVE L’INTRUS', W / 2, 300, { taille: 58, coul: OR, esp: 6, max: 980 });
    (p.options || []).forEach((o, i) => {
      const ki = back(pr(t, p.a + .1 + i * .12, .3)); if (ki <= 0) return;
      const cx = i % 2 ? 790 : 290, cy = i < 2 ? 680 : 1160, bad = i === p.intrus, kr = back(pr(t, tr, .35));
      g.save(); g.translate(cx, cy); const sc = ki * (!avant && bad ? lerp(1, 1.12, kr) : 1); g.scale(sc, sc);
      g.globalAlpha = !avant && !bad ? .3 : 1;
      g.fillStyle = al(CREME, .08); g.beginPath(); g.roundRect(-235, -220, 470, 440, 26); g.fill();
      g.strokeStyle = !avant && bad ? ROUGE : al(CREME, .35); g.lineWidth = !avant && bad ? 10 : 3; g.stroke();
      const im = o.img && S.img(o.img);
      if (im) { g.save(); g.beginPath(); g.roundRect(-205, -195, 410, 270, 16); g.clip(); g.filter = o.nb ? 'grayscale(1) contrast(1.2)' : 'contrast(1.05) saturate(1.1)'; S.cover(im, -205, -195, 410, 270, 1.05, .5, .35); g.restore(); }
      S.texte(o.t, 0, im ? 130 : -10, { taille: im ? 50 : 64, coul: CREME, max: 420 });
      if (o.sous) S.texte(o.sous, 0, im ? 180 : 60, { taille: 32, police: 'Spectral', it: true, poids: 400, coul: GRIS, max: 420 });
      g.restore();
      if (!avant && bad) O.tampon('INTRUS', cx, cy, pr(t, tr + .1, .3), -.12, 90, ROUGE);
    });
    if (avant) chrono(t, tc, tr, W / 2, 1530, 90);
    else if (p.expl) { const ke = eo(pr(t, tr + .4, .3)); g.save(); g.globalAlpha = ke;
      p.expl.split('|').forEach((x, i) => S.texte(x, W / 2, 1500 + i * 60, { taille: 48, coul: CREME, max: 960, contour: NOIR, contourL: 8 })); g.restore(); }
  }

  // devine : devine qui / quoi c'est. Image pixellisée qui se précise à chaque indice. Champs : img, sur,
  // indices = [[repère, texte], …], rep (repère de la révélation), nom, sous.
  let pix;
  function devine(p, t) {
    const I = p.indices || [], tr = tps(p.rep), avant = t < tr, vus = I.filter(([a]) => t >= tps(a)).length;
    S.texte(p.sur || 'DEVINE QUI C’EST', W / 2, 300, { taille: 58, coul: OR, esp: 6, max: 980 });
    const im = S.img(p.img);
    if (im) {
      const bloc = avant ? [70, 40, 24, 14, 9][Math.min(4, vus)] : 1, w = 640, h = 760, x = W / 2 - w / 2, y = 380;
      g.save(); g.beginPath(); g.roundRect(x, y, w, h, 24); g.clip();
      if (bloc > 1) {
        if (!pix) pix = document.createElement('canvas');
        pix.width = Math.ceil(w / bloc); pix.height = Math.ceil(h / bloc); const px = pix.getContext('2d');
        const sc = Math.max(pix.width / im.width, pix.height / im.height) * 1.05; px.filter = 'contrast(1.1) brightness(1.35)';
        px.drawImage(im, (pix.width - im.width * sc) / 2, (pix.height - im.height * sc) * .35, im.width * sc, im.height * sc);
        g.imageSmoothingEnabled = false; g.drawImage(pix, x, y, w, h); g.imageSmoothingEnabled = true;
      } else { const kr = eo(pr(t, tr, .4)); g.filter = `contrast(1.05) saturate(1.1) brightness(${lerp(2.2, 1, kr)})`; S.cover(im, x, y, w, h, 1.05, .5, .35); g.filter = 'none'; }
      g.restore(); g.strokeStyle = avant ? OR : VERT; g.lineWidth = 8; g.beginPath(); g.roundRect(x, y, w, h, 24); g.stroke();
    }
    I.forEach(([a, txt], i) => {
      const ki = back(pr(t, tps(a), .3)); if (ki <= 0 || !avant) return;
      const y = 1250 + i * 92; g.save(); g.globalAlpha = cl(ki); g.translate(lerp(-300, 0, ki), 0);
      g.fillStyle = al(OR, .16); g.beginPath(); g.roundRect(110, y - 38, 860, 76, 38); g.fill();
      S.texte('INDICE ' + (i + 1), 140, y, { taille: 30, coul: OR, align: 'left', poids: 700 });
      S.texte(txt, 340, y, { taille: 40, coul: CREME, align: 'left', max: 610 }); g.restore();
    });
    if (!avant) {
      const kv = back(pr(t, tr, .35)); g.save(); g.translate(W / 2, 1300); g.scale(lerp(1.8, 1, kv), lerp(1.8, 1, kv)); g.globalAlpha = cl(kv);
      S.texte(p.nom, 0, 0, { taille: 120, coul: OR, contour: NOIR, contourL: 12, max: 980 }); g.restore();
      if (p.sous) { const ks = eo(pr(t, tr + .3, .3)); g.save(); g.globalAlpha = ks;
        p.sous.split('|').forEach((x, i) => S.texte(x, W / 2, 1420 + i * 60, { taille: 48, it: true, poids: 400, police: 'Spectral', coul: CREME, max: 960 })); g.restore(); }
    }
  }

  // plusmoins : plus ou moins ? Champs : sur, q (« Lequel est le plus … ? »), a = {t, img, v, u}, b = {t, img, v, u},
  // chrono, rep. La valeur de a est donnée ; celle de b défile au verdict, flèche PLUS / MOINS.
  function plusmoins(p, t) {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a + .6, avant = t < tr;
    const fmt = v => Math.round(v).toLocaleString('fr-FR');
    [p.a_ || p.A, p.B].forEach(() => {});
    [['A', p.A, 0], ['B', p.B, 1]].forEach(([_, o, j]) => {
      if (!o) return; const y0 = j ? 960 : 0, hh = 960, ki = eo(pr(t, p.a + j * .2, .35));
      g.save(); g.beginPath(); g.rect(0, y0, W, hh); g.clip(); g.translate(j ? lerp(W, 0, ki) : lerp(-W, 0, ki), 0);
      const im = o.img && S.img(o.img);
      if (im) { g.filter = 'contrast(1.05) saturate(1.1) brightness(.62)'; S.cover(im, 0, y0, W, hh, 1.08 + (t - p.a) * .01, .5, .45); g.filter = 'none'; }
      else { g.fillStyle = j ? al(ROUGE, .15) : al(OR, .1); g.fillRect(0, y0, W, hh); }
      S.texte(o.t, W / 2, y0 + 380, { taille: 76, coul: CREME, contour: NOIR, contourL: 10, max: 980 });
      let val;
      if (!j) val = fmt(o.v) + (o.u ? ' ' + o.u : '');
      else if (avant) val = '?';
      else val = fmt(o.v * eo(cl((t - tr) / .9))) + (o.u ? ' ' + o.u : '');
      S.texte(val, W / 2, y0 + 540, { taille: 110, coul: j ? (avant ? CREME : OR) : OR, contour: NOIR, contourL: 12, police: 'Spectral', poids: 700, max: 980 });
      if (j && !avant && t > tr + .9) { const plus = p.B.v > p.A.v, kf = back(pr(t, tr + .9, .3)); g.save(); g.translate(W / 2, y0 + 700); g.scale(kf, kf);
        S.texte(plus ? '▲ PLUS' : '▼ MOINS', 0, 0, { taille: 90, coul: plus ? VERT : ROUGE, contour: NOIR, contourL: 10 }); g.restore(); }
      g.restore();
    });
    g.fillStyle = NOIR; g.fillRect(0, 950, W, 20);
    g.save(); g.translate(W / 2, 960); g.fillStyle = OR; g.beginPath(); g.arc(0, 0, 80, 0, 7); g.fill(); S.texte('VS', 0, 4, { taille: 64, coul: NOIR }); g.restore();
    if (p.q) S.texte(p.q, W / 2, 300, { taille: 50, coul: OR, contour: NOIR, contourL: 8, max: 980 });
    if (avant) chrono(t, tc, tr, 930, 1100, 70);
  }

  // erreur : trouve l'erreur dans une copie. Champs : matiere, sujet, lignes = ['…', …] (6 au plus), faute (indice),
  // correction, chrono, rep. Au verdict : la ligne fautive est barrée au stylo rouge et corrigée.
  function erreur(p, t) {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a + .6, avant = t < tr, k = eo(pr(t, p.a, .4));
    S.texte('TROUVE L’ERREUR', W / 2, 250, { taille: 58, coul: OR, esp: 6 });
    g.save(); g.translate(W / 2, lerp(1500, 860, k)); g.rotate(-.015);
    g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 40; g.fillStyle = '#f3ecdc'; g.fillRect(-500, -560, 1000, 1120); g.shadowColor = 'transparent';
    g.strokeStyle = 'rgba(80,110,160,.25)'; g.lineWidth = 2; for (let y = -300; y < 520; y += 125) { g.beginPath(); g.moveTo(-470, y + 45); g.lineTo(470, y + 45); g.stroke(); }
    g.strokeStyle = 'rgba(200,55,45,.5)'; g.beginPath(); g.moveTo(-380, -520); g.lineTo(-380, 520); g.stroke();
    S.texte('COPIE · ' + (p.matiere || ''), 0, -470, { taille: 32, coul: '#16120d', esp: 5 });
    (p.sujet || '').split('|').forEach((x, i) => S.texte(x, 0, -410 + i * 52, { taille: 44, police: 'Spectral', poids: 600, coul: '#16120d', max: 880 }));
    (p.lignes || []).forEach((x, i) => {
      const y = -250 + i * 125, bad = i === p.faute;
      const ki = eo(pr(t, p.a + .3 + i * .15, .3)); g.globalAlpha = ki;
      S.texte(x, -360, y, { taille: 52, police: 'Spectral', it: true, poids: 500, coul: '#16120d', align: 'left', max: 820 });
      g.globalAlpha = 1;
      if (bad && !avant) {
        const kb = pr(t, tr, .35), w = Math.min(820, S.largeur(x, { taille: 52, police: 'Spectral', it: true, poids: 500 }));
        g.strokeStyle = '#c8372d'; g.lineWidth = 7; g.beginPath(); g.moveTo(-365, y); g.lineTo(-365 + w * kb, y - 4); g.stroke();
        const kc = eo(pr(t, tr + .4, .4)); g.globalAlpha = kc;
        S.texte('→ ' + p.correction, -340, y + 58, { taille: 46, police: 'Spectral', it: true, poids: 600, coul: '#c8372d', align: 'left', max: 780 }); g.globalAlpha = 1;
      }
    });
    g.restore();
    if (avant) chrono(t, tc, tr, W / 2, 1520, 85);
    else O.tampon('ERREUR TROUVÉE', W / 2, 1560, pr(t, tr + .2, .3), -.06, 80, ROUGE);
  }

  return { copie, fiche, vraifaux, quiz3, niveau, ordre, intrus, devine, plusmoins, erreur };
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
  const tics = (tc, tr) => { for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]); };
  if (['niveau', 'ordre', 'intrus', 'plusmoins', 'erreur'].includes(p.type)) {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a + .6; tics(tc, tr);
    if (p.type === 'niveau') L.push([p.a, 'montee', .5], [tr, 'valide', .9]);
    if (p.type === 'ordre') { (p.cartes || []).forEach((c, i) => L.push([p.a + .15 + i * .12, 'pop', .35])); L.push([tr, 'whoosh', .7], [tr + .6, 'valide', .8]); }
    if (p.type === 'intrus') { (p.options || []).forEach((o, i) => L.push([p.a + .1 + i * .12, 'pop', .35])); L.push([tr, 'buzz', .8], [tr + .1, 'tampon', .8]); }
    if (p.type === 'plusmoins') { for (let k = 0; k < 9; k++) L.push([tr + k * .1, 'tic', .4]); L.push([tr + .9, 'valide', .9]); }
    if (p.type === 'erreur') L.push([p.a, 'papier', .5], [tr, 'stylo', .8], [tr + .2, 'tampon', .8]);
  }
  if (p.type === 'devine') { (p.indices || []).forEach(([a]) => L.push([tps(a), 'pop', .5])); L.push([tps(p.rep), 'gong', .8]); }
  if (p.type === 'vraifaux') {
    const tr = tps(p.rep), tc = p.chrono ? tps(p.chrono) : p.a;
    for (let x = tc + .1; x < tr - .05; x += 1) L.push([x, 'tic', .5]);
    L.push([tr, p.v ? 'valide' : (p.doux ? 'gong' : 'buzz'), p.doux ? .5 : .9]);
  }
};
window.TYPES_FORMATS = ['copie', 'fiche', 'vraifaux', 'quiz3', 'niveau', 'ordre', 'intrus', 'devine', 'plusmoins', 'erreur'];
