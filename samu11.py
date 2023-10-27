'''11.Create a real-time chat application using Flask-SocketIO.'''


# Code
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index5.html')

@socketio.on('message')
def handle_message(message):
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0")
