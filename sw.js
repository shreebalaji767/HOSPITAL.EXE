const CACHE='hospital-exe-v2';
const ASSETS=[
  './',
  './index.html',
  './facilities.html',
  './doctors.html',
  './comics.html',
  './css/style.css',
  './js/app.js',
  './manifest.webmanifest'
];

self.addEventListener('install',e=>{
  e.waitUntil(
    caches.open(CACHE)
      .then(c=>c.addAll(ASSETS))
      .then(()=>self.skipWaiting())
  );
});

self.addEventListener('activate',e=>{
  e.waitUntil(
    caches.keys().then(keys=>
      Promise.all(
        keys.filter(key=>key!==CACHE).map(key=>caches.delete(key))
      )
    ).then(()=>self.clients.claim())
  );
});

self.addEventListener('fetch',e=>{
  const request=e.request;

  if(request.method!=='GET') return;

  // Only cache normal web requests.
  // Browser extensions, devtools and other special schemes
  // cannot be stored in the Cache API.
  if(request.url.startsWith('chrome-extension://')) return;
  if(request.url.startsWith('chrome://')) return;
  if(request.url.startsWith('edge://')) return;
  if(request.url.startsWith('about:')) return;

  let url;
  try{
    url=new URL(request.url);
  }catch{
    return;
  }

  if(url.protocol!=='http:' && url.protocol!=='https:') return;

  e.respondWith(
    caches.match(request).then(cached=>{
      if(cached) return cached;

      return fetch(request).then(response=>{
        if(!response || !response.ok) return response;

        const copy=response.clone();

        caches.open(CACHE).then(cache=>{
          cache.put(request,copy).catch(()=>{});
        });

        return response;
      }).catch(()=>caches.match('./index.html'));
    })
  );
});