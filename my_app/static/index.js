$(()=> {
    console.log( "ready!" );
});

let i = 0;


let getRequest = function() {
    message = $('#form').val();
    $('#messages').prepend('<p>' + message);
    const treatedMessage = message.replace('?', ' ')
    return treatedMessage;
}


let sendRequest = function(request) {
    $.post(`http://localhost:5000/ajax/${request}`, (data) => {
        let responseMaps = data['response'];
        console.log('response: ' + responseMaps);
        showResponse(responseMaps);
        return responseMaps;    
    });
}


let showResponse = function(response) {
    $('#messages').prepend('<iframe>');
    $('iframe').attr('id', i);
    $('#' + i).attr('src', response);
    $('#' + i).addClass('googlemap');
    configMaps();
}


let configMaps = function() {
    $('.googlemap').attr('width', '400');
    $('.googlemap').attr('height', '250');
    $('.googlemap').attr('frameborder', '0');
    $('.googlemap').attr('style', 'border:0');
    $('.googlemap').attr('allowfullscreen');
}


let displayMessages = function() {
    let request = getRequest();
    let response = sendRequest(request);
    showResponse(response);
}


$("#button").on('click', function () {
    displayMessages();
});

$('#form').on('keypress',function(e) {
    if(e.which == 13) {
        displayMessages();
    }
});
