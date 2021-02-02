$(()=> {
    console.log( "ready!" );
});


function getRequest() {
    message = $('#form').val();
    $('#messages').prepend('<p>' + message);
    const treatedMessage = encodeURIComponent(message);
    // console.log(treatedMessage);
    return treatedMessage;
}


async function sendRequest(request) {
    return $.post(`http://localhost:5000/ajax/${request}`);
}


function showResponse(data) {
    $('#messages').prepend('<p>' + data['first_sentence'] + data['address'] + '.');
    setTimeout(() => {
        let iframe = $('<iframe>');
        $('#messages').prepend(iframe);
        iframe.attr('src', data['map']).addClass('googlemap');
        $('#messages').prepend('<p>' + data['second_sentence'] + data['wiki']);
        configMaps();
    }, 4000);   
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
    displayMessages();
});

$('#form').on('keypress', function(e) {
    if(e.which == 13) {
        displayMessages();
    }
});
