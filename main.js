const socket = io.connect('http://' + document.domain + ':' + location.port);

function sendMessage() {
    const message = document.getElementById('message_input').value;
    socket.emit('message', message);
    document.getElementById('message_input').value = '';
}

socket.on('message', function(message) {
    const ul = document.getElementById('messages');
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(message));
    ul.appendChild(li);
});

