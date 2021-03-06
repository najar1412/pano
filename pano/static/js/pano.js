// Init Scene, gui params
var scene = new THREE.Scene({ background: 0xffffff });
// var pano_id = '{{ test.id | tojson | safe }}';
// var pano_id = JSON.parse(document.getElementById("pano_id").dataset.panoid);


function postOption() {
    $.post( "/postmethod", {
        javascript_data: params
    });
}

// CAMERA
var camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 200);
camera.rotation.order = 'YXZ';
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
var light = new THREE.AmbientLight(0xffffff, 2);

scene.add(light);

// Effect Composer
composer = composer_passes(renderer, scene, camera, window);

function setDatGuiState(params) {
    background_mesh.material.emissiveIntensity = params['bg_brightness'];
    background_mesh.material.emissiveIntensity = params['fg_alpha'];
    light.intensity = params['exposure'];
    foreground_mesh.material.emissiveIntensity = params['FGLightMap'];
    foreground_mesh.material.emissive.setHex( params['FGLightMapColor'].replace("#", "0x") );

    camera.fov = params['focalLength'];
    camera.updateProjectionMatrix()

    bloomPass.strength = params['bloomStrength'];
    bloomPass.radius = params['bloomRadius'];
    bloomPass.threshold = params['bloomThreshold'];
}

setDatGuiState(params);

// RENDER LOOP
function render() {
    updateRotation();
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

function updateRotation() {
    const miniMap = document.getElementById('radar');

    const heading = camera.rotation.y;
    const radians = heading > 0
      ? heading
      : (2 * Math.PI) + heading;
    const degrees = THREE.Math.radToDeg(radians);
    const degreesRounded = Math.floor(degrees);
    $(miniMap).css({
        'position': 'relative',
        'bottom': '160px',
        'left': '80px',
        'width': '50px',
        'height': '50px',
        'transform-origin': 'bottom',
        'transform': 'rotate(-'+ `${degreesRounded}` +'deg)'
      });
  }