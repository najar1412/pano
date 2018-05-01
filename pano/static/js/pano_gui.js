function gui() {
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
    gui.closed = true;
}

function update() {
    foreground_geo.material = new THREE.MeshStandardMaterial({color: 0x000000})
    foreground_geo.material.emissive.setHex(params.FGLightMapColor.replace("#", "0x"))
};