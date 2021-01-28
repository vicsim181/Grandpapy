$(()=> {
    console.log( "ready!" );
});


function getRequest() {
    message = $('#form').val();
    $('#messages').prepend('<p>' + message);
    const treatedMessage = encodeURIComponent(message);
    console.log(treatedMessage);
    return treatedMessage;
}


async function sendRequest(request) {
    return $.post(`http://localhost:5000/ajax/${request}`);
}


function showFirstResponse(data) {
    $('#messages').prepend('<p>' + data['first_sentence'] + data['address'] + '.');
}


function showSecondResponse(data) {
    let iframe = $('<iframe>')
    $('#messages').prepend(iframe);
    iframe.attr('src', data['map']).addClass('googlemap');
    $('#messages').prepend('<p>' + data['second_sentence'] + data['wiki']);
    configMaps();
}


function configMaps() {
    $('.googlemap').attr('width', '400');
    $('.googlemap').attr('height', '250');
    $('.googlemap').attr('frameborder', '0');
    $('.googlemap').attr('style', 'border:0');
    $('.googlemap').attr('allowfullscreen');
}


// async function displayMessages() {
//     let request = getRequest();
//     let data = await sendRequest(request);
//     showFirstResponse(data);
//     showSecondResponse(data);
//     setTimeout(console.log('10 secondes'), 10000);
// }


$("#button").on('click', async function () {
    let request = getRequest();
    let data = await sendRequest(request);
    showFirstResponse(data);
    showSecondResponse(data);
    setTimeout(console.log('10 secondes'), 10000);
});

$('#form').on('keypress',async function(e) {
    if(e.which == 13) {
        let request = getRequest();
        let data = await sendRequest(request);
        showFirstResponse(data);
        showSecondResponse(data);
        setTimeout(console.log('10 secondes'), 10000);
    }
});
