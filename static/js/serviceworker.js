
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open('gcna-offline-access').then((cache) => {
            return cache.addAll([
                // Add URLs to assets you want to cache
                '/',
                '/adhome',
                '/addIH0/',
                '/login/',
                '/login1/',
                '/table/',
                '/table001/',
                '/add_to_session/',
                '/gcna8',
                '/gcna9',
                '/gcna10',
                '/gcna11',
                '/gcna12',
                '/DriedA',
                '/DriedB',
                '/FloatA',
                '/FloatB',
                '/Quality',
                '/gcna00_1/',
                '/gcna00_2/',
                '/gcna00_3/',
                '/gcna00_4/',
                '/gcna00_5/',
                '/gcna00_6/',
                '/gcna00_7/',
                '/gcna00_8/',
                '/gcna00_9/',
                '/gcna00_10/',
                '/gcna00_11/',
                '/gcna00_12/',
                '/gcna00_13/',
                '/gcna00_14/',
                '/gcna00_15/',
                '/gcna00_16/',
                '/gcna00_17/',
                '/gcna00_18/',
                '/gcna00_19/',
                '/gcna00_20/',
                '/gcna00_21/',
                '/gcna00_22/',
                '/gcna00_23/',
                '/gcna00_24/',


                '/0gcna00_1/',
                '/0gcna00_2/',
                '/0gcna00_3/',
                '/0gcna00_4/',
                '/0gcna00_5/',
                '/0gcna00_6/',
                '/0gcna00_7/',
                '/0gcna00_8/',
                '/0gcna00_9/',
                '/0gcna00_10/',
                '/0gcna00_11/',
                '/0gcna00_12/',
                '/0gcna00_13/',
                '/0gcna00_14/',
                '/0gcna00_15/',
                '/0gcna00_16/',
                '/0gcna00_17/',
                '/0gcna00_18/',
                '/0gcna00_19/',


                
                '/api/DriedA/',
                '/api/DriedB/',
                '/api/FloatA/',
                '/api/FloatB/',
                '/api/Farmer/',
                '/api/Quaility/',


                '/api/visit/',
                '/api/In-House-Drying/',
                '/api/Dispatch-Of-Dried-Nutmeg/',
                '/api/Dispatch-Of-Green/',
                '/api/Cracking-Summary/',
                '/api/Floation-Summary/',
                '/api/Package-Ciontrol/',
                '/api/Editors/',
                '/api/Labour-support/',
                '/api/Training-support/',
                '/api/land-info/',
                '/api/Land-Tenur/',
                '/api/Nutmeg-Trees/',
                '/api/Nutmeg-Variety/',
                '/api/Other-Crops/',
                '/api/Coconut-Trees/',
                '/api/Citrus-Mango-Trees/',
                '/api/Other-Spices-Trees/',
                '/api/Other-Seasoning-Trees/',
                '/api/Other-Crops-Cultivated/',
                '/api/Condition/',
                '/api/Nutmeg-Land/',
                '/api/Nutmeg-Frequency/',
                '/api/Potential-Risks/',
                '/api/Road-Access/',
                '/api/Food-Safety-and-Quality/',
                '/api/Farm-Water-Source/',
                '/api/Farm-House/',
                '/api/inspector-symmary/',
                '/api/Policy/',


                '/view_tablet/',
                '/view_tablet2/',
                '/view_Visit/',
                '/edit_Visit/',
                '/table1/',      
                '/table2/',      
            ]);
        })
    );
});



self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});

