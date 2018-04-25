// Init Scene, gui params
var scene = new THREE.Scene({ background: 0xffffff });
var params = {
    CA: false,
    FGLightMap: 1,
    FGLightMapColor: "#ffffff",
    exposure: 2,
    bloomStrength: 0,
    bloomThreshold: 0,
    bloomRadius: 0,
    focalLength: 50
};

// CAMERA
var camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 200);
camera.position.x = 0;
camera.position.y = 2;
camera.position.z = 10;

var renderer = new THREE.WebGLRenderer({ antialias: true});
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// ORBIT CONTROLS
var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.mouseButtons = {
    ORBIT: THREE.MOUSE.LEFT
};
controls.enableZoom = false;
controls.enableDamping = true;
controls.dampingFactor = 0.12;
controls.rotateSpeed = 0.1;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.01;
// controls.maxPolarAngle = Math.PI/2; // Don't let to go below the ground

// MAPS
var loader = new THREE.TextureLoader(manager)

var emissive_texture = loader.load('/static/pano/01/AJ001-VR1-Interior_Office_emission.jpg');

var foreground_texture = loader.load('/static/pano/01/AJ001-VR1-Interior_Office_fg.jpg');
var foreground_alpha = loader.load('/static/pano/01/AJ001-VR1-Interior_Office_alpha.jpg');

var background_texture = loader.load('/static/pano/01/AJ001-VR1-Interior_Office_bg.jpg');
var background_emissive_texture = emissive_texture.clone();

foreground_texture.anisotropy = 32;
foreground_texture.wrapS = THREE.RepeatWrapping;
foreground_texture.repeat.x = -1;
foreground_alpha.wrapS = THREE.RepeatWrapping;
foreground_alpha.repeat.x = -1;

emissive_texture.wrapS = THREE.RepeatWrapping;
emissive_texture.repeat.x = -1;

background_texture.wrapS = THREE.RepeatWrapping;
background_texture.repeat.x = -1;

// MATERIALS
var foreground_material = new THREE.MeshStandardMaterial({
    map: foreground_texture,
    alphaMap: foreground_alpha,
    emissive: "#ffffff",
    emissiveMap: emissive_texture,
    emissiveIntensity: 1,
    transparent: true,
    side: THREE.BackSide
});

var background_material = new THREE.MeshStandardMaterial({
    map: background_texture,
    side: THREE.BackSide,
    emissive: 0xffffff,
    emissiveIntensity: .3
});

// GEOMETRY
var foreground_geo = new THREE.SphereBufferGeometry(50, 100, 100);
var background_geo = new THREE.SphereBufferGeometry(100, 60, 40);

foreground_mesh = new THREE.Mesh(foreground_geo, foreground_material);
background_mesh = new THREE.Mesh(background_geo, background_material);

scene.add(foreground_mesh);
scene.add(background_mesh);




//GUI
var gui = new dat.GUI();
var f1 = gui.addFolder('Background');
var f2 = gui.addFolder('Foreground');
var f3 = gui.addFolder('Lens Effects');

f2.add(params, 'exposure', 0, 5).onChange(function (value) {
    light.intensity = Number(value);
});
f2.add(params, 'FGLightMap', 0, 3).onChange(function (value) {
    foreground_material.emissiveIntensity = Number(value);
});

var fg_emissive = f2.addColor( params, 'FGLightMapColor' ).name('Emissive Light Color').listen();
fg_emissive.onChange(function(value) {
    foreground_mesh.material.emissive.setHex( value.replace("#", "0x") );
});


f2.add(params, 'bloomThreshold', 0.0, 1.0).onChange(function (value) {
    bloomPass.threshold = Number(value);
});
f2.add(params, 'bloomStrength', 0.0, 3.0).onChange(function (value) {
    bloomPass.strength = Number(value);
});
f2.add(params, 'bloomRadius', 0.0, 2).onChange(function (value) {
    bloomPass.radius = Number(value);
});

f3.add(params, 'CA', false).onChange(function (value) {
    if (value == false) {
        rgbShift.uniforms.amount.value = 0;
    } else {
        rgbShift.uniforms.amount.value = .0005;
    };
});
f3.add(params, 'focalLength', 0.0, 100).onChange(function (value) {
    camera.fov = Number(value);
    camera.updateProjectionMatrix()
});
update();


// LIGHTING/ENV
var light = new THREE.AmbientLight(0xffffff, 2); // soft white light
scene.add(light);

// LOADING MANAGER
var manager = new THREE.LoadingManager();
manager.onStart = function (url, itemsLoaded, itemsTotal) {
    console.log('Started loading file: ' + url + '.\nLoaded ' + itemsLoaded + ' of ' + itemsTotal + ' files.');
    gui.closed = true;
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




//POST PROCESSING
composer = new THREE.EffectComposer(renderer);

renderPass = new THREE.RenderPass(scene, camera);
copyPass = new THREE.ShaderPass(THREE.CopyShader);
bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), .5, 1.5, .85, 1024);
rgbShift = new THREE.ShaderPass(THREE.RGBShiftShader);
rgbShift.uniforms.amount.value = 0;

composer.addPass(renderPass);
// composer.addPass( bloomPass );
composer.addPass(rgbShift);
composer.addPass(copyPass);
copyPass.renderToScreen = true;

// RENDER LOOP
function render() {
    requestAnimationFrame(render);
    controls.update();
    composer.render();
}

window.addEventListener('resize', onWindowResize, false);
render();

// Functions
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function allItemsLoaded() {
    $('.onepix-imgloader').fadeOut();
    // fade in content (using opacity instead of fadein() so it retains it's height.
    $('.loading-container > *:not(.onepix-imgloader)').fadeTo(8000, 100);
}

function update() {
    foreground_geo.material = new THREE.MeshStandardMaterial({color: 0x000000})
    foreground_geo.material.emissive.setHex(params.FGLightMapColor.replace("#", "0x"))
};
