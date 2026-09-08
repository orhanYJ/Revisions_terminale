// Service worker — L'Index raisonné (PWA)
// Stratégie : réseau d'abord pour la page (HTML), cache d'abord pour les assets.
const CACHE = "philo-v1";
const CORE = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icon-192.png",
  "./icon-512.png"
];

// Installation : pré-cache des ressources de base.
self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.addAll(CORE);
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

// Activation : nettoyage des anciens caches.
self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.filter(function (k) { return k !== CACHE; })
            .map(function (k) { return caches.delete(k); })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

// Requêtes : on ne gère que le même origine et le GET.
self.addEventListener("fetch", function (event) {
  var req = event.request;
  if (req.method !== "GET") return;

  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // laisser passer les polices Google, etc.

  var isDoc = req.mode === "navigate" ||
              (req.headers.get("accept") || "").indexOf("text/html") !== -1;

  if (isDoc) {
    // Réseau d'abord pour la page : contenu à jour, repli sur le cache hors ligne.
    event.respondWith(
      fetch(req).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put("./index.html", copy); });
        return res;
      }).catch(function () {
        return caches.match(req).then(function (m) {
          return m || caches.match("./index.html");
        });
      })
    );
  } else {
    // Cache d'abord pour les assets : rapide et disponible hors ligne.
    event.respondWith(
      caches.match(req).then(function (cached) {
        return cached || fetch(req).then(function (res) {
          var copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); });
          return res;
        });
      })
    );
  }
});
