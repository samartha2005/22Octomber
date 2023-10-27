'''7.Integrate a SQLite database with Flask to perform CRUD operations on a list of items.'''


# Code
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # SQLite database
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/data')
def index():
    items = Item.query.all()
    return render_template('index3.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")


