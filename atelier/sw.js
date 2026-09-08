const CACHE = "atelier-v1";
const COQUILLE = ["./", "./index.html", "./manifest.json", "./icon-192.png", "./icon-512.png"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(COQUILLE)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((noms) => Promise.all(noms.filter((n) => n !== CACHE).map((n) => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  // Les appels au modele ne passent jamais par le cache.
  if (url.origin !== self.location.origin) return;
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request).then((rep) => rep || fetch(e.request).then((reseau) => {
      const copie = reseau.clone();
      caches.open(CACHE).then((c) => c.put(e.request, copie));
      return reseau;
    }).catch(() => caches.match("./index.html")))
  );
});
