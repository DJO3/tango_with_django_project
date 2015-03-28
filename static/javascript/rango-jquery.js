$(document).ready( function() {

    $("#about-btn").addClass('btn btn-primary').click ( function() {

        msgstr = $("#msg").html();
        msgstr = msgstr + "o";
        $("#msg").html(msgstr);

    }).hover(function () {
            $(this).css('background-color', '#9f33b8');
            $(this).css('border-color', '#8732a3');
    },
        function() {
            $(this).css('background-color', '#337ab7');
            $(this).css('border-color', '#2e6da4');
    });

    //$("p").hover( function() {
    //        $(this).css('color', 'red');
    //},
    //function() {
    //        $(this).css('color', 'black');
    //});

});