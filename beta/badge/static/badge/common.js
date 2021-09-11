$(function () {
    $("#bar").click(function() {
        $(".menu ul").toggleClass("flex-row");
        if (barToggle) {
            $(".menu").css("display", "block");
            $(".logo").css("display", "none");
            barToggle = 0;
        } else {
            $(".menu").css("display", "none");
            $(".logo").css("display", "block");
            barToggle = 1;
        }
    });
});

barToggle = 1;
const swup = new Swup()