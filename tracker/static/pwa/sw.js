const CACHE_NAME = 'jan-aushadi-v2';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  // Pass-through network fetch (no offline caching yet)
  event.respondWith(fetch(event.request));
});