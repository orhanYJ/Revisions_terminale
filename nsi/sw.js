var CACHE = 'nsi-v3';
var ASSETS = ['./', 'index.html', 'manifest.json', 'icon-192.png', 'icon-512.png', 'assistant.js?v=9'];

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
  var isPage = e.request.mode === 'navigate' ||
    url.pathname.endsWith('/') || url.pathname.endsWith('index.html');

  if (isPage) {
    /* Réseau d'abord (sans la copie de 10 min du navigateur), cache en secours (hors ligne) */
    e.respondWith(
      fetch(e.request, { cache: 'no-cache' }).then(function (r) {
        var copie = r.clone();
        caches.open(CACHE).then(function (c) { c.put(e.request, copie); });
        return r;
      }).catch(function () {
        return caches.match(e.request).then(function (m) {
          return m || caches.match('./');
        });
      })
    );
  } else {
    /* Cache d'abord, réseau en secours */
    e.respondWith(
      caches.match(e.request).then(function (m) {
        return m || fetch(e.request).then(function (r) {
          if (r.ok && url.origin === location.origin) {
            var copie = r.clone();
            caches.open(CACHE).then(function (c) { c.put(e.request, copie); });
          }
          return r;
        });
      })
    );
  }
});
