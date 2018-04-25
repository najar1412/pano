//to display loading animation before it's ready
$(document).ready(function () {
    if ($('.loading-container').length) {

        // to show loading animation
        $imgloader = $('.loading-container');
        $loadingimg = $('<div id="canvasloader-container" class="onepix-imgloader"></div>');

        // $loadingimg.attr("src","images/flexslider/loading.gif");
        $imgloader.prepend($loadingimg);

        // canvasloader code
        var cl = new CanvasLoader('canvasloader-container');
        cl.setColor('#ffffff'); // default is '#000000'
        cl.setDiameter(55); // default is 40
        cl.setDensity(75); // default is 40
        cl.setRange(0.7); // default is 1.3
        cl.setSpeed(3); // default is 2
        cl.setFPS(22); // default is 24
        cl.show(); // Hidden by default

    }

});
