$(function () {
    $("#share").click(function() {

    });

    $("#download").click(function() {

    });
});

const qrcode = new QRCode(document.getElementById('qrcode'), {
    text: 'http://jindo.dev.naver.com/collie',
    width: 128,
    height: 128,
    colorDark : '#000',
    colorLight : '#fff',
    correctLevel : QRCode.CorrectLevel.H
  });
  
barToggle = 1;
const swup = new Swup()