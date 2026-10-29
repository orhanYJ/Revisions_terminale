// Fabrique le MP4 d'un épisode (1920 × 1080, 25 images/s) à partir de la page du lecteur en mode export.
// Usage (depuis la racine du dépôt, un serveur local servant le dépôt sur le port 8765) :
//   python3 -m http.server 8765 &
//   node outils/serie-philo/video.js liberte-1 SORTIE.mp4 [--sous]
// La page rend chaque image en fonction du temps (window.RENDU) ; trois navigateurs se partagent la durée,
// puis ffmpeg assemble les morceaux et y pose la piste voix + musique. Le MP4 n'est pas versionné (trop lourd).
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const code = process.argv[2], sortie = path.resolve(process.argv[3] || code + '.mp4');
const sous = process.argv.includes('--sous');
const FPS = 25, W = 1920, H = 1080, PARTS = 3;
const URL = `http://localhost:8765/philo/serie/${code}.html?export=1${sous ? '&sous=1' : ''}`;
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'serie-'));

async function morceau(i, debut, fin) {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto(URL);
  await p.evaluate(() => window.PRET);
  const f = path.join(tmp, `p${i}.mp4`);
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p', '-r', String(FPS), f], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let k = debut; k < fin; k++) {
    await p.evaluate(t => window.RENDU(t), k / FPS);
    const img = await p.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(img)) await new Promise(r => ff.stdin.once('drain', r));
    if (i === 0 && k % (FPS * 30) === 0) console.log(`  ${Math.round(100 * (k - debut) / (fin - debut))} %`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await b.close();
  return f;
}

(async () => {
  const data = fs.readFileSync(path.join(__dirname, '../../philo/serie', code + '.data.js'), 'utf8');
  const ep = JSON.parse(data.slice(data.indexOf('=') + 1).trim().replace(/;$/, ''));
  const n = Math.ceil(ep.dur * FPS), pas = Math.ceil(n / PARTS);
  console.log(`${code} : ${n} images…`);
  const parts = await Promise.all([...Array(PARTS)].map((_, i) => morceau(i, i * pas, Math.min(n, (i + 1) * pas))));
  const liste = path.join(tmp, 'liste.txt');
  fs.writeFileSync(liste, parts.map(f => `file '${f}'`).join('\n'));
  const audio = path.join(__dirname, '../../philo/serie', ep.audio.mix);
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', liste, '-i', audio,
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', sortie]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('écrit :', sortie, Math.round(fs.statSync(sortie).size / 1e6), 'Mo');
})();
