$(document).ready(function() {
    $(".dropdown-menu li a").click(function() {
        if ($(this).parent().find('.btn').length > 0) {
            $(this).parents("#_dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
            $(this).parents("#_dropdown").find('.btn').val($(this).data('value'));
        }
    });

    $('#btn-toggle').click(function() {
        $(this).find('.btn').toggleClass('active');
        if ($(this).find('.btn-success').length > 0) {
            $(this).find('.btn').toggleClass('btn-success');
        }
        $(this).find('.btn').toggleClass('btn-default');
    });

    $('#btn-toggle_HasChild').click(function() {
        $(this).find('.btn').toggleClass('active');
        if ($(this).find('.btn-success').length > 0) {
            $(this).find('.btn').toggleClass('btn-success');
        }
        $(this).find('.btn').toggleClass('btn-default');
    });

    $('#btn-toggle_Vegetable').click(function() {
            $(this).find('.btn').toggleClass('active');
            if ($(this).find('.btn-success').length > 0) {
                $(this).find('.btn').toggleClass('btn-success');
            }
            $(this).find('.btn').toggleClass('btn-default');
    });

    $('#btn-toggle_Relational').click(function() {
        $(this).find('.btn').toggleClass('active');
        if ($(this).find('.btn-success').length > 0) {
            $(this).find('.btn').toggleClass('btn-success');
        }
        $(this).find('.btn').toggleClass('btn-default');
    });
});
