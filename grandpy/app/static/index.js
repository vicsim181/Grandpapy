$(()=> {
    console.log( "ready!" );
});

let send_message = function() {
    let message = $('#form').val();
    $.getJSON(`http://localhost:5000/map/${message}`, (data)=> {
        console.log(data);
    });
}


