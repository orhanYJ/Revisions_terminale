// Planche de captures d'une vidéo de série (relecture image par image).
// Usage (serveur outils/serie-philo/serveur.py lancé, port 8765) :
//   node outils/serie-philo/planche.js <site>/serie/<code>.html <sortie> [pas=8] [debut=4]
// Écrit <sortie>-00.jpg, <sortie>-01.jpg… : feuilles de 4 × 4 images (1280 × 720 réduites), l'instant en jaune.
// Avec des instants en plus après --t (node planche.js page sortie --t 12 40.5 …), une seule feuille de ces instants.
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), __dirname] }));
const { execFileSync } = require('child_process');
const fs = require('fs');
const [page, out] = process.argv.slice(2);
const iT = process.argv.indexOf('--t');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('http://localhost:8765/' + page + '?export=1'); await p.evaluate(() => window.PRET);
  const dur = await p.evaluate(() => window.EPISODE.dur);
  let times;
  if (iT > 0) times = process.argv.slice(iT + 1).map(Number);
  else { const pas = +(process.argv[4] || 8), d0 = +(process.argv[5] || 4); times = []; for (let t = d0; t < dur; t += pas) times.push(t); }
  for (let k = 0; k * 16 < times.length; k++) {
    const ts = times.slice(k * 16, k * 16 + 16), files = [];
    for (const [i, t] of ts.entries()) { await p.evaluate(t => window.RENDU(t), t); const f = `${out}_tmp${i}.png`; await p.screenshot({ path: f }); files.push(f); }
    const args = []; files.forEach(f => args.push('-i', f));
    const n = files.length, cols = Math.min(4, n);
    let fc = files.map((_, i) => `[${i}]scale=640:360,drawtext=text='${ts[i]}s':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black[v${i}]`).join(';');
    const lay = files.map((_, i) => `${(i % cols) * 640}_${Math.floor(i / cols) * 360}`).join('|');
    fc += ';' + files.map((_, i) => `[v${i}]`).join('') + (n > 1 ? `xstack=inputs=${n}:layout=${lay}:fill=black` : 'null');
    const nom = iT > 0 ? out + '.jpg' : `${out}-${String(k).padStart(2, '0')}.jpg`;
    execFileSync('ffmpeg', ['-v', 'error', '-y', ...args, '-filter_complex', fc, nom]);
    files.forEach(f => fs.unlinkSync(f)); console.log(nom);
  }
  await b.close();
})();
