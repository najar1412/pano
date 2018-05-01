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

var renderer = new THREE.WebGLRenderer({ antialias: false});
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Loading manager
const manager = loadingManager();
// camera controls
const orbit_controls = OrbitControls(camera, renderer.domElement);

// geometry_mats
fg_mat = mat_foreground(manager);
bg_mat = mat_background(manager);
var foreground_geo = new THREE.SphereBufferGeometry(50, 100, 100);
var background_geo = new THREE.SphereBufferGeometry(100, 60, 100);

foreground_mesh = new THREE.Mesh(foreground_geo, fg_mat);
background_mesh = new THREE.Mesh(background_geo, bg_mat);

scene.add(foreground_mesh);
scene.add(background_mesh);

// lighting_env
var light = new THREE.AmbientLight(0xffffff, 2); // soft white light
scene.add(light);

// gui
gui()
update();

// Effect Composer
composer = composer_passes(renderer, scene, camera, window);

// RENDER LOOP
function render() {
    requestAnimationFrame(render);
    orbit_controls.update();
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


