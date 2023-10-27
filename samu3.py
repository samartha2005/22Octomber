'''3.Develop a Flask app that uses URL parameters to display dynamic content.'''
# Code

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/s')
def index():
    return "Welcome to the Flask URL Parameter Example!"

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")


# output
#https://purple-translator-yxoxb.pwskills.app:5000/greet?name=SAMARTHA%20MARUTI%20GAIKWAD