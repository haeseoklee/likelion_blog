$(document).ready(function(){
    $('.ui .segment .menu .item').on('click', function() {
        $('.ui .segment .menu .item').removeClass('active');
        $(this).addClass('active');
        console.log($(this))
    });              
});
