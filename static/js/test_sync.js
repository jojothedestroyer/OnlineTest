var openRequest = indexedDB.open('GCNA', 2);

// openRequest.onsuccess = function(e) {
//     var db = e.target.result;
//     var transaction = db.transaction(["visit"]);
//     var objectStore = transaction.objectStore("visit");
//     var getRequest = objectStore.getAll();

//     getRequest.onsuccess = function(event) {
//         var results = event.target.result;
//         results.forEach(function(result) {
//             fetch('/api/visit/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCookie('csrftoken')

//                 },
//                 body: JSON.stringify(result),
//             })
//             .then(response => response.json())
//             .then(data => console.log('Success:', data))
//             .catch((error) => console.error('Error:', error));
//         });
//     };
// };



// openRequest.onsuccess = function(e) {
//     var db = e.target.result;
//     var transaction = db.transaction(["visit"]);
//     var objectStore = transaction.objectStore("visit");
//     var getRequest = objectStore.getAll();

//     getRequest.onsuccess = function(event) {
//         var results = event.target.result;
//         results.forEach(function(result) {
//             fetch('/api/visit2/'+ result.id + '/', {
//                 method: 'PATCH',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCookie('csrftoken')

//                 },
//                 body: JSON.stringify(result),
//             })
//             .then(response => response.json())
//             .then(data => console.log('Success:', data))
//             .catch((error) => console.error('Error:', error));
//         });
//     };
// };




openRequest.onsuccess = function(e) {
    var db = e.target.result;
    var transaction = db.transaction(["visit"]);
    var objectStore = transaction.objectStore("visit");
    var getRequest = objectStore.getAll();

    getRequest.onsuccess = function(event) {
        var results = event.target.result;
        results.forEach(function(result) {
            fetch('/api/visit2/' + result.id + '/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
            })
            .then(response => {
                if (response.status === 404) {
                    // Object does not exist in Django, make a POST request to create it
                    return fetch('/api/visit/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify(result),
                    });
                } else {
                    // Object exists in Django, make a PATCH request to update it
                    return fetch('/api/visit2/' + result.id + '/', {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify(result),
                    });
                }
            })
            .then(response => response.json())
            .then(data => console.log('Success:', data))
            .catch((error) => console.error('Error:', error));
        });
    };
};






function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
