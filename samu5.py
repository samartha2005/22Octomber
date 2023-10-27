'''5.Implement user sessions in a Flask app to store and display user-specific data.'''

# Code
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure the app to use server-side sessions
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/abc')
def index():
    # Retrieve user-specific data from the session, or provide a default value
    user_data = session.get('user_data', 'Guest')
    return render_template('index1.html', user_data=user_data)

@app.route('/set_user_data', methods=['POST'])
def set_user_data():
    user_data = request.form['user_data']
    session['user_data'] = user_data
    return 'User data has been stored.'

if __name__ == '__main__':
    app.run(host="0.0.0.0")


# output
# https://purple-translator-yxoxb.pwskills.app:5000/abc