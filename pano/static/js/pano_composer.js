function composer_passes(renderer, scene, camera, window) {
    // adds all passes to composer
    // return: composer object
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

    return composer;
}