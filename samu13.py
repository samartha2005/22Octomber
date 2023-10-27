'''13.Implement notifications in a Flask app using websockets to notify users of updates.'''

# Code
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key
socketio = SocketIO(app)

@app.route('/def')
def index():
    return render_template('index7.html')

@socketio.on('notify')
def handle_notification(data):
    message = data.get('message', 'No message')
    socketio.emit('notification', {'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")



