var CACHE_NAME = "Django Cache";
var urlsToCache = [
  "/",
  "/static/app/css/style.css",
  "/static/app/img/happy_piggy_logo.png",
];

self.addEventListener("install", function (event) {
  //Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      console.log("Opened cache");
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return fetch(event.request).catch(function (rsp) {
        return response;
      });
    })
  );
});
