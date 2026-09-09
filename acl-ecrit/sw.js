const CACHE = 'aclecrit-v2';
const ASSETS = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png'];

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

  // Page (navigation) : réseau d'abord, cache en secours
  if (e.request.mode === 'navigate' || e.request.destination === 'document') {
    e.respondWith(
      fetch(e.request)
        .then(function (r) {
          var copy = r.clone();
          caches.open(CACHE).then(function (c) { c.put('./index.html', copy); });
          return r;
        })
        .catch(function () {
          return caches.match(e.request).then(function (m) { return m || caches.match('./index.html'); });
        })
    );
    return;
  }

  // Assets (icônes, manifest, polices...) : cache d'abord, réseau en complément
  e.respondWith(
    caches.match(e.request).then(function (m) {
      if (m) return m;
      return fetch(e.request).then(function (r) {
        if (r && (r.ok || r.type === 'opaque')) {
          var copy = r.clone();
          caches.open(CACHE).then(function (c) { c.put(e.request, copy); });
        }
        return r;
      });
    })
  );
});
