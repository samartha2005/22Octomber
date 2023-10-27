'''4.Create a Flask app with a form that accepts user input and displays it.'''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/html')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    user_input = request.form['user_input']
    return render_template('result.html', user_input=user_input)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


#output
# https://purple-translator-yxoxb.pwskills.app:5000/html
