function OrbitControls(camera, element) {
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

    return controls;
}

