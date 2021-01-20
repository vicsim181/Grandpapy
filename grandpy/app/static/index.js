$(()=> {
    console.log( "ready!" );
});

// // let send_message = function() {
// //     let message = $('#form').val();
// //     $.getJSON(`http://localhost:5000/map/${message}`, (data)=> {
// //         console.log(data);
// //     });
// // }

let sendMessage = function() {
    message = $('#form').val();
    const messageSection = $('#messages');
    console.log(message);
    let para = $.add('p');
    let node = document.createTextNode(message);
    para.appendChild(node);
    messageSection.appendChild(para);
}

// let getRequest = function() {

// }

// let showResponse = function() {

// }

// if ($('#button').trigger(buttonEvent)) function(event) {
    
// })


$("#button").on('click', function () {
    // event.preventDefault();
    // event.stopPropagation();
    alert('bonjour');
    sendMessage();
    
});