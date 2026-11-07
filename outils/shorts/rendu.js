// Fabrique un short : images (Playwright) → MP4 vertical 1080 × 1920, 30 images/s, avec la bande son de mix.py.
// Usage (depuis la racine du dépôt, serveur local : python3 -m http.server 8765) :
//   node outils/shorts/rendu.js libet a [--muet] [--planche]
//   --planche : une image par seconde en planche contact (contrôle), sans vidéo.
//   --son : refait seulement la bande son et la repose sur le MP4 existant.
// Écrit outils/shorts/sortie/<code>-<m>.mp4 (non versionné).
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');

const [code, m] = process.argv.slice(2);
const muet = process.argv.includes('--muet'), planche = process.argv.includes('--planche');
const FPS = 30, W = 1080, H = 1920, PARTS = 3;
const ICI = __dirname, SORTIE = path.join(ICI, 'sortie');
const URL = `http://localhost:8765/outils/shorts/short.html?c=${code}&m=${m}&export=1${muet ? '&muet=1' : ''}`;

async function page(b) {
  const p = await b.newPage({ viewport: { width: W, height: H } });
  p.on('console', x => { if (x.type() === 'error') console.log('console :', x.text()); });
  p.on('pageerror', e => console.log('erreur :', e.message));
  await p.goto(URL);
  await p.waitForFunction(() => window.PRET, null, { timeout: 30000 });
  await p.evaluate(() => window.PRET);
  return p;
}
const image = async (p, t) => { await p.evaluate(t => window.RENDU(t), t); return p.screenshot({ type: 'jpeg', quality: 93, clip: { x: 0, y: 0, width: W, height: H } }); };

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'short-'));
  if (planche) {
    const b = await chromium.launch(), p = await page(b);
    const dur = await p.evaluate(() => window.DUR), n = Math.ceil(dur);
    for (let k = 0; k < n; k++) fs.writeFileSync(path.join(tmp, `i${String(k).padStart(3, '0')}.jpg`), await image(p, k + .5));
    await b.close();
    const out = path.join(SORTIE, `${code}-${m}-planche.jpg`);
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-pattern_type', 'glob', '-i', path.join(tmp, 'i*.jpg'), '-vf', 'scale=270:480,tile=10x' + Math.ceil(n / 10), '-frames:v', '1', out]);
    console.log('planche :', out);
    return;
  }
  // sons d'abord (bande son), puis les images
  { const b = await chromium.launch(), p = await page(b);
    fs.writeFileSync(path.join(SORTIE, `${code}-${m}.sons.json`), JSON.stringify(await p.evaluate(() => window.SONS)));
    await b.close(); }
  if (!muet) execFileSync('python3', [path.join(ICI, 'mix.py'), code, m], { stdio: 'inherit' });
  if (process.argv.includes('--son')) {   // bande son seule : on la repose sur la vidéo déjà calculée
    const mp4 = path.join(SORTIE, `${code}-${m}.mp4`), tmp2 = mp4.replace('.mp4', '.tmp.mp4');
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', mp4, '-i', path.join(SORTIE, `${code}-${m}.mix.wav`), '-map', '0:v', '-map', '1:a',
      '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', tmp2]);
    fs.renameSync(tmp2, mp4); console.log('son reposé :', mp4); return;
  }
  const data = fs.readFileSync(path.join(SORTIE, `${code}${muet ? '.muet' : ''}.data.js`), 'utf8');
  const dur = JSON.parse(data.slice(data.indexOf('=') + 1).trim().replace(/;\s*$/, '')).dur;
  const n = Math.ceil(dur * FPS), pas = Math.ceil(n / PARTS);
  console.log(`${code}-${m} : ${n} images…`);
  const parts = await Promise.all([...Array(PARTS)].map(async (_, i) => {
    const b = await chromium.launch(), p = await page(b), f = path.join(tmp, `p${i}.mp4`);
    const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-r', String(FPS), f], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let k = i * pas; k < Math.min(n, (i + 1) * pas); k++) {
      const img = await image(p, k / FPS);
      if (!ff.stdin.write(img)) await new Promise(r => ff.stdin.once('drain', r));
      if (i === 0 && k % (FPS * 5) === 0) console.log(`  ${Math.round(100 * k / pas)} %`);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); return f;
  }));
  const liste = path.join(tmp, 'liste.txt');
  fs.writeFileSync(liste, parts.map(f => `file '${f}'`).join('\n'));
  const out = path.join(SORTIE, `${code}-${m}${muet ? '-muet' : ''}.mp4`);
  const audio = muet ? ['-f', 'lavfi', '-i', `anullsrc=r=48000:cl=mono`] : ['-i', path.join(SORTIE, `${code}-${m}.mix.wav`)];
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', liste, ...audio,
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('écrit :', out, (fs.statSync(out).size / 1e6).toFixed(1), 'Mo');
})();
