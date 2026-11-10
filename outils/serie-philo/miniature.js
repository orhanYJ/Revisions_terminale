// Capture PNG (1280 × 720) des miniatures écrites par kit_youtube.py.
// Usage : node outils/serie-philo/miniature.js DOSSIER ch1 [ch2 ...]   (serveur local sur le port 8765)
// La page est servie sous l'adresse du serveur local (et non en file://), sinon le navigateur refuse ses polices.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [dossier, ...codes] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.route('http://localhost:8765/__miniature/*', r => {
    const c = decodeURIComponent(r.request().url().split('/').pop());
    r.fulfill({ contentType: 'text/html; charset=utf-8', body: fs.readFileSync(path.resolve(dossier, c + '-miniature.html')) });
  });
  for (const c of codes) {
    await p.goto('http://localhost:8765/__miniature/' + encodeURIComponent(c));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    const polices = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family).filter((v, i, a) => a.indexOf(v) === i).join(', '));
    await p.screenshot({ path: path.resolve(dossier, c + '-miniature.png') });
    console.log('miniature :', c, '·', polices || 'aucune police chargée');
  }
  await b.close();
})();
