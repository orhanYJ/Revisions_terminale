// Superpositions visibles entre visuels d une vidéo de série, et avec les sous-titres (11/11/2026 : « des chevauchements partout »).
// Usage (serveur outils/serie-philo/serveur.py lancé, port 8765) : node outils/serie-philo/superpositions.js <site>/serie/<code>.html [pas=0.5]
// Affiche, par instant, les paires de visuels dont les blocs de texte ou d images se recouvrent (aires en pixels), et les blocs qui se
// recouvrent à l intérieur d un même visuel. Les photos de fond (tableau fond ou sombre) et le générique sont ignorés. Le rendu est
// celui de Chromium sous Linux : sous Windows, une police aux hauteurs mal déclarées peut décaler les lignes (voir maths/serie/fonts.css).
const { chromium } = require(require.resolve('playwright', {paths:[process.cwd(), __dirname]}));
const [page, pas] = [process.argv[2], +(process.argv[3] || 0.5)];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('http://localhost:8765/' + page + '?export=1'); await p.evaluate(() => window.PRET);
  const dur = await p.evaluate(() => window.EPISODE.dur);
  const D = dur || await p.evaluate(() => { const s = document.querySelector('script[src*=data]'); return 0; });
  const res = [];
  for (let t = 0; t < (dur || 1800); t += pas) {
    const r = await p.evaluate(t => {
      window.RENDU(t);
      const boites = [], pb = [];
      const tous = [...document.querySelectorAll('.scene .v')];
      const vs = tous.map((e, i) => [e, EPISODE.vis[i]]).filter(([e, v]) => e.style.display !== 'none' && +getComputedStyle(e).opacity > 0.25 && !(v.type === 'tableau' && (v.fond || v.sombre)) && v.type !== 'generique');
      const feuilles = el => { const out = []; const w = n => { const kids = [...n.children]; if (!kids.length || /^(svg|canvas|math|img)$/i.test(n.tagName)) { if (n.textContent.trim() || /^(svg|canvas|img)$/i.test(n.tagName)) out.push(n); return; } kids.forEach(w); }; w(el); return out; };
      vs.forEach(([e, v], i) => {
        let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9, rects = [];
        feuilles(e).forEach(f => { const q = f.getBoundingClientRect(); if (q.width < 2 || q.height < 2) return; const cs = getComputedStyle(f); if (cs.visibility === 'hidden' || +cs.opacity < 0.2) return; rects.push([q.left, q.top, q.right, q.bottom]); });
        boites.push({ i, txt: v.type + ':' + (v.id || '') + ' ' + e.textContent.trim().slice(0, 30), rects });
      });
      // chevauchements à l'intérieur d'un même visuel : blocs de texte qui se recouvrent
      vs.forEach(([e, v]) => {
        const blocs = [...e.querySelectorAll('*')].filter(f => f.children.length === 0 || /^(math)$/i.test(f.tagName)).filter(f => !f.closest('math') || f.tagName.toLowerCase() === 'math').filter(f => f.textContent.trim().length > 1);
        const R = blocs.map(f => { const q = f.getBoundingClientRect(); const cs = getComputedStyle(f); return (q.width < 2 || cs.visibility === 'hidden' || +cs.opacity < .2) ? null : [q.left, q.top, q.right, q.bottom, f]; }).filter(Boolean);
        for (let a = 0; a < R.length; a++) for (let c = a + 1; c < R.length; c++) {
          if (R[a][4].contains(R[c][4]) || R[c][4].contains(R[a][4])) continue;
          const s = Math.max(0, Math.min(R[a][2], R[c][2]) - Math.max(R[a][0], R[c][0])) * Math.max(0, Math.min(R[a][3], R[c][3]) - Math.max(R[a][1], R[c][1]));
          const pt = Math.min((R[a][2]-R[a][0])*(R[a][3]-R[a][1]), (R[c][2]-R[c][0])*(R[c][3]-R[c][1]));
          if (s > 150 && s > .25 * pt) pb.push(['interne:' + v.type + ':' + (v.id||''), R[a][4].textContent.trim().slice(0, 30), R[c][4].textContent.trim().slice(0, 30), Math.round(s)]);
        }
      });
      const st = document.querySelector('.scene .st'); const sr = st && st.style.display !== 'none' ? st.getBoundingClientRect() : null;
      const inter = (a, b) => Math.max(0, Math.min(a[2], b[2]) - Math.max(a[0], b[0])) * Math.max(0, Math.min(a[3], b[3]) - Math.max(a[1], b[1]));
      for (let a = 0; a < boites.length; a++) for (let c = a + 1; c < boites.length; c++) {
        let s = 0; boites[a].rects.forEach(r1 => boites[c].rects.forEach(r2 => s += inter(r1, r2)));
        if (s > 400) pb.push(['vis', boites[a].txt, boites[c].txt, Math.round(s)]);
      }
      if (sr && sr.width > 5) { const S = [sr.left, sr.top, sr.right, sr.bottom]; boites.forEach(bx => { let s = 0; bx.rects.forEach(r => s += inter(r, S)); if (s > 600) pb.push(['sous-titre', bx.txt, '', Math.round(s)]); }); }
      return pb;
    }, t);
    if (r.length) res.push([t, r]);
  }
  for (const [t, r] of res) console.log(t.toFixed(1), JSON.stringify(r));
  await b.close();
})();
