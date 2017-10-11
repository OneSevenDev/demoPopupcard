(function ($) {
    fn_init();
})(jQuery);

function fn_init() {
    var path_url = window.location.pathname;

    var array_link = path_url.split('/');

    var prefix = array_link[array_link.length - 3];

    if (prefix.length == 1){
        $('#' + array_link[array_link.length - 2]).addClass('active');
    } else {
        $('#all').addClass('active');
    }
}