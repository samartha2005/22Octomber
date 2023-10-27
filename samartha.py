      # Basics of Flask:
'''1.Create a Flask app that displays "Hello, World!" on the homepage.'''

# Code
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1><b><i>Hello, World!</i></b></h1>"
if __name__=="__main__":
    app.run(host="0.0.0.0")

# output
# https://purple-translator-yxoxb.pwskills.app:5000
