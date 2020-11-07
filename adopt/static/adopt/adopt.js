document.addEventListener('DOMContentLoaded', function() {
    var messages=document.querySelectorAll("#messages");
    for ( var a=0;a<messages.length;a++){
        messages[a].addEventListener('click',display_message);
    }
})

function display_message(){
    let message_id=this.dataset.message;
    fetch('/get_message/'+message_id).then(response=> response.json()).then(message=>{
        document.querySelector('#messages_view').style.display='none';
        document.querySelector('#message_view').style.display='block';
        document.querySelector('#send_to').innerHTML=`<a href="/profile/${message.sender_id}">${message.sender}</a>`;
        document.querySelector('#message').innerHTML=`<span>${message.message}</span>`;
        
    });
}