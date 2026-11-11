var CACHE = 'maths-v6';
var ASSETS = ['./', 'index.html', 'manifest.json', 'icon-192.png', 'icon-512.png', 'assistant.js?v=10', 'carnet-math.woff2'];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; })
        .map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  var url = new URL(e.request.url);
  /* Vidéos des chapitres (serie/) : le son est lu par plages, le service worker le laisse passer */
  if (url.pathname.endsWith('.mp3')) return;
  /* Une vidéo (serie/*.html, montée en iframe : c'est une navigation) se range sous sa propre adresse, jamais sous la page d'accueil */
  var serie = url.pathname.indexOf('/serie/') >= 0 && url.pathname.endsWith('.html');
  var isPage = serie || e.request.mode === 'navigate' ||
    url.pathname.endsWith('/') || url.pathname.endsWith('index.html');
  var cle = serie ? url.origin + url.pathname : e.request;

  if (isPage) {
    /* Réseau d'abord (sans le cache HTTP de 10 min de GitHub Pages), cache en secours (hors ligne) */
    e.respondWith(
      fetch(serie ? e.request.url : e.request, { cache: "no-cache" }).then(function (r) {
        var copie = r.clone();
        caches.open(CACHE).then(function (c) { c.put(cle, copie); });
        return r;
      }).catch(function () {
        return caches.match(cle, { ignoreSearch: serie }).then(function (m) {
          return m || (serie ? Response.error() : caches.match('index.html'));
        });
      })
    );
  } else {
    /* Cache d'abord, réseau en secours */
    e.respondWith(
      caches.match(e.request).then(function (m) {
        return m || fetch(e.request).then(function (r) {
          var copie = r.clone();
          caches.open(CACHE).then(function (c) { c.put(e.request, copie); });
          return r;
        });
      })
    );
  }
});
