'''10.Design a Flask app with proper error handling for 404 and 500 errors.'''


# Code
from flask import Flask, render_template

app = Flask(__name__)

# Define a custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define a custom 500 error handler
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Route for a sample page that generates a 500 error
@app.route('/generate_error')
def generate_error():
    1 / 0  # This will raise a ZeroDivisionError

# Default route
@app.route('/')
def index():
    return "Welcome to the Flask Error Handling Example!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# output

# https://purple-translator-yxoxb.pwskills.app:5000/404