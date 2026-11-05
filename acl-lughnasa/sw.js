const CACHE = 'acl-lughnasa-v6';
const ASSETS = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(
    ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  // vidéos résumé-analyse : les MP3 sont lus par plages (réponses 206, impossibles à mettre en cache) ; on les laisse passer
  if (url.pathname.endsWith('.mp3') || e.request.headers.has('range')) return;
  // une page serie/*.html est chargée en iframe (navigation) : elle garde sa propre adresse, jamais celle de la page d'accueil
  const page = e.request.mode === 'navigate' && !url.pathname.includes('/serie/');
  e.respondWith(
    fetch(e.request, { cache: 'no-cache' }).then(r => {
      if (r.ok && r.status === 200) {
        const copy = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy));
      }
      return r;
    }).catch(() => caches.match(e.request).then(r => r || (page ? caches.match('./index.html') : undefined)))
  );
});
