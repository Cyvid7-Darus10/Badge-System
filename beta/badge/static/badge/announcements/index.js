closeModal();

function openModal(id) {
    // adjust the modal position
    var offset = $(document).scrollTop(),
    viewportHeight = $(window).height(),
    $modal = $('#modal-container');
    $modal.css('top',  (offset - 50  + (viewportHeight/30)));


    let imgSrc = $("#card" + id + " img").attr('src');
    ImgEl = "<img src="+ imgSrc +" alt=''>";

    let text = $("#card" + id + " input").val();
    text = "<p>" + text + "</p>";
    
    console.log();
    $('.modal').html(ImgEl + text);
    $('#modal-container').removeAttr('class').addClass("open");
    $('body').addClass('modal-active');
    
}

function closeModal() {
    $('#modal-container').addClass('out');
    $('#modal-container').removeClass('modal-active');
}