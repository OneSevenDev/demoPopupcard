(function ($) {
    fn_init();
})(jQuery);

function fn_init() {
    fn_fill_comments();
}

function fn_fill_comments() {
    try {
        var url = '/public/api/ws/commets/';
        var send_data = '{}';
        var success = function (response) {
            console.log(response);

            var object = {};
            object.request = response;

            var item = fn_loadtemplates('entry-commend', object);
            $("#content-comment").html(item);
        };
        var error = function (xhr, ajaxOptions, thrownError) {
            console.log('error')
        };

        fn_callmethod(url, send_data, success, error);
    } catch (e) {
    }
}


function fn_callmethod(url, data, success, error) {
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: success,
        error: error
    });
}

function fn_callmethodasync(url, data, success, error, async) {
    $.ajax({
        async: async,
        type: "POST",
        url: url,
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: success,
        error: error
    });
}

function fn_loadtemplates(templateID, JsonObject) {
    Handlebars.registerHelper('ifCond', function (v1, v2, options) {
        if (v1 > v2) {
            return options.fn(this);
        }
        return options.inverse(this);
    });

    Handlebars.registerHelper('ifEquals', function (v1, v2, options) {
        if (v1 == v2) {
            return options.fn(this);
        }
        return options.inverse(this);
    });

    var stemplate = $("#" + templateID).html();
    var tmpl = Handlebars.compile(stemplate);
    var html = tmpl(JsonObject);
    return html;
}