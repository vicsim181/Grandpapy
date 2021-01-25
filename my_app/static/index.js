$(()=> {
    console.log( "ready!" );
});

let i = 0;


let getRequest = function() {
    message = $('#form').val();
    $('#messages').prepend('<p>' + message);
    const treatedMessage = encodeURIComponent(message);
    console.log(treatedMessage);
    return treatedMessage;
}


let sendRequest = function(request) {
    $.post(`http://localhost:5000/ajax/${request}`, (data) => {
        let responseMaps = data['map'];
        let responseWiki = data['wiki'];
        console.log('map: ' + responseMaps,
                    'wiki: ' + responseWiki);
        showResponse(responseMaps, responseWiki);
        return responseMaps, responseWiki;    
    });
}


let showResponse = function(response1, response2) {
    $('#messages').prepend('<iframe>');
    $('iframe').attr('id', i);
    $('#' + i).attr('src', response1);
    $('#' + i).addClass('googlemap');
    configMaps();
    $('#messages').prepend('<p>' + response2);
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
