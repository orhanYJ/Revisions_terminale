/* Service worker — SVT Terminale
   Stratégie : réseau d'abord pour les pages (mises à jour immédiates),
   repli cache hors ligne. Assets : cache d'abord.
   Les animations (anim/*.html) sont des pages à part : elles ont leur propre
   entrée de cache, pour ne jamais écraser la page d'accueil. */
const CACHE = "svt-v10";
const ANIMS = ["mitose", "replication", "expression", "enzyme", "globe", "tectonique",
  "ecosysteme", "immunite", "anticorps", "clonal", "meiose", "nondisj", "coinegal", "globines",
  "thg", "insuline", "endosymbiose"];
const ASSETS = ["./", "index.html", "manifest.json", "icon-192.png", "icon-512.png",
  "anim/moteur.css?v=2", "anim/moteur.js?v=2"].concat(ANIMS.map((a) => "anim/" + a + ".html"));

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
  const isHtml = req.mode === "navigate" || url.pathname.endsWith(".html") || url.pathname.endsWith("/");
  if (isHtml) {
    // page d'accueil sous la clé "./", animations sous leur propre adresse (sans paramètres)
    const isIndex = url.pathname.endsWith("/") || url.pathname.endsWith("/index.html");
    const key = isIndex ? "./" : url.origin + url.pathname;
    e.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(key, copy));
          return res;
        })
        .catch(() => caches.match(key, { ignoreSearch: true }))
    );
  } else {
    // assets : cache d'abord, complété au fil de l'eau
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
