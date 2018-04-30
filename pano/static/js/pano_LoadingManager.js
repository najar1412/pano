// LOADING MANAGER


function loadingManager() {
    var manager = new THREE.LoadingManager();
    manager.onStart = function (url, itemsLoaded, itemsTotal) {
        console.log('Started loading file: ' + url + '.\nLoaded ' + itemsLoaded + ' of ' + itemsTotal + ' files.');
    };
    
    manager.onLoad = function () {
        allItemsLoaded();
    };
    
    manager.onProgress = function (url, itemsLoaded, itemsTotal) {
        console.log('Loading file: ' + url + '.\nLoaded ' + itemsLoaded + ' of ' + itemsTotal + ' files.');
    };
    
    manager.onError = function (url) {
        console.log('There was an error loading ' + url);
    };

    return manager
}