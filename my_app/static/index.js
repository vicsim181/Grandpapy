$(()=> {
    console.log( "ready!" );
});

function treatInput(inputToTreat) {
    let specCar = ['{', '}', '<', '>', '&', '/']
    for (let cars = 0; cars < inputToTreat.length; cars++) {
        if (specCar.indexOf(inputToTreat[cars]) !== -1) {
            inputToTreat = inputToTreat.replace(inputToTreat[cars], '');
        };
    };
    return inputToTreat;
}


function getRequest() {
    message = $('#form').val();
    $('#form').val("");
    messageTreated = treatInput(message);
    $('.messages').append('<div class="request">' + messageTreated);
    let scroll = $('.board-main').prop('scrollHeight');
    $('.board-main').scrollTop(scroll);
    if (messageTreated.toLowerCase() === 'salut') {
        $('#Layer_1').hide();
        $('.messages').append("<div class='answer'>" + "Salut, tu veux quelque chose ?");
        return 0;
    } else {
        const encodedMessage = encodeURIComponent(message);
        return encodedMessage;
    }
}


async function sendRequest(request) {
    return $.post(`https://grandpapy.herokuapp.com/ajax/${request}`);
}


function showResponse(data) {
    $('.messages').append("<div class='answer'>" + data["first_sentence"] + data["address"] + ".");
    let scroll = $('.board-main').prop('scrollHeight');
    $('.board-main').scrollTop(scroll);
    setTimeout(() => {
        let iframe = $('<iframe>');
        $('.messages').append(iframe);
        iframe.attr('src', data['map']).addClass('googlemap');
        $('.messages').append('<div class="answer">' + data['second_sentence'] + data['wiki']);
        configMaps();
        $('#Layer_1').hide();
    }, 2000);
}


function showErrorSentence(sentence) {
    $('#Layer_1').hide();
    $('.messages').append("<div class='answer'>" + sentence + ".");
}

function configMaps() {
    $('.googlemap').attr('frameborder', '0');
    $('.googlemap').attr('style', 'border:0');
    $('.googlemap').attr('allowfullscreen');
}


async function displayMessages() {
    let request = getRequest();
    if (request === 0) {
        return;
    } else {
        try {
            let data = await sendRequest(request);
            if (data['status'] === 1) {
                showResponse(data);
            } else if (data['status'] === 0) {
                showErrorSentence(data['first_sentence']);
            }
        } catch(error) {
            $('#Layer_1').hide();
            $('.messages').append("<div class='answer'>" + "Désolé mais je ne suis pas en état de te répondre...");
        }
    }
}


$("#button").on('click', async function () {
    $('#Layer_1').show();
    await displayMessages();
    setTimeout(() => {
        let scroll = $('.board-main').prop('scrollHeight');
        $('.board-main').scrollTop(scroll);
    }, 2500);
});