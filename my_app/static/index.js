$(()=> {
    console.log( "ready!" );
});


function getRequest() {
    message = $('#form').val();
    $('#form').val("");
    $('.messages').append('<div class="request">' + message);
    const treatedMessage = encodeURIComponent(message);
    return treatedMessage;
}


async function sendRequest(request) {
    return $.post(`http://localhost:5000/ajax/${request}`);
}


function showResponse(data) {
    $('.messages').append("<div class='answer'>" + data["first_sentence"] + data["address"] + ".");
    setTimeout(() => {
        let iframe = $('<iframe>');
        $('.messages').append(iframe);
        iframe.attr('src', data['map']).addClass('googlemap');
        $('.messages').append('<div class="answer">' + data['second_sentence'] + data['wiki']);
        configMaps();
        $('#Layer_1').hide();
    }, 2000);   
}


function configMaps() {
    $('.googlemap').attr('frameborder', '0');
    $('.googlemap').attr('style', 'border:0');
    $('.googlemap').attr('allowfullscreen');
}


async function displayMessages() {
    let request = getRequest();
    let data = await sendRequest(request);
    showResponse(data);
}

$("#button").on('click', async function () {
    $('#Layer_1').show();
    displayMessages();
});

$('#form').on('keypress', function(e) {
    if(e.which == 13) {
        $('#Layer_1').show();
        displayMessages();
    }
});
