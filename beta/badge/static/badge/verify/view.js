$(function () {
    $("#download").click(function() {
        let badge = $('#badge');
        let filename = $('#label').html();

        base_image = new Image();
        base_image.crossOrigin="anonymous";
        base_image.src = badge.attr('src');

        canvas.width = 700;
        canvas.height = 700;

        base_image.onload = function(){
            context.globalAlpha = 1.0;
            context.drawImage(base_image, 0, 0, 700, 700);
            qr_image = new Image();
            qr_image.src = dataURI;
    
            qr_image.onload = function(){
                context.globalAlpha = 0.8;
                context.drawImage(qr_image, 500, 500, 200, 200);
                downloadURI(canvas.toDataURL(), filename + " Badge")
            }
        }        
    });
});

var canvas = document.createElement("CANVAS");
var context = canvas.getContext('2d');
var qr = new QRious({
    size: 200,
    value: window.location.href
});
var dataURI = qr.toDataURL();

function downloadURI(uri, name) {
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    delete link;
}

// facebook
function shareFB(fbShareLink) {
    var fbpopup = window.open("https://www.facebook.com/sharer/sharer.php?u=" + fbShareLink, "pop", "width=600, height=400, scrollbars=no");
    return false;
};
  
// twitter
function shareTwitter(twShareLink) {
    var twpopup = window.open("http://twitter.com/intent/tweet?" + twShareLink , "pop", "width=600, height=400, scrollbars=no");
    return false;
};


