$(function () {
    $.getJSON('/static/lib/profanity/swearWords.json', function(data) {
        swear_words_arr = data;
        regex = new RegExp('\\b(' + swear_words_arr.join('|') + ')\\b', 'i' );
    });

    const swup = new Swup();
    init();
    swup.on('contentReplaced', init);
});

var barToggle = 1;
var swear_words_arr = [];
var regex;

function init() {
    $('input').keyup(function() {
        var input = this.value;
        if (!noProfanity(input)) {
            $(this).val("");
        }
    });

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
}

function noProfanity(input) {
    if(regex.test(input)) {
        alert("Please refrain from using offensive words.");
        return false;
    }
    return true;
}
