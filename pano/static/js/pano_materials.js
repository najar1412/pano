function mat_foreground(manager) {
    var loader = new THREE.TextureLoader(manager);


    var emissive_texture = loader.load('/static/pano/default/default_emissive.jpg');

    var foreground_texture = loader.load('/static/pano/default/default_fg.jpg');
    var foreground_alpha = loader.load('/static/pano/default/default_alpha.jpg');


    foreground_texture.anisotropy = 16;
    foreground_texture.wrapS = THREE.RepeatWrapping;
    foreground_texture.repeat.x = -1;
    foreground_alpha.wrapS = THREE.RepeatWrapping;
    foreground_alpha.repeat.x = -1;

    emissive_texture.wrapS = THREE.RepeatWrapping;
    emissive_texture.repeat.x = -1;

    var foreground_material = new THREE.MeshStandardMaterial({
        map: foreground_texture,
        alphaMap: foreground_alpha,
        emissive: "#ffffff",
        emissiveMap: emissive_texture,
        emissiveIntensity: 1,
        transparent: true,
        side: THREE.BackSide
    });

    return foreground_material
}

function mat_background(manager) {
    var loader = new THREE.TextureLoader(manager)

    var background_texture = loader.load('/static/pano/default/default_bg.jpg');

    background_texture.wrapS = THREE.RepeatWrapping;
    background_texture.repeat.x = -1;

    var background_material = new THREE.MeshStandardMaterial({
        map: background_texture,
        side: THREE.BackSide,
        emissive: 0xffffff,
        emissiveIntensity: .3
    });

    return background_material
}