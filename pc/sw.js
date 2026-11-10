const CACHE = 'pc-v45';
/* Les animations (anim/*.html) sont des pages à part : elles ont leur propre
   entrée de cache, pour ne jamais écraser la page d'accueil. */
const ANIMS = ['photon', 'photoelec', 'cellule', 'acidebase', 'beerlambert', 'conductivite', 'titrage', 'lunette'];
const ASSETS = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png',
  './anim/moteur.css?v=4', './anim/moteur.js?v=4', './elements.css?v=2', './elements.js?v=2', './lumiere.css?v=1',
  './polices/plex-sans-400.woff2', './polices/plex-sans-400i.woff2', './polices/plex-sans-600.woff2', './polices/plex-sans-700.woff2',
  './polices/plex-cond-500.woff2', './polices/plex-cond-700.woff2', './polices/plex-mono-400.woff2', './polices/plex-mono-600.woff2',
  './polices/instrument-serif.woff2', './polices/instrument-serif-i.woff2', './polices/space-grotesk-400.woff2', './polices/space-grotesk-500.woff2',
  './polices/space-grotesk-700.woff2', './polices/jb-mono-400.woff2', './polices/jb-mono-600.woff2'].concat(ANIMS.map(function (a) { return './anim/' + a + '.html'; }));

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  var url = new URL(e.request.url);
  // Vidéos de cours (serie/) : le son est lu par plages, le service worker le laisse passer
  if (url.pathname.endsWith('.mp3')) return;

  // Pages : reseau d'abord, cache en secours (hors ligne).
  // La page d'accueil sous la cle './index.html', une animation ou une vidéo (serie/*.html) sous sa propre adresse (sans parametres).
  if (e.request.mode === 'navigate' || url.pathname.endsWith('.html')) {
    var accueil = url.pathname.endsWith('/') || url.pathname.endsWith('/index.html');
    var cle = accueil ? './index.html' : url.origin + url.pathname;
    // « no-cache » : toujours revalider auprès du serveur, sans réutiliser la copie
    // que le navigateur garde 10 minutes (GitHub Pages envoie max-age=600)
    e.respondWith(
      fetch(e.request.url, { cache: 'no-cache', credentials: 'same-origin' }).then(function (r) {
        var copie = r.clone();
        caches.open(CACHE).then(function (c) { c.put(cle, copie); });
        return r;
      }).catch(function () {
        return caches.match(cle, { ignoreSearch: true });
      })
    );
    return;
  }

  // Assets : cache d'abord, reseau en secours (puis mise en cache)
  e.respondWith(
    caches.match(e.request).then(function (hit) {
      return hit || fetch(e.request).then(function (r) {
        var copie = r.clone();
        caches.open(CACHE).then(function (c) { c.put(e.request, copie); });
        return r;
      });
    })
  );
});
