var CACHE = 'ses-v9';
var ASSETS = ['./', 'index.html', 'manifest.json', 'icon-192.png', 'icon-512.png', 'assistant.js?v=10'];

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
  if (url.origin !== self.location.origin) return;
  /* Vidéos du chapitre (serie/) : le son est lu par plages, le service worker le laisse passer */
  if (url.pathname.endsWith('.mp3')) return;
  /* Une vidéo (serie/*.html) est une page à part, montée en iframe : réseau d'abord, rangée sous sa propre adresse
     (une iframe est une navigation : ne jamais la ranger sous la clé de la page d'accueil) */
  if (url.pathname.indexOf('/serie/') >= 0 && url.pathname.endsWith('.html')) {
    var cle = url.origin + url.pathname;
    e.respondWith(
      fetch(e.request.url, { cache: 'no-cache', credentials: 'same-origin' }).then(function (r) {
        var copie = r.clone();
        caches.open(CACHE).then(function (c) { c.put(cle, copie); });
        return r;
      }).catch(function () { return caches.match(cle, { ignoreSearch: true }); })
    );
    return;
  }
  var isPage = e.request.mode === 'navigate' ||
    url.pathname.endsWith('/') || url.pathname.endsWith('index.html');

  if (isPage) {
    /* Réseau d'abord (sans le cache HTTP de 10 minutes de GitHub Pages), cache en secours hors ligne */
    e.respondWith(
      fetch(e.request, { cache: 'no-cache' }).then(function (r) {
        var copie = r.clone();
        caches.open(CACHE).then(function (c) { c.put('./', copie); });
        return r;
      }).catch(function () {
        return caches.match('./').then(function (m) {
          return m || caches.match('index.html');
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
