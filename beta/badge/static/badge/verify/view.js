$(function () {
    $("#share").click(function() {

    });

    $("#download").click(function() {
        let badge = $('#badge');
        let filename = $('#label').html();

        base_image = new Image();
        base_image.crossOrigin="anonymous";
        base_image.src = badge.attr('src');

        canvas.width = 500;
        canvas.height = 500;

        base_image.onload = function(){
            context.globalAlpha = 1.0;
            context.drawImage(base_image, 0, 0, 500, 500);
            qr_image = new Image();
            qr_image.src = dataURI;
    
            qr_image.onload = function(){
                context.globalAlpha = 0.5;
                context.drawImage(qr_image, 400, 400, 100, 100);
                downloadURI(canvas.toDataURL(), filename + " Badge")
            }
        }        
    });
});

function downloadURI(uri, name) {
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    delete link;
}


var canvas = document.createElement("CANVAS");
var context = canvas.getContext('2d');

var qr = new QRious({
    size: 200,
    value: window.location.href
});

var dataURI = qr.toDataURL();
