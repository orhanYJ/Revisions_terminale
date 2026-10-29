/* Service worker — DNL Histoire-Géo Terminale BFI
   Stratégie : réseau d'abord pour la page (mises à jour immédiates),
   repli cache hors ligne. Assets : cache d'abord. */
const CACHE = "dnl-v40-voix-remy";
const ASSETS = ["./", "index.html", "manifest.json", "icon-192.png", "icon-512.png"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  const isPdf = url.pathname.endsWith(".pdf");
  const isCarte = url.pathname.indexOf("/cartes/") >= 0 && url.pathname.endsWith(".html");
  const isPage = !isPdf && !isCarte && (req.mode === "navigate" || url.pathname.endsWith("/") || url.pathname.endsWith("index.html"));
  if (isCarte) {
    // carte animée ouverte dans une iframe : c'est une navigation, mais elle a sa propre clé de cache
    // (ne jamais la ranger sous "./", elle remplacerait la page d'accueil)
    const cle = url.origin + url.pathname;
    e.respondWith(
      fetch(cle, { cache: "no-cache" })
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(cle, copy));
          return res;
        })
        .catch(() => caches.match(cle))
    );
  } else if (isPdf) {
    // fiches imprimables : réseau d'abord (une fiche régénérée s'affiche tout de suite), copie pour le hors-ligne
    e.respondWith(
      fetch(req.url, { cache: "no-cache" })
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req))
    );
  } else if (isPage) {
    // « no-cache » : toujours revalider auprès du serveur, sans réutiliser la copie
    // que le navigateur garde 10 minutes (GitHub Pages envoie max-age=600)
    e.respondWith(
      fetch(req.url, { cache: "no-cache", credentials: "same-origin" })
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put("./", copy));
          return res;
        })
        .catch(() => caches.match("./"))
    );
  } else {
    e.respondWith(
      caches.match(req).then(
        (hit) =>
          hit ||
          fetch(req).then((res) => {
            const copy = res.clone();
            caches.open(CACHE).then((c) => c.put(req, copy));
            return res;
          })
      )
    );
  }
});
