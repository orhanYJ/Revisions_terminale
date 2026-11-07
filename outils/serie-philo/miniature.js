// Capture PNG (1280 × 720) des miniatures écrites par kit_youtube.py.
// Usage : node outils/serie-philo/miniature.js DOSSIER ch1 [ch2 ...]   (serveur local sur le port 8765)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [dossier, ...codes] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  for (const c of codes) {
    await p.goto('file://' + path.resolve(dossier, c + '-miniature.html'));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: path.resolve(dossier, c + '-miniature.png') });
    console.log('miniature :', c);
  }
  await b.close();
})();
