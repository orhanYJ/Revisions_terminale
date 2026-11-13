// Plans propres au short « totalitarismes60 » (« Les totalitarismes en 60 secondes »), style du modèle A
// (archives : noir, crème, or, rouge). O = outils du modèle (carte, multi, tampon, barreRouge, petitTitre, fondImg, C).
// Ton sobre : aucun son de jeu, aucune secousse sur les plans qui parlent des victimes (holodomor, purge, camps).
window.SANS_ST_A = ['chrono', 'trio', 'cercles', 'duel', 'ideo', 'vote', 'ville', 'jeunesse', 'camps', 'holodomor', 'purge'];
window.PROPRES_A = ['chrono', 'trio', 'cercles', 'duel', 'ideo', 'vote', 'ville', 'jeunesse', 'camps', 'holodomor', 'purge'];
window.TYPES_A = O => {
  const { g, W, H, cl, lerp, pr, eo, back, rnd } = S;
  const { NOIR, CREME, OR, ROUGE, GRIS } = O.C;
  const PAPIER = '#f3ecdc', BRUN = '#3a2f25';
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  const deux = (txt, y, taille = 110) => { const L = txt.split('|'); L.forEach((s, i) => O.multi([[s, i ? OR : CREME]], y + (i - (L.length - 1) / 2) * taille * 1.08, i ? taille : taille * .85)); };
  const titrePop = (txt, y, t, a, taille = 100) => { const k = back(pr(t, a, .3)); g.save(); g.translate(W / 2, y); g.scale(lerp(1.4, 1, k), lerp(1.4, 1, k)); g.translate(-W / 2, -y); deux(txt, y, taille); g.restore(); };
  const milliers = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');

  // compte à rebours de 60 s qui tourne
  function chrono(p, t) {
    const u = cl((t - p.a) / 60), reste = Math.max(0, 60 - Math.floor(t - p.a));
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

  // trois régimes : trois cartes (photo, pays, dates) qui arrivent à leur repère ; p.mach : « une même machine »
  function trio(p, t, l) {
    const C3 = [
      ['mussolini', 'ITALIE', '1922-1943', 1.15, .5, .25],
      ['potsdam', 'ALLEMAGNE', '1933-1945', 2.1, .37, .22],
      ['stalin', 'URSS', '1924-1953', 1.7, .5, .15],
    ];
    C3.forEach(([img, pays, dates, z, fx, fy], i) => {
      const ta = tps(p.rev[i]); if (t < ta) return;
      const k = eo(pr(t, ta, .3)), x = 190 + i * 350;
      O.carte(img, x, lerp(560, 780, k), 290, 400, (i - 1) * .03, z + l * .02, fx, fy, { lum: .9 });
      S.texte(pays, x, 1060, { taille: 54, coul: OR, max: 320 });
      S.texte(dates, x, 1125, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: CREME });
    });
    if (p.mach && t >= tps(p.mach)) {
      const kb = back(pr(t, tps(p.mach), .3));
      g.save(); g.translate(W / 2, 1330); g.scale(lerp(1.5, 1, kb), lerp(1.5, 1, kb)); g.translate(-W / 2, -1330);
      deux('TROIS RÉGIMES|UNE MÊME MACHINE', 1330, 110); g.restore();
    } else O.petitTitre('— TROIS RÉGIMES —', 1330);
  }

  // le contrôle total : l'État au centre, puis toute la société autour (p.ext = repère de l'anneau)
  function cercles(p, t) {
    const cx = W / 2, cy = 860, k0 = back(pr(t, p.a, .3));
    const te = tps(p.ext), ke = t >= te ? eo(pr(t, te, .6)) : 0;
    if (ke > 0) {
      g.save(); g.strokeStyle = OR; g.lineWidth = 8; g.globalAlpha = ke; g.beginPath(); g.arc(cx, cy, lerp(170, 410, ke), 0, 7); g.stroke(); g.restore();
      const MOTS = ['TRAVAIL', 'ÉCOLE', 'FAMILLE', 'LOISIRS', 'RELIGION', 'PENSÉE'];
      MOTS.forEach((m, i) => {
        const kk = eo(pr(t, te + .1 + i * .1, .3)); if (kk <= 0) return;
        const a = -Math.PI / 2 + i / MOTS.length * 6.283, r = lerp(200, 410, kk);
        g.save(); g.globalAlpha = kk; g.strokeStyle = 'rgba(217,180,90,.5)'; g.lineWidth = 4;
        g.beginPath(); g.moveTo(cx + Math.cos(a) * 160, cy + Math.sin(a) * 160); g.lineTo(cx + Math.cos(a) * (r - 70), cy + Math.sin(a) * (r - 70)); g.stroke();
        g.fillStyle = '#1b1712'; g.beginPath(); g.roundRect(cx + Math.cos(a) * r - 130, cy + Math.sin(a) * r - 38, 260, 76, 18); g.fill();
        g.strokeStyle = CREME; g.lineWidth = 3; g.stroke();
        S.texte(m, cx + Math.cos(a) * r, cy + Math.sin(a) * r + 2, { taille: 42, coul: CREME, max: 230 }); g.restore();
      });
    }
    g.save(); g.translate(cx, cy); g.scale(k0, k0);
    g.fillStyle = ROUGE; g.beginPath(); g.arc(0, 0, 150, 0, 7); g.fill();
    S.texte('L’ÉTAT', 0, 4, { taille: 76, coul: CREME, contour: NOIR, contourL: 6 }); g.restore();
    deux(ke > 0 ? 'PAS SEULEMENT L’ÉTAT|TOUTE LA SOCIÉTÉ' : 'TOUT|CONTRÔLER', 1460, 110);
  }

  // dictature / totalitarisme : deux cartes, la seconde à p.b2 ; p.ideo : « selon une idéologie »
  function duel(p, t) {
    const carteTxt = (y, k, haut, phrase, coul) => {
      if (k <= 0) return;
      g.save(); g.translate(lerp(-700, 0, eo(k)), 0);
      g.fillStyle = PAPIER; g.shadowColor = 'rgba(0,0,0,.6)'; g.shadowBlur = 30; g.fillRect(90, y - 170, 900, 340); g.shadowColor = 'transparent';
      g.fillStyle = coul; g.fillRect(90, y - 170, 22, 340);
      S.texte(haut, W / 2, y - 80, { taille: 58, coul, esp: 4 });
      S.texte(phrase, W / 2, y + 50, { taille: 92, police: 'Spectral', it: true, poids: 600, coul: NOIR, max: 820 });
      g.restore();
    };
    carteTxt(640, pr(t, p.a, .35), 'UNE DICTATURE', '« Tais-toi. »', GRIS);
    const t2 = tps(p.b2); if (t >= t2) carteTxt(1080, pr(t, t2, .35), 'LE TOTALITARISME', '« Change. »', ROUGE);
    if (p.ideo && t >= tps(p.ideo)) { const k = eo(pr(t, tps(p.ideo), .3)); g.save(); g.globalAlpha = k;
      S.texte('selon une idéologie', W / 2, 1390, { taille: 72, police: 'Spectral', it: true, poids: 500, coul: OR, contour: NOIR, contourL: 8 }); g.restore(); }
  }

  // trois buts suprêmes : items = [[repère, but, chef], …]
  function ideo(p, t) {
    O.petitTitre('— LE BUT SUPRÊME —', 420);
    p.items.forEach(([a, but, chef], i) => {
      const ta = tps(a); if (t < ta) return;
      const k = back(pr(t, ta, .3)), y = 640 + i * 300, actif = !p.items[i + 1] || t < tps(p.items[i + 1][0]);
      g.save(); g.globalAlpha = actif ? 1 : .6;
      g.fillStyle = actif ? 'rgba(217,180,90,.14)' : 'rgba(239,230,210,.05)'; g.fillRect(70, y - 115, 940, 230);
      g.translate(W / 2, y - 20); g.scale(k, k);
      S.texte(but, 0, 0, { taille: 120, coul: actif ? OR : CREME, contour: NOIR, contourL: 10, max: 900 });
      g.restore();
      S.texte('pour ' + chef, W / 2, y + 75, { taille: 52, police: 'Spectral', it: true, poids: 400, coul: CREME });
    });
  }

  // vote nazi (graphiques du cours) : quatre barres, la ligne des 50 % jamais atteinte ; p.jamais : verdict
  function vote(p, t) {
    const D = [['mai 1928', 2.6], ['sept. 1930', 18.3], ['juil. 1932', 37.4], ['nov. 1932', 33.1]];
    const y0 = 1320, h50 = 700, x0 = 150;
    O.petitTitre('— LE VOTE NAZI —', 420);
    g.strokeStyle = CREME; g.lineWidth = 5; g.beginPath(); g.moveTo(x0 - 20, y0); g.lineTo(1000, y0); g.stroke();
    // ligne de la majorité
    g.save(); g.setLineDash([24, 16]); g.strokeStyle = ROUGE; g.lineWidth = 6; g.beginPath(); g.moveTo(x0 - 20, y0 - h50); g.lineTo(1000, y0 - h50); g.stroke(); g.restore();
    S.texte('MAJORITÉ : 50 %', 1000, y0 - h50 - 40, { taille: 38, coul: ROUGE, align: 'right' });
    D.forEach(([lab, v], i) => {
      const k = eo(pr(t, p.a + .15 + i * .18, .5)), x = x0 + 40 + i * 210, h = v / 50 * h50 * k;
      g.fillStyle = i === 2 ? OR : 'rgba(217,180,90,.55)'; g.fillRect(x, y0 - h, 150, h);
      if (k > .3) S.texte(String(v).replace('.', ',') + ' %', x + 75, y0 - h - 36, { taille: 44, coul: CREME });
      S.texte(lab, x + 75, y0 + 44, { taille: 34, police: 'Spectral', it: true, poids: 400, coul: CREME });
    });
    if (p.jamais && t >= tps(p.jamais)) { const k = back(pr(t, tps(p.jamais), .3)); g.save(); g.translate(W / 2, 1500); g.scale(k, k);
      S.texte('JAMAIS LA MAJORITÉ', 0, 0, { taille: 104, coul: ROUGE, contour: NOIR, contourL: 10, max: 960 }); g.restore(); }
  }

  // panneau d'entrée de ville : 1925, puis le nom à p.nom
  function ville(p, t) {
    const k = back(pr(t, p.a, .35));
    g.save(); g.translate(W / 2, 860); g.scale(k, k);
    g.fillStyle = '#7a7368'; g.fillRect(-14, 150, 28, 520);
    g.fillStyle = CREME; g.strokeStyle = NOIR; g.lineWidth = 10; g.beginPath(); g.roundRect(-430, -170, 860, 340, 20); g.fill(); g.stroke();
    g.strokeStyle = ROUGE; g.lineWidth = 8; g.beginPath(); g.roundRect(-405, -145, 810, 290, 14); g.stroke();
    const tn = tps(p.nom);
    if (t >= tn) { const kn = eo(pr(t, tn, .35)); g.save(); g.globalAlpha = kn; S.texte('STALINGRAD', 0, -10, { taille: 130, coul: NOIR, max: 760 }); g.restore(); }
    else S.texte('· · ·', 0, -10, { taille: 130, coul: GRIS });
    S.texte('URSS', 0, 100, { taille: 44, coul: GRIS, esp: 10 });
    g.restore();
    S.texte('1925', W / 2, 1420, { taille: 150, police: 'Spectral', poids: 600, coul: OR, contour: NOIR, contourL: 10 });
    S.texte('une ville prend le nom du chef', W / 2, 1545, { taille: 56, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
  }

  // Jeunesses hitlériennes : une règle des âges, de 10 à 18 ans, qui se remplit
  function jeunesse(p, t) {
    O.petitTitre('— JEUNESSES HITLÉRIENNES —', 470);
    const x = a => lerp(110, 970, (a - 6) / 16), y = 980, k = eo(pr(t, p.a + .2, 1.2));
    g.fillStyle = 'rgba(239,230,210,.1)'; g.fillRect(x(6), y - 40, x(22) - x(6), 80);
    g.fillStyle = ROUGE; g.fillRect(x(10), y - 40, (x(18) - x(10)) * k, 80);
    for (let a = 6; a <= 22; a++) { g.strokeStyle = CREME; g.lineWidth = a % 2 ? 2 : 4; g.beginPath(); g.moveTo(x(a), y + 44); g.lineTo(x(a), y + (a % 2 ? 62 : 78)); g.stroke();
      if (!(a % 2)) S.texte(String(a), x(a), y + 116, { taille: 36, coul: a >= 10 && a <= 18 ? CREME : GRIS }); }
    // silhouettes qui grandissent de 10 à 18 ans
    for (let i = 0; i < 5; i++) {
      const a = 10 + i * 2; if (a > 10 + 8 * k + .01) continue;
      const hh = lerp(150, 260, i / 4), cx = x(a);
      g.fillStyle = 'rgba(239,230,210,.85)'; g.beginPath(); g.arc(cx, y - 70 - hh, hh * .13, 0, 7); g.fill();
      g.beginPath(); g.roundRect(cx - hh * .14, y - 60 - hh * .85, hh * .28, hh * .8, 10); g.fill();
    }
    S.texte('OBLIGATOIRES', W / 2, 1330, { taille: 120, coul: OR, contour: NOIR, contourL: 10 });
    S.texte('de 10 à 18 ans', W / 2, 1460, { taille: 70, police: 'Spectral', it: true, poids: 500, coul: CREME });
  }

  // police politique et camps : barbelés, puis les noms (items = [[repère, nom, sous], …])
  function camps(p, t) {
    const k = eo(pr(t, p.a, .6));
    g.save(); g.strokeStyle = 'rgba(239,230,210,.55)'; g.lineWidth = 4;
    [560, 640, 720].forEach((y, j) => { g.beginPath(); g.moveTo(0, y); g.lineTo(W * k, y + (j - 1) * 6); g.stroke();
      for (let x = 40 + j * 30; x < W * k; x += 110) { g.beginPath(); g.moveTo(x - 16, y - 16); g.lineTo(x + 16, y + 16); g.moveTo(x + 16, y - 16); g.lineTo(x - 16, y + 16); g.stroke(); } });
    g.restore();
    S.texte('POLICE POLITIQUE', W / 2, 860, { taille: 84, coul: CREME, contour: NOIR, contourL: 8, max: 960 });
    S.texte('et camps', W / 2, 960, { taille: 64, police: 'Spectral', it: true, poids: 400, coul: CREME });
    (p.items || []).forEach(([a, nom, sous], i) => {
      const ta = tps(a); if (t < ta) return;
      const kk = eo(pr(t, ta, .35)), y = 1180 + i * 230;
      g.save(); g.globalAlpha = kk;
      S.texte(nom, W / 2, y, { taille: 110, coul: OR, contour: NOIR, contourL: 10, max: 960 });
      S.texte(sous, W / 2, y + 85, { taille: 48, police: 'Spectral', it: true, poids: 400, coul: CREME, max: 960 });
      g.restore();
    });
  }

  // l'Holodomor : plan sombre et lent, un champ d'épis vides ; p.mil : « des millions »
  function holodomor(p, t) {
    const lt = t - p.a;
    g.save(); g.strokeStyle = 'rgba(217,180,90,.28)'; g.lineWidth = 3;
    for (let i = 0; i < 26; i++) { const x = 40 + i * 40 + rnd(i) * 18, hh = 140 + rnd(i + 9) * 120, sw = Math.sin(lt * .8 + i) * 6;
      g.beginPath(); g.moveTo(x, 1250); g.quadraticCurveTo(x + sw, 1250 - hh / 2, x + sw * 2, 1250 - hh); g.stroke(); }
    g.restore();
    const k = eo(pr(t, p.a, .8));
    g.save(); g.globalAlpha = k;
    S.texte('HOLODOMOR', W / 2, 640, { taille: 130, police: 'Spectral', poids: 600, coul: CREME, max: 960 });
    S.texte('UKRAINE · 1932-1933', W / 2, 760, { taille: 46, coul: OR, esp: 8 });
    S.texte('une famine provoquée', W / 2, 870, { taille: 62, police: 'Spectral', it: true, poids: 400, coul: CREME });
    g.restore();
    if (p.mil && t >= tps(p.mil)) { const km = eo(pr(t, tps(p.mil), .7)); g.save(); g.globalAlpha = km;
      S.texte('DES MILLIONS DE MORTS', W / 2, 1420, { taille: 88, coul: CREME, max: 960 }); g.restore(); }
  }

  // la Grande Purge : 68 points (un pour 10 000 exécutions) qui s'éteignent, compteur sobre
  function purge(p, t) {
    O.petitTitre('— LA GRANDE PURGE · 1937-1938 —', 420, CREME);
    const tn = p.n ? tps(p.n) : p.a + .4, u = eo(pr(t, tn, 1.2)), nb = Math.round(68 * u);
    for (let i = 0; i < 68; i++) {
      const x = 160 + (i % 10) * 84, y = 540 + Math.floor(i / 10) * 84;
      g.fillStyle = i < nb ? ROUGE : 'rgba(239,230,210,.18)'; g.beginPath(); g.arc(x, y, 22, 0, 7); g.fill();
    }
    S.texte(milliers(Math.round(lerp(0, 680000, u) / 1000) * 1000), W / 2, 1260, { taille: 170, police: 'Spectral', poids: 600, coul: CREME, contour: NOIR, contourL: 10 });
    S.texte('EXÉCUTIONS', W / 2, 1400, { taille: 74, coul: ROUGE, esp: 8 });
    S.texte('un point = 10 000 vies', W / 2, 1490, { taille: 40, police: 'Spectral', it: true, poids: 400, coul: GRIS });
  }

  return { chrono, trio, cercles, duel, ideo, vote, ville, jeunesse, camps, holodomor, purge };
};

// sons propres à ces plans (discrets ; rien de ludique sur les plans des victimes)
window.SONS_A = (p, L) => {
  const tps = a => Array.isArray(a) ? S.T(...a) - .04 : a;
  if (p.type === 'chrono') L.push([p.a, 'clic', .7], [p.a + .3, 'tic', .5], [p.a + .6, 'tic', .5]);
  if (p.type === 'trio') p.rev.forEach(a => L.push([tps(a), 'papier', .4]));
  if (p.type === 'cercles') L.push([p.a, 'pop', .4], [tps(p.ext), 'whoosh', .4]);
  if (p.type === 'duel') L.push([p.a, 'papier', .4], [tps(p.b2), 'papier', .4]);
  if (p.type === 'ideo') p.items.forEach(([a]) => L.push([tps(a), 'frappe', .45]));
  if (p.type === 'vote') L.push([p.a + .15, 'montee', .35]);
  if (p.type === 'ville') L.push([p.a, 'frotte', .4], [tps(p.nom), 'tampon', .5]);
  if (p.type === 'jeunesse') L.push([p.a + .2, 'montee', .3]);
  if (p.type === 'camps') L.push([p.a, 'souffle', .3]);
  if (p.type === 'holodomor') L.push([p.a, 'souffle', .35]);
  if (p.type === 'purge') L.push([p.n ? tps(p.n) : p.a + .4, 'coeur', .5]);
};
