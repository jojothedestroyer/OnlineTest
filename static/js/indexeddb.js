const modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility','visit','In-House-Drying','Dispatch-Of-Dried-Nutmeg','Dispatch-Of-Green','Cracking-Summary','Floation-Summary','Package-Ciontrol','Editors','Labour-support','Training-support','land-info','Land-Tenur','Nutmeg-Trees','Nutmeg-Variety','Other-Crops','Coconut-Trees','Citrus-Mango-Trees','Other-Spices-Trees','Other-Seasoning-Trees','Other-Crops-Cultivated','Condition','Nutmeg-Land','Nutmeg-Frequency','Potential-Risks','Road-Access','Food-Safety-and-Quality','Farm-Water-Source','Farm-House','inspector-symmary','Policy','Policy/<int:id>',];


function deleteDatabase() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.deleteDatabase('GCNA');

        request.onsuccess = function () {
            resolve();
        };

        request.onerror = function (event) {
            reject(event.target.error);
        };
    });
}

function openIndexedDBConnection() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open('GCNA', 2);

        request.onupgradeneeded = function (event) {
            const db = event.target.result;
            modelNames.forEach(modelName => {
                if (!db.objectStoreNames.contains(modelName)) {
                    db.createObjectStore(modelName, { keyPath: 'id' });
                }
            });
        };

        request.onsuccess = function (event) {
            resolve(event.target.result);
        };

        request.onerror = function (event) {
            reject(event.target.error);
        };
    });
}

function fetchDataAndStore(db, modelName) {
    return new Promise((resolve, reject) => {
        fetch(`/api/${modelName}/`)
            .then(response => response.json())
            .then(data => {
                const transaction = db.transaction(modelName, 'readwrite');
                const objectStore = transaction.objectStore(modelName);
                data.forEach(item => {
                    objectStore.put(item);
                });

                transaction.oncomplete = function () {
                    resolve();
                };
            })
            .catch(error => {
                console.error('Error fetching data for model:', modelName, error);
                reject(error);
            });
    });
}

deleteDatabase()
    .then(() => openIndexedDBConnection())
    .then(db => Promise.all(modelNames.map(modelName => fetchDataAndStore(db, modelName))))
    .then(() => console.log('All models stored successfully.'))
    .catch(error => console.error('Error storing models:', error));
