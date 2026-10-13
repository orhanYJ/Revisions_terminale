const CACHE = 'pc-v29';
/* Les animations (anim/*.html) sont des pages à part : elles ont leur propre
   entrée de cache, pour ne jamais écraser la page d'accueil. */
const ANIMS = ['photon'];
const ASSETS = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png',
  './anim/moteur.css?v=1', './anim/moteur.js?v=1'].concat(ANIMS.map(function (a) { return './anim/' + a + '.html'; }));

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

  // Pages : reseau d'abord, cache en secours (hors ligne).
  // La page d'accueil sous la cle './index.html', une animation sous sa propre adresse (sans parametres).
  if (e.request.mode === 'navigate' || url.pathname.endsWith('.html')) {
    var accueil = url.pathname.endsWith('/') || url.pathname.endsWith('/index.html');
    var cle = accueil ? './index.html' : url.origin + url.pathname;
    e.respondWith(
      fetch(e.request).then(function (r) {
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
