$(()=> {
    console.log( "ready!" );
});

let i = 0;
let responseMaps;
let responseWiki;
let firstSentence;
let secondSentence;



function getRequest() {
    message = $('#form').val();
    $('#messages').prepend('<p>' + message);
    const treatedMessage = encodeURIComponent(message);
    console.log(treatedMessage);
    return treatedMessage;
}


function sendRequest(request) {
    return $.post(`http://localhost:5000/ajax/${request}`);
    // return $.ajax({
    //     'url': `http://localhost:5000/ajax/${request}`,
        // 'contentType': true,
        // 'data': request,
        // 'dataType': 'text',
        // 'method': 'POST'
    // })
    // });
}


function assignResults(data) {
    responseMaps = data['map'];
    responseWiki = data['wiki'];
    firstSentence = data['first_sentence'];
    secondSentence = data['second_sentence'];
}
        // console.log('maps: ' + responseMaps,
        //             'wiki: ' + responseWiki,
        //             'first: ' + firstSentence,
        //             'second: ' + secondSentence);

function showResponse(responseMaps, responseWiki, firstSentence, secondSentence) {
    $('#messages').prepend('<p>' + firstSentence);
    $('#messages').prepend('<iframe id=' + i + '>');
    $('#' + i).attr('src', responseMaps);
    $('#' + i).addClass('googlemap');
    i ++;
    $('#messages').prepend('<p>' + secondSentence + responseWiki);
    configMaps();
}


function configMaps() {
    $('.googlemap').attr('width', '400');
    $('.googlemap').attr('height', '250');
    $('.googlemap').attr('frameborder', '0');
    $('.googlemap').attr('style', 'border:0');
    $('.googlemap').attr('allowfullscreen');
}


function failProcess() {
    console.log('ERREUR, ça ne marche pas !');
}


function displayMessages() {
    let request = getRequest()
    sendRequest(request)
    .then(data => assignResults(data))
    .then(console.log('maps: ' + responseMaps,
                      'wiki: ' + responseWiki,
                      'first: ' + firstSentence,
                      'second: ' + secondSentence))
    .then(showResponse)
    .catch(failProcess);
    // sendRequest(request)
    // showResponse(responseMaps, responseWiki, firstSentence, secondSentence);
}


$("#button").on('click', function () {
    displayMessages();
});

$('#form').on('keypress',function(e) {
    if(e.which == 13) {
        displayMessages();
    }
});
