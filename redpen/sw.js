var CACHE = "redpen-v1";
var ASSETS = ["./", "index.html", "manifest.json", "icon-192.png", "icon-512.png"];

self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; })
        .map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener("fetch", function (e) {
  if (e.request.method !== "GET") return;
  var isPage = e.request.mode === "navigate" || e.request.destination === "document";
  if (isPage) {
    /* page : réseau d'abord, cache en secours */
    e.respondWith(
      fetch(e.request).then(function (r) {
        var copy = r.clone();
        caches.open(CACHE).then(function (c) { c.put("./", copy); });
        return r;
      }).catch(function () {
        return caches.match("./").then(function (r) { return r || caches.match("index.html"); });
      })
    );
  } else {
    /* assets : cache d'abord, réseau en secours */
    e.respondWith(
      caches.match(e.request).then(function (r) {
        return r || fetch(e.request).then(function (resp) {
          var copy = resp.clone();
          caches.open(CACHE).then(function (c) { c.put(e.request, copy); });
          return resp;
        });
      })
    );
  }
});
