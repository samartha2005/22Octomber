'''12.Build a Flask app that updates data in real-time using WebSocket connections.'''


# Code
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index6.html')

@socketio.on('update_data')
def handle_update(data):
    socketio.emit('data_updated', data)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")


# output
# https://purple-translator-yxoxb.pwskills.app:5000